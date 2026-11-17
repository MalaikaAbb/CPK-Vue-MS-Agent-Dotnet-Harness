<script setup lang="ts">
// [harness] Printed under “Props Override” on the Slots page.
// The page prints only the template below; these imports are the only added lines.
import { CopilotChat, CopilotChatMessageView } from "@copilotkit/vue/v2";
</script>

<template>
<CopilotChat>
  <template #message-view="slotProps">
    <CopilotChatMessageView
      v-bind="slotProps"
      class="my-custom-messages"
      data-testid="message-view"
    />
  </template>
</CopilotChat>
</template>
