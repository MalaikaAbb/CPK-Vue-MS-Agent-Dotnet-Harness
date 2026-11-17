<script setup lang="ts">
/**
 * [harness] Standard catalog › “Replace a component”: the page prints MyCard.vue
 * and an appUI that overrides Card with it, but not the provider that uses
 * appUI. This is that provider, written like the page's own (runtime-url
 * "/api/copilotkit", :generativeUI="{ ui }"), with a CopilotChat.
 */
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
import { appUI } from "./app-ui";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit" :generativeUI="{ ui: appUI }">
    <CopilotChat />
  </CopilotKitProvider>
</template>
