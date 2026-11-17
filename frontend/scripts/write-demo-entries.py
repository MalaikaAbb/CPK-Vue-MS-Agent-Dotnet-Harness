"""[harness] Writes each route's demo-chat/Demo.vue from one table, so every demo route has the same shape."""
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "routes")
T = "/api/copilotkit-threads"
# route path → (subtitle, [(id, label, import path relative to demo-chat/, wrap-with-HarnessProvider runtime url or None)])
DEMOS = {
  "/quickstart": ("CopilotChat · default", [("app", "src/App.vue", "./App.vue", None)]),
  "/prebuilt-components": ("CopilotChat · my-agent", [("app", "App.vue", "./App.vue", None)]),
  "/custom-look-and-feel/slots": (None, [
    ("welcome-screen", "Welcome screen slot · SupportChat.vue", "./welcome-screen/SupportChat.vue", "/api/copilotkit"),
    ("assistant-message", "Assistant message slot · SupportChat.vue", "./assistant-message/SupportChat.vue", "/api/copilotkit"),
    ("disclaimer", "Disclaimer slot", "./disclaimer/Disclaimer.vue", "/api/copilotkit"),
    ("tailwind", "Tailwind classes", "./tailwind/TailwindClasses.vue", "/api/copilotkit"),
    ("props-override", "Props override", "./props-override/PropsOverride.vue", "/api/copilotkit"),
    ("custom-components", "Custom components (stand-in)", "./custom-components/CustomComponents.vue", "/api/copilotkit"),
    ("two-levels", "Nested · two levels (stand-in)", "./two-levels/TwoLevels.vue", "/api/copilotkit"),
    ("three-levels", "Nested · three levels", "./three-levels/ThreeLevels.vue", "/api/copilotkit"),
    ("labels", "Labels", "./labels/Labels.vue", "/api/copilotkit"),
  ]),
  "/custom-look-and-feel/headless-ui": (None, [
    ("minimal", "Minimal · HeadlessChat.vue", "./minimal/App.vue", None),
    ("complete", "Complete · RenderedMessages.vue", "./complete/HarnessComplete.vue", None),
  ]),
  "/programmatic-control": (None, [
    ("with-chat", "AgentTrigger + CopilotChat (harness)", "./HarnessWithChat.vue", None),
    ("app", "src/App.vue (verbatim, no chat)", "./App.vue", None),
  ]),
  "/prebuilt-components/copilot-threads-drawer": (None, [
    ("basic", "Set up · src/App.vue", "./basic/App.vue", None),
    ("toolbar", "Own button · App.vue with a toolbar button", "./toolbar/App.vue", None),
    ("controlled", "Controlled · ControlledChat.vue", "./controlled/components/ControlledChat.vue", T),
    ("css-parts", "Own button only · CSS parts", "./css-parts/HarnessCssParts.vue", None),
    ("header-slot", "Customization · header slot", "./header-slot/HeaderSlot.vue", T),
    ("row-slot", "Customization · #row slot", "./row-slot/RowSlot.vue", T),
  ]),
  "/headless-threads": ("ThreadSidebar · my-agent", [("app", "src/App.vue", "./App.vue", None)]),
  "/frontend-tools": ("filter_incidents · default", [("app", "src/App.vue", "./App.vue", None)]),
  "/generative-ui/tool-based": ("show_weather · default", [("app", "src/App.vue", "./App.vue", None)]),
  "/generative-ui/tool-rendering": (None, [
    ("default", "Zero-config · useDefaultRenderTool()", "./default/App.vue", None),
    ("catch-all", "Custom catch-all · BrandedToolCard (stand-in)", "./catch-all/App.vue", None),
    ("per-tool", "Per-tool · get_weather + wildcard", "./per-tool/App.vue", None),
  ]),
  "/generative-ui/state-rendering": ("ResearchProgress · researcher", [("app", "src/App.vue", "./App.vue", None)]),
  "/generative-ui/mcp-apps": (None, [
    ("default", "src/App.vue", "./default/App.vue", None),
    ("trusted", "Trusted widget configuration", "./trusted/App.vue", None),
  ]),
  "/shared-state": ("SharedWorkspace · workspace", [("app", "src/App.vue", "./App.vue", None)]),
  "/shared-state/rendering-in-app": ("Canvas · default", [("app", "src/App.vue", "./App.vue", None)]),
  "/shared-state/streaming": ("StreamingDocument · writer", [("app", "src/App.vue", "./App.vue", None)]),
  "/shared-state/agent-readonly": ("WorkspaceContext · default", [("app", "src/App.vue", "./App.vue", None)]),
  "/human-in-the-loop": ("schedule_meeting · default", [("app", "MeetingApproval.vue + harness chat", "./HarnessApp.vue", None)]),
  "/human-in-the-loop/useInterrupt": ("ApprovalPanel · default", [("app", "src/App.vue", "./App.vue", None)]),
  "/human-in-the-loop/headless": ("HeadlessInterruptPanel (stand-in)", [("app", "src/App.vue", "./App.vue", None)]),
  "/human-in-the-loop/governed-actions": ("approve_governed_action · default", [("app", "src/App.vue", "./App.vue", None)]),
  # User's choice: the WebMCP demo shows only the stand-in sample. The verbatim
  # OrderSearch.vue / webmcp.ts are on the notes page, not mounted on their own.
  "/webmcp": ("OrderSearch.vue + searchOrders stand-in", [
    ("use-frontend-tool-standin", "OrderSearch.vue + searchOrders stand-in", "./HarnessUseFrontendToolStandIn.vue", None),
  ]),
  # ── Generative UI › Components (pages outside /vue; Vue tab only) ──
  "/generative-ui/components": ("standardUI · default", [("app", "src/App.vue", "./App.vue", None)]),
  "/generative-ui/components/catalogs": ("shopUI · default", [("app", "Provider + shopUI (harness chat)", "./HarnessApp.vue", None)]),
  "/generative-ui/components/surfaces": ("featured surface · default", [("app", "Providers + FeaturedProducts (harness page)", "./HarnessApp.vue", None)]),
  "/generative-ui/components/standard-catalog": (None, [
    ("standard", "standardUI provider (harness chat)", "./HarnessApp.vue", None),
    ("override", "Card → MyCard override (harness provider)", "./override/HarnessOverride.vue", None),
  ]),
  "/generative-ui/components/state-and-actions": ("shopUI functions + events · default", [("app", "shopUI + ProductCard (harness provider)", "./HarnessApp.vue", None)]),
  "/generative-ui/components/theming": ("themed standardUI · default", [("app", "Theme provider (harness chat)", "./HarnessApp.vue", None)]),
  "/generative-ui/components/transports": (None, [
    ("tool", "render_ui tool (default)", "./tool/HarnessApp.vue", None),
    ("markdown", "transport: 'markdown'", "./markdown/HarnessApp.vue", None),
    ("agent-ids", "agentIds: ['shop']", "./agent-ids/HarnessApp.vue", None),
  ]),
  "/generative-ui/components/markdown-mode": (None, [
    ("app", "src/App.vue (harness chat in its slot)", "./HarnessApp.vue", None),
    ("no-context", "sendContext: false", "./no-context/HarnessApp.vue", None),
  ]),
  "/generative-ui/components/from-a2ui": ("appUI (After) · default", [("after", "After · appUI provider", "./HarnessApp.vue", None)]),
}
for path, (subtitle, variants) in DEMOS.items():
    lines = ['<script setup lang="ts">',
             "// [harness] Demo entry for this route: mounts the doc page's own files, listed on the notes page."]
    needs_wrap = any(v[3] for v in variants)
    # Samples load lazily: a sample's module (and any side effect on import, such as
    # WebMCP's webmcp.ts registering a tool) runs only when that sample is chosen.
    lines.append('import { defineAsyncComponent } from "vue";')
    lines.append("")
    lines.append('import VariantDemo from "@/components/harness/VariantDemo.vue";')
    if needs_wrap:
        lines.append('import { withHarnessProvider } from "@/lib/harness-mount";')
    for i, (_id, _label, imp, _wrap) in enumerate(variants):
        lines.append(f'const V{i} = defineAsyncComponent(() => import("{imp}"));')
    lines.append("")
    lines.append("const variants = [")
    for i, (vid, label, _imp, wrap) in enumerate(variants):
        comp = f'withHarnessProvider(V{i}{", " + repr(wrap).replace(chr(39), chr(34)) if wrap != "/api/copilotkit" else ""})' if wrap else f"V{i}"
        lines.append(f'  {{ id: "{vid}", label: "{label}", component: {comp} }},')
    lines.append("];")
    lines.append("</script>")
    lines.append("")
    sub = f' subtitle="{subtitle}"' if subtitle else ""
    lines.append(f'<template><VariantDemo parent-path="{path}"{sub} :variants="variants" /></template>')
    out = os.path.join(ROOT, path.lstrip("/"), "demo-chat", "Demo.vue")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write("\n".join(lines) + "\n")
print(len(DEMOS), "demo entries")
