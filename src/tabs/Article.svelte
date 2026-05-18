<script lang="ts">
    import Spinner from "../components/Spinner.svelte";
    import FourOFour from "./FourOFour.svelte";
    import { tagURL } from "../functions";

    export let meta: any = null;
    $: slug = meta?.params?.slug;

    let info: any;

    const articles = import.meta.glob("../articles/*.svelte");

    let ArticleContent: any;
    let loaded: boolean = false;
    let allTags: string[];
    let date: string;

    $: if (slug) {
        const loader = articles[`../articles/${slug}.svelte`];
        if (loader) {
            loader()
                .then((module: any) => {
                    ArticleContent = module.default;
                    info = module.meta;
                    allTags = info.tags.concat(info.secondarytags);
                    date = info.date;
                })
                .finally(() => (loaded = true));
        } else {
            loaded = true;
        }
    }

    $: if (loaded) {
        if (info.title != undefined && info.title != "") {
            document.title = info.title;
        } else if (info.text != undefined && info.text != "") {
            document.title = info.text;
        } else {
            document.title = "Article on romg.es";
        }
    }
</script>

{#if ArticleContent}
    <span class="article-topbar">
        <span class="tags">
            {#each allTags as tag, index}
                {#if index > 0}
                    &nbsp;&middot;
                {/if}
                <a class="tag-pills" href={tagURL(tag)}>{tag}</a>
            {/each}
        </span>
        <span>{date}</span>
    </span>
    <svelte:component this={ArticleContent} />
{:else if loaded}
    <FourOFour />
{:else}
    <center><Spinner /></center>
    <p class="center emph">Loading...</p>
{/if}

<style>
    .article-topbar {
        color: var(--text-color-secondary);
        display: flex;
        justify-content: space-between;
        border-bottom: 1px solid var(--border-color-secondary);
        margin-bottom: 10px;
        padding-bottom: 2px;
        align-items: end;
    }

    .tag-pills {
        color: var(--text-color-secondary);
        font-size: 0.9em;
        font-weight: 200;
    }
</style>
