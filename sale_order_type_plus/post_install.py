from odoo import api, SUPERUSER_ID
import logging
_logger = logging.getLogger(__name__)


def set_product_routes(cr):
    """Assign evaluation and consignment routes to all products.

    Args:
        cr (obj): sql cursor

    Returns:
        None
    """
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        tmpl_model = env["product.template"]
        route = env.ref("sale_order_type_plus.route_sale_evaluation")
        tmpl_model.search([]).write(
            {"route_ids": [(4, route.id)]})
        route = env.ref("sale_order_type_plus.route_sale_consignment")
        tmpl_model.search([]).write(
            {"route_ids": [(4, route.id)]})
        _logger.info("Products routes set.")


def set_product_routes_post(cr, registry):
    set_product_routes(cr)
