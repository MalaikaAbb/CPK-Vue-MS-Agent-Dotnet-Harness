<script setup lang="ts">
// [harness] Catalogs › “Hand it to the provider”.
// The page prints only the opening provider tag below; these imports, the
// <CopilotChat /> inside it and the closing tag are the only added lines.
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
import { shopUI } from "./shop-ui";
</script>

<template>
<CopilotKitProvider runtime-url="/api/copilotkit" :generativeUI="{ ui: shopUI }">
  <CopilotChat /> <!-- [harness] -->
</CopilotKitProvider> <!-- [harness] -->
</template>
