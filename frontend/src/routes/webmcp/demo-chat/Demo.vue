<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
const V0 = defineAsyncComponent(() => import("./HarnessUseFrontendToolStandIn.vue"));

const variants = [
  { id: "use-frontend-tool-standin", label: "OrderSearch.vue + searchOrders stand-in", component: V0 },
];
</script>

<template><VariantDemo parent-path="/webmcp" subtitle="OrderSearch.vue + searchOrders stand-in" :variants="variants" /></template>
