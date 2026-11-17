<script setup lang="ts">
/**
 * [harness] NOT FROM THE DOCS. Installs the flagged searchOrders stand-in
 * (search-orders.standin.ts) for as long as this sample is mounted, then
 * renders the wrapped sample unchanged.
 */
import { onBeforeMount, onUnmounted } from "vue";

import StandInBadge from "@/components/harness/StandInBadge.vue";

import { installSearchOrdersStandIn } from "./search-orders.standin";

let uninstall: (() => void) | undefined;
onBeforeMount(() => {
  uninstall = installSearchOrdersStandIn();
});
onUnmounted(() => uninstall?.());
</script>

<template>
  <div style="padding: 12px 16px 0"><StandInBadge name="searchOrders" /></div>
  <slot />
</template>
