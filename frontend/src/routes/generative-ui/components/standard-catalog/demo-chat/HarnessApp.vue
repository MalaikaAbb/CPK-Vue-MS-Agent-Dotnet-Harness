<script setup lang="ts">
// [harness] Standard catalog › “Turn it on”.
// Mounts the page's provider component with a <CopilotChat /> in its <slot />.
import { CopilotChat } from "@copilotkit/vue/v2";
import Providers from "./Providers.vue";
</script>

<template>
  <Providers>
    <CopilotChat />
  </Providers>
</template>
