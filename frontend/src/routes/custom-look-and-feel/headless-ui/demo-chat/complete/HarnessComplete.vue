<script setup lang="ts">
/**
 * [harness] NOT FROM THE DOCS — mounts the published RenderedMessages.vue.
 *
 * RenderedMessages renders the conversation but has no composer, and the page
 * publishes no App.vue for it. It is mounted under the same providers the
 * page's minimal example prints (CopilotKitProvider + a
 * CopilotChatConfigurationProvider for `my-agent`), with the published
 * HeadlessChat.vue from that example underneath as the composer, so both read
 * the one `my-agent` instance.
 */
import { CopilotChatConfigurationProvider, CopilotKitProvider } from "@copilotkit/vue/v2";

import HeadlessChat from "../minimal/HeadlessChat.vue";

import RenderedMessages from "./RenderedMessages.vue";
</script>

<template>
  <CopilotKitProvider runtime-url="/api/copilotkit">
    <CopilotChatConfigurationProvider agent-id="my-agent">
      <RenderedMessages />
      <hr />
      <p style="font-size: 12px; opacity: 0.7">[harness] composer below = HeadlessChat.vue from the minimal example</p>
      <HeadlessChat />
    </CopilotChatConfigurationProvider>
  </CopilotKitProvider>
</template>
