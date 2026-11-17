<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
const D = "frontend/src/routes/generative-ui/components/theming/demo-chat";
</script>

<template>
  <RouteHeader path="/generative-ui/components/theming" />
  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">Standard components with your accent color, font and radius via a <code>GenerativeUITheme</code> on the provider.</p>
    <div class="mt-4"><TryIt :prompts="['Show a card with a primary button']" expect="Components use the amber accent (#d97706) and 10px radius." fail="A prose answer and no component: render_ui reached the model without its guide (see the agent note)." /></div>
  </Panel>
  <Panel title="Published files, mounted verbatim">
    <div class="space-y-4">
      <SourceCode :file="`${D}/Providers.vue`" note="Untitled provider component with a slot." />
    </div>
  </Panel>
  <Panel title="Harness wrapper">
    <div class="space-y-4">
      <SourceCode :file="`${D}/HarnessApp.vue`" note="Mounts Providers with a CopilotChat in its slot." />
    </div>
  </Panel>
  <Panel title="Published, not mounted">
    <div class="space-y-4">
      <PublishedCode page="ms-agent-harness-dotnet__generative-ui__components__theming" :index="5" note="The same theme as a module." />
      <PublishedCode page="ms-agent-harness-dotnet__generative-ui__components__theming" :index="9" note="index.html dark-mode script: not applied, it would change every harness route." />
    </div>
  </Panel>
  <Callout tone="warn" title="Agent: the MS Agent Framework Quickstart agent (the ms-agent-py choice, same rules; README §9.9)">
    <p>The samples keep <code>runtime-url="/api/copilotkit"</code> as published, so <code>default</code> is the MS Agent Framework Quickstart agent. For a run that carries a catalog, the Copilot Runtime adds the <code>render_ui</code> tool to the run's tools and its guide (the components, their props, how to call the tool) to the run's context. This agent's adapter forwards the tools but not the context (verified by capturing the model request), so the model sees <code>render_ui</code> without the guide. The page's own runtime — a TanStack <code>BuiltInAgent</code>, on the overview page — is shown there and not served.</p>
  </Callout>
  <Callout tone="info" title="Framework tabs"><p>This page is not under <code>/vue</code>: it prints each sample for React, Angular, React Native and Vue. Only the Vue tab (and code outside the tabs) is used.</p></Callout>
</template>
