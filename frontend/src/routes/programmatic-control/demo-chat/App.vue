<script setup lang="ts">
import { CopilotKitProvider } from "@copilotkit/vue/v2";
import AgentTrigger from "./components/AgentTrigger.vue";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit">
    <AgentTrigger />
  </CopilotKitProvider>
</template>
