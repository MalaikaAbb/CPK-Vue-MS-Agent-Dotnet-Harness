<script setup lang="ts">
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
import WorkspaceContext from "./components/WorkspaceContext.vue";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit">
    <WorkspaceContext />
    <CopilotChat />
  </CopilotKitProvider>
</template>
