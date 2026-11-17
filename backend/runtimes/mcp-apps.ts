import { CopilotRuntime } from "@copilotkit/runtime/v2";

import { myAgent } from "../agents";

/**
 * The runtime behind /generative-ui/mcp-apps, mounted at
 * /api/copilotkit-mcp-apps.
 *
 * The block between the markers is MCP Apps' server.ts, verbatim apart from
 * one line. Everything outside the markers is [harness]:
 *
 * - `agent` is used by the page but never defined; it is the landing page's my_agent.
 * - The published `url` is a placeholder (`https://mcp.example.com/mcp`) that
 *   does not resolve. It is replaced by the page's own HTTP transport example,
 *   `http://localhost:3101/mcp`, where `npm run mcp:apps` starts the official
 *   ext-apps reference server. Override with MCP_APPS_URL. The published line
 *   is kept as a comment beside it.
 * - It is a separate runtime because `mcpApps` applies to every agent on a
 *   runtime; keeping it off /api/copilotkit means an MCP server that is down
 *   cannot affect any other route. Same precedent as the React harness.
 */
const agent = myAgent(); // [harness] see above

export function createMcpAppsRuntime(): CopilotRuntime {
  // ── BEGIN MCP Apps · server.ts (verbatim except the url line) ─────────────
  const runtime = new CopilotRuntime({
    agents: { default: agent },
    mcpApps: {
      servers: [
        {
          type: "http",
          // url: "https://mcp.example.com/mcp",   ← as published (placeholder)
          url: process.env.MCP_APPS_URL ?? "http://localhost:3101/mcp", // [harness]
          serverId: "support-tools",
        },
      ],
    },
  });
  // ── END MCP Apps · server.ts ──────────────────────────────────────────────
  return runtime;
}
