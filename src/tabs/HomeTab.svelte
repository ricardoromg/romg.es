<script lang="ts">
    import Brick from "../components/Brick.svelte";
    import Masonry from "../components/Masonry.svelte";
    import { filterTypeStore } from "../stores/filterTypeStore";

    export let filter: string = "";

    $: filterTypeStore.set(filter);

    const svelteArticles = import.meta.glob(`../articles/*.svelte`, {
        eager: true,
    });
    const data = Object.entries(svelteArticles).map(([path, module]: any) => {
        return module.meta;
    });

    function tagURL(tag: string): string {
        if (["music", "projects", "pictures"].includes(tag)) {
            return `/${tag}`;
        } else {
            return `/tag/${tag}`;
        }
    }
</script>

<Masonry>
    <Brick span={3}>
        <div class="intro-text">
            <p>
                Hi! I’m <span class="emph">Ricardo</span> and I’d like to tell you
                a little about me.
            </p>
            <p>
                I’m a physics student trying to understand how computers work, I
                enjoy listening to <a class="emph" href="/music">music</a>,
                playing games, taking
                <a class="emph" href="/pictures">pictures</a>, drinking coffee
                and petting <span class="emph">Kiko</span> (my dog).
            </p>
            <p>
                If you're in the mood for some nonsensical rambles, or want to
                check out my <a class="emph" href="/projects">work</a>, you are
                in the right place!
            </p>
        </div>
    </Brick>

    {#each data as brick}
        {#if $filterTypeStore == "" || brick.tags.find((elt) => elt == $filterTypeStore) != undefined}
            <!--<Brick>
                <pre>{JSON.stringify(brick, null, 2)}</pre>
                </Brick>-->

            <Brick
                name={brick.name}
                span={brick.span}
                link={brick.link}
                noContent={brick.noContent}
            >
                <div class={brick.style}>
                    <div class="brick-header">
                        <span>
                            {#each brick.tags as tag, index}
                                {#if index > 0}
                                    &nbsp;&middot;
                                {/if}
                                <a class="brick-tags" href={tagURL(tag)}
                                    >{tag}</a
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
