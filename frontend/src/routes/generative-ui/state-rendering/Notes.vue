<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
</script>

<template>
  <RouteHeader path="/generative-ui/state-rendering" />
  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      <code>useAgent</code> with <code>OnStateChanged</code> + <code>OnRunStatusChanged</code> on agent <code>researcher</code>;
      <code>ResearchProgress</code> renders <code>status</code>, a progress bar from <code>completed</code>/<code>total</code>, and <code>draft</code>.
    </p>
    <div class="mt-4">
      <TryIt :prompts="['Write a short note about bicycles']" expect="If the backend wrote these keys: status text, a moving bar and a draft." fail="What actually happens here: “Idle” and an empty bar (see below)." />
    </div>
  </Panel>
  <Panel title="The demo">
    <div class="space-y-4">
      <SourceCode file="frontend/src/routes/generative-ui/state-rendering/demo-chat/components/ResearchProgress.vue" />
      <SourceCode file="frontend/src/routes/generative-ui/state-rendering/demo-chat/App.vue" />
    </div>
  </Panel>
  <Callout tone="warn" title="Why this route is broken (README §9.4)">
    <p>The MS Agent Framework State Rendering page publishes no backend at all. <code>researcher</code> is therefore the Quickstart agent, which writes no state, so <code>ResearchProgress</code> stays on “Idle”.</p>
  </Callout>
  <Callout tone="harness" title="Agent id"><p><code>researcher</code> → <code>my_agent</code>, the MS Agent Framework Quickstart's agent (<code>backend/agents.ts</code>).</p></Callout>
</template>
