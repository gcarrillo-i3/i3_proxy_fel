# -*- encoding: utf-8 -*-

{
    'name': 'i3 FEL Guatemala',
    'version': '17.0.0.2.2',
    'category': 'Invoicing',
    'summary': 'Módulo Certificar en Guatemala-SAT',
    'description': """ 
# **Certificación SAT Guatemala por I3 y Felplex**

Este módulo está diseñado para facilitar la certificación ante la **Superintendencia de Administración Tributaria (SAT)** de Guatemala directamente desde **Odoo**. Con esta herramienta, las empresas pueden emitir **Documentos Tributarios Electrónicos (DTE)** de prueba, asegurando que cumplen con los requisitos establecidos por la SAT para la facturación electrónica.

                    """,
    'author': 'Integración Inteligente de Información S.A.',
    'website': 'https://i3.gt/fel',
    'support': 'info@i3.gt',
    'maintainer': 'I3',
    'license': 'OPL-1',
    'category': 'Accounting',
    'images': ['static/description/images/new_banner.gif'],
    'depends': ['account','l10n_gt'],
    'data': [
        'data/cargar_incoterms.xml',
        'data/cargar_diario.xml',
        'views/account_move_view.xml', 
        'views/journal_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
}
