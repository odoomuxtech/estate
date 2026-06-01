{
    'name': 'Real Estate',
    'summary': 'Estate Management System',
    'version': '1.0.0',
    'license': 'OEEL-1',
    'description': 'Estate Management System',
    'author': 'Estate Management System',
    'website': 'https://www.estate.com',
    'category': 'Estate',
    'depends': ['crm'],
    'application': True,
    'data': [
        # Security
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        # Views
        'views/estate_property_views.xml',
        # Menus
        'views/estate_menus.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}