<script lang="ts">
	import { scrapeOptions } from '../../mock/scraping-data';
	import Button from '../../components/Button.svelte';
	import type { ScrapeData } from 'src/types';
	import { handleApiRequest } from '../../services/api';
	import { getItem, setItem } from '../../services/storage';
	import { onMount } from 'svelte';

	let isLoading: boolean = false;
	let scrapedData: ScrapeData[] = [];
	let selectedCategory: string | null = null;

	// Handle category change
	function handleScrapeChategoryChange(e: Event): void {
		selectedCategory = (e.target as HTMLInputElement).value;
	}

	// Scrape website
	async function scrapeWebsite() {
		scrapedData = [];
		setItem('scrapedData', scrapedData);
		isLoading = true;

		const response = await handleApiRequest('/scrape-website', 'POST', {
			category: selectedCategory
		});
		scrapedData = response;
		setItem('scrapedData', scrapedData);
		isLoading = false;

		return scrapedData;
	}

	// Get scraped items on page load
	onMount(async () => {
		scrapedData = getItem<ScrapeData[]>('scrapedData') || [];
	});
</script>

<div>
	<h1 class="text-2xl lg:text-3xl font-bold">Web Scraping</h1>
	<p class="max-w-[500px]">Scraping categories on etsy with Selenium and BeautifulSoup</p>

	<div class="flex items-end flex-wrap gap-2 my-6">
		<div class="flex flex-col gap-1 w-full sm:w-auto">
			<label for="scrape_category">Choose Category</label>
			<select
				id="scrape_category"
				bind:value={selectedCategory}
				on:change={handleScrapeChategoryChange}
				class="rounded-lg text-neutral-800 px-4 py-2 min-w-full sm:w-[200px]"
			>
				<option disabled selected hidden></option>
				{#each scrapeOptions as { id, text }}
					<option value={id}>
						{text}
					</option>
				{/each}
			</select>
		</div>
		<Button
			text="Start Scraping"
			icon="scraping.png"
			{isLoading}
			on:clicked={scrapeWebsite}
			disabled={!selectedCategory}
		/>
	</div>

	<div>
		{#if scrapedData.length === 0}
			<p class="text-lg">No scraped items yet</p>
		{:else}
			<h2 class="text-2xl lg:text-3xl font-bold mb-4">Scraped Items</h2>

			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
				{#each scrapedData as { title, thumbnail, price, original_price, currency, rating_info, url }}
					<a
						href={url}
						target="_blank"
						class="bg-neutral-800 p-4 rounded-lg shadow-md space-y-2 hover:bg-neutral-900 transition"
					>
						<img src={thumbnail} alt={title} class="w-full h-40 object-cover rounded-lg" />
						<p class="title font-bold">{title}</p>
						<div class="flex flex-col">
							{#if original_price}
								<p class="text-sm line-through text-red-500 text-[12px]">
									{currency}
									{original_price}
								</p>
							{/if}
							<p class="text-sm font-bold text-lg">{currency} {price}</p>
						</div>
						<p class="text-sm">{rating_info}</p>
					</a>
				{/each}
			</div>
		{/if}
	</div>
</div>

<style>
	.title {
		overflow: hidden;
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-line-clamp: 2;
		-webkit-box-orient: vertical;
		line-height: 20px;
	}
</style>
