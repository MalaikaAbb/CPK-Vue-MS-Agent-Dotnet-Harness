<script setup lang="ts">
// [harness] Printed under “Customization › Named web-component slots”.
// The page prints only the template below; these imports are the only added lines.
import { CopilotThreadsDrawer } from "@copilotkit/vue/v2";
</script>

<template>
<CopilotThreadsDrawer>
  <span slot="header">My conversations</span>
</CopilotThreadsDrawer>
</template>
