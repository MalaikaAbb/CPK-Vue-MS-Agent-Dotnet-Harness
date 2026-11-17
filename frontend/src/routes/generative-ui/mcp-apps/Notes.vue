<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
</script>

<template>
  <RouteHeader path="/generative-ui/mcp-apps" />
  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      <code>mcpApps.servers</code> on the runtime; no frontend code beyond <code>CopilotChat</code>. When the agent calls a tool that has an
      MCP UI resource, the middleware fetches it and the built-in renderer draws it as a sandboxed iframe. The second sample adds
      <code>:mcp-apps="{ allowSameOriginFallback: true }"</code>.
    </p>
    <div class="mt-4">
      <TryIt :prompts="['What time is it on the server?']" expect="A get-time tool call followed by an inline iframe app from the MCP server." fail="Plain text — the MCP server on :3101 is not running (cd backend && npm run mcp:apps), or the run errors naming 3101." />
    </div>
  </Panel>
  <Panel title="The demo">
    <div class="space-y-4">
      <SourceCode file="frontend/src/routes/generative-ui/mcp-apps/demo-chat/default/App.vue" />
      <SourceCode file="frontend/src/routes/generative-ui/mcp-apps/demo-chat/trusted/App.vue" />
    </div>
  </Panel>
  <Panel title="The runtime — server.ts as published, and as mounted">
    <div class="space-y-4">
      <PublishedCode page="generative-ui__mcp-apps" :index="0" />
      <SourceCode file="backend/runtimes/mcp-apps.ts" />
    </div>
  </Panel>
  <Panel title="Transport shapes, as published">
    <div class="space-y-4">
      <PublishedCode page="generative-ui__mcp-apps" :index="3" />
      <PublishedCode page="generative-ui__mcp-apps" :index="4" />
    </div>
  </Panel>
  <Callout tone="harness" title="What the harness changed">
    <p>· The published server URL <code>https://mcp.example.com/mcp</code> is a placeholder. It is replaced by the page's own HTTP example, <code>http://localhost:3101/mcp</code>, served by the official ext-apps example (<code>npm run mcp:apps</code> in backend/, <code>@modelcontextprotocol/server-basic-react</code>). <code>MCP_APPS_URL</code> overrides it.</p>
    <p>· Separate runtime at <code>/api/copilotkit-mcp-apps</code> (both App.vue <code>runtime-url</code>s changed, published value kept as a comment), because <code>mcpApps</code> applies to every agent on a runtime.</p>
    <p>· <code>agent</code> is never defined on the page; it is the MS Agent Framework Quickstart's agent (<code>agent/Program.cs</code>), reached through the landing page's <code>HttpAgent</code> <code>my_agent</code> (<code>backend/agents.ts</code>).</p>
  </Callout>
</template>
