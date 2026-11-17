<script setup lang="ts">
/**
 * [harness] STAND-IN — NOT FROM THE DOCS.
 *
 * Adopt from A2UI's appUI registers an `Arrow` component (no props) but no
 * page defines it. Minimum to render: an arrow.
 */
import StandInBadge from "@/components/harness/StandInBadge.vue";
</script>

<template>
  <span class="inline-flex items-center gap-1 p-2"><StandInBadge name="Arrow" /> →</span>
</template>
