<script setup lang="ts">
/**
 * [harness] Decides whether a route gets the app shell.
 *
 * `/…/demo-chat` routes render full-bleed with no sidebar, so they can be
 * watched or recorded without the harness in frame. Everything else gets the
 * sidebar layout. There is no app-wide CopilotKitProvider: each demo mounts
 * the doc page's own App.vue, provider included, exactly as published.
 */
import { computed } from "vue";
import { RouterView, useRoute } from "vue-router";

import NavSidebar from "@/components/harness/NavSidebar.vue";

const route = useRoute();
const isDemo = computed(() => route.path.endsWith("/demo-chat"));
</script>

<template>
  <div v-if="isDemo" class="h-dvh overflow-hidden"><RouterView /></div>
  <template v-else>
    <NavSidebar />
    <main class="lg:pl-72">
      <div class="mx-auto max-w-5xl space-y-6 px-5 py-10 lg:px-8"><RouterView /></div>
    </main>
  </template>
</template>
