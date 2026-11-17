<script setup lang="ts">
/** [harness] Visible on screen wherever a stand-in for an unpublished component renders. */
defineProps<{ name: string }>();
</script>

<template>
  <span
    class="inline-flex items-center gap-1 rounded border border-dashed border-fuchsia-500 bg-fuchsia-50 px-1.5 py-0.5 font-mono text-[10px] font-bold uppercase tracking-wide text-fuchsia-700 dark:bg-fuchsia-950/60 dark:text-fuchsia-200"
    :title="`${name} is never published by the doc page — this is a minimal harness stand-in.`"
  >
    Harness stand-in · {{ name }}
  </span>
</template>
