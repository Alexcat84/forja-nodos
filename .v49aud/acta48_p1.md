
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
