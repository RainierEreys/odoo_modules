# -*- coding: utf-8 -*-
{
    'name': "odoo_framework",

    'summary': """
       Este modulo esta hecho para agregar campos a un modelo ya existente y 
        colocarlo en la vista de contactos, especificamente en la pestaña 'Datos adicionales'
        """,

    'description': """
        Este modulo esta hecho para agregar campos a un modelo ya existente y 
        colocarlo en la vista de contactos, especificamente en la pestaña 'Datos adicionales'
    """,

    'author': "Rainier Peña",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_partner_hb.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
