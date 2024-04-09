<script lang="ts">
	import { menu } from '../mock/menu-data';
	import { onMount } from 'svelte';
	import { setItem, getItem, clearStorage } from '../services/storage';
	import Button from './Button.svelte';
	import { goto } from '$app/navigation';

	let isSidebarOpen: boolean = false;
	let activeMenu: string;

	// Toggle sidebar
	function toggleSidebar(): void {
		isSidebarOpen = !isSidebarOpen;
	}

	// Handle menu change
	function handleMenuChange(menu: string): void {
		activeMenu = menu.replace('/', '');
		setItem('activeMenu', activeMenu);
		toggleSidebar();
	}

	// Handle empty storage
	function handleEmptyStorage(): void {
		clearStorage();
		goto('/');
		handleMenuChange('');
	}

	// Set active menu on page load
	onMount(() => {
		activeMenu = getItem('activeMenu') || '';
	});
</script>

<div class="bg-neutral-900">
	<button
		data-drawer-target="default-sidebar"
		data-drawer-toggle="default-sidebar"
		aria-controls="default-sidebar"
		type="button"
		on:click={toggleSidebar}
		class="inline-flex items-center p-2 my-2 ms-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-white transition"
	>
		<span class="sr-only">Open sidebar</span>
		<svg
			class="w-6 h-6"
			aria-hidden="true"
			fill="currentColor"
			viewBox="0 0 20 20"
			xmlns="http://www.w3.org/2000/svg"
		>
			<path
				clip-rule="evenodd"
				fill-rule="evenodd"
				d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"
			></path>
		</svg>
	</button>

	<div
		class={`fixed md:hidden top-0 z-30 left-0 h-full w-full bg-neutral-900/90 transition ${isSidebarOpen ? 'opacity-1 visible' : 'opacity-0 invisible'}`}
		on:click={toggleSidebar}
	></div>
	<aside
		id="default-sidebar"
		class={`fixed top-0 left-0 z-40 w-[250px] h-screen transition-transform -translate-x-full md:translate-x-0 ${isSidebarOpen ? 'translate-x-0' : '-translate-x-full'}`}
		aria-label="Sidebar"
	>
		<img
			src="/images/icons/close.png"
			on:click={toggleSidebar}
			alt="close icon"
			aria-labelledby="close sidebar"
			class="absolute top-2 right-2 w-4 h-4 object-contain md:hidden cursor-pointer"
		/>
		<div class="flex flex-col w-full h-full px-3 py-4 overflow-y-auto bg-gray-50 bg-neutral-800">
			<div class="space-y-2 p-3">
				<img
					src="/images/sm-logo.png"
					alt="sm-web logo"
					class="w-[100px] h-[100px] object-contain"
				/>
			</div>
			<ul class="space-y-2 font-medium">
				{#each menu as { name, link, icon }}
					<li>
						<a
							href={link}
							on:click={() => handleMenuChange(link)}
							class={`flex items-center p-2 text-gray-900 rounded-lg text-white hover:bg-neutral-700 dark:hover:bg-gray-700 group transition ${activeMenu === link.replace('/', '') ? 'bg-primary' : ''}`}
						>
							<img
								src={`/images/icons/${icon}`}
								alt={`${icon} icon`}
								class="w-6 h-6 object-contain"
							/>
							<span class="ms-3">{name}</span>
						</a>
					</li>
				{/each}
			</ul>

			<Button
				text="Empty Local Storage"
				icon="empty-cache.png"
				on:clicked={handleEmptyStorage}
				extraClass="!bg-neutral-500 hover:!bg-neutral-600 text-white !w-full mt-auto"
			/>
		</div>
	</aside>
</div>
