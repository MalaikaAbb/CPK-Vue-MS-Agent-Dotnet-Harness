<script setup lang="ts">
import { ref } from "vue";
import type { GenerativeUIInvokeResult } from "@copilotkit/vue/v2/generative-ui";

const props = defineProps<{
  productId: string;
  name: string;
  onAddToCart?: (args: { productId: string }) => Promise<GenerativeUIInvokeResult>;
}>();
const error = ref<string>();

async function add() {
  const result = await props.onAddToCart?.({ productId: props.productId });
  if (result && !result.ok) error.value = result.error.message;
}
</script>

<template>
  <article>
    <h4>{{ name }}</h4>
    <button v-if="onAddToCart" @click="add">Add to cart</button>
    <p v-if="error" role="alert">{{ error }}</p>
  </article>
</template>
