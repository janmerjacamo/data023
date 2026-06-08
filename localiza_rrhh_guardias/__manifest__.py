# -*- coding: utf-8 -*-
{
    "name": "Localiza RRHH y Guardias",
    "version": "19.0.1.0.0",
    "category": "Localiza",
    "summary": "Módulo limpio para reemplazar personalizaciones de Odoo Studio.",
    "author": "XIM Power / Localiza",
    "license": "LGPL-3",
    "depends": ['base', 'mail', 'hr', 'hr_payroll', 'localiza_studio_core', 'localiza_activos_lineas'],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/menus.xml",
    ],
    "installable": True,
    "application": True,
}
