<script>
    import { Link } from 'svelte-routing';
    import { getTest } from '../stores';
    import Test from '../components/Test.svelte';
    import VideoTest from '../components/VideoTest.svelte';
    import VideoTest1 from '../components/VideoTest1.svelte';

    let url = getTest;

    // let personName = 'Unknown';
    let personName = 'Beltran';
    let personConfidence = 90;

    function goToRegister() {
        window.location.href = "http://localhost:5173/register";
    }

    let data = {};

    function fetchJson() {
        return fetch(url)
            .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
            })
            .then(json => {
            data = json;
            })
            .catch(error => {
            console.error(`Error fetching data: ${error}`);
            });
        }


</script>


<section class="container mx-auto p-10">
    <div class="flex justify-center p-2">
        <h1 class="lg:text-3xl md:text-xl text-blue-900">Live</h1>
    </div>
</section>
<section class="container mx-auto p-10 max-w-2xl lg:max-w-4xl">
    <div class="p-5 space-x-2 flex justify-start">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M16 16c0 1.104-.896 2-2 2h-12c-1.104 0-2-.896-2-2v-8c0-1.104.896-2 2-2h12c1.104 0 2 .896 2 2v8zm8-10l-6 4.223v3.554l6 4.223v-12z"/></svg>
        <p class="font-mono">Portal</p>
    </div>
    <div class="flex justify-center items-center border rounded-xl h-40"> </div>
    <div class="p-5 lg:text-xl md:text-lg">
    {#if personName == "Unknown"}
        <h2 class="text-red-800">{personName}</h2>
    {:else}
        <h2 class="text-green-800 lg:text-2xl md:text-lg">{personName}</h2>
        <h2 class="text-green-800">{personConfidence}%</h2>
    {/if}
    </div>
</section>

<section class="mx-auto max-w-2xl lg:max-w-4xl p-20">
    <div>
        <button on:click={goToRegister} class="flex mx-auto w-2/3 justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
    </div>
</section>

<!-- <div>
    <Test/>
</div> -->

<div>
    <VideoTest />
</div>