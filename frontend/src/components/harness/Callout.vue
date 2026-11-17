<script setup lang="ts">
withDefaults(defineProps<{ tone?: "info" | "warn" | "premium" | "success" | "harness"; title?: string }>(), {
  tone: "info",
});

const tones = {
  info: "border-green-300 bg-green-50 text-green-950 dark:border-green-900 dark:bg-green-950/40 dark:text-green-100",
  warn: "border-amber-300 bg-amber-50 text-amber-950 dark:border-amber-900 dark:bg-amber-950/40 dark:text-amber-100",
  premium:
    "border-violet-300 bg-violet-50 text-violet-950 dark:border-violet-900 dark:bg-violet-950/40 dark:text-violet-100",
  success:
    "border-emerald-300 bg-emerald-50 text-emerald-950 dark:border-emerald-900 dark:bg-emerald-950/40 dark:text-emerald-100",
  // Everything the harness added or substituted that the doc page does not publish.
  harness:
    "border-fuchsia-400 bg-fuchsia-50 text-fuchsia-950 dark:border-fuchsia-800 dark:bg-fuchsia-950/40 dark:text-fuchsia-100",
} as const;
</script>

<template>
  <div :class="['rounded-lg border px-4 py-3 text-sm', tones[tone]]">
    <p v-if="title" class="font-semibold">
      <span v-if="tone === 'harness'" class="mr-1 rounded bg-fuchsia-600 px-1.5 py-0.5 text-[10px] font-bold uppercase tracking-wide text-white">Harness</span>
      {{ title }}
    </p>
    <div :class="title ? 'mt-1 space-y-2' : 'space-y-2'"><slot /></div>
  </div>
</template>
