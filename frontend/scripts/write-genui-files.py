"""
[harness] Writes the Generative UI › Components routes' files from the block
catalog (same catalog as write-doc-files.py).

These nine pages live outside /vue (https://docs.copilotkit.ai/ms-agent-harness-dotnet/
generative-ui/components/...) and print every sample in four framework tabs.
Only the Vue tab (and code outside any tab) is used. Every file is verbatim
except where a function below says otherwise:

  provider_line(...)  the page prints only an opening <CopilotKitProvider ...>
                      line; the harness adds the imports, a <CopilotChat />
                      inside it and the closing tag, nothing else.
  with_imports(...)   the page prints a .ts module without its imports; the
                      listed import lines are the only added lines.
  harness_chat(...)   the page prints a provider component with a <slot />;
                      the harness mounts it with a <CopilotChat /> in the slot.

Stand-ins for components the pages use but never publish (ProductRow,
Airport, Arrow) are hand-written, flagged files, not generated here.

Usage: python3 -I scripts/write-genui-files.py <catalog.json>
"""
import json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "routes", "generative-ui", "components")
blocks = json.load(open(sys.argv[1]))
P = "ms-agent-harness-dotnet__generative-ui__components"

def code(page, i, lang=None):
    key = P + ("__" + page if page else "")
    b = blocks[key][i]
    assert b["rendered"], (key, i)
    if lang: assert b["lang"] == lang, (key, i, b["lang"])
    return b["code"]

def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text if text.endswith("\n") else text + "\n")

V2 = '"@copilotkit/vue/v2"'
GENUI = '"@copilotkit/vue/v2/generative-ui"'

def provider_line(fragment, imports, why):
    line = fragment.strip()
    assert line.startswith("<CopilotKitProvider") and line.endswith(">") and "</" not in line, line[:60]
    return (
        '<script setup lang="ts">\n'
        f"// [harness] {why}\n"
        "// The page prints only the opening provider tag below; these imports, the\n"
        "// <CopilotChat /> inside it and the closing tag are the only added lines.\n"
        + "".join(f"{l}\n" for l in imports)
        + "</script>\n\n<template>\n"
        + line + "\n"
        + "  <CopilotChat /> <!-- [harness] -->\n"
        + "</CopilotKitProvider> <!-- [harness] -->\n"
        + "</template>\n"
    )

def with_imports(module, imports, why):
    return (
        f"// [harness] {why}\n"
        "// The page prints this module without its imports; these lines are the only added lines.\n"
        + "".join(f"{l}\n" for l in imports)
        + "// ── as published ──\n"
        + module
    )

def harness_chat(component_import, tag, why):
    return (
        '<script setup lang="ts">\n'
        f"// [harness] {why}\n"
        "// Mounts the page's provider component with a <CopilotChat /> in its <slot />.\n"
        f'import {{ CopilotChat }} from {V2};\n'
        f"{component_import}\n"
        "</script>\n\n<template>\n"
        f"  <{tag}>\n    <CopilotChat />\n  </{tag}>\n"
        "</template>\n"
    )

# ── Components and surfaces (overview) ───────────────────────────────────────
# The Vue tab's src/App.vue, verbatim. Its plugin entry (src/main.ts with
# GenerativeUIChart/GenerativeUIMap) is applied in the harness's own
# src/main.ts (labelled there).
write("demo-chat/App.vue", code("", 24, "vue"))

# ── Catalogs ────────────────────────────────────────────────────────────────
C = "catalogs/demo-chat"
write(f"{C}/components/ProductGrid.vue", code("catalogs", 3, "vue"))
write(f"{C}/components/ProductCard.vue", code("catalogs", 4, "vue"))
write(f"{C}/shop-ui.ts", code("catalogs", 5, "ts"))
write(f"{C}/HarnessApp.vue", provider_line(code("catalogs", 9, "vue"), [
    f"import {{ CopilotChat, CopilotKitProvider }} from {V2};",
    'import { shopUI } from "./shop-ui";',
], "Catalogs › “Hand it to the provider”."))

# ── Surfaces ────────────────────────────────────────────────────────────────
S = "surfaces/demo-chat"
write(f"{S}/components/FeaturedProducts.vue", code("surfaces", 3, "vue"))
write(f"{S}/components/RetryFallback.vue", code("surfaces", 21, "vue"))
write(f"{S}/Providers.vue", code("surfaces", 22, "vue"))
# FeaturedProducts imports ../shop-ui, which this page never prints. The
# Catalogs page prints that file (same id, acme/shop@1, and the ProductGrid /
# ProductCard the surface names), so it is copied here with its components.
write(f"{S}/shop-ui.ts", "// [harness] Not printed on this page: Catalogs' src/shop-ui.ts, verbatim (FeaturedProducts imports ../shop-ui).\n" + code("catalogs", 5, "ts"))
write(f"{S}/components/ProductGrid.vue", code("catalogs", 3, "vue"))
write(f"{S}/components/ProductCard.vue", code("catalogs", 4, "vue"))

# ── Standard catalog ────────────────────────────────────────────────────────
D = "standard-catalog/demo-chat"
write(f"{D}/Providers.vue", code("standard-catalog", 2, "vue"))
write(f"{D}/HarnessApp.vue", harness_chat('import Providers from "./Providers.vue";', "Providers",
      "Standard catalog › “Turn it on”."))
write(f"{D}/override/components/MyCard.vue", code("standard-catalog", 9, "vue"))
write(f"{D}/override/app-ui.ts", code("standard-catalog", 10, "ts"))

# ── State and actions ───────────────────────────────────────────────────────
A = "state-and-actions/demo-chat"
write(f"{A}/shop-ui.ts", with_imports(code("state-and-actions", 14, "ts"), [
    'import { z } from "zod";',
    f"import {{ createGenerativeUI }} from {GENUI};",
    'import ProductCard from "./components/ProductCard.vue";',
], "State and actions › “Run your code when users click”."))
write(f"{A}/components/ProductCard.vue", code("state-and-actions", 19, "vue"))

# ── Theming ─────────────────────────────────────────────────────────────────
write("theming/demo-chat/Providers.vue", code("theming", 2, "vue"))
write("theming/demo-chat/HarnessApp.vue", harness_chat('import Providers from "./Providers.vue";', "Providers",
      "Theming › “Set your colors”."))

# ── Transports ──────────────────────────────────────────────────────────────
TI = [f"import {{ CopilotChat, CopilotKitProvider }} from {V2};", f"import {{ standardUI }} from {GENUI};"]
write("transports/demo-chat/tool/HarnessApp.vue", provider_line(code("transports", 3, "vue"), TI, "Transports › the render_ui tool (default)."))
write("transports/demo-chat/markdown/HarnessApp.vue", provider_line(code("transports", 7, "vue"), TI, "Transports › markdown."))
write("transports/demo-chat/agent-ids/HarnessApp.vue", provider_line(code("transports", 11, "vue"), TI, "Transports › limit generative UI to some agents (agentIds)."))

# ── Markdown mode ───────────────────────────────────────────────────────────
write("markdown-mode/demo-chat/App.vue", code("markdown-mode", 3, "vue"))
write("markdown-mode/demo-chat/HarnessApp.vue", harness_chat('import App from "./App.vue";', "App",
      "Markdown mode › “Turn it on”: the page's src/App.vue has a <slot />."))
write("markdown-mode/demo-chat/no-context/HarnessApp.vue", provider_line(code("markdown-mode", 6, "vue"), TI,
      "Markdown mode › sendContext: false."))

# ── Adopt from A2UI ─────────────────────────────────────────────────────────
F = "from-a2ui/demo-chat"
write(f"{F}/app-ui.ts", with_imports(code("from-a2ui", 14, "ts"), [
    'import { z } from "zod";',
    'import Airport from "./components/Airport.vue"; // [harness] stand-in — never published',
    'import Arrow from "./components/Arrow.vue"; // [harness] stand-in — never published',
], "Adopt from A2UI › “After”: the catalog."))
write(f"{F}/HarnessApp.vue", provider_line(code("from-a2ui", 7, "vue"), [
    f"import {{ CopilotChat, CopilotKitProvider }} from {V2};",
    'import { appUI } from "./app-ui";',
], "Adopt from A2UI › “After”: the provider."))

print("ok")
