<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
const V0 = defineAsyncComponent(() => import("./default/App.vue"));
const V1 = defineAsyncComponent(() => import("./catch-all/App.vue"));
const V2 = defineAsyncComponent(() => import("./per-tool/App.vue"));

const variants = [
  { id: "default", label: "Zero-config · useDefaultRenderTool()", component: V0 },
  { id: "catch-all", label: "Custom catch-all · BrandedToolCard (stand-in)", component: V1 },
  { id: "per-tool", label: "Per-tool · get_weather + wildcard", component: V2 },
];
</script>

<template><VariantDemo parent-path="/generative-ui/tool-rendering" :variants="variants" /></template>
