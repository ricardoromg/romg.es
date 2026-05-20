<script context="module" lang="ts">
    import Image from "../components/Image.svelte";

    export const meta = {
        name: "260101-wiwitool",
        style: "brick-card brick-card-anim brick-card-img",
        span: 2,
        tags: ["projects"],
        secondarytags: ["Wiwitool", "Minecraft"],
        date: "01-01-26",
        title: "The Wiwitool",
        text: "Custom Minecraft painting & disc generator",
        image: "/260101-wiwitool/1.webp",
        noContent: false,
    };
</script>

<h1>The Wiwitool</h1>

<center>
    <div style="max-width: 700px;">
        <Image src="/260101-wiwitool/1.webp" />
    </div>
</center>

<p>
    The Wiwitool is a simple (or at least I hope so) tool that allows you, among
    other things, to create custom Minecraft paintings and music discs based on
    pictures and songs on your computer. The app, co-developed with <a
        class="emph"
        href="https://gligan.net"
        target="_blank">@raegnald</a
    >, runs fully on-device (locally) using a C++ backend compiled to
    WebAssembly (mostly developed by my partner-in-code) and a Svelte frontend
    (I made it pretty and user-friendly!).
</p>
<p>
    The tool is still being developed at the time of writing, with a hopefully
    big GUI update and onboarding coming soon(TM), probably after we're done
    with uni exams.
</p>
<p>
    If you're in the middle of your two-week Minecraft phase, be sure to <a
        class="emph"
        href="https://wiwitool.gligan.net"
        target="_blank">check it out</a
    >! And if you are more intersted in sniffing our yummy code go look at the
    <a class="emph" href="https://github.com/raegnald/wiwitool" target="_blank"
        >repo</a
    > (it's open source, baby).
</p>
