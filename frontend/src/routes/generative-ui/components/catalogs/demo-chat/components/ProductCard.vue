<script setup lang="ts">
defineProps<{ name: string; price: number; imageUrl: string }>();
</script>

<template>
  <article>
    <img :src="imageUrl" :alt="name" />
    <h4>{{ name }}</h4>
    <p>{{ "$" + price }}</p>
  </article>
</template>
