<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
</script>

<template>
  <RouteHeader path="/human-in-the-loop/useInterrupt" />
  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      <code>useInterrupt({ renderInChat: false })</code> exposes <code>slotProps</code> with the primary interrupt and
      <code>resolve</code>/<code>cancel</code>; <code>ApprovalPanel</code> renders it outside the transcript.
    </p>
    <div class="mt-4">
      <TryIt :prompts="['Book the meeting']" expect="If the agent interrupted: an Approve / Cancel panel; Approve resumes the run." fail="What actually happens here: the chat answers and the panel never appears." />
    </div>
  </Panel>
  <Panel title="Published files, mounted verbatim">
    <div class="space-y-4">
      <SourceCode file="frontend/src/routes/human-in-the-loop/useInterrupt/demo-chat/components/ApprovalPanel.vue" />
      <SourceCode file="frontend/src/routes/human-in-the-loop/useInterrupt/demo-chat/App.vue" />
    </div>
  </Panel>
  <Panel title="Published, not mounted"><PublishedCode page="human-in-the-loop__useInterrupt" :index="2" note="Fragment: reads slotProps from a useInterrupt call it does not print." /></Panel>
  <Callout tone="warn" title="Why no interrupt can fire (README §9.5)"><p><code>useInterrupt</code> reacts to a run that finishes with <code>outcome.type === "interrupt"</code> (or a legacy <code>on_interrupt</code> event). The MS Agent Framework Quickstart agent never raises one, and no Vue page publishes an MS Agent Framework agent that does.</p></Callout>
  <Callout tone="harness" title="What the harness added">
    <p>· <strong>MeetingChat.vue</strong> — App.vue imports it and the page never publishes it, so App.vue cannot compile without one. Stand-in: the page's ApprovalPanel above a CopilotChat.</p>
  </Callout>
  <Panel title="Harness stand-in"><SourceCode file="frontend/src/routes/human-in-the-loop/useInterrupt/demo-chat/components/MeetingChat.vue" /></Panel>
</template>
