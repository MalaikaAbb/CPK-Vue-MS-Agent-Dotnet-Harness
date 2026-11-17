import type { Plugin } from "vite";

import { docTargets } from "../src/lib/doc-sync/paths";
import { readLatestReport, readManifest } from "./doc-sync/store";
import { runDocSync } from "./doc-sync/run";

/**
 * [harness] The server half of /doc-sync.
 *
 * The React harness ran the sync as a Next Server Action and read the snapshot
 * in server components. A Vite app has no server of its own, so the same code
 * runs as dev-server middleware instead:
 *
 *   GET  /__harness/doc-sync/state  → manifest state + latest report
 *   POST /__harness/doc-sync/run    → runs the sync, returns its SyncResult
 *
 * Dev-only by construction (`configureServer` never runs in `vite build`), so
 * an unauthenticated endpoint that does outbound fetches and disk writes can
 * never ship. The built app shows the panels with "dev server only".
 */
export function harnessDocSync(): Plugin {
  return {
    name: "harness-doc-sync",
    configureServer(server) {
      server.middlewares.use("/__harness/doc-sync", async (req, res) => {
        const send = (status: number, body: unknown) => {
          res.statusCode = status;
          res.setHeader("content-type", "application/json");
          res.setHeader("cache-control", "no-store");
          res.end(JSON.stringify(body));
        };

        try {
          if (req.method === "GET" && (req.url === "/state" || req.url?.startsWith("/state?"))) {
            const [manifest, report] = await Promise.all([readManifest(), readLatestReport()]);
            return send(200, { manifest, report, tracked: docTargets().length });
          }
          if (req.method === "POST" && req.url === "/run") {
            return send(200, await runDocSync());
          }
          return send(404, { error: `No harness endpoint ${req.method} ${req.url}` });
        } catch (error) {
          return send(500, { error: error instanceof Error ? error.message : String(error) });
        }
      });
    },
  };
}
