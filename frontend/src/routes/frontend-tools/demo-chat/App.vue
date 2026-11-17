<script setup lang="ts">
import { CopilotKitProvider } from "@copilotkit/vue/v2";
import DashboardAgent from "./components/DashboardAgent.vue";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit">
    <DashboardAgent />
  </CopilotKitProvider>
</template>
