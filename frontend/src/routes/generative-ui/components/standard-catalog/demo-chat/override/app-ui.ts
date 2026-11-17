import { createGenerativeUI, standardUI } from "@copilotkit/vue/v2/generative-ui";
import MyCard from "./components/MyCard.vue";

export const appUI = createGenerativeUI({
  id: "acme/app@1",
  extends: [standardUI],
  overrides: { Card: { component: MyCard } },
  components: {},
});
