# CopilotKit Vue + Microsoft Agent Framework Harness (.NET) Test Suite

A navigable, working test harness for CopilotKit's **Vue** frontend against a **Microsoft Agent Framework (.NET)** agent, as documented under the `ms-agent-harness-dotnet` doc tree. Each Vue doc page is a route that runs that page's own code, plus the nine Generative UI › Components pages.

| | |
|---|---|
| **Doc sync date** | Machine-maintained: `doc-snapshot/manifest.json` → `syncedAt` (baseline taken 2026-11-13, 31 pages: 22 Vue pages + 9 Components pages). |
| **CopilotKit packages** | `@copilotkit/vue` 1.87.0 · `@copilotkit/core` 1.87.0 · `@copilotkit/runtime` 1.87.0 · `@ag-ui/client` 1.0.2 (`HttpAgent`, the same copy the runtime uses) |
| **Agent Framework** | `Microsoft.Agents.AI.Hosting.AGUI.AspNetCore` 1.19.0-preview.260822.1 · `Microsoft.Agents.AI.OpenAI` 1.19.0 (both pinned by the Quickstart) · `Microsoft.Agents.AI` 1.19.0 · `Microsoft.Extensions.AI` 10.9.0 · `OpenAI` 2.10.0 · .NET SDK 10.0.115 (`net10.0`; the Quickstart asks for 9.0+) |
| **Frontend** | Vite 8.3 · Vue 3.5 · vue-router 5.5 · TypeScript 6.0 · Tailwind 4.3 (harness chrome only) · zod 3.25.76 · `chart.js` 4.6.1 · `maplibre-gl` 5.24.1 (Components page's install line) |
| **Build status** | No CI. `vite build` ✅. `vue-tsc` reports 9 errors, all in published doc code (§9.10). All 86 URLs (every route, demo and sample, including the nine Components routes) mounted in headless Chrome with **zero console or page errors**. The chain (runtime → `HttpAgent` → the verbatim .NET agent → OpenAI) was driven with a **fake** key: runs reached OpenAI and failed only with `401 invalid_api_key`. A scratch copy pointed at a local capture server showed the run's frontend tool reaching the model, and context and state not. **No route has been driven against a live model yet.** |

---

## 2. Overview

Microsoft Agent Framework is Microsoft's agent SDK (.NET and Python); this repo tracks the docs' `ms-agent-harness-dotnet` tree, whose Quickstart, landing runtime and 29 of 31 pages are identical (apart from the slug) to the `ms-agent-dotnet` tree; Tool Rendering and Sub-agents differ (§9.4). CopilotKit reaches it over AG-UI: `Microsoft.Agents.AI.Hosting.AGUI.AspNetCore`'s `MapAGUIServer` serves an `AIAgent` from an ASP.NET Core app, the Copilot Runtime registers an AG-UI `HttpAgent` pointed at it, and `@copilotkit/vue` renders the conversation, tools and generated UI.

This repo turns the Quickstart and the Basics, Generative UI, Interactivity and Agent capabilities sections of the Vue MS Agent Framework (.NET) sidebar (22 pages) into one navigable Vite app. It adds the nine **Generative UI › Components** pages, which are not under `/vue` and print each sample for React, Angular, React Native and Vue; only their Vue tab is used. Every route mounts the page's code verbatim, bugs included, and shows the exact files that run. Anything the harness added is marked **[harness]** in the file, in a pink **Harness** callout on the notes page, and, for stand-in components, with a **HARNESS STAND-IN** badge on screen.

Tracks: **<https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet>** and **<https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components>**

---

## 3. Architecture

```
Browser — Vite dev server · localhost:5173
  │  @copilotkit/vue/v2; each /<route>/demo-chat mounts that page's own App.vue
  │  runtime-url="/api/copilotkit…" ──► Vite proxy /api → :8200
  ▼
Node · backend/server.ts · localhost:8200
  │  Vue Quickstart's host: createServer + createCopilotNodeListener({ cors: true })
  │  MS Agent Framework landing page's runtime: my_agent = new HttpAgent({ url: AGENT_URL })
  │  /api/copilotkit           every doc agent id → my_agent (incl. the Components samples' `default`)
  │  /api/copilotkit-threads   Intelligence quickstart's runtime (if key set)  [harness: own path]
  │  /api/copilotkit-mcp-apps  MCP Apps' runtime (mcpApps.servers)            [harness: own path]
  ▼  AGENT_URL (AG-UI over HTTP)
.NET · agent/ (AGUIServer, ASP.NET Core) · localhost:8000   (dotnet run)
  │  MS Agent Framework Quickstart: OpenAIClient("gpt-6-luna").AsIChatClient()…AsAIAgent("MyAgent") → app.MapAGUIServer("/", agent)
  ▼
OpenAI                                    MCP Apps example server on :3101 (MCP Apps route only)
```

**Three processes.** The agent is **C# on ASP.NET Core**. The Copilot Runtime is **TypeScript on Node** (`tsx`). The frontend is Vite.

**Where each piece comes from.**
- **The Vue MS Agent Framework Quickstart redirects to a landing page.** Its `.md` is the Vue (built-in agent) Quickstart, which says to keep its Vue frontend steps and take "the runtime wiring" from your framework's quickstart. So `App.vue`, `main.ts` and the Node host come from the Vue Quickstart.
- **The landing page's only code block is the runtime**, published as a Next.js route: `agents: { my_agent: new HttpAgent({ url: process.env.AGENT_URL! }) }`. It's used verbatim, hosted in the Vue Quickstart's Node listener.
- **The agent** is the MS Agent Framework Quickstart's (`/ms-agent-harness-dotnet/quickstart`, linked as the landing page's guide): "Use an existing agent", .NET tab. That's `agent/Program.cs` verbatim, in the project the Quickstart's own commands create: `dotnet new web -n AGUIServer` (placed in `agent/`), its two `dotnet add package` lines, `dotnet user-secrets init`. It builds and runs as published.

### Agent ids

The landing page registers only `my_agent`. The Vue samples use `default` (no agent-id), `my-agent`, `sales`, `support`, `researcher`, `workspace` and `writer`, and every one is `my_agent` (`backend/agents.ts`). Neither published page backend can run (§9.4). The Components samples keep `runtime-url="/api/copilotkit"` as published, so they run on `default` too (the choice you made for ms-agent-py, applied here under the same rules; §9.9).

### What the adapter does (verified by capturing the model request)

- **Frontend tools:** the .NET AG-UI host forwards every tool in the run's `tools` to the model, so `useFrontendTool`, `useComponent`, `useHumanInTheLoop` and generative UI's `render_ui` reach the Quickstart agent with no change to `Program.cs`.
- **Not forwarded:** the run's `context` and `state`. A captured request (from a scratch copy pointed at a local capture server) with a context value and a state object carried neither. So read-only context, shared-state reads, and the generative UI guide (which the runtime puts in context) never reach the model.
- **Not provided:** backend tools, state writes and interrupts. The Quickstart agent has none, and no page publishes a usable one.

---

## 4. Prerequisites

| Requirement | Version | Notes |
|---|---|---|
| Node.js | **24.12+** (or 22.18+) | `create-vue`'s scaffold requires it. Developed on 24.16. |
| npm | 10+ | Developed on npm 12. |
| .NET SDK | **9.0+** (the Quickstart's `dotnet --version` check) | Developed on 10.0.115; `dotnet new web` targets `net10.0` there. |
| OpenAI API key | — | Required, in the agent's **user-secrets** (`OPENAI_API_KEY`). The agent uses `gpt-6-luna` as published. |
| CopilotKit Intelligence key | — | Optional, only for the two Threads routes. |

---

## 5. Setup

```bash
git clone <this-repo> ms-agent-dotnet-harness && cd ms-agent-dotnet-harness
cd agent && dotnet restore && dotnet user-secrets set OPENAI_API_KEY "<your-openai-api-key>" && cd ..
cd backend && npm install && cd ..
cd frontend && npm install && cd ..
cp .env.example backend/.env            # AGENT_URL is pre-filled
```

| File | Variable | What it does |
|---|---|---|
| agent user-secrets | `OPENAI_API_KEY` | **Required.** Read by `Program.cs` from `builder.Configuration` (user-secrets load under `dotnet run`'s Development profile; an environment variable also works). Startup fails with `Set OPENAI_API_KEY` without it. |
| `backend/.env` | `AGENT_URL` | **Required.** The landing page's `HttpAgent` URL: `http://localhost:8000/`. |
| `backend/.env` | `CPK_INTELLIGENCE_API_KEY` | Optional. Intelligence for the Threads runtime: `cd backend && npx copilotkit@latest login && npx copilotkit@latest project select`. |
| `backend/.env` | `APP_USER_ID` · `MCP_APPS_URL` · `PORT` · `COPILOTKIT_TELEMETRY_DISABLED` | Optional: fixed local Threads identity (default `local-user`), MCP server URL (default `http://localhost:3101/mcp`), runtime port (default 8200), telemetry opt-out. |

**Ports:** agent **8000** (hard-coded in the Quickstart's `Program.cs`: `app.Run("http://localhost:8000")`), runtime **8200**, frontend **5173** (`strictPort`), MCP Apps example **3101**.

---

## 6. Running the project

```bash
# 1 — MS Agent Framework agent (the Quickstart's command)
cd agent && dotnet run
```
Success: `Now listening on: http://localhost:8000`. **If port 8000 is taken:** `Program.cs` hard-codes it, so free the port (don't edit the file).

```bash
# 2 — Copilot Runtime
cd backend && npm run dev
```
Success:
```
Copilot Runtime listening at http://localhost:8200/api/copilotkit
  Agent: http://localhost:8000/
  + /api/copilotkit-threads  (sse)
  + /api/copilotkit-mcp-apps
```

```bash
# 3 — Vue app
cd frontend && npm run dev               # → http://localhost:5173/
```

Open **<http://localhost:5173>**. The landing page's **Connection** panel probes the runtime paths. **MCP Apps route only:** `cd backend && npm run mcp:apps`.

---

## 7. What to expect: walkthrough per section

Each route has a notes page (`/<route>`: notes, Try-it prompts with pass/fail, the exact source, unmounted samples as published, Harness and gap callouts) and a demo (`/<route>/demo-chat`; a **Sample** picker where a page has several samples).

### Getting Started
**`/quickstart`**: **Try:** `Hello! What can you do?` **Pass:** a streamed reply. **Fail:** connection refused or `RUN_ERROR` means the agent isn't running or `AGENT_URL` is wrong. A 401 means the `OPENAI_API_KEY` user-secret is wrong.

### Basics
**`/prebuilt-components`**, **`/custom-look-and-feel/headless-ui`**, **`/programmatic-control`**: chat against `my_agent`: a streamed reply. Headless UI streams into bare rows. Programmatic Control's default sample adds a chat (harness, on request). **`/custom-look-and-feel/slots`**: nine samples; the **Disclaimer** sample shows no disclaimer (doc bug, §9.11).
**`/prebuilt-components/copilot-threads-drawer`**, **`/headless-threads`**: need `CPK_INTELLIGENCE_API_KEY`. `/api/copilotkit-threads/info` should report `mode: "intelligence"`.
**`/frontend-tools`**: **Try:** `Only show sev1 incidents`. **Pass:** "Current filter" changes to `sev1` and the agent confirms.

### Generative UI
**`/generative-ui/tool-based`**: **Try:** `Show me the weather in Paris`. **Pass:** an inline WeatherCard.
**`/generative-ui/tool-rendering`**: **Expected now:** a prose answer, no card (no backend tool is published, §9.4).
**`/generative-ui/state-rendering`**: **Expected now:** "Idle" (no backend published).
**`/generative-ui/mcp-apps`**: needs `npm run mcp:apps`. **Try:** `What time is it on the server?` **Pass:** a tool call, then an inline iframe app.

### Generative UI › Components (Vue tab of the `/ms-agent-harness-dotnet/generative-ui/components` pages)
All run on `default`, the Quickstart agent, which gets the `render_ui` tool but not its guide (§9.9). So **expect prose, or at best a guessed `render_ui` call**, until a backend passes the guide.
**`/generative-ui/components`**: the overview's `App.vue` with the standard catalog. **Try:** `Compare the Starter, Team, and Enterprise plans in a table`. **Pass:** a table component in the chat.
**`/generative-ui/components/catalogs`**: your own catalog (`ProductGrid`, `ProductCard`). **Pass:** a grid of product cards.
**`/generative-ui/components/surfaces`**: a page target (`featured`) above the chat; its default content is a **stand-in** `ProductRow`. **Pass:** the agent replaces it with a ProductGrid.
**`/generative-ui/components/standard-catalog`**: standard catalog, and a sample that replaces `Card` with `MyCard`.
**`/generative-ui/components/state-and-actions`**: `ProductCard` with "Add to cart" (an `onAddToCart` event bound to an `addToCart` function). The handler sample needs `./cart-store`, which isn't published, so clicking takes the card's error path.
**`/generative-ui/components/theming`**: standard components in the amber accent and 10px radius.
**`/generative-ui/components/transports`**: tool, markdown and `agentIds: ['shop']` samples.
**`/generative-ui/components/markdown-mode`**: **Expected now:** plain text. Markdown mode sends only the guide, in context.
**`/generative-ui/components/from-a2ui`**: the "After" provider; `Airport` and `Arrow` are **stand-ins**.

### Interactivity
**`/shared-state`**: **Try:** **Prefer concise answers**. **Pass:** `preferences.tone` appears in the agent state (Inspector › State). The notes list stays empty (§9.3).
**`/shared-state/rendering-in-app`**: the Canvas shows "Project launch", but the agent can't read or edit it (§9.3).
**`/shared-state/streaming`**: **Expected now:** "Waiting for a draft…" (no backend published).
**`/shared-state/agent-readonly`**: **Expected now:** the agent doesn't know the workspace (§9.3).
**`/human-in-the-loop`**: **Try:** `Schedule a meeting about Q3 planning with Dana`. **Pass:** a time-picker card (flagged stand-in); picking a slot resumes the run.
**`/human-in-the-loop/governed-actions`**: **Try:** `Refund $40 to customer 1182. Call approve_governed_action first with id a-1, tool send_refund, reference POL-7, verdict require_approval.` **Pass:** an approval card.
**`/human-in-the-loop/useInterrupt`**, **`/human-in-the-loop/headless`**: **Expected now:** no interrupt (§9.5).
**`/webmcp`**: stand-in sample only (your choice). In Chrome 149+ with WebMCP, **Run tool** `searchOrders` `{"status":"open"}` returns ORD-1001 and ORD-1004.

### Agent capabilities
**`/multi-agent/subagents`**: notes only (§9.4).

---

## 8. Testing checklist / current status

| Doc page | Route | Status | Notes |
|---|---|---|---|
| `/vue/ms-agent-harness-dotnet` | `/` | 📖 Reference | Landing page. |
| `/vue/ms-agent-harness-dotnet` (Quickstart) | `/quickstart` | ✅ Working | `Program.cs` verbatim; chain verified with a fake key (OpenAI 401). |
| `prebuilt-components` | same | ✅ Working | Only `CopilotChat` has code. |
| `custom-look-and-feel/slots` | same | ⚠️ Partial | Imports added to fragments; 2 stand-ins; `labels` type error; disclaimer never renders (§9.10, §9.11). |
| `custom-look-and-feel/headless-ui` | same | ✅ Working | |
| `programmatic-control` | same | ✅ Working | Default sample adds a harness chat (on request). |
| `prebuilt-components/copilot-threads-drawer` | same | ⚠️ Partial | Intelligence quickstart runtime, fixed local identity; needs a key (§9.7). |
| `headless-threads` | same | ⚠️ Partial | Same runtime (§9.7). |
| `frontend-tools` | same | ✅ Working | Adapter forwards the tool (captured). Not yet run against a live model. |
| `generative-ui/tool-based` | same | ✅ Working | Same. |
| `generative-ui/tool-rendering` | same | ❌ Broken | The page prints no backend tool for this framework (§9.4). |
| `generative-ui/state-rendering` | same | ❌ Broken | No backend published. |
| `generative-ui/mcp-apps` | same | ⚠️ Partial | Needs `npm run mcp:apps`; placeholder URL replaced (§9.8). |
| `generative-ui/components` | same | ⚠️ Partial | `App.vue` verbatim + chart/map plugins; `render_ui` without its guide (§9.9). |
| `generative-ui/components/surfaces` | same | ⚠️ Partial | `ProductRow` stand-in; same agent limit. |
| `generative-ui/components/catalogs` | same | ⚠️ Partial | Provider line wrapped with a chat; same agent limit. |
| `generative-ui/components/standard-catalog` | same | ⚠️ Partial | Same agent limit. |
| `generative-ui/components/state-and-actions` | same | ⚠️ Partial | `./cart-store` never published; same agent limit. |
| `generative-ui/components/theming` | same | ⚠️ Partial | Same agent limit. |
| `generative-ui/components/transports` | same | ⚠️ Partial | Tool: same agent limit. Markdown: nothing reaches the model. |
| `generative-ui/components/markdown-mode` | same | ❌ Broken | The guide travels only in context (§9.9). |
| `generative-ui/components/from-a2ui` | same | ⚠️ Partial | `Airport`/`Arrow` stand-ins; same agent limit. |
| `shared-state` | same | ⚠️ Partial | Read + tone write-back; nothing writes `notes` (§9.3). |
| `shared-state/rendering-in-app` | same | ⚠️ Partial | Canvas renders; agent can't read or write it (§9.3). |
| `shared-state/streaming` | same | ❌ Broken | No backend published. |
| `shared-state/agent-readonly` | same | ❌ Broken | Context not forwarded (§9.3). |
| `human-in-the-loop` | same | ⚠️ Partial | Adapter forwards the tool; `TimePickerCard` stand-in. |
| `human-in-the-loop/useInterrupt` | same | ❌ Broken | No interrupting agent published; `MeetingChat.vue` stand-in (§9.5). |
| `human-in-the-loop/headless` | same | ❌ Broken | Same; `HeadlessInterruptPanel.vue` stand-in (§9.5). |
| `human-in-the-loop/governed-actions` | same | ⚠️ Partial | Tool half forwarded; interrupt half §9.5; `executeSideEffect` undefined. |
| `webmcp` | same | ⚠️ Partial | Stand-in sample only; as published every call errors (§9.6). |
| `multi-agent/subagents` | same | ❌ Broken | `SubagentsAgent.cs` is printed truncated, with no host; no Vue code (§9.4). |

**Legend:** ✅ Working · ⚠️ Partial · 📖 Reference · 🚧 Not started · ❌ Broken. "Working" means wired and verified from code, mounts and the captured run; **not yet driven against a live model.**

---

## 9. Known issues / doc-vs-implementation discrepancies

All against `@copilotkit/vue` / `@copilotkit/runtime` 1.87.0, `Microsoft.Agents.AI.Hosting.AGUI.AspNetCore` 1.19.0-preview.260822.1, `Microsoft.Agents.AI` 1.19.0, and the docs as of the 2026-11-13 baseline.

**1. The Quickstart is split across three pages.** `/vue/ms-agent-harness-dotnet/quickstart` redirects (307) to the landing page. The root `.md` is the built-in Vue Quickstart (`BuiltInAgent`), rendered on `/vue`. The landing page renders a single code block, the runtime route, which appears in no `.md`. The agent is on the non-Vue `/ms-agent-harness-dotnet/quickstart` "Use an existing agent" tab, which renders client-side (verified through `data-raw-code`). That tab offers .NET and Python; this repo uses .NET. Its `Program.cs` is printed with uneven indentation (most lines indented 24 spaces); it's kept as published, and C# doesn't mind.

**2. The .NET host reports model errors as HTTP 500.** When the model call fails (for example a bad key), `MapAGUIServer` answers `HTTP 500` with the exception text before any AG-UI event (no `RUN_STARTED`), rather than streaming a `RUN_ERROR`. The Copilot Runtime turns that into a `RUN_ERROR` whose message starts `HTTP 500: System.ClientModel.ClientResultException: HTTP 401 …`. Left as is.

**3. Context and state never reach the model.** A captured model request from the Quickstart agent (scratch copy with the OpenAI endpoint pointed at a local capture server) carried the run's frontend tool but neither its `context` nor its `state`. So:
- [Agent Read-Only Context](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/shared-state/agent-readonly) can't work. The page credits "the backend's CopilotKit middleware"; this agent has none.
- Shared State's tone write-back reaches the run's state but not the model.
- Render state in app's Canvas can't be read or edited by the agent.

**4. No page backend can run.**
- [Tool Rendering](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/generative-ui/tool-rendering)'s "The backend tool definition" section says the agent must expose `get_weather`, but prints no code for this framework. The page source carries the build note `snippet skipped: region 'weather-tool-backend' missing in ms-agent-harness-dotnet::tool-rendering`. So there's nothing to serve.
- [Sub-agents](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/multi-agent/subagents) prints `agent/SubagentsAgent.cs` twice (320 and 395 lines; the second contains the first). It defines a `SubagentsAgent` (`DelegatingAIAgent`), its store and a `SubagentsAgentFactory`. But even the full print is **truncated**: it stops partway through `CreateAgent()`, with 53 `{` against 51 `}`, so it can't compile. No page prints a host that maps it. "Rendering a live delegation log" publishes no Vue code.

The Sub-agents file isn't written to `agent/`, because the .NET SDK compiles every `.cs` file in the project folder; it's shown on its route. State Rendering, State Streaming and Shared State publish no backend at all. (The block catalog's path-comment rule covers `.cs`, so the C# blocks verify against the rendered pages.)

**5. Interrupts.** [Pausing the Agent for Input](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/human-in-the-loop/useInterrupt) publishes `ApprovalPanel.vue` and an `App.vue` that imports a `MeetingChat.vue` it never publishes. [Headless Interrupts](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/human-in-the-loop/headless) publishes only an `App.vue` that imports a never-published `HeadlessInterruptPanel.vue`. Both are flagged stand-ins (the files can't compile without them). No agent that interrupts is published, so no interrupt can fire.

**6. Undefined functions left undefined.** `searchOrders` (WebMCP: as published every call throws; the demo shows only a flagged stand-in sample, your choice), `executeSideEffect` (Governed Actions), the helpers in §9.4, and on the Components pages `useCartStore` (`./cart-store`) and `vueBasicCatalog`.

**7. Threads: Intelligence quickstart runtime.** Wired per the [Vue MS Agent Framework (.NET) Intelligence quickstart](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/intelligence/quickstart). Its `authenticateApplicationUser` is never defined; per that page's "a fixed identity is suitable only for a local, single-user demo", it returns `local-user` / "Local user" (flagged, **not authentication**). Without `CPK_INTELLIGENCE_API_KEY` the path is plain SSE, and the runtime logs that `GET /threads` returns 403. Restart the backend after `project select`. The Threads `App.vue` files use `/api/copilotkit-threads` (published value kept as a comment).

**8. MCP Apps.** The published server URL is a placeholder, replaced by the page's own `http://localhost:3101/mcp` example served by `npm run mcp:apps`. It runs on its own runtime path because `mcpApps` applies to every agent on a runtime; both `App.vue` `runtime-url`s are changed (labelled).

**9. Generative UI › Components.**
- **The pages.** The nine pages live under `/ms-agent-harness-dotnet/generative-ui/components`, not `/vue`, and print each sample in React, Angular, React Native and Vue tabs. Only the Vue tab and untabbed code are used; tab membership is read from the snapshot's `<Tab value="Vue">` markup.
- **The agent (the ms-agent-py choice, same rules).** The overview's Vue setup includes its own runtime: a TanStack `BuiltInAgent` (`@tanstack/ai`, `openaiText("gpt-6-luna")`, `convertInputToTanStackAI`). It's shown on the route and not served. The samples keep `runtime-url="/api/copilotkit"`, so they run on the MS Agent Framework Quickstart agent.
- **The guide never reaches the model.** For a run that carries a catalog, the Copilot Runtime's generative-UI middleware adds `render_ui` to the run's tools and its guide (components, props, how to call the tool) to the run's context (verified in `@copilotkit/runtime` 1.87.0's `generative-ui-middleware`). This adapter forwards tools but not context (§9.3), so the model gets `render_ui` without the guide. Markdown mode sends only the guide, so for it nothing reaches the model at all.
- **What the harness wrote, all flagged:**
  - Five pages print only an opening `<CopilotKitProvider …>` line (Catalogs, Transports ×3, Markdown mode's `sendContext: false`, Adopt from A2UI's "After"); the harness adds the imports, a `<CopilotChat />` and the closing tag.
  - Three pages print a provider component with a `<slot />` (Standard catalog, Theming, Markdown mode's `App.vue`); the harness puts a `<CopilotChat />` in the slot.
  - Surfaces, Standard catalog's override and State and actions get small harness pages that put the published pieces together.
  - Two modules printed without imports (State and actions' `shop-ui.ts`, Adopt from A2UI's `app-ui.ts`) get only their import lines.
  - Surfaces' `FeaturedProducts.vue` imports `../shop-ui`, which that page never prints, so the Catalogs page's `shop-ui.ts` (same `acme/shop@1`) and its two components are copied there, labelled.
  - The overview's plugin entry (`GenerativeUIChart`, `GenerativeUIMap`) is applied in the harness's `src/main.ts`, and `chart.js` and `maplibre-gl` are installed per the page.
- **Stand-ins (flagged):** `ProductRow` (Surfaces), `Airport` and `Arrow` (Adopt from A2UI).
- **Shown only:**
  - Catalogs' type-error demo and its `exportA2UICatalog` script;
  - Surfaces' recommendations sample (`Product` type never published);
  - State and actions' cart samples (`./cart-store` never published);
  - Theming's `index.html` dark-mode script, since it would affect every route;
  - Markdown mode's backend fragment (`MY_PROMPT` undefined);
  - Adopt from A2UI's "Before" (`vueBasicCatalog` undefined).

**10. Type errors** (`npm run type-check`, 9 errors), all in published doc code:
- the `labels` prop is typed as literal default strings;
- `useRenderTool`, `useDefaultRenderTool` and `useHumanInTheLoop` reject render components that declare only the props they use;
- `searchOrders` ×2;
- Surfaces' `FeaturedProducts.vue` imports `../product`, a type module no page publishes.

`npm run build` is `vite build`.

**11. Slots › Disclaimer never renders.** `CopilotChat`'s `#input` slot props don't include `showDisclaimer`, so the sample's `CopilotChatInput` never shows its `#disclaimer` slot. Left as published.

**12. Fragments, stand-ins and wrappers (Vue pages).** Slots' fragments get imports only, and "Three levels" is nested in "Two levels". Headless UI's `RenderedMessages.vue` is mounted with the minimal `HeadlessChat.vue` as its composer. Shared State's two `SharedWorkspace.vue` fragments are merged. Stand-ins: `TimePickerCard.vue`, `MeetingChat.vue`, `HeadlessInterruptPanel.vue`, `CustomMessageView`, `CustomToolbarAction`, `BrandedToolCard`, `searchOrders` (on request). `HarnessApp.vue` mounts HITL's `MeetingApproval` beside a chat. **Shown only:** `agent.subscribe`, the watch-sources line, Headless Threads' pagination, `toggleItem`, useInterrupt's multi-interrupt template, and Governed Actions' type and `handleApproval`.

**13. The harness itself.** There's no root `CopilotKitProvider`: each demo mounts its page's own `App.vue`. Doc sync runs as Vite dev-server middleware and diffs the `.md` of all 31 tracked pages, so changes to the landing runtime block or the MS Agent Framework Quickstart are invisible to it. `npm run doc-files` re-reads both live. The block-catalog builder reads both backtick and tilde fences and code the rendered page carries in RSC text chunks.

---

## 10. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `Set OPENAI_API_KEY` at agent startup | No key in user-secrets or the environment | `cd agent && dotnet user-secrets set OPENAI_API_KEY "<key>"`. |
| `dotnet` not found, or a framework-version error | .NET SDK missing or older than 9.0 | Install the .NET SDK (§4). |
| Connection refused, or `RUN_ERROR` naming the agent URL | Agent not running, or `AGENT_URL` unset | Start terminal 1; set `AGENT_URL` in `backend/.env`; restart the backend. |
| `RUN_ERROR "HTTP 404"` or `address already in use` | Another server holds port 8000 | Free port 8000 (`Program.cs` hard-codes it). |
| `RUN_ERROR "HTTP 500: … HTTP 401 (invalid_api_key)"` | Wrong `OPENAI_API_KEY` user-secret | Fix it and restart the agent (§9.2 explains the HTTP 500). |
| Components samples answer in prose | The guide isn't forwarded (§9.9) | Expected with this agent. |
| `Agent … not found` | Backend isn't this repo's `server.ts` | Run `backend/server.ts`. |
| Threads stay on "Loading threads…" | Runtime started before the key existed (SSE → 403) | Restart the backend; the startup line must say `(intelligence)`. |
| CORS error on `/quickstart` or `/generative-ui/components` | Those `App.vue` files call `:8200` directly | Keep `cors: true`. |
| `Port 5173 is in use` | Another harness's Vite | Stop it (one harness at a time on 5173/8200). |

---

## Doc drift detection

`/doc-sync` fetches the `.md` behind all 31 tracked pages, diffs each against `doc-snapshot/pages/`, replaces the snapshot, and ranks changes High/Medium/Low. Commit `pages/`, `manifest.json` and `CHANGELOG.md`; `reports/` is gitignored. **Regenerating the doc files:** `cd frontend && npm run doc-files` does three things:
- rebuilds the block catalog (snapshot pages, plus the MS Agent Framework Quickstart fetched live, every block checked against the rendered page);
- rewrites the verbatim doc files, `src/lib/published.json` and `agent/Program.cs` (`write-doc-files.py`);
- rewrites the Components routes' files (`write-genui-files.py`).

---

## 11. Project structure

```
ms-agent-py/
├── CLAUDE.md · PR_GUIDELINES.md · README.md · .env.example
├── doc-snapshot/                    # pages/*.md + manifest.json — doc-sync baseline (31 pages)
├── agent/                           # MS Agent Framework (.NET) — ASP.NET Core :8000 (dotnet run)
│   ├── Program.cs                   # ★ Quickstart agent, verbatim
│   ├── AGUIServer.csproj            # `dotnet new web -n AGUIServer` + the Quickstart's two packages + user-secrets id
│   └── Properties/ · appsettings*.json   # from `dotnet new web`, unchanged
├── backend/                         # Copilot Runtime, Node :8200
│   ├── server.ts                    # ★ Vue Quickstart host + landing runtime
│   ├── agents.ts                    # HttpAgent per doc agent id
│   └── runtimes/ threads.ts · mcp-apps.ts
└── frontend/                        # Vite + Vue 3
    ├── scripts/ build-doc-catalog.py ([harness] .cs path titles) · write-doc-files.py · write-genui-files.py · write-demo-entries.py
    └── src/ main.ts ([harness] chart/map plugins) · lib/nav-config.ts (★ routes + statuses) · routes/<doc path>/{Notes.vue, demo-chat/} · …
```

---

## 12. References

**Getting Started**: [Quickstart (landing)](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet) · [Vue Quickstart (frontend steps)](https://docs.copilotkit.ai/vue) · [MS Agent Framework Quickstart (agent)](https://docs.copilotkit.ai/ms-agent-harness-dotnet/quickstart)

**Basics**: [Prebuilt Components](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/prebuilt-components) · [Slots](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/custom-look-and-feel/slots) · [Headless UI](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/custom-look-and-feel/headless-ui) · [Programmatic Control](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/programmatic-control) · [Threads Drawer](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/prebuilt-components/copilot-threads-drawer) · [Headless Threads](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/headless-threads) · [Frontend Tools](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/frontend-tools)

**Generative UI**: [Components as Tools](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/generative-ui/tool-based) · [Tool Call Rendering](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/generative-ui/tool-rendering) · [State Rendering](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/generative-ui/state-rendering) · [MCP Apps](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/generative-ui/mcp-apps)

**Generative UI › Components**: [Components and surfaces](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components) · [Surfaces](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/surfaces) · [Catalogs](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/catalogs) · [Standard catalog](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/standard-catalog) · [State and actions](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/state-and-actions) · [Theming](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/theming) · [Transports](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/transports) · [Markdown mode](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/markdown-mode) · [Adopt from A2UI](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/from-a2ui)

**Interactivity**: [Shared State](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/shared-state) · [Render agent state in your app](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/shared-state/rendering-in-app) · [State Streaming](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/shared-state/streaming) · [Agent Read-Only Context](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/shared-state/agent-readonly) · [HITL Overview](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/human-in-the-loop) · [Pausing the Agent for Input](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/human-in-the-loop/useInterrupt) · [Headless Interrupts](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/human-in-the-loop/headless) · [Governed Action Approval UI](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/human-in-the-loop/governed-actions) · [WebMCP](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/webmcp)

**Agent capabilities**: [Sub-agents](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/multi-agent/subagents)

**Intelligence (Threads routes)**: [Connect Intelligence in 5 minutes](https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/intelligence/quickstart)
