<script setup lang="ts">
/**
 * [harness] NOT FROM THE DOCS. The page says OrderSearch.vue "must run inside
 * your existing CopilotKitProvider" and prints none; this is that provider.
 */
import HarnessProvider from "@/components/harness/HarnessProvider.vue";

import ModelContextStatus from "./ModelContextStatus.vue";
import OrderSearch from "./OrderSearch.vue";
</script>

<template>
  <HarnessProvider>
    <ModelContextStatus mode="registered by useFrontendTool in OrderSearch.vue" />
    <OrderSearch />
  </HarnessProvider>
</template>
