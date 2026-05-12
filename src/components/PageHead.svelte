<script lang="ts">
    import { draw, fade, fly, slide } from "svelte/transition";
    import { filterTypeStore } from "../stores/filterTypeStore";
    import { Menu } from "@lucide/svelte";

    let minWidth: number = 650;
    let windowWidth: number = 1200;
    let showLinks: boolean = false;

    const growDuration = 100; // in ms
</script>

<section class="top-bar" bind:clientWidth={windowWidth} role="main">
    <a class="page-title" href="/">romg.es</a>
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
            {#if !showLinks}
                <!-- <Menu onclick={() => (showLinks = !showLinks)} /> -->
                <button
                    aria-label="button"
                    onclick={() => (showLinks = !showLinks)}
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        class="lucide lucide-menu-icon lucide-menu"
                    >
                        <path
                            in:draw={{ delay: 0, speed: 1, duration: 500 }}
                            d="M4 5h16"
                        />
                        <path
                            in:draw={{ delay: 0, speed: 1, duration: 500 }}
                            d="M4 12h16"
                        />
                        <path
                            in:draw={{ delay: 0, speed: 1, duration: 500 }}
                            d="M4 19h16"
                        />
                    </svg>
                </button>
            {:else}
                <button
                    aria-label="button"
                    onclick={() => (showLinks = !showLinks)}
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        class="lucide lucide-x-icon lucide-x"
                        ><path
                            in:draw={{ delay: 0, speed: 1, duration: 500 }}
                            d="M18 6 6 18"
                        /><path
                            in:draw={{ delay: 0, speed: 1, duration: 500 }}
                            d="m6 6 12 12"
                        /></svg
                    >
                </button>
            {/if}
        </div>
    {/if}
</section>

{#if showLinks && windowWidth < minWidth}
    <section
        class="grid-wrapper hamburger-links"
        transition:slide={{ duration: growDuration }}
    >
        <div
            class="hamburger-tabs"
            in:fly={{ delay: growDuration + 200, duration: 200, y: -30 }}
        >
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
        <div
            class="hamburger-tabs"
            in:fly={{ delay: growDuration + 100, duration: 200, y: -30 }}
        >
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
        <div
            class="hamburger-tabs"
            in:fly={{ delay: growDuration + 0, duration: 200, y: -30 }}
        >
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
        <div class="socials">
            <a
                in:fly={{ delay: 300, duration: 200, y: -30 }}
                class="nav-bar-social"
                href="https://github.com/ricardoromg"
                target="_blank">GitHub</a
            >
            <a
                in:fly={{ delay: 200, duration: 200, y: -30 }}
                class="nav-bar-social"
                href="https://www.instagram.com/ricardo.romg/"
                target="_blank">Instagram</a
            >
            <a
                in:fly={{ delay: 100, duration: 200, y: -30 }}
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

    .socials {
        grid-column-end: span 3;
        display: flex;
        flex-direction: row;
        gap: 10px;
    }

    .hamburger-links {
        & a.nav-bar-social {
            display: inline;
            border-radius: 20px;
            padding: 5px 10px;
            box-shadow:
                inset 0 2px 4px rgba(0, 0, 0, 0.1),
                inset 0 -1px 6px rgba(0, 0, 0, 0.08);
        }
    }

    .hamburger-tabs {
        border-radius: 20px;
        padding: 5px 10px;
        box-shadow:
            0 2px 4px rgba(0, 0, 0, 0.1),
            0 -1px 6px rgba(0, 0, 0, 0.08);
    }
</style>
