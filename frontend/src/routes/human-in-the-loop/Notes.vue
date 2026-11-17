<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
</script>

<template>
  <RouteHeader path="/human-in-the-loop" />
  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      Pattern 1: <code>useHumanInTheLoop</code> registers <code>schedule_meeting</code>. When the model calls it, the render component gets a
      <code>respond</code> callback while the call is executing, and the run resumes with the user's answer as the tool result.
    </p>
    <div class="mt-4">
      <TryIt :prompts="['Schedule a meeting about Q3 planning with Dana']" expect="A card with topic and attendee and three time slots; picking one resumes the run and the agent confirms that time." fail="A prose answer and no card — the model answered without calling the tool, or TimePickerCard failed to render." />
    </div>
  </Panel>
  <Panel title="Published file, mounted verbatim"><SourceCode file="frontend/src/routes/human-in-the-loop/demo-chat/components/MeetingApproval.vue" /></Panel>
  <Callout tone="harness" title="What the harness added">
    <p>· <strong>TimePickerCard.vue</strong> — imported by the page, never published. Without it the tool has no UI and never calls <code>respond</code>. Minimal stand-in: three fixed slots (the page mentions “static candidate slots”), plus “None of these”.</p>
    <p>· <strong>HarnessApp.vue</strong> — the page prints no App.vue; this mounts MeetingApproval beside a CopilotChat under the standard provider.</p>
  </Callout>
  <Panel title="Harness files">
    <div class="space-y-4">
      <SourceCode file="frontend/src/routes/human-in-the-loop/demo-chat/components/TimePickerCard.vue" />
      <SourceCode file="frontend/src/routes/human-in-the-loop/demo-chat/HarnessApp.vue" />
    </div>
  </Panel>
  <Callout tone="info" title="Pattern 2"><p><code>useInterrupt</code> is on its own route, <a href="/human-in-the-loop/useInterrupt" class="underline">Pausing the Agent for Input</a>.</p></Callout>
  <Callout tone="info" title="Agent (README §3)"><p><code>default</code> is the MS Agent Framework Quickstart's agent. Its AG-UI adapter forwards the run's frontend tools to the model (verified by capturing the request), so <code>schedule_meeting</code> reaches it with no backend change.</p></Callout>
</template>
