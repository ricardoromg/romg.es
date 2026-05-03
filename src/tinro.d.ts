declare module "tinro" {
  import { ComponentType, SvelteComponent } from "svelte";

  export const Route: ComponentType<SvelteComponent>;
  export const router: any;
  export const active: any;
}
