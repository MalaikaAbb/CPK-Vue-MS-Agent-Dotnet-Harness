<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
</script>

<template>
  <RouteHeader path="/shared-state/streaming" />
  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      <code>StreamingDocument</code> renders agent <code>writer</code>'s <code>state.document</code> with a LIVE badge while the run streams.
    </p>
    <div class="mt-4">
      <TryIt :prompts="['Write a short poem about autumn']" expect="If a backend streamed document: LIVE, then the poem growing in the article." fail="What actually happens here: LIVE while the run lasts, “Waiting for a draft…” throughout, the poem in the chat (see below)." />
    </div>
  </Panel>
  <Panel title="The demo">
    <div class="space-y-4">
      <SourceCode file="frontend/src/routes/shared-state/streaming/demo-chat/components/StreamingDocument.vue" />
      <SourceCode file="frontend/src/routes/shared-state/streaming/demo-chat/App.vue" />
    </div>
  </Panel>
  <Callout tone="warn" title="Why this route is broken (README §9.4)">
    <p>The page's subject is a backend mapping from a streaming tool argument to a state key, and the MS Agent Framework page publishes no backend for it. <code>writer</code> is the Quickstart agent, which streams no state.</p>
  </Callout>
  <Callout tone="harness" title="Agent id"><p><code>writer</code> → <code>my_agent</code>, the MS Agent Framework Quickstart's agent (<code>backend/agents.ts</code>).</p></Callout>
</template>
