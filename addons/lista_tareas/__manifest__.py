# -*- coding: utf-8 -*-
{
    'name': "Lista de Tareas",

    'summary': "Módulo de pruebas de Odoo probando cosas 3ra Parte",

    'description': """
Módulo de pruebas de Odoo en el que se listan tareas al más puro estilo agenda
    """,

    'author': "Cristian",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.12',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

