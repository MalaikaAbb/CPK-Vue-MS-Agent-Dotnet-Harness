<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
const V0 = defineAsyncComponent(() => import("./tool/HarnessApp.vue"));
const V1 = defineAsyncComponent(() => import("./markdown/HarnessApp.vue"));
const V2 = defineAsyncComponent(() => import("./agent-ids/HarnessApp.vue"));

const variants = [
  { id: "tool", label: "render_ui tool (default)", component: V0 },
  { id: "markdown", label: "transport: 'markdown'", component: V1 },
  { id: "agent-ids", label: "agentIds: ['shop']", component: V2 },
];
</script>

<template><VariantDemo parent-path="/generative-ui/components/transports" :variants="variants" /></template>
