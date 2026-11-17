<script setup lang="ts">
import { CopilotKitProvider } from "@copilotkit/vue/v2";
import HeadlessInterruptPanel from "./components/HeadlessInterruptPanel.vue";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit">
    <HeadlessInterruptPanel />
  </CopilotKitProvider>
</template>
