<script setup lang="ts">
// [harness] Printed under “Two levels deep” on the Slots page.
// The page prints only the template below; these imports are the only added lines.
import { CopilotChat, CopilotChatAssistantMessage, CopilotChatMessageView } from "@copilotkit/vue/v2";
import CustomToolbarAction from "./CustomToolbarAction.vue"; // [harness] stand-in — never published
</script>

<template>
<CopilotChat>
  <template #message-view="{ messages, isRunning }">
    <CopilotChatMessageView :messages="messages" :is-running="isRunning">
      <template #assistant-message="assistantProps">
        <CopilotChatAssistantMessage v-bind="assistantProps">
          <template #toolbar-items>
            <CustomToolbarAction />
          </template>
        </CopilotChatAssistantMessage>
      </template>
    </CopilotChatMessageView>
  </template>
</CopilotChat>
</template>
