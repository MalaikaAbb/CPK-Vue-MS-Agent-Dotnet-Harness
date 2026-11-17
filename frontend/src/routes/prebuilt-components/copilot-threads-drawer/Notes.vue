<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
const D = "frontend/src/routes/prebuilt-components/copilot-threads-drawer/demo-chat";
</script>

<template>
  <RouteHeader path="/prebuilt-components/copilot-threads-drawer" />

  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      <code>CopilotThreadsDrawer</code> beside <code>CopilotChat</code>, both inside one <code>CopilotChatConfigurationProvider</code>
      (agent <code>support</code>), so the drawer drives the chat with no thread state of your own. Six samples in the picker: the setup,
      your own New-conversation button, an app-controlled <code>thread-id</code>, the CSS-parts rule, and the header / row slots.
    </p>
    <div class="mt-4">
      <TryIt
        :prompts="['(Set up) send “Hello”, then open the drawer', '(Own button) click New conversation']"
        expect="The new thread gets a row after its first run; selecting a row replays it; New conversation returns the chat to its welcome screen with no row selected."
        fail="A locked view (no Threads license) or an empty list — check the Intelligence callout below (key set? Inspector shows “Intelligence connected”?)."
      />
    </div>
  </Panel>

  <Panel title="Published files, mounted verbatim">
    <div class="space-y-4">
      <SourceCode :file="`${D}/basic/App.vue`" />
      <SourceCode :file="`${D}/toolbar/components/NewConversationButton.vue`" />
      <SourceCode :file="`${D}/toolbar/App.vue`" />
      <SourceCode :file="`${D}/controlled/components/ControlledChat.vue`" />
      <SourceCode :file="`${D}/css-parts/hide-new-thread.css`" />
      <SourceCode :file="`${D}/header-slot/HeaderSlot.vue`" note="Fragment; the imports are the only added lines." />
      <SourceCode :file="`${D}/row-slot/RowSlot.vue`" note="Fragment; the imports are the only added lines." />
    </div>
  </Panel>

  <Panel title="The runtime" description="The Vue Intelligence quickstart's runtime, mounted at /api/copilotkit-threads.">
    <SourceCode file="backend/runtimes/threads.ts" />
  </Panel>

  <Callout tone="harness" title="What the harness changed or added">
    <p>· <code>runtime-url</code> in both App.vue files is <code>/api/copilotkit-threads</code> instead of the published <code>/api/copilotkit</code> (kept as a comment), so the Intelligence runtime cannot break every other route — same as the React harness's §9.49.</p>
    <p>· <code>ControlledChat.vue</code> (“Render ControlledChat inside your CopilotKitProvider”) and the two slot fragments have no provider on the page; they are mounted under HarnessProvider pointed at the same runtime.</p>
    <p>· The CSS-parts rule is injected only while its sample is open (<code>HarnessCssParts.vue</code>), on top of the toolbar sample the page pairs it with.</p>
    <p>· <code>public-license-key="ck_pub_..."</code> is kept verbatim — a placeholder.</p>
  </Callout>
  <Panel title="Harness wrapper"><SourceCode :file="`${D}/css-parts/HarnessCssParts.vue`" /></Panel>
  <Callout tone="harness" title="Intelligence — wired per the Vue Intelligence quickstart (README §9.7)">
    <p>· The Threads runtime is the <a href="https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/intelligence/quickstart" target="_blank" rel="noreferrer" class="underline">Intelligence quickstart</a>'s TypeScript runtime, verbatim: a <code>CopilotKitIntelligence</code> client plus <code>identifyUser</code>.</p>
    <p>· Its <code>authenticateApplicationUser</code> is never defined; per that page (“a fixed identity is suitable only for a local, single-user demo”) it returns a fixed <code>local-user</code> / “Local user”, the page's own local-demo values. Not authentication.</p>
    <p>· Needs <code>CPK_INTELLIGENCE_API_KEY</code>: run <code>npx copilotkit@latest login</code> and <code>npx copilotkit@latest project select</code> inside <code>backend/</code> (writes <code>backend/.env</code>), restart the backend, and check that <code>/api/copilotkit-threads/info</code> reports <code>mode: "intelligence"</code>. Without the key it is a plain SSE runtime with no thread store.</p>
    <p>· The page's confirmation: Inspector → Home shows <strong>Intelligence connected</strong>; after one message the thread appears under <strong>Rich Threads</strong>.</p>
  </Callout>
</template>
