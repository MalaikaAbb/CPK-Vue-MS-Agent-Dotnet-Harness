<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
import { withHarnessProvider } from "@/lib/harness-mount";
const V0 = defineAsyncComponent(() => import("./basic/App.vue"));
const V1 = defineAsyncComponent(() => import("./toolbar/App.vue"));
const V2 = defineAsyncComponent(() => import("./controlled/components/ControlledChat.vue"));
const V3 = defineAsyncComponent(() => import("./css-parts/HarnessCssParts.vue"));
const V4 = defineAsyncComponent(() => import("./header-slot/HeaderSlot.vue"));
const V5 = defineAsyncComponent(() => import("./row-slot/RowSlot.vue"));

const variants = [
  { id: "basic", label: "Set up · src/App.vue", component: V0 },
  { id: "toolbar", label: "Own button · App.vue with a toolbar button", component: V1 },
  { id: "controlled", label: "Controlled · ControlledChat.vue", component: withHarnessProvider(V2, "/api/copilotkit-threads") },
  { id: "css-parts", label: "Own button only · CSS parts", component: V3 },
  { id: "header-slot", label: "Customization · header slot", component: withHarnessProvider(V4, "/api/copilotkit-threads") },
  { id: "row-slot", label: "Customization · #row slot", component: withHarnessProvider(V5, "/api/copilotkit-threads") },
];
</script>

<template><VariantDemo parent-path="/prebuilt-components/copilot-threads-drawer" :variants="variants" /></template>
