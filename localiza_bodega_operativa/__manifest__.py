# -*- coding: utf-8 -*-
{
    'name': 'Localiza Bodega Operativa V5 Unificada',
    'version': '19.0.5.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Gestión integral de bodega: artículos, puestos, GPS, entregas y base para formularios operativos',
    'description': '''
Localiza Bodega Operativa
=========================
App integrada con Inventario para controlar productos operativos, GPS seriados,
puestos, entregas y carga masiva desde Excel.
    ''',
    'author': 'XIM Technology / Localiza',
    'website': 'https://ximpower.com',
    'license': 'LGPL-3',
    'depends': ['stock', 'product', 'contacts', 'mail', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequences.xml',
        'data/product_categories.xml',
        'data/stock_locations.xml',
        'views/product_template_views.xml',
        'views/localiza_articulo_views.xml',
        'views/localiza_puesto_views.xml',
        'views/localiza_gps_equipo_views.xml',
        'views/localiza_entrega_views.xml',
        'views/localiza_dashboard_views.xml',
        'wizard/localiza_import_wizard_views.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'localiza_bodega_operativa/static/src/scss/localiza_backend.scss',
        ],
    },
    'application': True,
    'installable': True,
}
