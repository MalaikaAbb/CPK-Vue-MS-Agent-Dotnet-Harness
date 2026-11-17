<script setup lang="ts">
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
import { standardUI } from "@copilotkit/vue/v2/generative-ui";
</script>

<template>
  <CopilotKitProvider
    runtime-url="http://localhost:8200/api/copilotkit"
    :generativeUI="{ ui: standardUI }"
  >
    <div style="height: 100vh">
      <CopilotChat />
    </div>
  </CopilotKitProvider>
</template>
