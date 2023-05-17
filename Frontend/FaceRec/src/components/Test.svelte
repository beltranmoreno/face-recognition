<script>
    import { onMount } from 'svelte';
    import { getTest } from '../stores';

    let url = getTest;
    let data = {};

    let options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    };

    onMount(async () => {
        const response = await fetch('http://127.0.0.1:5000/videos', options);
        const json = await response.json();
        data = json;
    });


</script>

<p>Hello</p>
<p>{data['hello']}</p>