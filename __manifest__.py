# -*- coding: utf-8 -*-
{
    'name': "Almacenes para usuario",

    'summary': """
        Módulo que añade el campo de almacen a los usuarios""",

    'description': """
        1. Añade el campo relacion almacen al modelo de usuarios para utilizar en varios otros modulos 
    """,

    'author': "Grupo Treming",
    'website': "http://www.treming.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '0.1',

    'depends': ['base', 'stock'],

    'data': [
        'views/res_user_view.xml',
    ]
}