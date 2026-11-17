<script setup lang="ts">
/**
 * [harness] STAND-IN — NOT FROM THE DOCS.
 *
 * Headless Interrupts publishes only an App.vue that imports
 * `./components/HeadlessInterruptPanel.vue`; the panel itself is never shown.
 * Minimal equivalent of what the page describes (useInterrupt with
 * `renderInChat: false`, rendered with no chat): the pending interrupt's
 * message and resolve / cancel. It also shows "no interrupt pending" so the
 * empty state is visible — BuiltInAgent never interrupts (README §9).
 */
import { useInterrupt } from "@copilotkit/vue/v2";

import StandInBadge from "@/components/harness/StandInBadge.vue";

const { slotProps } = useInterrupt({ renderInChat: false });
</script>

<template>
  <section style="padding: 16px">
    <StandInBadge name="HeadlessInterruptPanel" />
    <div v-if="slotProps">
      <p>{{ slotProps.interrupt?.message ?? "Interrupt pending" }}</p>
      <button @click="slotProps.resolve({ approved: true })">Resolve</button>
      <button @click="slotProps.cancel()">Cancel</button>
    </div>
    <p v-else>No interrupt pending.</p>
  </section>
</template>
