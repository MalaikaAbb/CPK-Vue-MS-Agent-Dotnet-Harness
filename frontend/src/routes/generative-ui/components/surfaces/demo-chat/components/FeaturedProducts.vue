<script setup lang="ts">
import { GenerativeUISurface } from "@copilotkit/vue/v2/generative-ui";
import type { Product } from "../product";
import { shopUI } from "../shop-ui";
import ProductRow from "./ProductRow.vue";

defineProps<{ products: Product[] }>();
</script>

<template>
  <GenerativeUISurface
    id="featured"
    :ui="shopUI"
    description="The Featured Products row of the home page. When the customer asks to see products here, show them as a ProductGrid with one ProductCard for each product. When they ask for the featured products again, delete this surface."
    :components="['ProductGrid', 'ProductCard']"
  >
    <ProductRow :products="products" />
  </GenerativeUISurface>
</template>
