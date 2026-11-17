<script setup lang="ts">
/**
 * [harness] STAND-IN — NOT FROM THE DOCS.
 *
 * HITL Overview's MeetingApproval.vue renders `TimePickerCard` for the
 * `schedule_meeting` tool but the page never publishes it. Without it the tool
 * has no UI and never calls `respond`, so the run never resumes.
 *
 * Minimal equivalent, using the page's own description ("static candidate
 * slots"): shows the tool's `topic` and `attendee` args, offers three fixed
 * slots plus "None of these", and calls `respond` once while the call is
 * executing. Props are the useHumanInTheLoop render contract.
 */
import { ref } from "vue";

import StandInBadge from "@/components/harness/StandInBadge.vue";

const props = defineProps<{
  args: { topic?: string; attendee?: string };
  status: "inProgress" | "executing" | "complete";
  respond?: (result: unknown) => Promise<void>;
}>();

const SLOTS = ["Tomorrow 10:00", "Tomorrow 14:00", "Friday 11:00"];
const chosen = ref<string | null>(null);

function pick(slot: string | null) {
  if (!props.respond || chosen.value) return;
  chosen.value = slot ?? "none";
  void props.respond(slot ? { approved: true, time: slot } : { approved: false });
}
</script>

<template>
  <section class="my-2 rounded-lg border border-slate-300 p-3 text-sm dark:border-slate-700">
    <StandInBadge name="TimePickerCard" />
    <p class="mt-1">Meeting: <strong>{{ args.topic ?? "…" }}</strong> with {{ args.attendee ?? "…" }}</p>
    <div v-if="status === 'executing' && !chosen" class="mt-2 flex flex-wrap gap-2">
      <button v-for="slot in SLOTS" :key="slot" class="rounded border px-2 py-1" @click="pick(slot)">{{ slot }}</button>
      <button class="rounded border px-2 py-1" @click="pick(null)">None of these</button>
    </div>
    <p v-else-if="chosen" class="mt-2 text-xs text-slate-500">Answered: {{ chosen }}</p>
    <p v-else class="mt-2 text-xs text-slate-500">{{ status }}</p>
  </section>
</template>
