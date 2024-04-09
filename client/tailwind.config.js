/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}', './node_modules/flowbite/**/*.js'],
	theme: {
		extend: {
			colors: {
				primary: '#AA00FF'
			}
		}
	},
	plugins: [require('flowbite/plugin')]
};
