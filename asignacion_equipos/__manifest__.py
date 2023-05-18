# -*- coding: utf-8 -*-
{
    'name': "asignacion_equipos",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Rainier Peña",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        #data va de primero
        'data/seq.xml',
        
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/type_equipment.xml',
        
        #LAS VISTAS MENU VAN DE ULTIMAS
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
