# PARA_ALEXIS: el testigo de guardas desmiente el estado del sello

La vuelta 1 cerro su apertura ciega con **una guarda en ROJO en el instante del
sello**, y por eso el sello NO se acepta (D.38.3 ensanchada el 16 sep 2026).

Lo que el testigo registro:

EL SELLO NO SE ACEPTA: 1 guarda(s) en rojo al sellar.
  la guarda 'guiones' estaba en ROJO en el instante del sello (2026-09-16 21:19:13). Una cifra vale en el instante del sello (D.38.3, 16 sep 2026): si al cerrar hay un rojo, la tabla de cierre no se escribio DESPUES de volver a correr las guardas. BARRIDO DE GUIONES EN ROJO: 4 hallazgo(s)

QUE SIGNIFICA. Una cifra vale en el instante del sello. Si al cerrar hay una guarda
en rojo, la tabla de cierre de la pagina **no se escribio despues de volver a correr
las guardas**, asi que cualquier cifra de estado que publique puede haber caducado
entre la medida y el sello. Le paso a la vuelta 29 con 44 minutos y cinco guiones en
medio, y costo una racha entera.

QUE NO SIGNIFICA. No dice que la clasificacion sea falsa ni que el trabajo este mal.
Dice que el estado que la pagina publica no se puede firmar.

Estado: rama extraccion-gerber_emyth, hash 6d2d56a.

Como retomar: deja el arbol limpio (lo que ensucio la guarda suele ser un fichero de
trabajo de la propia fase ciega), borra este fichero y relanza. El auditor vuelve a
abrir y esta vez el testigo lo confirma.
