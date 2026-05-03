<script>
    import Masonry from "./components/Masonry.svelte";
    import Brick from "./components/Brick.svelte";
    import data from "./contentTest.json";
    import PageHead from "./components/PageHead.svelte";
    import PageFoot from "./components/PageFoot.svelte";
    import HomeTab from "./tabs/HomeTab.svelte";
    import { viewStore } from "./stores/viewStore";
</script>

<PageHead />
<section class="main">
    {#if $viewStore == "HomeTab"}
        <HomeTab />
    {/if}
</section>
<PageFoot />
