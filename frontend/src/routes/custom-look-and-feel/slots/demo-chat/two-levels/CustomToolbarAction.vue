<script setup lang="ts">
/**
 * [harness] STAND-IN — NOT FROM THE DOCS.
 *
 * The Slots page puts `<CustomToolbarAction />` in the assistant toolbar under
 * “Two levels deep” but never defines it. This is a visible, inert button so
 * the slot's placement can be checked.
 */
import StandInBadge from "@/components/harness/StandInBadge.vue";
</script>

<template>
  <StandInBadge name="CustomToolbarAction" />
</template>
