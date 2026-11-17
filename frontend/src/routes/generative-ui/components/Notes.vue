<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
const D = "frontend/src/routes/generative-ui/components/demo-chat";
</script>

<template>
  <RouteHeader path="/generative-ui/components" />
  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">The overview's Vue setup: a provider given the standard catalog (<code>:generativeUI=&quot;{ ui: standardUI }&quot;</code>) and a plain <code>CopilotChat</code>; the agent answers visual questions by rendering standard components.</p>
    <div class="mt-4"><TryIt :prompts="['Compare the Starter, Team, and Enterprise plans in a table']" expect="A table component fills in inside the chat; a follow-up such as “add a column for support” changes it in place." fail="A prose answer and no component: render_ui reached the model without its guide (see the agent note)." /></div>
  </Panel>
  <Panel title="Published files, mounted verbatim">
    <div class="space-y-4">
      <SourceCode :file="`${D}/App.vue`" note="Vue tab, verbatim (runtime-url http://localhost:8200/api/copilotkit)." />
    </div>
  </Panel>
  <Panel title="Published for Vue, not mounted">
    <div class="space-y-4">
      <PublishedCode page="ms-agent-harness-dotnet__generative-ui__components" :index="26" note="The plugin entry. Applied in the harness's own src/main.ts (labelled), since the harness has one entry for every route." />
      <PublishedCode page="ms-agent-harness-dotnet__generative-ui__components" :index="11" note="The page's runtime for Vue: a TanStack BuiltInAgent with convertInputToTanStackAI. Not served — your choice was the MS Agent Quickstart agent." />
      <PublishedCode page="ms-agent-harness-dotnet__generative-ui__components" :index="6" note="The Vue tab's install line. @tanstack/* is not installed (its runtime is not served); chart.js and maplibre-gl are (next block)." />
      <PublishedCode page="ms-agent-harness-dotnet__generative-ui__components" :index="25" note="Installed in frontend/." />
    </div>
  </Panel>
  <Callout tone="harness" title="What the harness added">
    <p>· <code>src/main.ts</code> applies <code>GenerativeUIChart</code> and <code>GenerativeUIMap</code> (the page's plugin entry); <code>chart.js</code> and <code>maplibre-gl</code> are installed as the page says.</p>
  </Callout>
  <Callout tone="warn" title="Agent: the MS Agent Framework Quickstart agent (the ms-agent-py choice, same rules; README §9.9)">
    <p>The samples keep <code>runtime-url="/api/copilotkit"</code> as published, so <code>default</code> is the MS Agent Framework Quickstart agent. For a run that carries a catalog, the Copilot Runtime adds the <code>render_ui</code> tool to the run's tools and its guide (the components, their props, how to call the tool) to the run's context. This agent's adapter forwards the tools but not the context (verified by capturing the model request), so the model sees <code>render_ui</code> without the guide. The page's own runtime — a TanStack <code>BuiltInAgent</code>, on the overview page — is shown there and not served.</p>
  </Callout>
  <Callout tone="info" title="Framework tabs"><p>This page is not under <code>/vue</code>: it prints each sample for React, Angular, React Native and Vue. Only the Vue tab (and code outside the tabs) is used.</p></Callout>
</template>
