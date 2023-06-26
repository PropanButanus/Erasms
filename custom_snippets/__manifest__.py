{
    'name': 'Custom Snippets',
    'description': 'Custom Snippets',
    'summary': 'Custom Snippets',
    'author': 'Chinmay Roy',
    'website': 'https://chinmayroy.github.io/',
    'category': 'Website',
    'sequence': 1,
    'version': '16.0.1',
    'depends': ['hr_recruitment'],

    # Security
    'data': [
    ],

    # Views and templates
    'data': [
        'views/snippets/snippets.xml',
        'views/snippets/accordion.xml',
        'views/snippets/dropdown.xml',
        'views/snippets/custom_button.xml',
        'views/snippets/card.xml',
        'views/snippets/carousel.xml',
        'views/snippets/list.xml',
        'views/snippets/navbar.xml',
        'views/snippets/scrollspy.xml',
        'views/snippets/collapse.xml',
        'views/snippets/placeholder.xml',
        # 'views/snippets/options.xml',
    ],

    # Assets (CSS, JS, images)
    'assets': {
        'web.assets_frontend': [
            'custom_snippets/static/src/scss/styles.scss',
            # 'custom_snippets/static/src/js/explore_jobs.js',
            'custom_snippets/static/src/js/fetch_bitcoin_graph.js',
            'custom_snippets/static/src/css/owl.carousel.min.css',
            'custom_snippets/static/src/css/owl.theme.default.min.css',
            'custom_snippets/static/src/js/owl.carousel.min.js',
        ],
        'web._assets_primary_variables': [
            'custom_snippets/static/src/scss/primary_variables.scss',
        ],
    },

    # Images and other media
    'images': [
        'static/description/images/banner.gif',
        'static/description/icon.png',
    ],
    'icon': 'custom_snippets/static/description/icon.png',
    # Other settings
    'auto_install': False,
    'application': False,
    'price': 0,
    'currency': 'USD',
    'license': 'LGPL-3',
    'contributors': [
        'Chinmay Roy <https://chinmayroy.github.io/>',
    ],
}
