<script setup lang="ts">
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
import ResearchProgress from "./components/ResearchProgress.vue";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit">
    <ResearchProgress />
    <CopilotChat agent-id="researcher" />
  </CopilotKitProvider>
</template>
