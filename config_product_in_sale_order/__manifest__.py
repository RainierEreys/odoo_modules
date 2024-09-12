{
    'name': "Configurador de Productos",
    'summary': """MathData""",
    'description': """
        MathData configurador de productos para subscripcion de usuario
    """,
    'category': 'Uncategorized',
    'depends': ['base','website','sale','sale_subscription'],
    'installable': True,
    'application': True,    
    'data': [        
        'security/ir.model.access.csv',
        'views/config_product.xml',                
    ],
    'assets':{
        'web.assets_frontend':[
            'config_product_in_sale_order/static/src/scss/estilos_configurados.scss',
            'config_product_in_sale_order/static/src/js/config_product_subscription.js',
        ]
    },
    "license": "LGPL-3",
}