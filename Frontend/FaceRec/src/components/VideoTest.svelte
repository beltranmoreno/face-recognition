<!-- VideoPlayer.svelte -->
<script>
    import { onMount, onDestroy } from 'svelte';
    import { writable } from 'svelte/store';
  
    const imageStream = writable([]);
  
    let imageSource;
    let imageInterval;
  
    onMount(() => {
      // Start fetching the image stream
      startImageStream();
    });
  
    onDestroy(() => {
      // Clean up resources
      stopImageStream();
    });
  
    function startImageStream() {
      imageSource = new EventSource('http://127.0.0.1/videos'); // Replace with your server URL
  
      imageSource.onmessage = (event) => {
        const imageURL = event.data;
        imageStream.update(images => [...images, imageURL]);
      };
  
      imageSource.onerror = (error) => {
        console.error('Error fetching image:', error);
      };
    }
  
    function stopImageStream() {
      if (imageSource) {
        imageSource.close();
      }
    }
  </script>
  
  <div>
    {#each $imageStream as imageURL}
      <img src={imageURL} alt="Stream Image" />
    {/each}
  </div>
  