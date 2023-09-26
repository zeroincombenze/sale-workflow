{
    "name": "Sale Order Type Improvement",
    "version": "12.0.0.1.0",
    "category": "Sale Management",
    "summary": "Sale Order Base Stock Management",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/crm",
    "development_status": "Alpha",
    "license": "AGPL-3",
    "depends": [
        "sale_stock",
        "sale_order_type",
        "stock",
    ],
    "version_depends": ["sale_stock==12.0.1.0"],
    "data": [
        "views/sale_order_type_view.xml",
        "views/stock_picking_view.xml",
    ],
    "pre_init_hook": "check_4_depending",
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
