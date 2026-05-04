<script lang="ts">
    import FourOFour from "./FourOFour.svelte";

    export let meta: any = null;
    $: slug = meta?.params?.slug;

    const articles = import.meta.glob("../articles/*.svelte");

    let ArticleContent: any;
    let loaded: boolean = false;

    $: if (slug) {
        const loader = articles[`../articles/${slug}.svelte`];
        if (loader) {
            loader()
                .then((module: any) => {
                    ArticleContent = module.default;
                })
                .finally(() => (loaded = true));
        } else {
            loaded = true;
        }
    }
</script>

{#if ArticleContent}
    <svelte:component this={ArticleContent} />
{:else if loaded}
    <FourOFour />
{:else}
    <p class="center emph">Loading...</p>
{/if}
