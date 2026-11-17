<script setup lang="ts">
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
import GovernedActionApproval from "./components/GovernedActionApproval.vue";
import GovernedActionTool from "./components/GovernedActionTool.vue";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit">
    <GovernedActionApproval />
    <GovernedActionTool />
    <CopilotChat />
  </CopilotKitProvider>
</template>
