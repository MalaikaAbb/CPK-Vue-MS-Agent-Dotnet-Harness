<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
const V0 = defineAsyncComponent(() => import("./HarnessApp.vue"));
const V1 = defineAsyncComponent(() => import("./override/HarnessOverride.vue"));

const variants = [
  { id: "standard", label: "standardUI provider (harness chat)", component: V0 },
  { id: "override", label: "Card → MyCard override (harness provider)", component: V1 },
];
</script>

<template><VariantDemo parent-path="/generative-ui/components/standard-catalog" :variants="variants" /></template>
