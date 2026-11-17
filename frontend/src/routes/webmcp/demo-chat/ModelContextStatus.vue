<script setup lang="ts">
/** [harness] NOT FROM THE DOCS — reports whether this browser exposes WebMCP (test step 3 on the page). */
const available = typeof document !== "undefined" && "modelContext" in document;
defineProps<{ mode: string }>();
</script>

<template>
  <p style="padding: 12px 16px; font-size: 13px">
    [harness] <code>document.modelContext</code>:
    <strong>{{ available ? "present" : "absent" }}</strong>
    — {{ available ? `searchOrders should appear in the Model Context Tool Inspector (${mode}).` : "registration is a no-op here. Use Chrome 149+ with WebMCP enabled." }}
  </p>
</template>
