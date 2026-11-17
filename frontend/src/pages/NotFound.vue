<script setup lang="ts">
import { RouterLink, useRoute } from "vue-router";
const route = useRoute();
</script>

<template>
  <p class="text-sm text-rose-700">
    No route at <code>{{ route.path }}</code>. See the <RouterLink to="/status" class="underline">status overview</RouterLink>.
  </p>
</template>
