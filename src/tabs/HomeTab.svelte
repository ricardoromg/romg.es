<script>
    import { fly } from "svelte/transition";
    import Brick from "../components/Brick.svelte";
    import Masonry from "../components/Masonry.svelte";
    import data from "../contentTest.json";
    import { filterTypeStore } from "../stores/filterTypeStore";
    import { quadInOut } from "svelte/easing";
</script>

<!-- svelte-ignore a11y_click_events_have_key_events -->
<!-- svelte-ignore a11y_missing_attribute -->
<!-- svelte-ignore a11y_no_static_element_interactions -->
<Masonry>
    <Brick span={3}>
        <div class="intro-text">
            <p>
                Hi! I’m <span class="emph">Ricardo</span> and I’d like to tell you
                a little about me.
            </p>
            <p>
                I’m a physics student trying to understand how computers work, I
                enjoy listening to <a
                    class="emph"
                    onclick={() => {
                        filterTypeStore.set("music");
                    }}>music</a
                >, playing games, taking
                <a
                    class="emph"
                    href="#"
                    onclick={() => {
                        filterTypeStore.set("pictures");
                    }}>pictures</a
                >, drinking coffee and petting
                <span class="emph">Kiko</span>
                (my dog).
            </p>
            <p>
                If you're in the mood for some nonsensical rambles, or want to
                check out my <a
                    class="emph"
                    onclick={() => {
                        filterTypeStore.set("projects");
                    }}>work</a
                >, you are in the right place!
            </p>
        </div>
    </Brick>

    {#each data as brick}
        {#if $filterTypeStore == "" || brick.tags.find((elt) => elt == $filterTypeStore) != undefined}
            <Brick span={brick.span} link={brick.link}>
                <div class={brick.style}>
                    <div class="brick-header">
                        <span>
                            {#each brick.tags as tag, index}
                                {#if index > 0}
                                    &middot;
                                {/if}
                                <a
                                    class="brick-tags"
                                    onclick={() => {
                                        filterTypeStore.set(tag);
                                    }}>{tag}</a
                                >
                            {/each}
                        </span>
                        <span>
                            {brick.date}
                        </span>
                    </div>
                    {#if brick.title != undefined && brick.title != ""}
                        <div class="brick-card-title">
                            <span class="emph">{brick.title}</span>
                        </div>
                    {/if}
                    {#if brick.text != undefined && brick.text != ""}
                        <div class="brick-card-text">
                            <span>{brick.text}</span>
                        </div>
                    {/if}

                    {#if brick.image != undefined && brick.image != ""}
                        <img src={brick.image} />
                    {/if}
                </div>
            </Brick>
        {/if}
    {/each}
</Masonry>
