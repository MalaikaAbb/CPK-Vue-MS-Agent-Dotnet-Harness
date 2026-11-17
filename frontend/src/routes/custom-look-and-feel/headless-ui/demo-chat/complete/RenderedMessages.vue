<script setup lang="ts">
import { computed } from "vue";
import {
  CopilotChatAssistantMessage,
  CopilotChatMessageView,
  CopilotChatUserMessage,
  useAgent,
} from "@copilotkit/vue/v2";

const { agent } = useAgent({ agentId: "my-agent" });
const messages = computed(() => agent.value?.messages ?? []);
const isRunning = computed(() => agent.value?.isRunning ?? false);
</script>

<template>
  <CopilotChatMessageView :messages="messages" :is-running="isRunning">
    <template #assistant-message="assistantProps">
      <article class="assistant-bubble">
        <CopilotChatAssistantMessage v-bind="assistantProps" />
      </article>
    </template>
    <template #user-message="userProps">
      <article class="user-bubble">
        <CopilotChatUserMessage v-bind="userProps" />
      </article>
    </template>
  </CopilotChatMessageView>
</template>
