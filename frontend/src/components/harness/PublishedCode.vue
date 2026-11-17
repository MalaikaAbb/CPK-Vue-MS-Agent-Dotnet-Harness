<script setup lang="ts">
import { computed } from "vue";

import published from "@/lib/published.json";

import CodeFigure from "./CodeFigure.vue";

/**
 * [harness] A code block exactly as the doc page publishes it, read from
 * src/lib/published.json (written from the page's .md by
 * scripts/write-doc-files.py, highlight markers stripped as the rendered page
 * does). Used for samples that are shown but not mounted.
 */
const props = defineProps<{ page: string; index: number; note?: string }>();

type Block = { lang: string; title: string | null; code: string; rendered: boolean };
const block = computed(() => (published as Record<string, Block[]>)[props.page]?.[props.index]);
const LANG: Record<string, string> = { typescript: "ts", ts: "ts", vue: "vue", python: "python", csharp: "csharp", bash: "bash", css: "css" };
const caption = computed(() => {
  const b = block.value;
  if (!b) return `missing block ${props.page}[${props.index}]`;
  const where = b.rendered ? "as published" : "in the .md export only — NOT on the rendered page";
  return `${b.title ?? "(untitled snippet)"} — ${where}`;
});
</script>

<template>
  <CodeFigure
    v-if="block"
    :code="block.code"
    :caption="caption"
    :language="LANG[block.lang]"
    :note="note"
    scroll="block"
  />
  <p v-else class="text-sm text-rose-700">No published block {{ page }}[{{ index }}].</p>
</template>
