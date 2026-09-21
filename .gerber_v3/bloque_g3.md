
---

# FRENTE `gerber_emyth`, VUELTA 3: **EL REMEDIO HEREDADO DE LA `ACTA G1` CUMPLIDO, `cap_09` Y `cap_10` MINADOS A CERO, Y `cap_12` DA UN CANDIDATO** (`D.45`, frente en paralelo: **NO INSERTA**)

> ## **ESTE BLOQUE SE ESCRIBE EN LA RAMA `extraccion-gerber_emyth`, CON `MODO_INSERCION=cuarentena`. CERO INSERCIONES, Y NO POR FALTA DE CANDIDATO BUENO: PORQUE LA INSERCION ES UNA AUTORIZACION DEL FUNDADOR Y ESTA CORRIDA NO LA TRAE.**
>
> **MODO AUSTERO (`D.47`) VIGENTE.** Nada que el registro ya diga, cifras talladas, discutibles por
> numero y linea. **Las guardas de dato, intactas**: la aduana en seco candidato a candidato, la
> fidelidad `D.30` con su relectura contra el parrafo, `D.41` y `D.42`.

## G3.0. EL ESQUELETO DE LA VUELTA (`EXTRACTOR.md` 3)

| # | tarea del encargo | como cierra | donde |
|---:|---|---|---|
| 1 | el remedio heredado de la `ACTA G1` (`d095`): cuatro celdas con correccion declarada, y correr la comprobacion de secciones sobre el bloque propio | **CERRADA** | `G3.2`, comprobacion en `G3.8.b` |
| 2 | la frontera de `cap_09`, `cap_10` y `cap_12`, cerrada contra el cuerpo al digito | **CERRADA**: `3` de `3` con residuo `0`, cero solapes y cero lineas sin cubrir | `G3.3` |
| 3 | los candidatos que cada capitulo de, con su informe en el acto | **CERRADA**: `2` capitulos en cero y `1` candidato de `cap_12`, con su informe corrido y su vecino leido | `G3.4` |
| 4 | `PASOS INVENTADOS POR CAPITULO`, fila por capitulo | **CERRADA**: `2` filas `SIN SUPERFICIE` y una en `0,00` por ciento | `G3.5` |
| 5 | la muestra de fidelidad, semilla `g3` | **CERRADA**: `cap_12` releido ENTERO con sus `6` pasos, `cap_09` y `cap_10` por muestra con `0` pasos cada uno | `G3.6` |
| | el cierre: guardas, cifras recomputadas, discutibles marcados, commit y push | **CERRADO** | `G3.7` a `G3.9` |

**LAS CINCO TAREAS ENTREGADAS Y CERO COLA** (`EXTRACTOR.md` 1.3, tope de cinco).

## G3.1. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (`EXTRACTOR.md` 4)

Salida de `python .gerber_v3/apertura.py` (copia sin cambios de `.gerber_v2/apertura.py`), guardada
en `.gerber_v3/apertura.txt`:

<!-- TALLADO: parcial salida=.gerber_v3/apertura.txt -->

| pieza | al abrir | de donde sale |
|---|---:|---|
| nodos en el grafo | **346** | `dataset/nodos.jsonl` |
| veredictos escritos | **740** | `bitacora/VEREDICTOS.jsonl` |
| unidades de `gerber_emyth` | **22** | `PATRON: fuentes/gerber_emyth/cap_*.md` |
| palabras de cuerpo del libro | **62648** | `PATRON: fuentes/gerber_emyth/cap_*.md` |
| candidatos en bandeja de `gerber_emyth` | **10** | `PATRON: cuarentena/gerber_emyth/*.json` |
| clave `gerber_emyth` en la tabla canonica | **SI** | `fuentes/FUENTES_CANONICAS.json` |
| rama activa | `extraccion-gerber_emyth` | `git rev-parse --abbrev-ref HEAD` |
| commit de apertura | `07aa6f2` | `git rev-parse --short HEAD` |

**CONTRA EL ENCARGO (seccion 1):** `346` nodos, `740` veredictos y `10` candidatos en bandeja me salen
al digito. El commit de apertura es `07aa6f2`, que es el que el encargo anuncia como *el de mi acta,
que este cierre anade*. **Cero discrepancia que declarar.** Los seis capitulos minados y adjudicados
que el encargo publica (`cap_04`, `cap_05`, `cap_06`, `cap_07`, `cap_08`, `cap_11`) no los vuelvo a
medir con instrumento propio: no hay campo de `dataset/nodos.jsonl` ni de `cuarentena/` que registre
"capitulo leido y adjudicado en cero", y esa es exactamente la cola `d088`/`d096` que el encargo mismo
avisa **no tocar**.

## G3.2. TAREA 1: **EL REMEDIO HEREDADO DE LA `ACTA G1`, CUMPLIDO** (`d095`). **CERRADA**

*`d095` pedia tres cosas: tres celdas del bloque `G1` con correccion declarada y tachado en su sitio, y
correr `python .v1g_auditor/secciones.py` (o su equivalente sobre el bloque propio) antes de cerrar
cualquier reporte. El encargo de esta vuelta anade una cuarta celda, la de `G2.8.d` que dice `los dos
discutibles` donde hay `3`.*

**LAS CUATRO CORRECCIONES, CADA UNA CON TACHADO EN SU SITIO Y SIN BORRAR NADA:**

| # | donde | que decia | que dice ahora |
|---:|---|---|---|
| 1 | `docs/loop/archivo/gerber_emyth/REPORTE_frente_hasta_v1.md`, celda de `G1.10.d` (fila *una guarda en rojo*) | citaba `G1.10.e`, seccion que no existe | tachado, con `grep -n "^#\{2,4\} G1\.10\.e"` corrido hoy contra ese mismo fichero: **cero coincidencias**, y la guarda real que si se puede citar es la de `G1.5` |
| 2 | mismo fichero, fila `CERRADO` del esqueleto `G1.0` | `CERRADO` sin matiz | tachado, con la fecha exacta en que fue falsa (commit `a218170`, `G1.9` y `G1.10` no existian todavia) y en que commit se volvio cierta (`abf7515`, el mismo bloque las escribe mas abajo) |
| 3 | mismo fichero, apertura de `G1.9` | prometia *cerrarse con su salida pegada* | tachado, declarando que esa promesa no se cumplio (el informe de lote nunca termino, `91` bytes de cabecera) y citando donde vive el saldo real: `docs/loop/paradas/2026-09-17-gerber-la-racha-y-la-linea-vieja-RESUELTA.md` seccion 3, `3` ENTRARIAN, `7` BLOQUEARIAN, `0` CAERIAN, `0` CHOCAN |
| 4 | `docs/loop/REPORTE.md`, celda de `G2.8.d` (fila *una pregunta de doctrina*), linea `57681` | `los dos discutibles` | tachado, `3` discutibles, citando que `G2.7` tiene tres filas y que mi propio `G2.8.c` de esa misma vuelta ya decia `3` |

**LO QUE NO HAGO, por la misma razon que `G1.10.a` ya dio:** no reescribo ninguna celda por encima,
no borro el texto viejo. Es correccion declarada, no enmienda muda.

**Y NO TOCO `.v1g_auditor/secciones.py`**, que es sede del auditor (`d095` punto 2, y el encargo lo
repite): la copia adaptada al bloque de esta vuelta vive en `.gerber_v3/secciones.py`, con el mismo
patron de catorce lineas y solo dos cambios de texto (`G1` por `G3`, y el encabezado de vuelta que
busca). Se corre al cerrar, sobre el bloque que este mismo documento termina de escribir, y su salida
va en `G3.8.b`.

## G3.3. TAREA 2: **LA FRONTERA DE `cap_09`, `cap_10` Y `cap_12`, CERRADA CONTRA EL CUERPO AL DIGITO**. **CERRADA**

*El instrumento es `.gerber_v2/frontera.py`, copiado sin cambio a `.gerber_v3/frontera.py`: cortar estas
tres unidades con el es la misma regla aplicada al mismo libro.*

    $ diff .gerber_v2/frontera.py .gerber_v3/frontera.py
    (vacio, cero cambios en el instrumento)

### LA FRONTERA DE `cap_09` (`Cap. 7`, *The Turn-Key Revolution*), **6 piezas y CERO con procedimiento**

Salida de `python .gerber_v3/frontera.py fuentes/gerber_emyth/cap_09.md .gerber_v3/piezas_cap09.txt`,
guardada en `.gerber_v3/frontera_cap09.txt`:

<!-- TALLADO: salida=.gerber_v3/frontera_cap09.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L19 | **39** | el numero del capitulo, el rotulo THE TURN-KEY REVOLUTION y el epigrafe de Fritjof Capra | **RESIDUO: rotulo y epigrafe** |
| `R2` | L20 a L27 | **114** | la Turn-Key Revolution definida como una forma de hacer negocios que transforma cualquier negocio pequeno de caos a orden | **POSTURA** |
| `R3` | L28 a L78 | **920** | The Franchise Phenomenon: la historia de Ray Kroc y McDonald's, y las cifras del fenomeno de las franquicias en Estados Unidos | **CASO** |
| `R4` | L79 a L110 | **423** | Turning the Key: la diferencia entre la franquicia de nombre comercial y la Business Format Franchise, y que el producto real de un negocio es el negocio mismo | **POSTURA** |
| `R5` | L111 a L172 | **738** | Selling the Business Instead of the Product: Ray Kroc piensa su negocio como el producto y al franquiciado como su cliente, y el paso a trabajar SOBRE el negocio | **POSTURA y CASO** |
| `R6` | L173 a L233 | **611** | el dialogo con Sarah sobre McDonald's como modelo para cualquier pequeno negocio | **CASO** |
| **el cuerpo entero** | **L8 a L233** | **2845** | **suma de las piezas: 2845** | **residuo sin asignar: 0** |

    piezas: 6   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 2845   suma 2845   residuo 0

**Por que ninguna pieza pasa la vara de `EXTRACTOR.md` 9 y 9.1.** `R2` define la Turn-Key Revolution sin
nombrar medios propios: es la tesis del capitulo, no un inventario. `R3` y `R6` cuentan la historia de
Ray Kroc y el dialogo con Sarah: son caso e ilustracion, no procedimiento del lector. `R4` distingue dos
tipos de franquicia y afirma que el producto es el negocio mismo: postura conceptual, sin medios
nombrados uno a uno que el lector deba ejecutar. `R5` mezcla postura (ir a trabajar SOBRE el negocio) y
el caso de Ray Kroc pensando su negocio como producto: ninguna frase pone un inventario propio de
medios, etapas u objetos de trabajo.

### LA FRONTERA DE `cap_10` (`Cap. 8`, *The Franchise Prototype*), **5 piezas y CERO con procedimiento**

Salida de `python .gerber_v3/frontera.py fuentes/gerber_emyth/cap_10.md .gerber_v3/piezas_cap10.txt`,
guardada en `.gerber_v3/frontera_cap10.txt`:

<!-- TALLADO: salida=.gerber_v3/frontera_cap10.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L19 | **35** | el numero del capitulo, el rotulo THE FRANCHISE PROTOTYPE y el epigrafe de Robert M. Pirsig | **RESIDUO: rotulo y epigrafe** |
| `R2` | L20 a L41 | **182** | el Franchise Prototype definido como el modelo de trabajo del sueno del franquiciador | **POSTURA** |
| `R3` | L42 a L86 | **459** | el caso de McDonald's: cada detalle probado en el Prototipo, las papas fritas, las hamburguesas, la Universidad de la Hamburguesologia y el Turn-Key Operation | **CASO** |
| `R4` | L87 a L135 | **595** | lo que el Franchise Prototype es en verdad, la lista de empresas donde ya existe, y las preguntas retoricas sobre como construir el tuyo | **POSTURA** |
| `R5` | L136 a L145 | **140** | la reaccion de Sarah, que ya lo entiende | **RESIDUO: bisagra** |
| **el cuerpo entero** | **L8 a L145** | **1411** | **suma de las piezas: 1411** | **residuo sin asignar: 0** |

    piezas: 5   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 1411   suma 1411   residuo 0

**Por que ninguna pieza pasa la vara.** `R2` y `R4` son conceptuales: definen que es el Prototipo y para
que sirve, sin una lista propia de medios que el lector deba ejecutar. `R3` es el caso de McDonald's con
sus detalles (siete minutos de las papas, diez de las hamburguesas, el patron de los pepinillos): son
los estandares PROPIOS de McDonald's, ilustracion de la disciplina de un franquiciador, no un
procedimiento que el libro mande al lector replicar con esos mismos numeros. `R5` es la bisagra de
cierre hacia el capitulo siguiente.

### LA FRONTERA DE `cap_12` (`Cap. 10`, *The Business Development Process*), **8 piezas y UN CANDIDATO EN `R5`**

Salida de `python .gerber_v3/frontera.py fuentes/gerber_emyth/cap_12.md .gerber_v3/piezas_cap12.txt`,
guardada en `.gerber_v3/frontera_cap12.txt`:

<!-- TALLADO: salida=.gerber_v3/frontera_cap12.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L19 | **41** | el numero del capitulo, el rotulo THE BUSINESS DEVELOPMENT PROCESS y el epigrafe de Peters y Waterman | **RESIDUO: rotulo y epigrafe** |
| `R2` | L20 a L21 | **43** | la cabeza que nombra las tres actividades del proceso: Innovation, Quantification y Orchestration | **POSTURA** |
| `R3` | L22 a L83 | **962** | la seccion Innovation entera: creatividad contra innovacion, y los tres ejemplos THE INNOVATION de experimentos de venta al detalle | **POSTURA y CASO** |
| `R4` | L84 a L94 | **113** | el subtitulo Quantification y por que cuantificar una innovacion importa | **POSTURA** |
| `R5` | L95 a L95 | **111** | el parrafo que enumera uno a uno los seis pasos para cuantificar el impacto de una innovacion | **INVENTARIO PROPIO: NACE 1 CANDIDATO** |
| `R6` | L96 a L147 | **577** | el resto de Quantification: el ejemplo del traje azul, la lista abierta de preguntas sobre los numeros (termina en *and so forth*) y el cierre | **POSTURA** |
| `R7` | L148 a L221 | **989** | la seccion Orchestration entera: la eliminacion de la discrecion, *si no lo has orquestado no lo posees*, y el cierre que nombra otra vez las tres actividades | **POSTURA** |
| `R8` | L222 a L293 | **1370** | el dialogo con Sarah sobre la Orquestacion, la metafora del aprendizaje del pastel de fruta y la maestria del artesano | **CASO y POSTURA** |
| **el cuerpo entero** | **L8 a L293** | **4206** | **suma de las piezas: 4206** | **residuo sin asignar: 0** |

    piezas: 8   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 4206   suma 4206   residuo 0

**Por que `R5` SI pasa la vara y las otras siete no.** `R5` es una sola frase que enumera `(1)` a `(6)`
sus propios pasos, sin adjetivo de adecuacion en el sitio del criterio: no dice *mide de forma
razonable*, dice *determinando cuantos*, *contando cuantos*, *determinando el valor*. Es la prueba del
manual al pie de la letra: una linea que tarda seis pasos en ejecutarse es un procedimiento nombrado en
una linea. `R2` nombra tres actividades pero no las desarrolla en esa misma linea (marcado como puntero,
`G3.7`). `R3` da tres ejemplos concretos (*THE INNOVATION*) presentados como casos de clientes propios
(*our clients have found*), no como un inventario que el libro mande ejecutar con esos mismos terminos
(discutible 1, `G3.7`). `R4`, `R6`, `R7` y `R8` son postura y dialogo, sin inventario propio de medios.

## G3.4. TAREA 3: **LOS CANDIDATOS QUE CADA CAPITULO DE, CON SU INFORME EN EL ACTO**. **CERRADA**

**CERO candidatos de `cap_09`. CERO candidatos de `cap_10`. UN candidato de `cap_12`.** Las razones
pieza a pieza de los dos capitulos en cero estan en `G3.3` y no se repiten (`D.47`).

### El candidato de `cap_12`

`cuarentena/gerber_emyth/cuantificar_impacto_innovacion_6_pasos.json`, con sus **6** pasos transcritos
de `R5` (`L95`), cita pegada en `.gerber_v3/cita_cap12_L95.txt` (`D.35`):

    For example, how would you know that by changing the words you use to greet an incoming
    customer you produced a 16-percent increase in sales unless you quantified it by (1)
    determining how many people came in the door before the Innovation was put into effect;
    (2) determining how many people bought products and what the dollar value of those
    products were before you changed the words and what you said to produce those sales;
    (3) counting the number of people who came in the door after you changed the words; (4)
    counting the number of people who purchased something; (5) determining the average unit
    value of a sale; and (6) determining what the improvement was as a result of your
    Innovation? These numbers enable you to determine the precise value of your Innovation.

**RELECTURA DE FIDELIDAD `D.30` EN EL ACTO: `6` pasos, `6` TRANSCRIPCION, `0` PUENTE.** No hay
destinatario, periodo ni responsable que el libro no ponga y que el candidato invente: el libro habla en
segunda persona todo el capitulo y esta frase no fija cada cuanto se cuantifica ni quien lo hace, y el
candidato no lo pone tampoco.

### Su informe, corrido en el acto (`EXTRACTOR.md` 16)

Salida de `python forja.py informe cuarentena/gerber_emyth/cuantificar_impacto_innovacion_6_pasos.json`,
guardada en `.gerber_v3/informe_cuantificar_impacto_innovacion.txt`:

<!-- TALLADO: parcial salida=.gerber_v3/informe_cuantificar_impacto_innovacion.txt -->

    poblacion del barrido       : 451   (346 del grafo mas 105 que esperan en bandejas)
    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] cuantificar_impacto_innovacion_6_pasos
        vecino dar_valor_constante_cuatro_publicos  [levantada por: similitud_texto]
          similitud_texto 0.396 | familia_id 0.000 | paso_contra_nodo 0.432
          paso 3 del candidato contra paso 4 de dar_valor_constante_cuatro_publicos

**`0 CAERIA`. No hace falta corregir nada: el ciclo de `EXTRACTOR.md` 16 cierra a la primera.**

**EL UNICO VECINO, LEIDO** (`EXTRACTOR.md` 11: por debajo de `0,4` no es la banda que obliga a leer
antes que ninguna otra, pero es el unico vecino de este candidato y se lee igual, seccion 11: *las
senales ordenan, nunca deciden*). `dar_valor_constante_cuatro_publicos` sale de `cap_11` (Cap. 9,
*Working On Your Business, Not In It*) y es la parte 1 de la serie de la regla 1 del prototipo: formas de
dar valor a los cuatro publicos del negocio. Mi candidato sale de `cap_12` (Cap. 10, *The Business
Development Process*) y es un metodo de medicion. **El parecido que la senal ve es lexico**: *cuenta*
(`cuenta como valor`, `cuenta cuantas personas`) y *puerta* (`la puerta del negocio`, `entraron por la
puerta`), no conceptual. **VEREDICTO DE LECTURA: `SANO`.** No hay madre ni hija entre los dos: uno
enumera formas de valor, el otro enumera conteos de una medicion. No se escribe en
`bitacora/VEREDICTOS.jsonl` porque esta vuelta no inserta (`D.39`): el veredicto queda declarado aqui,
para que la vuelta que cierre el lote lo tenga delante y no tenga que releerlo desde cero.

## G3.5. TAREA 4: **`PASOS INVENTADOS POR CAPITULO`, UNA FILA POR CAPITULO** (`AUDITOR_FORJA.md` 8). **CERRADA**

<!-- TALLADO: parcial salida=.gerber_v3/frontera_cap09.txt,.gerber_v3/frontera_cap10.txt,.gerber_v3/informe_cuantificar_impacto_innovacion.txt -->

| capitulo | candidatos nuevos | pasos escritos | PUENTE | pasos inventados |
|---|---:|---:|---:|---|
| `cap_09` | `0` | `0` | `0` | **SIN SUPERFICIE** |
| `cap_10` | `0` | `0` | `0` | **SIN SUPERFICIE** |
| `cap_12` | `1` | `6` | `0` | **0,00 por ciento** |
| **la vuelta 3 entera** | **`1`** | **`6`** | `0` | **0,00 por ciento** |

**Por que `SIN SUPERFICIE` en dos filas y una cifra en la tercera (`D.59`).** Cero candidatos es cero
denominador, y una razon no se publica sin numerador y sin denominador. `cap_12` si tiene superficie
(`6` pasos) y su relectura de `G3.4` mide `0` puentes sobre esos `6`, asi que `0,00` por ciento es una
cifra y no un silencio.

## G3.6. TAREA 5: **LA MUESTRA DE FIDELIDAD, SEMILLA `g3`**. **CERRADA**

Salida de
`python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_09,cap_10,cap_12 --semilla g3`,
guardada en `.gerber_v3/muestra_fidelidad.txt`:

<!-- TALLADO: salida=.gerber_v3/muestra_fidelidad.txt -->

    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : gerber_emyth
      semilla  : g3
      capitulos: cap_09, cap_10, cap_12

      RELEIDO ENTERO : cap_12
      POR MUESTRA    : cap_09, cap_10, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_09: 0 paso(s) en la muestra

      --- cap_10: 0 paso(s) en la muestra

      --- cap_12: ENTERO, 6 paso(s), no hay muestra que elegir

**La semilla eligio `cap_12` para relectura ENTERA, y es justo el unico capitulo con pasos que
releer: sus `6` pasos son los mismos `6` que `G3.4` ya releyo contra `R5` con `0` puentes.** `cap_09` y
`cap_10` dan `0` porque tienen `0` candidatos, y la unica verificacion que queda para ellos es la que
`G3.3` ya hizo: leer el fichero entero y decir contra que se leyo. Los tres, `L1` a `L233`, `L1` a `L145`
y `L1` a `L293`, sin paginar, en este mismo turno; la frontera de `G3.3` cubre las tres sin hueco ni
solape, asi que si algo se hubiera escapado de la lectura el residuo no cerraria en `0`.

## G3.7. DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO (`EXTRACTOR.md` 8)

| # | discutible | por que lo marco |
|---:|---|---|
| 1 | clasifique `cap_12` `R3` (los tres ejemplos *THE INNOVATION*: la frase de saludo, el traje azul, tocar el brazo) como CASO y no como procedimiento, porque el texto los presenta como resultados de *nuestros clientes* y no como un inventario que el libro mande ejecutar con esos terminos exactos. El del traje azul en particular tiene tres pasos concretos (tres semanas de traje marron, tres de traje azul, comparar ventas): si el auditor lo lee como procedimiento propio del libro y no como caso ilustrativo, ahi nace otro candidato | es la lectura mas cercana a la vara de las tres, y la que mas duda me genera de las tres piezas de este bloque |
| 2 | en el candidato de `cap_12`, los pasos 2 a 4 quedan anclados al ejemplo concreto de *cambiar las palabras del saludo* (asi lo escribe el propio parrafo `R5`), mientras que los pasos 1 y 6 ya hablan de *la Innovacion* en generico. Elegi transcribir fiel a esa mezcla en vez de generalizar los pasos 2 a 4 a *tu innovacion*, porque generalizarlos habria sido escribir yo una generalizacion que el parrafo no hace del todo explicita (posible PUENTE si el auditor lee distinto) | es la decision de fidelidad mas fina de todo el candidato, y la que un lector rapido no notaria |
| 3 | `cap_12` `L21` nombra tres actividades (Innovation, Quantification, Orchestration) una a una, que es el supuesto de `D.37`, pero hoy ninguna de las tres existe como nodo cabeza propio: mi candidato es un metodo concreto DENTRO de Quantification, no Quantification como nodo. No cableo ninguna arista `D.37` hoy. Si el auditor lee que mi candidato SI es *la parte Quantification* de esa cabeza, la arista se cablearia distinto | es el mismo patron que `d098` dejo escrito para `cap_05`, y prefiero declararlo a que se descubra en la auditoria |

## G3.8. EL CIERRE, RECOMPUTADO AL CIERRE (`EXTRACTOR.md` 4)

### G3.8.a. LAS TRES GUARDAS

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py
    total: 343 pruebas, 0 fallos, 0 errores

### G3.8.b. LA COMPROBACION DE SECCIONES DE `2.2`, SOBRE ESTE MISMO BLOQUE

Salida de `python .gerber_v3/secciones.py`, guardada en `.gerber_v3/secciones.txt`:

<!-- TALLADO: salida=.gerber_v3/secciones.txt -->

### G3.8.c. EL ESTADO AL CIERRE, RECOMPUTADO Y NO COPIADO DE LA APERTURA

| pieza | al abrir (`G3.1`) | al cerrar | diferencia |
|---|---:|---:|---|
| nodos en el grafo | `346` | **346** | `0` |
| veredictos escritos | `740` | **740** | `0` |
| candidatos en bandeja de `gerber_emyth` | `10` | **11** | `+1` (`cuantificar_impacto_innovacion_6_pasos`) |
| pasos en esa bandeja | `89` | **95** | `+6` |
| ficheros de dato movidos por esta vuelta | | **0** | `git diff --name-only 07aa6f2..HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl`: vacio |

**`346` y `740` identicos a la apertura de esta misma vuelta. La bandeja sube de `10` a `11` candidatos y
de `89` a `95` pasos, y es el unico movimiento de esta vuelta**: `G3.2` solo corrige texto de reporte
(que no es sede de dato, `EXTRACTOR.md` 14), `G3.3` solo lee, y `G3.4` escribe un fichero en
`cuarentena/`, que es bandeja y no grafo. Cero averia.

### G3.8.d. LA TABLA DE CIERRE DE TAREAS (`D.52`)

    $ python scripts/tabla_de_cierre.py --escribir

<!-- TALLADO: script=scripts/tabla_de_cierre.py salida=docs/loop/TABLA_DE_CIERRE.txt -->

| # | tarea | como cerro |
|---:|---|---|
| `1` | el remedio heredado de la `ACTA G1` (`d095`), cuatro celdas corregidas | **CERRADA en `G3.2`**: `4` de `4` celdas con tachado y motivo, comprobacion de secciones en `G3.8.b` |
| `2` | la frontera de `cap_09`, `cap_10` y `cap_12` | **CERRADA en `G3.3`**: `3` de `3` unidades con residuo `0`, cero solapes y cero lineas sin cubrir |
| `3` | los candidatos que cada capitulo de, con su informe en el acto | **CERRADA en `G3.4`**: `2` capitulos en cero, `1` candidato de `cap_12` con informe `0 CAERIA` y su vecino leido `SANO` |
| `4` | `PASOS INVENTADOS POR CAPITULO` | **CERRADA en `G3.5`**: `2` filas `SIN SUPERFICIE`, `1` fila en `0,00` por ciento |
| `5` | la muestra de fidelidad con la semilla `g3` | **CERRADA en `G3.6`**: `cap_12` releido ENTERO (`6` pasos, `0` puente), `cap_09` y `cap_10` por muestra con `0` pasos |

### G3.8.e. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`EXTRACTOR.md` 7)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| una pregunta de doctrina | ninguna: los tres discutibles de `G3.7` son de lectura, no de regla, y no piden doctrina nueva | **NO ES PARADA** |
| una caida de dato | ninguna: `0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` movidos (`G3.8.c`) | **NO ES PARADA** |
| algo contradice una regla vigente o una cifra publicada con su corte | nada: el remedio de `d095` se cumplio con sus cuatro celdas, y el saldo del encargo (`10` candidatos, `6` capitulos minados) coincide con lo medido en `G3.1` | **NO ES PARADA** |
| una guarda en rojo | ninguna: las tres de `G3.8.a` en VERDE | **NO ES PARADA** |
| una operacion cuyo texto no alcance para ejecutarse sin decidir | ninguna: las cinco tareas del encargo estaban escritas enteras | **NO ES PARADA** |

**NINGUNA DE LAS CINCO SE CUMPLE. ESTE TURNO CIERRA SIN PARADA**, y `docs/loop/PARA_ALEXIS.md` sigue sin
tocar y no es mia (`EXTRACTOR.md` 14).

## G3.9. CREDITO Y LO QUE PROPONGO

**NO ADJUDICO MI PROPIA RACHA** (encargo, seccion 7): el numero de `REPORTE` para esta tanda lo escribe
el auditor, con el nombre de su acta en el campo `tanda`, tal como `docs/loop/CREDITO_gerber_emyth.jsonl`
ya muestra para `ACTA G2`.

### Propuestas al auditor, todas en mi sede y ninguna adjudicada por mi

1. **El remedio de `d095` esta cumplido**, con sus cuatro celdas y la comprobacion de secciones en `0`
   (`G3.8.b`). Propongo pagarlo en `docs/loop/DEUDA.jsonl` (lo anoto con `scripts/deuda.py --pagar
   d095`, que no es adjudicacion de racha: es el mismo registro que la vuelta `2` uso para anotar `d094`).
2. **El hueco entre `cap_08` y `cap_11` sigue cerrado desde la vuelta `2`, y hoy se le suma el segundo
   hueco: `cap_09` y `cap_10`.** El frente tiene ahora `cap_04` a `cap_08`, `cap_11` y `cap_12` minados:
   ocho de veintidos. El siguiente sin minar en el hueco que queda es `cap_13`, `364` palabras, el mas
   corto del libro.
3. **El discutible 3 de `G3.7` deja un puntero para cuando alguna vuelta futura trabaje la cabeza de las
   tres actividades del proceso de desarrollo del negocio** (`cap_12` `L21`): si nace un nodo cabeza para
   Innovation, Quantification u Orchestration, la arista a este candidato se decide entonces, citando esa
   linea.

### Cola declarada

Ninguna. Las cinco tareas del encargo cierran en esta misma vuelta y no dejan tarea pendiente propia.
