
# ACTA 48. VUELTA 49, lote 7 (`grove_high_output`), **VUELTA DE SANEAMIENTO, LA QUINTA DESDE LA `44`**: **LA VUELTA ENTREGA LO QUE SE LE PIDIO Y SUS CIFRAS ME SALEN AL DIGITO**. Reproduzco sus **cuatro relojes de aduana** de sus propios ficheros (`559,4`, `1479,4`, `855,8`, `1174,4`), **recomputo la tabla de coste entera** con sus nueve porcentajes, **rehago la banda de Wilson de `0` de `20`** y me da su `0,1611` al cuarto decimal, **cuento por mi los `137` pasos de las `19` fichas de `cap_04`** y compruebo por diferencia que **las `19` conservan sus pasos identicos**, **corro los `44` tramos** y la cola de `14` que pego sale igual fila por fila, **el tallado me da `223 / 125 / 98` exacto**, y **sus `4` vecinos de cola los saco yo de sus dos informes al milesimo**. **Su censo de `782` lo reconstruyo y da `782`**: la diferencia con mis `780` de hoy es **mi propia apertura**, que sustituyo a la suya y aporta `2` rutas donde la anterior aportaba `4`. **De sus SEIS discutibles marcados se sostienen CINCO y CAE UNO**, el `5`: su *el censo solo suma `2` rutas porque la unidad de `D.42` es la CELDA y mis citas viven en bloques de codigo* **es falso como mecanismo**, y lo mido: `censar_rutas.py` **si** trata una linea de bloque como unidad y **si** la toma como sede cuando la ruta va sola entre comillas; lo que impide contarlas es que **el marcador `TALLADO` no lleva comillas invertidas y su ruta no llega a extraerse**. Es **prosa que el mismo marco como inferencia**, asi que **registra y NO acumula**, y `REPORTE` baja de `1 de 3` a **`0`** por `D.38.1`. `CLASE`, `CIFRA PUBLICADA` y `DATO MOVIDO` salen **LIMPIAS** con su motivo medido: `git diff 50a9d83..HEAD` sobre `dataset/`, `bitacora/`, `config/`, `censos/`, `esquema/`, `src/`, `scripts/`, `tests/`, `hooks/` y el banco **no imprime un solo fichero**. **Y DESENTIERRO LO MAS GRANDE DE ESTA AUDITORIA, QUE NO ES DE NADIE DE HOY Y SE COBRA EN LA VUELTA 50**: **`8` de las `19` fichas de `cap_04` declaran dentro de su propio `resumen_teorico` un numero de palabras que NI la frontera que ellas mismas citan NI mi recuento reproducen** (`P7` dice `356` y la frontera publica `210`; `P10` dice `337` contra `236`; `P19` dice `118` contra `76`), y **ningun rango del capitulo entero, ningun tokenizador y ningun recuento de caracteres da esas ocho cifras**: son ocho numeros escritos a mano en la vuelta 46, y las `19` fichas entran al grafo en la vuelta 50. **Y LA CAIDA QUE PESA ES MIA, Y SON DOS DE LA MISMA FAMILIA**: mi deuda `d031` cita `src/aduana.py` linea `315` como cuerpo de la senial `1` **y esa linea es cuerpo de la senial `3`**, y mi apertura sellada publica *`9` golpes en mi prosa* cuando **el mismo instrumento corrido hoy sobre la misma pagina da `12`**, porque lo corri antes de escribir mis dos ultimas secciones y **el golpe que se me escapo es un `unico` sin lista**, que es el patron que el remedio nombra con esa palabra. **`AUDITOR` sube de `1 de 3` a `2 de 3`**, penultimo escalon, **asi que mi remedio va ENCARGADO como TAREA BLOQUEANTE DEL AUDITOR y no solo declarado**. Ninguna condicion de parada se cumple: **no escribo `PARA_ALEXIS.md`**, y el encargo de la vuelta `50` sale de esta sede.

## 48.0. HUECO DE ACTA: **NO LO HAY**, y va antes que nada

La `ACTA 47` cubre la **vuelta 48** y yo audito la **vuelta 49**, que es la inmediatamente
siguiente. **Cubro una vuelta y ni una mas.**

## 48.1. LA HERENCIA DE `D.40`, DECLARADA Y COMPROBADA, Y UNA DE LAS DOS NO SE SOSTIENE

    $ git hash-object docs/loop/APERTURA_CIEGA.md
    e3c0555500a0a25079b95744b83b29acf35b826b
    $ tail -1 docs/loop/SELLOS_APERTURA.jsonl
    {"vuelta": 5, "fecha": "2026-09-19 12:09:05", "sello": "e3c0555500a0a25079b95744b83b29acf35b826b"}

Ese bloque mide la huella de mi pagina sellada contra el sello que el arnes guardo. `LECTURA`:
**el sello esta intacto y no toque la pagina despues de sellarla.**

| heredado | mi apertura declaro | lo que adjudico hoy |
|---|---|---|
| **`HEREDADO 1`** (correr la comprobacion y pegar su salida antes de escribir `CUMPLIDO`) | `CUMPLIDO`, con el barrido pegado entero en su seccion `14` y `9` golpes contestados uno a uno | **LA FORMA SI, LA SUSTANCIA NO.** La salida esta pegada, que es la letra del remedio; pero se corrio **antes** de escribir las secciones `14` y `15`, y el mismo instrumento sobre la pagina sellada da hoy `12` golpes y `11` universales. **`48.9.a`** |
| **`HEREDADO 2`** (toda frase mia que acompane a un pegado dice lo que ESE pegado mide) | `CUMPLIDO`, con el instrumento de la seccion `15` que saca los `23` bloques con su frase de encima y de debajo | **SE SOSTIENE, y lo compruebo leyendo**: el molde es el mismo en los `23`, la frase de debajo empieza por *Ese bloque mide* o *Ese bloque cuenta*, y **la conclusion va aparte y marcada `LECTURA`** |

## 48.2. LO QUE RECOMPUTE CON MIS PROPIOS COMANDOS, Y NO COPIE DE SU REPORTE

### 48.2.a. Las guardas y el estado

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python forja.py resolutor
    nodos vivos: 346
    nodos deprecados (archivo): 0
    alias registrados: 0
    $ time python tests/test_aceptacion.py
      total: 318 pruebas, 0 fallos, 0 errores
    real	1m41.879s
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
    $ ls cuarentena/grove_high_output/*.json | wc -l
    41

Ese bloque corre las cuatro guardas del arbol y cuenta las lineas de tres ficheros y los ficheros
de una carpeta. `LECTURA`: **las cuatro cifras de cierre que su `KK.5.a` publica (`346`, `740`,
`1`, `41`) son las mias**, y son las que mi propio encargo fijo por adelantado.

### 48.2.b. Las cifras que solo se pueden comprobar recomputandolas

| lo que verifique | el reporte publica | lo que me sale | de donde lo saco |
|---|---:|---:|---|
| **reloj de la aduana de `d027`** | `559,4` s | `9m19.396s` | `.v49/informe_d027.txt`, linea `real` |
| **reloj de la aduana de `d032`** | `1479,4` s | `24m39.398s` | `.v49/informe_d032.txt` |
| **reloj de `cap_02` `P2`** | `855,8` s | `14m15.821s` | `.v49/informe_cap02_1.txt` |
| **reloj de `cap_02` `P5`** | `1174,4` s | `19m34.408s` | `.v49/informe_cap02_2.txt` |
| **las cuatro pasadas** | `4069,0` s | `4069,0` | suma mia |
| **media por pasada** | `1017,3` s | `1017,25` | `4069,0` entre `4` |
| **correccion de prosa** | `2038,8` s, `44,2` por ciento | `2038,8`, `44,19` | `559,4` mas `1479,4` |
| **pasadas sobre el turno** | `88,2` por ciento | `88,20` | `4069,0` entre `4613,6` |
| **el turno en minutos** | `76,9` de `82,5` | `76,89` de `82,48` | `4613,6` y `4949` entre `60` |
| **la estimacion corta** | `12,6` por ciento | `12,61` | `1017,3` entre `903,4` |
| **la quinta pasada no cabe** | `880` menos `432` igual `448` | `448`, y la mas barata del dia costo `559,4` | aritmetica suya, correcta |
| **las `20` corridas de `d033`** | suma `449,7`; menor `21,7`, media `22,5`, mayor `23,1` | `449,7`; `21,7`, `22,48`, `23,1` | sumadas por mi de su tabla pegada |
| **la banda de `0` de `20`** | Wilson, de `0,0000` a `0,1611` | `0,1611` | recomputada con `z = 1,959964` |
| **el `1` de `6` queda fuera por** | `0,0056` | `0,1667` menos `0,1611` | mia |
| **tallado `D.41`** | `223 / 125 / 0 / 0 / 0 / 98` | **identico** | `python scripts/tallar_reporte.py` corrido hoy |
| **`P38` es el puesto** | `5` de `44` | `5` (`P5`, `P2`, `P34`, `P3`, `P38`) | `.v47aud/44_tramos.py` |
| **`P36` es el puesto** | `36` de `44`, `101` palabras | `36` de `44`, `101` | el mismo |
| **la cola de `14` de `JJ.3.b.bis`** | de `122` a `8`, catorce filas | **las catorce identicas** | el mismo |
| **los pasos de `cap_04`** | `137` | `137` en `19` fichas | `.v49aud/24_pasos_por_capitulo.py` |
| **marcadores `TALLADO` de la vuelta** | `30` (`29` mas el de `JJ.3.b.bis`) | `29` mas `1` | conteo mio sobre el reporte |
| **`KK.2.e`, el grep que no reproduce** | `3` contra `2` | `3` contra `2` | los dos `grep` corridos por mi |
| **los `4` vecinos de `KK.3.c`** | `0.614`, `0.412` y `0.429`, `0.397`, `0.372` | **los cuatro al milesimo** | sus dos informes de `cap_02` |
| **los `4` vecinos de `d027`** | `4` sobre umbral | `0.380`, `0.371`, `0.366`, `0.352` | su informe, y **son los mismos cuatro de mi barrido ciego** |
| **poblacion del barrido** | `390` (`346` mas `44`) | `346` mas `41` mas `3` | mi `.v49aud/12_poblacion_barrida.py` |
| **la deuda al cierre** | de `16` a `14` | `pendientes: 14    pagadas: 10` | `python scripts/deuda.py` |
| **el credito** | cinco rachas, ninguna en su tope | **identico** | `python forja.py credito` |
| **la cola de doctrina** | congelada en `11` | `11 pregunta(s), 0 bloquea(n)` | `python forja.py tablero` |

`LECTURA`: **las veinticuatro me salen.** Y el unico digito que no cuadra es de redondeo y lo
digo: la tabla de `KK.5.h` publica `4613,6` de total y **la suma de sus seis filas redondeadas da
`4613,5`**, porque el instrumento suma los relojes sin redondear y redondea una sola vez al final.
**Eso es la practica correcta, no una cifra falsa**, y lo compruebo con los segundos enteros de
sus ficheros (`559,396` mas `1479,398` mas `855,821` mas `1174,408` mas `449,7` mas `94,832`).

### 48.2.c. Las tres citas de linea que su reporte usa como prueba, abiertas por mi

    $ grep -n "^def senal_" src/aduana.py
    278:def senal_similitud_texto(texto_a, texto_b):
    295:def senal_familia_id(id_a, id_b):
    304:def senal_paso_contra_nodo(candidato, vecino):
    $ grep -n "^def tablas_de\|^def _declaracion" scripts/tallar_reporte.py
    112:def tablas_de(texto):
    139:def _declaracion(lineas, inicio, hasta=None):
    $ sed -n '392p;406p;419,421p' tests/test_aceptacion.py
            self.sucio = os.path.join(RAIZ, "tests", "tmp_archivo_con_guion.md")
                proceso = subprocess.Popen([interprete, "hooks/pre-commit"], cwd=RAIZ,
            codigo, salida, quien = self.correr_hook()
            self.assertEqual(codigo, 0,
                             "el repo ha de estar limpio antes de ensuciarlo:\n%s" % salida)

Ese bloque mide en que linea empieza cada funcion citada y que hay escrito en las cinco lineas de
`tests/` que su `KK.4.c` pega.

`LECTURA`: **las tres citas del reporte son exactas, y la lectura que `KK.2.d` saca de ellas
tambien.** La senial `1` compara `titulo` mas `resumen_teorico` mas pasos y la `3` compara los
pasos contra el cuerpo `titulo` mas `resumen_teorico`: **el `entregable_esperado` no entra en
ninguna de las dos**, asi que **su `sha1` identico antes y despues de la correccion de `d027` es
la prueba que dice ser**, y su `559,4` s se pagaron por un resultado determinado de antemano.

### 48.2.d. Su censo de `782` contra mis `780`: **lo reconstruyo y da `782`**

    $ python .v49aud/20_censo_por_documento.py
    docs/loop/REPORTE.md             pasan  614  caen 0   {'con contenido': 552, 'PATRON': 62}
    docs/loop/ACTA_AUDITOR.md        pasan  164  caen 0   {'con contenido': 145, 'VACIA A PROPOSITO': 3, 'PATRON': 10, 'vacia por protocolo': 6}
    docs/loop/APERTURA_CIEGA.md      pasan    2  caen 0   {'con contenido': 2}
    SUMA DE LOS TRES                  780
    .v49aud/apertura_v48.md          pasan    4  caen 0   {'con contenido': 4}

Ese bloque parte el censo por documento con las funciones del propio `scripts/censar_rutas.py`, y
mide aparte la apertura ciega **que estaba en el arbol cuando el extractor cerro**, sacada con
`git show 8d124c1:docs/loop/APERTURA_CIEGA.md`.

`LECTURA`: **`780` menos `2` mas `4` son `782`, su cifra exacta.** `censar_rutas.py` lee **tres**
documentos y uno de ellos es `APERTURA_CIEGA.md`: mi pagina sustituyo a la suya y aporta dos rutas
donde la anterior aportaba cuatro. **Su `782` era cierto de su arbol y mi `780` es cierto del mio,
y no hay caida.**

`LECTURA` **sobre el unico digito de su reparto que no reconstruyo**: el publica `700` con
contenido y `7` vacias por protocolo, y mi reconstruccion da `701` y `6`, **con la misma suma**.
La diferencia es una ruta de artefacto de maquina que estaba vacia en su instante y tiene
contenido en el mio. **Es el mismo desfase de momento que el propio reporte declara, medido en la
otra columna.**

## 48.3. LA GUARDA QUE DECLARA MORDIENDO, VUELTA A MORDER POR MUTACION (cosecha `7.C`)

**La que su reporte declara mordiendo es la puerta de `D.39`**: `KK.0.a` la mide cerrada y de ahi
saca sus cero inserciones. La muerdo sobre una **copia**, sin tocar `config/`:

    $ ( cd .v49aud/mut && python puerta.py )    con grove anadido a cerrados_en_extraccion en la COPIA
    grove_high_output CERRADO EN EXTRACCION: True
    $ python .v48/puerta.py                     sobre el arbol de verdad, intacto
    grove_high_output CERRADO EN EXTRACCION: False
    $ git status --short -- config/
    (sin salida)

Ese bloque mide la puerta con la celda que la decide cambiada y sin cambiar, y comprueba que el
arbol de verdad no se movio. `LECTURA`: **la medida responde a su entrada, asi que la cifra que el
reporte publica es real y no una firma.**

**Y LO QUE NO ME CALLO, PORQUE `7.C` ME MANDA DECLARAR SI HAY CASO ROJO AUTOMATICO:**

    $ grep -rn "cerrados_en_extraccion" src/ forja.py hooks/ scripts/
    src/tablero.py:89:    for grupo in ("liberados", "cerrados_en_extraccion"):
    src/tablero.py:187:    cerrados = declarado.get("cerrados_en_extraccion") or {}

Ese bloque mide **quien lee esa llave en el codigo de la casa**.

`LECTURA`: **la lee el tablero y nadie mas.** Ni `forja.py` ni ningun modulo del camino de
insercion la consultan, asi que **NO HAY CASO ROJO AUTOMATICO: la puerta de `D.39` es una regla
que el extractor aplica a mano, no una guarda que tumbe sola.** Lo declaro aqui, que es
exactamente lo que `7.C` manda hacer cuando no hay nada que tumbar por su cuenta. **REGISTRO Y NO
ADJUDICO** (`D.56` congela la doctrina y `D.45` me veda `src/`), y lo anoto en `DEUDA.jsonl` para
que no se pierda.

## 48.4. LA RELECTURA CIEGA: **SEIS DISCUTIBLES MARCADOS, CINCO SE SOSTIENEN Y UNO CAE**

*Empiezo por los marcados, que es lo que `5.1` ordena. Los que pude clasificar sin el reporte los
lleve ya decididos de la fase ciega; los que dependian de el los cierro aqui con su instrumento.*

| # | el discutible, por su numero y su seccion | mi adjudicacion |
|---:|---|---|
| **1** | `KK.3.d`: corto la `TAREA 3` y no la `4` | **SE SOSTIENE.** El encargo autoriza el corte **en la pasada** con esas palabras, y la `TAREA 3` es la que se mide en pasadas. Rehice su aritmetica: quedaban `448` s utiles y la pasada mas barata del dia costo `559,4`. **Y su motivo es el bueno**: una tasa con `13` corridas es otra tasa, y `d024` nace parcial con sus restantes nombrados |
| **2** | `KK.2.e`: deja dentro de la ficha una cita que hoy no reproduce | **SE SOSTIENE, y la declaracion vale mas que el defecto.** Corri los dos `grep`: el citado da `3` porque la ficha pasa a contener la cadena, el preciso da `2`. **La afirmacion es cierta y reproducible; lo defectuoso es la linea del metodo.** Sede `cuarentena/`, que `d027` ya adjudico que **no es sede de `5.2`**: registra y no acumula. **La reparacion va ENCARGADA para la vuelta 50**, donde esa ficha pasa la aduana de todos modos y sale gratis |
| **3** | `KK.2.a`: la correccion confinada al `entregable_esperado` | **SE SOSTIENE, y lo compruebo campo a campo.** El defecto vive en el `entregable` y solo ahi: `titulo` y `condiciones_activacion` no publican cuenta, `denominaciones.nombre_largo` **enumera sin escribir el numero**, y ningun paso lo escribe. **Y la propia ficha da el motivo bueno, no el del experimento**: *tocarlo sin necesidad habria movido la cola de vecinos sin que ninguna deuda lo pidiera*, con `src/aduana.py` linea `278` citada **correctamente** |
| **4** | `KK.4.b`: cruza su banda con el punto `1` de `6` | **SE SOSTIENE, porque el mismo escribe que no es un contraste formal.** Y traigo la discrepancia que me toca declarar y no resolver copiando: **mi apertura publico `39,3`, `13,9` y `10,9` por ciento** (cota exacta de una cola, Clopper y Pearson) **y el publica `16,11`** (Wilson a dos colas). **Las dos son correctas bajo su metodo y NO son comparables entre si** |
| **5** | `KK.5.e`: su lectura del censo | **CAE.** Ver `48.6.a` |
| **6** | `KK.1.a`: la columna `nodo(s)` es pronostico de la frontera y no lo minado | **SE SOSTIENE, y lo cierro mas fuerte que el.** El lo deducia de dos filas; yo lo cuento entero: la columna pronostica **`22`** nodos sobre `44` tramos y la bandeja tiene **`19`** fichas de `cap_04`. **La diferencia es `3`, que son exactamente `P41`, `P42` y `P44`**, los tres que `47.5.d` manda a la vuelta 50 |

    $ python .v49aud/26_discutibles.py     (la mitad que cierra el discutible 6)
    tramos de la frontera             : 44
    nodos PRONOSTICADOS por la columna: 22
    fichas de cap_04 en la bandeja    : 19
    diferencia                        : 3

Ese bloque suma la columna `nodo(s)` de los `44` tramos y la compara con las fichas de `cap_04`
que hay en la bandeja.

**DENTRO CONTRA FUERA DEL MARCADO** (`5.3`, y es la cifra que mueve el credito): **`1` caida
DENTRO del marcado de `6`, `0` FUERA.** La unica caida del reporte es la que el mismo puso en su
lista antes de saber si acertaba, **que es justo lo que la metrica quiere premiar**: el extractor
sabia donde estaba su duda.

## 48.5. LAS ADJUDICACIONES

### 48.5.a. **`8` DE LAS `19` FICHAS DE `cap_04` DECLARAN PALABRAS QUE NADIE REPRODUCE**

**Mi fase ciega lo trajo como hallazgo y dijo que solo se cerraba contra la tabla de frontera, que
vive en el reporte. Hoy lo cierro.**

    $ python .v49aud/25_de_donde_sale_la_cifra.py
    ficha                                                pieza rango declarado   dice cuento  que rango daria la cifra declarada
    buscar_actividad_alta_palanca_tres_vias              P19   L203  a L213     118     76  L196 a L213
    detectar_palanca_negativa_actividad_mando            P21   L219  a L219      73     73  -- cuadra --
    detectar_palanca_negativa_actividad_mando            P24   L231  a L235     356    356  -- cuadra --
    elegir_momento_actividad_palanca_maxima              P20   L215  a L217     297    237  ninguno cercano
    empujar_persona_reunion_direccion_preferida          P13   L167  a L167     174    147  ninguno cercano
    escalonar_fuentes_informacion_gerencial              P9    L153  a L153     208    183  ninguno cercano
    programar_visita_area_observar_despachar             P10   L155  a L157     337    236  ninguno cercano
    reunir_informacion_gerencial_vias_variadas           P7    L145  a L147     356    210  ninguno cercano
    subir_productividad_gerencial_tres_vias              P18   L195  a L201      62     60  ninguno cercano
    transmitir_objetivos_prioridades_preferencias        P11   L159  a L159     197    160  ninguno cercano

    piezas declaradas leidas: 10 ; cuadran 2 ; discrepan 8

Ese bloque cuenta las palabras del rango de lineas que cada ficha declara dentro de su propio
`resumen_teorico`, las compara con la cifra que esa misma ficha escribe, y busca si algun rango
vecino daria la cifra declarada.

**Y LA FRONTERA QUE ESAS OCHO FICHAS CITAN DICE LO QUE DIGO YO, no lo que dicen ellas:**

    $ sed -n '43941p;43943p;43944p;43945p;43947p;43952p;43953p;43954p' docs/loop/REPORTE.md
    | L145 a L147 | 210 | 1 | P7  LAS VIAS POR LAS QUE LLEGA LA INFORMACION...
    | L153 a L153 | 183 | 1 | P9  LA JERARQUIA DE LA INFORMACION...
    | L155 a L157 | 236 | 1 | P10 LA VISITA AL SITIO...
    | L159 a L159 | 160 | 1 | P11 transmitir objetivos, prioridades y preferencias...
    | L167 a L167 | 147 | 1 | P13 EL EMPUJON...
    | L195 a L201 |  60 | 1 | P18 CABEZA DE SERIE: las TRES vias de subir la productividad gerencial...
    | L203 a L213 |  76 | 1 | P19 CABEZA DE SERIE: las TRES vias basicas de la actividad de alta palanca...
    | L215 a L217 | 237 | 1 | P20 la palanca depende de CUANDO...

Ese bloque imprime ocho filas de la tabla de frontera de `cap_04` publicada en la vuelta 46
(`HH.2.c`), que es la frontera que esas ocho fichas nombran dentro de si mismas.

`LECTURA`: **las ocho fichas contradicen a la frontera que citan, y mi recuento coincide con la
frontera en las ocho.** Y no es una forma distinta de contar: probe el recuento por espacios, por
palabras alfanumericas y por caracteres, **y ninguno da esas ocho cifras**; y probe todos los
rangos contiguos del capitulo entero, **y solo `P19` encuentra uno** (`L196 a L213`), que no es el
que la ficha declara. **Son ocho numeros escritos a mano.** Las dos que cuadran (`P21` y `P24`)
son las de la ficha que NO nace de ese molde, y **las tandas de las vueltas 47 y 48 cuadran todas
al digito**, medido en mi fase ciega.

**ADJUDICO, Y EN TRES PIEZAS:**

1. **NO ES CAIDA DE ESTA TANDA.** Las ocho se escribieron en la **vuelta 46**; esta vuelta toco
   dos fichas y solo una de ellas es de las ocho (`P7`), en un campo distinto. **Una racha cuenta
   tandas, y esta tanda no las escribio.**
2. **NO ES `CIFRA PUBLICADA`**, porque la sede es `cuarentena/<libro>/<id>.json` y `d027` ya
   adjudico que **una ficha de cuarentena no es sede de `5.2`**, recogido en la `ACTA 47`.
3. **PERO SE PAGA ANTES DE LA INSERCION, Y ESO SI ES MIO DE ENCARGAR.** Las `19` fichas entran al
   grafo en la vuelta 50, y en cuanto entren esas ocho cifras dejan de estar en la bandeja. **Es
   la enfermedad que el protocolo nombra en su propia cabecera** (*la vara es el instrumento,
   nunca un campo declarado a mano*), y el remedio es de una linea por ficha: **escribir el numero
   que la frontera publica, por correccion declarada y sin borrar el viejo.** Va en la `TAREA 2`
   del encargo y queda anotado en `DEUDA.jsonl`.

**Y LO QUE ESTO NO TUMBA, dicho para que no se lea de mas:** no tumba ninguna de las dos
correcciones de esta vuelta, que van por otro sitio y las verifique contra el libro; no tumba el
`0` `PUENTE` de `cap_04`, que es sobre pasos y no sobre palabras; y no tumba la tabla de frontera
de `HH.2.c`, **que es precisamente la que sale bien.**

### 48.5.b. **LO DEMAS QUE ADJUDICO, SIN REABRIR LO QUE YA ESTABA ADJUDICADO**

| # | lo que adjudico | con que |
|---:|---|---|
| `a` | **el cierre corto de `d024` en `2` de `3` es correcto y esta DECLARADO con sus tres piezas**: el numero, el reloj y los `5` que quedan nombrados uno a uno | `EXTRACTOR.md` 12.4 me manda verificar que el cierre corto se declare, **y se declara** |
| `b` | **`d024` sigue abierta y tiene que seguirlo.** Pasa de `7` sin medir a `5` sin medir, y son `5` y no `4` porque el tramo cerro en `2` | el encargo lo fijo por adelantado y `scripts/deuda.py` la lista viva |
| `c` | **`d033` NO se marca pagada aunque su tarea cerro, y hace bien**: su propio `KK.4.d` escribe que la condicion de la roja observada, el arbol en movimiento, **no se ha reproducido** | su registro sigue vivo en `scripts/deuda.py`, y `KK.4.d` razona contra su propio interes |
| `d` | **la propuesta de saltarse el recalculo cuando el `sha1` del texto de las seniales no cambia queda RECOGIDA Y NO ADJUDICADA**: vive en `src/` y `D.45` la deja fuera de toda sesion en paralelo. **Es parada de `src/`, no parada de bucle** | `D.45`, y `48.2.c` verifica que la medida que la sostiene es correcta |
| `e` | **su lectura de `KK.2.d` es correcta y la FIRMO**: las dos especies de correccion no son la misma cosa. La que no toca el texto de las seniales es **inutil de recalcular y cara de correr**, y esta demostrado con su `sha1`, no supuesto | `48.2.c` |
| `f` | **`cap_04` cierra en la vuelta 50 con `P41`, `P42` y `P44`, y NO se salta a `cap_05`**, aunque `forja.py tablero --puedo` diga *continuar desde el capitulo siguiente al ultimo minado*. **Esa es la trampa que la `ACTA 45` desenterro y sigue viva**: es `d028`, y `D.45` la deja fuera de mi alcance | `47.5.d`, y `48.4` fila `6` mide que faltan exactamente `3` |
| `g` | **la colision de `D.52` se volvio a pagar a mano por quinta vez y el sello es el bueno**: las dos huellas `9bf10e67...` que compare en la fase ciega salen de `git hash-object`, **sin leer una sola celda de ninguna de las dos tablas** | `d030`, que `D.45` tambien deja fuera de mi alcance |
| `h` | **su `KK.5.f` nombra a `d024` y a `d031` como no pagadas y omite a `d033` de esa lista.** No es caida: el registro esta bien y la aritmetica de `16` a `14` lo hace inferible, pero **una lista de lo que NO se paga que deja fuera una de las tres se lee mal**, y lo dejo escrito | `scripts/deuda.py`, que las lista vivas las tres |

## 48.6. LAS CAIDAS DEL EXTRACTOR, CON SU SEDE Y SU CUENTA

### 48.6.a. **UNA, Y ES LA QUE EL MISMO MARCO: EL MECANISMO DEL CENSO** (`KK.5.e`, punto `1`)

**Lo que publico:** *el censo solo suma `2` rutas, porque **la unidad de `D.42` es la CELDA** y la
mayoria de mis citas viven en bloques de codigo, no en celdas.*

    $ python .v49aud/26_discutibles.py
    marcador TALLADO tal cual                unidades 1  rutas extraidas ninguna
    marcador TALLADO con comillas            unidades 1  rutas extraidas [('.v49/coste.txt', 'linea', False)]
    linea de bloque con comando              unidades 1  rutas extraidas ninguna
    linea de bloque, ruta sola en comillas   unidades 1  rutas extraidas [('.v49/coste.txt', 'linea', True)]
    celda de tabla de donde sale             unidades 3  rutas extraidas [('.v49/coste.txt', 'celda 3', True)]

Ese bloque pasa cinco formas de cita por `unidades_de`, `parece_ruta` y `es_sede` de
`scripts/censar_rutas.py`, e imprime que ruta extrae cada una y si la toma como sede.

`LECTURA`: **una linea de bloque SI es una unidad del censo y SI puede ser sede**, como muestra la
cuarta fila. **Lo que impide contar sus treinta marcadores es otra cosa: el marcador `TALLADO` no
lleva comillas invertidas**, y `EN_COMILLAS` solo extrae lo que va entre ellas, **asi que su ruta
no llega a extraerse nunca.** La cifra `2` es cierta; **el porque es falso.**

**SEDE Y CUENTA:** vive en **prosa de acompanamiento** de `KK.5.e`, no en tabla ni en cabecera ni
en conclusion, **y el propio reporte la marco como inferencia** en su fila `5` de discutibles
(*lo deduzco de que la cifra no se movio, no de haber leido `censar_rutas.py`*). Por `5.2`,
**REGISTRA Y NO ACUMULA.**

**LO QUE SI HIZO BIEN, y no es un consuelo sino la diferencia entre esta caida y otra:** marco el
sitio antes de saber si acertaba y dijo con sus palabras que era una inferencia. **Una inferencia
declarada que resulta falsa cuesta una linea de acta; una inferencia escondida dentro de la frase
de una cifra viaja de acta en acta.**

### 48.6.b. **LO QUE COMPROBE ANTES DE DECIR QUE NO HAY MAS**

| especie | esta tanda | como lo comprobe |
|---|---|---|
| **`CLASE`** | **NINGUNA, y no es opinion** | `bitacora/VEREDICTOS.jsonl` sigue en `740` y `config/pares_mutuos.jsonl` en `1`: **la vuelta no escribio ni un veredicto**, asi que no hay veredicto que poder poner mal |
| **`DATO MOVIDO`** | **NINGUNA** | `git diff --stat 50a9d83..HEAD` sobre `dataset/`, `bitacora/`, `config/`, `censos/`, `esquema/`, `src/`, `scripts/`, `tests/`, `hooks/`, `forja.py` y el banco **no imprime un solo fichero** |
| **`CIFRA PUBLICADA`** | **NINGUNA** | las unicas sedes duraderas que la vuelta toco son dos fichas de `cuarentena/`, que `d027` adjudico que **no son sede de `5.2`**; y sus dos correcciones las verifique renglon a renglon contra el libro en mi fase ciega |
| **`REPORTE`** | **UNA, y NO acumula** | `48.6.a`. Recompute ademas las veinticuatro filas de `48.2.b` y **ninguna otra se movio** |

**LA TANDA ES LIMPIA PARA LA ESPECIE QUE `REPORTE` ACUMULA**, asi que por la correccion declarada
del 16 sep 2026 en `5.4` (*`LIMPIA` significa sin caidas de la especie que esa racha acumula, y
una tanda con caidas solo de las que no acumulan reinicia la racha igual*) **`REPORTE` baja de
`1 de 3` a `0`.** **No es un indulto mio: es la letra**, y la caida queda escrita arriba con su
nombre, que es lo que `5.4` dice que la hace util.

## 48.7. LA MUESTRA PINEADA DE LOS SANOS (`AUDITOR_FORJA.md` 7)

    $ git diff --stat 50a9d83..HEAD -- bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
    (sin salida)
    $ wc -l bitacora/VEREDICTOS.jsonl
    740 bitacora/VEREDICTOS.jsonl

Ese bloque mide si la vuelta escribio algun veredicto y cuantos hay en el registro.

`LECTURA`: **la tanda tiene `0` veredictos `SANO`, porque tiene `0` veredictos.** La seccion `7`
manda releerlos todos mientras sean menos de tres: **releo los cero y publico la cifra**, que es
lo que la regla pide. **No invento una muestra donde no hay poblacion**, y con `0` de `0` **no hay
tasa ni banda que publicar**: una tasa sobre cero casos no es un cero, es una celda que no existe.
**Semilla: no hace falta, porque no hay nada que sortear**, y decirlo es mas honesto que escribir
un numero al lado de una muestra vacia.

## 48.8. `PASOS INVENTADOS POR CAPITULO` (`AUDITOR_FORJA.md` 8). **UNA FILA POR CAPITULO**

    $ python .v49aud/24_pasos_por_capitulo.py
    cap_02    7 fichas    50 pasos
    cap_03   15 fichas   121 pasos
    cap_04   19 fichas   137 pasos
    contra HEAD~1  : 19 fichas con los MISMOS pasos, 0 distintas, 0 ausentes
    contra HEAD    : 19 fichas con los MISMOS pasos, 0 distintas, 0 ausentes

Ese bloque cuenta los pasos de cada ficha de la bandeja de `grove_high_output`, repartidos por el
`cap_NN.md` que la propia ficha declara, y compara paso a paso las `19` de `cap_04` contra el
commit anterior y contra el de la vuelta.

| capitulo | pasos escritos EN ESTA VUELTA | `PUENTE` | por ciento | el denominador vivo, contado hoy por mi |
|---|---:|---:|---|---|
| `cap_02` | **`0`** | **`0`** | **sin fila**: `0` entre `0` | `50` pasos en `7` fichas |
| `cap_03` | **`0`** | **`0`** | **sin fila**: `0` entre `0` | `121` pasos en `15` fichas |
| `cap_04` | **`0`** | **`0`** | **sin fila**: `0` entre `0` | `137` pasos en `19` fichas |
| **total del lote 7** | **`0`** | **`0`** | **sin fila** | `308` pasos en `41` fichas |

**POR QUE NO HAY PORCENTAJE, Y POR QUE NO ES UN CERO:** una vuelta de saneamiento **no escribe un
solo paso**, asi que el numerador y el denominador son los dos cero. **Mi propio encargo lo dijo
por adelantado** y la vuelta lo cumplio con su motivo escrito (`KK.5.g`), **que es justo lo que
`8.3` punto `3` pide que no falte.**

**Y LO QUE SI FIRMO, PORQUE LO MEDI Y NO LO COPIE:** **`cap_04` sigue en `0` `PUENTE` de `137`
pasos.** La razon por la que no hace falta releer los `137` contra su renglon es que **ninguno se
movio**: las `19` fichas conservan sus pasos identicos contra `HEAD~1` y contra `HEAD`, medido por
diferencia, y la unica que cambio por dentro cambio su `resumen_teorico` **y ni un paso**.

**EL VOLUMEN DEL LOTE SIGUIENTE NO SE MUEVE** (`8.1`): sin fila no hay comparacion que hacer, y la
ultima medida viva sigue siendo la de la vuelta 48. **La vuelta 50 corre al escalon que `47.5.d`
ya fijo**: cerrar `cap_04` con `P41`, `P42` y `P44`.

## 48.9. MIS CAIDAS PROPIAS, CON MI NOMBRE. **DOS, Y LAS DOS DE LA MISMA FAMILIA**

### 48.9.a. **Mi apertura sellada publica `9` donde su propio instrumento da `12`**

    $ python .v49aud/17_superlativos.py      (MI instrumento, corrido HOY sobre la pagina sellada)
    SUPERLATIVOS, que es lo que el remedio obliga a contestar: 12 golpes en mi prosa, 16 lineas sangradas descartadas
       ...
       linea 655  [superlativo con nombre en medio] el grafo mas
       linea 656  [superlativo con nombre en medio] la ficha declara de mas
       linea 684  [unicidad                  ] unico          ...rase es cierta:** eso es lo unico que una maquina no puede...

    AFIRMACIONES UNIVERSALES, que no las pide el remedio y las barro igual: 11 golpes en mi prosa
       ...
       linea 785  [universal afirmativa      ] todos          ...s de esta pagina se lista a todos menos a si mismo**...

Ese bloque corre **mi propio instrumento del remedio** sobre la apertura tal como quedo sellada, y
su cabecera imprime la cuenta de golpes.

`LECTURA`: **mi pagina publica `9` y `10`; el mismo instrumento sobre el mismo fichero da hoy `12`
y `11`.** La causa es mia y es de las de siempre: **lo corri antes de escribir mis secciones `14` y
`15`, y despues segui escribiendo.** De los tres golpes de mas, **dos son mi propia tabla de
contestaciones repitiendo frases ya contestadas** (lineas `655` y `656`), **pero el de la linea
`684` es un superlativo nuevo y sin contestar**: *eso es lo unico que una maquina no puede hacer
aqui*, **sin lista de lo que una maquina si puede hacer.** Y `unico` **es literalmente uno de los
cuatro patrones que el `REMEDIO 1` de la `ACTA 46` nombra por su nombre**.

**ES `CIFRA PUBLICADA PROPIA`** (`D.38.2`: *una cifra falsa en tu acta o en tu apertura sellada*):
el `9` no describe la pagina que sella. **Y es tambien la sustancia del `REMEDIO 1` rota**, que es
la otra especie de mi racha. **Las dos viven en la misma racha y la suben una sola vez**, porque
una racha cuenta tandas y no caidas.

**LO QUE NO ME ABSUELVE, Y LO DIGO YO:** la letra del `HEREDADO 1` pide pegar la salida, y la
pegue. **Pero el remedio existe para que ningun superlativo mio quede sin lista, y uno quedo.**
Cumplir la forma de un remedio y romperle la sustancia es exactamente lo que le acabo de cargar al
extractor en `48.6.a`, y no me lo puedo cobrar en un sitio y perdonar en el otro.

### 48.9.b. **Mi deuda `d031` cita una linea que no es de la senial que dice**

    $ grep '"d031"' docs/loop/DEUDA.jsonl      (el trozo que lo dice)
    ... el resumen_teorico alimenta la senial 1 (src/aduana.py linea 315) ...
    $ awk 'NR>=314 && NR<=315' src/aduana.py
        cuerpo_candidato = comun.normalizar_texto(
            "%s. %s" % (candidato.get("titulo") or "", candidato.get("resumen_teorico") or ""))

Ese bloque imprime lo que escribi en `d031` y lo que hay en la linea `315` de `src/aduana.py`.

`LECTURA`: **la linea `315` es cuerpo de `senal_paso_contra_nodo`, que es la senial `3` y empieza
en la `304`** (`48.2.c`). La senial `1` empieza en la `278`. **La sustancia de `d031` se sostiene y
es incluso mas ancha de lo que escribi** (el `resumen_teorico` alimenta la `1` **y** la `3`),
**pero la linea que publique como prueba de la `1` no es de la `1`.** Sede `docs/loop/DEUDA.jsonl`,
que es `docs/`, y por tanto sede de `5.2`. **La cita es mia y el fallo es mio.**

**Y LA AGRAVA que el extractor, en esta misma vuelta, cito la `278` CORRECTAMENTE dentro de la
ficha de `d027`.** El la tenia bien y yo la tenia mal.

**CORRECCION DECLARADA, SIN BORRAR**, anotada en el mismo registro con su linea nueva y su cita a
esta seccion.

### 48.9.c. **LO QUE COMPROBE ANTES DE DECIR QUE NO HAY MAS**

Volvi a medir hoy las cifras de mi pagina sellada, una a una: `346`, `740`, `1` y `41`; el reparto
`7`, `15` y `19` de la bandeja; las `469`, `396`, `242` y `101` palabras; los `390` de poblacion;
los `4` y los `0` vecinos sobre umbral y sus digitos; los `15` pares de `cap_02`; el `23` de
bloques pegados; las huellas `997ece8f`, `f6f4f4dd`, `17327e3a` y `9bf10e67`; y las `14` deudas
vivas con sus `10` pagadas. **Ninguna se movio.** Las dos unicas que no se sostienen son las de
`48.9.a` y `48.9.b`.

### 48.9.d. **MI TAREA BLOQUEANTE DEL AUDITOR PARA LA VUELTA 50** (`5.5`, escalada al penultimo escalon)

> **`AUDITOR` esta en `2 de 3`. La escalada se ENCARGA, no solo se declara**, y declararla sin
> encargarla seria una caida propia mas, escrita con mi nombre.

| | |
|---|---|
| **TAREA BLOQUEANTE DEL AUDITOR, vuelta 50** | **El barrido del remedio se corre COMO ULTIMA OPERACION de mi fase ciega, sobre la pagina ya terminada, y su salida se pega DESPUES de todo lo demas.** Si al pegarla escribo una linea mas de prosa, **lo vuelvo a correr.** La cuenta de golpes que publique tiene que ser la del fichero que el arnes va a sellar, **no la de una version intermedia** |
| **como se comprueba que esta roto** | se corre `.v49aud/17_superlativos.py` (o su sucesor) **sobre la apertura ya sellada** y se compara su cabecera con la cuenta que la pagina publica. **Si no coinciden, roto**, sin discusion y sin necesidad de leer una sola frase |
| **por que esta forma y no otra** | mis tres ultimas caidas propias son de la misma familia: **una cifra de la fase ciega que dejo de ser cierta porque la pagina siguio creciendo.** El remedio no puede ser *acuerdate*: tiene que ser **un orden de operaciones con una comprobacion mecanica al final** |
| **`REMEDIO` segundo, que sigue vivo y esta tanda CUMPLIO** | el `HEREDADO 2` de la `ACTA 47`: toda frase mia que acompane a un pegado dice lo que ESE pegado mide, y la conclusion va aparte y marcada `LECTURA` |

## 48.10. EL CREDITO DE ESTA TANDA

| especie | esta tanda | racha al cerrar | por que |
|---|---|---|---|
| **`CLASE`** | **LIMPIA** | **`0 de 2`** | cero veredictos escritos en la vuelta (`740` contra `740`, medido por diferencia) |
| **`CIFRA PUBLICADA`** | **LIMPIA** | **`0 de 2`** | las dos sedes duraderas que la vuelta toco son fichas de `cuarentena/`, que `d027` adjudico que no son sede de `5.2`, y sus correcciones las verifique contra el libro |
| **`DATO MOVIDO`** | **LIMPIA** | **`0 de 2`** | el `git diff` de la vuelta entera sobre `dataset/`, `bitacora/`, `config/` y `censos/` sale vacio |
| **`REPORTE`** | **`1` caida, de PROSA, NO acumula** | **de `1 de 3` a `0`** | `48.6.a`, y `5.4` corregida el 16 sep: una tanda con caidas solo de las que no acumulan **reinicia la racha igual** |
| **`AUDITOR`** | **`2` caidas, las dos de mis especies** | **de `1 de 3` a `2 de 3`** | `48.9.a` y `48.9.b`. **Lo subo yo**, y por eso `48.9.d` va encargada y no solo declarada |

## 48.11. LAS CONDICIONES DE PARADA (`AUDITOR_FORJA.md` 3): **NINGUNA SE CUMPLE**

| condicion | como sale | medido con |
|---|---|---|
| **doctrina NUEVA necesaria** | **NO.** Las adjudicaciones de `48.5` se apoyan en reglas escritas y citadas: `5.2`, `5.4`, `7.B`, `7.C`, `D.38.1`, `D.45`, `47.5.d` y la adjudicacion de sede de `d027`. **Y las dos preguntas nuevas que traigo** (la puerta de `D.39` sin caso rojo automatico, y las ocho cifras declaradas a mano) **se registran con su medida y se quedan ahi**, que es lo que `D.56` manda hacer con una pregunta nueva | `48.3`, `48.5.a` |
| **contradiccion con regla o cifra publicada** | **NO.** Las tres correcciones de esta vuelta, las dos del extractor y la mia de `d031`, se escriben por **correccion declarada sin borrar**, que es el mecanismo que ya existe | `48.5`, `48.9.b` |
| **decision de Alexis** | **NO.** No se borra contenido, no se mueve un umbral, no se cambia el alcance, no se crea un remoto, no se publica fuera del repo | `git diff` de `config/` vacio |
| **fallo tecnico repetido** | **NO.** `gate`, `guiones`, las `318` pruebas, el tallado y el censo: **los cinco verdes hoy y corridos por mi.** La corrida roja de `d033` **no se repitio**: las `20` del extractor mas mis `6` dan `0` de `26` | `48.2.a` |
| **credito roto** | **NO.** `AUDITOR` en `2 de 3` y el tope es `3`; las otras cuatro por debajo del suyo | `48.10` |
| **campania consumada** | **NO** | `python forja.py tablero`: *MUNDO 11: faltan 3 de 3 libros del corte* |

**NO ESCRIBO `docs/loop/PARA_ALEXIS.md`.** El encargo de la vuelta `50` sale de esta sede.

## 48.12. EL COSTE DEL TURNO (`D.55`)

    $ python -c "import json,io;print(json.loads(io.open('docs/loop/ultimo_apertura.json',encoding='utf-8').read())['total_cost_usd'])"
    12.353634999999997

Ese bloque lee el coste que **el arnes** escribio para mi fase ciega. El de este segundo turno no
lo puedo leer desde dentro, porque el arnes lo escribe cuando mi turno ya termino.

**`12,35` USD en la fase ciega sola, por encima de los `10` de `D.55`, y lo declaro aunque la
vuelta sea de saneamiento.** En que se fue, con su instrumento al lado: **los barridos `D.38.4`**,
que miden la senial `1` de cada ficha contra los otros `389` de la poblacion **uno a uno y sin
muestra**. Solo los nueve de la fase ciega (`d027`, `d032` y los `7` de `cap_02`) costaron
`378,0`, `820,3`, `510,8`, `426,7`, `140,6`, `127,0`, `185,0`, `166,3` y `223,2` s, que suman
**`2.977,9` s de reloj**. **No hay forma barata de cumplir `D.38.4`:** la alternativa es aproximar,
y aproximar es justo lo que la regla prohibe.

**LA PIEZA CARA DE ESTE SEGUNDO TURNO ES LA PRUEBA DE ACEPTACION** (`318` pruebas, `1m41.879s`) y
**el resto son guiones de segundos**: el tallado, el censo partido por documento, los `44` tramos,
el recuento de pasos, la mutacion de la puerta sobre una copia y la aritmetica. **En mis dos
turnos no corre ni una aduana**, que es la pieza que se lleva el `88,2` por ciento del turno del
extractor. **Su turno es caro en reloj de maquina y el mio en fichas leidas.**
