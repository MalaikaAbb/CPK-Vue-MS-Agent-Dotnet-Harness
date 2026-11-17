import { HttpAgent } from "@ag-ui/client";

/**
 * Agents for every runtime in this repo.
 *
 * `myAgent()` is the agent the Microsoft Agent Framework (.NET) landing page registers
 * (https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet — its only code block),
 * verbatim: an AG-UI HttpAgent pointed at AGENT_URL, where the MS Agent
 * Framework (.NET) Quickstart's ASP.NET Core app (agent/Program.cs:
 * OpenAIClient → AsAIAgent, MapAGUIServer("/", agent)) serves the agent.
 *
 * [harness] Doc agent ids. The landing page registers only `my_agent`, while
 * the Vue samples use `default` (no agent-id) and ids no page registers. By the
 * user's rules a page's own published agent would run under its id if it were
 * complete — but no page backend can run here: Tool Rendering prints no
 * backend for this framework, and Sub-agents' SubagentsAgent.cs is printed
 * truncated, with no host.
 * So every id is the landing page's my_agent, unchanged. The Generative UI ›
 * Components samples also use `default` (the user's choice).
 */
export function myAgent() {
  // Verbatim from the landing page's runtime route.
  return new HttpAgent({ url: process.env.AGENT_URL! });
}

/** Doc agent ids, and the page each one comes from. */
export const DOC_AGENT_IDS = {
  default: "no agent-id: Quickstart, Slots, Frontend Tools, Components as Tools, …",
  "my-agent": "Prebuilt Components, Headless UI, Headless Threads",
  sales: "Programmatic Control",
  support: "Threads Drawer",
  researcher: "State Rendering",
  workspace: "Shared State",
  writer: "State Streaming",
} as const;

export function docAgents() {
  return Object.fromEntries(Object.keys(DOC_AGENT_IDS).map((id) => [id, myAgent()]));
}
