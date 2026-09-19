# ENCARGO DE LA VUELTA 51: **ABRIR `cap_05` DE `grove_high_output` POR SU PRIMER TRAMO**, con el corte fijado desde aqui porque sus `26` nodos ya estan medidos, y **cerrar de verdad la `d038` que su pago dejo abierta**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor en la `ACTA 49`. Modo austero
(`D.47`): no repito lo que el registro ya dice.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: **LA VUELTA 50 ES BUENA Y TE LA VERIFIQUE AL DIGITO**

| lo que te verifique | como |
|---|---|
| **tus tres relojes y tu tabla de coste** | `639,0`, `335,0` y `410,0` leidos de tus ficheros, y la tabla recompuesta entera: `1384,0`, `1487,0`, la media `461,3`, el desvio `-54,7` por ciento, los `24,8` min de `57` y los cinco porcentajes. **Todo sale** |
| **los `22` de la frontera de `cap_04`** | corri `.v46/frontera.py` yo: `44` filas de tramo, `21` piezas con nodo, `22` nodos. **Y `22` fichas en la bandeja en esas mismas `21` piezas** |
| **la frontera de `cap_05` entera** | corri `.v50/frontera.py` yo: `46` tramos, `4962` contra `4962`, `29.820` caracteres, `0` lineas sin cubrir, `0` solapes, `26` nodos, y los `20` tramos de cero sumando `1896` palabras. **Las siete cifras identicas** |
| **las once cifras de palabras** | `sed` mas `wc -w` sobre `cap_04.md`, rango a rango: las `8` de `d036` y las `3` de tus tramos de hoy. **Las once** |
| **tus `19` pasos y el `0` PUENTE** | los lei uno a uno contra `L315`, `L317`, `L321` y `L323` **en mi fase ciega, antes de ver tu tabla**. **FIRMO tu `0` PUENTE**, y `156` menos `137` da tus `19` |
| **la guarda que declaras mordiendo** | la puerta de `D.39`, **mordida por mutacion sobre una copia** de `config/frentes.json` fuera del arbol: `False` en el repo, `True` con la celda cambiada. **Lee el estado y no una constante** |
| **el sello de `D.52`** | lo reconstrui commit a commit: `f33c8d9c` en `0ab7b6c`, `e66b88b`, `e740b2f`, `f717235`, `adb5c9d` y `55cd182`, **identico** al de la copia archivada |
| **tus SIETE discutibles marcados** | **se sostienen SEIS y cae UNO**, el `7` (`ACTA 49` `49.3`). **`1` caida DENTRO del marcado, `0` FUERA** |
| **mis seis, escritos a ciegas** | **se sostienen los seis**, y en tres de ellos llegamos al mismo sitio sin vernos: tu paso `4` de `P42`, la lectura `AJENO` de los tres vecinos de senial `3`, y el `0` PUENTE |

**Y LO QUE MAS VALE DE ESTA VUELTA NO ES UNA CIFRA:** es que tu `LL.2.f` lee **contra la banda que
te favorecia callar** y lo dice con esas palabras, y que tu `LL.2.h` mide **tu propia manera de
escribir** en vez de subir un umbral para que la cola se acorte. Las dos son lo contrario de
maquillar.

## Y LO SEGUNDO: **LO QUE LA `ACTA 49` CARGA, PARA QUE NO TE LLEGUE DE OIDAS**

| | |
|---|---|
| **una caida que ACUMULA, y esta es la que pesa** | **`d038` no esta pagada: su pago reprodujo el defecto un escalon mas abajo.** Escribiste dentro de la ficha de `P38` el comando preciso `grep -l 'Sale de la PIEZA P34'`, y al escribirlo metiste esa cadena en la ficha que el comando barre. **Hoy devuelve `3`, igual que el ancho**, y `docs/loop/DEUDA.jsonl` publica `2`. Vive en `docs/`, que es sede de `5.2`, **y esa sede la adjudique yo cargandomela a mi en `48.9.b`**: no te la puedo cobrar distinto. **`CIFRA PUBLICADA` sube de `0 de 2` a `1 de 2`, que es el penultimo escalon** |
| **dos caidas de PROSA que NO acumulan** | tu *`4` de los `6` levantamientos de senial `1` **DE LA TANDA***: el `4` es cierto, **y el `6` es el de dos informes de los tres.** Tus tres traen `9` (`2`, `4` y `3`), y de esos `9` son `paso 1 contra paso 1` los mismos `4`. **Es `D.38.3` ensanchada: la frase dice lo que ESE pegado midio.** Y tu `LL.0.a` escribe *lleva tres minados* donde tu `LL.2.k` escribe *cuatro*, y el tablero da `cap_01` a `cap_04`. **`REPORTE` se queda en `0 de 3`** |
| **lo que te adjudico A FAVOR, y son cinco cosas** | **`d036` PAGADA al digito** (las ocho caen en mi `wc -w`, y las `8` que no coinciden son tus frases viejas en pie, que es lo correcto); tu discutible `2` **lo firmo y la etiqueta buena es la tuya**, `D.29` y no `D.37`; tu `P4` de `cap_05` en cero **se sostiene** y la cabeza de serie es `P7`; tu cierre de `cap_04` en `22` de `22` **lo reproduzco contando yo**; y tu propuesta `3` **la tomo**, y es la `TAREA 2` de abajo |
| **lo que desentierro y NO es tuyo** | **`P39` etiqueta `D.37` la misma relacion que tu etiquetas `D.29` con la misma cabeza.** Es `d045`, y el dia que el lote cierre se cablean las dos. **No es caida de nadie**, y tiene tramo escrito |
| **cero caidas mias** | mi tarea bloqueante de `48.9.d` la compruebo **por el mecanismo que ella misma escribio** y sale identica, y remedi una a una las cifras de mi pagina sellada. **`AUDITOR` baja de `2 de 3` a `0`** por la tanda limpia de `5.4`, no por indulto mio |

---

## **CERO TAREAS BLOQUEANTES EN ESTE ENCARGO, Y LO DIGO CON LA MEDIDA** (`D.55`)

**Ninguna de las cuatro guardas de DATO esta en rojo**, y son las cuatro unicas que bloquean:

    $ python forja.py gate              GATE VERDE, 346 nodos, con el cerrojo y censo_no_decrece dentro
    $ python forja.py guiones           BARRIDO VERDE
    $ python tests/test_aceptacion.py   318 pruebas, 0 fallos, 0 errores, en 100,1 s
    fidelidad D.30 de cap_04            0 PUENTE de 156 pasos, contados y firmados por mi

**Asi que nada de lo de abajo te bloquea.** Si te encuentras una guarda de DATO en rojo, **eso si
es averia y se arregla antes de seguir.**

## **EL TECHO DE ESTA VUELTA, EN SUS DOS MITADES** (`d011`, con la mitad en minutos recalculada sobre TU medida)

| unidad | cifra | de donde sale |
|---|---:|---|
| **en pasadas de aduana, y es la mitad que muerde** | **`6`** | una por candidato de la `TAREA 2`, en el mismo acto en que se escribe (`EXTRACTOR.md` 16). **La `TAREA 3` no compra ninguna** |
| **en minutos** | **`57`** | `461,3` s por pasada, que es **tu** media de la vuelta 50 y la que `47.5.c` manda usar, por `6` dan `2768` s; mas `100` de la prueba de aceptacion y `60` de las otras cuatro guardas: `2928` s, `48,8` min, **redondeado arriba a `57` para dejar sitio a que la bandeja crezca** |

**POR QUE `6` Y NO MAS, y es tu propia advertencia de `LL.4.c` la que lo fija:** cada ficha que
entra en la bandeja sube la poblacion del barrido, y tus tres pasadas de hoy la vieron pasar de
`391` a `393`. **Seis candidatos la dejan en `50`**, y por eso el techo no se estira. **Si una
pasada se desmanda, cierras corto en ese candidato y lo declaras con su cifra** (`EXTRACTOR.md`
12.4). Y si sobra turno, **no lo gastas escribiendo un septimo**: lo devuelves.

---

## TAREA 1. **LOS REGISTROS, Y DENTRO DE ELLOS EL PAGO QUE DE VERDAD CIERRA `d038`**

**Es de registro y de una reparacion de prosa. Ninguna guarda de DATO esta en rojo, asi que no
bloquea.**

**1.a.** Recoge sin reabrirlo lo que la `ACTA 49` adjudica: las cinco filas de `49.5` y las cinco
de *lo que te adjudico A FAVOR*. **No las rediscutas.**

**1.b.** Anota tu caida de `CIFRA PUBLICADA`. **Esta en `1 de 2`, que es el penultimo escalon.** La
lees de `python forja.py credito`, **no la tecleas**, y **no la discutes**: esta medida con su
instrumento en `49.4.a`. Y las dos de prosa que no acumulan, igual.

**1.c. PAGA `d044`, QUE ES LA REAPERTURA DE `d038`, Y ESTA VEZ SACANDO LA CITA DEL OBJETO QUE
MIDE.** El pago anterior cambio el comando y conservo el mecanismo; **elegir un comando mas fino no
cierra esto**, porque cualquier cadena escrita dentro de la ficha acaba dentro de la poblacion que
el comando barre. Lo que si lo cierra:

- **dentro de la ficha de `P38` queda la AFIRMACION, con sus dos ids escritos**
  (`decir_no_trabajo_excede_capacidad` y `usar_calendario_herramienta_planificacion_produccion`) y
  **sin ningun comando que se barra a si mismo**;
- **el comando vive fuera de la bandeja**, en tu reporte o en el registro, con su salida pegada;
- **por correccion declarada y sin borrar** ni la linea vieja ni la del pago de la vuelta 50
  (manual principio `6`);
- **y lo compruebas despues de escribirlo, no antes**: corres el `grep` **sobre el arbol ya
  corregido** y pegas lo que da. **Esa es la leccion entera de `49.4.a`, y te la pido en el acto en
  que puede volver a morderte.**

**1.d.** Lee `python scripts/deuda.py` y di que haces con las cuatro nuevas (`d044` a `d047`).
**`d047` es mia y de maquinaria**: `D.45` nos deja fuera a los dos, y solo se cita.

## TAREA 2. **`cap_05` ABRE POR SU PRIMER TRAMO: SEIS CANDIDATOS, Y EL CORTE VA FIJADO DESDE AQUI**

**Tu propuesta `3` de `LL.5.k` la tomo, y esta es la razon escrita:** `cap_05` da `26` nodos contra
un techo de `15`, **medidos por ti ANTES de empezar**, que es lo que `cap_04` no tuvo. `12.4`
autoriza cerrar corto sobre la marcha; **planificar el corte sale mas barato y deja la linea del
tramo escrita desde el principio.**

**LO QUE MINAS HOY, tomado de tu propia tabla de `LL.4.b` y de ningun otro sitio:**

| pieza | tramo | nodos | que es |
|---|---|---:|---|
| `P6` | `L21 a L21` | `1` | infundir regularidad a la reunion de proceso |
| `P7` | `L23 a L23` | `1` | **cabeza de serie**: las tres clases de reunion de proceso |
| `P11` | `L33 a L35` | `1` | cada cuanto se tiene el uno a uno |
| `P12` | `L37 a L39` | `1` | cuanto dura y donde |
| `P13` | `L41 a L41` | `1` | la reunion es del subordinado |
| `P14` | `L43 a L43` | `1` | que se trata en ella |
| | | **`6`** | |

**LO QUE NO TOCAS HOY, y lo digo para que el corte sea una decision y no un descuido:** `P15` a
`P20`, que son los `6` que le quedan al uno a uno; `P26` a `P28`, la reunion de personal; `P31` a
`P35`, la revision de operaciones; y `P38` a `P42` mas `P45`, la reunion de mision. **Son `20`
nodos, y `6` mas `20` son los `26` de tu tabla.** Van a las vueltas siguientes por las secciones
del propio libro. **No los adelantas aunque sobre turno.**

**COMO SE ESCRIBE CADA UNO, y no hay atajo:**

- **la frontera dentro del nodo ANTES de cortar**, con `cero frontera interna` o con el prestamo
  **declarado**. Esto ultimo es `d046` y sale de tu `P41`: si un paso resuelve su referente con un
  tramo vecino, **se dice**, aunque la regla lo autorice;
- **las palabras del tramo son las que `LL.4.b` publica** y las recomputas para comprobar que las
  reproduces, como hiciste en `LL.2.d`. **Si tu recuento discrepa, paras y lo traes**;
- **fidelidad `D.30` paso a paso, con su `sed` pegado**, y los puentes que estuviste a punto de
  escribir declarados dentro de la ficha;
- **aduana en el MISMO acto**, uno por vez, con su reloj (`EXTRACTOR.md` 16);
- **CERO INSERCIONES.** La puerta de `D.39` mide `False` para este libro y `cap_05` no cierra el
  lote 7, que tiene `18` capitulos. **Mide la puerta tu, no la heredes de este encargo.**

## TAREA 3. **`d045` Y `d046`: DOS CORRECCIONES DE PROSA, CERO PASADAS DE ADUANA**

**Adjudicado aqui, con la misma razon que la vuelta 50 uso y que se cumplio:** un cambio que no
toca un paso, ni una atribucion, ni un titulo, **no mueve un vecino**, y comprarle una pasada de
`461,3` s seria gastar el techo sin comprar medida. **Tu propio `LL.3.d` lo midio: `9` de `9` con
solo `resumen_teorico` tocado.**

**3.a. `d045`, la etiqueta de la arista.** `preparar_respuestas_estandar_interrupciones_repetidas`
declara `D.29` y `buscar_regularidad_bloques_iguales_trabajo_mando` declara `D.37` **la misma
relacion con la misma cabeza**. **La tuya es la buena y te la firmo**: `D.37` ata la cabeza con las
partes que **la cabeza NOMBRA**, y la cabeza nombra tres vias (el ritmo, la palanca y la mezcla);
los dos nodos son **medios** de la primera. **Corriges la ficha de `P39` por correccion declarada y
sin borrar**, y dejas escrito el motivo dentro de ella. **No tocas la tuya**, que ya esta bien.

**3.b. `d046`, el prestamo sin declarar de `P41`.** Su paso `1` escribe *porque hay formas mejores
que esconderte* y `L315` abre con `There are better ways` **sin decir mejores que que**: lo dice
`L313`, que es la pieza `P40` con cero nodos. **Adjudico que NO es caida** (manual 3.5: el material
de un tramo de cero entra **nombrado dentro** del nodo de su doctrina, que es exactamente lo que tu
mismo aplicas en `LL.4.d` para los cinco casos de `cap_05`). **Lo que falta es decirlo**: la ficha
afirma `EL TRAMO ENTERO ES DE ESTE NODO: cero frontera interna` y toma material de fuera.
**Correccion declarada dentro de la ficha, sin borrar, nombrando `L313` y la regla.**

**3.c.** Al cerrar la tarea, **las dos guardas de una linea** (`gate` y `guiones`) sobre el arbol
con las correcciones dentro. Es lo unico que pueden certificar de una correccion de prosa: **que no
rompiste una ficha.**

## TAREA 4. **EL CIERRE, CON LAS MISMAS PIEZAS DE SIEMPRE**

- **las cinco guardas** (`gate`, `guiones`, las `318` pruebas, el tallado y el censo), corridas y
  pegadas;
- **la tabla `D.52`** con su colision de `d030` pagada a mano por septima vez y su sello
  `hash-object`. **Y esta vez el comando que pegues nombra el COMMIT con su hash, no `HEAD`**: es
  `d047`, y `HEAD` deja de reproducir en cuanto lo mueves;
- **el estado recomputado al cierre**, no copiado de la apertura. **Lo que predigo:**
  `cuarentena/grove_high_output/` pasa de `44` a **`50`**; `dataset/nodos.jsonl` sigue en **`346`**;
  `bitacora/VEREDICTOS.jsonl` en **`740`**; `config/pares_mutuos.jsonl` en **`1`**. **Las tres
  ultimas son la caida que buscar**: si se mueve una, es que entro un nodo y la puerta esta cerrada;
- **`PASOS INVENTADOS POR CAPITULO` con su fila**, por capitulo y no como media, con numerador y
  denominador. **`cap_05` estrena fila y `cap_04` cierra en `156` pasos con `0` PUENTE**;
- **la linea del tramo con su reloj**, y **la media por pasada recalculada**, que es la que la
  vuelta 52 usara. **Publicala con el numero de vecinos de cada pasada al lado**, que es tu propia
  propuesta `1` y la tomo: `639,0` con `2` vecinos y `335,0` con `7` dicen que la media sola no
  explica nada;
- **la deuda recomputada**, con la lista de lo que queda abierto **impresa del instrumento y no
  tecleada por ti**, como hiciste en `LL.5.h`;
- **tus discutibles marcados ANTES de saber si aciertas.**

---

## LO QUE NO HACES EN ESTA VUELTA

- **No insertas.** La puerta de `D.39` mide `False` para `grove_high_output` y el lote no cierra.
  **Meter un nodo antes seria caida de dato**, no un adelanto.
- **No saltas a `cap_06`** aunque `forja.py tablero --puedo` te mande continuar desde el capitulo
  siguiente al ultimo minado: **`capitulos_minados` cuenta capitulos que dieron al menos UN
  candidato**, y `cap_05` va a quedar en `6` de `26`. Es `d028`, es la misma trampa de siempre,
  **la publicas entera y no la obedeces.**
- **No reabres la frontera de `cap_05`.** Usas la que `LL.4.b` publica. **Si tu recuento de palabras
  discrepa de ella, paras y lo traes**: eso seria que la frontera esta mal y es otra vuelta.
- **No adelantas los `20` nodos que este encargo deja fuera**, aunque sobre turno.
- **No tocas `src/`, `scripts/`, `tests/`, el banco, el arnes ni los protocolos** (`D.45` y la
  moratoria de `EXTRACTOR.md` 13). **Correr una prueba no es tocarla.**
- **No pagas `d047`, `d037`, `d028`, `d029`, `d030`, `d022`, `d020` ni `d033`**: son maquinaria y
  `D.45` te las veda. Se citan y ya.
- **No abres doctrina.** La cola sigue congelada en `11` (`D.56`). Si te encuentras una pregunta
  nueva, **registrala en tu reporte con su medida y dejala ahi**, como hiciste en `LL.2.h` y
  `LL.5.k`, que es lo que hay que hacer.
- **No cambias un paso para bajar una senial.** Lo escribiste tu en `LL.2.h` y es doctrina de la
  casa: engordar el paso `4` de `P42` para complacer un umbral seria escribir lo que el libro no
  escribe.

---

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.
