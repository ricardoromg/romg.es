<!-- Attribution: https://css-tricks.com/making-a-masonry-layout-that-works-today/ -->

<script lang="ts">
    import { onMount, onDestroy, setContext, tick } from "svelte";
    import { writable } from "svelte/store";
    import Spinner from "./Spinner.svelte";

    export let brickMinWidth: number = 200;
    let masonryWidth: number = 200;
    let masonryLayout: HTMLDivElement;
    let rendered = false;
    let observer: ResizeObserver;
    let mutationObserver: MutationObserver;
    const columnCount = writable(1);
    setContext("masonry", { columnCount });

    onMount(() => {
        if (masonryLayout) {
            reloadLayout();

            // Watch for items being added/removed (Filtering)
            mutationObserver = new MutationObserver(() => {
                reloadLayout();
            });

            mutationObserver.observe(masonryLayout, {
                childList: true,
                subtree: true,
            });
        }
    });

    onDestroy(() => {
        if (observer) observer.disconnect();
        if (mutationObserver) mutationObserver.disconnect();
    });

    export async function reloadLayout() {
        if (observer) observer.disconnect();
        if (!masonryLayout) return;

        const computedStyle = getComputedStyle(masonryLayout);
        const colGapStr = computedStyle.columnGap;
        const colGap = parseFloat(colGapStr) || 0;
        masonryLayout.style.setProperty("row-gap", "0px", "important");

        const items = getChildren(masonryLayout) as HTMLElement[];

        // Initial layout (might be slightly off)
        await layout({ colGap, items });

        // Non-blocking wait for media to refine the layout
        Promise.all([
            areImagesLoaded(masonryLayout),
            areVideosLoaded(masonryLayout),
        ])
            .then(() => {
                const items = getChildren(masonryLayout) as HTMLElement[];
                layout({ colGap, items });
            })
            .catch(() => {});

        // Also listen for individual image loads to be more responsive
        masonryLayout.querySelectorAll("img").forEach((img) => {
            if (!img.complete) {
                img.addEventListener(
                    "load",
                    () => {
                        const items = getChildren(
                            masonryLayout,
                        ) as HTMLElement[];
                        layout({ colGap, items });
                    },
                    { once: true },
                );
            }
        });

        observer = new ResizeObserver(() => {
            const items = getChildren(masonryLayout) as HTMLElement[];
            layout({ colGap, items });
        });

        observer.observe(masonryLayout);
    }
    function getChildren(container: HTMLElement) {
        let children = container.children;

        // Compensate for Astro Slots
        if (children[0]?.nodeName === "ASTRO-SLOT")
            children = children[0].children;
        return Array.from(children);
    }

    async function areImagesLoaded(container: HTMLElement) {
        const images = Array.from(container.querySelectorAll("img"));
        const promises = images.map((img) => {
            return new Promise<void>((resolve, reject) => {
                if (img.complete) return resolve();
                img.onload = () => resolve();
                img.onerror = reject;
            });
        });
        return Promise.all(promises);
    }

    function areVideosLoaded(container: HTMLElement) {
        const videos = Array.from(container.querySelectorAll("video"));
        const promises = videos.map((video) => {
            return new Promise<void>((resolve, reject) => {
                if (video.readyState === 4) return resolve(); // HAVE_ENOUGH_DATA
                video.onloadedmetadata = () => resolve();
                video.onerror = reject;
            });
        });
        return Promise.all(promises);
    }

    async function layout({
        colGap,
        items,
    }: {
        colGap: number;
        items: HTMLElement[];
    }) {
        if (!masonryLayout) return;

        // Ensure Svelte has finished any pending updates before we measure
        await tick();

        const computedCols = Math.floor(masonryWidth / brickMinWidth);
        const clampedCols = Math.max(computedCols, 1);
        columnCount.set(clampedCols);
        const rowHeight = 1;
        masonryLayout.style.gridAutoRows = `${rowHeight}px`;

        items.forEach((item) => {
            const ib = item.getBoundingClientRect();
            const span = Math.ceil((ib.height + colGap) / rowHeight);
            item.style.gridRowEnd = `span ${span}`;
        });

        rendered = true;
    }
</script>

{#if !rendered}
    <center>
        <Spinner />
    </center>
{/if}

<div
    bind:this={masonryLayout}
    bind:clientWidth={masonryWidth}
    class="masonry"
    class:loaded={rendered}
    style={`grid-template-columns: repeat(auto-fit, minmax(min(${brickMinWidth}px, 100%), 1fr));`}
>
    <slot />
</div>

<style>
    .masonry {
        display: grid;
        gap: 1rem;
        grid-auto-flow: dense;
        opacity: 0;
        transition: opacity var(--transition-speed, 0.25s) ease-in;
    }

    .masonry.loaded {
        opacity: 1;
    }
</style>
