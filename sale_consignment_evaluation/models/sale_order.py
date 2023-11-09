from odoo import api, models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange('type_id')
    def onchange_type_id(self):
        for order in self:
            if order.type_id and order.type_id.transportation_reason_id:
                order.transportation_reason_id = order.type_id.transportation_reason_id


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    qty_delivered_method = fields.Selection(
        selection_add=[("on_demand", "After return")])

    @api.multi
    @api.depends("product_id")
    def _compute_qty_delivered_method(self):
        super(SaleOrderLine, self)._compute_qty_delivered_method()
        for line in self:
            if line.order_id.type_id.not_sale:
                line.qty_delivered_method = "on_demand"

    def _compute_qty_delivered(self):
        # Actual quantity will be computed by RMA picking
        super(SaleOrderLine, self)._compute_qty_delivered()
        lines = self.filtered(lambda sol: sol.qty_delivered_method == "on_demand")
        for line in lines:
            line.qty_delivered = 0.0
