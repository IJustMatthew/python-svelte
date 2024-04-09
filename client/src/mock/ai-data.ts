import type { SelectOption } from 'src/types';

export const aspectRatioOptions: SelectOption[] = [
	{ id: '1:1-512', text: `5120*512 (1/1)` },
	{ id: '1:1-1024', text: `1024*1024 (1/1)` },
	{ id: '16/9-1280', text: `1280*720 (16/9)` },
	{ id: '16/9-1920', text: `1920*1080 (16/9)` }
];

export const countOptions: SelectOption[] = [
	{ id: '1', text: '1 Image' },
	{ id: '2', text: '2 Images' },
	{ id: '3', text: '3 Images' },
	{ id: '4', text: '4 Images' }
];
