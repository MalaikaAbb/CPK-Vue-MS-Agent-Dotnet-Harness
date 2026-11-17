<script setup lang="ts">
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
import "@copilotkit/vue/styles.css";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit">
    <CopilotChat agent-id="my-agent" />
  </CopilotKitProvider>
</template>
