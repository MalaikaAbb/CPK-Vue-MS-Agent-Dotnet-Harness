<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
</script>

<template>
  <RouteHeader path="/human-in-the-loop/headless" />
  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      Interrupts resolved from a panel with no chat mounted. The page publishes one file — the App.vue below — and describes the panel in
      prose only.
    </p>
    <div class="mt-4">
      <TryIt :prompts="['(nothing to type — there is no chat)']" expect="If something ran and interrupted: the pending interrupt and Resolve / Cancel." fail="What actually happens here: “No interrupt pending.” permanently." />
    </div>
  </Panel>
  <Panel title="Published file, mounted verbatim"><SourceCode file="frontend/src/routes/human-in-the-loop/headless/demo-chat/App.vue" /></Panel>
  <Callout tone="warn" title="Why no interrupt can fire (README §9.5)"><p><code>useInterrupt</code> reacts to a run that finishes with <code>outcome.type === "interrupt"</code> (or a legacy <code>on_interrupt</code> event). The MS Agent Framework Quickstart agent never raises one, and no Vue page publishes an MS Agent Framework agent that does.</p></Callout>
  <Callout tone="harness" title="What the harness added">
    <p>· <strong>HeadlessInterruptPanel.vue</strong> — imported by App.vue, never published. Stand-in: <code>useInterrupt({ renderInChat: false })</code> with resolve / cancel, as the page describes. Nothing on this route starts a run, so no interrupt can arrive even in principle.</p>
  </Callout>
  <Panel title="Harness stand-in"><SourceCode file="frontend/src/routes/human-in-the-loop/headless/demo-chat/components/HeadlessInterruptPanel.vue" /></Panel>
</template>
