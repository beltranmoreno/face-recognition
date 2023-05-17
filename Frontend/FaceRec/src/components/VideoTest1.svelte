<script>
    import { onMount } from 'svelte';
  
    let videoElement;
  
    async function fetchVideoStream() {
      try {
        const response = await fetch('http://127.0.0.1:5000/videos');
  
        if (!response.ok) {
          throw new Error('Failed to fetch video feed');
        }
  
        const mediaSource = new MediaSource();
        videoElement.src = URL.createObjectURL(mediaSource);
  
        mediaSource.addEventListener('sourceopen', async () => {
          const sourceBuffer = mediaSource.addSourceBuffer('video/mp4; codecs="avc1.4D401E"');
  
          const readableStream = response.body;
  
          const reader = readableStream.getReader();
  
          let appendPromise = Promise.resolve();
  
          async function readAndAppend() {
            const { done, value } = await reader.read();
  
            if (done) {
              mediaSource.endOfStream();
              return;
            }
  
            await appendPromise;
  
            try {
              sourceBuffer.appendBuffer(value);
              appendPromise = new Promise(resolve => {
                sourceBuffer.addEventListener('updateend', resolve);
              });
            } catch (error) {
              console.error('Error appending buffer:', error);
            }
  
            readAndAppend();
          }
  
          readAndAppend();
        });
      } catch (error) {
        console.error('Error fetching video feed:', error);
      }
    }
  
    onMount(() => {
      fetchVideoStream();
    });
  </script>
  
  <div>
    <video bind:this={videoElement} controls autoplay muted></video>
  </div>
  