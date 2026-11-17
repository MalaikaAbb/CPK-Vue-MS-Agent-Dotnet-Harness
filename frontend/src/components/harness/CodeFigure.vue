<script setup lang="ts">
import { ref, watchEffect } from "vue";

import { highlight } from "@/lib/highlight";

/**
 * The one code block in the app. Both SourceCode (files from this repo) and
 * CodeBlock (snippets as published) render through it. Ported from the React
 * harness; highlighting is async, so plain text shows until Shiki is ready.
 */
const props = withDefaults(
  defineProps<{
    code: string;
    caption?: string;
    language?: string;
    note?: string;
    scroll?: "block" | "inline";
  }>(),
  { scroll: "block" },
);

const html = ref<string | null>(null);
watchEffect(async () => {
  const { code, language } = props;
  html.value = language ? await highlight(code, language) : null;
});
</script>

<template>
  <figure class="code-figure overflow-hidden rounded-lg border border-slate-800 bg-slate-950">
    <figcaption
      v-if="caption || language"
      class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 px-4 py-2 font-mono text-xs text-slate-400"
    >
      <span class="min-w-0 break-all">{{ caption }}</span>
      <span v-if="language" class="shrink-0 uppercase">{{ language }}</span>
    </figcaption>
    <p v-if="note" class="border-b border-amber-900 bg-amber-950/40 px-4 py-2 text-xs text-amber-200">
      {{ note }}
    </p>
    <!-- Shiki escapes the code; the input is this repo's own files and published doc snippets. -->
    <div
      v-if="html"
      :class="scroll === 'block' ? 'max-h-[36rem] overflow-auto' : 'overflow-x-auto'"
      v-html="html"
    />
    <pre
      v-else
      :class="[
        scroll === 'block' ? 'max-h-[36rem] overflow-auto' : 'overflow-x-auto',
        'p-4 text-xs leading-relaxed text-slate-100',
      ]"
    ><code>{{ code }}</code></pre>
  </figure>
</template>
