<script setup lang="ts">
// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page.
import { defineAsyncComponent } from "vue";

import VariantDemo from "@/components/harness/VariantDemo.vue";
const V0 = defineAsyncComponent(() => import("./HarnessApp.vue"));

const variants = [
  { id: "app", label: "MeetingApproval.vue + harness chat", component: V0 },
];
</script>

<template><VariantDemo parent-path="/human-in-the-loop" subtitle="schedule_meeting · default" :variants="variants" /></template>
