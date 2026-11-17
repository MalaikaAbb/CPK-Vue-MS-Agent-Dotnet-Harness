<script setup lang="ts">
// [harness] Printed under “Custom Components” on the Slots page.
// The page prints only the template below; these imports are the only added lines.
import { CopilotChat } from "@copilotkit/vue/v2";
import CustomMessageView from "./CustomMessageView.vue"; // [harness] stand-in — never published
</script>

<template>
<CopilotChat>
  <template #message-view="{ messages, isRunning }">
    <CustomMessageView :messages="messages" :is-running="isRunning" />
  </template>
</CopilotChat>
</template>
