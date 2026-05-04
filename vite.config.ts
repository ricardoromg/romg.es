import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

const maxAppWidth: number = 1200;

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte()],
  define: {
    MAX_APP_WIDTH: maxAppWidth,
  },
});
