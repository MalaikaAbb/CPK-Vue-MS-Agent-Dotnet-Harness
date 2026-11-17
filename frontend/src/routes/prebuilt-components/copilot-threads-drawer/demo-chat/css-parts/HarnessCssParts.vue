<script setup lang="ts">
/**
 * [harness] NOT FROM THE DOCS — applies the published CSS-parts rule.
 *
 * The page prints the `::part(new-thread-button)` / `::part(launcher-new-thread)`
 * rule to use with your own "New conversation" button, i.e. the toolbar
 * sample. This mounts that sample (toolbar/App.vue, verbatim) with the rule
 * (hide-new-thread.css, verbatim) injected only while this sample is open, so
 * it cannot leak into the other drawer samples.
 */
import css from "./hide-new-thread.css?raw";

import App from "../toolbar/App.vue";
</script>

<template>
  <component :is="'style'">{{ css }}</component>
  <App />
</template>
