<script setup lang="ts">
import { RouterLink } from "vue-router";

import DocSyncedAt from "@/components/doc-sync/DocSyncedAt.vue";
import Panel from "@/components/harness/Panel.vue";
import StatusBadge from "@/components/harness/StatusBadge.vue";
import { DOCS_ROOT, NAV, demoPath, docUrl } from "@/lib/nav-config";

const groups = NAV.filter((g) => g.title !== "Harness");
</script>

<template>
  <header class="border-b border-slate-200 pb-5 dark:border-slate-800">
    <h1 class="text-2xl font-semibold tracking-tight text-slate-900 dark:text-slate-50">Status overview</h1>
    <p class="mt-2 max-w-3xl text-sm text-slate-600 dark:text-slate-400">
      Every doc page tracked by this harness, its route, and where it stands. This mirrors the checklist in the repo README.
    </p>
    <p class="mt-2 text-sm text-slate-500">
      Synced against
      <a :href="DOCS_ROOT" target="_blank" rel="noreferrer" class="text-[var(--accent)] underline underline-offset-4">the live docs</a>
      on <DocSyncedAt />.
    </p>
  </header>

  <Panel v-for="group in groups" :key="group.title" :title="group.title">
    <div class="overflow-x-auto">
      <table class="w-full min-w-[40rem] text-left text-sm">
        <thead>
          <tr class="border-b border-slate-200 text-xs uppercase tracking-wide text-slate-500 dark:border-slate-800">
            <th class="pb-2 pr-4 font-medium">Route</th>
            <th class="pb-2 pr-4 font-medium">Status</th>
            <th class="pb-2 font-medium">Doc page</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-100 dark:divide-slate-800">
          <tr v-for="route in group.routes" :key="route.path" class="align-top">
            <td class="py-3 pr-4">
              <RouterLink :to="route.path" class="font-medium text-[var(--accent)] underline underline-offset-4">{{ route.title }}</RouterLink>
              <p class="mt-0.5 font-mono text-xs text-slate-500">{{ route.path }}</p>
              <a v-if="demoPath(route)" :href="demoPath(route)" target="_blank" rel="noreferrer" class="mt-1 inline-block text-xs text-slate-500 underline underline-offset-4 hover:text-[var(--accent)]">demo ↗</a>
            </td>
            <td class="py-3 pr-4">
              <StatusBadge :status="route.status" />
              <p v-if="route.statusNote" class="mt-1 max-w-xs text-xs text-slate-500">{{ route.statusNote }}</p>
            </td>
            <td class="py-3">
              <a :href="docUrl(route)" target="_blank" rel="noreferrer" class="font-mono text-xs text-slate-600 underline underline-offset-4 dark:text-slate-400">{{ route.docPath }}</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </Panel>
</template>
