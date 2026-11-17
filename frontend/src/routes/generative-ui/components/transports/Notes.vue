<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
const D = "frontend/src/routes/generative-ui/components/transports/demo-chat";
</script>

<template>
  <RouteHeader path="/generative-ui/components/transports" />
  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">How generated UI travels: the default <code>render_ui</code> tool, or <code>transport: 'markdown'</code> (the agent writes a2ui code blocks in its reply), and limiting generative UI to some agents with <code>agentIds</code>.</p>
    <div class="mt-4"><TryIt :prompts="['Compare three plans in a table']" expect="Tool: a component via render_ui. Markdown: a component from an a2ui block in the reply. agentIds ['shop']: plain text, since the chat's agent is default." fail="Tool: as the agent note. Markdown: plain text — this transport sends only the guide, in context, which this agent never receives." /></div>
  </Panel>
  <Panel title="Harness wrappers around the published provider lines">
    <div class="space-y-4">
      <SourceCode :file="`${D}/tool/HarnessApp.vue`" note="Opening provider line verbatim; imports, chat and closing tag added." />
      <SourceCode :file="`${D}/markdown/HarnessApp.vue`" note="Same." />
      <SourceCode :file="`${D}/agent-ids/HarnessApp.vue`" note="Same. No agent is registered as shop." />
    </div>
  </Panel>
  <Panel title="Published, not mounted">
    <div class="space-y-4">
      <PublishedCode page="ms-agent-harness-dotnet__generative-ui__components__transports" :index="4" note="A runtime option (generativeUI: true), printed as a Next route; the harness runtime is unchanged." />
    </div>
  </Panel>
  <Callout tone="warn" title="Agent: the MS Agent Framework Quickstart agent (the ms-agent-py choice, same rules; README §9.9)">
    <p>The samples keep <code>runtime-url="/api/copilotkit"</code> as published, so <code>default</code> is the MS Agent Framework Quickstart agent. For a run that carries a catalog, the Copilot Runtime adds the <code>render_ui</code> tool to the run's tools and its guide (the components, their props, how to call the tool) to the run's context. This agent's adapter forwards the tools but not the context (verified by capturing the model request), so the model sees <code>render_ui</code> without the guide. The page's own runtime — a TanStack <code>BuiltInAgent</code>, on the overview page — is shown there and not served.</p>
  </Callout>
  <Callout tone="info" title="Framework tabs"><p>This page is not under <code>/vue</code>: it prints each sample for React, Angular, React Native and Vue. Only the Vue tab (and code outside the tabs) is used.</p></Callout>
</template>
