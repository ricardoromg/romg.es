<script lang="ts">
    import { filterTypeStore } from "../stores/filterTypeStore";
    import { Menu } from "@lucide/svelte";

    let minWidth: number = 650;
    let windowWidth: number = 1200;
    let showLinks: boolean = true;
</script>

<section class="top-bar" bind:clientWidth={windowWidth}>
    <a class="page-title" href="/"> romg.es </a>
    {#if windowWidth > minWidth}
        <div class="navigation-items">
            <a
                class="nav-bar-link"
                href="/projects"
                style:font-weight={$filterTypeStore == "projects"
                    ? 600
                    : "inherit"}
            >
                projects
            </a>
            &middot;
            <a
                class="nav-bar-link"
                href="/music"
                style:font-weight={$filterTypeStore == "music"
                    ? 600
                    : "inherit"}
            >
                music
            </a>
            &middot;
            <a
                class="nav-bar-link"
                href="/pictures"
                style:font-weight={$filterTypeStore == "pictures"
                    ? 600
                    : "inherit"}
            >
                pictures
            </a>
        </div>

        <div>
            <a
                class="nav-bar-social"
                href="https://github.com/ricardoromg"
                target="_blank">GitHub</a
            >
            &middot;
            <a
                class="nav-bar-social"
                href="https://www.instagram.com/ricardo.romg/"
                target="_blank">Instagram</a
            >
            &middot;
            <a
                class="nav-bar-social"
                href="https://open.spotify.com/user/uq7oset96hcm7bgrplffenxhv?si=c91d6261520d4b8c"
                target="_blank">Spotify</a
            >
        </div>
    {:else}
        <div id="hamburger">
            <Menu onclick={() => (showLinks = !showLinks)} />
        </div>
    {/if}
</section>
{#if showLinks && windowWidth < minWidth}
    <section class="grid-wrapper hamburger-links">
        <div>
            <a
                class="nav-bar-link"
                href="/projects"
                style:font-weight={$filterTypeStore == "projects"
                    ? 600
                    : "inherit"}
            >
                projects
            </a>
        </div>
        <div>
            <a
                class="nav-bar-link"
                href="/music"
                style:font-weight={$filterTypeStore == "music"
                    ? 600
                    : "inherit"}
            >
                music
            </a>
        </div>
        <div>
            <a
                class="nav-bar-link"
                href="/pictures"
                style:font-weight={$filterTypeStore == "pictures"
                    ? 600
                    : "inherit"}
            >
                pictures
            </a>
        </div>
        <div>
            <a
                class="nav-bar-social"
                href="https://github.com/ricardoromg"
                target="_blank">GitHub</a
            >
        </div>
        <div>
            <a
                class="nav-bar-social"
                href="https://www.instagram.com/ricardo.romg/"
                target="_blank">Instagram</a
            >
        </div>
        <div>
            <a
                class="nav-bar-social"
                href="https://open.spotify.com/user/uq7oset96hcm7bgrplffenxhv?si=c91d6261520d4b8c"
                target="_blank">Spotify</a
            >
        </div>
    </section>
{/if}

<style>
    #hamburger {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: right;
        flex: 1;
    }
</style>
