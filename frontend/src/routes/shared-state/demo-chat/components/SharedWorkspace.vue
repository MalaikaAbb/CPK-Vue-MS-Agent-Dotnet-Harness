<!--
  [harness] The Shared State page prints SharedWorkspace.vue in two fragments
  (“Reading agent state”, then “Writing agent state”); the second has no imports
  and uses `agent` from the first. They are merged here, each verbatim, in order.
-->
<script setup lang="ts">
import { computed } from "vue";
import { useAgent, UseAgentUpdate } from "@copilotkit/vue/v2";

type WorkspaceState = {
  notes?: string[];
  preferences?: { tone?: string };
};

const { agent } = useAgent({
  agentId: "workspace",
  updates: [UseAgentUpdate.OnStateChanged],
});
const state = computed(
  () => (agent.value?.state ?? {}) as WorkspaceState,
);

// ── [harness] second fragment of this file (“Writing agent state”) ──
function setTone(tone: string) {
  const current = agent.value;
  if (!current) return;

  const previous = (current.state ?? {}) as WorkspaceState;
  current.setState({
    ...previous,
    preferences: { ...previous.preferences, tone },
  });
}
</script>

<template>
  <ul>
    <li v-for="note in state.notes ?? []" :key="note">{{ note }}</li>
  </ul>
  <!-- [harness] second fragment's template -->
  <button @click="setTone('concise')">Prefer concise answers</button>
</template>
