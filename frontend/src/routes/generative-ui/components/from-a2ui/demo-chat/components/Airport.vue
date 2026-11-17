<script setup lang="ts">
/**
 * [harness] STAND-IN — NOT FROM THE DOCS.
 *
 * Adopt from A2UI's appUI registers an `Airport` component (props `code`,
 * `city`) but no page defines it. Minimum to render: the code with the city
 * under it, as the catalog's description says.
 */
import StandInBadge from "@/components/harness/StandInBadge.vue";

defineProps<{ code: string; city: string }>();
</script>

<template>
  <div class="inline-flex flex-col items-center p-2">
    <StandInBadge name="Airport" />
    <strong>{{ code }}</strong>
    <small>{{ city }}</small>
  </div>
</template>
