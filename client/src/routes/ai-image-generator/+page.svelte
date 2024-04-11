<script lang="ts">
	import Button from '../../components/Button.svelte';
	import Spinner from '../../components/Spinner.svelte';
	import { aspectRatioOptions, countOptions } from '../../mock/ai-data';
	import { handleApiRequest } from '../../services/api';
	import { onMount } from 'svelte';
	import { getItem, setItem } from '../../services/storage';
	import type { PromptOptions } from 'src/types';

	let error: string | null = null;
	let isLoading: boolean = false;
	let promptOptions: PromptOptions = {
		token: null,
		prompt: null,
		exclude: '',
		ratio: '1:1-512',
		count: '1'
	};
	let generatedImages: string[] = [];

	// Handle category change
	function handleResolutionChange(e: Event): void {
		promptOptions.ratio = (e.target as HTMLInputElement).value;
	}

	// Handle category change
	function handleCountChange(e: Event): void {
		promptOptions.count = (e.target as HTMLInputElement).value;
	}

	async function handleImgCreation() {
		if (!promptOptions.token || !promptOptions.prompt) {
			return;
		}
		isLoading = true;
		error = null;

		const response = await handleApiRequest(
			'/ai/image-creation',
			'POST',
			promptOptions,
			errorCallback
		);

		generatedImages = response;
		setItem('generatedImages', generatedImages);
		isLoading = false;
	}

	// If there is an error, set error message
	function errorCallback(errorMsg: string) {
		isLoading = false;
		error = errorMsg;
	}

	// Get stored images on mount
	onMount(() => {
		const storedImages = getItem('generatedImages');
		if (storedImages) {
			generatedImages = storedImages as string[];
		}
	});
</script>

<div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
	<div class="my-2">
		<h1 class="text-2xl lg:text-3xl font-bold">AI Image Generator</h1>
		<p class="max-w-[500px]">Generate images with stable-diffusion AI.</p>

		<form class="w-full my-6 space-y-2">
			<div class="flex flex-col w-full space-y-1">
				<label for="title">
					Your Token -
					<a target="_blank" href="https://replicate.com/" class="text-blue-400 underline"
						>Replicate Api key
					</a>
				</label>
				<input
					required
					type="text"
					id="title"
					class="rounded-lg text-neutral-800 px-4 py-2"
					placeholder="Your API token here..."
					bind:value={promptOptions.token}
				/>
				{#if error}
					<p class="text-red-300">{error}</p>
				{/if}
			</div>

			<div class="flex flex-col w-full space-y-1">
				<label for="descritpion">Prompt</label>
				<textarea
					required
					id="descritpion"
					class="rounded-lg text-neutral-800 px-4 py-2"
					placeholder="What you want to see on the pictures (Samurai cat eating pizza, cinematic, realistic)..."
					bind:value={promptOptions.prompt}
				/>
			</div>

			<div class="flex flex-col w-full space-y-1">
				<label for="title">Exclude specific things (separated with comma)</label>
				<input
					type="text"
					id="title"
					class="rounded-lg text-neutral-800 px-4 py-2"
					placeholder="sword, blood, violence"
					bind:value={promptOptions.exclude}
				/>
			</div>

			<div class="flex flex-col gap-1">
				<label for="scrape_category">Resolution</label>
				<select
					id="scrape_category"
					bind:value={promptOptions.ratio}
					on:change={handleResolutionChange}
					class="rounded-lg text-neutral-800 px-4 py-2 min-w-full sm:w-[200px]"
				>
					{#each aspectRatioOptions as { id, text }}
						<option value={id}>
							{text}
						</option>
					{/each}
				</select>
			</div>

			<div class="flex flex-col gap-1">
				<label for="scrape_category">Image count</label>
				<select
					id="scrape_category"
					bind:value={promptOptions.count}
					on:change={handleCountChange}
					class="rounded-lg text-neutral-800 px-4 py-2 min-w-full sm:w-[200px]"
				>
					{#each countOptions as { id, text }}
						<option value={id}>
							{text}
						</option>
					{/each}
				</select>
			</div>

			<div class="!mt-4 w-full">
				<Button
					text="Generate Image(s)"
					icon="images.png"
					{isLoading}
					on:clicked={handleImgCreation}
					extraClass="!w-full"
				/>
			</div>
		</form>
	</div>

	<div>
		<h2 class="text-2xl lg:text-3xl font-bold mb-4">Generated images</h2>
		{#if generatedImages.length === 0}
			{#if isLoading}
				<Spinner loadingText="Creating Image(s)..." />
			{:else}
				<p>No images created yet.</p>
			{/if}
		{:else}
			<div class="grid grid-cols-1 lg:grid-cols-2 gap-4" id="images">
				{#each generatedImages as item}
					<a href={item} target="_blank" class="hover:brightness-110 transition">
						<img
							src={item}
							alt={item}
							class="w-full h-auto object-cover rounded-xl cursor-pointer"
						/>
					</a>
				{/each}
			</div>
		{/if}
	</div>
</div>
