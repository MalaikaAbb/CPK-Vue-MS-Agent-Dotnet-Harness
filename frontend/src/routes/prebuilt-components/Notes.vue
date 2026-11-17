<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
</script>

<template>
  <RouteHeader path="/prebuilt-components" />

  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      The page's one code sample: the stylesheet imported once, <code>CopilotKitProvider</code> around the app, and
      <code>CopilotChat agent-id="my-agent"</code> in the provider's default slot.
    </p>
    <div class="mt-4">
      <TryIt :prompts="['Hello', 'What did I just say?']" expect="Streamed replies in a full-height chat; the second answer recalls the first message." fail="Agent my-agent not found — the backend is not running this repo's server.ts." />
    </div>
  </Panel>

  <Panel title="The demo"><SourceCode file="frontend/src/routes/prebuilt-components/demo-chat/App.vue" /></Panel>

  <Callout tone="harness" title="Agent id">
    <p><code>my-agent</code> is never registered by any Vue page. It is the MS Agent Framework Quickstart's agent (<code>agent/Program.cs</code>), reached through the landing page's <code>HttpAgent</code> <code>my_agent</code> (<code>backend/agents.ts</code>).</p>
  </Callout>

  <Callout tone="warn" title="Named on the page, no code on the page">
    <p>· <code>CopilotSidebar</code> and <code>CopilotPopup</code> — only linked (to /vue/prebuilt-components/sidebar and /popup, outside this pass).</p>
    <p>· <code>useConfigureSuggestions</code> — described, no sample.</p>
    <p>· The page itself says other prebuilt-component variations "do not have a runnable Vue Showcase route yet".</p>
  </Callout>
</template>
