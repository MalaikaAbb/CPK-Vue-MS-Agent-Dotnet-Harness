<script setup lang="ts">
import { computed } from "vue";

import { readSource } from "@/lib/source";

import CodeFigure from "./CodeFigure.vue";

/**
 * Renders a file from this repository verbatim — what runs is what is shown.
 * Compare it directly against the doc page linked in the route header.
 */
const props = defineProps<{ file: string; region?: string; note?: string }>();
const source = computed(() => readSource(props.file, props.region));
const caption = computed(() =>
  source.value.lineRange
    ? `${source.value.path}  ·  lines ${source.value.lineRange.start}–${source.value.lineRange.end}`
    : source.value.path,
);
</script>

<template>
  <CodeFigure
    :code="source.code"
    :caption="caption"
    :language="source.language"
    :note="source.error ?? note"
  />
</template>
