<script lang="ts">
	import Button from '../../components/Button.svelte';
	import type { Todo } from 'src/types';
	import { handleApiRequest } from '../../services/api';
	import { onMount } from 'svelte';

	let isLoading: boolean = false;
	let todos: Todo[] = [];
	let currentTodo: Todo = { id: '', title: '', description: '' };
	let isEditModeActive = false;
	let showError = false;

	// Handle Todo form - addition and update
	async function handleTodoForm() {
		if (!currentTodo.title || !currentTodo.description) {
			showError = true;
			return;
		} else {
			showError = false;
		}

		isLoading = true;

		if (isEditModeActive) {
			const response = await handleApiRequest('/todo/update', 'POST', currentTodo);
			todos = response;
		} else {
			let date = new Date();
			currentTodo.id = date.getTime().toString();

			const response = await handleApiRequest('/todo/add', 'POST', currentTodo);
			todos = response;
		}

		currentTodo = { id: '', title: '', description: '' };
		isLoading = false;
		isEditModeActive = false;
	}

	// Handle Todo edit button click
	function handleTodoEdit(id: string, title: string, description: string) {
		isEditModeActive = true;
		currentTodo = { id, title, description };
	}

	// Handle Todo delete
	async function handleTodoDelete(id: string) {
		isLoading = true;

		const response = await handleApiRequest('/todo/delete', 'POST', { id });
		todos = response;
		isLoading = false;
	}

	// Get Todos
	async function getTodos(): Promise<Todo[]> {
		isLoading = true;

		const response = await handleApiRequest('/todos', 'GET');
		todos = response;
		isLoading = false;

		return todos as Todo[];
	}

	// Get Todos on page load
	onMount(() => {
		getTodos();
	});
</script>

<div>
	<h1 class="text-2xl lg:text-3xl font-bold">TODO List</h1>
	<p class="max-w-[500px]">Make basic CRUD operations.</p>

	<form class="w-full md:w-[500px] my-6">
		<div class="flex flex-col w-full space-y-1">
			<label for="title">Title</label>
			<input
				required
				type="text"
				id="title"
				class="rounded-lg text-neutral-800 px-4 py-2"
				placeholder="Todo title..."
				bind:value={currentTodo.title}
			/>
		</div>

		<div class="flex flex-col w-full space-y-1">
			<label for="descritpion">Descritpion</label>
			<textarea
				required
				id="descritpion"
				class="rounded-lg text-neutral-800 px-4 py-2"
				placeholder="Todo description..."
				bind:value={currentTodo.description}
			/>
		</div>
		{#if showError}
			<p class="text-red-400">Please fill out all fields.</p>
		{/if}
		<div class="mt-4 w-full">
			<Button
				text={isEditModeActive ? 'Update todo' : 'Add todo'}
				icon={isEditModeActive ? 'edit.png' : 'add.png'}
				{isLoading}
				on:clicked={handleTodoForm}
				extraClass="!w-full"
			/>
		</div>
	</form>
	<div class="max-w-[500px]">
		<h2 class="text-2xl lg:text-3xl font-bold mb-4">Todo List Items</h2>

		{#if todos.length === 0}
			<p>No todos found.</p>
		{:else}
			{#each todos as { id, title, description }}
				<div class="flex flex-col w-full gap-2 relative bg-neutral-800 rounded-lg p-3 mb-4">
					<p class="font-bold text-lg">{title}</p>
					<p class="font-sm">{description}</p>
					<div class="absolute top-3 right-3 flex gap-2">
						<img
							src="/images/icons/edit.png"
							alt="edit icon"
							class="w-4 h-4 object-contain cursor-pointer"
							on:click={() => handleTodoEdit(id, title, description)}
						/>
						<img
							src="/images/icons/close.png"
							alt="close icon"
							class="w-4 h-4 object-contain cursor-pointer"
							on:click={() => handleTodoDelete(id)}
						/>
					</div>
				</div>
			{/each}
		{/if}
	</div>
</div>
