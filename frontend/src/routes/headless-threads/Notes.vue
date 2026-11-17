<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
</script>

<template>
  <RouteHeader path="/headless-threads" />

  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      <code>useThreads({ agentId: "my-agent" })</code> rendered by hand — select (<code>setActiveThreadId(id, { explicit: true })</code>),
      rename, archive, delete — beside <code>CopilotChat</code> in one <code>CopilotChatConfigurationProvider</code>.
    </p>
    <div class="mt-4">
      <TryIt
        :prompts="['Send “Hello”, then click the new thread', 'Rename / Archive / Delete a row']"
        expect="Rows appear after a thread's first run, sorted by recent activity; selecting one replays its history; Rename sets the name to “Renamed”."
        fail="“Loading…” forever or an empty list — check the Intelligence callout below (key set? Inspector shows “Intelligence connected”?)."
      />
    </div>
  </Panel>

  <Panel title="The demo">
    <div class="space-y-4">
      <SourceCode file="frontend/src/routes/headless-threads/demo-chat/components/ThreadSidebar.vue" />
      <SourceCode file="frontend/src/routes/headless-threads/demo-chat/App.vue" />
    </div>
  </Panel>

  <Panel title="The runtime — Headless Threads' server.ts as published (not mounted: its verifyAppSession is undefined), and the Intelligence-quickstart runtime that is">
    <div class="space-y-4">
      <PublishedCode page="headless-threads" :index="0" />
      <SourceCode file="backend/runtimes/threads.ts" />
    </div>
  </Panel>

  <Panel title="Published, not mounted" description="The pagination fragment calls useThreads with no import and renders only the Load-more button.">
    <PublishedCode page="headless-threads" :index="3" />
  </Panel>

  <Callout tone="harness" title="What the harness changed">
    <p>· <code>runtime-url</code> is <code>/api/copilotkit-threads</code> (published: <code>/api/copilotkit</code>, kept as a comment).</p>
  </Callout>
  <Callout tone="harness" title="Intelligence — wired per the Vue Intelligence quickstart (README §9.7)">
    <p>· The Threads runtime is the <a href="https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/intelligence/quickstart" target="_blank" rel="noreferrer" class="underline">Intelligence quickstart</a>'s TypeScript runtime, verbatim: a <code>CopilotKitIntelligence</code> client plus <code>identifyUser</code>.</p>
    <p>· Its <code>authenticateApplicationUser</code> is never defined; per that page (“a fixed identity is suitable only for a local, single-user demo”) it returns a fixed <code>local-user</code> / “Local user”, the page's own local-demo values. Not authentication.</p>
    <p>· Needs <code>CPK_INTELLIGENCE_API_KEY</code>: run <code>npx copilotkit@latest login</code> and <code>npx copilotkit@latest project select</code> inside <code>backend/</code> (writes <code>backend/.env</code>), restart the backend, and check that <code>/api/copilotkit-threads/info</code> reports <code>mode: "intelligence"</code>. Without the key it is a plain SSE runtime with no thread store.</p>
    <p>· The page's confirmation: Inspector → Home shows <strong>Intelligence connected</strong>; after one message the thread appears under <strong>Rich Threads</strong>.</p>
  </Callout>
</template>
