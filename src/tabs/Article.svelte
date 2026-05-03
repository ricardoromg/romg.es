<script lang="ts">
    import FourOFour from "./FourOFour.svelte";

    export let meta: any = null;
    $: slug = meta?.params?.slug;

    const articles = import.meta.glob("../articles/*.svelte");

    let ArticleContent: any;

    $: if (slug) {
        const loader = articles[`../articles/${slug}.svelte`];
        if (loader) {
            loader().then((module: any) => {
                ArticleContent = module.default;
            });
        }
    }
</script>

{#if ArticleContent}
    <svelte:component this={ArticleContent} />
{:else}
    <FourOFour />
{/if}
