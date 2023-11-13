This module adds some features to order type (see below Features for more info).

**Destination location**

You can force destination location based on order type. If destination location field
is empty, ordinary Odoo process is executed, which is customer location.

**Automatic owner assign or de-assign on picking confirmation**

When picking is confirmed, the owner can be assigned or deassigned or none operation
is done. This feature is useful specific order types, like:

* For for evaluation order
* On consignment order
* Subcontract work (tolling) order

Leave empty for manual management.

**Automatic picking validation upon sale order confirmation**

Force picking validation on sale order confirmation.

**Delivered quantity method**

This field force the delivered method for all sale order lines.
A new method "After Return" is added to list. Delivered quantity of all sale order lines
with this method are set ot zero when picking is confirmed.
Actual delivered quantity will be set on confirmation of "for sale" specific picking.

This feature is useful for specific order type (see above *Automatic owner assign ...*).

**Not for sale**

Usually, sale orders start the sale process which ends with an invoice.
This flag declare that the sale order is not for sale. Delivered quantity in all
sale order lines are set with "After Return" (see above *Delivered quantity method*).
