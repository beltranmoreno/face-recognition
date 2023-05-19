<script>
    import { onMount } from 'svelte';
    import { getTest } from '../stores';
    import { each } from 'svelte/internal';
    import { dataStoreName } from '../stores';
    import ViewImage from './ViewImage.svelte';

    let url = getTest;
    let data = {};

    let options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    };

    let isLoading = true;
    let isSpinning = false;
    let names = '';
    onMount(async () => {
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
    });

    let animationDuration = 1.0;
    let animationDelay = 0.33;

    async function checkAgain(){
        isLoading = true;
        isSpinning = true;
        try {
            const response = await fetch('http://127.0.0.1:5000/test');
            data = await response.json();
            isLoading = false;
            isSpinning = false;
            names = data['names'];
            dataStoreName.set(names);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };
    

    
</script>


<div class="flex justify-center p-5 bg-slate-200 max-w-min rounded-xl">

{#if isLoading}
    <div class="dot-dot-dot animate-pulse"></div>
{:else}
<div class="flex space-x-4 items-center">
    <div>
        <p class="text-7xl font-sans text-gray-700">{names}</p>
    </div>
    {#if names != 'Unknown'}
        <ViewImage />
    {/if}
</div>
{/if}
</div>

<button on:click={checkAgain} title="Recheck" class="max-w-min rounded-full bg-slate-200 hover:bg-slate-300 p-5 items-center fixed bottom-16 left-1/2 transform -translate-x-1/2 shadow-md">
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-10 h-10 ${isSpinning ? 'animate animate-spin' : ''}">
        <path stroke-linecap="round" stroke-linejoin="round" d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99" />
    </svg>      
</button>


<style>
    .dot-dot-dot {
      position: relative;
      display: inline-block;
      width: 48px;
      height: 48px;
      font-size: 48px;
    }
  
    .dot-dot-dot::before {
      content: '';
      position: absolute;
      top: -50%;
      left: 20%;
      width: 100%;
      height: 100%;
      animation: dot-dot-dot 1.5s infinite;
    }
  
    @keyframes dot-dot-dot {
      0%, 80%, 100% {
        content: '.';
        opacity: 0;
      }
      40% {
        content: '..';
        opacity: 1;
      }
      60% {
        content: '...';
        opacity: 1;
      }
    }

  </style>
