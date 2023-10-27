# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    account_id = fields.Many2one(
        "account.account",
        string="Account",
        domain=[('deprecated', '=', False)],
        help="The income account related to the selected product.")

    @api.multi
    def _prepare_invoice_line(self, qty):
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        if self.account_id:
            res["account_id"] = self.account_id.id
        return res