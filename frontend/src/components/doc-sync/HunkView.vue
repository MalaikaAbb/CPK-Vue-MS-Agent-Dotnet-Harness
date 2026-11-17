<script setup lang="ts">
import type { Hunk } from "@/lib/doc-sync/types";

import SeverityBadge from "./SeverityBadge.vue";

/** Deliberately not Shiki-highlighted: +/- interleaved lines are not valid input to any grammar. */
defineProps<{ hunk: Hunk }>();

const LINE_STYLES = {
  add: "bg-emerald-50 text-emerald-900 dark:bg-emerald-950/50 dark:text-emerald-200",
  remove: "bg-rose-50 text-rose-900 dark:bg-rose-950/50 dark:text-rose-200",
  context: "text-slate-500 dark:text-slate-400",
} as const;
const GUTTER = { add: "+", remove: "−", context: " " } as const;
</script>

<template>
  <div class="rounded-lg border border-slate-200 dark:border-slate-800">
    <div class="flex flex-wrap items-center gap-x-3 gap-y-1 border-b border-slate-200 px-3 py-2 text-xs dark:border-slate-800">
      <SeverityBadge :severity="hunk.severity" />
      <span class="font-mono text-slate-500 dark:text-slate-400">line {{ hunk.startLine }}</span>
      <span v-if="hunk.heading" class="text-slate-600 dark:text-slate-400">under <span class="font-medium">{{ hunk.heading }}</span></span>
      <code v-if="hunk.language" class="rounded bg-slate-100 px-1.5 py-0.5 font-mono text-slate-700 dark:bg-slate-800 dark:text-slate-300">{{ hunk.language }}</code>
      <span v-if="hunk.truncated" class="text-amber-700 dark:text-amber-400">truncated</span>
    </div>
    <div class="overflow-x-auto">
      <pre class="min-w-full text-xs leading-relaxed"><div
        v-for="(line, i) in hunk.lines"
        :key="i"
        :class="['flex gap-2 px-3', LINE_STYLES[line.op]]"
      ><span aria-hidden="true" class="select-none opacity-60">{{ GUTTER[line.op] }}</span><span class="whitespace-pre-wrap break-words">{{ line.text || " " }}</span></div></pre>
    </div>
  </div>
</template>
