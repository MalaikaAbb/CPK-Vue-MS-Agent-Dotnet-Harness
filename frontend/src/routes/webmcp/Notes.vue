<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
</script>

<template>
  <RouteHeader path="/webmcp" />
  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      A frontend tool, <code>searchOrders</code>, mirrored onto <code>document.modelContext</code> with a read-only annotation through
      <code>useFrontendTool({ ..., webmcp })</code>. The demo has one sample: the page's <code>OrderSearch.vue</code>, verbatim, with a
      flagged <code>searchOrders</code> stand-in so calls succeed.
    </p>
    <div class="mt-4">
      <TryIt
        :prompts="['Open the demo in Chrome 149+ with chrome://flags/#enable-webmcp-testing on', 'DevTools › Application › WebMCP → Run tool searchOrders with status: open']"
        expect="The status line reads “present”; the panel lists one searchOrders with its description and readOnly flag; the call returns ORD-1001 and ORD-1004 as a JSON string."
        fail="searchOrders missing from the panel in a WebMCP-enabled browser, or a call error (Console shows the reason)."
      />
    </div>
  </Panel>
  <Panel title="Published files">
    <div class="space-y-4">
      <SourceCode file="frontend/src/routes/webmcp/demo-chat/OrderSearch.vue" note="Mounted verbatim in the demo." />
      <SourceCode file="frontend/src/routes/webmcp/demo-chat/webmcp.ts" note="Shown only — not mounted (the demo shows only the stand-in sample, by the user's choice)." />
    </div>
  </Panel>
  <Callout tone="warn" title="searchOrders is never defined (README §9.6)">
    <p>Both published samples call <code>searchOrders(status)</code>, which the page never defines. As published, every call throws <code>ReferenceError: searchOrders is not defined</code> (confirmed in Chrome); registration and discovery still work.</p>
  </Callout>
  <Callout tone="harness" title="What the harness added">
    <p>· <strong>searchOrders stand-in</strong> (on request): <code>search-orders.standin.ts</code> returns fixed sample orders filtered by <code>status</code> — no real data, no network. The published file is not edited: <code>WithSearchOrdersStandIn.vue</code> installs <code>searchOrders</code> as a browser global while the demo is mounted (what the bare <code>searchOrders(...)</code> resolves to at call time) and removes it on unmount. A pink HARNESS STAND-IN badge shows on screen.</p>
    <p>· <strong>Demo is the stand-in sample only</strong>, by the user's choice. The verbatim-only <code>OrderSearch.vue</code> and the <code>webmcp.ts</code> (<code>CopilotKitCore</code>) samples are not mounted.</p>
    <p>· OrderSearch.vue “must run inside your existing CopilotKitProvider”, which the page does not print — it is mounted under HarnessProvider.</p>
    <p>· A status line reporting whether <code>document.modelContext</code> exists (the page's test step 3).</p>
  </Callout>
  <Panel title="Harness files">
    <div class="space-y-4">
      <SourceCode file="frontend/src/routes/webmcp/demo-chat/search-orders.standin.ts" />
      <SourceCode file="frontend/src/routes/webmcp/demo-chat/WithSearchOrdersStandIn.vue" />
      <SourceCode file="frontend/src/routes/webmcp/demo-chat/HarnessUseFrontendToolStandIn.vue" />
      <SourceCode file="frontend/src/routes/webmcp/demo-chat/HarnessUseFrontendTool.vue" />
      <SourceCode file="frontend/src/routes/webmcp/demo-chat/ModelContextStatus.vue" />
    </div>
  </Panel>
</template>
