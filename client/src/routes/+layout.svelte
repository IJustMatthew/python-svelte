<script>
	import '../app.css';
	import Sidebar from '../components/Sidebar.svelte';
</script>

<div class="layout-wrapper">
	<Sidebar />
	<div class="bg-neutral-700 min-h-screen text-white py-[60px] px-[20px] md:p-[40px]">
		<slot />
	</div>
</div>

<style>
	.layout-wrapper {
		display: grid;
		grid-template-columns: 250px 1fr;
	}

	@media screen and (max-width: 768px) {
		.layout-wrapper {
			grid-template-columns: 1fr;
		}
	}
</style>
