import { createRouter, createWebHistory, type RouteRecordRaw } from "vue-router";

import { ALL_ROUTES, demoPath } from "@/lib/nav-config";

/**
 * [harness] Routes are derived, not listed: every nav entry maps to
 * `src/routes/<path>/Notes.vue`, and a nav entry with `hasDemo` also maps
 * `<path>/demo-chat` to `src/routes/<path>/demo-chat/Demo.vue`. The three
 * harness pages (/, /status, /doc-sync) live in src/pages/.
 */
const notes = import.meta.glob("/src/routes/**/Notes.vue");
const demos = import.meta.glob("/src/routes/**/demo-chat/Demo.vue");

const HARNESS_PAGES: Record<string, () => Promise<unknown>> = {
  "/": () => import("@/pages/HomePage.vue"),
  "/status": () => import("@/pages/StatusPage.vue"),
  "/doc-sync": () => import("@/pages/DocSyncPage.vue"),
};

const routes: RouteRecordRaw[] = [];
for (const meta of ALL_ROUTES) {
  const page = HARNESS_PAGES[meta.path] ?? notes[`/src/routes${meta.path}/Notes.vue`];
  if (page) routes.push({ path: meta.path, component: page });
  const demo = demoPath(meta);
  const demoComponent = demos[`/src/routes${meta.path}/demo-chat/Demo.vue`];
  if (demo && demoComponent) routes.push({ path: demo, component: demoComponent });
}
routes.push({ path: "/:pathMatch(.*)*", component: () => import("@/pages/NotFound.vue") });

export default createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior: () => ({ top: 0 }),
});
