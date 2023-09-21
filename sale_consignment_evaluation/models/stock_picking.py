from odoo import api, models, fields, _


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    owner_mode = fields.Selection(
        selection=[
            ("assign", _("Assign")),
            ("anonimize", _("Anonimize")),
        ],
        string="Stock Owner Mode",
    )


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def action_assign(self):
        super().action_assign()
        for picking in self:
            if picking.picking_type_id.owner_mode == "assign":
                picking.owner_id = picking.partner_id
                picking.action_assign_owner()
            elif picking.picking_type_id.owner_mode == "anonimize":
                picking.move_line_ids.write({'owner_id': False})
