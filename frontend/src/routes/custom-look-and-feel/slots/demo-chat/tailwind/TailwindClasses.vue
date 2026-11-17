<script setup lang="ts">
// [harness] Printed under “Tailwind Classes” on the Slots page.
// The page prints only the template below; these imports are the only added lines.
import { CopilotChat, CopilotChatMessageView } from "@copilotkit/vue/v2";
</script>

<template>
<CopilotChat>
  <template #message-view="{ messages, isRunning }">
    <CopilotChatMessageView
      class="rounded-xl bg-gray-50 p-4 dark:bg-gray-900"
      :messages="messages"
      :is-running="isRunning"
    />
  </template>
</CopilotChat>
</template>
