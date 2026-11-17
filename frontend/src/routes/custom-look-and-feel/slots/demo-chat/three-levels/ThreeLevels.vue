<script setup lang="ts">
// [harness] Printed under “Three levels deep” on the Slots page, as a fragment that reads `assistantProps` from an enclosing slot it does not print; nested in the Two-levels fragment for that reason.
// The page prints only the template below; these imports are the only added lines.
import { CopilotChat, CopilotChatAssistantMessage, CopilotChatMessageView } from "@copilotkit/vue/v2";
</script>

<template>
<CopilotChat>
  <template #message-view="{ messages, isRunning }">
    <CopilotChatMessageView :messages="messages" :is-running="isRunning">
      <template #assistant-message="assistantProps">
        <!-- [harness] ↓ the Three-levels fragment, verbatim, inside the Two-levels slot it reads assistantProps from -->
        <CopilotChatAssistantMessage v-bind="assistantProps">
          <template #copy-button="{ onCopy }">
            <button type="button" @click="onCopy">Copy response</button>
          </template>
        </CopilotChatAssistantMessage>
      </template>
    </CopilotChatMessageView>
  </template>
</CopilotChat>
</template>
