from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange('type_id')
    def onchange_type_id(self):
        for order in self:
            if order.type_id and order.type_id.transportation_reason_id:
                order.transportation_reason_id = order.type_id.transportation_reason_id
