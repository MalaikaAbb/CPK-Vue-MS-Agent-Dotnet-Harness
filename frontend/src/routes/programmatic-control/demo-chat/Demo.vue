<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
const V0 = defineAsyncComponent(() => import("./HarnessWithChat.vue"));
const V1 = defineAsyncComponent(() => import("./App.vue"));

const variants = [
  { id: "with-chat", label: "AgentTrigger + CopilotChat (harness)", component: V0 },
  { id: "app", label: "src/App.vue (verbatim, no chat)", component: V1 },
];
</script>

<template><VariantDemo parent-path="/programmatic-control" :variants="variants" /></template>
