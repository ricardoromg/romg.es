<script>
    import { tick } from "svelte";
    import { filterTypeStore } from "../stores/filterTypeStore";
</script>

<!-- svelte-ignore a11y_click_events_have_key_events -->
<!-- svelte-ignore a11y_missing_attribute -->
<!-- svelte-ignore a11y_no_static_element_interactions -->
<section class="top-bar">
    <a
        class="page-title"
        onclick={() => {
            filterTypeStore.set("");
        }}
    >
        romg.es
    </a>

    <div class="navigation-items">
        <a
            class="nav-bar-link"
            onclick={() => {
                filterTypeStore.set("projects");
            }}
            style:font-weight={$filterTypeStore == "projects" ? 600 : "inherit"}
        >
            projects
        </a>
        &middot;
        <a
            class="nav-bar-link"
            onclick={() => {
                filterTypeStore.set("music");
            }}
            style:font-weight={$filterTypeStore == "music" ? 600 : "inherit"}
        >
            music
        </a>
        &middot;
        <a
            class="nav-bar-link"
            onclick={() => {
                filterTypeStore.set("pictures");
            }}
            style:font-weight={$filterTypeStore == "pictures" ? 600 : "inherit"}
        >
            pictures
        </a>
    </div>

    <div class="nav-bar-social">
        <a href="https://github.com/ricardoromg" target="_blank">GitHub</a>
        &middot;
        <a href="https://www.instagram.com/ricardo.romg/" target="_blank"
            >Instagram</a
        >
        &middot;
        <a
            href="https://open.spotify.com/user/uq7oset96hcm7bgrplffenxhv?si=c91d6261520d4b8c"
            target="_blank">Spotify</a
        >
    </div>
</section>
