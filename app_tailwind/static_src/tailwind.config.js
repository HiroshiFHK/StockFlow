module.exports = {
    content: [
        // '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../static/**/*.js',
        // '../../**/templates/**/*.html',
    ],
    theme: {
        extend: {},
        fontFamily: {
            'inter': ['Inter', 'sans-serif'],
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
