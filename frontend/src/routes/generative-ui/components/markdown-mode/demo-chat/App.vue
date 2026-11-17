<script setup lang="ts">
import { CopilotKitProvider } from "@copilotkit/vue/v2";
import { standardUI } from "@copilotkit/vue/v2/generative-ui";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit" :generativeUI="{ ui: standardUI, transport: 'markdown' }">
    <slot />
  </CopilotKitProvider>
</template>
