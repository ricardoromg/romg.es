<script lang="ts">
    import data from "../../public/alt.json";

    export let src: string = "/";
    export let alt: string = "";

    $: if (!alt) {
        const imageInAltJson = data.find((image) => image.src === src);
        if (imageInAltJson) {
            alt = imageInAltJson.alt;
        }
    }
</script>

<img {...$$restProps} {src} {alt} />
