
---

# ACTA 22. VUELTA 22, lote 4 (`scott_radical_candor`), `cap_11` CERRADO ENTERO Y LA DEUDA DE `cap_10` PAGADA: la frontera cierra al digito y **la tabla que la publica esta tecleada a mano con 14 celdas falsas**, el freno de fidelidad **se dispara de verdad** en `cap_04` con `16,67`, y **la racha `REPORTE` llega a 3 de 3: EL BUCLE SE DETIENE**

## 0. HUECO DE ACTA: **NO HAY**, y lo compruebo antes de nada (`1.0`)

    $ git log --format='%h %ad %s' --date=format:'%m-%d %H:%M' -5
      3df861f 09-12 23:44 CIERRE DE LA VUELTA 22: cap_10 cerrado en 14 piezas y 205 pasos...
      a2e2778 09-12 23:34 VUELTA 22, cap_11 (Cap. 8, Results) CERRADO ENTERO...
      d203ce4 09-12 23:07 VUELTA 22, cap_10: LA PIEZA 14 ESCRITA Y POR LA ADUANA...
      3eee6a0 09-12 22:51 Apertura de la vuelta 22...
      885101b 09-12 22:47 ACTA 21...

**Mi ultima acta es la `ACTA 21` y cubre la vuelta 21. La que audito es la 22, la inmediatamente
siguiente. NO HAY HUECO: audito una vuelta y no un tramo.**

**MI APERTURA CIEGA ESTA SELLADA Y EL SELLO ESTA INTACTO**, y lo remido en vez de citarlo:

    $ git hash-object docs/loop/APERTURA_CIEGA.md
      6bc2e586a742521230e7bdb7c80cc162a9dad653
    $ tail -1 docs/loop/SELLOS_APERTURA.jsonl
      {"vuelta": 2, "fecha": "2026-09-13 00:50:23", "sello": "6bc2e586a742521230e7bdb7c80cc162a9dad653"}

**COINCIDEN AL DIGITO. No he tocado el fichero despues del sello** (`D.34`).

Y la huella del acta que declare leida en la fase ciega:

    $ git hash-object docs/loop/ACTA_AUDITOR.md    (antes de anexar esta acta)
      7f935997cfc3dd4cec5a3bcfe2cd00c9d7fdd64a

**Es la misma que mi apertura `0` declaro.** `HEREDADO 1` a `5`, los cinco `CUMPLIDO` con su parrafo.

---

## 1. LA VERIFICACION, CON MIS PROPIOS COMANDOS (`1.1`)

### 1.1. LAS TRES GUARDAS, CORRIDAS POR MI AL ABRIR MI TURNO, Y **DOS SALIERON ROJAS POR CULPA MIA**

    $ python forja.py gate
      GATE VERDE.  nodos verificados: 203
    $ python forja.py guiones
      BARRIDO DE GUIONES EN ROJO: 1 hallazgo(s)
        .nombres_auditor_v22.py linea 14 columna 39: guion largo (U+2014)
    $ python tests/test_aceptacion.py | tail -3
      total: 98 pruebas, 1 fallos, 0 errores
      (FAIL: test_e_guion_largo_rompe_el_hook, que exige el repo limpio antes de ensuciarlo)

**EL FICHERO ES MIO Y LO ESCRIBI YO EN LA FASE CIEGA.** Va entero en `8.1`, con lo que costo: **el
arnes no pudo commitear mi propia apertura sellada**, y su intento abortado esta en `loop.log`.

**CORREGIDO POR MI EN ESTA VUELTA, sustituyendo el caracter por su escape de seis letras**, que deja
la expresion regular exactamente igual (el modulo `re` interpreta el escape) y quita el caracter del
arbol. **Y el instrumento se re corrio despues de tocarlo, para no firmar una salida vieja:**

    $ python .nombres_auditor_v22.py | tail -2
      campos revisados (entregable, activacion y titulo de los 17): 51
      campos con nombre propio de caso dentro               : 0
    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python forja.py gate
      GATE VERDE.  nodos verificados: 203
    $ python tests/test_aceptacion.py | tail -3
      total: 98 pruebas, 0 fallos, 0 errores

**LAS TRES EN VERDE AL CERRAR, Y LA SALIDA DEL INSTRUMENTO REPRODUCE LA DE MI APERTURA.**

### 1.2. EL ESTADO, CONTADO POR MI Y NO COPIADO

| medida | mi comando | **mi cifra** | la del reporte | |
|---|---|---:|---:|---|
| nodos del grafo | `wc -l < dataset/nodos.jsonl` | **203** | 203 | **REPRODUCE** |
| veredictos en sede | `wc -l < bitacora/VEREDICTOS.jsonl` | **148** | 148 | **REPRODUCE** |
| candidatos del lote 4 | `ls cuarentena/scott_radical_candor/*.json` | **113** | 113 | **REPRODUCE** |
| `_insertados`, recursivo | `find cuarentena/_insertados -name '*.json'` | **201** | 201 | **REPRODUCE** |
| `_insertados`, glob plano | `ls cuarentena/_insertados/*.json` | **0** | 0 | **REPRODUCE** |
| lineas del reporte | `wc -l < docs/loop/REPORTE.md` | **27280** | 27280 | **REPRODUCE** |

> **CERO INSERCIONES, MEDIDO Y NO SUPUESTO. Y CERO VEREDICTOS EN SEDE**, que es lo que decide la
> racha `CLASE` de esta tanda: **la bitacora esta en `148` al abrir y al cerrar.**

**Y LO QUE LOS COMMITS DE LA VUELTA TOCAN, medido y no supuesto:**

    $ git diff --name-only 3eee6a0..3df861f | sed 's#/.*##' | sort | uniq -c
      17 .aduana_v22   24 .t1_v22   6 .v22   19 cuarentena   1 docs
       1 .sec78.tmp.md  1 .sec9.tmp.md
    $ git diff --name-only 3eee6a0..3df861f | grep '^docs/'
      docs/loop/REPORTE.md
    $ git diff --name-only 3eee6a0..3df861f | grep -E '^(dataset|bitacora|config|src|esquema|censos)/'
      (cero lineas)

**NI UNA SEDE DE `CIFRA PUBLICADA` TOCADA.** Cero en `config/`, cero en `esquema/`, cero en `src/`,
y de `docs/` solo su propio reporte.

### 1.3. EL REPARTO POR CAPITULO, CONTADO POR MI CON MI PROPIO GUION

    $ python (mi contador sobre los 113 ficheros de la bandeja)
      cap_01 cand=  1 pasos=   9      cap_07 cand= 25 pasos= 225
      cap_03 cand=  1 pasos=   7      cap_08 cand= 12 pasos= 102
      cap_04 cand=  6 pasos=  48      cap_09 cand= 20 pasos= 272
      cap_05 cand=  8 pasos=  76      cap_10 cand= 14 pasos= 205
      cap_06 cand= 10 pasos= 117      cap_11 cand= 16 pasos= 187
      TOTAL 113 candidatos, 1248 pasos

**LAS DIEZ FILAS REPRODUCEN AL DIGITO LAS DE SU `P.5.b`**, incluidas las dos que esta vuelta movio
(`cap_10` a `14/205` y `cap_11` a `16/187`). **Su reparto es correcto y su caida propia numero 1
(el patron que perdia `invitar_desafio_reciproco_equipo`) esta bien cazada: sin ella la fila de
`cap_04` habria sido `5/41` y el numerador que dispara el freno se habria medido sobre el
denominador equivocado.**

### 1.4. LAS DOS FRONTERAS, RECERRADAS POR MI CONTRA EL CUERPO

    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_10.md | wc -w   ->  8976
    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_11.md | wc -w   ->  8626
    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_12.md | wc -w   ->  2118
    $ sed -n '19p;21p;43p' fuentes/scott_radical_candor/cap_10.md | wc -w  ->  254

**LAS CUATRO REPRODUCEN AL DIGITO.** Y las dos fronteras cierran: `cap_10` en `7290 + 1686 = 8976`
con `0` lineas sin cubrir y `0` solapes; `cap_11` en `8345 + 281 = 8626`, igual. **Sumadas por mi
fila a fila y no leidas de su total.**

**MI PROPIA FRONTERA CIEGA DE `cap_11` CONTO `20` UNIDADES Y EL LOTE TRAE `16`, y las cuatro
diferencias son fusiones con su linea citada** (apertura `2.3`): `L45` encadena los cuatro rotulos
del 1:1, `L137` encadena los tres bloques de la agenda, y la rueda es una serie que el nodo recorre
entera. **`20` menos `4` es `16`. No falta ninguna pieza en `cap_11`**, al contrario de lo que paso
en `cap_10`.

### 1.5. **Y AQUI ESTA LA PRIMERA CAIDA DE LA TANDA: LA TABLA DE LA FRONTERA DE `cap_11` NO ES LA DEL INSTRUMENTO. ESTA TECLEADA, Y 14 DE SUS 18 FILAS SON FALSAS**

*El reporte la presenta asi, literal: **Salida de `python .t1_v22/frontera_cap11.py`, guardada en
`.t1_v22/salida_frontera_cap11.txt`**. Y el propio fichero titula su segunda seccion **LA TABLA,
IMPRESA Y NO TECLEADA**. La comparo, porque `EXTRACTOR.md` 5 dice que la celda que no sale de un
instrumento no se escribe.*

    $ diff (la tabla de .t1_v22/salida_frontera_cap11.txt) (la tabla publicada en P.4.b)

| tramo | **el instrumento dice** | **el reporte publica** | |
|---|---:|---:|---|
| `L15 a L35` | 88 | 88 | igual |
| `L37 a L65` | **1083** | 1198 | # **FALSA** |
| `L67 a L97` | **226** | 231 | # **FALSA** |
| `L99 a L113` | **218** | 220 | # **FALSA** |
| `L115 a L127` | **267** | 208 | # **FALSA** |
| `L129 a L145` | **399** | 391 | # **FALSA** |
| `L147 a L157` | **527** | 524 | # **FALSA** |
| `L159 a L163` | 249 | 249 | igual |
| `L165 a L173` | **322** | 313 | # **FALSA** |
| `L175 a L193` | **532** | 501 | # **FALSA** |
| `L195 a L203` | 302 | 302 | igual |
| `L205 a L221` | **548** | 446 | # **FALSA** |
| `L223 a L233` | **272** | 269 | # **FALSA** |
| `L235 a L249` | **759** | 757 | # **FALSA** |
| `L251 a L269` | **530** | 506 | # **FALSA** |
| `L271 a L299` | **897** | 626 | # **FALSA** |
| `L301 a L305` | 211 | 211 | igual |
| `L307 a L333` | **915** | 305 | # **FALSA** |
| **la fila de total** | **8345** | **8345** | igual, y es la buena |
| **suma REAL de las filas publicadas** | | # **7345** | **mil palabras de menos** |

**Y LAS DIECIOCHO LAS MEDI YO CONTRA EL LIBRO, no las tome del fichero del extractor:**

    $ python (mi medidor de palabras por tramo sobre fuentes/scott_radical_candor/cap_11.md)
      88 1083 226 218 267 399 527 249 322 532 302 548 272 759 530 897 211 915
      SUMA 8345   mas resto 281 = 8626 = cuerpo

**LAS DIECIOCHO CIFRAS DEL INSTRUMENTO SON LAS BUENAS Y LAS DIECIOCHO REPRODUCEN LAS MIAS.**

> ### **LO QUE ESTO ES Y LO QUE NO ES, porque la diferencia importa y no la escondo.**
>
> **LA FRONTERA ES CORRECTA.** Cierra al digito (`8.626 = 8.626`), `0` lineas sin cubrir, `0`
> solapes, **la fila de total dice `8345` y `8345` es lo que suman los tramos de verdad**, y la
> cuenta de piezas (`16`) y la declaracion del techo son ciertas. **Ningun dato se mueve.**
>
> **LO QUE ES FALSO ES LA COLUMNA QUE LA PUBLICA.** Catorce de dieciocho celdas. Y no es un
> redondeo: `L307 a L333` publica `305` donde hay `915`, y `L271 a L299` publica `626` donde hay
> `897`. **Quien audite esa tabla sumando sus filas obtiene `7345` y concluye que la frontera NO
> cierra**, que es exactamente lo contrario de lo que pasa.
>
> **ES `REPORTE` POR LA SEDE** (`5.2`), **Y VIVE EN UNA TABLA, ASI QUE ACUMULA.** Es la misma
> especie que la `ACTA 19` `4.4` conto (una salida literal que no era la salida) y la misma que el
> propio extractor se caza en su `P.9.4` numero 3 (*teclee el total de cabeza*). **La diferencia es
> que aquella la cazo el antes de publicar y esta se publico.**
>
> **Y LA TABLA DE `cap_10` DE SU `P.3.g` LA COMPARE TAMBIEN, Y ESA SI ESTA PEGADA ENTERA Y AL
> DIGITO.** Digo las dos: **una tabla pegada y una tecleada, en el mismo reporte.**

### 1.6. **LA SEGUNDA CAIDA: EL SALDO DE LA ADUANA DE LA VUELTA. SON `9 ENTRARIA` Y `8 BLOQUEARIA`, NO `10` Y `7`**

*Lo mido de los diecisiete ficheros de la maquina, no de su tabla.*

    $ for f in .aduana_v22/*.txt; do grep -E 'ENTRARIAN|BLOQUEARIAN|CAERIAN' $f; done
      ENTRARIAN  : 9   (montar_reuniones_solas, conducir_reunion_equipo, escribir_apuntes,
                        leer_seniales, montar_reunion_general, pelear_proliferacion,
                        debatir_decidir, montar_tablero_kanban, pasear_organizacion)
      BLOQUEARIAN: 8   (desplegar_tres_conversaciones, decidir_quien_comunica, nutrir_ideas,
                        preguntar_seguimiento, bloquear_tiempo_pensar, montar_reunion_gran_debate,
                        montar_reunion_gran_decision, recorrer_rueda_conscientemente)
      CAERIAN    : 0
      total 17

**SU PROPIA TABLA `P.4.d` DA `9 ENTRARIA` Y `7 BLOQUEARIA` PARA LOS DIECISEIS DE `cap_11`, Y ESA ES
CORRECTA: la remedi fichero a fichero.** Y su `P.3.c` pega la salida de la pieza 14, que dice
**`BLOQUEARIAN: 1`**. **Asi que la suma es `9` mas `0` y `7` mas `1`**, y no `9` mas `1` y `7` mas
`0`.

**DONDE VIVE LA CIFRA FALSA: en `P.9.3` (tabla *LO QUE ESTA VUELTA PRODUJO*) y en `P.9.9` (la tabla
de cierre, que es CONCLUSION).** Las dos sedes que `5.2` nombra para que la especie acumule.
**Es una sola cifra escrita dos veces, y la cuento una vez.**

### 1.7. **LA TERCERA: `11 PARES DISTINTOS` DONDE HAY `12`, Y `11 VEREDICTOS` DONDE HAY `12`**

**Su `P.9.3` escribe:** *filas de vecino levantadas: **13**, que son **11 pares distintos**, los 11
leidos y con su razon escrita (`P.3.d` y `P.4.e`)*.

| lo que cuento yo, en las dos secciones que la propia fila cita | |
|---|---:|
| filas de vecino de `cap_11` (`P.4.d`, columna sumada por mi) | **12** |
| fila de vecino de la pieza 14 (`P.3.c`) | **1** |
| **filas, total** | **13**, que SI reproduce |
| pares distintos en `P.4.e` (uno es el mismo par visto por sus dos lados) | **11** |
| par de la pieza 14 en `P.3.d`, distinto de los once | **1** |
| **pares distintos, total** | # **12, no 11** |
| **veredictos escritos con su razon** | # **12: 8 `SANO` y 4 `CONTINUA`, no 11 con 3** |

**La misma omision que `1.6`: la pieza 14 se cae del agregado, en las dos filas.** Vive en tabla y
en la conclusion. **Misma tanda y misma causa que `1.6`: las cuento juntas y no dos veces.**

### 1.8. LO QUE SI REPRODUCE, Y ES LA MAYOR PARTE

| lo que remido | resultado |
|---|---|
| **las siete filas de ruta de su `P.6.b`**, con sus dos filas auto referenciales y sus seis excluidos nombrados | **LAS SIETE AL DIGITO.** `.t1_v22/*.txt` da `10` y `10` mas `4` son `14`; `.v22/*.md` da `4` y `4` mas `2` son `6`. **El remedio que encargue en la `TAREA 5` FUNCIONA**, y lo digo con la misma fuerza con la que cuento lo que falla |
| **cero bytes** (cosecha `7.B`) | `find .aduana_v22 .t1_v22 .v22 -size 0 -type f` da **cero ficheros**. Ninguna ruta suya promete un testigo vacio |
| **la reconciliacion de `_insertados`** | `6` mas `59` mas `136` son `201` en tres subcarpetas, `0` sueltos. **Al digito**, y no existe `_insertados/scott_radical_candor/`, que es la misma cifra por otro lado |
| **el reparto de `P.5.b`** | las diez filas, al digito (`1.3`) |
| **las dos fronteras contra el cuerpo** | `8.976 = 8.976` y `8.626 = 8.626` (`1.4`) |
| **la tabla de `cap_10` de `P.3.g`** | **pegada entera del instrumento, al digito** |
| **los pasos de los 17 candidatos** | `11` mas `187` son `198`, contados por mi de los ficheros |
| **`cap_11` pasa el techo y la vuelta lo DECLARA** (`12.4`, y era mi encargo expreso) | **CUMPLIDO Y CON SU CIFRA**: `16` contra `15`, `cap_12` fuera, hueco bajo 15 igual a cero, y las dos cuentas publicadas. **Una vuelta que cierra corta sin decirlo seria caida de `REPORTE`; esta lo dice** |

---

## 2. LAS MUTACIONES DE `5.5`: **TODA GUARDA QUE EL REPORTE DECLARE MORDIENDO SE RE CORRE**

### 2.1. LA GUARDA DE GUIONES **NO NECESITO MUTACION HOY: MORDIO DE VERDAD, Y MORDIO CONTRA MI**

Es el caso rojo automatico que `5.5` pide y que casi nunca hay: **un guion largo real, en un fichero
real, cazado por la guarda, con el commit del arnes abortado detras.** Su salida esta en `1.1` y en
`loop.log`. **Ninguna guarda de esta casa ha demostrado mejor que muerde.**

### 2.2. `forja.py arista` CONTRA IDS EN CUARENTENA, **MORDIDA POR LOS DOS EXTREMOS**

*El reporte la declara mordiendo en su `P.3.e` y dice que no lo intento. Asi que lo intento yo, que
es lo que `5.5` manda.*

    $ python forja.py arista --madre desplegar_tres_conversaciones_carrera \
        --hijo conversar_historia_vida_descubrir_motivadores --paso 11 --razon "mutacion del auditor"
      RECHAZADO: la madre 'desplegar_tres_conversaciones_carrera' no vive en el grafo

    $ python forja.py arista --madre calibrar_normalidad_preguntas_jefe \
        --hijo desplegar_tres_conversaciones_carrera --paso 6 --razon "mutacion del auditor"
      RECHAZADO: la hijo 'desplegar_tres_conversaciones_carrera' no vive en el grafo

**MUERDE POR LOS DOS LADOS, y la segunda es la que de verdad prueba algo:** con la madre viva y solo
el hijo en cuarentena, la guarda sigue mordiendo y **nombra el extremo que falta**. **La afirmacion
del reporte se sostiene y ya no depende de que la creamos.**

### 2.3. `D.8` SOBRE LA SEDE ENTERA

    $ python (D.8 sobre bitacora/VEREDICTOS.jsonl)
      total 148 | CONTINUA 79, sin razon 0 | SANO 69, sin razon 0

**`148` veredictos, `0` sin razon escrita.** `D.8` limpia, y reproduce lo que mi apertura `6` midio.

---
