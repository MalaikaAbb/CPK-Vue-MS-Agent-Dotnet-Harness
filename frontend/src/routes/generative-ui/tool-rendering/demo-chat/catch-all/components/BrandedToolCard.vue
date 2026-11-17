<script setup lang="ts">
/**
 * [harness] STAND-IN — NOT FROM THE DOCS.
 *
 * Tool Rendering's “Custom catch-all” passes `render: BrandedToolCard` to
 * useDefaultRenderTool but never defines it. Minimal card: the tool name, its
 * live status and, once complete, the raw result.
 */
import StandInBadge from "@/components/harness/StandInBadge.vue";

defineProps<{ name: string; status: string; result?: string }>();
</script>

<template>
  <article class="my-2 rounded-lg border border-slate-300 p-3 text-sm dark:border-slate-700">
    <StandInBadge name="BrandedToolCard" />
    <p class="mt-1"><strong>{{ name }}</strong> · {{ status }}</p>
    <pre v-if="status === 'complete'" class="mt-1 whitespace-pre-wrap text-xs">{{ result }}</pre>
  </article>
</template>
