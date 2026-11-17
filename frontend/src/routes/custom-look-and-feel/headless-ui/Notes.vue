<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
const D = "frontend/src/routes/custom-look-and-feel/headless-ui/demo-chat";
</script>

<template>
  <RouteHeader path="/custom-look-and-feel/headless-ui" />

  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      <strong>Minimal</strong>: a text-only message list and composer from <code>useAgent</code> + <code>useCopilotKit</code>, under the
      provider markup the page prints. <strong>Complete</strong>: the page's <code>RenderedMessages.vue</code>, which composes the public
      message leaves so tool, reasoning and activity content still render.
    </p>
    <div class="mt-4">
      <TryIt
        :prompts="['Write two sentences about otters']"
        expect="Minimal: unstyled <article> rows, “Thinking…” while running, Send disabled during the run. Complete: the same conversation drawn with CopilotKit's assistant/user bubbles inside .assistant-bubble / .user-bubble wrappers."
        fail="Nothing appears after Send — agent my-agent is not registered on the runtime."
      />
    </div>
  </Panel>

  <Panel title="Minimal example">
    <div class="space-y-4">
      <SourceCode :file="`${D}/minimal/HeadlessChat.vue`" />
      <SourceCode :file="`${D}/minimal/App.vue`" note="The page prints the provider markup without imports; the imports are the only added lines." />
    </div>
  </Panel>

  <Panel title="Complete example">
    <div class="space-y-4">
      <SourceCode :file="`${D}/complete/RenderedMessages.vue`" />
      <SourceCode :file="`${D}/complete/HarnessComplete.vue`" />
    </div>
  </Panel>

  <Callout tone="harness" title="What the harness added">
    <p>· Imports on the provider fragment.</p>
    <p>· <code>RenderedMessages.vue</code> has no composer and the page publishes no App.vue for it, so <code>HarnessComplete.vue</code> mounts it under the minimal example's providers with the published <code>HeadlessChat.vue</code> as its input.</p>
    <p>· Agent <code>my-agent</code> is the MS Agent Framework Quickstart's agent (<code>agent/Program.cs</code>), reached through the landing page's <code>HttpAgent</code> <code>my_agent</code> (<code>backend/agents.ts</code>).</p>
  </Callout>

  <Callout tone="warn" title="Doc notes">
    <p>· <code v-pre>{{ message.content }}</code> in HeadlessChat renders non-string content (content-part arrays) as JSON text; the page says the minimal example is text-only.</p>
  </Callout>
</template>
