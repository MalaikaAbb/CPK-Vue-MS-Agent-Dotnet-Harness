<script setup lang="ts">
import {
  CopilotChat,
  CopilotChatConfigurationProvider,
  CopilotKitProvider,
  CopilotThreadsDrawer,
} from "@copilotkit/vue/v2";
import "@copilotkit/vue/styles.css";
</script>

<template>
  <!-- [harness] published: runtime-url="/api/copilotkit" — the Threads runtime is mounted separately at /api/copilotkit-threads (README §9) -->
  <CopilotKitProvider
    runtime-url="/api/copilotkit-threads"
    public-license-key="ck_pub_..."
  >
    <CopilotChatConfigurationProvider agent-id="support">
      <div style="display: flex; height: 100dvh">
        <CopilotThreadsDrawer />
        <CopilotChat />
      </div>
    </CopilotChatConfigurationProvider>
  </CopilotKitProvider>
</template>
