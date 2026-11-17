<script setup lang="ts">
/**
 * [harness] NOT FROM THE DOCS — added at the user's request.
 *
 * The page's App.vue mounts only AgentTrigger (two buttons), so a run's
 * output is visible only in the Inspector. This mounts the same published
 * AgentTrigger.vue, unchanged, beside a CopilotChat on the same agent
 * (`sales`) under one provider. They share one agent instance, so the
 * message AgentTrigger adds and the reply it triggers appear in the chat.
 * The verbatim App.vue is still available as the second sample.
 */
import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";

import AgentTrigger from "./components/AgentTrigger.vue";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit">
    <div style="display: flex; flex-direction: column; height: 100%">
      <div style="display: flex; gap: 8px; padding: 12px 16px; border-bottom: 1px solid #e5e7eb">
        <AgentTrigger />
      </div>
      <div style="flex: 1; min-height: 0">
        <CopilotChat agent-id="sales" />
      </div>
    </div>
  </CopilotKitProvider>
</template>
