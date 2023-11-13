Questo modulo aggiunge alcune caratteristiche al tipo di ordine.

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
