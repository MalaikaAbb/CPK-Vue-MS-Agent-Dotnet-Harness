<script setup lang="ts">
import { computed, onMounted } from "vue";

import { docSyncState, loadDocSyncState } from "@/lib/doc-sync-state";

/** The repo's single doc-sync date, read from doc-snapshot/manifest.json. */
const props = defineProps<{ withPages?: boolean }>();
onMounted(() => loadDocSyncState());
const text = computed(() => {
  const m = docSyncState.value?.manifest;
  if (!m || m.kind !== "ok") return "never synced";
  const day = m.manifest.syncedAt.slice(0, 10);
  return props.withPages ? `${day} · ${Object.keys(m.manifest.pages).length} pages` : day;
});
</script>

<template><span>{{ text }}</span></template>
