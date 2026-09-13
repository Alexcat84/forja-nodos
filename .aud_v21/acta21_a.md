
---

# ACTA 21. VUELTA 21, lote 4 (`scott_radical_candor`), `cap_10` CERRADO ENTERO: la vuelta del extractor sale **limpia de `CLASE` y de `CIFRA PUBLICADA`**, la frontera de `cap_10` se corrige de **13 a 14** y **la pieza que falta es MIA**, y **el criterio de `PASOS INVENTADOS` se corrige contra su propia linea base**

*Escrita el 12 sep 2026. Auditor del bucle, `AUDITOR_FORJA.md`. Sede del auditor por `5.6`.*

## 0. HUECO DE ACTA: **NO HAY**, y lo compruebo antes de nada (`1.0`)

    $ grep -n "^# ACTA" docs/loop/ACTA_AUDITOR.md | tail -2
      18136:# ACTA 20. VUELTA 20, lote 4 (scott_radical_candor), cap_09 CERRADO y cap_10 cortado...
    $ grep -n "^# VUELTA 21" docs/loop/REPORTE.md
      24910:# VUELTA 21, los registros de la ACTA 20 y de la parada del 12 sep, cap_10 ENTERO...

**La ultima acta escrita es la `ACTA 20` y cubre la vuelta 20, que es la inmediatamente anterior a
la que audito. NO HAY VUELTA SIN ACTA DELANTE.** Esta acta cubre **una sola vuelta, la 21**.

### 0.1. LA HERENCIA `D.40`, DECLARADA EN LA FASE CIEGA Y VERIFICADA AQUI

La declare en `docs/loop/APERTURA_CIEGA.md` seccion `0`, con las tres lineas que el arnes pide y
con la huella **remedida por mi** (`git hash-object` sobre `ACTA_AUDITOR.md`,
`2b3ce599fc21120237d5fbc485498a78d74d6789`, identica a la del prompt). El arnes lo dio por bueno:

    [2026-09-12 22:09:01]   herencia declarada: acta leida por su huella y los 3 heredados resueltos
    [2026-09-12 22:09:01]   apertura ciega sellada: 47153396dc9369bb930421ae0c3fde2bdf22f7ea

**Los tres heredados quedaron en `CUMPLIDO`. Uno de los tres NO lo estaba, y lo digo yo en `8.2`.**

### 0.2. EL SELLO DE MI APERTURA CIEGA

    $ tail -1 docs/loop/SELLOS_APERTURA.jsonl
      {"vuelta": 1, "fecha": "2026-09-12 22:09:01", "sello": "47153396dc9369bb930421ae0c3fde2bdf22f7ea"}

**No he tocado `APERTURA_CIEGA.md` desde que se sello**, y el arnes lo verifica al cerrar mi turno.

### 0.3. **LO QUE MI APERTURA SELLADA NO LLEGO A ESCRIBIR, Y VA AQUI ARRIBA PORQUE ES UNA CAIDA MIA**

**`docs/loop/APERTURA_CIEGA.md` TERMINA EN LA SECCION `5.2`.** Sus secciones `6` (el barrido
`D.38.4`), `7` (el par de la lupa entero), `8` (lo que significan las `0` aristas) y `9` (el
segundo barrido de guiones) **NO EXISTEN EN EL FICHERO SELLADO**, y el fichero las promete cuatro
veces por su numero (`1.4`, `3` fila 13, y dos filas de la tabla `0.3`).

    $ wc -l docs/loop/APERTURA_CIEGA.md
      456 docs/loop/APERTURA_CIEGA.md
    $ grep -c "^## 6\.\|^## 7\.\|^## 8\.\|^## 9\." docs/loop/APERTURA_CIEGA.md
      0

**LA CAUSA, MEDIDA Y NO SUPUESTA:** el barrido `D.38.4` sobre `299` de poblacion con el medidor de
la casa **no cabe en un turno si se corre en serie**. Lo he vuelto a correr hoy entero y lo mido en
`5`: **`3.874` medidas, `7.118,6` segundos de instrumento, entre `6,2` y `12,7` minutos por
candidato.** En serie son **dos horas**; hoy cabe porque lo he partido en trece procesos a la vez.
**El turno de la fase ciega se acabo antes que el barrido en serie.**

**LO QUE HAGO CON ELLO:** el barrido se corre **hoy, en esta fase**, y va entero en la seccion `5`
de esta acta, que es la unica sede que me queda. **Lo que no hago es darlo por cumplido**: va en
`8.2` con su nombre y acumula.

---

## 1. LA VERIFICACION, CON MIS PROPIOS COMANDOS (`1.1`)

### 1.1. LAS GUARDAS, CORRIDAS POR MI AL ABRIR EL TURNO

    $ python forja.py gate
      GATE VERDE.
        nodos verificados: 203
        guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
                 vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
                 arista_incompleta, guiones
    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py | tail -2
      total: 98 pruebas, 0 fallos, 0 errores

**LAS TRES EN VERDE Y LAS TRES CORRIDAS POR MI.** Las `98` pruebas reproducen la cifra que el
reporte publica en `O.6.1`, y son ocho mas que las `90` de la vuelta 20: las de `D.40` (13) y las
de la poblacion nueva (6) menos las que se reagruparon.

### 1.2. MI PROPIO CONTEO, CONTRA EL QUE EL REPORTE PUBLICA

    $ wc -l < dataset/nodos.jsonl                                  ->  203
    $ wc -l < bitacora/VEREDICTOS.jsonl                            ->  148
    $ ls cuarentena/scott_radical_candor/*.json | wc -l            ->   96
    $ find cuarentena/_insertados -name '*.json' | wc -l           ->  201
    $ find cuarentena/_insertados -name '*.json' | grep -c scott   ->    0

**LAS CINCO REPRODUCEN AL DIGITO.** Grafo `203` y bitacora `148` son las mismas al abrir y al
cerrar la vuelta 21, asi que **la vuelta no toco la sede de la aduana**, que es lo que el reporte
afirma en `O.10` y lo que hace que esta tanda no tenga poblacion de `CLASE` en sede.

**Y UNA PRECISION SOBRE `_insertados`, PORQUE EL REPORTE DA DOS CIFRAS PARA LA MISMA CARPETA Y NO
LAS RECONCILIA:** su `O.0` imprime `cuarentena/_insertados/ -> 0` y su `O.10` dice `201`. **Las dos
son ciertas y son de dos comandos distintos**: el glob plano (`ls _insertados/*.json`) da `0`
porque los 201 viven en subcarpetas por libro, y el recursivo (`find`) da `201`. **No es caida de
cifra** (ninguna de las dos salidas es falsa), pero **una carpeta con dos numeros en el mismo
reporte invita a sospechar**, y la fila del alcance del comando va encargada.

### 1.3. **EL DESGLOSE DEL LOTE, RECONTADO CON UN INSTRUMENTO MIO Y DISTINTO DEL SUYO** (`8.3` punto 1)

*No copio su tabla: escribo mi propio recorrido de la bandeja, deduciendo la unidad de la marca
`UNIDAD DE ORIGEN` del `resumen_teorico` de cada fichero, y cuento `len(pasos_accionables)`.*

    $ python (recorro cuarentena/scott_radical_candor/*.json y reparto por UNIDAD DE ORIGEN)
      candidatos: 96 pasos: 1050
        cap_01 candidatos= 1 pasos=   9
        cap_03 candidatos= 1 pasos=   7
        cap_04 candidatos= 6 pasos=  48
        cap_05 candidatos= 8 pasos=  76
        cap_06 candidatos=10 pasos= 117
        cap_07 candidatos=25 pasos= 225
        cap_08 candidatos=12 pasos= 102
        cap_09 candidatos=20 pasos= 272
        cap_10 candidatos=13 pasos= 194
      SIN: []

> ### **LAS NUEVE FILAS Y LOS DOS TOTALES REPRODUCEN AL DIGITO, Y LA FILA DE RESIDUO ES CERO CON SU LISTA VACIA.**

**Y LOS TRECE DE `cap_10`, UNO A UNO, CON SUS PASOS CONTADOS POR MI:** `admitir_pronto` **9**,
`armar_plan_anual` **29**, `calibrar_ascensos` **19**, `calibrar_decision` **13**,
`contactar_despedido` **6**, `conversar_historia_vida` **15**, `conversar_suenios` **15**,
`evitar_obsesion` **10**, `facilitar_despido` **11**, `montar_proceso` **32**,
`reconocer_excelencia` **13**, `sopesar_consejo_legal` **8**, `trazar_plan_dieciocho` **14**.
**Suman `194` y son `13`.** Las trece filas de su `O.3.c` reproducen al digito.

**LOS CUERPOS DE LAS QUINCE UNIDADES, REMEDIDOS POR MI:**

    $ for f in fuentes/scott_radical_candor/cap_*.md; do sed -n '8,$p' $f | wc -w; done
      cap_00 218   cap_01 2846  cap_02 3908  cap_03 627   cap_04 6263
      cap_05 8756  cap_06 11587 cap_07 13678 cap_08 6140  cap_09 17482
      cap_10 8976  cap_11 8626  cap_12 2118  cap_13 9298  cap_14 7638

**`80.481` de `cap_00` a `cap_10` y `27.680` de `cap_11` a `cap_14` salen de sumar estas quince
filas, no de copiarlas.** Las dos cifras del reporte reproducen.

### 1.4. **LAS CIFRAS MEDIDAS DEL REPORTE, REPRODUCIDAS CON MI PROPIO INSTRUMENTO**

*`1.1` de mi protocolo: nada se acepta sin verificarse. Estas son las que el reporte presenta como
salida de un medidor, y las he vuelto a sacar del medidor yo.*

| lo que el reporte publica | donde | **lo que mi comando devuelve hoy** | |
|---|---|---|---|
| el par de la lupa da `0,257 / 0,143 / 0,472` y **ninguna señal lo levanta** | `O.5.b` | `similitud_texto 0.257`, `familia_id 0.143`, `paso_contra_nodo 0.472`, `levantada_por []`, `detalle_paso` *paso 10 del candidato contra paso 9* | **REPRODUCE** |
| `evitar_obsesion` contra `reconocer_excelencia` cae a `0,343` y **deja de levantarse** | `O.6.5.b` | `0.343` en un sentido y `0.348` en el otro, `levantada_por []` en los dos | **REPRODUCE** |
| el par del discutible 7 da `0,228 / 0,125 / 0,442`, **ninguna lo levanta** | `O.6.6` | identico, `levantada_por []` | **REPRODUCE** |
| `forja.py arista` **rechaza** porque la madre no vive en el grafo | `O.4.b` | rechazo literal, misma frase, `nada se escribio`: grafo `203` y bitacora `148` despues de mis tres intentos | **REPRODUCE** |
| los trece informes finales dan **6 `ENTRARIA`, 7 `BLOQUEARIA`, 0 `CAERIA`** con poblacion **299** | `O.6.2` | `7 [BLOQUEARIA]`, `6 [ENTRARIA]`, `pob=299` en los trece, y **las mismas trece asignaciones fila a fila** | **REPRODUCE** |
| **9 filas de vecino** entre los siete bloqueados, que son **6 pares distintos** | `O.6.5.a` | `9` filas contadas por mi de los trece ficheros; tres pares por sus dos extremos y tres por uno: **6 distintos** | **REPRODUCE** |
| las 22 cuentas atribuidas **retiradas sin perder contenido** | `O.3.d` | los 17 pasos y las 5 denominaciones abiertos uno a uno: **ninguna cuenta atribuida queda**, los medios del libro siguen enteros, y los pasos siguen siendo **194** | **REPRODUCE** |
| los tres entregables de `P7`, `P8` y `P9` **limpios de datos del caso** | `O.6.6` disc. 6 | `Russ`, `Sarah`, `Todd`, `Google`, `Laraway` y `Bourbon` buscados en los tres: **cero** | **REPRODUCE** |

### 1.5. **LAS RUTAS QUE EL REPORTE PUBLICA COMO PRUEBA** (cosecha `7.B`), Y **DOS NO REPRODUCEN**

*`7.B`: una ruta publicada como evidencia cuenta como cifra en su sede. Corro las nueve filas de su
`O.6.7` con el mismo comando que la fila declara.*

| ruta | lo que el reporte publica | **lo que da hoy** | |
|---|---:|---:|---|
| `.aduana_v21/*.txt` | 16 | **16** | ok |
| `.aduana_v21/final/*.txt` | 13 | **13** | ok |
| dictamenes de `final/` | 13 | **13** | ok |
| dictamenes de la raiz | 14 | **14** | ok |
| `.aduana_v21/sellos_candidatos.txt` | 13 | **13** | ok |
| `.aduana_v21/arista_intento_1.txt`, `RECHAZADO` | 1 | **1** | ok |
| `.t1_v21/*.py` | 9 | **9** | ok |
| `.t1_v21/*.txt` | 13 | # **14** | **NO** |
| `.v21/*.md` | 14 | # **16** | **NO** |

**LAS SIETE CONTABLES REPRODUCEN AL DIGITO. LAS DOS QUE NO SON LAS DOS QUE CUENTAN LOS FICHEROS QUE
EL PROPIO ACTO DE PUBLICAR CREA**, y lo demuestro con la hora de cada fichero en vez de suponerlo:

    $ ls -la --time-style=+%H:%M:%S .v21/*.md .t1_v21/*.txt   (los cuatro que importan)
      21:30:48  .v21/frag_rutas.md              <- el fragmento que CONTIENE esta tabla
      21:31:48  .t1_v21/salida_cierre_final.txt <- nace 1 minuto DESPUES de contarse la fila
      21:32:06  .v21/frag_cierre_h.md           <- nace 1 minuto y 18 s DESPUES

> ### **LAS DOS FILAS ERAN CIERTAS EN EL SEGUNDO EN QUE SE CONTARON Y FALSAS EN EL SEGUNDO EN QUE SE COMMITEARON.** El remedio que la vuelta 20 escribio (*la tabla se cuenta al final de todo y no antes*) **se ejecuto a la letra**: las nueve filas llevan su comando y su salida, y la tabla se conto la ultima. **Lo que falla no es el cumplimiento: es el alcance.** Dos de sus nueve filas cuentan **el fichero que se esta escribiendo al escribirlas**, y esas no se pueden hacer verdaderas midiendo mejor.

**MI ADJUDICACION VA EN `4.7`.** Aqui solo queda registrada la medida.

---

## 2. LAS MUTACIONES DE `5.5`: **TODA GUARDA QUE EL REPORTE DECLARE MORDIENDO SE RE CORRE**

*Cosecha `7.C`: una guarda publicada como mordiendo que no muerde es cifra falsa. El reporte
declara tres mordiendo en esta vuelta, y las muerdo las tres.*

### 2.1. MUTACION 1: la guarda `guiones` (el reporte la declara mordiendo en `O.6.1.b`)

    $ printf 'prueba del auditor \xe2\x80\x94 guion largo\n' > .aud_v21/mutacion_guion.md
    $ python forja.py guiones
      BARRIDO DE GUIONES EN ROJO: 1 hallazgo(s)
        .aud_v21/mutacion_guion.md linea 1 columna 20: guion largo (U+2014)
    $ rm .aud_v21/mutacion_guion.md ; python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**MUERDE, y vuelve a verde al quitar el fichero.** El rojo que el reporte cuenta contra si mismo en
`O.6.1.b` es de esta guarda y no de un adorno.

### 2.2. MUTACION 2: la guarda `reglas_id` (el reporte la declara mordiendo en `O.6.2`)

    $ python -c "from src import reglas_id; ..."
      admitir_pronto_bajo_desempenio_cuatro_razones -> ["id '...': preposicion o articulo
                                                        prohibido: bajo (regla 3)"]
      admitir_pronto_mal_desempenio_cuatro_razones  -> []

**MUERDE CON EL ID QUE CAYO Y ACEPTA EL CORREGIDO.** El id que el reporte dice que tumbo la puerta
es exactamente el que la regla 3 rechaza, y por la palabra que el reporte nombra.

### 2.3. MUTACION 3: la guarda de `forja.py arista` (el reporte la declara mordiendo en `O.4.b`)

    $ python forja.py arista --madre facilitar_despido_tres_cosas --hijo admitir_pronto_... --paso 11
      RECHAZADO: la madre 'facilitar_despido_tres_cosas' no vive en el grafo
    $ python forja.py arista --madre registrar_fuente_canonica --hijo facilitar_despido_tres_cosas --paso 1
      RECHAZADO: la hijo 'facilitar_despido_tres_cosas' no vive en el grafo

**MUERDE, Y MUERDE POR EL EXTREMO QUE FALTA Y NO EN BLOQUE:** con una madre que **si** vive en el
grafo (`registrar_fuente_canonica`) el rechazo cambia de extremo y nombra al hijo. **Eso confirma
la precision que el reporte escribe contra si mismo en `O.4.b`:** el rechazo cae en la primera
guarda del modulo y **el `--paso 11` no llego a validarlo la maquina**. Lo he leido yo en el codigo:

    $ sed -n '104,111p' src/arista.py
      for etiqueta, pedido, resuelto in (("madre", madre_id, madre), ("hijo", hijo_id, hijo)):
          if resuelto is None:
              return resultado.rechazar("la %s '%s' no vive en el grafo" % (etiqueta, pedido), ...)

**Y NADA SE ESCRIBIO EN NINGUNO DE MIS TRES INTENTOS:** grafo `203`, bitacora `148`, y
`git status` sin un solo fichero de `dataset/` ni de `bitacora/` tocado.
