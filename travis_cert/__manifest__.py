{
    'name': "travis_cert",

    'summary': """
    To send message to custom controller to be informed from the test's results
    """,

    'author': "Fernando La Chica",
    'website': "https://flachica.github.io/fernandolachica/",

    'category': 'Human Resources',
    'version': '13.0.0.1.0',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/test_case.xml',
    ],
    'application': True,
}
