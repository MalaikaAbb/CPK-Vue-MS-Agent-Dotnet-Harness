<script setup lang="ts">
// [harness] Printed under “Disclaimer slot” on the Slots page.
// The page prints only the template below; these imports are the only added lines.
import { CopilotChat, CopilotChatInput } from "@copilotkit/vue/v2";
</script>

<template>
<CopilotChat>
  <template #input="inputProps">
    <CopilotChatInput v-bind="inputProps">
      <template #disclaimer>
        <p class="support-disclaimer">Responses may be inaccurate.</p>
      </template>
    </CopilotChatInput>
  </template>
</CopilotChat>
</template>
