<script lang="ts">
    import { getContext } from "svelte";
    import { writable, type Writable } from "svelte/store";

    export let span: number = 1;
    export let link: string = "";
    export let name: string = "";
    export let noContent: boolean | undefined = false;

    const masonryContext = getContext<{ columnCount: Writable<number> }>(
        "masonry",
    );
    const columnCount = masonryContext
        ? masonryContext.columnCount
        : writable(1);
    $: clampedSpan = Math.min(span, $columnCount);
</script>

<div
    class="brick"
    style={`grid-column-end: span ${clampedSpan}`}
    {...$$restProps}
>
    {#if link != undefined && link != ""}
        <a class="brick-link" href={link} target="_blank">
            <slot />
        </a>
    {:else if noContent == undefined || !noContent}
        <a class="brick-link" href="/article/{name}">
            <slot />
        </a>
    {:else}
        <slot />
    {/if}
</div>

<style>
    .brick {
        display: flex;
        flex-flow: column;
        gap: 1rem;

        align-self: start;
    }
</style>
