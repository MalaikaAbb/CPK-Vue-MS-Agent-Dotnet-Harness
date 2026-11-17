<script setup lang="ts">
// [harness] Printed under “Labels” on the Slots page.
// The page prints only the template below; these imports are the only added lines.
import { CopilotChat } from "@copilotkit/vue/v2";
</script>

<template>
<CopilotChat
  :labels="{
    chatInputPlaceholder: 'Ask your agent anything…',
    welcomeMessageText: 'How can I help you today?',
    chatDisclaimerText: 'AI responses may be inaccurate.',
  }"
/>
</template>
