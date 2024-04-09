<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();
	export let isLoading: boolean | undefined = undefined;
	export let text: string;
	export let icon: string;
	export let disabled: boolean | undefined = undefined;
	export let extraClass: string | undefined = undefined;

	function btnClicked() {
		dispatch('clicked');
	}
</script>

<button
	on:click={btnClicked}
	class={`flex gap-2 w-full sm:w-auto items-center justify-center bg-neutral-800 px-4 h-[42px] rounded-lg transition hover:bg-neutral-900 disabled:bg-neutral-500 ${extraClass}`}
	{disabled}
>
	{text}
	{#if isLoading}
		<img src="/images/icons/spinner.svg" alt="spinner icon" class="w-5 h-5 object-contain" />
	{:else}
		<img src={`/images/icons/${icon}`} alt={`${icon} icon`} class="w-5 h-5 object-contain" />
	{/if}
</button>
