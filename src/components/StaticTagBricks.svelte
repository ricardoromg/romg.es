<script lang="ts">
    import Brick from "./Brick.svelte";

    export let filter: string = "";
</script>

{#if filter == ""}
    <Brick span={3} link="" noContent={true}>
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
{:else if filter == "music"}
    <Brick span={3} link="" noContent={true}>
        <div class="intro-text">
            <p>
                When it comes to music, I like to think that I am a jack of all
                trades, from the grungiest of <span class="emph">indie</span> to
                the poppiest of pop; from the saddest
                <span class="emph">acoustic</span>
                to the most psychedelic <span class="emph">hyperpop</span>; my
                playlists have it all!
            </p>
            <p>
                But still, everyone has their favourites and I am a real sucker
                for gut-wrenching heartbreaking ballads. Some all-time
                favourites include <span class="emph">Mitski</span>,
                <span class="emph">Adrianne Lenker</span>,
                <span class="emph">Sufjan Stevens</span>
                &amp; <span class="emph">Lucy Dacus</span>. Maybe someday I'll
                write about them.
            </p>
            <p>
                Oh, and I'm BIG into Y2K and own a quaint but ever-growing <span
                    class="emph">CD</span
                >
                collection and plan on fixing up an iPod to relive humanity's golden
                era, 2007.
            </p>
        </div>
    </Brick>
{:else if filter == "playlist"}
    <Brick span={3} link="" noContent={true}>
        <div class="intro-text">
            <p>
                Since I have a tendency to get <span class="emph">stuck</span>
                listening to the same 3 songs on <span class="emph">loop</span>
                for months on end, I've been trying to actively
                <span class="emph">broaden</span> my musical
                <span class="emph">horizons</span>, which is how I have wound up
                with such a wide array of tastes.
            </p>
            <p>
                To aid in making myself listen to new music, I try to make a
                <span class="emph">brand new playlist every month</span>, which
                may contain some oldies, but absolutely must include something
                new every month.
            </p>
        </div>
    </Brick>
{:else if filter == "pictures"}
    <Brick span={3} link="" noContent={true}>
        <div class="intro-text">
            <p>
                When I was younger, I really didn't like taking pictures, at
                least of myself, but I realized that as <span class="emph"
                    >memories</span
                >
                fade, nothing is quite as good as a
                <span class="emph">picture</span>
                (it's worth at least <span class="emph">1000 words</span>!).
            </p>
            <p>
                So, I decided that I was going to start taking more pictures,
                not necessarily of anything special, just <span class="emph"
                    >snapshots</span
                >
                into my life, so that 10, 20 or 50 years on I could maybe try to
                <span class="emph">remember</span> what life was like.
            </p>
            <p>
                Since I was already taking pictures, I decided I might as well
                upload some to <a
                    class="emph"
                    href="https://www.instagram.com/ricardo.romg/">Instagram</a
                >, and so, for over two years I've been uploading monthly
                snapshots into my life, sometimes exciting, sometimes mundane,
                but always there.
            </p>
        </div>
    </Brick>
{:else if filter == "projects"}
    <Brick span={3} link="" noContent={true}>
        <div class="intro-text">
            <p>
                Over the years I have realized that I <span class="emph"
                    >really</span
                >
                like computers and programming, and may be looking to eventually find
                work mixing my love for <span class="emph">physics</span> and
                <span class="emph">computers</span>.
            </p>
            <p>
                For that, I've decided that I need to broaden my computing
                horizons and have been taking on some <span class="emph"
                    >small projects</span
                >; some in
                <span class="emph">Python</span>, others in a variety of
                programming languages to eventually have a
                <span class="emph">basic understanding</span> of most languages and
                architectures.
            </p>
        </div>
    </Brick>
{/if}
