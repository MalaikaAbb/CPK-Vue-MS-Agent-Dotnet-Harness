<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
const V0 = defineAsyncComponent(() => import("./HarnessApp.vue"));
const V1 = defineAsyncComponent(() => import("./no-context/HarnessApp.vue"));

const variants = [
  { id: "app", label: "src/App.vue (harness chat in its slot)", component: V0 },
  { id: "no-context", label: "sendContext: false", component: V1 },
];
</script>

<template><VariantDemo parent-path="/generative-ui/components/markdown-mode" :variants="variants" /></template>
