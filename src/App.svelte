<script>
    import { Route, router } from "tinro";
    import PageHead from "./components/PageHead.svelte";
    import PageFoot from "./components/PageFoot.svelte";
    import HomeTab from "./tabs/HomeTab.svelte";
    import Article from "./tabs/Article.svelte";
    import FourOFour from "./tabs/FourOFour.svelte";

    router.mode.history();
</script>

<PageHead />
<div class="main" style="--max-app-width: {MAX_APP_WIDTH}px">
    <Route path="/">
        <HomeTab filter="" />
    </Route>

    <Route path="/tag/:tag" let:meta>
        <HomeTab filter={meta.params.tag} />
    </Route>

    <Route path="/projects" exact>
        <HomeTab filter="projects" />
    </Route>

    <Route path="/music" exact>
        <HomeTab filter="music" />
    </Route>

    <Route path="/pictures" exact>
        <HomeTab filter="pictures" />
    </Route>

    <Route path="/article/:slug" let:meta>
        {#if !["music", "pictures", "projects"].includes(meta.params.slug)}
            <Article {meta} />
        {/if}
    </Route>

    <Route fallback>
        <FourOFour />
    </Route>
</div>
<PageFoot />
