# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import api
from openerp.osv import osv, fields

class SaleLayoutCategory(osv.Model):
    _inherit = 'sale_layout.category'

    textonly = fields.boolean('Text-only section')
