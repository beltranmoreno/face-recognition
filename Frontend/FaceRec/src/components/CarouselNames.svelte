<script>
    import { onMount } from 'svelte';
  
    let names = ['John', 'Jane', 'Alice', 'Bob'];
    let spinning = false;
    let currentIndex = 0;
    let spinningInterval;
  
    const startSpin = () => {
      spinning = true;
      spinningInterval = setInterval(() => {
        currentIndex = (currentIndex + 1) % names.length;
      }, 100);
  
      setTimeout(() => {
        spinning = false;
        clearInterval(spinningInterval);
      }, 3000);
    };
  
    onMount(() => {
      startSpin();
    });
  </script>
  
  <style>
    .slot-machine {
      height: 6rem;
      overflow: hidden;
      position: relative;
    }
  
    .slot-machine .slot {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 2rem;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 1.5rem;
      font-weight: bold;
      color: #333;
      transition: top 1s cubic-bezier(.17,.67,.83,.67);
    }
  
    .slot-machine .slot:nth-child(1) {
      top: -2rem;
    }
  
    .slot-machine .slot:nth-child(2) {
      top: 0;
    }
  
    .slot-machine .slot:nth-child(3) {
      top: 2rem;
    }
  </style>
  
  <div class="slot-machine">
    {#each names as name, index (name)}
      <div class="slot">
        <p>{name}</p>
      </div>
    {/each}
  </div>
  
  <button on:click="{startSpin}" class="mt-4 bg-blue-500 text-white py-2 px-4 rounded">Spin</button>
  