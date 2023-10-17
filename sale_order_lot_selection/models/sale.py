from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    lot_id = fields.Many2one(
        'stock.production.lot', 'Lot', copy=False)

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
        super(SaleOrderLine, self).product_id_change()
        self.lot_id = False

    @api.onchange('product_id')
    def _onchange_product_id_set_lot_domain(self):
        available_lot_ids = []
        if self.order_id.warehouse_id and self.product_id:
            location = self.order_id.warehouse_id.lot_stock_id
            quants = self.env['stock.quant'].read_group([
                ('product_id', '=', self.product_id.id),
                ('location_id', 'child_of', location.id),
                ('quantity', '>', 0),
                ('lot_id', '!=', False),
            ], ['lot_id'], 'lot_id')
            available_lot_ids = [quant['lot_id'][0] for quant in quants]
        self.lot_id = False
        return {
            'domain': {'lot_id': [('id', 'in', available_lot_ids)]}
        }


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        # we use this because compatibility with sale exception module
        if isinstance(res, bool) and res:
            for order in self:
                if (
                        not hasattr(order, "type_id")
                        or order.type_id.auto_validate_picking != "lot_filled"
                ):
                    continue
                auto_assign = True
                for line in order.order_line:
                    if line.product_id.tracking in ("lot",
                                                    "serial") and not line.lot_id:
                        auto_assign = False
                        break
                if not auto_assign:
                    continue

                pickings = [p for p in order.picking_ids if p.state == "confirmed"]
                if len(pickings) != 1:
                    continue

                lots = {}
                for line in order.order_line:
                    if line.lot_id:
                        lots[line.lot_id] = line
                auto_validate = True
                for move in pickings[0].move_ids_without_package:
                    for line in move.move_line_ids:
                        if line.lot_id in lots:
                            line.qty_done = min(lots[line.lot_id].product_uom_qty,
                                                line.lot_id.product_qty)
                        else:
                            auto_validate = False
                if auto_validate:
                    pickings[0].button_validate()
        return res
