{
    'name': 'Custom Product Module',
    'version': '1.0',
    'summary': 'Module to call an external API when a field in product.template is updated.',
    'author': 'Your Name',
    'website': 'https://www.felirni.com',
    'category': 'Uncategorized',
    'depends': ['base', 'product'],  # List of dependencies
    'data': [
        'security/ir.model.access.csv',  # Access control rules
        'views/product_template_views.xml',  # Views definition
    ],
    'installable': True,
    'application': True,
}