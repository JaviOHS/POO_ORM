module.exports = {
  darkMode: 'class',
  content: [
    'orm_project/**/*.html',
    'orm_project/**/*.js',
    'node_modules/preline/dist/*.js',
    // Añade otros tipos de archivos donde utilices Tailwind CSS
  ],
  theme: {
    extend: {
      fontFamily: {
        'quicksand': ['Quicksand', 'sans-serif'],
      },
    }
  },
  plugins: [
    require('preline/plugin'),
  ],
}
