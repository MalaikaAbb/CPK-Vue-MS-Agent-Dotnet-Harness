<script setup lang="ts">
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
import StreamingDocument from "./components/StreamingDocument.vue";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit">
    <StreamingDocument />
    <CopilotChat agent-id="writer" />
  </CopilotKitProvider>
</template>
