<script setup lang="ts">
import Callout from "@/components/harness/Callout.vue";
import Panel from "@/components/harness/Panel.vue";
import PublishedCode from "@/components/harness/PublishedCode.vue";
import RouteHeader from "@/components/harness/RouteHeader.vue";
import SourceCode from "@/components/harness/SourceCode.vue";
import TryIt from "@/components/harness/TryIt.vue";
const D = "frontend/src/routes/generative-ui/tool-rendering/demo-chat";
</script>

<template>
  <RouteHeader path="/generative-ui/tool-rendering" />
  <Panel title="What it demonstrates">
    <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300">
      Three ways to draw a tool call — the built-in <code>*</code> renderer, a custom catch-all, and a per-tool <code>useRenderTool</code> for
      <code>get_weather</code> — for the page's backend tool, <code>get_weather</code>, which no served agent has (a gap, see below).
    </p>
    <div class="mt-4">
      <TryIt :prompts="['What is the weather in Tokyo?']" expect="Per-tool: “Checking Tokyo” while the call runs, then the city and the tool's JSON result (68°, Sunny). Zero-config: a status card with arguments and result. Catch-all: the BrandedToolCard stand-in." fail="What actually happens here: a prose answer with no card — default is the Quickstart agent, which has no get_weather (see the gap below)." />
    </div>
  </Panel>
  <Panel title="Published files, mounted verbatim">
    <div class="space-y-4">
      <SourceCode :file="`${D}/default/components/AgentExperience.vue`" />
      <SourceCode :file="`${D}/per-tool/components/WeatherToolCard.vue`" />
      <SourceCode :file="`${D}/per-tool/components/AgentExperience.vue`" />
      <SourceCode :file="`${D}/per-tool/App.vue`" note="The same published App.vue is copied into each variant directory, unchanged." />
    </div>
  </Panel>
  <Callout tone="warn" title="Gap: the page prints no backend tool (README §9.4)">
    <p>The page's “The backend tool definition” section says the agent must expose <code>get_weather</code>, but for this framework it prints no code: the page's source carries the build note “snippet skipped: region 'weather-tool-backend' missing in ms-agent-harness-dotnet::tool-rendering”. Per your rules nothing was written in its place. <code>default</code> is the Quickstart agent, which has no backend tools, so the renderers never see a <code>get_weather</code> call.</p>
  </Callout>
  <Panel title="Custom catch-all" description="The page prints only one line for this file.">
    <div class="space-y-4">
      <PublishedCode page="generative-ui__tool-rendering" :index="1" />
      <SourceCode :file="`${D}/catch-all/components/AgentExperience.vue`" />
      <SourceCode :file="`${D}/catch-all/components/BrandedToolCard.vue`" />
    </div>
  </Panel>
  <Panel title="Published, not mounted">
    <PublishedCode page="generative-ui__tool-rendering" :index="4" note="Fragment: `parameters` and `locale` are never declared." />
  </Panel>
  <Callout tone="harness" title="What the harness added">
    <p>· The catch-all <code>AgentExperience.vue</code> wraps the published line; <code>BrandedToolCard</code> is a stand-in — never published.</p>
  </Callout>
</template>
