<script lang="ts">
    export let src: string = "/";
    export let alt: string = "";
    export let styleid: string = "";
    export let styleclass: string = "";
    import data from "../../public/alt.json";

    $: if (!alt) {
        const imageInAltJson = data.find((image) => image.src === src);
        if (imageInAltJson) {
            alt = imageInAltJson.alt;
        }
    }
</script>

<img id={styleid} class={styleclass} {src} {alt} />
