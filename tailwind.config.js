/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "project/apps/**/templates/**/*.html",
    "project/templates/**/*.html",
    "./node_modules/tw-elements/dist/js/**/*.js",
    
  ],
  theme: {
    extend: {},
  },
  plugins: [require("tw-elements/dist/plugin.cjs")],
  darkmode: "class"
}

