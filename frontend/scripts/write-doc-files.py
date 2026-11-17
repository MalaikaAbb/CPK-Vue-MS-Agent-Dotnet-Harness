"""
[harness] Writes every doc sample this repo mounts, byte-for-byte from the
published page, so no doc code is ever retyped by hand.

Input: a blocks.json catalog — every fenced block from each Vue doc page's .md
export, dedented, with `[!code highlight]` markers stripped (the rendered page
strips them too), each flagged `rendered` if it appears on the rendered page.

Output:
  - src/routes/**           the verbatim files (published filenames)
  - src/lib/published.json  every block, for pages that show a sample as published

Only two transforms exist, both visible in the output file:
  - runtime_url: replaces the published runtime-url on routes whose runtime
    lives on its own base path, with the published value kept as a comment.
  - wrap: fragments printed without <script>/imports get a <script setup> of
    imports only, headed by a [harness] comment.
Usage: python3 -I scripts/write-doc-files.py <blocks.json>
"""
import json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src")
blocks = json.load(open(sys.argv[1]))

def code(page, i):
    b = blocks[page][i]
    assert b["rendered"], f"{page}[{i}] is not on the rendered page"
    return b["code"]

def write(rel, text):
    path = os.path.join(ROOT, "routes", rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text if text.endswith("\n") else text + "\n")

def runtime_url(text, new, why):
    old = 'runtime-url="/api/copilotkit"'
    assert text.count(old) == 1, "expected exactly one runtime-url"
    head, tail = text.split(old)
    line_start = head.rfind("\n", 0, head.rfind("<CopilotKitProvider")) + 1
    indent = head[line_start:len(head) - len(head.lstrip()) if False else line_start]
    tag_line = head[line_start:]
    ws = tag_line[: len(tag_line) - len(tag_line.lstrip())]
    note = f'{ws}<!-- [harness] published: runtime-url="/api/copilotkit" — {why} -->\n'
    return head[:line_start] + note + head[line_start:] + f'runtime-url="{new}"' + tail

def wrap(fragment, imports, why):
    return (
        '<script setup lang="ts">\n'
        f"// [harness] {why}\n"
        "// The page prints only the template below; these imports are the only added lines.\n"
        + "".join(f"{line}\n" for line in imports)
        + "</script>\n\n<template>\n"
        + fragment.rstrip("\n")
        + "\n</template>\n"
    )

V2 = '"@copilotkit/vue/v2"'

# ── Quickstart ───────────────────────────────────────────────────────────────
write("quickstart/demo-chat/App.vue", code("index", 6))

# ── Basics ───────────────────────────────────────────────────────────────────
write("prebuilt-components/demo-chat/App.vue", code("prebuilt-components", 0))

S = "custom-look-and-feel/slots/demo-chat"
write(f"{S}/welcome-screen/SupportChat.vue", code("custom-look-and-feel__slots", 0))
write(f"{S}/assistant-message/SupportChat.vue", code("custom-look-and-feel__slots", 1))
frag = "Printed under “{}” on the Slots page."
write(f"{S}/disclaimer/Disclaimer.vue", wrap(code("custom-look-and-feel__slots", 2),
      [f"import {{ CopilotChat, CopilotChatInput }} from {V2};"], frag.format("Disclaimer slot")))
write(f"{S}/tailwind/TailwindClasses.vue", wrap(code("custom-look-and-feel__slots", 3),
      [f"import {{ CopilotChat, CopilotChatMessageView }} from {V2};"], frag.format("Tailwind Classes")))
write(f"{S}/props-override/PropsOverride.vue", wrap(code("custom-look-and-feel__slots", 4),
      [f"import {{ CopilotChat, CopilotChatMessageView }} from {V2};"], frag.format("Props Override")))
write(f"{S}/custom-components/CustomComponents.vue", wrap(code("custom-look-and-feel__slots", 5),
      [f"import {{ CopilotChat }} from {V2};",
       'import CustomMessageView from "./CustomMessageView.vue"; // [harness] stand-in — never published'],
      frag.format("Custom Components")))
write(f"{S}/two-levels/TwoLevels.vue", wrap(code("custom-look-and-feel__slots", 6),
      [f"import {{ CopilotChat, CopilotChatAssistantMessage, CopilotChatMessageView }} from {V2};",
       'import CustomToolbarAction from "./CustomToolbarAction.vue"; // [harness] stand-in — never published'],
      frag.format("Two levels deep")))
# Three levels: the published fragment reads `assistantProps` from an enclosing
# slot it does not print. It is nested inside the two-levels fragment's
# `#assistant-message="assistantProps"` slot, replacing that fragment's own
# CopilotChatAssistantMessage — both pieces verbatim.
two = code("custom-look-and-feel__slots", 6)
three = code("custom-look-and-feel__slots", 7)
inner_start = two.index("        <CopilotChatAssistantMessage")
inner_end = two.index("</CopilotChatAssistantMessage>") + len("</CopilotChatAssistantMessage>")
three_indented = "\n".join(("        " + l) if l else l for l in three.rstrip("\n").split("\n"))
nested = two[:inner_start] + "        <!-- [harness] ↓ the Three-levels fragment, verbatim, inside the Two-levels slot it reads assistantProps from -->\n" + three_indented + two[inner_end:]
write(f"{S}/three-levels/ThreeLevels.vue", wrap(nested,
      [f"import {{ CopilotChat, CopilotChatAssistantMessage, CopilotChatMessageView }} from {V2};"],
      "Printed under “Three levels deep” on the Slots page, as a fragment that reads `assistantProps` from an enclosing slot it does not print; nested in the Two-levels fragment for that reason."))
write(f"{S}/labels/Labels.vue", wrap(code("custom-look-and-feel__slots", 8),
      [f"import {{ CopilotChat }} from {V2};"], frag.format("Labels")))

H = "custom-look-and-feel/headless-ui/demo-chat"
write(f"{H}/minimal/HeadlessChat.vue", code("custom-look-and-feel__headless-ui", 0))
write(f"{H}/minimal/App.vue", wrap(code("custom-look-and-feel__headless-ui", 1),
      [f"import {{ CopilotChatConfigurationProvider, CopilotKitProvider }} from {V2};",
       'import HeadlessChat from "./HeadlessChat.vue";'],
      "Printed under “Minimal example” as the provider markup for HeadlessChat."))
write(f"{H}/complete/RenderedMessages.vue", code("custom-look-and-feel__headless-ui", 2))

write("programmatic-control/demo-chat/components/AgentTrigger.vue", code("programmatic-control", 0))
write("programmatic-control/demo-chat/App.vue", code("programmatic-control", 1))

T = "prebuilt-components/copilot-threads-drawer/demo-chat"
WHY_T = "the Threads runtime is mounted separately at /api/copilotkit-threads (README §9)"
write(f"{T}/basic/App.vue", runtime_url(code("prebuilt-components__copilot-threads-drawer", 0), "/api/copilotkit-threads", WHY_T))
write(f"{T}/toolbar/components/NewConversationButton.vue", code("prebuilt-components__copilot-threads-drawer", 1))
write(f"{T}/toolbar/App.vue", runtime_url(code("prebuilt-components__copilot-threads-drawer", 2), "/api/copilotkit-threads", WHY_T))
write(f"{T}/controlled/components/ControlledChat.vue", code("prebuilt-components__copilot-threads-drawer", 3))
write(f"{T}/css-parts/hide-new-thread.css", code("prebuilt-components__copilot-threads-drawer", 4))
write(f"{T}/header-slot/HeaderSlot.vue", wrap(code("prebuilt-components__copilot-threads-drawer", 5),
      [f"import {{ CopilotThreadsDrawer }} from {V2};"], "Printed under “Customization › Named web-component slots”."))
write(f"{T}/row-slot/RowSlot.vue", wrap(code("prebuilt-components__copilot-threads-drawer", 6),
      [f"import {{ CopilotThreadsDrawer }} from {V2};"], "Printed under “Customization › Per-row content”."))

write("headless-threads/demo-chat/components/ThreadSidebar.vue", code("headless-threads", 1))
write("headless-threads/demo-chat/App.vue", runtime_url(code("headless-threads", 2), "/api/copilotkit-threads", WHY_T))

write("frontend-tools/demo-chat/components/DashboardAgent.vue", code("frontend-tools", 0))
write("frontend-tools/demo-chat/App.vue", code("frontend-tools", 1))

# ── Generative UI ────────────────────────────────────────────────────────────
G = "generative-ui/tool-based/demo-chat"
write(f"{G}/components/WeatherCard.vue", code("generative-ui__tool-based", 0))
write(f"{G}/components/AgentExperience.vue", code("generative-ui__tool-based", 1))
write(f"{G}/App.vue", code("generative-ui__tool-based", 2))

R = "generative-ui/tool-rendering/demo-chat"
app = code("generative-ui__tool-rendering", 5)   # no backend served for this page (gap, README §9)
write(f"{R}/default/components/AgentExperience.vue", code("generative-ui__tool-rendering", 0))
write(f"{R}/default/App.vue", app)
catch_all_line = code("generative-ui__tool-rendering", 1).rstrip("\n")
write(f"{R}/catch-all/components/AgentExperience.vue",
      '<script setup lang="ts">\n'
      "// [harness] The page prints only the one useDefaultRenderTool line below for this\n"
      "// file. The imports and <template> are the zero-config AgentExperience.vue's, and\n"
      "// BrandedToolCard is a stand-in — it is never published.\n"
      f"import {{ CopilotChat, useDefaultRenderTool }} from {V2};\n"
      'import BrandedToolCard from "./BrandedToolCard.vue"; // [harness] stand-in\n\n'
      f"{catch_all_line}\n"
      "</script>\n\n<template><CopilotChat /></template>\n")
write(f"{R}/catch-all/App.vue", app)
write(f"{R}/per-tool/components/WeatherToolCard.vue", code("generative-ui__tool-rendering", 2))
write(f"{R}/per-tool/components/AgentExperience.vue", code("generative-ui__tool-rendering", 3))
write(f"{R}/per-tool/App.vue", app)

write("generative-ui/state-rendering/demo-chat/components/ResearchProgress.vue", code("generative-ui__state-rendering", 0))
write("generative-ui/state-rendering/demo-chat/App.vue", code("generative-ui__state-rendering", 1))

WHY_M = "the MCP Apps runtime is mounted separately at /api/copilotkit-mcp-apps (README §9)"
write("generative-ui/mcp-apps/demo-chat/default/App.vue", runtime_url(code("generative-ui__mcp-apps", 1), "/api/copilotkit-mcp-apps", WHY_M))
write("generative-ui/mcp-apps/demo-chat/trusted/App.vue", runtime_url(code("generative-ui__mcp-apps", 2), "/api/copilotkit-mcp-apps", WHY_M))

# ── Interactivity
# ADK publishes neither MeetingChat.vue (useInterrupt) nor HeadlessInterruptPanel.vue
# (Headless Interrupts); both App.vue files import them, so flagged stand-ins
# (not written by this script) sit beside them. ────────────────────────────────────────────────────────────
a = code("shared-state", 0); b = code("shared-state", 1)
a_script, a_tmpl = a.split("</script>")
b_script, b_tmpl = b.split("</script>")
b_body = b_script.replace('<script setup lang="ts">\n', "", 1)
a_tmpl_inner = a_tmpl.strip().removeprefix("<template>").removesuffix("</template>").strip("\n")
b_tmpl_inner = b_tmpl.strip().removeprefix("<template>").removesuffix("</template>").strip("\n")
write("shared-state/demo-chat/components/SharedWorkspace.vue",
      "<!--\n  [harness] The Shared State page prints SharedWorkspace.vue in two fragments\n"
      "  (“Reading agent state”, then “Writing agent state”); the second has no imports\n"
      "  and uses `agent` from the first. They are merged here, each verbatim, in order.\n-->\n"
      + a_script.rstrip("\n") + "\n\n// ── [harness] second fragment of this file (“Writing agent state”) ──\n"
      + b_body.rstrip("\n") + "\n</script>\n\n<template>\n" + a_tmpl_inner
      + "\n  <!-- [harness] second fragment's template -->\n" + b_tmpl_inner + "\n</template>\n")
write("shared-state/demo-chat/App.vue", code("shared-state", 2))

write("shared-state/rendering-in-app/demo-chat/components/Canvas.vue", code("shared-state__rendering-in-app", 0))
write("shared-state/rendering-in-app/demo-chat/App.vue", code("shared-state__rendering-in-app", 1))
write("shared-state/streaming/demo-chat/components/StreamingDocument.vue", code("shared-state__streaming", 0))
write("shared-state/streaming/demo-chat/App.vue", code("shared-state__streaming", 1))
write("shared-state/agent-readonly/demo-chat/components/WorkspaceContext.vue", code("shared-state__agent-readonly", 0))
write("shared-state/agent-readonly/demo-chat/App.vue", code("shared-state__agent-readonly", 1))

write("human-in-the-loop/demo-chat/components/MeetingApproval.vue", code("human-in-the-loop", 0))
write("human-in-the-loop/useInterrupt/demo-chat/components/ApprovalPanel.vue", code("human-in-the-loop__useInterrupt", 1))
write("human-in-the-loop/useInterrupt/demo-chat/App.vue", code("human-in-the-loop__useInterrupt", 3))
write("human-in-the-loop/headless/demo-chat/App.vue", code("human-in-the-loop__headless", 0))

GA = "human-in-the-loop/governed-actions/demo-chat"
write(f"{GA}/components/GovernedActionApproval.vue", code("human-in-the-loop__governed-actions", 1))
write(f"{GA}/components/GovernedActionTool.vue", code("human-in-the-loop__governed-actions", 3))
write(f"{GA}/components/GovernedActionCard.vue", code("human-in-the-loop__governed-actions", 4))
write(f"{GA}/App.vue", code("human-in-the-loop__governed-actions", 5))

write("webmcp/demo-chat/OrderSearch.vue", code("webmcp", 0))
write("webmcp/demo-chat/webmcp.ts", code("webmcp", 1))

# ── MS Agent Framework (.NET) agent project (repo-root agent/) ──────────────
# agent/ is the project the Quickstart's "Use an existing agent" › .NET steps
# create (`dotnet new web -n AGUIServer`, two `dotnet add package` lines,
# `dotnet user-secrets init`); Program.cs is its published Program.cs,
# verbatim. The Vue pages' C# backends (Tool Rendering's agent/Program.cs,
# Sub-agents' agent/SubagentsAgent.cs) are NOT written: the .NET SDK compiles
# every .cs file under the project, and neither can be added as published
# (README §9). They are shown on their routes from published.json.
AGENT = os.path.join(ROOT, "..", "..", "agent")

def write_agent(rel, text):
    path = os.path.join(AGENT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text if text.endswith("\n") else text + "\n")

def qs(title, must):
    hits = [b for b in blocks["framework-quickstart"] if b["title"] == title and b["rendered"] and must in b["code"]]
    assert len(hits) == 1, f"expected one rendered {title} containing {must!r}, got {len(hits)}"
    return hits[0]["code"]

write_agent("Program.cs", qs("Program.cs", "MapAGUIServer"))

# ── Every block, for "as published" panels ───────────────────────────────────
with open(os.path.join(ROOT, "lib", "published.json"), "w") as f:
    json.dump(blocks, f, indent=1)
print("ok")
