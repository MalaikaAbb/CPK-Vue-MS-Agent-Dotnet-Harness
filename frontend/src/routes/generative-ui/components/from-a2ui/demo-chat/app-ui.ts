// [harness] Adopt from A2UI › “After”: the catalog.
// The page prints this module without its imports; these lines are the only added lines.
import { z } from "zod";
import Airport from "./components/Airport.vue"; // [harness] stand-in — never published
import Arrow from "./components/Arrow.vue"; // [harness] stand-in — never published
// ── as published ──
import {
  createGenerativeUI,
  standardUI,
} from "@copilotkit/vue/v2/generative-ui";

export const appUI = createGenerativeUI({
  id: "acme/flights@1",
  extends: [standardUI],
  components: {
    Airport: {
      component: Airport,
      description: "An airport by IATA code, with its city under it.",
      props: z.object({ code: z.string(), city: z.string() }),
    },
    Arrow: { component: Arrow, description: "An arrow between two airports." },
  },
});
