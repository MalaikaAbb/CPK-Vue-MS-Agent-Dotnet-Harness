<script setup lang="ts">
// [harness] The page prints only the one useDefaultRenderTool line below for this
// file. The imports and <template> are the zero-config AgentExperience.vue's, and
// BrandedToolCard is a stand-in — it is never published.
import { CopilotChat, useDefaultRenderTool } from "@copilotkit/vue/v2";
import BrandedToolCard from "./BrandedToolCard.vue"; // [harness] stand-in

useDefaultRenderTool({ render: BrandedToolCard });
</script>

<template><CopilotChat /></template>
