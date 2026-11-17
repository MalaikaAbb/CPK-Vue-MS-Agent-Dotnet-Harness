<script setup lang="ts">
defineProps<{ title?: string }>();
</script>

<template>
  <section>
    <h3 v-if="title">{{ title }}</h3>
    <div class="grid grid-cols-2 gap-4">
      <slot name="children" />
    </div>
  </section>
</template>
