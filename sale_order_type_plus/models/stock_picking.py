from odoo import api, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def action_assign(self):
        super().action_assign()
        for picking in self:
            picking.owner_id = picking.partner_id
            picking.action_assign_owner()
