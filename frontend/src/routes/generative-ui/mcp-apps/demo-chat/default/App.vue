<script setup lang="ts">
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
</script>

<template>
  <!-- [harness] published: runtime-url="/api/copilotkit" — the MCP Apps runtime is mounted separately at /api/copilotkit-mcp-apps (README §9) -->
  <CopilotKitProvider runtime-url="/api/copilotkit-mcp-apps">
    <main style="height: 100dvh"><CopilotChat /></main>
  </CopilotKitProvider>
</template>
