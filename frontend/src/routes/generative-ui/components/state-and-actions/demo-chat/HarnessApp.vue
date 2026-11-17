<script setup lang="ts">
/**
 * [harness] State and actions › “Run your code when users click”: the page
 * prints shopUI (an addToCart function and an onAddToCart event) and
 * ProductCard.vue, but its handler sample (useGenerativeUIFunction) needs
 * `./cart-store`, which no page publishes, so it is shown and not mounted.
 * This is the provider for shopUI, written like the page's own, with a
 * CopilotChat. With no handler registered, clicking “Add to cart” takes the
 * card's own error path.
 */
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
import { shopUI } from "./shop-ui";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit" :generativeUI="{ ui: shopUI }">
    <CopilotChat />
  </CopilotKitProvider>
</template>
