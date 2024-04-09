<script lang="ts">
	import type { YoutubeData } from 'src/types';
	import Button from '../../components/Button.svelte';
	import Spinner from '../../components/Spinner.svelte';
	import { handleApiRequest } from '../../services/api';
	import { onMount } from 'svelte';

	let videoUrl: string = '';
	let isLoading: boolean = true;
	let isDownloading: boolean = false;
	let convertedVideo: YoutubeData | null = null;
	let videoList: string[] | null = null;
	let error: string | null = null;

	// Get formerly downloaded videos
	async function getVideos(): Promise<string[]> {
		const response = await handleApiRequest('/get-videos', 'GET');
		videoList = response;
		isLoading = false;

		return videoList as string[];
	}

	// Download youtube video
	async function downloadVideo() {
		isDownloading = true;
		error = null;

		const response = await handleApiRequest(
			'/yt-download',
			'POST',
			{ video_url: videoUrl },
			errorCallback
		);
		convertedVideo = response;
		isDownloading = false;
		videoUrl = '';

		await getVideos();
		return convertedVideo;
	}

	// If there is an error, set error message
	function errorCallback(errorMsg: string) {
		isDownloading = false;
		error = errorMsg;
	}

	// Copy Video path to clipboard
	function copyPathText(text: string): void {
		if (!navigator.clipboard) {
			console.log('Clipboard API not available');
			return;
		}
		navigator.clipboard.writeText(text).then(
			function () {
				console.log('Async: Copying to clipboard was successful!');
			},
			function (err) {
				console.error('Async: Could not copy text: ', err);
			}
		);
	}

	// Get videos on page load
	onMount(async () => {
		await getVideos();
	});
</script>

<div>
	<!-- Page title and description -->
	<h1 class="text-2xl lg:text-3xl font-bold">Youtube Downloader</h1>
	<p class="max-w-[500px]">
		Enter the URL of the video you want to download. The video will be downloaded in the highest
		quality available.
	</p>

	<!-- Video Form -->
	<div class="mt-6 flex-wrap flex items-center jsutify-center sm:justify-start gap-2">
		<input
			type="text"
			bind:value={videoUrl}
			class="rounded-lg text-neutral-800 px-4 py-2 min-w-full sm:min-w-[50%]"
		/>
		<Button
			text="Download Video"
			icon="download.png"
			isLoading={isDownloading}
			on:clicked={downloadVideo}
		/>
	</div>
	{#if error}
		<p class="text-red-300">{error}</p>
	{/if}

	<!-- Show downloaded video & access path -->
	{#if convertedVideo && !isDownloading}
		<div class="mt-6">
			<p class="m-0">Containing Folder</p>
			<button
				title="Copy To Clipboard"
				class="max-w-[500px] bg-primary p-2 text-left rounded-lg my-2 outline-0"
				on:click={() => copyPathText(convertedVideo.path)}
			>
				{convertedVideo.path}
			</button>
			<video
				controls
				poster={convertedVideo.thumbnail}
				class="aspect-video max-w-[500px] w-full h-auto"
			>
				<source src={`/youtube/${convertedVideo.file}.mp4`} type="video/mp4" />
				<track src="" kind="captions" srclang="en" label="english_captions" />
				Your browser does not support HTML video.
			</video>
		</div>
	{/if}

	<!-- Formerly downloaded videos -->
	<h2 class="text-2xl lg:text-3xl font-bold mt-[100px] mb-4">Formerly Downloaded Videos</h2>
	{#if videoList?.length === 0}
		<p>No videos have been downloaded yet.</p>
	{/if}
	<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 w-full">
		{#if videoList}
			{#each videoList as video}
				<div class="flex flex-col p-4 bg-neutral-800 rounded-lg">
					<video controls class="aspect-video w-full h-auto">
						<source src={`/youtube/${video}`} type="video/mp4" />
						<track src="" kind="captions" srclang="en" label="english_captions" />
						Your browser does not support HTML video.
					</video>
					<p class="mt-2">{video}</p>
				</div>
			{/each}
		{/if}
	</div>
	{#if isLoading}
		<Spinner />
	{/if}
</div>
