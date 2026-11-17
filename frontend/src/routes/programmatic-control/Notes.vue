<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
</script>

<template>
  <RouteHeader path="/programmatic-control" />

  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      Two buttons and no chat. <strong>Run agent</strong> appends a fixed user message with <code>agent.addMessage</code> and calls
      <code>copilotkit.runAgent({ agent: toRaw(current) })</code>; <strong>Stop</strong> calls <code>copilotkit.stopAgent</code>.
    </p>
    <div class="mt-4">
      <TryIt
        :prompts="['Click “Run agent”', 'Click “Stop” while it runs']"
        expect="Run disables and Stop enables while the run is live, then they flip back. In the default sample the chat below shows “Summarize the latest sales data” and the streamed reply; Stop cuts the reply off. The verbatim src/App.vue sample renders no output — use the Inspector → Agents › AG-UI Events (agent sales) there."
        fail="Run never disables, or the console logs “CopilotKit runAgent failed” — check agent sales on /info."
      />
    </div>
  </Panel>

  <Panel title="The demo">
    <div class="space-y-4">
      <SourceCode file="frontend/src/routes/programmatic-control/demo-chat/components/AgentTrigger.vue" />
      <SourceCode file="frontend/src/routes/programmatic-control/demo-chat/App.vue" />
    </div>
  </Panel>

  <Panel title="Published, not mounted" description="A fragment: it watches an `agent` it never declares. Mounting it would mean writing the surrounding component, so it is shown only.">
    <div class="space-y-4">
      <PublishedCode page="programmatic-control" :index="2" />
    </div>
  </Panel>

  <Callout tone="harness" title="What the harness added">
    <p>· <code>sales</code> is the MS Agent Framework Quickstart's agent (<code>agent/Program.cs</code>), reached through the landing page's <code>HttpAgent</code> <code>my_agent</code> (<code>backend/agents.ts</code>).</p>
    <p>· <strong>Chat (added on request):</strong> the default sample, <code>HarnessWithChat.vue</code>, mounts the published <code>AgentTrigger.vue</code> unchanged beside a <code>CopilotChat agent-id="sales"</code> under one provider, so a programmatic run is visible. The page's own <code>App.vue</code> is the second sample in the picker.</p>
  </Callout>
  <Panel title="Harness wrapper"><SourceCode file="frontend/src/routes/programmatic-control/demo-chat/HarnessWithChat.vue" /></Panel>
  <Callout tone="warn" title="Doc notes">
    <p>· The page's AgentTrigger never renders the agent's reply; the harness chat sample exists for that.</p>
  </Callout>
</template>
