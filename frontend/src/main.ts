import { createApp } from "vue";
import App from "./HarnessShell.vue"; // [harness] Quickstart: `import App from "./App.vue"` — each doc App.vue lives under src/routes/
import "@copilotkit/vue/styles.css";
// [harness] Generative UI › Components prints these two plugins in its Vue app entry
// (`createApp(App).use(GenerativeUIChart).use(GenerativeUIMap)`); the harness has one
// entry for every route, so they are applied here.
import { GenerativeUIChart } from "@copilotkit/vue/v2/generative-ui/chart";
import { GenerativeUIMap } from "@copilotkit/vue/v2/generative-ui/map";

import "./harness.css"; // [harness] Tailwind for the harness chrome
import router from "./router"; // [harness] one route per doc page

// Quickstart: createApp(App).mount("#app");
createApp(App).use(router).use(GenerativeUIChart).use(GenerativeUIMap).mount("#app"); // [harness] + the two plugins
