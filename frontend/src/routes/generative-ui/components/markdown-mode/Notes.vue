<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
const D = "frontend/src/routes/generative-ui/components/markdown-mode/demo-chat";
</script>

<template>
  <RouteHeader path="/generative-ui/components/markdown-mode" />
  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">The agent writes UI inside its markdown reply, in <code>a2ui</code> code blocks, with no tool call; <code>sendContext: false</code> leaves the guide to your backend, which reads it from the run's forwarded props.</p>
    <div class="mt-4"><TryIt :prompts="['Give me a plan estimator with a seats slider']" expect="An interactive card from an a2ui block in the reply." fail="Plain text: the guide travels in context (or forwarded props with sendContext: false), and this agent receives neither." /></div>
  </Panel>
  <Panel title="Published files, mounted verbatim">
    <div class="space-y-4">
      <SourceCode :file="`${D}/App.vue`" note="Vue tab, verbatim: a provider with a slot." />
    </div>
  </Panel>
  <Panel title="Harness files">
    <div class="space-y-4">
      <SourceCode :file="`${D}/HarnessApp.vue`" note="Mounts App.vue with a CopilotChat in its slot." />
      <SourceCode :file="`${D}/no-context/HarnessApp.vue`" note="The published opening line with sendContext: false; imports, chat and closing tag added." />
    </div>
  </Panel>
  <Panel title="Published, not mounted">
    <div class="space-y-4">
      <PublishedCode page="ms-agent-harness-dotnet__generative-ui__components__markdown-mode" :index="0" note="What such a reply looks like." />
      <PublishedCode page="ms-agent-harness-dotnet__generative-ui__components__markdown-mode" :index="7" note="The envelope the provider sends in forwarded props." />
      <PublishedCode page="ms-agent-harness-dotnet__generative-ui__components__markdown-mode" :index="8" note="Backend fragment (Python): MY_PROMPT is never defined and no agent uses it — a gap." />
    </div>
  </Panel>
  <Callout tone="warn" title="Agent: the MS Agent Framework Quickstart agent (the ms-agent-py choice, same rules; README §9.9)">
    <p>The samples keep <code>runtime-url="/api/copilotkit"</code> as published, so <code>default</code> is the MS Agent Framework Quickstart agent. For a run that carries a catalog, the Copilot Runtime adds the <code>render_ui</code> tool to the run's tools and its guide (the components, their props, how to call the tool) to the run's context. This agent's adapter forwards the tools but not the context (verified by capturing the model request), so the model sees <code>render_ui</code> without the guide. The page's own runtime — a TanStack <code>BuiltInAgent</code>, on the overview page — is shown there and not served.</p>
  </Callout>
  <Callout tone="info" title="Framework tabs"><p>This page is not under <code>/vue</code>: it prints each sample for React, Angular, React Native and Vue. Only the Vue tab (and code outside the tabs) is used.</p></Callout>
</template>
