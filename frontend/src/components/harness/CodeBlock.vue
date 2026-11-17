<script setup lang="ts">
/** A snippet written into the page — used for code exactly as the doc page publishes it. */
import CodeFigure from "./CodeFigure.vue";

defineProps<{ code: string; filename?: string; language?: string }>();
</script>

<template>
  <CodeFigure :code="code" :caption="filename" :language="language" scroll="inline" />
</template>
