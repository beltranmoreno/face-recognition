<script>
    // let personName = 'Unknown';
    let personName = 'Beltran';
    let personConfidence = 90;

</script>


<section class="w-screen p-10">
    <div class="flex justify-center p-2">
        <h1 class="lg:text-3xl md:text-xl text-blue-900">Live</h1>
    </div>
</section>
<section class="container mx-auto p-10">
    <div class="p-5 flex justify-start">
        <p class="font-mono">Portal</p>
    </div>
    <div class="flex justify-center items-center border rounded-xl h-20"> </div>
    <div class="p-5 lg:text-xl md:text-lg">
    {#if personName == "Unknown"}
        <h2 class="text-red-800">{personName}</h2>
    {:else}
        <h2 class="text-green-800">{personName}</h2>
        <h2 class="text-green-800">{personConfidence}%</h2>
    {/if}
    </div>
</section>

<section class="container mx-auto flex justify-around">
    <div class="border px-10 py-5">
        <button>Add</button>
    </div>
    <div class="border px-10 py-5">
        <button>Manage</button>
    </div>
</section>
