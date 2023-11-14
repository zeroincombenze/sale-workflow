from odoo import api, models, fields, _


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    owner_mode = fields.Selection(
        selection=[
            ("assign", _("Assign")),
            ("anonymize", _("Anonymize")),
        ],
        string="Stock Owner Mode",
        help=(
            "When picking is assigned the ownership of stock may be automatically"
            " assigned (if value is 'assign') or anonymized (if value is 'anonymize')"
            " or neither assignment neither anonymizing will be done"
        )
    )


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def action_assign(self):
        super().action_assign()
        for picking in self:
            owner_mode = (
                picking.picking_type_id.owner_mode
                or (picking.sale_id.type_id and picking.sale_id.type_id.owner_mode)
            )
            if owner_mode == "assign":
                picking.owner_id = picking.partner_id
                picking.action_assign_owner()
            elif owner_mode == "anonimize":
                picking.move_line_ids.write({'owner_id': False})
