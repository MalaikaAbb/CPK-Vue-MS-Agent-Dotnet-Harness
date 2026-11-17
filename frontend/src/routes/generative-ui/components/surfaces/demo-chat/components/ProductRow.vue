<script setup lang="ts">
/**
 * [harness] STAND-IN — NOT FROM THE DOCS.
 *
 * Surfaces' FeaturedProducts.vue renders `<ProductRow :products="products" />`
 * as the surface's default content but no page defines ProductRow. This is the
 * minimum that lets it mount: it takes the one prop the page passes and lists
 * each product's name.
 */
import StandInBadge from "@/components/harness/StandInBadge.vue";

defineProps<{ products: { name: string }[] }>();
</script>

<template>
  <div class="flex flex-wrap items-center gap-2 p-2">
    <StandInBadge name="ProductRow" />
    <span v-for="p in products" :key="p.name" class="rounded border px-2 py-1 text-sm">{{ p.name }}</span>
  </div>
</template>
