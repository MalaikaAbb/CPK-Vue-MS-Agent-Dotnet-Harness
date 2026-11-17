<script setup lang="ts">
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
import Canvas from "./components/Canvas.vue";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit">
    <div class="app-shell">
      <Canvas />
      <CopilotChat />
    </div>
  </CopilotKitProvider>
</template>
