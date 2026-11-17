<script setup lang="ts">
// [harness] Markdown mode › “Turn it on”: the page's src/App.vue has a <slot />.
// Mounts the page's provider component with a <CopilotChat /> in its <slot />.
import { CopilotChat } from "@copilotkit/vue/v2";
import App from "./App.vue";
</script>

<template>
  <App>
    <CopilotChat />
  </App>
</template>
