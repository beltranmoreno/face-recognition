<script>
    let frameData = null;
    let data = {};
    let show = false;

    async function getFrame(){
        
        try {
            const response = await fetch('http://127.0.0.1:5000/frame');
            data = await response.json();
            show = true;
            frameData = data.frame;
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };
</script>

<div>
    <button on:click={getFrame} title="View" class="max-w-min rounded-full bg-slate-50 hover:bg-slate-100 p-3 items-center shadow-sm">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" />
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>                   
    </button>
</div>

<div>
    {#if show}
    <div class="fixed inset-0 flex items-center justify-center z-50">
        <img src="data:image/jpeg;base64,{frameData}" alt="Frame">
        <button class="px-4 py-2 bg-blue-500 text-white rounded-lg" on:click={() => show = false}>
            Close
          </button>
    </div>
    {:else}
    <p>Loading frame...</p>
    {/if}
</div>