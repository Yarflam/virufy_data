module.exports = {
    plugins: {
        autoprefixer: {},
        'postcss-flexbugs-fixes': {},
        'postcss-for': {},
        'postcss-import': {},
        'postcss-mixins': {},
        'postcss-nesting': {},
        'postcss-percentage': {},
        'postcss-simple-vars': {},
        'postcss-calc': {},
        'postcss-preset-env': {
            stage: 0,
            features: {
                'nesting-rules': true,
                'color-mod-function': true,
                'custom-media': true
            }
        }
    }
};
