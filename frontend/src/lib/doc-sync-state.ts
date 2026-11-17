import { ref } from "vue";

import type { DocSyncReport, Manifest, SyncResult } from "./doc-sync/types";

/**
 * [harness] Client side of /doc-sync.
 *
 * The React harness read the manifest and latest report in server components
 * and re-rendered with `refresh()` after the Server Action. Here the Vite
 * dev-server plugin (harness/vite-plugin.ts) serves the same two reads, and
 * every panel shares this one reactive copy, refreshed after a run — so the
 * button's message and the panels below it never disagree.
 */
export type ManifestState =
  | { kind: "absent" }
  | { kind: "ok"; manifest: Manifest }
  | { kind: "error"; error: string };

export interface DocSyncState {
  manifest: ManifestState;
  report: DocSyncReport | null;
  tracked: number;
}

export const docSyncState = ref<DocSyncState | null>(null);
/** Set when the endpoint is unreachable — i.e. a `vite build` preview, not the dev server. */
export const docSyncUnavailable = ref<string | null>(null);

let loading: Promise<void> | null = null;

export function loadDocSyncState(force = false): Promise<void> {
  if (loading && !force) return loading;
  loading = fetch("/__harness/doc-sync/state", { cache: "no-store" })
    .then(async (res) => {
      if (!res.ok || !(res.headers.get("content-type") ?? "").includes("json")) {
        throw new Error(`HTTP ${res.status}`);
      }
      docSyncState.value = (await res.json()) as DocSyncState;
      docSyncUnavailable.value = null;
    })
    .catch((error: unknown) => {
      docSyncUnavailable.value = `Doc sync runs in the Vite dev server only (${error instanceof Error ? error.message : String(error)}).`;
    });
  return loading;
}

export async function runDocSync(): Promise<SyncResult> {
  try {
    const res = await fetch("/__harness/doc-sync/run", { method: "POST" });
    const result = (await res.json()) as SyncResult;
    await loadDocSyncState(true);
    return result;
  } catch (error) {
    return {
      ok: false,
      baseline: false,
      message: `Doc sync endpoint unreachable: ${error instanceof Error ? error.message : String(error)}`,
      changed: 0,
      highest: "none",
    };
  }
}
