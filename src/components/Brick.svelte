<script lang="ts">
    export let span: number = 1;
    export let link: string = "";
    export let name: string = "";
</script>

<div class="brick" style={`grid-column-end: span ${span}`} {...$$restProps}>
    {#if link != undefined && link != ""}
        <a class="brick-link" href={link} target="_blank">
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
