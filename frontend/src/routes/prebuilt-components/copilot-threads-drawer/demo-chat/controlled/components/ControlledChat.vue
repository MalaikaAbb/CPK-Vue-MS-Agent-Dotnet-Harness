<script setup lang="ts">
import { ref } from "vue";
import {
  CopilotChat,
  CopilotChatConfigurationProvider,
  CopilotThreadsDrawer,
} from "@copilotkit/vue/v2";

const threadId = ref<string>(crypto.randomUUID());
const selectThread = (id: string) => {
  threadId.value = id;
};
const startNewConversation = () => {
  threadId.value = crypto.randomUUID();
};
</script>

<template>
  <CopilotChatConfigurationProvider :thread-id="threadId">
    <CopilotThreadsDrawer
      :on-thread-select="selectThread"
      :on-new-thread="startNewConversation"
    />
    <button type="button" @click="startNewConversation">
      New conversation
    </button>
    <CopilotChat />
  </CopilotChatConfigurationProvider>
</template>
