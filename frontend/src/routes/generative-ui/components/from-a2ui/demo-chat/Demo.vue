<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
const V0 = defineAsyncComponent(() => import("./HarnessApp.vue"));

const variants = [
  { id: "after", label: "After · appUI provider", component: V0 },
];
</script>

<template><VariantDemo parent-path="/generative-ui/components/from-a2ui" subtitle="appUI (After) · default" :variants="variants" /></template>
