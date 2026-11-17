<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
</script>

<template>
  <RouteHeader path="/multi-agent/subagents" />
  <Callout tone="warn" title="Gap: an agent with no host and no frontend (README §9.4)">
    <p>· <code>agent/SubagentsAgent.cs</code> (printed twice; the second print is the whole file and contains the first) defines a <code>SubagentsAgent</code> (a <code>DelegatingAIAgent</code>), its delegation store and a <code>SubagentsAgentFactory.CreateAgent()</code>. Even the full print is cut off inside <code>CreateAgent()</code> (53 <code>{</code>, 51 <code>}</code>), so it cannot compile, and no page prints a host that maps it. Per your rules nothing was written in its place; it is not served.</p>
    <p>· The “Rendering a live delegation log” section publishes no Vue code, so this route has no demo, and nothing would call the agent.</p>
  </Callout>
  <Panel title="Published backend, as printed">
    <PublishedCode page="multi-agent__subagents" :index="1" note="agent/SubagentsAgent.cs, the full print." />
  </Panel>
</template>
