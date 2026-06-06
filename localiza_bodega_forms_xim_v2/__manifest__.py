{
    'name': 'Localiza Bodega Forms XIM V5 Unificada',
    'version': '19.0.5.0.0',
    'summary': 'Formularios operativos V2 integrados a Bodega Operativa',
    'description': '''
Complemento V5 para Localiza Bodega Operativa.
Agrega formularios independientes, secciones relacionales, líneas de artículos,
carga masiva, panel visual tipo operaciones y reportes PDF imprimibles.
''',
    'author': 'XIM Power / Localiza',
    'website': 'https://ximpower.com',
    'category': 'Inventory/Inventory',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'product', 'stock', 'hr', 'localiza_bodega_operativa'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/form_sections.xml',
        'data/dashboard_cards.xml',
        'data/unified_dashboard_cards.xml',
        'views/form_section_views.xml',
        'views/operational_form_views.xml',
        'views/form_import_views.xml',
        'views/forms_dashboard_views.xml',
        'views/unified_dashboard_views.xml',
        'reports/operational_form_report.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
}
