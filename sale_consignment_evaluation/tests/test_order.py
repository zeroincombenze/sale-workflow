import os
import logging
from .testenv import MainTest as SingleTransactionCase

_logger = logging.getLogger(__name__)

TEST_SALE_ORDER = {
    "z0bug.sale_order_1": {
        "date_order": "####-##-##",
        "partner_id": "base.res_partner_2",
        "type_id": "sale_consignment_evaluation.evaluation_sale_type",
    },
}

TEST_SETUP_LIST = [
    "sale.order",
]


class TestOrder(SingleTransactionCase):

    def setUp(self):
        super().setUp()
        # Add following statement just for get debug information
        self.debug_level = 0
        data = {"TEST_SETUP_LIST": TEST_SETUP_LIST}
        for resource in TEST_SETUP_LIST:
            item = "TEST_%s" % resource.upper().replace(".", "_")
            data[item] = globals()[item]
        self.declare_all_data(data)  # TestEnv swallows the data
        self.setup_env()  # Create test environment

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

