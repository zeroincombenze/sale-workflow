=================================================================
|icon| Sale Order Type Improvement/Tipo ordine evoluto 12.0.0.1.0
=================================================================

**S.O. type to manage On Consignment / For Evaluation**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/sale-workflow/12.0/sale_order_type_plus/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| This module adds some features to order type (see below Features for more info).

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


|it| Questo modulo aggiunge alcune caratteristiche al tipo di ordine.

**Ubicazione di destinazione**

SI può forzare l'ubicazione di destinazione in base al tipo di ordine. Se il campo è
lasciato vuoto viene eseguito il normale processo di Odoo che è ubicazione clienti.

**Assegnazione o deassegnazione automatica del proprietario dello stock**

Quanto un prelievo è confermato, il proprieatrio dello stock può essere assegnato,
deassegnato o nessuna operazione è eseguita. Questa caratteristica è indispensabile
per alcuni tipi di ordine, quali:

* Ordine di conto visione
* Ordine di conto deposito
* Ordine di conto lavoro

Lasciare vuoto per gestione manuale.

**Validazione automatica del prelievo alla conferma ordine**

Forza la conferma del prelievo alla conferma dell'ordine.

**Metodo consegna quantità**

Questo campo forza il Metodo consegna quantità su tutte le righe dell'ordine.
Un nuovo metodo "Dopo reso" è disponibile. Le quantità consegnate di tutte le righe con
questo metodo sono impostate a zero alla conferma del prelievo. Il valore reale sarà
calcolato da specifica conferma di prelievo per vendita.

Questa caratteristica è indispensabile per alcuni tipi di ordine (vedere sopra
*Assegnazione o deassegnazione automatica ...*)


**No per vendita**

Di norma, gli ordini iniziano il processo di vendita che termina con un una fattura.
Questa impostazione dichiara che l'ordine non è per la vendita. Il metodo di calcolo
di consegna quantità è impostata con "Dopo reso" (vedere
sopra *Metodo consegna quantità*).



Features | Caratteristiche
--------------------------

+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Description | Descrizione                                                | Z0incomben | OCA | Note(s)                                          |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Version | Versione                                                       | 12.0.0.1.0 | N/D | Compared with *sale_order_type* 12.0.1.3.0       |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Order Number sequence | Sequenza numerazione                             | ✅         | ✅  |                                                  |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Journal_id | Registro sezionale                                          | ✅         | ✅  |                                                  |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Warehouse | Magazzino                                                    | ✅         | ✅  |                                                  |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Picking policy | Politica di prelievo                                    | ✅         | ✅  |                                                  |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Company | Azienda                                                        | ✅         | ✅  |                                                  |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Payment term | Termini di pagamento                                      | ✅         | ✅  |                                                  |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Price list | Listino                                                     | ✅         | ✅  |                                                  |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Incoterms|Incoterm                                                       | ✅         | ✅  |                                                  |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Route | Rotta                                                            | ✅         | ✅  |                                                  |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Analytic account | Conto analitico                                       | ✅         | ✅  |                                                  |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Destination location | Ubicazione di destinazione                        | ✅         | ❌  |                                                  |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| S.N./Lot from SO to Picking | Lotti/n.serie in prelievo da ordine        | ✅         | ❌  | Requires *sale_order_lot_selection* module       |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Auto confirm picking upon SO confirmation | Conferma prelievo all'ordine | ✅         | ❌  |                                                  |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Assign stock owner | Assegna proprietario stock                          | ✅         | ❌  | Used by *sale_consignment_evaluation* module     |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Deassign stock owner | Deassegna proprietario stock                      | ✅         | ❌  | Used by *rma_sale_consignment_evaluation* module |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Compute delivery q.ty on demand | Calcolo q.tà consegnata su richiesta   | ✅         | ❌  | Used by *rma_sale_consignment_evaluation* module |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+
| Not for sale | No per vendita                                            | ✅         | ❌  | Used by *sale_consignment_evaluation* module     |
+--------------------------------------------------------------------------+------------+-----+--------------------------------------------------+



Configuration | Configurazione
------------------------------

To configure Sale Order Types you need to:

☰ Sales > Configuration > Sales Orders Types >
Create a new sale order type with all the settings you want

The field **Picking Auto Confirmation** requires module *sale_order_lot_selection*.



Usage | Utilizzo
----------------

☰  Sales > Sales Orders, and create a new sale order.

Select the new type you have created before and all settings will be propagated.



Getting started | Primi passi
=============================

|Try Me|


Prerequisites | Prerequisiti
----------------------------

* python 3.7
* postgresql 9.6+ (best 10.0+)

::

    cd $HOME
    # Follow statements activate deployment, installation and upgrade tools
    cd $HOME
    [[ ! -d ./tools ]] && git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -pUT
    source $HOME/devel/activate_tools



Installation | Installazione
----------------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instructions are just an  | Istruzioni di esempio valide solo per    |
| example; use on Linux CentOS 7+ | distribuzioni Linux CentOS 7+,           |
| Ubuntu 14+ and Debian 8+        | Ubuntu 14+ e Debian 8+                   |
|                                 |                                          |
| Installation is built with:     | L'installazione è costruita con:         |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://zeroincombenze-tools.readthedocs.io/>`__ |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| $HOME/12.0 |
+----------------------------------------------------------------------------+

::

    # Installation based on `zeroincombenze® tools <https://zeroincombenze-tools.readthedocs.io/en/latest/>`__
    # Odoo repository installation; OCB repository must be installed
    deploy_odoo clone -r sale-workflow -b 12.0 -G zero -p $HOME/12.0
    # Upgrade virtual environment
    vem amend $HOME/12.0/venv_odoo



Upgrade | Aggiornamento
-----------------------

::

    # Upgrade based on zeroincombenze® tools
    deploy_odoo update -r sale-workflow -b 12.0 -G zero -p $HOME/12.0
    vem amend $HOME/12.0/venv_odoo
    # Adjust following statements as per your system
    sudo systemctl restart odoo



Support | Supporto
------------------

|Zeroincombenze| This module is supported by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__



Get involved | Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/sale-workflow/issues>`_.

In case of trouble, please check there if your issue has already been reported.



Known issues | Roadmap
----------------------

This module replaces the standard Odoo function ``sale.order._action_launch_stock_rule()``
of the module *sale_stock*. The function, now can use the destination location different
from the partner destination location.
In this way is very simple to manage sale order on consignment or for evaluation or
for tolling agreement or for subcontracting.
For this reason, this module depends on specific 12.0.1.0 version of *sale_stock module*

This module may conflict with *sale_order_automatic_workflow* because overlaps some
features of that module. Please choice this module or else
*sale_order_automatic_workflow* but not both.



Proposals for enhancement
-------------------------

|en| If you have a proposal to change this module, you may want to send an email to <cc@shs-av.com> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|it| Se hai proposte per migliorare questo modulo, puoi inviare una mail a <cc@shs-av.com> per un iniziale contatto.



ChangeLog History | Cronologia modifiche
----------------------------------------

12.0.0.1.0 (2023-10-22)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] First version
* [QUA] Test coverage 38% (84: 52+32) [0 TestPoints] - quality rating 20 (target 100)



FAQ | Domande & Risposte
------------------------

*I read about issue! May this module conflict with Odoo modules?*

No. This module is fully integrated with Odoo and OCA modules.
This module checks for Odoo module version. If Odoo module will be updated,
we will ASAP upgrade this module.



Credits | Didascalie
====================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


Authors | Autori
----------------

* `SHS-AV s.r.l. <https://www.zeroincombenze.it>`__



Contributors | Contributi da
----------------------------

* `Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>`__



Maintainer | Manutenzione
-------------------------

* `Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>`__



----------------

|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://www.zeroincombenze.it/>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato da `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sulla propria infrastuttura.
La distribuzione `Zeroincombenze® <https://www.zeroincombenze.it/>`__ è progettata per le esigenze del mercato italiano.


|
|

This module is part of sale-workflow project.

Last Update / Ultimo aggiornamento: 2023-11-14

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-black.png
    :target: https://odoo-community.org/page/development-status
    :alt: 
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/sale-workflow.svg?branch=12.0
    :target: https://travis-ci.com/zeroincombenze/sale-workflow
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/sale-workflow/badge.svg?branch=12.0
    :target: https://coveralls.io/github/zeroincombenze/sale-workflow?branch=12.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/sale-workflow/branch/12.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/sale-workflow/branch/12.0
    :alt: Codecov
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-12.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/12.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-12.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/12.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-12.svg
    :target: https://erp12.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov| image:: https://codecov.io/gh/OCA/sale-workflow/branch/12.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/sale-workflow/branch/12.0
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |halt| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/halt.png
.. |info| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/info.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/Desktoptelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md
.. |chat_with_us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
   :target: https://t.me/Assitenza_clienti_powERP
