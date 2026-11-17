<script setup lang="ts">
import { CopilotKitProvider } from "@copilotkit/vue/v2";
import AgentExperience from "./components/AgentExperience.vue";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit"><AgentExperience /></CopilotKitProvider>
</template>
