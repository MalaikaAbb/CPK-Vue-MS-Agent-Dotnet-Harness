import { defineComponent, h, type Component } from "vue";

import HarnessProvider from "@/components/harness/HarnessProvider.vue";

/**
 * [harness] Mounts a published component under HarnessProvider, for pages that
 * publish a component but no App.vue to provide it. Every use is named in a
 * Harness callout on that route's notes page.
 */
export function withHarnessProvider(component: Component, runtimeUrl?: string): Component {
  return defineComponent({
    name: "WithHarnessProvider",
    setup: () => () => h(HarnessProvider, { runtimeUrl }, { default: () => h(component) }),
  });
}
