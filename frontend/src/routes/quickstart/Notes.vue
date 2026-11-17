<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
</script>

<template>
  <RouteHeader path="/quickstart" />

  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      The whole stack, assembled from the three places the docs put it: the Vue app from the Vue Quickstart (<code>App.vue</code> with
      <code>CopilotChat</code>), the runtime from the Microsoft Agent Framework (.NET) landing page (an AG-UI <code>HttpAgent</code> named <code>my_agent</code>
      pointed at <code>AGENT_URL</code>) hosted in the Vue Quickstart's Node <code>server.ts</code>, and the agent from the MS Agent Framework
      Quickstart (<code>Program.cs</code>: an OpenAI chat client turned into an agent with <code>AsAIAgent</code>, served by <code>app.MapAGUIServer("/", agent)</code> on ASP.NET Core). Three
      processes: the agent on :8000, the runtime on :8200, Vite on :5173.
    </p>
    <div class="mt-4">
      <TryIt
        :prompts="['Hello! What can you do?', 'Write a haiku about rivers.']"
        expect="A streamed reply from the MS Agent Framework agent; the Inspector's AG-UI Events show RUN_STARTED → TEXT_MESSAGE_* → RUN_FINISHED."
        fail="Connection refused or RUN_ERROR — the agent is not running on :8000 or AGENT_URL is unset; a 401 — OPENAI_API_KEY missing from the agent's user-secrets; “Set OPENAI_API_KEY” at startup — not set at all."
      />
    </div>
  </Panel>

  <Panel title="The demo" description="Verbatim src/App.vue from the Vue Quickstart, which the Microsoft Agent Framework (.NET) Vue Quickstart's .md is.">
    <SourceCode file="frontend/src/routes/quickstart/demo-chat/App.vue" />
  </Panel>

  <Panel title="The runtime, as published on the MS Agent Framework landing page" description="Its only code block — a Next.js route.">
    <PublishedCode page="index" :index="9" />
  </Panel>

  <Panel title="This repo's runtime" description="The Vue Quickstart's Node host with the landing page's agent registration; additions marked [harness].">
    <div class="space-y-4">
      <SourceCode file="backend/server.ts" />
      <SourceCode file="backend/agents.ts" />
    </div>
  </Panel>

  <Panel title="The agent — MS Agent Framework Quickstart, “Use an existing agent” › .NET" description="Program.cs verbatim, in the project the Quickstart's own commands create (dotnet new web -n AGUIServer, two dotnet add package lines, dotnet user-secrets init). Run with dotnet run.">
    <div class="space-y-4">
      <SourceCode file="agent/Program.cs" />
      <SourceCode file="agent/AGUIServer.csproj" />
    </div>
  </Panel>

  <Panel title="The Vue Quickstart's server.ts and main.ts, as published">
    <div class="space-y-4">
      <PublishedCode page="index" :index="4" note="Host only — its BuiltInAgent registration is replaced by the landing page's HttpAgent, as the Vue Quickstart itself instructs for an existing agent." />
      <PublishedCode page="index" :index="5" />
    </div>
  </Panel>

  <Callout tone="harness" title="How the three sources fit (README §3, §9.1)">
    <p>· <strong>The Vue Microsoft Agent Framework (.NET) Quickstart redirects to a landing page.</strong> Its .md is the built-in Vue Quickstart, which says: if you already have an agent, keep its Vue frontend steps and take the runtime wiring from your framework's quickstart.</p>
    <p>· <strong>The landing page</strong> publishes only the runtime route (<code>my_agent: new HttpAgent({ url: process.env.AGENT_URL! })</code>), as a Next.js route; a Vue app has no Next route, so it is hosted in the Vue Quickstart's Node listener.</p>
    <p>· <strong>The agent</strong> is from the MS Agent Framework Quickstart the landing page links as its guide: the “Use an existing agent” path, .NET tab — <code>gpt-6-luna</code> via <code>OpenAIClient</code> (reasoning effort “none”), made an agent named <code>MyAgent</code> (“You are a helpful assistant.”) and mapped with <code>MapAGUIServer("/", agent)</code> on <code>http://localhost:8000</code>.</p>
    <p>· The runtime also registers the doc agent ids (<code>backend/agents.ts</code>); each is <code>my_agent</code>.</p>
  </Callout>

  <Callout tone="info" title="What this agent can and cannot do (README §3)">
    <p>The .NET AG-UI host (<code>Microsoft.Agents.AI.Hosting.AGUI.AspNetCore</code>) forwards every CopilotKit frontend tool to the model, so frontend tools and HITL work with no change to <code>Program.cs</code>. It does not put the run's context or state into the model request (verified by capturing it), so read-only context and shared state are gaps. It has no backend tools and never interrupts.</p>
  </Callout>
</template>
