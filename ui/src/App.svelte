<script>
  import {onMount} from 'svelte'

  const api = import.meta.env.PROD ? import.meta.env.BASE_URL + "/uploads" : "http://localhost:5000/uploads"

  onMount(async () => {
    const response = await fetch(api, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    const json = await response.json()
    uploads = json
  })
  
  $: uploads = []
</script>

<main>
  <nav class="flex flex-row px-4 py-2">
    <h1 class="font-medium">KVD</h1>
  </nav>

  <section class="w-full max-w-xl mx-auto">
    {#each uploads as upload}
      <div class="px-2 py-1 w-full rounded-lg hover:bg-zinc-100"> 
        <a href={[api,upload.name].join("/")} class="font-medium">{upload.name}</a>
        <span>{upload.size} bytes</span>
        <span>{upload.contentType}</span>
      </div>
    {/each}
  </section>
</main>

