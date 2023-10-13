import os
import logging
from .testenv import MainTest as SingleTransactionCase

_logger = logging.getLogger(__name__)


TEST_STOCK_LOCATION = {
    "z0bug.test_customer_location": {
        "name": "Alternate Customer Location",
        "location_id": "stock.stock_location_locations_partner",
        "usage": "customer",
    },
}

TEST_SALE_ORDER_TYPE = {
    "z0bug.test_sale_order_type": {
        "name": "Test Sale Order Type",
        "warehouse_id": "stock.warehouse0",
        "location_dest_id": "z0bug.test_customer_location",
    },
}

TEST_SALE_ORDER = {
    "z0bug.sale_order_1": {
        "date_order": "####-##-##",
        "partner_id": "base.res_partner_2",
        "type_id": "z0bug.test_sale_order_type",
    },
}

TEST_SALE_ORDER_LINE = {
    "z0bug.sale_order_1_1": {
        "sequence": 1,
        "product_id": "product.product_product_1",
        "order_id": "z0bug.sale_order_1",
        "price_unit": 30.75,
        "product_uom_qty": 10,
        "name": "Virtual Interior Design",
    },
}

TEST_SETUP_LIST = [
    "stock.location",
    "sale.order.type",
    "sale.order",
    "sale.order.line",
]


class TestOrder(SingleTransactionCase):

    def setUp(self):
        super().setUp()
        self.debug_level = 0
        data = {"TEST_SETUP_LIST": TEST_SETUP_LIST}
        for resource in TEST_SETUP_LIST:
            item = "TEST_%s" % resource.upper().replace(".", "_")
            data[item] = globals()[item]
        self.declare_all_data(data)
        self.setup_env()

    def tearDown(self):
        super().tearDown()
        if os.environ.get("ODOO_COMMIT_TEST", ""):  # pragma: no cover
            # Save test environment, so it is available to dump
            self.env.cr.commit()  # pylint: disable=invalid-commit
            _logger.info("✨ Test data committed")

    def test_mytest(self):
        _logger.info(
            "🎺 Testing test_mytest"  # Use unicode char to best log reading
        )
        for xref in TEST_SALE_ORDER:
            order = self.resource_browse(xref)
            order.action_confirm()
            for picking in order.picking_ids:
                if picking.state == "confirmed":
                    picking.action_assign()
                    self.assertEqual("z0bug.test_customer_location",
                                     picking.location_dest_id)

