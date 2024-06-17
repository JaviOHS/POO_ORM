module.exports = {
  darkMode: 'class',
  content: [
    'orm_project/**/*.html',
    'orm_project/**/*.js',
    'node_modules/preline/dist/*.js',
    'node_modules/flowbite/**/*.js',    
    // Añade otros tipos de archivos donde utilices Tailwind CSS
  ],
  theme: {
    extend: {
      colors: {
        primary: '#050812',
        secondary: '#070B15',
        content: '#0A0F1A',
        inputs: '#030306',
      },
      fontFamily: {
        'quicksand': ['Quicksand', 'sans-serif'],
        'playwrite': ['Playwrite', 'sans-serif'],
      },
    }
  },
  plugins: [
    require('preline/plugin'),
    require('flowbite/plugin'),
  ],
}
