<script setup lang="ts">
// [harness] Printed under “Minimal example” as the provider markup for HeadlessChat.
// The page prints only the template below; these imports are the only added lines.
import { CopilotChatConfigurationProvider, CopilotKitProvider } from "@copilotkit/vue/v2";
import HeadlessChat from "./HeadlessChat.vue";
</script>

<template>
<CopilotKitProvider runtime-url="/api/copilotkit">
  <CopilotChatConfigurationProvider agent-id="my-agent">
    <HeadlessChat />
  </CopilotChatConfigurationProvider>
</CopilotKitProvider>
</template>
