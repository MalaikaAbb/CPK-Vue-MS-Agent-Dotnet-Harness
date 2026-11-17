<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
const V0 = defineAsyncComponent(() => import("./App.vue"));

const variants = [
  { id: "app", label: "App.vue", component: V0 },
];
</script>

<template><VariantDemo parent-path="/prebuilt-components" subtitle="CopilotChat · my-agent" :variants="variants" /></template>
