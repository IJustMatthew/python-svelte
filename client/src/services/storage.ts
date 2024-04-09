// Set item in local storage
export function setItem<T>(key: string, payload: T): void {
	localStorage.setItem(key, JSON.stringify(payload));
}

// Get item from local storage
export function getItem<T>(key: string): T {
	const data = localStorage.getItem(key);
	return JSON.parse(data as string);
}

// Remove item from local storage
export function removeItem(key: string): void {
	localStorage.removeItem(key);
}

// Clear local storage
export function clearStorage(): void {
	localStorage.clear();
}
