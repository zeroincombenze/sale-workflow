This module replaces the standard Odoo function `sale.order._action_launch_stock_rule()`
of the module *sale_stock*. The function, now can use the destination location different
from the partner destination location.
In this way is very simple to manage sale order on consignment or for evaluation or
for tolling agreement or for subcontracting.
For this reason, this module depends on specific 12.0.1.0 version of *sale_stock module*

This module may conflict with *sale_order_automatic_workflow* because overlaps some
features of that module. Please choice this module or else
*sale_order_automatic_workflow* but not both.
