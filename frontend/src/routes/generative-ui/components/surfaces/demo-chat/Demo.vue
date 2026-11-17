<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
const V0 = defineAsyncComponent(() => import("./HarnessApp.vue"));

const variants = [
  { id: "app", label: "Providers + FeaturedProducts (harness page)", component: V0 },
];
</script>

<template><VariantDemo parent-path="/generative-ui/components/surfaces" subtitle="featured surface · default" :variants="variants" /></template>
