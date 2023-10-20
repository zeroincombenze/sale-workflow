from odoo import fields, models, _


class SaleOrderType(models.Model):
    _inherit = "sale.order.type"

    location_dest_id = fields.Many2one(
        comodel_name="stock.location",
        domain=[("usage", "=", 'customer')],
        string="Destination Location",
        help="Force the destination location rather than using customer location"
    )
    owner_mode = fields.Selection(
        selection=[
            ("assign", _("Assign")),
            ("anonymize", _("Anonymize")),
        ],
        string="Stock Owner Mode",
        help=(
            "When picking is assigned the ownership of stock mey be automatically"
            " assigned (if value is 'assign') or anonymized (if value is 'anonymize')"
            " or neither assignment neither anonymizing will be done"
        )
    )
    auto_validate_picking = fields.Selection(
        [
            ("none", _("None")),
            ("validate", _("Validate")),
            ('lot_filled', _('Only with lots/serial numbers filled')),
            ('assign', _('Only assign lots/serial numbers filled')),
        ],
        default="none",
        required=True,
        help="Pickings are confirmed automatically upon sale confirmation:"
        " always, if you set '" + _("Validate") + "' or else just if all order lines"
        " have lot/serial number (this feature requires lot/serial number activation"
        " and supplemental module installed."
    )
