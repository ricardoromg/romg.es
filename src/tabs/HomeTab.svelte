<script lang="ts">
    import Brick from "../components/Brick.svelte";
    import Masonry from "../components/Masonry.svelte";
    import StaticTagBricks from "../components/StaticTagBricks.svelte";
    import { filterTypeStore } from "../stores/filterTypeStore";

    export let filter: string = "";

    $: filterTypeStore.set(filter);

    const svelteArticles = import.meta.glob(`../articles/*.svelte`, {
        eager: true,
    });
    const data = Object.entries(svelteArticles)
        .map(([path, module]: any) => {
            return module.meta;
        })
        .reverse();

    function tagURL(tag: string): string {
        if (["music", "projects", "pictures"].includes(tag)) {
            return `/${tag}`;
        } else {
            return `/tag/${tag}`;
        }
    }
</script>

<Masonry>
    <StaticTagBricks filter={$filterTypeStore} />

    {#each data as brick}
        {#if $filterTypeStore == "" || (brick.tags != undefined && brick.tags.find((elt) => elt == $filterTypeStore) != undefined)}
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
