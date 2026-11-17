import {
  CopilotKitIntelligence,
  CopilotRuntime,
} from "@copilotkit/runtime/v2";

import { docAgents, myAgent } from "../agents";

/**
 * The runtime behind the two Threads routes (Threads Drawer, Headless
 * Threads), mounted at /api/copilotkit-threads.
 *
 * Built from the Vue Intelligence quickstart
 * (https://docs.copilotkit.ai/vue/ms-agent-harness-dotnet/intelligence/quickstart, TypeScript tab).
 * The block between the BEGIN/END markers is that page's runtime code,
 * verbatim. Everything outside the markers is [harness]:
 *
 * - `agents`: the page keeps "your existing agent registration". Here that is
 *   the landing page's `my_agent` plus the doc agent ids the Threads
 *   samples use (`support`, `my-agent` → my_agent; agents.ts).
 * - `authenticateApplicationUser`: the page calls it but leaves it to "your
 *   server-side authentication function". The page also says "a fixed
 *   identity is suitable only for a local, single-user demo" — which is what
 *   this is. The values are the page's own local-demo values from its native
 *   runtime tabs (`APP_USER_ID="local-user"`, name "Local user"). NOT FOR
 *   PRODUCTION: every caller is the same user.
 * - CopilotKitIntelligence throws at construction when the key is blank,
 *   which would take the whole server down. So the page's runtime is built
 *   only when CPK_INTELLIGENCE_API_KEY is set; otherwise this path serves a
 *   plain SSE runtime (no thread store), as the React harness does.
 * - It stays on its own base path, not /api/copilotkit, so no other route
 *   depends on Intelligence. Same precedent as the React harness's §9.49.
 *
 * Headless Threads publishes an older shape of this runtime whose
 * identifyUser calls an undefined `verifyAppSession`; it is shown on that
 * route as published, and no longer mounted.
 */
const agents = { my_agent: myAgent(), ...docAgents() }; // [harness]

/** [harness] Fixed local identity — see above. Not authentication. */
async function authenticateApplicationUser(
  _request: Request,
): Promise<{ id: string; name: string } | null> {
  return { id: process.env.APP_USER_ID || "local-user", name: "Local user" };
}

export const threadsMode = process.env.CPK_INTELLIGENCE_API_KEY
  ? "intelligence"
  : "sse";

function pageRuntime() {
  // ── BEGIN Intelligence quickstart · "Your CopilotKit runtime" (verbatim) ──
  // Create the Intelligence client with your project API key. Keep this key on the server.
  const intelligence = new CopilotKitIntelligence({
    apiKey: process.env.CPK_INTELLIGENCE_API_KEY!,
  });

  const runtime = new CopilotRuntime({
    agents,
    // Pass the Intelligence client to the runtime
    intelligence,
    // Identify the user from a verified session or token
    identifyUser: async (request) => {
      const user = await authenticateApplicationUser(request);
      if (!user) throw new Error("Unauthorized");
      return { id: user.id, name: user.name };
    },
  });
  // ── END Intelligence quickstart ───────────────────────────────────────────
  return runtime;
}

export function createThreadsRuntime(): CopilotRuntime {
  if (threadsMode === "intelligence") return pageRuntime();
  // [harness] No key: SSE fallback with the same agents and no Intelligence.
  return new CopilotRuntime({ agents });
}
