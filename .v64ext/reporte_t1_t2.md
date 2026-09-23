
## 64.1. TAREA 1: LOS REGISTROS DE LA `ACTA 62`, SIN REABRIR EL ARGUMENTO (`D.47`)

| que | donde |
|---|---|
| **`D1` CAE, dentro del marcado**: los `4` pasos de `equilibrar` con *y apunta su coste* cuentan como PUENTE por el ejemplar de `D.30` (los `13` de `36` del lote `1` son `4` retirados y `9` clausulas reescritas). **`cap_02` queda en `4` de `50`, `8,0` por ciento**; `cap_03` en `0` de `80`. **Lo aplico en esta vuelta**: la clausula reescrita CUENTA como PUENTE en `64.2` | `ACTA 62` `62.5` y `62.6` |
| *el ultimo commit que los toca es del `16` sep* era falso para `5` de `16` (`4` del `18`, `1` del `19`); la conclusion sigue en pie. Prosa, no acumula | `ACTA 62` `62.3` |
| `R5` sigue vivo **con su letra**: si corto un bloque `$`, por el final y dentro del bloque `(recortado, entero en <fichero>)`. **En esta vuelta los cortes van en el propio comando** (`grep -n -o`, `cut`), que es lo que el comando imprime, y el unico corte de bloque lleva la formula (`64.0`) | `ACTA 62` `62.4` y `62.13` |
| **`REPORTE` baja a `0 de 3`** | `ACTA 62` `62.9` |

**`T1` CERRADA.**

## 64.2. TAREA 2: `d005`, LOS SEIS DE `cap_03`

### 64.2.a. LA RELECTURA DE FIDELIDAD ENTERA (`D.30`), `41` PASOS, SIN MUESTRA

`cap_03` leido entero con `cat -n` en esta vuelta (L1 a L179), y cada paso de los seis contra la linea de
la que dice salir. **La marca de cada paso, con su linea y lo que la decide, esta en `.v64ext/fidelidad.tsv`
(una fila por paso), y la cuenta la hace un instrumento que abre las fichas**, no yo:

<!-- TALLADO: parcial salida=.v64ext/contar_fidelidad.txt -->

    $ python .v64ext/contar_fidelidad.py
    candidato                                        cap     pasos   T   P
    archivar_indicadores_resolver_problemas          cap_03      4   4   0
    construir_grafico_escalonado_pronosticos         cap_03      8   7   1
    construir_indicador_tendencia_patron             cap_03      6   6   0
    elegir_fabricar_pedido_pronostico                cap_03      9   8   1
    elegir_indicador_salida_trabajo_administrativo   cap_03      7   7   0
    emparejar_indicadores_efecto_contraefecto        cap_03      7   7   0
    pasos sin fila: 0 [] | filas sin paso: 0 []

    PASOS INVENTADOS POR CAPITULO, los seis de d005
    cap_03  candidatos 6  pasos 41  T 39  P 2  inventado 4,9 por ciento

**DOS PASOS PUENTE EN `41`, LOS DOS DE CLAUSULA, Y LOS DOS REESCRITOS EN LA BANDEJA ANTES DE NINGUNA
INSERCION**, con su `CORRECCION DECLARADA de la vuelta 64` anexada al `resumen_teorico` y el texto viejo
dentro (`.v64ext/corregir.py`, idempotente, y el `git diff` del commit de esta tarea lo ensena entero).
**Cuentan como PUENTE aunque ya esten corregidos** (`ACTA 62` `62.5`). Y en la misma pasada, **cuatro
entregables y un titulo** con puentes de la especie que la `63` bautizo SOPORTE, mas uno de RESPONSABLE y
uno de DISPOSICION; no suman en la metrica porque no son pasos, y se corrigen igual:

<!-- TALLADO: parcial salida=.v64ext/corregir.txt -->

    $ python .v64ext/corregir.py
    CAMBIA  construir_grafico_escalonado_pronosticos         paso 5
    CAMBIA  construir_grafico_escalonado_pronosticos         titulo 
    CAMBIA  construir_grafico_escalonado_pronosticos         entregable_esperado 
    CAMBIA  construir_indicador_tendencia_patron             entregable_esperado 
    CAMBIA  elegir_fabricar_pedido_pronostico                paso 8
    CAMBIA  elegir_fabricar_pedido_pronostico                entregable_esperado 
    CAMBIA  elegir_indicador_salida_trabajo_administrativo   entregable_esperado 
    CAMBIA  emparejar_indicadores_efecto_contraefecto        entregable_esperado 

| ficha | que traia | que dice hoy | especie | la linea que NO lo dice |
|---|---|---|---|---|
| `construir_grafico...` paso `5` | *y debajo el mismo pronostico* | *y con el el mismo pronostico* | **PASO PUENTE**, disposicion | `93:The stagger chart then provides the same forecast prepared in the following month, in the month after that, and so on` |
| `construir_grafico...` titulo y entregable | *encima de los anteriores*; *una fila por mes, los meses en columnas* | *junto a los anteriores*; *cada pronostico mensual junto a los anteriores* | disposicion: la figura no esta en el texto, y la ficha decia *debajo* en un sitio y *encima* en otro | `91:as compared to several prior forecasts` |
| `elegir_fabricar...` paso `8` | *Mezcla las dos vias donde te convenga* | *Cuenta con que las dos vias pueden convivir en la misma operacion* | **PASO PUENTE**, criterio: el libro describe, no manda mezclar | `109:Our breakfast factory makes its product to customer order, but buys from its suppliers` y `109:building” to forecast is a very common business practice` |
| `elegir_fabricar...` entregable | *Escrito cual de las dos vias* | *Decidido cual de las dos vias* | soporte | L103 a L109 no mandan escribirlo |
| `construir_indicador_tendencia...` entregable | *con el patron dibujado encima ... y escrito el porque* | *contra el patron ... y pensado el porque* | soporte y disposicion | `89:makes you think through why the results were what they were` |
| `elegir_indicador_salida...` entregable | *con su pareja escrita al lado y el responsable de la calificacion nombrado* | *con su pareja de calidad al lado* | soporte y **responsable** | `37:as assessed by a senior manager with an office in that building`: el evaluador del ejemplo, no un responsable que se nombra |
| `emparejar...` entregable | *su pareja escrita al lado ... en el mismo sitio* | *su pareja ... vigilados a la vez* | soporte | `31:you need to monitor both inventory levels and the incidence of shortages` |

**Las citas de la tabla, pegadas** (`D.35`), con el corte en el propio `grep -o`, que imprime solo el trozo
que casa (el fichero entero de las once en `.v64ext/citas.txt`):

<!-- TALLADO: parcial salida=.v64ext/citas.txt -->

    $ grep -n -o 'The stagger chart then provides the same forecast prepared in the following month, in the month after that, and so on' fuentes/grove_high_output/cap_03.md
    93:The stagger chart then provides the same forecast prepared in the following month, in the month after that, and so on
    $ grep -n -o 'as compared to several prior forecasts' fuentes/grove_high_output/cap_03.md
    91:as compared to several prior forecasts
    $ grep -n -o 'Our breakfast factory makes its product to customer order, but buys from its suppliers' fuentes/grove_high_output/cap_03.md
    109:Our breakfast factory makes its product to customer order, but buys from its suppliers
    $ grep -n -o 'building. to forecast is a very common business practice' fuentes/grove_high_output/cap_03.md
    109:building” to forecast is a very common business practice
    $ grep -n -o 'makes you think through why the results were what they were' fuentes/grove_high_output/cap_03.md
    89:makes you think through why the results were what they were
    $ grep -n -o 'as assessed by a senior manager with an office in that building' fuentes/grove_high_output/cap_03.md
    37:as assessed by a senior manager with an office in that building
    $ grep -n -o 'you need to monitor both inventory levels and the incidence of shortages' fuentes/grove_high_output/cap_03.md
    31:you need to monitor both inventory levels and the incidence of shortages

**Y NINGUNA CAE EN LA PUERTA TRAS CORREGIRLA**: la parte de la aduana que decide `CAERIA` (esquema, id,
fuentes y guiones), corrida sobre las cinco fichas tocadas sin el barrido de vecinos, que lo sustituye `2.c`:

<!-- TALLADO: parcial salida=.v64ext/validar.txt -->

    $ python .v64ext/validar.py construir_grafico_escalonado_pronosticos construir_indicador_tendencia_patron elegir_fabricar_pedido_pronostico elegir_indicador_salida_trabajo_administrativo emparejar_indicadores_efecto_contraefecto
    NO CAERIA  construir_grafico_escalonado_pronosticos  (esquema, id, fuentes y guiones en verde)
    NO CAERIA  construir_indicador_tendencia_patron  (esquema, id, fuentes y guiones en verde)
    NO CAERIA  elegir_fabricar_pedido_pronostico  (esquema, id, fuentes y guiones en verde)
    NO CAERIA  elegir_indicador_salida_trabajo_administrativo  (esquema, id, fuentes y guiones en verde)
    NO CAERIA  emparejar_indicadores_efecto_contraefecto  (esquema, id, fuentes y guiones en verde)

> **DISCUTIBLES DE FIDELIDAD, MARCADOS ANTES DE SABER SI ACIERTO**
>
> - **`D64.1`**: `archivar_indicadores_resolver_problemas` paso `1` lo marco `T`. Su coda *en vez de dejar que se
>   pierdan segun pasan los dias* no esta en L99, pero **no manda hacer nada** que L99 no mande: es el criterio
>   con el que la `ACTA 62` `62.5` separo *apunta* (PUENTE) de *ordena* (TRANSCRIPCION). Un lector estricto
>   que la cuente pone `cap_03` en `3` de `41`, el `7,3` por ciento: **la conclusion no cambia**.
> - **`D64.2`**: `elegir_fabricar...` paso `9` y `construir_grafico...` paso `5` convierten en imperativo un ejemplo
>   del libro (los titulados y el programa en L109; los pedidos entrantes de una division de Intel en L93).
>   Los marco `T` en su contenido, porque L109 juzga la alternativa (*which would be foolish*) y L93 dice
>   que ahi el grafico fue *more productive than* en ningun otro sitio; **del paso `5` solo cuento la
>   clausula *debajo***. Si los dos contaran entero, `cap_03` sale `3` de `41`, el `7,3` por ciento, y
>   con `D1` tambien, `4` de `41`, el `9,8`: **todavia por debajo del `10`**.

### 64.2.b. LOS VECINOS: YA MEDIDOS, Y SE COMPRUEBA ANTES DE USARLOS

**No se re corre ningun informe.** Los pares salen de los seis informes archivados de la fase ciega
anulada (poblacion `462`), que lee `.v64ext/medir_pares.py` con la misma expresion de `.v63aud/vecinos_d005.py`,
y cada par se mide otra vez con `aduana.medir` **antes** de corregir nada: **los `16` pares de `d005` y los `19`
de `d140` salen hoy con las mismas tres seniales que su informe, al redondeo**, que es el control de que la
lista vieja sirve (`.v64ext/pares_antes.txt`, poblacion `grafo 346 + bandejas 116 = 462`). Los veredictos van
en `64.3`, juntos con los de `d140`, en bloques `VEREDICTOS LISTOS DE <id>`.

### 64.2.c. LA SENIAL SE MOVIO CON LA CORRECCION, Y SE DICE (`d031`)

**Cinco de las seis fichas cambiaron** (su `resumen_teorico` crece con la correccion declarada, y la senial
`1` lo lee). **Mido cada par de esas fichas otra vez, en los dos sentidos**, mas los pares de `d141` y los
que la lectura de `T4` pide (`.v64ext/pares_despues.txt`, `90` lineas). **Lo que se movio:**

<!-- TALLADO: parcial salida=.v64ext/pares_despues.txt -->

    $ grep -E "^d005 +emparejar_indicadores_efecto_contraefecto +revisar|^lectura dimensionar_plantilla_administrativa_pronostico +(construir_indicador_tendencia|elegir_fabricar)|^lectura elegir_fabricar_pedido_pronostico +dimensionar|^d005 +construir_indicador_tendencia_patron +emparejar|^d005 +elegir_fabricar_pedido_pronostico +emparejar|^d005 +emparejar_indicadores_efecto_contraefecto +elegir_indicador|^lectura construir_indicador_tendencia_patron +dimensionar" .v64ext/pares_despues.txt

| par, en el sentido del candidato | informe archivado | HOY | que cambia |
|---|---|---|---|
| `emparejar...` contra `revisar_tres_preguntas_valor_carrera` | `0.354/0.000/0.386`, levantaba | `0.334/0.0/0.386`, **NO LEVANTA** | **DEJA DE LEVANTAR.** Mi lectura dice SANO (ajenos), pero **no va en el bloque `--veredicto`**: un veredicto sobre quien la senial no levanta se registra como lectura declarada, y eso seria mentir en la bitacora |
| `construir_indicador_tendencia...` contra `dimensionar_plantilla...` | no estaba | `0.373/0.0/0.405`, **LEVANTA**; y `0.38` en el sentido contrario | **VECINO NUEVO**, y es un par de `d141` que la `ACTA 62` dio por no levantado en ningun sentido: hoy lo levanta la correccion. Entra en los dos bloques |
| `dimensionar_plantilla...` contra `elegir_fabricar...` | no estaba | `0.353/0.143/0.455`, **LEVANTA**; el contrario no (`0.334`) | **VECINO NUEVO**, en un solo sentido: `D.36` pide que `dimensionar_plantilla` entre despues |
| `emparejar...` contra `elegir_indicador_salida...` | no estaba en el informe de `emparejar` | `0.383/0.125/0.468`, **LEVANTA** | vecino nuevo en ese sentido; el otro ya levantaba |
| `construir_indicador_tendencia...` contra `emparejar...` | no estaba | `0.393/0.143/0.427`, **LEVANTA** | vecino nuevo en ese sentido |
| `elegir_fabricar...` contra `emparejar...` | no estaba | `0.362/0.0/0.419`, **LEVANTA** | vecino nuevo en ese sentido |

**Y LO QUE ESTE METODO NO PUEDE VER, y lo digo:** un par a par solo mide los pares que alguien nombra. Si la
correccion levanta a un vecino que ningun informe listaba y que ningun par de lectura mira, **aqui no sale**.
**Quise cerrarlo barriendo las cinco fichas corregidas contra la poblacion entera con `aduana.buscar_vecinos`**
(`.v64ext/barrer_corregidas.py`), **y no cabe**: una sola ficha paso de `590` s sin terminar y el corte la
mato sin salida (lanzada a las `09:55`, `date` a las `10:05:37`). **Cinco serian mas de cincuenta minutos, y
no lo lanzo** (encargo, punto `0`). **Entre los `22` de `cap_02` y `cap_03` si lo cierro**, con la matriz de
`T4`; fuera de ellos, **lo encuentra el `insertar` de la `65`, que bloquea y pide leer**, que es el
mecanismo de la casa para el vecino nuevo.
