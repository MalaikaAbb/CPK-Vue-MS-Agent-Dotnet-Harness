<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
const V0 = defineAsyncComponent(() => import("./minimal/App.vue"));
const V1 = defineAsyncComponent(() => import("./complete/HarnessComplete.vue"));

const variants = [
  { id: "minimal", label: "Minimal · HeadlessChat.vue", component: V0 },
  { id: "complete", label: "Complete · RenderedMessages.vue", component: V1 },
];
</script>

<template><VariantDemo parent-path="/custom-look-and-feel/headless-ui" :variants="variants" /></template>
