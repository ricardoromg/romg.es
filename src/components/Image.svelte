<script lang="ts">
    import data from "../../public/alt.json";

    export let src: string = "/";
    export let alt: string = "";
    export let width: number | undefined = undefined;
    export let height: number | undefined = undefined;

    $: {
        const imageData = data.find((image) => image.src === src);
        if (imageData) {
            if (!alt) alt = imageData.alt;
            if (!width && imageData.width) width = imageData.width;
            if (!height && imageData.height) height = imageData.height;
        }
    }
</script>

<img
    {...$$restProps}
    {src}
    {alt}
    {width}
    {height}
    style="width: 100%; height: auto; display: block;"
/>
