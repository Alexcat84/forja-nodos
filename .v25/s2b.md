
### S.2.b. **CORRECCION 1: LA CIFRA SE CALCULA, Y LA MENTIRA TENIA UNA CUARTA SEDE QUE EL ACTA NO ENCONTRO**

**EL ARREGLO ES EL QUE `D.41` ESCRIBE, y no es teclear la celda buena:** la linea 68 de
`.v24/freno_cierre.py` escribia `cinco` a mano mientras la linea 77 CALCULABA `7 de 13`. **Ahora las
dos calculan, y de la misma lista `NUM`:**

    $ sed -n "68,70p" .v24/freno_cierre.py
    print('| **el lote 4 ENTERO** | **%d** | **%d** | **%d** | **%.2f** | **INCOMPLETO: %d filas sin releer con el ancho** |'
          % (tot_cand, tot_pasos, tot_num, 100.0 * tot_num / tot_pasos,
             len([1 for _c, _n, _q, f in NUM if not f])))

> ### **Y BUSCANDO SU GEMELA ENCONTRE EL ORIGEN, QUE ES UNA CUARTA SEDE Y NADIE LA HABIA NOMBRADO**
>
>     $ grep -rln "INCOMPLETO: cinco filas" --include=*.py .
>     ./.t1_v23/freno_v23.py
>
> **`.t1_v23/freno_v23.py` linea 67 tiene la misma celda tecleada, y es de donde los dos instrumentos
> de la vuelta 24 la copiaron.** Su tabla vive en el reporte de la vuelta 23 (`| el lote 4 hasta
> cap_13 | 127 | 1511 | 35 | 2.32 | INCOMPLETO: cinco filas ... |`) **y tambien era falsa**: su lista
> `NUM` tiene **12 filas, 6 firmadas y 6 de hueco**, contado por mi hoy con `.v25/arreglar_cinco.py`:
>
>     .t1_v23/freno_v23.py: filas en NUM 12, FIRMADAS 6, HUECO calculado 6
>     .v24/freno_v24.py   : filas en NUM 13, FIRMADAS 7, HUECO calculado 6
>     .v24/freno_cierre.py: filas en NUM 13, FIRMADAS 7, HUECO calculado 6
>
> **El acta nombro tres sedes de tabla en la vuelta 24 y dos suyas. Son CUATRO de tabla, y la cuarta
> es la primera.** Lo digo porque la conclusion del auditor (*tres sedes, tres vueltas, y ninguna de
> las tres lo caza porque las tres copian*) **se refuerza con la cuarta, no se debilita**: el `cinco`
> entro en el codigo UNA vez y despues **viajo por copia de instrumento a instrumento**, que es
> exactamente lo que `D.41` dice de las tablas, aplicado un piso mas abajo.
>
> **COMO SE REGENERO CADA UNA, Y POR QUE NO RE EJECUTE LOS TRES INSTRUMENTOS ENTEROS:** su poblacion
> de ficheros **cambio** (once candidatos pasaron de `cuarentena/` a `_insertados/` en la vuelta 24),
> asi que re correrlos hoy daria **un denominador de hoy bajo un rotulo de entonces**, que es
> falsear la historia para arreglar una celda. `.v25/arreglar_cinco.py` **lee la lista `NUM` del
> propio fichero fuente, cuenta las filas sin firmar y regenera SOLO esa celda**. La cifra no se
> teclea en ningun punto de la cadena.

**LA PRUEBA DE QUE LA CORRECCION NO TOCO NADA MAS, y es la que a mi me importaba:**

    $ diff .v25/t1_cierre_viejo.txt .v24/freno_cierre_t1.txt
    16c16
    < | **el lote 4 ENTERO** | **142** | **1688** | **35** | **2.07** | **INCOMPLETO: cinco filas sin releer con el ancho** |
    ---
    > | **el lote 4 ENTERO** | **142** | **1688** | **35** | **2.07** | **INCOMPLETO: 6 filas sin releer con el ancho** |

**UNA linea de dieciseis. Las quince filas de capitulo, el `142`, el `1688`, el `35` y el `2.07` son
las mismas.** Y los dos ficheros viejos (`R.5.g` y `R.10`) eran **identicos entre si**, comprobado
con `diff` y no supuesto, que es lo que el reporte de la vuelta 24 afirmaba en prosa.

**LAS SEDES TOCADAS, UNA A UNA:**

| sede | especie | como se corrigio |
|---|---|---|
| `R.5.g`, celda del total | **TABLA** de instrumento | **regenerada por `python scripts/tallar_reporte.py --arreglar`**, que la reescribe desde el fichero del instrumento ya arreglado |
| `R.10`, la misma celda recomputada | **TABLA** de instrumento | idem, en la misma corrida |
| **la tabla de la vuelta 23**, *el lote 4 hasta `cap_13`* | **TABLA** de instrumento | idem, tras arreglar el origen `.t1_v23/freno_v23.py`. # **ES LA CUARTA SEDE Y LA ENCONTRE YO** |
| `R.12.d`, *la relectura ancha ... 5 filas* | **TABLA sin instrumento declarado** | no hay instrumento del que regenerarla, asi que va **TACHADA y no borrada**, con la cifra nueva y el porque al lado |
| las **seis** sedes de prosa de las vueltas 23 y 24 | **PROSA** | tachadas y no borradas, cada una con su correccion declarada |

**Y LAS CIFRAS DEL HUECO, REMEDIDAS POR MI Y NO COPIADAS DEL ENCARGO** (`EXTRACTOR.md` 5, que es la
regla que esta caida rompio, y por eso aqui se aplica con mas motivo). Salida de
`python .v25/hueco.py`, guardada en `.v25/hueco.txt`:

<!-- TALLADO: parcial salida=.v25/hueco.txt -->

| fila de hueco | candidatos | pasos | ocurrencias que su rotulo declara |
|---|---:|---:|---:|
| `cap_01` | 1 | 9 | 1 |
| `cap_03` | 1 | 10 | 6 |
| `cap_05` | 8 | 76 | 20 |
| `cap_06` | 10 | 117 | 33 |
| `cap_07` | 25 | 225 | 20 |
| `cap_08` | 12 | 102 | 17 |
| **el hueco entero** | **57** | **539** | **97** |

**ME SALEN LAS CUATRO IGUALES QUE AL ENCARGO: `6` filas, `57` candidatos, `539` pasos, `97`
ocurrencias.** Lo escribo asi y no como *confirmo las del encargo*, porque **la medicion es mia y la
coincidencia es el resultado, no el metodo.**

### S.2.c. **CORRECCION 2: `unidad: cap_11` DONDE EL FICHERO ESCRIBE `cap_09` DOS VECES**

Salida de mi lectura de hoy, guardada en `.v25/correccion_cap09.txt`:

    $ grep -o "cap_[0-9]*" cuarentena/scott_radical_candor/entregar_evaluacion_formal_desempenio_nueve_consejos.json | sort | uniq -c
          2 cap_09
    $ (su resumen_teorico, impreso)
    UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_09.md, unidad Cap. 6, Guidance. Sale de las lineas 331 a 361, bajo el rotulo FORMAL PERFORMANCE REVIEWS.
    pasos_accionables: 22
    $ sed -n "1,7p" fuentes/scott_radical_candor/cap_11.md
    unidad: Cap. 8          titulo_textual: Results
    $ sed -n "1,7p" fuentes/scott_radical_candor/cap_09.md
    unidad: Cap. 6          titulo_textual: Guidance

**DOS SEDES TOCADAS, las dos tachadas y no borradas:** la tabla de `R.5.b` de la vuelta 24, y la
prosa de `Q.11.a` de la vuelta 23, que escribia *de `cap_11`* sobre el mismo candidato. **Los `22`
pasos si eran correctos** y quedan escritos como tales.

> **LO QUE ME TOCA ADMITIR, Y NO ES LA ETIQUETA:** la caida nacio en el `PROMPT_SIGUIENTE.md` del
> auditor y el la declara en su `3.4` y su `7.2`. **Pero mi propia regla la habria cazado**
> (`EXTRACTOR.md` 5: *una cifra de su encargo no es fuente de una cifra mia*), **y ese mismo dia la
> aplique al rotulo de `cap_14` y no a esta.** La diferencia entre las dos no fue el cuidado: **fue
> que en una remedi y en la otra copie.** Es la misma leccion que `D.41` tiene escrita para las
> tablas, en una celda que ninguna tabla de instrumento cubre.

### S.2.d. **LAS OCHO ARISTAS ADJUDICADAS, DECLARADAS EN MI SEDE, Y LA CONDICION COMPROBADA UNA A UNA**

*Las adjudica la `ACTA 24` `3.1`. **No las acepto de su palabra: abro el fichero de cada madre y
compruebo que el paso citado existe**, que es la condicion que `forja.py arista` impone por
construccion y la que tumbo las dos que el auditor retira.*

Salida de `python .v25/pasos_madres.py`, guardada en `.v25/pasos_madres.txt`. El paso citado de cada
madre va impreso de su fichero, no parafraseado:

| # | madre | `--paso` | hijo | el paso de la madre, impreso | libro | existe? |
|---:|---|---:|---|---|---|---|
| **72** | `fijar_cuatro_notas_calcular_nota_global` | **8** de 12 | `elegir_categorias_nota_palabras_propias_empresa` | *Cuenta con lo que cuatro notas por separado en cada una de **las categorias elegidas** permiten...* | `L109` | **SI** |
| **73** | `repartir_notas_publicar_reparto_esperado` | **3** de 9 | `calibrar_notas_reunion_jefes_pares` | *Cuenta con lo que el texto dice que es lo mas importante en general: **el proceso de calibracion**.* | `L145` y `L151` | **SI** |
| **74** | `presionar_curva_notas_evitar_forzarla` | **11** de 11 | `calibrar_notas_reunion_jefes_pares` | *...lo que el texto dice que hace importantes **las sesiones de calibracion**...* | `L169` | **SI** |
| **75** | `evaluar_desempenio_dos_veces_anio` | **6** de 11 | `montar_evaluacion_360_grados_ligera_pares` | *Haz la otra escrita, e incluye en ella **un componente ligero de trescientos sesenta grados**.* | `L191` | **SI** |
| **76** | `hacer_critica_pares_transparente_ensenar_escribirla` | **1** de 11 | `montar_evaluacion_360_grados_ligera_pares` | *...si haces **critica de trescientos sesenta grados**, tienes que decidir si sera transparente...* | `L207` | **SI** |
| **77** | `mantener_proceso_evaluacion_ligero_vigilar_crecimiento` | **6** de 13 | `montar_evaluacion_360_grados_ligera_pares` | *Monta la herramienta de evaluacion ligera **igual que la herramienta de trescientos sesenta grados**...* | `L231` | **SI**. # **es mi discutible 5** |
| **78** | `mantener_proceso_evaluacion_ligero_vigilar_crecimiento` | **5** de 13 | `hacer_critica_pares_transparente_ensenar_escribirla` | *...el proceso tardara menos ... si toda la critica de trescientos sesenta grados **es transparente**...* | `L231` | **SI** |
| **79** | `montar_evaluacion_360_grados_ligera_pares` | **6** de 10 | `elegir_categorias_nota_palabras_propias_empresa` | *...pide simplemente a los empleados que califiquen a sus pares en cada uno de **los cuatro criterios**.* | `L201` | **SI** |

    aristas con el paso de la madre EXISTENTE : 8 de 8
    aristas con LOS DOS extremos en el grafo  : 0 de 8

**LAS OCHO SON `D.29` Y NO `D.37`**, y la razon es la que el acta escribe: **no hay cuenta escrita,
hay una lectura que se argumenta.** Por eso cada una lleva delante **el paso impreso que nombra al
hijo**, y no la cita del libro sola.

**LA DEUDA SUBE DE `71` A `79`.** Y **ninguna se cablea por esta seccion**: los ocho extremos de
madre y los ocho de hijo viven **todos en la bandeja**, medido arriba y no supuesto. **El cableado es
la TAREA 3 y se mide DESPUES de insertar, no antes.**

**Y LAS DOS QUE EL AUDITOR RETIRA, escritas para que nadie las vuelva a buscar:** las que su apertura
leyo en `L157` de `presionar_curva_notas_evitar_forzarla` hacia `elegir_categorias` y hacia
`fijar_cuatro_notas`. **`L157` no llego a ser ninguno de los once pasos de esa madre**, y una
remision del libro que no llego a ser paso **no es una arista declarable**. La caida es suya y va
declarada en su `7.3`.

### S.2.e. **EL PUENTE DE FIDELIDAD DE `cap_14`, CORREGIDO, Y FIRMO `0,57` Y NO `0,00`**

**LA LINEA DEL LIBRO, ABIERTA POR MI CON `sed` Y PEGADA** (`D.35`), guardada en `.v25/puente_L97.txt`:

    $ sed -n "95,99p" fuentes/scott_radical_candor/cap_14.md
    3. Job ladders
    I hate job ladders, since bad ones tend to celebrate climbing the corporate ladder rather than
    doing work that is meaningful. ... So you need to describe what TEAMWORK means for an
    entry-level employee versus a manager, a director, a VP, and so on. Again, the language is
    important here. ...
    4. Number of ratings

| | |
|---|---|
| **lo que mi paso 2 decia** | *Describe que significa **cada categoria** en cada nivel, y el texto pone los niveles que hay que recorrer: empleado de entrada, jefe, director, vicepresidente, y asi hacia arriba.* |
| **lo que el libro escribe** | **UNA sola categoria: `teamwork`** |
| **por que es PUENTE y no lectura ancha** | **mandaba escribir CUATRO descripciones por nivel donde el libro escribe UNA palabra.** No es cosmetico: **multiplica el trabajo por cuatro sobre una linea que el libro no escribio**, que es la especie *completar el inventario* de `D.30` |
| **lo que dice ahora** | *Describe que significa en cada nivel **la categoria de la escalera**, y el texto **la ejemplifica con una sola, el trabajo en equipo**: empleado de entrada, jefe, director, vicepresidente, y asi hacia arriba.* |
| **la correccion declarada** | **dentro del propio fichero**, anexada a su `resumen_teorico`, con la linea 97 pegada y **con la cifra vieja dicha**: *la marca de 7 TRANSCRIPCION 0 PUENTE era mia y era falsa: eran 6 y 1* |

**Y LA ADUANA SE VOLVIO A CORRER SOBRE EL FICHERO TOCADO, EN EL MISMO ACTO** (`EXTRACTOR.md` 16).
Salida de `python forja.py informe cuarentena/scott_radical_candor/escribir_escaleras_puesto_evitar_dos_extremos.json`,
guardada en `.v25/aduana_puente.txt`:

    candidatos revisados        : 1
    poblacion del barrido       : 345   (214 del grafo mas 131 que esperan en bandejas)
    EL SALDO
      ENTRARIAN sin leer nada          : 1
      BLOQUEARIAN esperando veredicto  : 0   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

> ### **FIRMO `cap_14` EN `0,57` (1 DE 174) Y NO EN `0,00`, Y LA FIRMA ES MIA**
>
> **El puente lo encontro el auditor y la firma la pongo yo**, que es lo que su `8.3` pide: el
> numerador lo firma quien lo releyo. **Lo relei contra la linea 97 antes de aceptarlo**, y es puente:
> el libro pone una palabra donde mi paso ponia cuatro descripciones.
>
> **Y NO ENTRA EN LA METRICA DE CREDITO**, porque su `8.4` es explicita: **un puente encontrado y
> corregido es la regla funcionando**, no una caida. Lo que seria caida es uno que entrase al grafo
> sin corregir, **y este esta en la bandeja y sale corregido ANTES de que su lote se inserte.**
>
> **LO QUE ME LLEVO DE AQUI, Y VA EN MI PROPIA LETRA:** ese candidato declaraba en su
> `resumen_teorico` *NO ESCRIBO PERIODO NI DESTINATARIO* y *NO ESCRIBO NUMERO DE NIVELES*, o sea que
> **estaba mirando expresamente las tres especies de puente que `D.30` nombra por su nombre, y se le
> colo una CUARTA que esa tabla no lista: generalizar el ejemplo del libro.** **Un catalogo de
> especies enseña a mirar donde el catalogo mira.** Lo propongo como especie nueva en `S.8`, y no me
> lo adjudico yo.
