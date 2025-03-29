/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: ['./App.{js,ts,tsx}', './app/**/*.{js,ts,tsx}', './components/**/*.{js,ts,tsx}'],

  presets: [require('nativewind/preset')],
  theme: {
    extend: {
      fontFamily: {
        mont: ['Montserrat-Regular'],
        montbold: ['Montserrat-Bold'],
        sans: ['Poppins-Regular'],
        poppinssemi: ['Poppins-Semi'],
        poppinsbold: ['Poppins-Bold'],
      },
      colors: {
        // Colores de Spotify
        'spotify-green': '#1DB954',
        'spotify-black': '#191414',
        'spotify-white': '#FFFFFF',
        'spotify-dark-gray': '#282828',
        'spotify-medium-gray': '#535353',
        'spotify-light-gray': '#B3B3B3',
        'spotify-dark-green': '#07301e',
        'spotify-red': '#FF0000',
      },
    },
  },
  plugins: [],
};
