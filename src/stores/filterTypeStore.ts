import { writable, type Writable } from "svelte/store";

export const filterTypeStore: Writable<string> = writable("");
