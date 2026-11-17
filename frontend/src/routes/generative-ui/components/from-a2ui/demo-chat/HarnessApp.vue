<script setup lang="ts">
// [harness] Adopt from A2UI › “After”: the provider.
// The page prints only the opening provider tag below; these imports, the
// <CopilotChat /> inside it and the closing tag are the only added lines.
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
import { appUI } from "./app-ui";
</script>

<template>
<CopilotKitProvider runtime-url="/api/copilotkit" :generativeUI="{ ui: appUI }">
  <CopilotChat /> <!-- [harness] -->
</CopilotKitProvider> <!-- [harness] -->
</template>
