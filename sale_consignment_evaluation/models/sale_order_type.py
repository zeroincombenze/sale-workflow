from odoo import fields, models


class SaleOrderType(models.Model):
    _inherit = "sale.order.type"

    transportation_reason_id = fields.Many2one(
        comodel_name="stock.picking.transportation_reason",
        string="Transportation Reason")

