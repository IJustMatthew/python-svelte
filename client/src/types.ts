export type Reference = {
	title: string;
	link: string;
	img: string;
};

export type Menu = {
	name: string;
	link: string;
	icon: string;
};

export type SelectOption = {
	id: string;
	text: string;
};

export type ScrapeData = {
	currency: string;
	original_price: string;
	price: string;
	rating_info: string;
	title: string;
	thumbnail: string;
	url: string;
};

export type YoutubeData = {
	path: string;
	thumbnail: string;
	file: string;
};

export type Todo = {
	id: string;
	title: string;
	description: string;
};

export type PromptOptions = {
	token: string | null;
	prompt: string | null;
	exclude: string;
	ratio: string;
	count: string;
};
