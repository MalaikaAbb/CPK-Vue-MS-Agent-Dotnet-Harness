<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
import { withHarnessProvider } from "@/lib/harness-mount";
const V0 = defineAsyncComponent(() => import("./welcome-screen/SupportChat.vue"));
const V1 = defineAsyncComponent(() => import("./assistant-message/SupportChat.vue"));
const V2 = defineAsyncComponent(() => import("./disclaimer/Disclaimer.vue"));
const V3 = defineAsyncComponent(() => import("./tailwind/TailwindClasses.vue"));
const V4 = defineAsyncComponent(() => import("./props-override/PropsOverride.vue"));
const V5 = defineAsyncComponent(() => import("./custom-components/CustomComponents.vue"));
const V6 = defineAsyncComponent(() => import("./two-levels/TwoLevels.vue"));
const V7 = defineAsyncComponent(() => import("./three-levels/ThreeLevels.vue"));
const V8 = defineAsyncComponent(() => import("./labels/Labels.vue"));

const variants = [
  { id: "welcome-screen", label: "Welcome screen slot · SupportChat.vue", component: withHarnessProvider(V0) },
  { id: "assistant-message", label: "Assistant message slot · SupportChat.vue", component: withHarnessProvider(V1) },
  { id: "disclaimer", label: "Disclaimer slot", component: withHarnessProvider(V2) },
  { id: "tailwind", label: "Tailwind classes", component: withHarnessProvider(V3) },
  { id: "props-override", label: "Props override", component: withHarnessProvider(V4) },
  { id: "custom-components", label: "Custom components (stand-in)", component: withHarnessProvider(V5) },
  { id: "two-levels", label: "Nested · two levels (stand-in)", component: withHarnessProvider(V6) },
  { id: "three-levels", label: "Nested · three levels", component: withHarnessProvider(V7) },
  { id: "labels", label: "Labels", component: withHarnessProvider(V8) },
];
</script>

<template><VariantDemo parent-path="/custom-look-and-feel/slots" :variants="variants" /></template>
