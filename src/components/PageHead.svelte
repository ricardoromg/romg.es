<script>
    import { tick } from "svelte";
    import { filterTypeStore } from "../stores/filterTypeStore";
</script>

<section class="top-bar">
    <a class="page-title" href="/"> romg.es </a>

    <div class="navigation-items">
        <a
            class="nav-bar-link"
            href="/projects"
            style:font-weight={$filterTypeStore == "projects" ? 600 : "inherit"}
        >
            projects
        </a>
        &middot;
        <a
            class="nav-bar-link"
            href="/music"
            style:font-weight={$filterTypeStore == "music" ? 600 : "inherit"}
        >
            music
        </a>
        &middot;
        <a
            class="nav-bar-link"
            href="/pictures"
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
