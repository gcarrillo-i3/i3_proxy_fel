# -*- encoding: utf-8 -*-

{
    'name': 'i3_proxy',
    'version': '17.0.0.0.1',
    'category': 'Invoicing',
    'summary': 'Módulo Certificar en Guatemala-SAT',
    'description': """ 
# **Certificación SAT Guatemala por I3 y Felplex**

Este módulo está diseñado para facilitar la certificación ante la **Superintendencia de Administración Tributaria (SAT)** de Guatemala directamente desde **Odoo**. Con esta herramienta, las empresas pueden emitir **Documentos Tributarios Electrónicos (DTE)** de prueba, asegurando que cumplen con los requisitos establecidos por la SAT para la facturación electrónica.

## **Características principales:**

- ### **📄 Diario Preconfigurado**
  - El módulo crea un diario específico llamado **`FACT FELPLEX/I3`**, el cual está completamente configurado y listo para ser utilizado por un certificador autorizado para emitir hasta **5 DTE de prueba**.

- ### **🔗 Integración Sencilla**
  - Integra sin problemas los procesos de facturación en **Odoo** con los requerimientos de la **SAT**, asegurando una transición fluida hacia la certificación.

- ### **✅ Compatibilidad y Conformidad**
  - Asegura que todas las emisiones de prueba cumplen con las normativas vigentes, proporcionando un entorno controlado para realizar las pruebas necesarias antes de la certificación final.

---

Este módulo es una herramienta esencial para cualquier empresa en Guatemala que busque certificar sus procesos de facturación electrónica con la **SAT** de manera rápida y eficiente, directamente desde **Odoo**.

---
                    """,
    'author': 'Integración Inteligente de Información S.A.',
    'website': 'https://portal.i3.gt/',
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
