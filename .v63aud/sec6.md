**EL ORDEN DENTRO DE LA TANDA NO TIENE PROBLEMA.** Cada madre que leo dentro de la tanda va delante
de su hijo si se inserta por capitulo y por pieza: `construir_flujo...` antes que `rehacer_flujo...`
y este antes que `equilibrar...`; `dimensionar_inventario...` (`cap_02`) antes que
`decidir_aceptar...` (`cap_03`); `representar_actividad_caja_negra...` antes que
`construir_indicador_linealidad...`.

**EL PROBLEMA ESTA FUERA DE LA TANDA, Y LO DECLARO: DOS DE LOS `16` SON HIJOS DE CANDIDATOS DE `d005`,
QUE NO ENTRAN EN ESTA VUELTA.** `dimensionar_plantilla_administrativa_pronostico` tiene dos madres ahi
y `casar_flujo_fabricacion_flujo_ventas` tiene una clara y otra floja (seccion 5.2). **Si los dos
hijos entran ahora**, sus veredictos se escriben sin la madre en el grafo, y **la senial no los va a
levantar cuando las madres entren**, porque hoy no los levanta en ningun sentido. **LECTURA:** o esos
dos esperan a la vuelta que repare `d005`, o su veredicto de hoy deja escrito el par pendiente para que
la vuelta de `d005` declare la arista por lectura. **No es mio decidir el orden** (`D.36`: lo fija quien
autoriza la insercion); lo dejo leido para que la adjudicacion lo tenga delante.

**LAS SERIES (`D.37`): NINGUNA EN LA TANDA.** Los tres textos que cuentan sus partes no tienen las
partes como nodos: *las tres operaciones* de `clasificar_trabajo...` (L39), *los cinco datos* de
`elegir_cinco_indicadores...` (L17 a L27) y *las dos tecnicas* de `elegir_inspeccion...` (L141), que
viven dentro del mismo nodo. Los tres puntos de inspeccion de `cap_03` L131 si tienen dos partes con
nodo (la de recepcion en `dimensionar_inventario...` y la de proceso en `preferir_inspeccion...`),
**pero L131 no tiene nodo cabeza**, asi que no hay arista cabeza a parte que declarar.
