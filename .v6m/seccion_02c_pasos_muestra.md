
## 2.c. Candidatos, `PASOS INVENTADOS POR CAPITULO`, y la muestra de fidelidad `m6`

**CANDIDATOS ESCRITOS EN ESTA TAREA: `0`.** Ningun `python forja.py informe` que correr: no hay ficha que
pasar por la aduana en seco porque ninguna pieza de `cap_16` ni de `cap_17` paso la prueba del inventario
(`2.a`, `2.b`). Los dos capitulos se firman **LEYENDOLOS ENTEROS** (`EXTRACTOR.md` `17.4`: *un capitulo que
no da nodo se firma leyendolo entero*), que es exactamente lo que las dos tablas de frontera de `2.a` y
`2.b` hacen: cubren el cuerpo completo de cada fichero, `L9` a `L37` y `L9` a `L427`, sin residuo.

| capitulo | pasos escritos | PUENTE | PASOS INVENTADOS | contra el tope de `10` |
|---|---:|---:|---|---|
| `cap_16` (Ripples) | `0` | `0` | **`SIN SUPERFICIE`**, leido entero de `L9` a `L37` | no aplica |
| `cap_17` (Glossary, Notes, Index) | `0` | `0` | **`SIN SUPERFICIE`**, leido entero de `L9` a `L427` | no aplica |
| **el tramo** | **`0`** | **`0`** | **`SIN SUPERFICIE`** | no aplica |

**La muestra de fidelidad, con la semilla de esta vuelta** (`D.58`, `EXTRACTOR.md` `15.4`):

    $ python scripts/muestra_fidelidad.py --libro marquet_turn_the_ship --capitulos cap_16,cap_17 --semilla m6
    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : marquet_turn_the_ship
      semilla  : m6
      capitulos: cap_16, cap_17

      RELEIDO ENTERO : cap_17
      POR MUESTRA    : cap_16, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_16: 0 paso(s) en la muestra

      --- cap_17: ENTERO, 0 paso(s), no hay muestra que elegir

Guardado en `.v6m/muestra/muestra_m6.txt`. **La semilla `m6` elige `cap_17` para relectura entera y `cap_16`
para muestra**, y en los dos casos da `0` porque los dos capitulos tienen `0` pasos: no hay candidato de
`cap_16` ni de `cap_17` en la bandeja de esta vuelta. **Ningun capitulo pasa del `10` por ciento** (no hay
numerador ni denominador): no hay relectura entera que escalar mas alla de la que ya hice pieza por pieza en
`2.a` y `2.b`.

**LOS DOS CAPITULOS QUEDAN MINADOS EN CERO, LEIDOS ENTEROS, CON SU FRONTERA COMPLETA VERIFICADA CONTRA EL
FICHERO.**
