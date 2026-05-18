<script lang="ts">
    import Brick from "../components/Brick.svelte";
    import Image from "../components/Image.svelte";
    import Masonry from "../components/Masonry.svelte";
    import StaticTagBricks from "../components/StaticTagBricks.svelte";
    import { tagURL } from "../functions";
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

    $: if (filter != "") {
        document.title = `romg.es | ${filter}`;
    } else {
        document.title = `romg.es`;
    }

    $: if (filter != "") {
        document.title = `romg.es | ${filter}`;
    } else {
        document.title = `romg.es`;
    }
</script>

<Masonry>
    <StaticTagBricks filter={$filterTypeStore} />

    {#each data as brick}
        {@const allTags =
            brick.tags == undefined
                ? []
                : brick.tags.concat(
                      brick.secondarytags == undefined
                          ? []
                          : brick.secondarytags,
                  )}
        {@const tagFound =
            allTags != undefined &&
            allTags.find((elt: any) => elt == $filterTypeStore) != undefined}
        {@const numberOfSecondaryTags =
            brick.secondarytags == undefined ? 0 : brick.secondarytags.length}

        {#if $filterTypeStore == "" || tagFound}
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
                            {#if numberOfSecondaryTags != 0}
                                <span
                                    title={brick.secondarytags.join(", ")}
                                    class="display-secondary-tags-on-brick"
                                >
                                    +{numberOfSecondaryTags}
                                </span>
                            {/if}
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
                        <Image src={brick.image} />
                    {/if}
                </div>
            </Brick>
        {/if}
    {/each}
</Masonry>

<style>
    .display-secondary-tags-on-brick {
        font-size: 0.7em;
    }
</style>
