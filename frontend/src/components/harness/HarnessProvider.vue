<script setup lang="ts">
/**
 * [harness] NOT FROM THE DOCS.
 *
 * Several Vue doc pages publish a component and say "render it below
 * CopilotKitProvider" without publishing the App.vue that does so. This is
 * that missing provider, shaped exactly like every App.vue the Vue docs do
 * publish: `<CopilotKitProvider runtime-url="/api/copilotkit">`. Nothing else.
 * `runtime-url` is overridable only for the Threads routes, whose runtime is
 * mounted at /api/copilotkit-threads (README §9).
 *
 * Each notes page that uses it says so in a Harness callout.
 */
import { CopilotKitProvider } from "@copilotkit/vue/v2";

withDefaults(defineProps<{ runtimeUrl?: string }>(), { runtimeUrl: "/api/copilotkit" });
</script>

<template>
  <CopilotKitProvider :runtime-url="runtimeUrl">
    <slot />
  </CopilotKitProvider>
</template>
