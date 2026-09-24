
## 3. **LO QUE ENTRO ES LO QUE SE LEYO** (`D.58`, `D.30`)

La fidelidad de los `20` de la tanda esta leida **entera** en dos fases ciegas y adjudicada en dos actas:
los catorce de la `63` sobre `b63405c` (`ACTA 62` `62.5` y `62.6`), los seis de `d005` sobre `997054d`
(`ACTA 63` `63.3.a` y `63.5`). **Lo que mido aqui es si los bytes que entraron son esos**, en dos sitios:
la ficha archivada en `_insertados/` y el nodo del dataset.

    $ python .v65aud/entra_lo_leido.py | tail -3
    filas: 20 | ficha igual a su lectura: 20 | distinta: 0 | nodo igual a su ficha leida fuera de aristas: 20 | distinto: 0
    pasos en el dataset de cap_02: 50
    pasos en el dataset de cap_03: 108

(recortado por el principio: las `20` filas una a una, enteras en `.v65aud/entra_lo_leido.txt`)

**LECTURA:** **los `20` nodos del grafo son, campo a campo, las fichas cuya fidelidad se leyo entera**, y
lo unico que el `insertar` les anadio son aristas (`nodos_previos`, `nodos_siguientes`), que mido en la
seccion `5`. **No hay ficha que releer antes de firmar nada.**

## 4. **`PASOS INVENTADOS POR CAPITULO`, SOBRE LO QUE ENTRO** (`8`, `8.2`, `8.3`)

**Rotulo, para que no se me mueva la poblacion** (`R8`, `ACTA 62`): **los pasos de los `20` nodos que
entraron**, clasificados por **las lecturas enteras de mis dos fases ciegas con las adjudicaciones de las
`ACTA 62` y `63` aplicadas**, no desde cero y no a ojo. El instrumento exige que cada paso del nodo tenga su
fila y que ninguna fila sobre.

    $ python .v65aud/pasos_inventados.py
    adjudicado  construir_grafico_escalonado_pronosticos         paso 5  T -> P  (ACTA 63 63.3.a)
    adjudicado  detectar_arreglar_fallo_etapa_menor_valor        paso 1  D -> T  (ACTA 62 62.5)
    adjudicado  elegir_fabricar_pedido_pronostico                paso 8  T -> P  (ACTA 63 63.3.a)
    adjudicado  emparejar_indicadores_efecto_contraefecto        paso 1  P -> T  (ACTA 63 63.3.a)
    adjudicado  equilibrar_capacidad_personal_inventario_plazo   paso 2  T -> P  (ACTA 62 62.5)
    adjudicado  equilibrar_capacidad_personal_inventario_plazo   paso 3  T -> P  (ACTA 62 62.5)
    adjudicado  equilibrar_capacidad_personal_inventario_plazo   paso 4  T -> P  (ACTA 62 62.5)
    adjudicado  equilibrar_capacidad_personal_inventario_plazo   paso 5  T -> P  (ACTA 62 62.5)
    pasos sin fila: 0 [] | filas sin paso: 0 []
    capitulo pasos    T    P    D  P/pasos
    cap_02      50   46    4    0    8.00%
    cap_03     108  106    2    0    1.85%

Los cuatro de `equilibrar` los localiza el instrumento solo, por la clausula *y apunta su coste* en
`b63405c^`, que tiene los mismos `8` pasos que lo que entro:

    $ for c in b63405c^ b63405c; do git show $c:cuarentena/grove_high_output/equilibrar_capacidad_personal_inventario_plazo.json | python -c "import json,sys; print('$c', len(json.load(sys.stdin)['pasos_accionables']))"; done
    b63405c^ 8
    b63405c 8

| capitulo | que es | pasos que entraron | PUENTE | por ciento |
|---|---|---:|---:|---:|
| `cap_02` | Cap. 1, *The Basics of Production*, los `7` de la `63` | `50` | `4` | **`8,00`** |
| `cap_03` | Cap. 2, *Managing the Breakfast Factory*, `7` de la `63` y los `6` de `d005` | `108` | `2` | **`1,85`** |

**LECTURA:** el peor capitulo, `cap_02`, esta por debajo del `10`: **no se baja escalon** (`8.1`). Los seis
PUENTE son de clausula y **entraron ya reescritos**: seccion `3`, los bytes del grafo son los corregidos.
**`cap_03` no es una clase nueva sino la union de dos lecturas ya firmadas**: los siete de la `63` sin
ningun PUENTE, y los dos de `d005` que firmo la `ACTA 63`. **Su poblacion no es la de la `ACTA 62`**, que
contaba los nueve de la bandeja: `variar_frecuencia_inspeccion_nivel_calidad` y
`simplificar_trabajo_reducir_numero_pasos` no entraron (filas `21` y `22` de `.v64ext/orden.txt`), y
esta cuenta es sobre lo que entro.
