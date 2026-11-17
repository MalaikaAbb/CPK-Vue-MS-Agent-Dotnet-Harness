<script setup lang="ts">
import { onMounted, ref } from "vue";
import { RouterLink } from "vue-router";

import DocDriftPanel from "@/components/doc-sync/DocDriftPanel.vue";
import Panel from "@/components/harness/Panel.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import TryIt from "@/components/harness/TryIt.vue";
import { DOCS_ROOT } from "@/lib/nav-config";

/** Agent id → agent (backend/agents.ts). Every id is the landing page's HttpAgent → the MS Agent Framework Quickstart agent. */
const AGENTS: [string, string, string][] = [
  ["default", "my_agent", "Quickstart, Slots, Frontend Tools, Components as Tools, Rendering in app, Agent Read-Only Context, HITL, useInterrupt, Headless Interrupts, Governed Actions, WebMCP"],
  ["my-agent", "my_agent", "Prebuilt Components, Headless UI, Headless Threads"],
  ["sales", "my_agent", "Programmatic Control"],
  ["support", "my_agent", "Threads Drawer"],
  ["researcher", "my_agent", "State Rendering"],
  ["workspace", "my_agent", "Shared State"],
  ["writer", "my_agent", "State Streaming"],
];

const RUNTIMES = ["/api/copilotkit", "/api/copilotkit-threads", "/api/copilotkit-mcp-apps"];
type Probe = { status: "pending" | "ok" | "error"; detail: string };
const probes = ref<Record<string, Probe>>(
  Object.fromEntries(RUNTIMES.map((r) => [r, { status: "pending", detail: "probing…" }])),
);

onMounted(() => {
  for (const base of RUNTIMES) {
    fetch(`${base}/info`, { cache: "no-store" })
      .then(async (res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const info = (await res.json()) as { mode?: string; agents?: Record<string, unknown> };
        probes.value[base] = {
          status: "ok",
          detail: `mode ${info.mode ?? "?"} · agents: ${Object.keys(info.agents ?? {}).join(", ")}`,
        };
      })
      .catch((error: unknown) => {
        probes.value[base] = {
          status: "error",
          detail: `${error instanceof Error ? error.message : String(error)} — is \`npm run dev\` running in backend/?`,
        };
      });
  }
});
</script>

<template>
  <RouteHeader path="/" />

  <DocDriftPanel />

  <Panel title="What this is">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      A working test harness for CopilotKit's <strong>Vue</strong> frontend (<code>@copilotkit/vue</code>) against a
      <strong>Microsoft Agent Framework (.NET)</strong> agent — an AG-UI <code>HttpAgent</code> in the Copilot Runtime, talking to the MS Agent Framework
      Quickstart's ASP.NET Core agent. Each
      route implements one Vue doc page using that page's code verbatim, and shows the exact source that runs. Anything the harness had
      to add is marked <span class="rounded bg-fuchsia-600 px-1.5 py-0.5 text-[10px] font-bold uppercase text-white">Harness</span>.
    </p>
    <p class="mt-3 text-sm">
      Docs tracked:
      <a :href="DOCS_ROOT" target="_blank" rel="noreferrer" class="text-[var(--accent)] underline underline-offset-4">{{ DOCS_ROOT }}</a>
    </p>
  </Panel>

  <Panel title="Connection" description="Probed from the browser, through the Vite proxy, against each runtime's /info.">
    <ul class="space-y-2 text-sm">
      <li v-for="(probe, base) in probes" :key="base" class="flex flex-wrap items-baseline gap-2">
        <span
          :class="[
            'inline-block h-2 w-2 rounded-full',
            probe.status === 'ok' ? 'bg-emerald-500' : probe.status === 'error' ? 'bg-rose-500' : 'bg-slate-400',
          ]"
        />
        <code class="font-mono text-xs">{{ base }}</code>
        <span class="text-xs text-slate-600 dark:text-slate-400">{{ probe.detail }}</span>
      </li>
    </ul>
  </Panel>

  <Panel
    title="Agent ids → agents"
    description="The landing page registers only `my_agent`. Vue samples use other ids; the two page backends cannot run, so each is my_agent."
  >
    <div class="overflow-x-auto">
      <table class="w-full min-w-[44rem] text-left text-sm">
        <thead>
          <tr class="border-b border-slate-200 text-xs uppercase tracking-wide text-slate-500 dark:border-slate-700">
            <th class="pb-2 pr-4 font-medium">Agent id</th>
            <th class="pb-2 pr-4 font-medium">Agent</th>
            <th class="pb-2 font-medium">Used by</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-100 dark:divide-slate-800">
          <tr v-for="[id, graph, used] in AGENTS" :key="id" class="align-top">
            <td class="py-2 pr-4 font-mono text-xs text-slate-800 dark:text-slate-100">{{ id }}</td>
            <td class="py-2 pr-4 font-mono text-xs text-slate-600 dark:text-slate-400">{{ graph }}</td>
            <td class="py-2 text-slate-600 dark:text-slate-400">{{ used }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </Panel>

  <Panel title="Start here">
    <TryIt
      :prompts="['What can you do?']"
      expect="On /quickstart → Open demo, a streamed reply rendered as markdown."
      fail="A RUN_ERROR — check the agent is running (agent/: dotnet run) and OPENAI_API_KEY is set in its user-secrets."
    />
    <p class="mt-3 text-sm text-slate-600 dark:text-slate-400">
      The <RouterLink to="/status" class="text-[var(--accent)] underline underline-offset-4">status overview</RouterLink> lists every route in one table.
    </p>
  </Panel>
</template>
