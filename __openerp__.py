# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'MFGT - Sale Layout - Text-only section',
    'version': '9.0.0.0.1',
    'author': 'Philipp Hug',
    'category': 'Custom',
    'website': 'https://www.mfgt.ch/',
    'licence': 'LGPL-3',
    'summary': 'Customizations for MFGT',
    'depends': [
        'report',
        'sale',
        'sale_layout',
    ],
    'data': [
        'views/report_invoice_layouted.xml',
        'views/report_quotation_layouted.xml',
#        'views/sale_layout_category_view.xml',
    ],
    'installable': True,
    'application': False,
}
