<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
</script>

<template>
  <RouteHeader path="/shared-state" />
  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      Agent <code>workspace</code>'s state read through <code>useAgent</code> and rendered as a notes list, and written back with
      <code>agent.setState</code> from the “Prefer concise answers” button.
    </p>
    <div class="mt-4">
      <TryIt :prompts="['Click “Prefer concise answers”, then ask: Write a two-line poem']" expect="The click writes preferences.tone into the agent state (Inspector › State); the chat replies." fail="What does not happen here: the notes list never fills — no published MS Agent Framework backend writes state (see below)." />
    </div>
  </Panel>
  <Panel title="The demo">
    <div class="space-y-4">
      <SourceCode file="frontend/src/routes/shared-state/demo-chat/components/SharedWorkspace.vue" />
      <SourceCode file="frontend/src/routes/shared-state/demo-chat/App.vue" />
    </div>
  </Panel>
  <Panel title="The two fragments, as published">
    <div class="space-y-4">
      <PublishedCode page="shared-state" :index="0" />
      <PublishedCode page="shared-state" :index="1" />
    </div>
  </Panel>
  <Callout tone="harness" title="What the harness changed">
    <p>· The page prints <code>SharedWorkspace.vue</code> twice (reading, then writing; the second has no imports and uses <code>agent</code> from the first). Merged into one file, each verbatim.</p>
    <p>· <code>workspace</code> → <code>my_agent</code>, the MS Agent Framework Quickstart's agent (<code>backend/agents.ts</code>); the page publishes no backend.</p>
  </Callout>
  <Callout tone="warn" title="Doc note (README §9.3)">
    <p>The MS Agent Framework Shared State page publishes no backend. The Quickstart agent has no tools, and its adapter does not pass the run's state to the model (verified by capturing the request), so nothing writes <code>notes</code> and the list stays empty; the tone write-back reaches the run's state.</p>
  </Callout>
</template>
