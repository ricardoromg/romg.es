import { writable, type Writable } from "svelte/store";

export const viewStore: Writable<string> = writable("HomeTab");
