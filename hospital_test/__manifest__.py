{
    'name': 'Hospital test',
    'description': 'Anjeličku môj stražnicku opatruj moju dušičku',
    'author': 'Ja',
    'category': 'Website',
    'installable': True,
    'sequence': 1,
    'version': '16.0.1',
    'depends': ['hr_recruitment'],


    # Views and templates
    'data': [
        'views/menu.xml',
        'views/patient.xml',
        'security/ir.model.access.csv',
    ],

    # Assets (CSS, JS, images)
    'assets': {
        'web.assets_frontend': [
        ],
        'web._assets_primary_variables': [
        ],
    },

    # Images and other media
    'images': [
    ],
    # Other settings
    'auto_install': False,
    'application': False,
    'price': 0,
    'currency': 'USD',
    'license': 'LGPL-3',
}
