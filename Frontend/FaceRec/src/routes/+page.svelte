<script>
    import { Link } from 'svelte-routing';
    import { getTest } from '../stores';
    import Test from '../components/Test.svelte';
    import VideoTest from '../components/VideoTest.svelte';
    import VideoTest1 from '../components/VideoTest1.svelte';
    import IntroText from '../components/IntroText.svelte';
    import Check from '../components/Check.svelte';
    import CarouselNames from '../components/CarouselNames.svelte';

    let url = getTest;

    // let personName = 'Unknown';
    let personName = '';
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


<!-- <section class="container mx-auto p-10">
    <div class="flex justify-center p-2">
        <h1 class="lg:text-3xl md:text-xl text-blue-900">Live</h1>
    </div>
</section> -->
<section class="container mx-auto p-10 max-w-2xl lg:max-w-4xl space-y-5">
    <div class="space-x-4 flex justify-start items-center">
        <div class="p-5  rounded-lg bg-slate-200 max-w-min text-blue-500">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" color="currentColor"><path d="M16 16c0 1.104-.896 2-2 2h-12c-1.104 0-2-.896-2-2v-8c0-1.104.896-2 2-2h12c1.104 0 2 .896 2 2v8zm8-10l-6 4.223v3.554l6 4.223v-12z"/></svg>
        </div>
        <h1 class="text-6xl font-sans text-blue-500">Camera</h1>
    </div>
    <div class="w-full h-0 border"></div>
    <IntroText />
    <div class="flex justify-center py-10">
        <Test/>
    </div>
</section>

<!-- 
<Check /> -->


