interface errorCallback {
	(message: string): void;
}

export async function handleApiRequest<T>(
	url: string,
	method: string,
	data?: T,
	errorCallback?: errorCallback
) {
	const res = await fetch('http://127.0.0.1:5000/api' + url, {
		method: method,
		headers: {
			'Access-Control-Allow-Origin': import.meta.env.VITE_CORS_URL,
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	});

	const responseData = await res.json();

	if (res.ok) {
		const result = responseData;
		return result;
	} else {
		if (errorCallback) errorCallback(responseData.error);
		throw new Error(res.statusText);
	}
}
