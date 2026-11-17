<script setup lang="ts">
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
import SharedWorkspace from "./components/SharedWorkspace.vue";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit">
    <SharedWorkspace />
    <CopilotChat agent-id="workspace" />
  </CopilotKitProvider>
</template>
