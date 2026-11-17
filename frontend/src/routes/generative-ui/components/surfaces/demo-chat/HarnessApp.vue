<script setup lang="ts">
/**
 * [harness] The Surfaces page prints FeaturedProducts.vue (a page target) and a
 * provider component with an error boundary (Providers.vue), but no page that
 * puts them together. This mounts the page's Providers with the page's
 * FeaturedProducts and a CopilotChat to talk to it. `products` is two harness
 * sample items (the page's `Product` type module is never published).
 */
import { CopilotChat } from "@copilotkit/vue/v2";
import Providers from "./Providers.vue";
import FeaturedProducts from "./components/FeaturedProducts.vue";

const products = [
  { id: "p1", name: "Trail Runner", price: 120, imageUrl: "" },
  { id: "p2", name: "City Sneaker", price: 90, imageUrl: "" },
];
</script>

<template>
  <Providers>
    <FeaturedProducts :products="products" />
    <CopilotChat />
  </Providers>
</template>
