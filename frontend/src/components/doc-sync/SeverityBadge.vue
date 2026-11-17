<script setup lang="ts">
import type { Severity } from "@/lib/doc-sync/types";

defineProps<{ severity: Severity }>();

const SEVERITY_STYLES: Record<Severity, string> = {
  high: "border-rose-300 bg-rose-50 text-rose-800 dark:border-rose-800 dark:bg-rose-950/60 dark:text-rose-200",
  medium: "border-amber-300 bg-amber-50 text-amber-800 dark:border-amber-800 dark:bg-amber-950/60 dark:text-amber-200",
  low: "border-violet-300 bg-violet-50 text-violet-800 dark:border-violet-800 dark:bg-violet-950/60 dark:text-violet-200",
  none: "border-slate-300 bg-white text-slate-500 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-400",
};
const SEVERITY_LABEL: Record<Severity, string> = { high: "High", medium: "Medium", low: "Low", none: "None" };
</script>

<template>
  <span :class="['inline-flex shrink-0 items-center rounded-full border px-2.5 py-0.5 text-xs font-medium', SEVERITY_STYLES[severity]]">
    {{ SEVERITY_LABEL[severity] }}
  </span>
</template>
