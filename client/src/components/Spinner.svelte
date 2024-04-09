<script lang="ts">
	export let loadingText = 'Loading...';
</script>

<div class="flex flex-col gap-2 w-full">
	<p class="text-white text-lg">{loadingText}</p>
	<img src="images/icons/spinner.svg" alt="spinner" class="w-8 h-8 object-contain" />
</div>
