<script setup lang="ts">
// [harness] Transports › limit generative UI to some agents (agentIds).
// The page prints only the opening provider tag below; these imports, the
// <CopilotChat /> inside it and the closing tag are the only added lines.
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
import { standardUI } from "@copilotkit/vue/v2/generative-ui";
</script>

<template>
<CopilotKitProvider
  runtime-url="/api/copilotkit"
  :generativeUI="{ ui: standardUI, agentIds: ['shop'] }"
>
  <CopilotChat /> <!-- [harness] -->
</CopilotKitProvider> <!-- [harness] -->
</template>
