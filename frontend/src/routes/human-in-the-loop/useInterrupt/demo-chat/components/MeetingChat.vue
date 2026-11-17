<script setup lang="ts">
/**
 * [harness] STAND-IN — NOT FROM THE DOCS.
 *
 * The useInterrupt page's App.vue imports `./components/MeetingChat.vue`,
 * which the page never publishes — so App.vue cannot even compile without it.
 * Minimal equivalent: the page's own ApprovalPanel.vue (verbatim, beside this
 * file) above a CopilotChat that starts runs. The panel only appears if the
 * agent interrupts, which BuiltInAgent never does (README §9).
 */
import { CopilotChat } from "@copilotkit/vue/v2";

import StandInBadge from "@/components/harness/StandInBadge.vue";

import ApprovalPanel from "./ApprovalPanel.vue";
</script>

<template>
  <div style="display: flex; flex-direction: column; height: 100%">
    <div style="padding: 8px"><StandInBadge name="MeetingChat" /></div>
    <ApprovalPanel />
    <CopilotChat />
  </div>
</template>
