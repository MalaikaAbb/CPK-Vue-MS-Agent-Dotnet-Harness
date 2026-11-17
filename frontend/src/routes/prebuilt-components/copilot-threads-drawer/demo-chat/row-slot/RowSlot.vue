<script setup lang="ts">
// [harness] Printed under “Customization › Per-row content”.
// The page prints only the template below; these imports are the only added lines.
import { CopilotThreadsDrawer } from "@copilotkit/vue/v2";
</script>

<template>
<CopilotThreadsDrawer>
  <template #row="{ thread }">
    <strong>{{ thread.name ?? "New conversation" }}</strong>
  </template>
</CopilotThreadsDrawer>
</template>
