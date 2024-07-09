/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],

    theme: {
        extend: {
            fontFamily: {
                body: ['Fira Code']
            }
        },
    },

    plugins: [
        require("@tailwindcss/typography"),
        require('daisyui'),
    ],

    daisyui: {
        themes: ["dracula"]
    },
}

