import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import tailwindcss from '@tailwindcss/vite'

import { harnessDocSync } from './harness/vite-plugin'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    tailwindcss(), // [harness] the harness chrome is styled with Tailwind, as in the React harness
    harnessDocSync(), // [harness] /doc-sync server endpoints (dev only)
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  server: {
    // Same port Vite defaults to and the Quickstart quotes. strictPort so the
    // README's URL is always the right one.
    port: 5173,
    strictPort: true,
    // [harness] Most Vue doc samples use `runtime-url="/api/copilotkit"`, a
    // same-origin path. The Quickstart's runtime is a separate Node server on
    // :8200, so the dev server forwards /api there. (The Quickstart's own
    // App.vue uses the absolute http://localhost:8200 URL and needs no proxy.)
    proxy: {
      '/api': 'http://localhost:8200',
    },
    fs: {
      // The notes pages show backend/*.ts and doc-snapshot files verbatim,
      // imported with `?raw` from outside frontend/.
      allow: ['..'],
    },
  },
})
