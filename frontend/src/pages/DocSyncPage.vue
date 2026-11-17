<script setup lang="ts">
import { computed, onMounted } from "vue";
import { RouterLink } from "vue-router";

import CheckMark from "@/components/doc-sync/CheckMark.vue";
import DocSyncButton from "@/components/doc-sync/DocSyncButton.vue";
import PageComparison from "@/components/doc-sync/PageComparison.vue";
import SeverityBadge from "@/components/doc-sync/SeverityBadge.vue";
import Callout from "@/components/harness/Callout.vue";
import KeyValue from "@/components/harness/KeyValue.vue";
import Panel from "@/components/harness/Panel.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import { docSyncState, docSyncUnavailable, loadDocSyncState } from "@/lib/doc-sync-state";
import { normalizeDocPath } from "@/lib/doc-sync/paths";
import type { PageReport } from "@/lib/doc-sync/types";
import { NAV, docUrl } from "@/lib/nav-config";

/**
 * The full drift report, ported from the React harness. Every tracked section
 * is listed, matched or not, and each row expands to the comparison behind it.
 */
onMounted(() => loadDocSyncState());

const manifestState = computed(() => docSyncState.value?.manifest);
const manifest = computed(() => (manifestState.value?.kind === "ok" ? manifestState.value.manifest : null));
const baseline = computed(() => manifestState.value?.kind === "absent");
const report = computed(() => docSyncState.value?.report ?? null);
const byDocPath = computed(
  () => new Map<string, PageReport>((report.value?.pages ?? []).map((p) => [p.docPath, p])),
);
const groups = NAV.filter((g) => g.title !== "Harness");

const OUTCOME_TEXT: Record<string, string> = {
  unchanged: "unchanged",
  changed: "changed",
  new: "stored",
  missing: "404 upstream",
  unstable: "unstable",
  error: "error",
};
function summarize(counts: Record<string, number>): string {
  const parts = Object.entries(counts)
    .filter(([, n]) => n > 0)
    .map(([k, n]) => `${n} ${OUTCOME_TEXT[k] ?? k}`);
  return parts.length > 0 ? parts.join(" · ") : "nothing checked";
}
const formatStamp = (iso: string) => iso.replace("T", " ").replace(/\.\d+Z$/, " UTC");
</script>

<template>
  <RouteHeader path="/doc-sync" />

  <Callout v-if="docSyncUnavailable" tone="warn" title="Dev server only">{{ docSyncUnavailable }}</Callout>

  <Panel
    title="Snapshot"
    description="Fetches the markdown source behind every doc page this repo tracks, diffs it against the stored copy, then replaces that copy."
  >
    <template #actions><DocSyncButton v-if="docSyncState" :baseline="baseline" /></template>
    <KeyValue
      :rows="[
        ['Last synced', manifest ? formatStamp(manifest.syncedAt) : 'never — no snapshot yet'],
        ['Doc pages tracked', `${docSyncState?.tracked ?? '—'}`],
        ['Last run', report ? `${report.durationMs}ms · ${report.pages.length} checked` : '—'],
        ['Result', report?.aborted ? 'aborted — snapshot untouched' : report ? summarize(report.counts) : '—'],
      ]"
    >
      <template v-if="report && !report.aborted" #Result>
        <span class="inline-flex items-center gap-2"><SeverityBadge :severity="report.highest" />{{ summarize(report.counts) }}</span>
      </template>
    </KeyValue>
  </Panel>

  <Callout tone="warn" title="Blind spot: the .md export is not the rendered page">
    <p>
      The MS Agent Framework root page renders as a landing page whose only code (the runtime route) is not in its <code>.md</code>, and the
      agent (<code>Program.cs</code>) lives on the non-Vue MS Agent Framework Quickstart, which this sync does not track. This sync diffs the Vue
      pages' <code>.md</code> only, so changes to either are invisible here; <code>npm run doc-files</code> re-reads both live (README §9).
    </p>
  </Callout>

  <Callout v-if="manifestState?.kind === 'error'" tone="warn" title="The manifest could not be read">
    <p>{{ manifestState.error }}</p>
    <p>Delete <code>doc-snapshot/manifest.json</code> and re-run to rebuild the baseline.</p>
  </Callout>
  <Callout v-if="baseline" tone="info" title="No snapshot recorded yet">
    <p>The first run stores {{ docSyncState?.tracked }} pages and has nothing to compare them against.</p>
  </Callout>
  <Callout v-if="report?.aborted" tone="warn" title="Run aborted — snapshot left untouched">
    <p>{{ report.aborted.reason }}</p>
    <p>The sync commits all pages or none.</p>
  </Callout>
  <Callout v-if="report && !report.aborted && report.highest === 'high'" tone="warn" title="A change landed inside a code block">
    <p>An implementation here may no longer match what its doc page teaches. Expand the flagged sections below, reconcile the affected routes, and re-run the sync.</p>
  </Callout>

  <Panel title="Sections checked" description="Every doc page this repo tracks, in nav order. Expand a row to compare the stored copy against the one just fetched.">
    <div class="space-y-6">
      <div v-for="group in groups" :key="group.title">
        <h3 class="text-xs font-semibold uppercase tracking-wide text-slate-500 dark:text-slate-400">{{ group.title }}</h3>
        <div class="mt-2 divide-y divide-slate-200 rounded-lg border border-slate-200 dark:divide-slate-800 dark:border-slate-800">
          <details v-for="route in group.routes" :key="route.path" class="group">
            <summary class="flex cursor-pointer list-none flex-wrap items-center gap-x-3 gap-y-1 px-3 py-2 text-sm hover:bg-slate-50 dark:hover:bg-slate-800/60">
              <span aria-hidden="true" class="w-3 shrink-0 select-none font-mono text-xs text-slate-400 transition-transform group-open:rotate-90 dark:text-slate-500">▸</span>
              <CheckMark :outcome="byDocPath.get(normalizeDocPath(route.docPath))?.outcome" />
              <span class="font-medium text-slate-900 dark:text-slate-100">{{ route.title }}</span>
              <code class="font-mono text-xs text-slate-500 dark:text-slate-400">{{ route.path }}</code>
              <SeverityBadge
                v-if="(byDocPath.get(normalizeDocPath(route.docPath))?.severity ?? 'none') !== 'none'"
                :severity="byDocPath.get(normalizeDocPath(route.docPath))!.severity"
              />
              <span class="ml-auto text-xs text-slate-500 dark:text-slate-400">
                {{ OUTCOME_TEXT[byDocPath.get(normalizeDocPath(route.docPath))?.outcome ?? ""] ?? "not checked" }}
              </span>
            </summary>
            <div class="border-t border-slate-200 bg-slate-50 px-3 py-3 dark:border-slate-800 dark:bg-slate-900/60">
              <div class="mb-3 flex flex-wrap items-center gap-x-3 gap-y-1 text-xs">
                <a :href="docUrl(route)" target="_blank" rel="noreferrer" class="text-[var(--accent)] underline underline-offset-4">doc page ↗</a>
                <RouterLink :to="route.path" class="text-[var(--accent)] underline underline-offset-4">open route</RouterLink>
                <code class="font-mono text-slate-500 dark:text-slate-400">{{ normalizeDocPath(route.docPath) }}</code>
              </div>
              <PageComparison :page="byDocPath.get(normalizeDocPath(route.docPath))" />
            </div>
          </details>
        </div>
      </div>
    </div>
  </Panel>

  <Panel
    v-if="report && (report.sitemap.newUnmapped.length > 0 || report.sitemap.confirmedRemoved.length > 0)"
    title="Nav drift"
    description="Compared against the site's sitemap, which is the only way to notice pages that were added or removed rather than edited."
  >
    <div v-if="report.sitemap.confirmedRemoved.length > 0" class="mb-4">
      <h3 class="text-xs font-semibold uppercase tracking-wide text-rose-700 dark:text-rose-400">Removed upstream</h3>
      <ul class="mt-2 space-y-1"><li v-for="url in report.sitemap.confirmedRemoved" :key="url" class="font-mono text-xs text-slate-600 dark:text-slate-400">{{ url }}</li></ul>
    </div>
    <div v-if="report.sitemap.newUnmapped.length > 0">
      <h3 class="text-xs font-semibold uppercase tracking-wide text-slate-500 dark:text-slate-400">New upstream, no route here ({{ report.sitemap.newUnmapped.length }})</h3>
      <p class="mt-1 text-sm text-slate-600 dark:text-slate-400">Listed once, then folded into the manifest's <code>knownUnmapped</code> so they stop being reported.</p>
      <ul class="mt-2 space-y-1"><li v-for="url in report.sitemap.newUnmapped" :key="url" class="font-mono text-xs text-slate-600 dark:text-slate-400">{{ url }}</li></ul>
    </div>
  </Panel>
</template>
