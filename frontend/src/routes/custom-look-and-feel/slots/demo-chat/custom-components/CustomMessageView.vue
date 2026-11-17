<script setup lang="ts">
/**
 * [harness] STAND-IN — NOT FROM THE DOCS.
 *
 * The Slots page renders `<CustomMessageView :messages :is-running />` under
 * “Custom Components” but never defines it. This is the minimum that makes
 * that sample mount: it receives exactly the two props the page passes and
 * renders each message's role and text.
 */
import StandInBadge from "@/components/harness/StandInBadge.vue";

defineProps<{
  messages: { id: string; role: string; content?: unknown }[];
  isRunning: boolean;
}>();
</script>

<template>
  <section class="flex flex-col gap-2 p-4">
    <StandInBadge name="CustomMessageView" />
    <article v-for="m in messages" :key="m.id" class="rounded border border-slate-200 px-3 py-2 text-sm dark:border-slate-700">
      <strong>{{ m.role }}:</strong> {{ typeof m.content === "string" ? m.content : JSON.stringify(m.content) }}
    </article>
    <p v-if="isRunning" class="text-xs text-slate-500">running…</p>
  </section>
</template>
