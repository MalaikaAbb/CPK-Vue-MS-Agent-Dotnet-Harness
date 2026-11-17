<script setup lang="ts">
import { computed } from "vue";
import { RouterLink } from "vue-router";

import { demoPath, docUrl, findRoute } from "@/lib/nav-config";

import StatusBadge from "./StatusBadge.vue";

/**
 * Every route renders this. It resolves its own metadata from the path so a
 * page can never drift from the nav or the status table.
 */
const props = defineProps<{ path: string }>();
const route = computed(() => findRoute(props.path));
const demo = computed(() => (route.value ? demoPath(route.value) : undefined));
</script>

<template>
  <header v-if="!route" class="border-b border-rose-300 pb-4">
    <p class="text-sm text-rose-700">No nav entry registered for <code>{{ path }}</code>.</p>
  </header>
  <header v-else class="border-b border-slate-200 pb-5 dark:border-slate-800">
    <div class="flex flex-wrap items-center gap-3">
      <h1 class="text-2xl font-semibold tracking-tight text-slate-900 dark:text-slate-50">{{ route.title }}</h1>
      <StatusBadge :status="route.status" />
    </div>
    <p class="mt-2 max-w-3xl text-sm text-slate-600 dark:text-slate-400">{{ route.summary }}</p>
    <p v-if="route.statusNote" class="mt-2 max-w-3xl text-sm text-slate-500">{{ route.statusNote }}</p>
    <div class="mt-4 flex flex-wrap items-center gap-3 text-sm">
      <!-- Always a new tab: the demo route is chrome-free and meant to be watched on its own. -->
      <a v-if="demo" :href="demo" target="_blank" rel="noreferrer" class="rounded-md bg-[var(--accent)] px-3 py-1.5 font-medium text-white">
        Open demo ↗
      </a>
      <a :href="docUrl(route)" target="_blank" rel="noreferrer" class="font-medium text-[var(--accent)] underline underline-offset-4">
        Doc page being tested ↗
      </a>
      <RouterLink to="/status" class="text-slate-500 underline underline-offset-4 hover:text-slate-800 dark:hover:text-slate-200">
        All statuses
      </RouterLink>
    </div>
  </header>
</template>
