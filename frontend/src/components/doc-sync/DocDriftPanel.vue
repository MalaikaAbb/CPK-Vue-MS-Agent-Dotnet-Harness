<script setup lang="ts">
import { computed, onMounted } from "vue";
import { RouterLink } from "vue-router";

import Panel from "@/components/harness/Panel.vue";
import { docSyncState, docSyncUnavailable, loadDocSyncState } from "@/lib/doc-sync-state";

import DocSyncButton from "./DocSyncButton.vue";
import SeverityBadge from "./SeverityBadge.vue";

/** The doc-drift summary and its sync button, for the landing page. */
onMounted(() => loadDocSyncState());
const baseline = computed(() => docSyncState.value?.manifest.kind === "absent");
const tracked = computed(() => docSyncState.value?.tracked ?? 0);
const report = computed(() => docSyncState.value?.report ?? null);
</script>

<template>
  <Panel
    title="Doc drift"
    :description="`Re-fetch the markdown behind all ${tracked} tracked doc pages, diff against the stored snapshot, then replace it.`"
  >
    <template #actions><DocSyncButton v-if="!docSyncUnavailable" :baseline="baseline" /></template>
    <p v-if="docSyncUnavailable" class="text-sm text-slate-600 dark:text-slate-400">{{ docSyncUnavailable }}</p>
    <p v-else-if="baseline" class="text-sm text-slate-600 dark:text-slate-400">
      No snapshot yet. The first run stores {{ tracked }} pages; from the next one on, anything the docs change shows up here.
    </p>
    <div v-else class="flex flex-wrap items-center gap-x-3 gap-y-2 text-sm">
      <SeverityBadge :severity="report?.highest ?? 'none'" />
      <span class="text-slate-700 dark:text-slate-300">
        {{
          report?.aborted
            ? report.aborted.reason
            : report
              ? `${report.counts.changed} changed · ${report.counts.unchanged} unchanged · ${report.counts.missing} missing`
              : "Snapshot stored, no run recorded yet."
        }}
      </span>
      <RouterLink to="/doc-sync" class="text-[var(--accent)] underline underline-offset-4">Full report</RouterLink>
    </div>
  </Panel>
</template>
