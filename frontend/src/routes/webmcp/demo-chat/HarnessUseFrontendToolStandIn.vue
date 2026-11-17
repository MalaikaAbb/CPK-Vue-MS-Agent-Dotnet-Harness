<script setup lang="ts">
/** [harness] The useFrontendTool sample (verbatim OrderSearch.vue) with the searchOrders stand-in installed. */
import HarnessUseFrontendTool from "./HarnessUseFrontendTool.vue";
import WithSearchOrdersStandIn from "./WithSearchOrdersStandIn.vue";
</script>

<template>
  <WithSearchOrdersStandIn><HarnessUseFrontendTool /></WithSearchOrdersStandIn>
</template>
