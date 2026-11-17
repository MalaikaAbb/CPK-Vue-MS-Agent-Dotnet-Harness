<script setup lang="ts">
import {
  CopilotChat,
  CopilotChatConfigurationProvider,
  CopilotKitProvider,
} from "@copilotkit/vue/v2";
import ThreadSidebar from "./components/ThreadSidebar.vue";
</script>

<template>
  <!-- [harness] published: runtime-url="/api/copilotkit" — the Threads runtime is mounted separately at /api/copilotkit-threads (README §9) -->
  <CopilotKitProvider runtime-url="/api/copilotkit-threads">
    <CopilotChatConfigurationProvider agent-id="my-agent">
      <div class="flex" style="height: 100dvh">
        <ThreadSidebar />
        <CopilotChat />
      </div>
    </CopilotChatConfigurationProvider>
  </CopilotKitProvider>
</template>
