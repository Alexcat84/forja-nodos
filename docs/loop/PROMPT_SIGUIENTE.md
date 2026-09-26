# ENCARGO DE LA VUELTA 74: **SANEAMIENTO. SE PAGAN `d078` Y `d077`, QUE SON DE LAS FICHAS DE GROVE QUE QUEDAN, Y `d084` CON `d006`, LA FIRMA DE FIDELIDAD QUE LE FALTA A `cap_13` DE SCOTT. NO SE INSERTA NADA Y NO SE TOCA NI UN BYTE DE LA BANDEJA DE GROVE**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 72`, que audito la vuelta `73`.
`AUDITOR_FORJA.md` seccion `1.4`. **Toda cifra de medida de esta pagina va dentro de un bloque `$` con su salida, o lleva en
su misma linea la seccion de la `ACTA 72` donde esta pegada** (`R8`, `ACTA 72` `72.11`).*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: SANEAMIENTO**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **POR QUE ESTA VUELTA NO INSERTA, Y LO DICE EL INSTRUMENTO**

    $ python scripts/deuda.py --clase 74
    SANEAMIENTO
      han pasado 5 vuelta(s) desde la ultima de saneamiento (la 69) y la cadencia es 5, con 55 deuda(s) pendientes

**La cadencia la cuenta el registro, no el encargo** (`D.58`): esta vuelta **no inserta nada**, y las fichas de Grove que dejo
listas la `73` entran en la vuelta siguiente, contra la huella que la `73` sello y la `ACTA 72` reprodujo (`72.1`). **Por eso
esta vuelta no toca `cuarentena/`**: una ficha que cambie ahora deja sin valor su barrido y su huella (`d031`).

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_18), citando su frontera. D.50.

**La frase de *continuar desde `cap_18`* es de extraccion y no aplica**: Grove esta minado entero. `d084` y `d006` leen nodos
que ya viven en el grafo, de `scott_radical_candor`, que esta `INSERTADO`: **leerlos no es tomar ese libro**, y no se escribe
nada suyo.

**PUEDES LANZAR TRABAJOS DE FONDO, PERO NINGUNO VIVO AL CERRAR TU TURNO**: los recoges todos dentro, vigilandolos si tardan.
**Si no te caben, no los lances: lo dices en el reporte.** Y **NINGUN `insertar`**, ni en primer plano ni de fondo.

**Las deudas que paga esta vuelta**, tal como estan en el registro:

    $ python scripts/deuda.py | grep -E "^  (d006|d077|d078|d084) "
      d006   41      relectura          cap_13 entero esta en 4 de 212, el 1,89 por ciento, 
      d077   58      aduana             LA TANDA 58 ESCRIBIO SUS SIETE FICHAS EN UN LOTE DE 
      d078   58      relectura          responder_primer_aviso_renuncia_subordinado TRAE P3 
      d084   59      relectura          d006 se pago sobre un 154 rancio. El libro mayor de 

**Su texto entero esta en `docs/loop/DEUDA.jsonl`**, y lo lees entero antes de pagar ninguna.

---

## TAREA 1: **REGISTROS DE LA `ACTA 72`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Tu vuelta, reproducida**: lo que movio fuera de `docs/loop/` y de `.v73ext/` son las fichas corregidas, sin tocar grafo, bitacora ni censos; tus instrumentos dan lo que pegaste | `ACTA 72` `72.1` |
| **Tu fidelidad, tu barrido y tus veredictos, cruzados enteros contra mi lectura sellada**: la unica diferencia es `D73.9` | `72.3` |
| **Tus diez discutibles se sostienen**, `D73.1` a `D73.10`; **`D73.9` lo gana tu lectura**, y la `ACTA 60` `60.5` par `2` se corrige por correccion declarada | `72.5` |
| **Una afirmacion falsa tuya**: la fila `D73.2` de tu tabla `73.5.d` dice *despues del commit*, y el barrido arranco antes; la sustancia de `d031` se cumple. `REPORTE` en tabla | `72.2`, `72.7` |
| **`R5` cumplido** en tu tramo | `72.0` |

## TAREA 2: **`d078` Y `d077`, LAS DEUDAS DE LAS FICHAS DE GROVE**

1. **`d078`** pide decidir el dia de la insercion si los pasos `3` y `5` de `responder_primer_aviso_renuncia_subordinado` se funden.
   **Ya esta decidido**: tu `D73.5` los dejo los dos, por lo que el `5` trae y el `3` no, y la `ACTA 72` `72.5` lo sostuvo. **Se paga
   citando esas secciones**, y la ficha no se toca.
2. **`d077`** pide releer las fichas de la tanda `58` contra su cola de lectura real antes de que entren. **Primero, cuales son**,
   por instrumento y no de memoria: las fechas de la cita de `d077` y lo que sus fichas dicen de si mismas, en la bandeja o en
   `cuarentena/_insertados/grove_high_output/`. **Despues, una fila por ficha**: en que vuelta se barrio sobre grafo mas bandejas
   antes de entrar o de quedar lista, que acta firmo ese barrido y sus lineas, y **si alguna lectura de vecino le cambio el
   texto**. Si alguna entro sin barrido de su dia, **no la pagas: lo dices con su fila**.
3. **Paga con `python scripts/deuda.py --pagar <id> --vuelta 74 --como "..."`**, con el `como` en un fichero de `.v74ext/`, y
   declara la vuelta con `python scripts/deuda.py --saneamiento --vuelta 74`, como la `69`.

## TAREA 3: **`d084` Y `d006`: LA FIDELIDAD DE LOS NODOS DE `cap_13` DE SCOTT QUE NADIE HA FIRMADO**

Los que nombra `d084`, **leidos contra `fuentes/scott_radical_candor/cap_13.md` entero**, cada paso marcado `T` o `P` con su
linea, en un fichero con una fila por paso como `.v73ext/fidelidad.tsv`, y sus citas comprobadas con una copia de
`.v73ext/citas.sh`. Sus pasos, por instrumento:

    $ python -c "import json; ids=['contar_cuatro_historias_propias_ver_hueco_intencion','dar_elogio_disciplina_igual_critica','medir_critica_respuesta_oyente_brujula']; [print(d['id'], len(d['pasos_accionables']), 'pasos') for d in map(json.loads, open('dataset/nodos.jsonl', encoding='utf-8')) if d['id'] in ids]"
    contar_cuatro_historias_propias_ver_hueco_intencion 17 pasos
    dar_elogio_disciplina_igual_critica 20 pasos
    medir_critica_respuesta_oyente_brujula 33 pasos

1. **La clausula reescrita CUENTA como `P`** (`ACTA 62` `62.5`), y **la posibilidad convertida en orden tambien** (`D71.9`,
   sostenida en la `ACTA 70` `70.5`; `D73.3`, sostenida en la `ACTA 72` `72.5`). **Marca discutible todo paso en que dudes, al
   escribirlo.**
2. **ESTOS NODOS VIVEN EN EL GRAFO: NO LOS CORRIGES.** Si encuentras un `PUENTE`, **no tocas `dataset/`, ni la bitacora, ni los
   censos**: lo escribes con su texto, su linea y la correccion que propones, y **lo traes**. Un puente en el grafo es la guarda
   de fidelidad `D.30`, y **eso lo adjudica la `ACTA 73` antes de que nadie mueva un dato.**
3. **`PASOS INVENTADOS`, una fila por nodo y el total del capitulo**, por una copia de `.v73ext/contar_fidelidad.py`, y el libro
   mayor de la `ACTA 58` `58.2.d` vuelto a correr al final (`python .v60aud/libro_mayor_cap13.py`), pegado. **`d084` y `d006` se
   pagan solo si tu fichero de filas cubre, uno por uno, los pasos que su linea *SIN FIRMA DE NADIE* cuenta**, y la firma es
   la de la `ACTA 73`: tu pagas, yo firmo, y si mi firma no llega el pago se corrige por correccion declarada.

**Si no te cabe entero, parte por nodo**, el mas corto primero, y **lo que no hagas lo dices con su fila vacia**: `d084` queda
pendiente con lo que falte.

## TAREA 4: **EL CIERRE**

- **El censo antes y despues**, con una copia de `.v73ext/censo.sh`: **no se mueve nada.** Grafo, bitacora, pares mutuos,
  bandeja de Grove e insertados al abrir son los de la `ACTA 72` `72.1`, y al cerrar tienen que ser los mismos.
- **Las fichas de Grove, byte a byte las que sello la `73`**: `python .v73ext/pasos_y_huellas.py` vuelto a correr, con su salida
  identica a `.v73ext/pasos_y_huellas.txt`, pegado.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera
  cambiada a la `74`, y pegado.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`,
  **pegados**. **El cierre estricto tiene que salir en verde: cualquier rojo es tuyo.**
- Commitea `docs/loop/` y tu carpeta `.v74ext/`. **Si nada te obliga a parar, no escribas `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO INSERTAS NADA**, y **NO TERMINAS TU TURNO CON NADA VIVO**.
- **NO TOCAS `cuarentena/`**, ni la bandeja de Grove ni las de Gerber y Marquet.
- **NO TOCAS `dataset/`, `bitacora/` NI `censos/`**: esta vuelta lee y paga, no mueve dato.
- **NO TOCAS `src/`, `scripts/`, el banco, el arnes ni los protocolos** (`7.F`, `D.55`), **ni `APERTURA_CIEGA.md`**. Los procesos
  del fundador que veas vivos en otra copia no son tuyos: ni los tocas ni los esperas.
- **NO PAGAS NINGUNA DEUDA QUE ESTE ENCARGO NO NOMBRE**, y **NO ABRES NINGUN LIBRO.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
