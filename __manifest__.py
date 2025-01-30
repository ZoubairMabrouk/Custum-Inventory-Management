# -*- coding: utf-8 -*-
{
    'name': "Inventory Management",

    'summary': "Simplified Inventory Management",

    'description': "Manage products, stock entries, exits, and low-stock notifications.",

    'author': "Zoubair MABROUK",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock','product','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/inventory_view.xml',
        'views/product_view.xml',
        'views/menu_view.xml',
        'data/ir_model_data.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['ex-module/static/icon.png'],
    'icon':'ex-module/static/icon.png',
    'application':True,
    'installable': True,
    'auto_install': False,
}
