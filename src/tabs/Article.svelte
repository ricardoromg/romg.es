<script lang="ts">
    import Spinner from "../components/Spinner.svelte";
    import FourOFour from "./FourOFour.svelte";
    import { tagURL } from "../functions";

    export let slug: string = "";

    const articles = import.meta.glob("../articles/*.svelte");

    let ArticleContent: any;
    let meta: any;
    let loaded: boolean = false;
    let allTags: string[];
    let date: string;

    $: if (slug) {
        const loader = articles[`../articles/${slug}.svelte`];
        if (loader) {
            loader()
                .then((module: any) => {
                    ArticleContent = module.default;
                    meta = module.meta;

                    const Tags = meta?.tags || [];
                    const SecondaryTags = meta?.secondarytags || [];
                    allTags = Tags.concat(SecondaryTags);

                    date = meta.date;
                })
                .finally(() => (loaded = true));
        } else {
            loaded = true;
        }
    }

    $: if (loaded) {
        if (meta?.title != "") {
            document.title = meta.title;
        } else if (meta?.text != "") {
            document.title = meta.text;
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
    <div style={"width: 100%; max-width:900px; margin: 0 auto"}>
        <svelte:component this={ArticleContent} />
    </div>
{:else if loaded}
    <FourOFour />
{:else}
    <div class="loading">
        <center><Spinner /></center>
        <p class="center emph">Loading...</p>
    </div>
{/if}

<style>
    .loading {
        position: absolute;
        top: 50vh;
        left: 50vw;
        transform: translate(-50%, -50%);
    }

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
