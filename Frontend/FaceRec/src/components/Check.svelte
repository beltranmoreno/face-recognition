<script>
    import { dataStoreName } from '../stores';

    let isLoading = true;
    let names = '';
    let data = {};
    async function checkAgain(){
        try {
            const response = await fetch('http://127.0.0.1:5000/test');
            data = await response.json();
            isLoading = false;
            names = data['names'];
            console.log(names);
            dataStoreName.set(names);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

</script>



<button on:click={checkAgain} title="Recheck" class="max-w-min rounded-full bg-slate-200 hover:bg-slate-300 p-5 items-center fixed bottom-16 left-1/2 transform -translate-x-1/2 shadow-md">
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-10 h-10">
        <path stroke-linecap="round" stroke-linejoin="round" d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99" />
    </svg>      
</button>