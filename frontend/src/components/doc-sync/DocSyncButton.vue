<script setup lang="ts">
import { ref } from "vue";
import { RouterLink } from "vue-router";

import { runDocSync } from "@/lib/doc-sync-state";
import type { SyncResult } from "@/lib/doc-sync/types";

/** The one control the whole feature hangs off. Rendered on both `/` and `/doc-sync`. */
const props = defineProps<{ baseline: boolean }>();
const pending = ref(false);
const result = ref<SyncResult | null>(null);

async function run() {
  pending.value = true;
  try {
    result.value = await runDocSync();
  } finally {
    pending.value = false;
  }
}
</script>

<template>
  <div class="flex flex-col items-end gap-2">
    <button
      type="button"
      :disabled="pending"
      class="inline-flex shrink-0 items-center gap-2 rounded-lg border border-slate-300 bg-white px-3 py-1.5 text-sm font-medium text-slate-800 shadow-sm transition hover:bg-slate-50 disabled:cursor-not-allowed disabled:opacity-60 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-100 dark:hover:bg-slate-800"
      @click="run"
    >
      <span v-if="pending" aria-hidden="true" class="size-3 animate-spin rounded-full border-2 border-slate-400 border-t-transparent" />
      {{ pending ? "Fetching docs…" : props.baseline ? "Create doc baseline" : "Sync docs now" }}
    </button>
    <p
      v-if="result && !pending"
      :class="['max-w-xs text-right text-xs', result.ok ? 'text-slate-600 dark:text-slate-400' : 'text-rose-700 dark:text-rose-400']"
    >
      {{ result.message }}
      <RouterLink v-if="result.ok && result.changed > 0" to="/doc-sync" class="text-[var(--accent)] underline underline-offset-4">See the diffs</RouterLink>
    </p>
  </div>
</template>
