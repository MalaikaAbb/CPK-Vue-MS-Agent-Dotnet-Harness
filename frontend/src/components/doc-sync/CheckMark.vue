<script setup lang="ts">
import { computed } from "vue";

import type { PageOutcome } from "@/lib/doc-sync/types";

/**
 * The per-section check mark. `outcome` is undefined for a route whose doc page
 * was not part of the last run — a neutral dot, because "not checked" and
 * "checked and fine" must never look alike.
 */
const props = defineProps<{ outcome?: PageOutcome }>();

const OUTCOME_LABEL: Record<PageOutcome, string> = {
  unchanged: "Unchanged",
  changed: "Changed",
  new: "New",
  missing: "404 upstream",
  unstable: "Unstable",
  error: "Error",
};
const OUTCOME_MARK: Record<PageOutcome, { glyph: string; className: string }> = {
  unchanged: { glyph: "✓", className: "text-emerald-600 dark:text-emerald-400" },
  changed: { glyph: "!", className: "text-amber-600 dark:text-amber-400" },
  new: { glyph: "+", className: "text-teal-600 dark:text-teal-400" },
  missing: { glyph: "✗", className: "text-rose-600 dark:text-rose-400" },
  unstable: { glyph: "~", className: "text-amber-600 dark:text-amber-400" },
  error: { glyph: "✗", className: "text-rose-600 dark:text-rose-400" },
};
const mark = computed(() =>
  props.outcome ? OUTCOME_MARK[props.outcome] : { glyph: "·", className: "text-slate-400 dark:text-slate-600" },
);
const label = computed(() => (props.outcome ? OUTCOME_LABEL[props.outcome] : "Not checked"));
</script>

<template>
  <span :aria-label="label" :title="label" :class="['inline-flex w-4 shrink-0 justify-center font-mono text-sm font-semibold', mark.className]">
    {{ mark.glyph }}
  </span>
</template>
