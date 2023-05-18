# -*- coding: utf-8 -*-
{
    'name': "report_invoice",

    'summary': """
        MODULO PARA CREAR REPORTES PARA FACTURAS
        """,

    'description': """
        MODULO PARA CREAR REPORTES PARA FACTURAS
    """,

    'author': "Rainier Peña",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    
    #SE AGREGÓ EL MODULO WEB QUE ES LA BASE PARA HACER REPORTE
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        #LOS ARCHIVOS DATA VAN PRIMERO 
        'data/paper_format.xml',
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/einvoice_a4.xml',
        'reports/einvoice_ticket.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
