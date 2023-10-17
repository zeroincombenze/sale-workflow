{
    "name": "On Consignment and For Evaluation workflow",
    "version": "12.0.0.1.0",
    "category": "Sale Management",
    "summary": "On Consignment and For Evaluation Sale management",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/crm",
    "development_status": "Alpha",
    "license": "AGPL-3",
    "depends": [
        "sale_order_type_plus",
        "l10n_it_ddt",
    ],
    "data": [
        "data/stock_location.xml",
        "data/stock_data.xml",
        "data/sale_order_type.xml",
        "views/sale_order_type_view.xml",
    ],
    "post_init_hook": "set_product_routes_post",
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
