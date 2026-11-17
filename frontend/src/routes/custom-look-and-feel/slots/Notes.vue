<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
const D = "frontend/src/routes/custom-look-and-feel/slots/demo-chat";
</script>

<template>
  <RouteHeader path="/custom-look-and-feel/slots" />

  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      Every sample on the Slots page, one per entry in the demo's <strong>Sample</strong> picker: the welcome-screen and assistant-message
      <code>SupportChat.vue</code> files, then the disclaimer, Tailwind, props-override, custom-component, two- and three-level nested, and
      labels fragments.
    </p>
    <div class="mt-4">
      <TryIt
        :prompts="['(welcome screen) click “Show my open tickets”', '(assistant message / two & three levels) say Hello', '(labels) look at the placeholder and disclaimer']"
        expect="Welcome: a custom card whose button sends the message. Assistant message: a “Reviewed” badge in each reply's toolbar. Disclaimer: nothing under the composer — a doc bug, see “Disclaimer slot never renders” below. Three levels: a “Copy response” button replaces the copy icon. Labels: the three custom strings."
        fail="A default chat with no change — the slot name did not bind."
      />
    </div>
  </Panel>

  <Panel title="Published files, mounted verbatim">
    <div class="space-y-4">
      <SourceCode :file="`${D}/welcome-screen/SupportChat.vue`" />
      <SourceCode :file="`${D}/assistant-message/SupportChat.vue`" />
    </div>
  </Panel>

  <Panel title="Published fragments, mounted with imports added" description="The page prints these as bare <CopilotChat> markup. Each file adds a <script setup> of imports only; the template is the fragment verbatim.">
    <div class="space-y-4">
      <SourceCode :file="`${D}/disclaimer/Disclaimer.vue`" />
      <SourceCode :file="`${D}/tailwind/TailwindClasses.vue`" />
      <SourceCode :file="`${D}/props-override/PropsOverride.vue`" />
      <SourceCode :file="`${D}/custom-components/CustomComponents.vue`" />
      <SourceCode :file="`${D}/two-levels/TwoLevels.vue`" />
      <SourceCode :file="`${D}/three-levels/ThreeLevels.vue`" />
      <SourceCode :file="`${D}/labels/Labels.vue`" />
    </div>
  </Panel>

  <Callout tone="warn" title="Disclaimer slot never renders (README §9)">
    <p>The published sample binds <code>v-bind="inputProps"</code> from <code>CopilotChat</code>'s <code>#input</code> slot. Those slot props do not include <code>showDisclaimer</code>, and <code>CopilotChatInput</code> only shows its disclaimer when <code>showDisclaimer</code> is true (unset, it falls back to <code>positioning === "absolute"</code>, which is false here). <code>CopilotChat</code>'s own default input passes <code>show-disclaimer</code> explicitly; the sample does not, so its <code>#disclaimer</code> slot is never rendered — the default disclaimer disappears too. Left as published; adding <code>show-disclaimer</code> to the sample's <code>CopilotChatInput</code> would be the fix.</p>
  </Callout>

  <Callout tone="harness" title="What the harness added">
    <p>· <strong>Imports</strong> on the seven fragments above — nothing else in those files.</p>
    <p>· <strong>Three levels deep</strong> reads <code>assistantProps</code> from an enclosing slot it does not print, so it sits inside the Two-levels fragment's <code>#assistant-message="assistantProps"</code> slot.</p>
    <p>· <strong>Stand-ins</strong> for two components the page uses but never defines: <code>CustomMessageView</code> and <code>CustomToolbarAction</code> (each shows a HARNESS STAND-IN badge).</p>
    <p>· <strong>Provider</strong>: no sample includes one, so each is mounted under HarnessProvider (<code>runtime-url="/api/copilotkit"</code>, agent <code>default</code>).</p>
  </Callout>
  <Panel title="Harness stand-ins">
    <div class="space-y-4">
      <SourceCode :file="`${D}/custom-components/CustomMessageView.vue`" />
      <SourceCode :file="`${D}/two-levels/CustomToolbarAction.vue`" />
      <SourceCode file="frontend/src/components/harness/HarnessProvider.vue" />
    </div>
  </Panel>
</template>
