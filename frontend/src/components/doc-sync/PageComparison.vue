<script setup lang="ts">
import type { PageReport } from "@/lib/doc-sync/types";

import HunkView from "./HunkView.vue";

/**
 * What expanding a section row shows: the stored copy vs the one just pulled.
 * An unchanged page shows the matching hashes — the evidence the check ran.
 */
defineProps<{ page?: PageReport }>();
const short = (hash?: string) => (hash ? hash.slice(0, 12) : "—");
</script>

<template>
  <p v-if="!page" class="text-sm text-slate-600 dark:text-slate-400">This doc page was not part of the last run.</p>
  <div v-else class="space-y-3">
    <p v-if="page.error" class="text-sm text-amber-700 dark:text-amber-400">{{ page.error }}</p>
    <p v-if="page.outcome === 'unchanged'" class="text-sm text-slate-600 dark:text-slate-400">
      Identical — the page fetched just now hashes the same as the stored copy, so nothing on this route needs re-checking.
    </p>
    <p v-if="page.outcome === 'new'" class="text-sm text-slate-600 dark:text-slate-400">
      Stored for the first time. There was no earlier copy to compare against, so differences start showing from the next sync.
    </p>
    <p v-if="page.outcome === 'missing'" class="text-sm text-rose-700 dark:text-rose-400">
      The page returned 404. The previously stored copy has been kept, so you can still read what it used to say.
    </p>
    <p v-if="page.outcome === 'unstable'" class="text-sm text-amber-700 dark:text-amber-400">
      Two reads seconds apart returned different content — a deploy probably landed mid-run. This page was left out of the snapshot; sync again.
    </p>
    <p v-if="page.snapshotEdited" class="text-sm text-amber-700 dark:text-amber-400">
      The stored copy had been changed locally — it no longer matched the hash recorded for it. This diff therefore starts from your edited copy.
    </p>
    <p v-if="page.rewritten" class="text-sm text-rose-700 dark:text-rose-400">Rewritten past the diff cap — read the page itself rather than the hunks below.</p>
    <p v-if="page.fenceCountChanged" class="text-sm text-rose-700 dark:text-rose-400">
      The number of fenced code blocks changed — treated as high regardless of what the line diff found.
    </p>
    <p v-if="page.fenceParseWarning" class="text-sm text-amber-700 dark:text-amber-400">
      A code fence was left unclosed at end of file, so the severities below are less reliable than usual.
    </p>

    <dl class="grid grid-cols-[minmax(0,9rem)_1fr] gap-x-4 gap-y-1 text-xs">
      <template v-for="[k, v] in ([
        ['Existing snapshot', short(page.previousSha256)],
        ['Newly fetched', short(page.sha256)],
        ['Size', page.bytes ? `${page.bytes} bytes · ${page.lines} lines` : '—'],
      ] as [string, string][])" :key="k">
        <dt class="text-slate-500 dark:text-slate-400">{{ k }}</dt>
        <dd class="font-mono break-all text-slate-700 dark:text-slate-300">{{ v }}</dd>
      </template>
    </dl>

    <template v-if="page.hunks.length > 0">
      <p class="text-xs text-slate-500 dark:text-slate-400">
        <span class="font-mono text-rose-700 dark:text-rose-400">−</span> existing snapshot
        &nbsp;&nbsp;<span class="font-mono text-emerald-700 dark:text-emerald-400">+</span> newly fetched
      </p>
      <div class="space-y-3"><HunkView v-for="(hunk, i) in page.hunks" :key="i" :hunk="hunk" /></div>
    </template>
    <p v-if="page.droppedHunks" class="text-xs text-slate-500 dark:text-slate-400">{{ page.droppedHunks }} further hunk(s) not shown.</p>
  </div>
</template>
