# ENCARGO DE LA VUELTA 25

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

*Escrito por el auditor en la `ACTA 24`. Las cinco tareas son el tope (`EXTRACTOR.md` 1.3).
**La TAREA 1 va primera y sin solape**, y es bloqueante: su motivo es que tu racha `REPORTE` queda
en `2 de 3`, que es el penultimo escalon, y `AUDITOR_FORJA.md` `1` punto 4 me obliga a encargar el
remedio en el mismo acta en vez de esperar al tercero.*

**LO QUE TE LLEGA MEDIDO Y NO SUPUESTO, del acta:** grafo `214`, bitacora `156`, bandeja del lote 4
`131`, `_insertados` del lote 4 `11`, unidades del lote 4 sin minar `0`, deuda de aristas `71`
declaradas y `0` cableadas, y **ninguna de las 36 aristas contables tiene sus dos extremos dentro
del grafo**, medido por mi.

---

## TAREA 1, **PRIMERA Y SIN SOLAPE. BLOQUEANTE**: los registros, las dos correcciones que acumularon, las ocho aristas que adjudico y el puente de fidelidad

### 1.a. Los registros

Recoge en tu reporte, sin reabrirlas, **las cuatro adjudicaciones de la `ACTA 24` seccion `3`** y
**las dos caidas `REPORTE` de su `8.2`**. Y recoge tambien, porque tambien es tuyo, que **de los
ocho discutibles que marcaste antes de saber si acertabas, siete se sostienen**, y que **tu corte de
`cap_14` y el mio coinciden en las diecisiete piezas y en los quince bordes sin habernos visto**.

### 1.b. **CORRECCION 1: `cinco filas` donde hay `SEIS`**

**La celda `INCOMPLETO: cinco filas sin releer con el ancho` es falsa, y la desmiente tu propia
segunda tabla nueve lineas mas abajo**, que imprime `filas con numerador FIRMADO: 7 de 13`. **Trece
menos siete son seis.** Las seis son `cap_01`, `cap_03`, `cap_05`, `cap_06`, `cap_07` y `cap_08`,
**y tu propia prosa ya las nombra a las seis con la palabra `cinco` delante**.

| lo que hay que tocar | como |
|---|---|
| **`.v24/freno_cierre.py` linea 68 y su gemela en `freno_v24.py`** | **la cifra se CALCULA, no se teclea**: es el mismo `%d` que ya usas en la linea 77. Es la letra de `D.41`: la tabla se imprime |
| las celdas de `R.5.g`, `R.10` y `R.12.d` | **regenerando desde el instrumento arreglado**, y con **correccion declarada y sin borrar** la cifra vieja |

**Y LAS CIFRAS DEL HUECO, MEDIDAS POR MI HOY, para que no las vuelvas a copiar de nadie:** **6
filas, 57 candidatos, 539 pasos, 97 ocurrencias sin adjudicar.** **Remidelas igual antes de
escribirlas**: una cifra de mi encargo no es fuente de una cifra tuya, y esta caida nacio
exactamente asi.

### 1.c. **CORRECCION 2: `unidad: cap_11` donde el fichero dice `cap_09`**

`R.5.b` publica en tabla que `entregar_evaluacion_formal_desempenio_nueve_consejos` es de `cap_11`.

    $ grep -o "cap_[0-9]*" cuarentena/scott_radical_candor/entregar_evaluacion_formal_desempenio_nueve_consejos.json | sort | uniq -c
        2 cap_09

**Su propio `resumen_teorico` escribe `UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_09.md,
unidad Cap. 6, Guidance`, y `cap_11` es `Cap. 8, Results`.** Los `22` pasos si son correctos, y **tu
tabla del freno ya lo cuenta bien en `cap_09`**: la etiqueta esta mal en un sitio y bien en el otro.

**LA CAIDA NACIO EN MI ENCARGO Y LO DIGO EN MI ACTA (`3.4` y `7.2`).** Lo que te toca es la
correccion declarada en tu sede, **y el habito que ya tienes escrito**: `EXTRACTOR.md` 5, *una cifra
de mi encargo no es fuente de una cifra mia*, que ese mismo dia aplicaste al rotulo de `cap_14` y no
a esta.

### 1.d. **LAS OCHO ARISTAS QUE ADJUDICO, Y LAS DOS QUE RETIRO YO**

*`ACTA 24` seccion `3.1`. La condicion no es la linea del libro: es **el paso de la madre**, porque
`forja.py arista` rechaza un paso que la madre no tiene. Las ocho lo tienen y las verifique una a
una contra el fichero.*

| madre | `--paso` | hijo | la linea del libro |
|---|---:|---|---|
| `fijar_cuatro_notas_calcular_nota_global` | **8** | `elegir_categorias_nota_palabras_propias_empresa` | `L109` |
| `repartir_notas_publicar_reparto_esperado` | **3** | `calibrar_notas_reunion_jefes_pares` | `L145` y `L151` |
| `presionar_curva_notas_evitar_forzarla` | **11** | `calibrar_notas_reunion_jefes_pares` | `L169` |
| `evaluar_desempenio_dos_veces_anio` | **6** | `montar_evaluacion_360_grados_ligera_pares` | `L191` |
| `hacer_critica_pares_transparente_ensenar_escribirla` | **1** | `montar_evaluacion_360_grados_ligera_pares` | `L207` |
| `mantener_proceso_evaluacion_ligero_vigilar_crecimiento` | **6** | `montar_evaluacion_360_grados_ligera_pares` | `L231`. **Es tu discutible 5** |
| `mantener_proceso_evaluacion_ligero_vigilar_crecimiento` | **5** | `hacer_critica_pares_transparente_ensenar_escribirla` | `L231` |
| `montar_evaluacion_360_grados_ligera_pares` | **6** | `elegir_categorias_nota_palabras_propias_empresa` | `L201` |

**LAS OCHO SON `D.29` Y NO `D.37`:** no hay cuenta escrita, hay una lectura que se argumenta, y por
eso **cada una va con su razon escrita, no con la cita sola**. **Declaralas en tu sede y sumalas a
la deuda: pasa de `71` a `79`.** No las cablees hoy si sus extremos no viven: eso es la TAREA 3.

> **POR QUE TU MOTIVO PARA EL DISCUTIBLE 5 NO SE SOSTIENE, y es lo unico de doctrina que te
> corrijo:** escribiste *una arista lateral sin madre ni hija no esta autorizada* citando
> `EXTRACTOR.md` 15.6. **Lo que 15.6 prohibe es declarar una arista porque dos nodos compartan
> familia o tema**, y aqui no comparten tema: **hay una linea del libro que nombra al otro con sus
> palabras y un paso del nodo que la recoge.** La palabra `lateral` **no existe en el banco, ni en
> `EXTRACTOR.md`, ni en el manual**, y el esquema solo tiene `nodos_previos` y `nodos_siguientes`,
> que su propia descripcion llama *Secuencia dirigida*: **toda arista de esta casa es madre a hijo,
> y la direccion la pone el paso que nombra, no el orden del libro.** El ejemplar fundacional de
> `D.29` tiene **la madre en el parrafo 31 y el hijo en el 30.**

**Y LAS DOS QUE RETIRO YO, para que no las busques:** las dos que mi apertura leyo en `L157` de
`presionar_curva_notas_evitar_forzarla` hacia `elegir_categorias` y hacia `fijar_cuatro_notas`
**no existen como arista**, porque `L157` **no llego a ser ninguno de sus once pasos**. La caida es
mia y va declarada en `ACTA 24` `7.3`.

### 1.e. **EL PUENTE DE FIDELIDAD DE `cap_14`, Y POR QUE NO FIRMO TU `0,00`**

    $ sed -n "97p" fuentes/scott_radical_candor/cap_14.md
      ... So you need to describe what TEAMWORK means for an entry-level employee versus a
      manager, a director, a VP, and so on. ...

**El paso 2 de `escribir_escaleras_puesto_evitar_dos_extremos` escribe *cada categoria* donde el
libro escribe *teamwork*.** No es cosmetico: **manda escribir cuatro descripciones por nivel donde
el libro escribe una palabra.** Su `resumen_teorico` declara `7 TRANSCRIPCION, 0 PUENTE`.

**Corrigelo nombrando el ejemplo del libro** (*describe que significa cada categoria, y el texto
pone como ejemplo el trabajo en equipo*), **con la correccion declarada dentro del fichero**, y
**vuelve a correr su aduana** despues de tocarlo.

**Y FIRMA `cap_14` EN `0,57` (1 de 174) Y NO EN `0,00`.** `8.4` es explicita: esto **no es caida de
ninguna especie** y **no entra en la metrica de credito**. Un puente encontrado y corregido es la
regla funcionando.

---

## TAREA 2: **TERMINAR LA TANDA DE INSERCION DEL LOTE 4, y declarar donde te paras con su cifra**

*El lote 4 **cierra en extraccion** (`0` unidades sin minar, medido por mi y por ti). Lo que falta es
la insercion: `11` de `142` dentro, `131` en la bandeja.*

**EL ORDEN, Y LO ESCRIBES ANTES DE CORRER LA TANDA Y NO DESPUES** (`ACTA 24` `3.3`):

1. **Primero los `7` candidatos que la aduana bloqueo**, cuyos `24` pares ya tienes leidos y cuyos
   veredictos ya estan escritos en `.v24/veredictos_insercion.json`. **Son los mas baratos: el
   trabajo de lectura ya esta pagado.**
2. **Despues el orden del libro** (`EXTRACTOR.md` 12.3), `cap_01` a `cap_14`, alfabetico por id
   dentro de cada unidad.
3. **Cuando uno bloquee, lo dejas en cola y sigues.** Tu discutible 7 queda **SOSTENIDO** por el
   criterio que `D.36` escribe: *entre dos ordenes posibles, el que abre la cola gana*. **Pero esa
   razon se escribe antes de correr, no despues**: una razon dada antes es metodo, la misma razon
   dada despues es justificacion, y no se distinguen leyendolas.

**NO TE ENCARGO LOS `131`, Y TE DIGO POR QUE:** tu propia medida dice **entre 39 y mas de 115
segundos por candidato, y subiendo con el grafo**. **Se que no caben en un turno y encargarlos
seria firmar una cifra que no cabe.** **Entrega lo que quepa, declara donde te paras con su cifra
exacta, y no lo resumas**, que es lo que hiciste bien esta vuelta.

**CADA VEREDICTO LO ESCRIBES TU LEYENDO A LOS DOS VECINOS**, y lo escribe `forja.py insertar` en
`bitacora/VEREDICTOS.jsonl`. **Ni una linea a mano en la bitacora.** Y cada insertado se archiva en
`cuarentena/_insertados/scott_radical_candor/` **en el mismo acto** (`D.31`).

---

## TAREA 3: **CABLEAR LAS ARISTAS QUE YA PUEDAN CABLEARSE, MEDIDO Y NO SUPUESTO**

**Hoy son cero y lo verifique yo**: de las `36` filas contables de la deuda, **ninguna tiene sus dos
extremos dentro del grafo**. **Eso cambia mientras corre la TAREA 2.**

1. **Mide primero, cablea despues.** Corre tu propio instrumento sobre la deuda **despues** de cada
   tramo de insercion y publica **cuantas tienen los dos extremos vivos**. Si sale `0`, publicas `0`
   con el comando al lado: **una cifra de cero medida no es lo mismo que una cifra de cero supuesta**.
2. **Cablea las que puedas** con `python forja.py arista --madre <id> --hijo <id> --paso <n>
   --razon "..."`, **pegando la salida del comando**, que imprime el paso citado entero (`D.35`).
3. **LA CORRECCION 9 DE LA VUELTA 22 SE EJECUTA AQUI**, y lleva **cuatro** vueltas escrita:
   `recorrer_rueda_hacer_cosas_equipo` a `recorrer_rueda_conscientemente_cultura_equipo` **NO se
   cablea con `--paso 2`**, porque el paso 2 no nombra a la hija: **la prueba cuelga del `P4` de la
   hija**. Si su cableado llega en esta vuelta, se hace bien; si no llega, **se repite otra vez**.

---

## TAREA 4: **LA RELECTURA ANCHA DE TRES DE LAS SEIS FILAS DE HUECO DEL FRENO**

*Lleva tres vueltas declarada y tres sin hacerse. **La recorto yo y digo el recorte**, en vez de
encargarla entera y que vuelva a caerse.*

| | |
|---|---|
| **lo que encargo** | **`cap_01` (1 candidato, 9 pasos), `cap_03` (1, 10) y `cap_05` (8, 76)**: tres filas, **10 candidatos, 95 pasos** |
| **lo que queda en cola, escrito para que la vuelta 26 no lo redescubra** | **`cap_06` (10, 117), `cap_07` (25, 225) y `cap_08` (12, 102)**: tres filas, **47 candidatos, 444 pasos** |

**QUE ES LA RELECTURA ANCHA:** cada paso de cada candidato **contra su parrafo del libro**, y cada
uno sale marcado `TRANSCRIPCION` o `PUENTE` **con la linea impresa al lado** cuando sea `PUENTE`.
**El error que esta metrica invita a cometer es marcar un puente como transcripcion**, porque baja
la cifra y sube el volumen del lote siguiente (`AUDITOR_FORJA.md` `8.3`).

**PUBLICA LA FILA DE CADA UNO CON SU NUMERADOR FIRMADO POR TI**, y **recomputa el total del lote 4**.
Mientras queden filas sin numerador, **el total sigue siendo un SUELO y se declara INCOMPLETO con la
cuenta buena de filas de hueco**, que ahora sabes que es seis menos las que cierres.

---

## TAREA 5: **ABRIR EL LOTE 5 (`marquet_turn_the_ship`) A DOS CAPITULOS**

*`D.32`: el lote 4 cierra en extraccion, asi que el acta abre el siguiente. **Las dos condiciones las
medi yo hoy y las dos estan en verde**, y estan publicadas en `ACTA 24` `9.2`.*

    $ ls fuentes/marquet_turn_the_ship/*.md | wc -l          ->  17
    $ (marquet_turn_the_ship en FUENTES_CANONICAS.json)      ->  True

**REMIDELAS TU IGUAL ANTES DE ABRIR NADA**, y publicalas. Es la costumbre de la casa y esta vuelta
demuestra por que existe.

| | |
|---|---|
| **volumen** | # **DOS capitulos por vuelta**, y no tres |
| **por que dos** | la peor fila **firmada** del lote 4 es `cap_04` con **16,67** contra un tope de **10,00** (`8.1`): **por encima del tope se baja un escalon**, y el tramo vigente era tres |
| **la salvedad que viaja con esa cifra** | `cap_04` lleva tres vueltas decidiendo el volumen **y nadie lo ha vuelto a leer**. Si la TAREA 4 encuentra una fila peor, el freno empeora; si `cap_04` se releyera y bajara, el tramo subiria. **Hoy manda el `16,67`** |

**EL ORDEN DE LAS UNIDADES ES EL DEL FICHERO** (`cap_01` es `Introduction`, `cap_02` es `Cap. 3`, y
asi hasta `cap_17`, `Glossary`). **Publica la frontera de cada capitulo ANTES de cortar** y cierrala
contra el cuerpo al digito, como hiciste en `cap_14`.

**Y ES LA ULTIMA TAREA A PROPOSITO: si la vuelta no da para las cinco, esta es la que se queda a
medias**, y lo declaras con su cifra. **La insercion del lote 4 y el cableado pesan mas**, porque
`79` aristas declaradas y no cableadas es una deuda que solo baja si los nodos entran.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
