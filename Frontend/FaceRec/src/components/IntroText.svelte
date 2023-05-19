<script>
    import { onMount, onDestroy } from 'svelte';
    import { dataStoreName } from '../stores';
  
    let name = '';
    const unsubscribe = dataStoreName.subscribe(data => {

      name = data;
      //console.log(name);
    });
 
    let words = ['There', 'is', 'someone', 'at', 'the', 'front', 'door.', 'I', 'think', 'it', 'might', 'be:'];
    let displayedWords = [];
  
    onMount(() => {
      let index = 0;
      const interval = setInterval(() => {
        displayedWords = words.slice(0, index + 1);
        index++;
  
        if (index === words.length) {
          clearInterval(interval);
        }
      }, 150);
    });
    onDestroy(() => {
    unsubscribe();
  });
  </script>
  
  <h1>
    {#each displayedWords as word}
      <span class="word-animation lg:text-7xl md:text-6xl sm:text-5xl font-sans text-gray-500">{word} </span>
    {/each}
  </h1>
  
  <style>
    .word-animation {
      animation: fadeIn 0.5s ease-in;
    }
  
    @keyframes fadeIn {
      from {
        opacity: 0;
      }
      to {
        opacity: 1;
      }
    }
  </style>
  