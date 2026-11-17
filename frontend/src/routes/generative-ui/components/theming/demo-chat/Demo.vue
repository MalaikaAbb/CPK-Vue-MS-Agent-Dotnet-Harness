<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
const V0 = defineAsyncComponent(() => import("./HarnessApp.vue"));

const variants = [
  { id: "app", label: "Theme provider (harness chat)", component: V0 },
];
</script>

<template><VariantDemo parent-path="/generative-ui/components/theming" subtitle="themed standardUI · default" :variants="variants" /></template>
