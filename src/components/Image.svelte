<script lang="ts">
    import data from "../../public/images.json";

    export let src: string = "";
    export let alt: string = "";
    export let width: number | undefined = undefined;
    export let height: number | undefined = undefined;
    let availableSizes: number[] = [];
    let id: number;
    let dir: string;

    // Turns backslashes (\) into forwardslashes (/).
    function fixBackslashes(str: string): string {
        return str.replaceAll("\\", "/");
    }

    function canonicalSource(image) {
        return "/" + fixBackslashes(image.dir) + "/" + image.id + ".webp";
    }

    $: {
        const imageData = data.find((image) => canonicalSource(image) === src);
        if (imageData) {
            if (!alt) alt = imageData.alt;
            if (!width && imageData.width) width = imageData.width;
            if (!height && imageData.height) height = imageData.height;
            availableSizes = imageData.sizes;
            dir = fixBackslashes(imageData.dir);
            id = imageData.id;
        }
    }

    $: srcset = availableSizes
        .sort((a, b) => b - a)
        .map((size) => {
            if (size == width) return `${dir}/${id}.webp ${size}w`;
            else return `${dir}/${id}-${size}.webp ${size}w`;
        })
        .join(", ");
</script>

{#if availableSizes.length == 0}
    <!-- Haven't found image in images.json -->
    <img
        {...$$restProps}
        {src}
        {alt}
        {width}
        {height}
        style="width: 100%; height: auto; display: block;"
    />
{:else}
    <!-- Have got multiple sizes to display dynamically -->
    <img
        {...$$restProps}
        {alt}
        {width}
        {height}
        {srcset}
        loading="lazy"
        sizes="auto"
        style="width: 100%; height: auto; display: block;"
    />
{/if}
