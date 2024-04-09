<script>
	import { reference } from '../mock/home-data';
</script>

<div>
	<h1 class="text-2xl lg:text-3xl font-bold">Home</h1>
	<p class="max-w-[500px]">
		This is a demo application to present some of my svelte and python skills. Please take a look at
		my other demo pages, or my github page.
	</p>
	<div class="inline-block py-4">
		<a
			href="https://github.com/IJustMatthew"
			target="_blank"
			class="flex gap-2 items-center bg-neutral-900 p-2 rounded-lg hover:bg-neutral-800 transition"
		>
			<img
				src="/images/icons/github.svg"
				alt="github icon"
				class="w-[30px] h-[30px] inline-block"
			/>
			<p>IJustMatthew Github</p>
		</a>
	</div>

	<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
		{#each reference as { title, link, img }}
			<a
				href={link}
				target="_blank"
				class="rounded-lg bg-neutral-800 hover:bg-neutral-900 transition group"
			>
				<img
					src={`/images/other/${img}`}
					alt={img}
					class="w-full group-hover:brightness-90 transition h-[200px] object-cover inline-block rounded-t-lg"
				/>
				<p class="py-4 px-2 text-white font-bold">{title}</p>
			</a>
		{/each}
	</div>
</div>
