# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class ProductionLot(models.Model):
    _inherit = "stock.production.lot"

    @api.multi
    def name_get(self):
        res = []
        for lot in self:
            if self.env.context.get("show_qty", False):
                res.append((lot.id, "%s (%s) - %s" % (lot.name,
                                                      lot.product_qty,
                                                      lot.life_date)))
            else:
                res.append((lot.id, lot.name))
        return res
