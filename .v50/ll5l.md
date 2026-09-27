
### LL.5.l. **`cerrar_reporte.py`, LA QUINTA GUARDA, CORRIDA Y PEGADA** (`EXTRACTOR.md` 12.6, `D.41`)

<!-- TALLADO: parcial salida=.v50/cerrar_reporte_cola.txt -->

    $ python scripts/cerrar_reporte.py     (la cola, sin las 72 lineas de rancio)
    [cierre] tabla de cierre de tareas (D.52)
    [cierre] gate de integridad
    [cierre] barrido de guiones
    [cierre] prueba de aceptacion
    [cierre] vigencia de los veredictos (D.15): COLA DE TRABAJO, no guarda

    LA VIGENCIA TIENE COLA, Y ESO NO PONE EL CIERRE EN ROJO (D.15).
    Un rancio no se cita como vigente: se relee con el texto de hoy,
    o se declara por que sigue valiendo. Las dos cosas las hace una
    persona, y por eso esto no pone nada en rojo.

    CIERRE VERDE: las cuatro guardas que muerden, el tallado y el censo. La vigencia corrio y publico su cuenta arriba: es cola, no guarda (D.15).

**CIERRE VERDE A LA PRIMERA**, y el tallado corrio **en estricto**, que es lo que esta guarda anade
sobre el hook.

**LA COLA DE VIGENCIA SIGUE EN `72` Y NINGUNO DE LOS `72` ES MIO, Y NO LO PROMETO: LO MIDO.**
`D.38.4` manda que la vigencia mida **grafo mas bandejas**, asi que **retocar nueve fichas de
cuarentena y anadir tres si podria volver rancio un veredicto.** No ha pasado:

<!-- TALLADO: parcial salida=.v50/rancio_ninguno_mio.txt -->

    $ grep -c "RANCIO" .v50/cerrar_reporte.txt
    72
    $ grep -c "<las 9 fichas corregidas y los 3 candidatos nuevos>" .v50/cerrar_reporte.txt
    0

**Cero de los `72` nombra a ninguna de las `12` fichas que toque o escribi hoy.** Los `72` son de
`scott_radical_candor` y vienen de antes de esta vuelta. **Y la cuenta coincide con la que la
vuelta 49 publico en `KK.5.k`, que cito como contraste y no como fuente** (`EXTRACTOR.md` 5): mi
cifra sale del `grep` de arriba, corrido hoy. **Que no se haya movido tiene explicacion medible:**
esta vuelta no toco ni una linea de `bitacora/VEREDICTOS.jsonl` (`LL.5.a`: sigue en `740`), y **las
fichas que cambiaron no tienen veredicto escrito**, porque ninguna ha entrado nunca por la aduana.

**Y LO QUE SI PUEDO DECIR ESTA VEZ Y LA VUELTA 49 NO PUDO:** aquella no midio la cola al abrir y
tuvo que declararlo. **Yo tampoco la medi al abrir, y lo digo igual**: lo que sostengo no es que
fueran `72` antes, sino **que cero de los `72` de hoy cuelga de algo que yo haya tocado**, y eso es
exactamente lo que el `grep` de arriba mide.
