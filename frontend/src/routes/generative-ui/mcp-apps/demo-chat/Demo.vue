<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
const V0 = defineAsyncComponent(() => import("./default/App.vue"));
const V1 = defineAsyncComponent(() => import("./trusted/App.vue"));

const variants = [
  { id: "default", label: "src/App.vue", component: V0 },
  { id: "trusted", label: "Trusted widget configuration", component: V1 },
];
</script>

<template><VariantDemo parent-path="/generative-ui/mcp-apps" :variants="variants" /></template>
