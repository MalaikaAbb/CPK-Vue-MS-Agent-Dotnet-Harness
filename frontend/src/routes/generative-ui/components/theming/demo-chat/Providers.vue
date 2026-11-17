<script setup lang="ts">
import { CopilotKitProvider } from "@copilotkit/vue/v2";
import { standardUI, type GenerativeUITheme } from "@copilotkit/vue/v2/generative-ui";

const theme: GenerativeUITheme = {
  "--a2ui-color-accent": "#d97706",
  "--a2ui-font-family": "Inter, sans-serif",
  "--a2ui-radius-md": "10px",
};
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit" :generativeUI="{ ui: standardUI, theme }">
    <slot />
  </CopilotKitProvider>
</template>
