<script setup lang="ts">
import { computed, type Component } from "vue";
import { useRoute, useRouter } from "vue-router";

import DemoFrame from "./DemoFrame.vue";

/**
 * [harness] A `/demo-chat` route with one or more published samples.
 *
 * Each variant is a doc file (or flagged harness wrapper) mounted as-is. The
 * active one is keyed, so switching samples unmounts the previous one — and
 * with it the doc's own CopilotKitProvider — instead of leaking its agent
 * state into the next sample. The choice lives in `?v=` so links are stable.
 */
const props = defineProps<{
  parentPath: string;
  subtitle?: string;
  variants: { id: string; label: string; component: Component }[];
}>();

const route = useRoute();
const router = useRouter();
const activeId = computed({
  get: () => {
    const v = route.query.v;
    return typeof v === "string" && props.variants.some((x) => x.id === v) ? v : props.variants[0]!.id;
  },
  set: (id: string) => void router.replace({ query: { ...route.query, v: id } }),
});
const active = computed(() => props.variants.find((v) => v.id === activeId.value)!);
</script>

<template>
  <DemoFrame
    v-model="activeId"
    :parent-path="parentPath"
    :subtitle="subtitle ?? active.label"
    :variants="variants.length > 1 ? variants.map(({ id, label }) => ({ id, label })) : undefined"
  >
    <component :is="active.component" :key="active.id" />
  </DemoFrame>
</template>
