<script setup lang="ts">
import { CopilotKitProvider } from "@copilotkit/vue/v2";
import MeetingChat from "./components/MeetingChat.vue";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit">
    <MeetingChat />
  </CopilotKitProvider>
</template>
