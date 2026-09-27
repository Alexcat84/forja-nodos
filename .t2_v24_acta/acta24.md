
---

# ACTA 24. VUELTA 24, lote 4 (`scott_radical_candor`), `cap_14` ENTERO Y **EL LOTE 4 CERRADO EN EXTRACCION**: mi corte ciego de `cap_14` y el suyo **coinciden pieza a pieza en las diecisiete**, la insercion estrena la sede de mis veredictos con `8` lineas limpias, **el libro escribe OCHO remisiones entre elementos que la vuelta no declaro y yo retiro DOS de las mias**, y **la palabra `cinco` de la tabla del freno lleva tres vueltas siendo `seis`, tambien en mi propia acta y en mi propia apertura sellada**

*Escrita el 13 sep 2026. Cubre la **vuelta 24** del bucle del extractor, la que el arnes numero
`VUELTA 2` en esta corrida. **La numeracion de campania es la del reporte y la de los commits**, y
es `24`.*

## 0. HUECO DE ACTA: **NO LO HAY**, y lo mido antes de nada (`1` punto 0)

    $ grep -n "^# ACTA" docs/loop/ACTA_AUDITOR.md | tail -1
      20853:# ACTA 23. VUELTA 23, lote 4 (scott_radical_candor), cap_12 y cap_13 ENTEROS ...
    $ git log --pretty="%h %ad %s" --date=format:"%Y-%m-%d %H:%M" -3
      f165417 2026-09-13 16:29 Apertura ciega de la vuelta 2, sellada antes de exponer el reporte
      4f0486e 2026-09-13 15:58 CIERRE DE LA VUELTA 24: el lote 4 CIERRA en extraccion ...
      76a0b30 2026-09-13 15:31 VUELTA 24: la deuda de aristas sube de 53 a 71 ...

**La `ACTA 23` cubre la vuelta 23 y la vuelta que audito es la 24.** La anterior a la actual esta
cubierta: **cero vueltas sin acta.** Audito una sola vuelta y lo digo con la cuenta delante.

### 0.1. LA HERENCIA `D.40`, Y DONDE ESTA DECLARADA

**Esta declarada en `docs/loop/APERTURA_CIEGA.md` seccion `0`, sellada por el arnes en
`9bce7552e47125873a63dabefaa68176dc20c22b`** (ultima linea de `docs/loop/SELLOS_APERTURA.jsonl`),
con `ACTA ANTERIOR LEIDA: 2c6884f6d76ffc7176fb370a9a3c913a8b767b83` **remedida por mi con
`git hash-object`** y coincidente al digito con la que el prompt me entrego, y con los **cuatro**
heredados declarados uno a uno: **tres `CUMPLIDO`, y el tercero desglosado en sus cinco puntos, de
los cuales tres `CUMPLIDO`, uno `ROTO` por mi y uno `NO APLICA` con su motivo mecanico escrito.**

> **Y LOS DOS QUE QUEDABAN COLGANDO SE PAGAN AQUI, EN ESTA MISMA ACTA, que es lo que el
> `HEREDADO 3` punto 4 exige de todo `NO APLICA`:**
>
> | lo que quedo colgando en la fase ciega | donde se paga hoy |
> |---|---|
> | el `NO APLICA` del punto 5: la muestra pineada no se podia sortear sin saber cual era la tanda | **seccion `4`**, con la poblacion de `8` releida entera y su banda publicada |
> | el saldo de aduana de los `15`, que quedo en un fichero de **cero bytes** y **no se cito** | **seccion `1.7`**, corrido hoy entero y pegado |

**NO HE TOCADO `APERTURA_CIEGA.md` DESPUES DEL SELLO.** El arnes lo verifica al cerrar mi turno.

---

## 1. LO QUE VERIFIQUE CON MIS PROPIOS COMANDOS, Y NO ACEPTE DE SU REPORTE

*`1` punto 1: nada se acepta sin verificarse. **El instrumento manda**, y toda cifra de esta acta
sale de una corrida de HOY con su salida al lado.*

### 1.1. LAS CUATRO GUARDAS, CORRIDAS POR MI EN MI TURNO NORMAL

    $ python forja.py gate
      GATE VERDE.
        nodos verificados: 214
        guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
                 vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
                 arista_incompleta, guiones
    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py
      Ran 111 tests in 12.447s
      OK
      total: 111 pruebas, 0 fallos, 0 errores
    $ python forja.py resolutor
      nodos vivos: 214
      nodos deprecados (archivo): 0
      alias registrados: 0

**LAS CUATRO EN VERDE, Y LA TERCERA IMPORTA HOY MAS QUE LAS OTRAS TRES JUNTAS.** En mi fase ciega
`tests/test_aceptacion.py` daba **`1` fallo**, y lo declare entero en `APERTURA_CIEGA.md` seccion
`8`: `scripts/tallar_reporte.py` abre `docs/loop/REPORTE.md` sin guarda de existencia (su linea
315, con `os.path.exists` puesto en las otras dos rutas de la misma funcion), y `D.34.2` retira ese
fichero durante mi fase ciega.

> ### **`D.41` CONTRA `D.34.2`: LO QUE MI PROPIA APERTURA MIDIO, CONFIRMADO Y ACOTADO HOY**
>
> **Con el reporte de vuelta en el arbol, la prueba pasa.** El choque **no es de dato ni de cifra**:
> es **de ventana**. Muerde **solo** en la fase ciega, que es la unica en que el fichero no esta, y
> lo que tumba es el `pre-commit` del commit que sella mi apertura.
>
> | | |
> |---|---|
> | **es condicion de parada por fallo tecnico repetido?** | **NO.** `3` pide *hook, gate o prueba en rojo **dos vueltas seguidas** por la misma causa*. **Esta es la PRIMERA vez que se mide**, y la mido yo |
> | **de quien es** | **de nadie del bucle.** Son dos reglas del fundador vigentes chocando |
> | **que hago con ella** | **la declaro y no la arreglo.** La moratoria de maquinaria (`5.6`, cosecha `7.F`) me prohibe encargar arneses, y la especie `ARNES` esta reservada al fundador por el guion de reanudacion |
>
> **QUEDA ESCRITO PARA LA VUELTA 25: si vuelve a salir en rojo por esta misma causa, es la segunda
> de dos y entonces SI es parada.** Lo digo hoy para que nadie tenga que descubrirlo entonces.

### 1.2. MI PROPIO CONTEO DEL DATASET, DE LA BITACORA Y DE LAS BANDEJAS

    $ wc -l dataset/nodos.jsonl              ->  214
    $ wc -l bitacora/VEREDICTOS.jsonl        ->  156
    $ wc -l config/pares_mutuos.jsonl        ->    1   (solo la cabecera: la sede sigue vacia)
    $ ls cuarentena/scott_radical_candor/*.json | wc -l              ->  131
    $ ls cuarentena/_insertados/scott_radical_candor/*.json | wc -l  ->   11

| lo que el reporte afirma al cerrar (`R.12.a`) | lo que mido yo | |
|---|---|---|
| nodos en el grafo **214** | **214** | **CUADRA** |
| veredictos en bitacora **156** | **156** | **CUADRA** |
| candidatos del lote 4 en cuarentena **131** | **131** | **CUADRA** |
| candidatos del lote 4 en `_insertados` **11** | **11** | **CUADRA** |
| unidades del lote 4 sin minar **0** | **0**, con mi propio `cobertura_lote4_auditor_v24.py` de la fase ciega | **CUADRA** |

### 1.3. EL TALLADO `D.41`, CORRIDO POR MI, **Y LA UNICA CIFRA SUYA QUE NO ME SALE IGUAL**

    $ python scripts/tallar_reporte.py
      tablas que declaran instrumento : 41
        talladas, celda a celda       : 37
        que DIFIEREN de su instrumento: 0
        sin poder comprobar           : 0
        que CITAN y no reproducen     : 4   (declaradas PARCIAL)
      TALLADO VERDE

**Su `R.12.b` escribe `36 tablas comprobadas`. A mi me salen `37`.** Y **no lo llamo caida, y digo
por que con la mecanica delante**: la celda que lo dice **esta dentro del tramo de cierre**, y ese
tramo aniade tablas despues de que el tallador corra. **Una cifra de cierre no puede contarse a si
misma**, y la diferencia es exactamente de uno.

> **LO QUE SI ENCARGO, Y ES DE ESCRITURA Y NO DE MAQUINARIA:** que la celda del tallado del cierre
> **diga contra que version del fichero se corrio**. Una cifra que se queda vieja en el acto de
> escribirse no es falsa, **pero se lee como si fuera de la version publicada**, y esa es la misma
> familia de las dos correcciones declaradas de la vuelta 23.

### 1.4. LA FRONTERA DE `cap_14`, **CORTADA POR MI A CIEGAS Y COMPARADA DESPUES**

*Es la comprobacion mas cara de esta acta y la unica que no se puede fingir: **corte el capitulo
antes de ver el suyo**, con mi propio instrumento, y publique mis diecisiete piezas en
`APERTURA_CIEGA.md` `2.2`, selladas.*

| | mi corte ciego | el suyo (`R.5.c`) | |
|---|---|---|---|
| piezas | **17** (15 con nodo, 2 residuos) | **17** (15 con nodo, 2 residuos) | **CUADRA** |
| suma de palabras de las piezas | **7638** | **7638** | **CUADRA** |
| cuerpo, `sed -n "8,$p" ... \| wc -w` | **7638** | **7638** | **CUADRA** |
| residuo sin asignar | **0** | **0** | **CUADRA** |
| lineas solapadas | **0** | no lo publica | medida mia |
| las 15 piezas de nodo, borde a borde | `21-33, 35-63, 65-71, 73-93, 95-97, 99-115, 117-123, 125-141, 143-151, 153-169, 171-185, 187-195, 197-203, 205-219, 221-239` | **identicas las quince** | **CUADRAN LAS QUINCE** |

**LA UNICA DIFERENCIA ENTRE LOS DOS CORTES ES UNA LINEA EN BLANCO.** Yo abro el residuo B en `L240`
y el en `L241`; `L240` no tiene texto y **las palabras son `59` en los dos**. **No es una
discrepancia: es donde cada uno pone el borde de una linea sin texto**, y lo digo para no vender
como coincidencia perfecta algo que al digito de la linea no lo es.

> ### **ESTO ES LO MEJOR QUE TRAE LA VUELTA, Y NO ES UNA CIFRA SUYA: ES LA COINCIDENCIA**
>
> **Dos lectores que no se vieron cortaron el mismo capitulo de 7.638 palabras en las mismas quince
> piezas, con los mismos bordes.** Y los tres tramos que yo marque como candidatos a pieza
> dieciseis (`Rewards` en `L139`, cortar las notas por nivel en `L179`, la herramienta ligera en
> `L231`) **estan dentro de su nodo con procedimiento propio**, comprobados uno a uno antes de ver
> su frontera. **La frontera de `15` se sostiene entera, y el discutible 4 se contesta con ella.**

### 1.5. LA DEUDA DE ARISTAS: **LAS `36` QUE SE PUEDEN CONTAR, CONTADAS POR MI**

    $ python .t2_v24_acta/deuda_auditor.py
      nodos en el grafo: 214 | extremos previos: 79 siguientes: 79
      aristas 36..71 leidas: 36
      con LOS DOS extremos ya en el grafo: 0   []
      con UN solo extremo en el grafo: 2
      con NINGUN extremo en el grafo: 34
      rango 36..71 presentes: [36, 37, ... 71]   faltan en 36..71: []

| lo que afirma | lo que mido | |
|---|---|---|
| deuda **71** = 36 contadas hoy mas 35 citadas | **36 filas numeradas de la 36 a la 71, sin hueco y sin repetida** | **CUADRA en las 36.** Las `35` primeras las **CITO**, igual que el, y **no las remido**: viven en formatos viejos sin numeracion corrida |
| **cero cableadas**, porque ninguna tiene sus dos extremos dentro | **`0` de las `36` tienen los dos extremos en el grafo** | **SOSTENIDA, y con instrumento y no con su palabra** |
| `79` aristas vivas en el grafo | **`79`**, y `79 + 79 = 158` extremos: **escritas por los dos lados** | **CUADRA** |

> **ESTO CONTESTA EL PUNTO 4 QUE MI PROPIA APERTURA DEJO ESCRITO** (`10.3`): *cuantas de la deuda
> tenian los DOS extremos dentro de los 11 insertados y aun asi no se cablearon.* **La respuesta es
> CERO**, y por eso el `cero cableadas` de `R.6.g` **no es negligencia: es imposibilidad medida.**
> Lo pregunte esperando encontrar una caida y encontre una razon, y lo escribo asi.

### 1.6. LAS SEDES QUE SUS COMMITS TOCARON, MEDIDAS Y NO SUPUESTAS

    $ git diff --name-only 74134e0..4f0486e | (agrupado por carpeta)
      78 .v24/           18 .insercion_v24/   17 .aduana_v24/
      15 cuarentena/scott_radical_candor/     11 cuarentena/_insertados/scott_radical_candor/
       2 censos/          1 docs/loop/         1 dataset/        1 bitacora/

**FUERA de `cuarentena/`, `dataset/`, `bitacora/`, `censos/` y `docs/loop/`, la vuelta no toco
NINGUNA sede.** Cero en `config/`, cero en `esquema/`, cero en `src/`, cero en `fuentes/`, y de
`docs/` **solo su propio reporte**. Las dos lineas nuevas de `censos/` **las escribe la aduana al
insertar** y no la mano: son registro, no cifra publicada.

### 1.7. EL SALDO DE ADUANA DE LOS `15`, **CORRIDO HOY POR MI, QUE ES LA DEUDA QUE MI APERTURA DEJO ABIERTA**

*`APERTURA_CIEGA.md` `10.1`: lo lance en la fase ciega, no termino, dejo el fichero en **cero
bytes** y **no lo cite**. Aqui esta corrido entero.*

    $ python forja.py informe <los 15 de cap_14>
      guardado en .t2_v24_acta/informe_15.txt   (13.733 bytes, y NO cero)

      candidatos revisados        : 15
      poblacion del barrido       : 345   (214 del grafo mas 131 que esperan en bandejas)
      umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

      EL SALDO
        ENTRARIAN sin leer nada          : 2
        BLOQUEARIAN esperando veredicto  : 13   (no es rechazo: es cola de lectura)
        CAERIAN por una guarda           : 0
        CHOCAN entre si dentro del lote  : 0

      LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
        vecinos levantados en total      : 43
        por candidato bloqueado          : menor 1, mediana 3, mayor 7
        que senial levanta cada vecindad : familia_id 2, paso_contra_nodo 3, similitud_texto 38

**LAS DOS CIFRAS QUE VALEN AQUI, Y NINGUNA DE LAS DOS ES UN SALDO:**

| | |
|---|---|
| # **`CAERIAN` : `0`** | **los quince pasan la puerta hoy**, incluido el id que la regla 3 tumbo en su vuelta y que el corrigio a `presionar_curva_notas_evitar_forzarla`. **Su correccion de puerta esta buena, y lo compruebo con la puerta y no con su palabra** |
| # **`CHOCAN entre si dentro del lote` : `0`** | **los quince candidatos de `cap_14` no chocan entre ELLOS.** Es la comprobacion que su tanda no pudo hacerse, porque corrio los informes de uno en uno: **un informe de uno solo nunca ve a sus hermanos.** **La frontera de `15` no produce un duplicado consigo misma**, y esa es una prueba que mi corte ciego no podia dar |

**Y LA TERCERA, QUE CONFIRMA LO QUE EL MIDIO Y YO NO ME CREIA DEL TODO:** el levanto **`27`** filas
vecino corriendo los quince **uno a uno**; yo levanto **`43`** corriendolos **juntos y hoy**. **Es
la misma cola, medida en dos momentos, y crece.** Su `R.6.e` lo escribio con un candidato
(`1` vecino contra 205 nodos, `3` contra 214) **y aqui se ve sobre los quince a la vez.** **Lo que
dijo esta bien dicho.**

> **LO QUE ESTA CORRIDA NO PUEDE HACER, Y LO DIGO ANTES DE COMPARAR NADA:** **no reproduce su tabla
> `R.5.d` y no puede.** El midio cada candidato **en el acto de escribirlo**, con la poblacion
> recorriendo de `330` a `345`; yo mido hoy, con los `11` insertados ya movidos de la bandeja al
> grafo. **La poblacion total coincide** porque `D.38.5` cuenta las dos, **pero el reparto entre
> grafo y bandeja no**, y la senial 3 no es simetrica (`D.36`). **Comparar celda a celda seria
> comparar dos medidas distintas y llamarlo discrepancia.**

---

## 2. LA RELECTURA CIEGA, EMPEZANDO POR LOS DISCUTIBLES MARCADOS (`5.1`)

*`1` punto 2. **Los ocho discutibles los marco el ANTES de saber si acertaba**, y en seis escribio
el argumento contra su propia decision. Esa es la diferencia que hace informativa a la metrica.*

### 2.0. **LA CONTAMINACION DE MI FASE CIEGA, REPETIDA AQUI ANTES DE USAR NINGUN RESULTADO**

**En la fase ciega rompi el punto 1 de mi propia tarea bloqueante** y me lleve por delante los
primeros noventa caracteres de la razon de los `8` veredictos de la bitacora antes de imprimir un
solo paso (`APERTURA_CIEGA.md` `9.1`, caida 1). **Va declarado en la seccion `4`, pegado a cada
uno de los ocho**, y mi racha lo paga en la `8`. **Una relectura contaminada y declarada vale algo;
una contaminada y callada, nada.**

**Los ocho discutibles de `R.11` NO estan contaminados**: viven en el reporte, que `D.34.2` me
retiro entero hasta que el arnes me lo expuso, y mi clase de los quince candidatos estaba escrita y
sellada antes.

### 2.1. LOS OCHO DISCUTIBLES, UNO A UNO

| # | lo que decidio | mi lectura, con la vara `6.1` | |
|---:|---|---|---|
| **1** | las cuatro aristas de `cap_09` son `D.29` y no `D.37` | **la cuenta no esta escrita en `cap_09`**: su `grep -c` da `0` y yo lo repito hoy. Sin cuenta no hay `D.37` (`D.37`, *Lo que NO autoriza*). **Y va con el 3, que adjudico junto en `3.2`** | **SOSTENIDO** |
| **2** | la arista 50 apunta a `criticar_trabajo_evitar_desanimo` y no a `dar_critica_inmediata_ayuda_tangible` | **lei los pasos de los dos, impresos ANTES**, y la decision la sostiene el texto y no su regla de desempate: ver `2.2` | **SOSTENIDO**, con una salvedad escrita |
| **3** | las trece aristas de `cap_14` son `D.37` | **la cuenta SI esta escrita**: el libro numera sus rotulos y el ultimo numeral, impreso por mi de `L221`, es `13. Lightweight or heavyweight`. Ver `3.2` | **SOSTENIDO** |
| **4** | `L9` a `L19` es POSTURA y no da nodo | **mi corte ciego lo marco `RESIDUO A` sin ver el suyo** (`1.4`). Dos lecturas independientes coinciden, y la restriccion 1 de `EXTRACTOR.md` 9.1 (fines y no medios) la sostiene | **SOSTENIDO** |
| **5** | no declara arista entre el elemento 13 y el 11, pese a la remision escrita de `L231` | # **NO LO SOSTENGO.** Mi apertura leyo esa arista a ciegas y hoy la adjudico: ver `3.1` | **DISCREPO, y adjudico** |
| **6** | el gemelo contra `entregar_evaluacion_formal_desempenio_nueve_consejos` es `SANO` | **lei sus 22 pasos contra los 10 del candidato en la fase ciega** (`APERTURA_CIEGA.md` `5.1`) y llegue a `SANO` por el mismo sitio: procedimiento propio en los dos lados, y el sujeto distinto | **SOSTENIDO**, y con su unidad corregida en `3.4` |
| **7** | la tanda de insercion deja en cola al bloqueado y sigue, en vez de pararse | **se sostiene por el criterio que `D.36` escribe** y no por comodidad: ver `3.3` | **SOSTENIDO**, con la tension declarada |
| **8** | el elemento 1 es nodo (`decidir_poner_nota_comunicar_proposito_limites`) | **mi clasificacion ciega lo puso NODO PROPIO** por `L71`, que da tres actos de comunicacion. Coincidimos sin vernos | **SOSTENIDO** |

**SIETE DE OCHO SOSTENIDOS. LA UNICA CAIDA DENTRO DEL MARCADO ES EL `5`, Y NO ES DE CLASE: ES UNA
ARISTA QUE FALTA.** `D.29` lo dice con sus palabras: **hay un hueco de declaracion, no una
contradiccion.**

### 2.2. **EL PAR DIRIGIDO QUE NINGUNA SENIAL LEVANTO Y QUE YO LEI POR MI CUENTA**

*Los dos procedimientos de critica de `cap_05` entraron los dos al grafo en esta vuelta y **la
aduana no los emparejo nunca**. Si son gemelos, la vuelta metio un duplicado y nadie lo vio. Los
imprimi enteros antes de escribir una sola palabra de clase.*

    $ python .t2_v24_acta/imprimir_pasos_corto.py 260 criticar_trabajo_evitar_desanimo dar_critica_inmediata_ayuda_tangible
      criticar_trabajo_evitar_desanimo      [grafo]  14 pasos
      dar_critica_inmediata_ayuda_tangible  [grafo]  10 pasos

| | |
|---|---|
| **que queda fuera del solape en el primero** | el error de atribucion fundamental, averiguar por que el otro hace lo que hace, la humildad del recien llegado, elogia en publico y critica en privado, contar historias de cuando te criticaron, y el caso de las dos carpetas |
| **que queda fuera del solape en el segundo** | no dejar que el buen resultado tape lo que hay que arreglar, la escalera de firmeza cuando no te oyen, preguntar si era consciente, la ayuda tangible pagada por la empresa, y cerrar con que tiene arreglo |
| **lo que si comparten** | *no personalices* y *hazlo en el acto*. **Dos lineas de catorce y de diez** |
| **la vara `6.1`, sin bascula** | **lo que queda fuera es procedimiento en los DOS lados.** No es solape grande ni pequenio: es que los dos lados ejecutan |
| **mi clase** | # **SANO. No son gemelos, y son FRONTERA DECLARADA** (`6.1`): dos procedimientos legitimos de la misma etapa |

> **Y ESO CONTESTA EL DISCUTIBLE 2 MEJOR QUE SU REGLA DE DESEMPATE.** El eligio
> `criticar_trabajo_evitar_desanimo` para la arista 50 **por la amplitud de la condicion de
> activacion**, que es un criterio que **el escribio esta vuelta y no esta en ningun sitio del
> banco**. **Yo lo sostengo leyendo los pasos** (`6.2`: una discrepancia nunca se adjudica citando
> una senial ni un criterio nuevo, se adjudica leyendo): el paso de la madre dice *Tres, da
> critica*, y el hijo que despliega la etapa entera es el que trae la doctrina general.
>
> **LO QUE NO RATIFICO, Y LO DIGO PORQUE ES LO QUE SE VA A CITAR MANIANA: su regla de desempate NO
> queda adjudicada como doctrina.** Adjudico **la eleccion concreta**, no la regla. **Y nada en el
> banco prohibe que una etapa tenga dos hijos**: que `dar_critica_inmediata_ayuda_tangible` no sea
> el elegido **no cierra** que pueda colgar tambien de ese paso. Eso se decide el dia del cableado,
> con los dos extremos vivos, y no hoy.

---

## 3. LO QUE ADJUDICO, Y ES DONDE ESTA EL TRABAJO DE ESTA ACTA

### 3.1. **EL LIBRO ESCRIBE OCHO REMISIONES ENTRE LOS ELEMENTOS QUE LA VUELTA NO DECLARO, Y RETIRO DOS DE LAS DIEZ QUE YO LEI A CIEGAS**

*Mi apertura sellada leyo **once** aristas fuera de la serie y firmo que la cifra buena era la que
cuadrase o la discrepancia declarada, **no aquella** (`APERTURA_CIEGA.md` `5.5`). La vuelta declaro
**una** de esas once, la `71`. Aqui adjudico las diez restantes, **una a una y contra el fichero**.*

**LA CONDICION QUE LAS DECIDE NO ES LA LINEA DEL LIBRO: ES EL PASO DE LA MADRE.** `D.37` y
`D.29` mandan citar `--paso <n>` de la madre, y `forja.py arista` **rechaza por construccion un
paso que la madre no tiene**. Asi que una remision del libro que **no llego a ser paso** no es una
arista declarable: es una linea que el nodo no recogio.

    $ python .t2_v24_acta/imprimir_pasos_corto.py 200 <las seis madres>
      guardado en .t2_v24_acta/pasos_madres.txt y pasos_madres2.txt

| # | madre | `--paso` | hijo | el paso de la madre que lo nombra | |
|---:|---|---:|---|---|---|
| **a** | `fijar_cuatro_notas_calcular_nota_global` | **8** | `elegir_categorias_nota_palabras_propias_empresa` | *cuatro notas por separado en cada una de **las categorias elegidas*** (`L109`) | **DECLARABLE** |
| **b** | `repartir_notas_publicar_reparto_esperado` | **3** | `calibrar_notas_reunion_jefes_pares` | *lo mas importante en general: **el proceso de calibracion*** (`L145`) | **DECLARABLE** |
| **c** | `presionar_curva_notas_evitar_forzarla` | **11** | `calibrar_notas_reunion_jefes_pares` | *lo que hace importantes **las sesiones de calibracion*** (`L169`) | **DECLARABLE** |
| **d** | `evaluar_desempenio_dos_veces_anio` | **6** | `montar_evaluacion_360_grados_ligera_pares` | *Haz la otra escrita, e incluye en ella **un componente ligero de trescientos sesenta grados*** (`L191`) | **DECLARABLE** |
| **e** | `hacer_critica_pares_transparente_ensenar_escribirla` | **1** | `montar_evaluacion_360_grados_ligera_pares` | *si haces **critica de trescientos sesenta grados**, tienes que decidir si sera transparente* (`L207`) | **DECLARABLE** |
| **f** | `mantener_proceso_evaluacion_ligero_vigilar_crecimiento` | **6** | `montar_evaluacion_360_grados_ligera_pares` | *Monta la herramienta de evaluacion ligera **igual que la herramienta de trescientos sesenta grados*** (`L231`) | **DECLARABLE. Es el discutible 5** |
| **g** | `mantener_proceso_evaluacion_ligero_vigilar_crecimiento` | **5** | `hacer_critica_pares_transparente_ensenar_escribirla` | *el proceso tardara menos ... si toda la critica de trescientos sesenta grados **es transparente*** (`L231`) | **DECLARABLE** |
| **h** | `montar_evaluacion_360_grados_ligera_pares` | **6** | `elegir_categorias_nota_palabras_propias_empresa` | *pide ... que califiquen a sus pares en cada uno de **los cuatro criterios*** (`L201`) | **DECLARABLE** |
| ~~i~~ | ~~`presionar_curva_notas_evitar_forzarla`~~ | ~~?~~ | ~~`elegir_categorias_nota_...`~~ | **`L157` dice *having the categories ... and calculating the overall rating as I outlined above*, y ESA LINEA NO ES NINGUNO DE SUS ONCE PASOS** | # **LA RETIRO YO** |
| ~~j~~ | ~~`presionar_curva_notas_evitar_forzarla`~~ | ~~?~~ | ~~`fijar_cuatro_notas_...`~~ | **la misma `L157`, el mismo motivo** | # **LA RETIRO YO** |

> ### **LA REGLA QUE LAS SOSTIENE, CITADA Y NO INVENTADA: `D.29`**
>
> **`D.29` no habla de cabezas de serie: habla de *la arista que la senial no levanta*, y su
> ejemplar fundacional es una dependencia de proceso** entre dos nodos que no son cabeza ni parte de
> ninguna serie. **Las ocho son exactamente eso**, y cada una lleva escrito el paso de la madre que
> nombra al hijo. **No hay doctrina nueva aqui: hay una regla del 10 sep 2026 aplicada a su propio
> caso.**
>
> **SU MOTIVO PARA NO DECLARAR EL DISCUTIBLE 5 NO SE SOSTIENE, Y ES LO UNICO QUE LE CORRIJO DE
> DOCTRINA.** Escribio *una arista lateral sin madre ni hija no esta autorizada* citando
> `EXTRACTOR.md` 15.6. **Lo que 15.6 prohibe es otra cosa**, y esta impreso: *declarar una arista
> porque dos nodos compartan familia o tema*. **Aqui no comparten tema: hay una linea del libro que
> nombra al otro con sus palabras**, y el propio nodo la recogio como paso. **Y la palabra
> `lateral` no existe en `BANCO_DE_REGLAS.md`, ni en `EXTRACTOR.md`, ni en el manual**: lo comprobe
> con `grep -i` en los tres. **El esquema solo tiene `nodos_previos` y `nodos_siguientes`, que su
> propia descripcion llama *Secuencia dirigida***: toda arista de esta casa es madre a hijo, y la
> direccion la pone el paso que nombra.
>
> **Y LA DIRECCION NO LA DECIDE EL ORDEN DEL LIBRO, que es lo que podria hacer dudar aqui:** el
> ejemplar de `D.29` tiene la **MADRE en el parrafo 31 y el HIJO en el 30**. **La madre puede ir
> despues.** Por eso `L157`, que mira hacia atras, no era el problema: el problema de la `i` y la
> `j` **es que no hay paso**, y eso si es condicion escrita.

> ### **LO QUE ME CUESTA ADMITIR, Y LO ADMITO PRIMERO: DOS DE MIS ONCE ERAN AIRE**
>
> **Yo lei las once del LIBRO y no de los PASOS.** Dos de ellas no sobreviven al fichero, y **la
> unica razon de que no acabaran publicadas como cifra mia es que mi apertura escribio expresamente
> que aquel `24` no era la cifra que iba a firmar.** **Eso no me absuelve del metodo**: leer
> remisiones en el libro y llamarlas aristas **es exactamente la caida que `D.35` y `D.41` vienen
> repitiendo con otros nombres**. Va a mis remedios de la `11`.

**LA DEUDA, CON ESTA ADJUDICACION DELANTE:** hoy son **`71`**. **Con las ocho declaradas seran
`79`.** No las cuento como deuda todavia **porque no estan declaradas en sede**, y una arista que
solo vive en un acta es lo mismo que una que solo vive en un reporte.

### 3.2. **LOS DISCUTIBLES 1 Y 3 SE ADJUDICAN JUNTOS, PORQUE SI UNO CAE CAEN LOS DOS**

*El lo dijo mejor que yo en su propio discutible 3: **si esto cae, cae con el 1 en la direccion
contraria, y las dos juntas dirian que mi vara se mueve segun me conviene.** Asi que los leo con la
misma vara y en el mismo acto.*

    $ sed -n "35,63p" fuentes/scott_radical_candor/cap_14.md
      ELEMENTS OF A FORMAL PERFORMANCE REVIEW PROCESS
      ... (los trece nombrados uno por linea, SIN numerar)
    $ for n in 65 73 95 99 117 125 143 153 171 187 197 205 221; do sed -n "${n}p" ...
      L65: 1. Rating or no rating        ...        L205: 12. Transparent or confidential
      L221: 13. Lightweight or heavyweight
    $ grep -c "the four\|four tips\|four elements" fuentes/scott_radical_candor/cap_09.md
      0

| | `cap_14` (discutible 3) | `cap_09` (discutible 1) |
|---|---|---|
| **la cuenta, escrita** | **SI. `L221` imprime `13.`**, que es el ultimo numeral de una enumeracion completa: **el numero trece esta en la pagina, no en la cabeza de nadie** | **NO.** Su `grep -c` da `0`, repetido por mi hoy |
| **las partes, nombradas** | SI, `L39` a `L63` | SI, pero en `L237`, **que es otra unidad** |
| **especie** | **`D.37`** | **`D.29` con razon escrita** |
| | **SOSTENIDO** | **SOSTENIDO** |

> ### **LA LECTURA QUE ADJUDICO, Y ES LA ESTRECHA**
>
> **`D.37` pide que el texto *diga cuantas partes hay*.** Una serie numerada cuyo ultimo ordinal es
> `13.` **dice cuantas hay**: el lector no infiere ni cuenta, **lee el numero**. Exigir ademas que
> sea un cardinal en letra (*"los trece elementos"*) **seria pedirle a la regla una forma lexica que
> la regla no escribe**, y la correccion del titular del 11 sep restringio el ALCANCE, no el
> vocabulario.
>
> **Y LO QUE QUEDA DICHO PARA QUE NO SE ENSANCHE MANIANA:** `D.37` sigue exigiendo **la cuenta en el
> texto** y **la parte que ESE paso nombra**. **Lo que adjudico es que un ordinal impreso cuenta
> como cuenta**, y nada mas. **Si esta lectura se quiere estrechar, es correccion declarada del
> fundador y no de una vuelta** (`6.3`).
>
> **LO QUE NO CAMBIA EN NINGUNO DE LOS DOS CASOS, y por eso esto no mueve un dato:** `D.37` y `D.29`
> **no discuten si la arista existe, sino quien la sostiene.** Las trece de `cap_14` y las cuatro de
> `cap_09` **se declaran igual**, y las cuatro ya traen su razon escrita una a una.

### 3.3. **EL DISCUTIBLE 7: LA DESVIACION DE ORDEN SE SOSTIENE POR EL CRITERIO QUE `D.36` ESCRIBE**

**`D.36`, impresa:** *Entre dos ordenes posibles, el que abre la cola gana. **Leer de mas cuesta una
lectura; leer de menos cuesta una arista que nadie sabra que falta.***

**Dejar en cola al bloqueado y seguir mete a ese candidato MAS TARDE, con MAS nodos delante, y por
tanto abre MAS pares.** La desviacion cae del lado que la regla nombra. **SOSTENIDA.**

> **Y DECLARO LA TENSION EN VEZ DE CALLARLA, porque la misma `D.36` cierra diciendo:** *ni el
> extractor ni el auditor deciden el orden de insercion; lo fija quien autoriza la insercion, que es
> el fundador.* **No la leo como mordida aqui**, y digo por que: lo que el fundador fijo es el orden
> del libro (`EXTRACTOR.md` 12.3), **y ese orden no legisla que hacer con un candidato que la aduana
> bloquea a mitad de tanda**. El no eligio entre dos ordenes autorizados: **resolvio un hueco del
> autorizado, y lo declaro antes de que se notara**, que es lo que la casa pide.
>
> **LO QUE SI ENCARGO:** que la vuelta 25 **escriba el orden que va a usar ANTES de correr la
> tanda**, y no despues. Una razon dada antes es un metodo; la misma razon dada despues es una
> justificacion, y no se distinguen leyendolas.

### 3.4. **EL GEMELO ES DE `cap_09` Y NO DE `cap_11`, Y LA CAIDA NACIO EN MI PROPIO ENCARGO**

    $ grep -o "cap_[0-9]*" cuarentena/scott_radical_candor/entregar_evaluacion_formal_desempenio_nueve_consejos.json | sort | uniq -c
        2 cap_09
    $ (su propio resumen_teorico, impreso)
      UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_09.md, unidad Cap. 6, Guidance.
      Sale de las lineas 331 a 361, bajo el rotulo FORMAL PERFORMANCE REVIEWS.
    $ sed -n "1,7p" fuentes/scott_radical_candor/cap_11.md
      unidad: Cap. 8        titulo_textual: Results

**Su `R.5.b` publica `unidad | cap_11` en tabla. El fichero dice `cap_09` dos veces, y su propio
`resumen_teorico` lo escribe con todas las letras.** Los `22` pasos si son correctos.

| | |
|---|---|
| **de donde salio** | **de mi `PROMPT_SIGUIENTE.md` `4.b`**, que escribio *de `cap_11`*. **La caida es mia de origen** y la cace yo en la fase ciega (`APERTURA_CIEGA.md` `9.1`, caida 2) |
| **por que es suya tambien** | **su propia regla lo dice**, y la aplico dos secciones antes con el rotulo de `cap_14`: *una cifra de mi encargo no es fuente de una cifra mia* (`EXTRACTOR.md` 5, y su `R.5.a`). **Remidio el rotulo del capitulo y no remidio la unidad del gemelo** |
| **sede y especie** | vive en una **TABLA** de `docs/loop/REPORTE.md`: especie **`REPORTE`, y ACUMULA** (`5.2`) |
| **la mia** | vive en `docs/loop/PROMPT_SIGUIENTE.md`. **Ver `7.2`, donde digo por que no acumula y por que eso es un agujero y no un merito** |

**Y NO TOCA NINGUN DATO: el freno reparte ese candidato por su `UNIDAD DE ORIGEN`**, y por eso su
propia tabla del freno lo cuenta en `cap_09` (20 candidatos, 272 pasos) **y no en `cap_11`**, como
verifique en la `5`. **La etiqueta esta mal en un sitio y bien en el otro.**

---

## 4. LA MUESTRA PINEADA DE LOS `SANO` (seccion `7`)

*Y aqui se paga el `NO APLICA` del `HEREDADO 3` punto 5.*

### 4.1. LA POBLACION, Y POR QUE NO HAY SORTEO

    $ python (cuenta bitacora/VEREDICTOS.jsonl, ultimas 8 lineas, por fecha)
      total veredictos: 156 | de fecha 2026-09-13: 8
      clases: 8 SANO, 0 CONTINUA, 0 REPITE | candidatos distintos: 4
      razones vacias: 0

| lo que `7` pide | lo que hago |
|---|---|
| poblacion: los `SANO` **de la tanda**, en sede | **8** |
| cuantos: el mayor entre TRES y el 20 por ciento, techo de VEINTE | pedidos **3** |
| como se eligen: al azar con semilla escrita | # **NO SORTEO: LEO LOS OCHO.** Con una poblacion de `8` un sorteo de `3` mide menos que leer la poblacion entera, y la semilla solo sirve para no elegir a ojo. **Leer todo no es elegir a ojo** |
| `D.8`: un `SANO` sin razon escrita es caida aunque acierte | **cero: las ocho traen razon no vacia**, y la mas corta tiene 158 caracteres |

### 4.2. LOS OCHO, RELEIDOS CON LOS PASOS IMPRESOS ANTES Y LA CONTAMINACION DECLARADA

*Metodo, y es el que mi propia tarea bloqueante pedia: **primero los pasos de los dos lados**
(`imprimir_pasos.py`), **despues mi clase escrita**, y **solo entonces** la razon de la bitacora.
**En los ocho arrastro la contaminacion de `2.0`**: vi los primeros noventa caracteres de su razon
en la fase ciega. Lo digo en los ocho y no en uno.*

| # | par | mi clase, escrita antes de destapar | su clase | |
|---:|---|---|---|---|
| 1 | `manejar_enfado_persona_desafiada` contra `delimitar_franqueza_radical_cinco_noes` | **SANO**: uno maneja un enfado ya ocurrido, el otro comprueba cinco limites antes de hablar | SANO | **SOSTENIDO** |
| 2 | idem contra `desplegar_marco_franqueza_radical` | **SANO**: el vecino fotocopia y reparte un cartel | SANO | **SOSTENIDO** |
| 3 | idem contra `repartir_semana_cuarenta_horas_jefe` | **SANO**: el vecino reparte cuarenta horas de calendario | SANO | **SOSTENIDO** |
| 4 | `criticar_trabajo_evitar_desanimo` contra `desplegar_marco_franqueza_radical` | **SANO**: *no personalices* contra *no uses el marco como test de personalidad*. Misma prohibicion, dos objetos | SANO | **SOSTENIDO** |
| 5 | `dar_critica_inmediata_ayuda_tangible` contra `desplegar_marco_franqueza_radical` | **SANO**: ni objeto ni acto comun | SANO | **SOSTENIDO** |
| 6 | `cambiar_potencial_trayectoria_crecimiento` contra `delimitar_franqueza_radical_cinco_noes` | **SANO**: colocar personas contra delimitar un metodo | SANO | **SOSTENIDO** |
| 7 | **el mas caro:** `cambiar_potencial_trayectoria_crecimiento` contra `cambiar_mentalidad_fija_crecimiento` (**cruza `scott` y `zhuo`**, `familia_id 0.333`) | **SANO**: el vecino trabaja **tu propia** mentalidad para poder pedir opinion, con los cuatro escenarios de Dweck; el candidato coloca a **otros** en trayectorias cambiando la palabra potencial. **Sujeto distinto y objeto distinto** | SANO | **SOSTENIDO** |
| 8 | `cambiar_potencial_trayectoria_crecimiento` contra `desplegar_marco_franqueza_radical` | **SANO**: vocabulario del libro y nada mas | SANO | **SOSTENIDO** |

### 4.3. LA TASA, CON SU BANDA, Y LA BANDA DICE QUE NO SIRVE

    $ python .t2_v24_acta/banda.py
      caidas 0 de 8  ->  tasa 0.0000
      banda exacta (Clopper-Pearson) al 95 por ciento: [0.0000 , 0.3694]

| | |
|---|---|
| releidos | **8 de 8**, la poblacion entera |
| se sostienen | **8** |
| caen | **0** |
| tasa de caida | **0,00 por ciento** |
| banda al 95 por ciento | **de `0` a `36,9` por ciento** |

> # **LA BANDA ES INUTIL Y LO DIGO EN VEZ DE PRESENTARLA COMO MEDIDA** (`7`, *una tasa sin banda es
> media cifra*, y `11` de la `ACTA 23`, *cuando la banda salga inutil se dice que es inutil*).
>
> **Con `8` de poblacion y cero caidas, el techo de la banda es `36,9 por ciento`.** Eso significa
> que **una tasa real de uno de cada tres seria compatible con lo que acabo de medir.** La tanda
> sale limpia, **y limpia no es lo mismo que medida.**
>
> **Y LO QUE SI VALE DE ESTA TANDA, que no es la tasa:** es la **primera** en la campania cuyos
> veredictos viven en `bitacora/VEREDICTOS.jsonl` y no en un reporte. **Hasta hoy la racha de
> `CLASE` no podia acumular porque no habia nada en sede donde una clase pudiera estar mal.**

---

## 5. `PASOS INVENTADOS POR CAPITULO` (seccion `8`), **FIRMADA POR MI Y CON UNA CIFRA SUYA CORREGIDA Y UNA MIA**

### 5.1. PUNTO 1 DE `8.3`: CUENTO YO LOS PASOS, DE LOS FICHEROS Y HOY

    $ python .t2_v24_acta/freno_auditor.py
      unidad      candidatos   pasos
      cap_01              1       9      cap_08             12     102
      cap_03              1      10      cap_09             20     272
      cap_04              6      48      cap_10             14     206
      cap_05              8      76      cap_11             16     187
      cap_06             10     117      cap_12              2      50
      cap_07             25     225      cap_13             12     212
                                         cap_14             15     174
      TOTAL             142    1688      ficheros leidos: 142   sin unidad: []

> **LAS VEINTISEIS CELDAS DEL DENOMINADOR CUADRAN AL DIGITO CON SU TABLA, LAS VEINTISEIS**, contadas
> de `cuarentena/` mas `_insertados/` con mi propio instrumento. **El `142` y el `1688` tambien.**
> **Esa mitad de la tabla esta bien y lo digo antes de decir lo que esta mal.**

### 5.2. PUNTO 2 DE `8.3`: RELEO MARCADOS `TRANSCRIPCION` CONTRA SU PARRAFO, **Y ENCUENTRO UN PUENTE**

*`8.3`: **el error que esta metrica invita a cometer es marcar un puente como transcripcion**,
porque baja la cifra y sube el volumen del lote siguiente. Asi que releo hacia ahi.*

    $ sed -n "97p" fuentes/scott_radical_candor/cap_14.md
      ... So you need to describe what TEAMWORK means for an entry-level employee versus a
      manager, a director, a VP, and so on. ...

**El paso 2 de `escribir_escaleras_puesto_evitar_dos_extremos` dice:** *Describe que significa
**cada categoria** en cada nivel.* **El libro nombra UNA: `teamwork`.**

| | |
|---|---|
| **el argumento a favor de su `TRANSCRIPCION`** | la frase anterior del libro es general (*el desempenio de un recien licenciado no deberia medirse con la misma vara que el de un director general*), y las categorias son cuatro. **La lectura ancha es razonable** |
| **por que aun asi es PUENTE** | **`D.30` existe para no aceptar una lectura razonable como si fuera el texto.** Y el efecto no es cosmetico: el paso manda escribir **cuatro** descripciones por nivel donde el libro escribe **una palabra**. **Multiplica el trabajo por cuatro sobre una linea que el libro no escribio** |
| **como se arregla** | nombrando el ejemplo del libro: *describe que significa cada categoria, y el texto pone como ejemplo el trabajo en equipo*. **Va al encargo** |

**Y SU PROPIO `resumen_teorico` DE ESE CANDIDATO DECLARA `7 pasos, 7 TRANSCRIPCION, 0 PUENTE`.** La
discrepancia es entre su lectura y la mia, **y publico la mia con la linea impresa al lado** para
que se pueda juzgar sin creerme.

> **Y NO ES UNA CAIDA DE NINGUNA ESPECIE, y lo digo porque si no se leeria como tal:** `8.4` dice
> que esta metrica **no entra en la metrica de credito**. **Un puente encontrado y corregido es la
> regla funcionando.** Lo que seria caida es uno que entrase al grafo sin corregir, **y este esta en
> la bandeja y sale corregido en la vuelta 25.**

### 5.3. **LA TABLA, FILA POR CAPITULO** (`8.2`), CON LAS DOS CORRECCIONES DENTRO

| unidad | candidatos | pasos | numerador | tasa | quien firma el numerador |
|---|---:|---:|---:|---:|---|
| `cap_01` | 1 | 9 | **sin medir** | **HUECO** | nadie: `1` ocurrencia sin releer con el ancho |
| `cap_03` | 1 | 10 | **sin medir** | **HUECO** | nadie: `6` ocurrencias |
| `cap_04` | 6 | 48 | **8** | **16,67** | el extractor, vuelta 22, leido uno a uno |
| `cap_05` | 8 | 76 | **2** | **2,63 (parcial)** | `20` ocurrencias sin releer con el ancho |
| `cap_06` | 10 | 117 | **sin medir** | **HUECO** | nadie: `33` ocurrencias |
| `cap_07` | 25 | 225 | **sin medir** | **HUECO** | nadie: `20` ocurrencias |
| `cap_08` | 12 | 102 | **sin medir** | **HUECO** | nadie: `17` ocurrencias |
| `cap_09` | 20 | 272 | **7** | **2,57** | el extractor, vuelta 22 |
| `cap_10` | 14 | 206 | **17** | **8,25** | **MIO**, `ACTA 21` `7.2` |
| `cap_11` | 16 | 187 | **1** | **0,53** | **MIO**, `ACTA 22` `4.1`, el candelabro |
| `cap_12` | 2 | 50 | **0** | **0,00** | el extractor, leido en el acto |
| `cap_13` | 12 | 212 | **0** | **0,00** | el extractor, leido en el acto |
| **`cap_14`** | **15** | **174** | # **1** | # **0,57** | # **MIO, y NO firmo su `0,00`**: el puente de `5.2` |
| **el lote 4 ENTERO** | **142** | **1688** | **36** | **2,13** | # **SUELO, NO MEDIDA: SEIS filas sin numerador** |

| | |
|---|---:|
| filas con numerador firmado por alguien | **7** de **13** |
| **filas de HUECO** | # **6**, y no `5` |
| el hueco, medido por mi hoy | **57 candidatos, 539 pasos, 97 ocurrencias sin adjudicar** |
| **la fila que decide, que es la peor firmada** | `cap_04` con **16,67** |
| tope de `PASOS INVENTADOS` (`8.1`, 11 sep) | **10,00** |
| **el freno** | # **DISPARADO**, por la misma fila y por tercera vuelta |
| **tramo que deja al lote 5** | **DOS capitulos por vuelta** |

### 5.4. **LA PALABRA `cinco` LLEVA TRES VUELTAS DONDE HAY `seis`, Y UNA DE LAS TRES SEDES ES MIA**

    $ grep -n "cinco\|FIRMADO" .v24/freno_cierre.py
      68: print('| **el lote 4 ENTERO** | ... **INCOMPLETO: cinco filas sin releer con el ancho** |'
      77: print('| filas con numerador FIRMADO | **%d** de **%d** |'

**LA LINEA 68 ESCRIBE `cinco` A MANO. LA LINEA 77 CALCULA `7 de 13`.** El mismo instrumento se
desmiente a si mismo nueve lineas mas abajo, **y el tallador `D.41` lo da por bueno porque la tabla
SI es la de su instrumento.** Es, al digito, la leccion que su propia caida 3 escribio: *el
tallador comprueba que la tabla es la del instrumento, no que el instrumento mida lo que dice
medir.*

| donde vive el `cinco` | sede | acumula? |
|---|---|---|
| `R.5.g`, celda de la fila total | **TABLA** de `docs/loop/REPORTE.md` | **SI**, especie `REPORTE` |
| `R.10`, la misma celda recomputada | **TABLA** | la misma caida |
| `R.12.d`, *la relectura ancha de las filas de hueco del freno: **5 filas*** | **TABLA** de cierre | la misma caida |
| `R.5.g` punto 3 y cierre de `R.10`: ***cinco filas** (`cap_01`, `cap_03`, `cap_05`, `cap_06`, `cap_07`, `cap_08`)* | **PROSA**, y **con las SEIS nombradas al lado de la palabra `cinco`** | no por sede, **pero es donde mejor se ve** |
| # **`ACTA 23` `11.1`: *la relectura ancha de las **cinco** filas de hueco (`cap_03`, `cap_05`, `cap_06`, `cap_07`, `cap_08`, 96 ocurrencias)*** | # **MI ACTA** | # **SI, Y ES MIA** |
| # **`APERTURA_CIEGA.md` `0`, `HEREDADO 4`: *las cinco filas de hueco : 56 candidatos, 530 pasos*** | # **MI APERTURA SELLADA** | # **SI, Y ES MIA** |

**LA CIFRA BUENA, MEDIDA HOY:** el hueco son **SEIS** filas, **57** candidatos, **539** pasos y
**97** ocurrencias. Las mias decian `56`, `530` y `96`: **eran la suma exacta de CINCO filas, y yo
las presente como el hueco.** La que falta es **`cap_01`** (1 candidato, 9 pasos, 1 ocurrencia).

> **DE DONDE VIENE, PORQUE IMPORTA PARA QUE NO VUELVA:** la prosa de la vuelta 23 nombro cinco
> capitulos cuando su propia tabla decia `6 de 12` firmadas. **Yo copie la lista de nombres en vez
> de restar la tabla**, y la vuelta 24 aniadio `cap_01` a la lista **sin tocar la palabra `cinco`**,
> con lo que la frase quedo diciendo *cinco* delante de seis nombres. **Tres sedes, tres vueltas, y
> ninguna de las tres lo caza porque las tres copian.**
>
> **LO QUE ESTO NO CAMBIA:** el `16,67` de `cap_04` sigue siendo la peor fila firmada y **el freno
> sigue disparado igual**. **La cifra falsa no movio el volumen de ningun lote**, y lo digo para no
> cobrarme un dano que no hubo.

---

## 6. **LA GUARDA QUE EL REPORTE DECLARA MORDIENDO, RE CORRIDA POR MUTACION** (`5.5`)

*`5.5`: **la guarda que no muerde es cifra.** Su `R.9` caida 7 declara que el tallador `D.41`
**puso un commit en ROJO**. Eso es una guarda declarada mordiendo, y se comprueba mutando.*

    $ git hash-object docs/loop/REPORTE.md
      d1b0a387cd80f58016242802502cae10470097c7
    $ (mutacion: en la tabla del freno, 1688 -> 1689, UNA celda)
    $ python scripts/tallar_reporte.py
      tablas que declaran instrumento : 41
        talladas, celda a celda       : 36
        que DIFIEREN de su instrumento: 1
      DIFIERE  docs/loop/REPORTE.md linea 29284
        declara: .v24/freno_tabla1.txt
        1 fila(s) distintas de su instrumento:
          **el lote 4 ENTERO**   pasos   reporte '**1689**'  instrumento '**1688**'
      TALLADO EN ROJO: 1 tabla(s) dicen venir de un instrumento y no coinciden con el.
    $ git checkout -- docs/loop/REPORTE.md
    $ git hash-object docs/loop/REPORTE.md
      d1b0a387cd80f58016242802502cae10470097c7

> # **LA GUARDA MUERDE.** Cambie **un digito** de **una celda** y el tallador la nombro con su
> fichero, su linea y su columna. **El reporte no exagera al declararla mordiendo.**
>
> **Y EL FICHERO QUEDO COMO ESTABA, con la huella repetida a los dos lados de la mutacion.** Una
> mutacion que no se deshace no es una prueba: es un dania declarado.
>
> **LO QUE ESTA MUTACION TAMBIEN DEMUESTRA, Y NO A SU FAVOR: `D.41` NO PUEDE CAZAR EL `cinco` DE LA
> `5.4`.** El tallador compara la tabla contra la salida del instrumento, y ahi los dos dicen
> `cinco`. **Una guarda que compara dos copias de la misma frase no valida la frase.**

---

## 7. MIS PROPIAS CAIDAS Y RETIRADAS DE ESTA VUELTA (`5.3`)

*`2`: mis errores se declaran con nombre, como los suyos. **La metrica que solo encuentra fallos
ajenos no es una metrica.***

### 7.1. **CAIDA PROPIA 1: `REMEDIO ROTO`. ROMPI EL PUNTO 1 DE MI PROPIA TAREA BLOQUEANTE**

**Declarada entera en `APERTURA_CIEGA.md` `9.1` caida 1, sellada.** Mi remedio decia: *cuando
necesite CONTAR razones, cuento con `grep -c` y no abro el fichero, y los pasos de todo par que vaya
a adjudicar se imprimen ANTES.* **A los pocos minutos de empezar la fase ciega corri un lector de
`bitacora/VEREDICTOS.jsonl` que imprimia `razon[:90]`**, y me lleve por delante los primeros noventa
caracteres de la razon de los ocho pares de la tanda **sin haber impreso un solo paso.**

| | |
|---|---|
| **especie** | **`REMEDIO ROTO` de `D.38.2`, y de la mitad que SI cuenta**: es sustancia de auditoria, una LECTURA que el remedio ordenaba. **No es formato de artefacto** |
| **por que es peor que la vez anterior** | la rompi **sobre la bitacora, que es sede de `CLASE`**, y **con el remedio entregado por el arnes en la primera pantalla de mi prompt.** No puedo alegar que no llego |
| **que hice con ella** | **no presente los ocho como relectura limpia**: van con la contaminacion declarada en `2.0` y repetida en `4.2` |

### 7.2. **CAIDA PROPIA 2: `CIFRA PUBLICADA PROPIA`. `cinco` FILAS DONDE HAY `SEIS`, EN MI ACTA Y EN MI APERTURA SELLADA**

**Desarrollada entera en `5.4`.** `D.38.2` define `CIFRA PUBLICADA PROPIA` como *una cifra falsa en
tu acta o en tu apertura sellada*, **y esta esta en las dos**: `ACTA 23` `11.1` y
`APERTURA_CIEGA.md` `0`.

> **Y AQUI HAY UN AGUJERO QUE ME BENEFICIA Y QUE DIGO YO, QUE SOY EL BENEFICIADO** (es la misma
> forma de la cosecha `7.D`): **el rotulo falso `cap_11` que yo escribi en `PROMPT_SIGUIENTE.md`
> `4.b` NO acumula en ninguna racha.** `D.38.2` cierra su lista en *tu acta o tu apertura sellada*,
> y el encargo no esta. **Cuando el extractor lo copio, acumulo contra EL** (`3.4`). **Mi encargo es
> sede mia (`5.6`) y es de donde salio la cifra.**
>
> **NO ME LO APUNTO COMO SI ACUMULARA, porque una racha no se decide por lo que a uno le parece
> justo; y lo dejo escrito para que quien pueda cerrar la lista lo vea.** Va a la `11`.

### 7.3. **RETIRADA: DOS DE LAS ONCE ARISTAS QUE MI APERTURA LEYO NO SOBREVIVEN AL FICHERO**

**Desarrollada en `3.1`, filas `i` y `j`.** Lei once remisiones **en el libro** y dos de ellas
**nunca llegaron a ser paso de su madre**, que es la condicion que `D.29` y `forja.py arista`
exigen. **La cifra de `24` que mi apertura escribio era de `22`.**

> **POR QUE LA LLAMO RETIRADA Y NO `CIFRA PUBLICADA PROPIA`, y digo la diferencia en vez de
> esconderla:** mi apertura escribio, literal, *la cifra que firme en el acta sera la que cuadre con
> la del reporte o la discrepancia declarada, **no esta***. **Una cifra declarada provisional y
> retirada en el turno siguiente no es una cifra publicada falsa; es el metodo funcionando.**
>
> **Y AUN ASI ME CUESTA, porque el beneficiado soy yo:** la distincion entre la `7.2` (falsa, y me
> la apunto) y esta (provisional, y no) **la estoy trazando yo sobre mis dos cifras.** La dejo
> escrita con las dos frases literales al lado **para que cualquiera pueda decir que me absolvi.**

### 7.4. LO QUE SI AGUANTO, Y LO DIGO PORQUE UN `REMEDIO ROTO` SOLO INFORMA SI TAMBIEN SE DECLARA CUANDO AGUANTA

| remedio | como quedo |
|---|---|
| `D.38.3`, ninguna cifra de la apertura sin instrumento al lado | **AGUANTA.** Y el unico testigo de cero bytes que tuve **quedo declarado y NO citado**, y hoy pagado (`1.7`) |
| `D.38.4`, el barrido sobre grafo mas bandejas | **AGUANTA, y dio su mejor ejemplar:** poblacion `345 = 214 + 131` cuadrada al digito contra `forja.py informe`, y **los 15 vecinos mas proximos, los 15, en la bandeja** |
| `D.34`, no recuperar de git los cuatro retirados | **AGUANTA.** Y encontre `.v24/r2.md` y `.v24/r9.md` en el arbol **y no los abri** |
| `HEREDADO 3` punto 2, todo rotulo de unidad sale de `sed -n "1,7p"` | **AGUANTA, y ademas cazo una caida vieja mia con el** (`3.4`) |
| `HEREDADO 3` punto 3, la vara sin bascula aplicada a mi propio argumento | **AGUANTA.** Tache el tamanio de mi argumento de frontera y el argumento siguio en pie (`APERTURA_CIEGA.md` `2.3`) |
| `HEREDADO 3` punto 1, imprimir los pasos antes de ver la razon | # **ROTO.** `7.1` |

---

## 8. LAS RACHAS AL CERRAR

### 8.1. LAS CUATRO, CON SU MOTIVO

| especie | de quien | venia en | **queda en** | por que |
|---|---|---|---|---|
| **`CLASE`** | extractor | 0 de 2 | **0 de 2** | **releidos los `8` veredictos de la bitacora, que es la primera tanda suya que vive en sede**, mas los `8` discutibles y el par dirigido de `2.2`. **Cero clases mal puestas.** Y `D.8` limpio: ninguna razon vacia |
| **`CIFRA PUBLICADA`** | extractor | 0 de 2 | **0 de 2** | **sus commits no tocan ni una sede de esta especie** (`1.6`): cero en `config/`, `esquema/`, `src/`, `fuentes/`, y de `docs/` solo su propio reporte. Las dos lineas de `censos/` las escribe la aduana |
| **`REPORTE`** | extractor | 1 de 3 | # **2 DE 3** | **dos caidas, las dos en TABLA**: el `cinco` que son `seis` (`5.4`) y el `cap_11` que es `cap_09` (`3.4`). **La tanda se cuenta una vez, no dos** |
| **la mia, una sola** | **auditor** | 1 de 3 | # **2 DE 3** | **`REMEDIO ROTO` (`7.1`) y `CIFRA PUBLICADA PROPIA` (`7.2`).** Las dos de `D.38.2`. **Se cuentan como UNA tanda**, igual que las suyas |

### 8.2. **LAS DOS CAIDAS `REPORTE`, CON SU SEDE, PORQUE LA SEDE DECIDE SI ACUMULA**

| # | la caida | donde vive | acumula? |
|---:|---|---|---|
| **1** | **`cinco filas sin releer con el ancho` donde su propia segunda tabla dice `7 de 13` firmadas, o sea SEIS** | **TABLA** de `R.5.g`, **TABLA** de `R.10` y **TABLA** de cierre `R.12.d` | # **SI** |
| **2** | **`unidad: cap_11` para un candidato cuyo fichero dice `cap_09` dos veces** | **TABLA** de `R.5.b` | # **SI** |
| **3** | *la columna de poblacion **recorre de `331` a `342`***, cuando su propia tabla imprime de `330` a `345` | **PROSA** de `R.5.d` | **NO** |

> ### **LO QUE LAS DOS QUE ACUMULAN TIENEN EN COMUN, PORQUE ES LO QUE HAY QUE ENCARGAR**
>
> **LAS DOS SON CIFRAS COPIADAS DE UNA SEDE ANTERIOR SIN REMEDIRLAS**, y las dos venian de mi:
> el `cinco` de mi `ACTA 23` y el `cap_11` de mi `PROMPT_SIGUIENTE.md`. **Su propia regla las
> hubiera cazado a las dos** (`EXTRACTOR.md` 5: *una cifra de mi encargo no es fuente de una cifra
> mia*), **y el la aplico ese mismo dia al rotulo de `cap_14` y no a estas dos.**
>
> **Y `D.41` NO PUEDE CAZAR NINGUNA DE LAS DOS.** La primera porque el instrumento imprime la
> mentira (`6`); la segunda porque esa tabla no declara instrumento. **No es maquinaria lo que
> falta: es restar la tabla en vez de copiar la frase.**
>
> **LA ESCALADA SE ENCARGA, NO SOLO SE DECLARA** (`1` punto 4 y `5.5`). **`REPORTE` queda en `2 de
> 3`, que es el penultimo escalon**, asi que **el remedio va encargado como TAREA 1 bloqueante** del
> `PROMPT_SIGUIENTE.md`, y no como sugerencia.

### 8.3. **POR QUE NO PONGO NINGUNA RACHA A CERO**

**`5.4`: la racha no se reinicia sola; la reinicia una tanda limpia o una decision escrita del
fundador, y ninguna de las dos soy yo.** Ni su tanda ni la mia estan limpias: **la suya tiene dos
caidas de tabla y la mia dos de `D.38.2`.** Las cuatro filas de `8.1` quedan donde las dejo la
medida.

**Y LO MISMO AL REVES: NO SUBO LA DE `CLASE` NI LA DE `CIFRA PUBLICADA` PORQUE NO ENCONTRE NADA.**
Buscarlas y no encontrarlas es el resultado, y la seccion `4.3` dice exactamente cuanto vale ese
resultado con `8` de poblacion: **poco, y con banda.**

### 8.4. **MI PROPIA RACHA EN `2 DE 3`, Y LO QUE ESO ME OBLIGA A HACER HOY**

*Cosecha `7.D`, recogida en `5.5`: **tres actas seguidas con la misma caida propia obligan a que el
acta siguiente ABRA con su remedio como tarea bloqueante del propio auditor.** Y `1` punto 4: **la
escalada se encarga, no solo se declara.***

**Estoy en el penultimo escalon de mi propia racha.** El remedio del punto 1 **ya se escribio dos
veces cada vez mas simple y las dos se rompio** (`ACTA 23` `11`, y antes). **Escribirlo una tercera
vez igual seria fingir que el problema es la redaccion.** Lo que cambia en la version de la `11` es
**el orden del turno**, no la promesa.

---

## 9. `D.32`: **ESTA ACTA CIERRA EL LOTE 4 EN EXTRACCION Y ABRE EL LOTE 5**

*`1` punto 5: **si el acta cierra un lote, abre el siguiente**, midiendo sus dos condiciones,
publicandolas, y escribiendo el encargo **en vez de una parada** si estan en verde.*

### 9.1. EL CIERRE DEL LOTE 4, MEDIDO POR MI Y NO ACEPTADO

    $ python .t1_v24_auditor/cobertura_lote4_auditor_v24.py     (mio, de la fase ciega)
      unidades del lote 4                  : 15
      candidatos leidos                    : 142  (bandeja 131 + insertados 11)
      unidades A CERO por las dos lecturas : 2  ['cap_00', 'cap_02']
    $ sed -n "1,7p" fuentes/scott_radical_candor/cap_00.md  ->  unidad: Copyright Page
    $ sed -n "1,7p" fuentes/scott_radical_candor/cap_02.md  ->  unidad: Introduction

**Las dos unidades a cero estan saldadas en vueltas anteriores** (`cap_00` no es minable; `cap_02`
se mino con resultado cero candidatos). **`0` unidades sin minar: el lote 4 CIERRA EN EXTRACCION.**

> **Y LO QUE NO CIERRA, DICHO EN LA MISMA FRASE PARA QUE NO SE LEA DE MENOS: LA INSERCION VA POR
> `11` DE `142`.** `D.32` es explicita: **la insercion del lote que cierra se pide aparte y NO
> bloquea la extraccion del siguiente.** Por eso abro el 5 **y** encargo el resto de la insercion
> del 4, y no una cosa en vez de la otra.

### 9.2. LAS DOS CONDICIONES DEL LOTE 5, MEDIDAS HOY Y EN EL ACTO

*`ORDEN_DE_LOTES.md` fila 5: el lote que toca es **`marquet_turn_the_ship`**, 17 unidades.*

    $ ls fuentes/marquet_turn_the_ship/*.md | wc -l
      17
    $ python (lee las claves de fuentes/FUENTES_CANONICAS.json)
      claves en la tabla canonica: 13
      marquet_turn_the_ship presente: True

| condicion de apertura (`D.32`) | medida hoy | |
|---|---|---|
| **el material esta en `fuentes/<clave>/`** | **17 ficheros `.md`** | # **VERDE** |
| **la clave esta en la tabla canonica** | **`True`** | # **VERDE** |

**LAS DOS EN VERDE. ABRO EL LOTE 5, y por tanto esta acta escribe encargo y NO parada.**

**Y NO COPIO LA MEDIDA DE LA `ACTA 23` `9`**, que ya las habia medido: **las he vuelto a correr
hoy**, que es lo que mi propia apertura dejo escrito en `10.3` punto 6.

### 9.3. EL VOLUMEN DEL LOTE 5, DECIDIDO SOBRE LA PEOR FILA FIRMADA (`8.1` y `8.2`)

| | |
|---|---|
| peor fila **firmada** del lote 4 | `cap_04`, **16,67** |
| tope | **10,00** |
| **por encima del tope, asi que se baja un escalon** | el tramo vigente es **TRES** (correccion declarada del 12 sep, punto 2), **y baja a DOS** |
| **el lote 5 corre a** | # **DOS capitulos por vuelta** |

**Y LA SALVEDAD QUE VIAJA CON ESA CIFRA:** `cap_04` lleva tres vueltas decidiendo el volumen **y
nadie lo ha vuelto a leer**. El `2,13` del lote entero es **un SUELO**, porque **seis** de sus trece
filas no tienen numerador. **Mientras eso siga asi, el freno no esta midiendo el lote: esta
midiendo una fila de la vuelta 22.**

---

## 10. LA VUELTA 24, EN UNA TABLA

| | |
|---|---|
| **lo que verifique con mis comandos** | las **4** guardas, el conteo de grafo, bitacora y bandejas (**5 de 5 cuadran**), el tallado, el resolutor, la **frontera de `cap_14` cortada a ciegas por mi**, las **36** filas contables de la deuda, las sedes que tocaron sus commits y el saldo de aduana de los 15 |
| **la frontera** | # **LAS 17 PIEZAS Y LOS 15 BORDES COINCIDEN CON LOS SUYOS, sin habernos visto.** `7638 = 7638`, residuo `0`, solapes `0` |
| **el saldo de aduana de los 15, corrido por mi hoy** | # **`CAERIAN 0`** (su correccion de puerta esta buena) y # **`CHOCAN entre si dentro del lote: 0`** (la frontera de `15` no se duplica consigo misma, y esa prueba su tanda no podia darla). `43` filas vecino hoy contra `27` suyas: **la cola crece, como el dijo** |
| **discutibles releidos** | **8 de 8.** **7 sostenidos**, **1 discrepancia** (el `5`), que es una arista que falta y no una clase mal puesta |
| **muestra pineada** | **8 de 8**, la poblacion entera de la tanda en sede. **8 sostenidos, 0 caidas.** Tasa `0,00`, **banda de `0` a `36,9`: inutil, y lo digo** |
| **pares dirigidos mios** | **6**: los cinco de mi apertura mas el de `2.2`, que **ninguna senial levanto** y que era el candidato a duplicado de la vuelta |
| **lo que adjudico** | **8 aristas que el libro escribe y la vuelta no declaro**, con su paso citado; **2 mias retiradas**; los discutibles **1 y 3 juntos** con la lectura estrecha de `D.37`; el **7** por el criterio de `D.36`; y la unidad del gemelo, **`cap_09`** |
| **caidas suyas** | **2 de especie `REPORTE`, las dos en TABLA y las dos copiadas de una sede mia sin remedir.** Cero de `CLASE`. Cero de `CIFRA PUBLICADA` |
| **caidas mias** | **2 de `D.38.2`**: un `REMEDIO ROTO` y una `CIFRA PUBLICADA PROPIA`. Mas **una retirada** de dos aristas que lei en el libro y no en los pasos |
| **`PASOS INVENTADOS`** | **firmo la tabla entera**, con **`cap_14` en `0,57` y no en `0,00`** (un puente mio encontrado), y con **SEIS filas de hueco y no cinco**: `57` candidatos, `539` pasos, `97` ocurrencias |
| **rachas** | `CLASE` **0 de 2**, `CIFRA PUBLICADA` **0 de 2**, `REPORTE` # **2 de 3**, la mia # **2 de 3** |
| **paradas** | # **NINGUNA.** Ver `8.4` y la tabla de abajo |
| **`D.32`** | # **EL LOTE 4 CIERRA EN EXTRACCION Y ABRO EL LOTE 5** (`marquet_turn_the_ship`), con sus dos condiciones medidas hoy en verde y **DOS capitulos por vuelta** |

### 10.1. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`3`)

| condicion | |
|---|---|
| **doctrina NUEVA necesaria** | **NO.** Las cuatro adjudicaciones de `3` las cubre una regla escrita citada: `D.29` las ocho aristas, `D.37` con su condicion de cuenta, `D.36` el orden, y `EXTRACTOR.md` 5 la unidad |
| **contradiccion con regla vigente o cifra publicada** | **NO.** Las dos caidas `REPORTE` y las dos mias se resuelven con correccion declarada, que es una regla de correccion existente. **El choque `D.41` contra `D.34.2` es real y va declarado** (`1.1`), **pero no se ha repetido todavia** |
| **decision de Alexis reservada** | **NO.** Nada de borrar contenido, mover umbrales, cambiar alcance, crear remotos ni publicar. **La PARADA que el declaro en `R.2.d` la recojo y la resuelvo en `11.2` sin tocar su sede** |
| **fallo tecnico repetido** | **NO, y por poco.** `gate`, `guiones`, `test_aceptacion` y el tallado **en verde, corridos por mi** (`1.1`). El fallo de mi fase ciega es **la primera** de las dos que harian parada |
| **credito roto** | **NO.** `CLASE` `0 de 2`, `CIFRA PUBLICADA` `0 de 2`, `REPORTE` `2 de 3`, la mia `2 de 3`. **Ninguna en su ultimo escalon**, y las dos que estan en el penultimo **llevan su remedio encargado como tarea bloqueante** |
| **campania consumada** | **NO.** El lote 4 cierra en extraccion y le falta la insercion; **quedan siete lotes detras** |

> # **NO SE CUMPLE NINGUNA CONDICION DE PARADA. NO ESCRIBO `PARA_ALEXIS.md`, Y `PROMPT_SIGUIENTE.md` VA ESCRITO ENTERO.**

---

## 11. **LOS REMEDIOS QUE ME DEJO A MI MISMO**, para que el arnes se los entregue al auditor siguiente (`D.40`)

*Van aqui y no en `PROMPT_SIGUIENTE.md`, que es el encargo del EXTRACTOR. `src/herencia.py` los saca
de este acta.*

> ### **TAREA BLOQUEANTE DEL AUDITOR, para la vuelta 25**
>
> **1. EL ORDEN DEL TURNO CAMBIA, PORQUE LA PROMESA YA FALLO DOS VECES.** La version simple del
> remedio (*no abras el fichero de razones*) **la rompi igual**. Lo que cambia ahora **no es lo que
> prometo: es cuando lo hago.** **LO PRIMERO que corro en la fase ciega, antes de abrir ningun
> fichero de trabajo, es `imprimir_pasos` sobre los pares de la tanda**, y esa salida queda en
> disco. **Un fichero que ya existe no se puede contaminar despues.** Si al empezar no se cual es la
> tanda, imprimo **los pasos de todo lo que la bitacora cambio ese dia**, que se saca con
> `cut -f candidato,vecino` sin leer la columna `razon`.
>
> **2. UNA CIFRA QUE YO COPIO DE MI PROPIA ACTA SE REMIDE ANTES DE ESCRIBIRLA.** El `cinco` de `5.4`
> **lo publique yo dos veces sin restar la tabla que tenia al lado**. El extractor tiene esa regla
> escrita (`EXTRACTOR.md` 5) y **yo no la tengo escrita contra mi mismo.** La tengo desde hoy:
> **ninguna cifra pasa de un acta mia a la siguiente sin su comando de hoy al lado**, y **cuando una
> cifra viene con una lista de nombres, se cuenta la lista.**
>
> **3. UNA ARISTA SE LEE EN LOS PASOS, NO EN EL LIBRO.** Dos de mis once (`7.3`) eran lineas del
> libro que ningun paso recogio. **Antes de escribir una arista en cualquier sede mia, imprimo el
> paso de la madre que la sostiene**, con su numero. Sin numero de paso no la escribo, ni siquiera
> como lectura provisional.
>
> **4. LA APERTURA CIEGA SIGUE TRAYENDO SU BARRIDO `D.38.4` Y SU HERENCIA `D.40` UNA A UNA**, y
> **todo `NO APLICA` se paga en el turno normal de la MISMA vuelta**, como pague hoy los dos de
> `0.1`.
>
> **5. LA MUESTRA PINEADA SE PUBLICA CON SU BANDA, Y CUANDO LA BANDA NO SIRVA SE DICE**, como en
> `4.3`. **Y cuando la poblacion quepa entera, se lee entera en vez de sortearse**, diciendo por que.

### 11.1. **LO QUE ENCARGO AL EXTRACTOR Y NO A MI**, y va en `PROMPT_SIGUIENTE.md`

**TAREA 1 es bloqueante y su motivo es la racha**: `REPORTE` en `2 de 3` es el penultimo escalon, y
`1` punto 4 me obliga a encargar el remedio **en el mismo acta**. Las dos correcciones (`cinco` a
`seis`, `cap_11` a `cap_09`) van ahi con su correccion declarada y sin borrar, **y la linea 68 de
`.v24/freno_cierre.py` se arregla calculando en vez de tecleando**, que es la letra de `D.41`.

### 11.2. **LA PARADA QUE EL DECLARO EN `R.2.d`: LA RESUELVO YO Y NO LLEGA A ALEXIS**

**Tiene razon en pararse y lo hizo bien.** `EXTRACTOR.md` 14 asigna `docs/BANCO_DE_REGLAS.md` a
Alexis, **mi propio encargo le mando escribir ahi**, y el se nego citando la regla. **Eso es
exactamente lo que `7` le pide.**

| | |
|---|---|
| **quien tenia mal el encargo** | **yo.** Mi `PROMPT_SIGUIENTE.md` puso una tarea en una sede que el no tiene |
| **es parada de las de `3`?** | **NO.** `3` reserva a Alexis *borrar contenido, cambiar el alcance, mover umbrales, crear remotos, publicar*. **Una nota de uso pegada a `D.41` no es ninguna de las cinco** |
| **como se resuelve** | **retirando la tarea, que es lo que hago.** No la reescribo para otra sede y no se la paso a nadie: **la nota que el redacto queda en su `R.2.d`, entera y lista para pegar**, y quien tenga la sede la pega cuando quiera |

**NO ESCRIBO YO EN EL BANCO EN ESTA VUELTA.** Hay precedente de que el auditor lo ha hecho
(`fa1f15a`, `ACTA 18`), **pero un precedente no es una regla**, y la regla que tengo delante
(`EXTRACTOR.md` 14) no me nombra a mi tampoco. **Lo dejo donde el lo dejo.**

### 11.3. **UN REMEDIO QUE NO ES MIO Y QUE ESTA VEZ SI ENCARGO**

**La relectura ancha de las filas de hueco del freno lleva TRES vueltas declarada y tres sin
hacerse**, y la `ACTA 23` `11.1` la dejo escrita como primera tarea de la vuelta 25. **Hoy la
encargo, y la encargo RECORTADA con su recorte dicho**, que es lo contrario de encargarla entera y
que se caiga sola:

| | |
|---|---|
| **el hueco entero** | **6 filas, 57 candidatos, 539 pasos, 97 ocurrencias** |
| **lo que encargo** | **`cap_01`, `cap_03` y `cap_05`: 3 filas, 10 candidatos, 95 pasos.** Cierran la mitad de las filas por menos de la quinta parte del trabajo |
| **lo que queda en cola, dicho y no callado** | **`cap_06`, `cap_07` y `cap_08`: 3 filas, 47 candidatos, 444 pasos.** **Va escrito aqui para que la vuelta 26 no tenga que redescubrirlo** |

> **POR QUE NO LA ENCARGO ENTERA:** `539` pasos releidos contra el libro, **en la misma vuelta que
> tiene que terminar una insercion de 131 candidatos y abrir un lote**, es una cifra que ya se que
> no cabe. **Encargar lo que no cabe y que vuelva sin hacerse es lo que lleva tres vueltas pasando.**
> **Un recorte declarado no es una omision silenciosa** (`5.5`, *el exceso se declara y se reparte
> en tramos siguientes, nunca se dobla*).

---
