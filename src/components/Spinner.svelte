<script lang="ts">
    import { onDestroy, onMount } from "svelte";
    import { linear } from "svelte/easing";
    import { draw } from "svelte/transition";

    export let spinnerSize: number = 40;

    let animationTime: number = 200;
    let spinnerCycle: boolean = true;
    let loaderInterval: ReturnType<typeof setInterval>;

    onMount(() => {
        spinnerCycle = true;

        loaderInterval = setInterval(
            () => {
                spinnerCycle = !spinnerCycle;
            },
            animationTime * 8 + 200,
        );
    });

    onDestroy(() => {
        if (loaderInterval) clearInterval(loaderInterval);
    });
</script>

<svg
    xmlns="http://www.w3.org/2000/svg"
    width={spinnerSize}
    height={spinnerSize}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    class="lucide lucide-loader-icon lucide-loader"
    id="spinnerComponent"
>
    {#if spinnerCycle}
        <path
            in:draw={{
                duration: animationTime,
                delay: animationTime * 0,
                easing: linear,
            }}
            out:draw={{
                duration: animationTime,
                delay: animationTime * 0,
                easing: linear,
            }}
            d="M12 6v-4"
        />
        <path
            in:draw={{
                duration: animationTime,
                delay: animationTime * 1,
                easing: linear,
            }}
            out:draw={{
                duration: animationTime,
                delay: animationTime * 1,
                easing: linear,
            }}
            d="m16.2 7.8 2.9-2.9"
        />
        <path
            in:draw={{
                duration: animationTime,
                delay: animationTime * 2,
                easing: linear,
            }}
            out:draw={{
                duration: animationTime,
                delay: animationTime * 2,
                easing: linear,
            }}
            d="M18 12h4"
        />
        <path
            in:draw={{
                duration: animationTime,
                delay: animationTime * 3,
                easing: linear,
            }}
            out:draw={{
                duration: animationTime,
                delay: animationTime * 3,
                easing: linear,
            }}
            d="m16.2 16.2 2.9 2.9"
        />
        <path
            in:draw={{
                duration: animationTime,
                delay: animationTime * 4,
                easing: linear,
            }}
            out:draw={{
                duration: animationTime,
                delay: animationTime * 4,
                easing: linear,
            }}
            d="M12 18v4"
        />
        <path
            in:draw={{
                duration: animationTime,
                delay: animationTime * 5,
                easing: linear,
            }}
            out:draw={{
                duration: animationTime,
                delay: animationTime * 5,
                easing: linear,
            }}
            d="M7.8 16.2 l-2.9 2.9"
        />
        <path
            in:draw={{
                duration: animationTime,
                delay: animationTime * 6,
                easing: linear,
            }}
            out:draw={{
                duration: animationTime,
                delay: animationTime * 6,
                easing: linear,
            }}
            d="M6 12h-4"
        />
        <path
            in:draw={{
                duration: animationTime,
                delay: animationTime * 7,
                easing: linear,
            }}
            out:draw={{
                duration: animationTime,
                delay: animationTime * 7,
                easing: linear,
            }}
            d="M7.8 7.8 l-2.9-2.9"
        />
    {/if}
</svg>

<style>
    #spinnerComponent {
        animation: 4s linear infinite spin;
    }

    @keyframes spin {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
</style>
