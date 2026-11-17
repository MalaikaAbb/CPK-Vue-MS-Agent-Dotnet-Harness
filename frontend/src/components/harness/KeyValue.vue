<script setup lang="ts">
defineProps<{ rows: [string, string][] }>();
</script>

<template>
  <dl class="grid grid-cols-[minmax(0,10rem)_1fr] gap-x-4 gap-y-2 text-sm">
    <div v-for="[k, v] in rows" :key="k" class="contents">
      <dt class="font-medium text-slate-500 dark:text-slate-400">{{ k }}</dt>
      <dd class="min-w-0 break-words text-slate-800 dark:text-slate-200">
        <slot :name="k">{{ v }}</slot>
      </dd>
    </div>
  </dl>
</template>
