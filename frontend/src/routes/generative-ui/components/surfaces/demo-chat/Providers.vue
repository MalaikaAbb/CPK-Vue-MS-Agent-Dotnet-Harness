<script setup lang="ts">
import { CopilotKitProvider } from "@copilotkit/vue/v2";
import type { GenerativeUIErrorInfo } from "@copilotkit/vue/v2/generative-ui";
import RetryFallback from "./components/RetryFallback.vue";
import { shopUI } from "./shop-ui";

function onError(info: GenerativeUIErrorInfo) {
  console.warn(info.kind, info.surfaceId, info.error.message);
}
</script>

<template>
  <CopilotKitProvider
    runtime-url="/api/copilotkit"
    :generativeUI="{ ui: shopUI, errorBoundary: { onError, fallback: RetryFallback } }"
  >
    <slot />
  </CopilotKitProvider>
</template>
