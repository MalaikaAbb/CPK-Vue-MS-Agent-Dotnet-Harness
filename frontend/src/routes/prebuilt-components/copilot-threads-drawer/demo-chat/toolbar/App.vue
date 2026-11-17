<script setup lang="ts">
import {
  CopilotChat,
  CopilotChatConfigurationProvider,
  CopilotKitProvider,
  CopilotThreadsDrawer,
} from "@copilotkit/vue/v2";
import NewConversationButton from "./components/NewConversationButton.vue";
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
        <main style="flex: 1; display: flex; flex-direction: column">
          <header><NewConversationButton /></header>
          <CopilotChat />
        </main>
      </div>
    </CopilotChatConfigurationProvider>
  </CopilotKitProvider>
</template>
