# ENCARGO DE LA VUELTA 48: **TERMINAR `cap_04` HASTA DONDE LLEGUE EL TECHO, Y EL TECHO YA SE CUENTA EN PASOS**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor en la `ACTA 46`. Modo
austero (`D.47`): no repito lo que el registro ya dice.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: **LA VUELTA 47 CERRO ENTERA Y SU CIERRE CORTO ES CORRECTO**

**Segunda tanda seguida sin una sola caida que acumule.** `CLASE`, `CIFRA PUBLICADA` y
`DATO MOVIDO` salen **LIMPIAS**, y `REPORTE` se queda en `0 de 3`.

| lo que te verifique | como |
|---|---|
| **el cierre corto** | `EXTRACTOR.md` 12.4 dice que una vuelta que cierra en un capitulo **y no lo dice** es caida de `REPORTE`. **Tu lo dijiste con las tres piezas**: el numero (`6` de `8`), el reloj (`4090` s contra `4020`) y los que quedan nombrados por su tramo. **No hay caida** |
| **el `22` de la frontera** | lo recompuse **hoy** y no lo cite: `44` filas, `8846` contra `8846`, `0` sin cubrir, `0` solapes. **Era lo que mi propia apertura se dejo a deber** |
| **los `45` pasos y el `0` PUENTE** | conte el denominador de las `14` fichas (`95` pasos en `cap_04`) y **FIRMO tu `0` de `95`** |
| **los seis relojes y los seis informes** | cada intervalo de sus dos marcas, cada saldo de aduana (`2` `ENTRARIA`, `4` `BLOQUEARIA`, `0` `CAERIA`, `9` vecinos) y **tus nueve pares de cola al milesimo** |
| **tus trece cifras derivadas** | `681,7`, `90,9`, `80,9`, `12,4`, `34,8`, `4900`, `95,3`, `44` pasos, `4090` contra `4020`. **Me salen todas** |
| **la guarda que declaras mordiendo** | la mordi **por mutacion** y muerde; y tu instrumento de tanda **reproduce su salida byte a byte** contra la que pegaste |
| **tus seis discutibles marcados** | **se sostienen los SEIS** (`ACTA 46` `46.4`). Dentro del marcado `6` de `6`, fuera del marcado `0` caidas de clase |

**Y DOS COSAS QUE HICISTE BIEN Y NO TE APUNTASTE:** la correccion de la ficha de `P27`
**anade `808` caracteres y no borra ni uno** del texto viejo, que es manual principio 6
cumplido a la letra y lo comprobe por diferencia; y los cinco sitios de tentacion de `II.3.a`
son **lo mejor que ha producido esta metrica**, porque una cifra de cero no prueba que no
hubiera tentacion.

## Y LO SEGUNDO: **LO QUE LA `ACTA 46` CARGA, PARA QUE NO TE LLEGUE DE OIDAS**

| | |
|---|---|
| **tus dos caidas son de PROSA y NO acumulan** | el superlativo de `II.3.b` (*el tramo mas rico de la tanda, `P27` con `347`*, cuando `P24` tiene `356` y el tramo entero de tu candidato `1` tiene `429`) y el *el mas proximo* de `II.2.f`. Las dos en prosa de acompaniamiento, y `5.2` dice que ahi no acumula |
| **el fondo de la segunda sigue siendo bueno** | la senial `2` levanto un pariente legitimo que tu lectura no habia visto. **Lo falso es el ranking, no el hallazgo**: el instrumento de la casa da que el que SI escribiste gana en `2` de las `3` seniales |
| **la que te adjudico a favor** | la arista hacia un id que todavia no existe **no es caida**, y te digo por que en `46.5.b`. Lo que si hace es dejarla fragil, y la vuelta 48 la paga sin coste propio |
| **dos deudas nuevas, anotadas por mi y NO tuyas de pagar hoy** | `d030` y `d031`. **`D.55`: la deuda no bloquea la produccion** |
| **una medida mia que NO adjudico** | `13` de tus `45` pasos abren declarando y no ejecutando, y de esos `13` tu marcaste `5`. **Esta en `46.7`, medida, y se queda ahi**: `D.56` congela la doctrina y `6.3` dice que mover la vara es decision del fundador. **No cambies nada por esto.** Te lo digo para que lo sepas, no para que actues |

---

## **CERO TAREAS BLOQUEANTES EN ESTE ENCARGO, Y LO DIGO CON LA MEDIDA** (`D.55`)

**Ninguna guarda de DATO esta en rojo**, y son las cuatro unicas que bloquean:

    $ python forja.py gate            GATE VERDE, 346 nodos
    $ python forja.py guiones         BARRIDO VERDE
    $ python tests/test_aceptacion.py 318 pruebas, 0 fallos, 0 errores
    fidelidad D.30 de cap_04          0 PUENTE de 95 pasos, releidos por mi uno a uno
    cerrojo y censo no decreciente    dentro del gate, verdes

**Asi que nada de lo de abajo te bloquea.** Si te encuentras una guarda de DATO en rojo, eso
si es averia y se arregla antes de seguir.

---

## TAREA 1. **LOS REGISTROS DE LA `ACTA 46`**

**Cerrada cuando las cuatro filas esten hechas y dichas. Es de registro, no de reparacion.**

### 1.a. **La correccion declarada del superlativo de `II.3.b`**

Escribe **al lado de tu `II.3.b`**, sin borrar el texto viejo, que `P27` **no es el tramo mas
rico de la tanda**: lo es `P24` con `356` palabras, y el tramo entero del candidato `1` es
`P21` mas `P24`, `429`. **La cifra `347` era cierta; el superlativo no.** Pega debajo la lista
ordenada entera de los siete tramos, que es lo que un superlativo necesita para publicarse
(`D.38.3` ensanchada). **La tienes en `ACTA 46` `46.6.a`, salida de `.v47aud/44_tramos.py`.**

**Y DI TAMBIEN LA SEGUNDA MITAD**, que es la que de verdad importa: la frase *los `23` tramos
que la frontera dejo en cero son justamente los pobres* **la sostiene tu tabla de frontera**,
donde cada cero lleva su regla escrita, **y no la sostiene la medida en palabras que el
parrafo ofrece dos renglones despues**: `199,7` de media los de cero contra `202,6` los que
dan nodo, y los dos tramos mas ricos del capitulo (`P5` con `674` y `P2` con `530`) dan cero.
**Separa la medida de la conclusion y marca la conclusion con `LECTURA`.**

### 1.b. **La correccion declarada del `el mas proximo` de `II.2.f`**

Al lado del texto viejo, sin borrarlo: **el pariente que tu ficha SI escribio,
`elegir_inspeccion_barrera_monitorizacion`, gana en `similitud_texto` (`0,266` contra `0,226`)
y en `paso_contra_nodo` (`0,491` contra `0,435`).** El otro gana solo en `familia_id`, que
compara la cadena del id, **y tu propio parrafo ya dice que la familia la comparten porque
comparten el objeto en el id.** `AUDITOR_FORJA.md` 6.2 con `D.19` detras: **una proximidad no
se adjudica citando una senial.** La salida esta en `46.6.b`.

**LO QUE NO CAMBIA:** la arista sigue declarada y se cablea el dia de la insercion. **Lo que
se corrige es el ranking, no el hallazgo.**

### 1.c. **Las dos deudas nuevas, DICHAS y NO PAGADAS**

| id | que es | por que no la pagas hoy |
|---|---|---|
| **`d030`** | `scripts/tabla_de_cierre.py --escribir` escribe siempre en la misma ruta viva, asi que cada cierre deja en rojo la tabla de la vuelta anterior. **Tercer ejemplar seguido.** Es distinto de `d009` y de `d022` | **es maquinaria**, y la moratoria de `EXTRACTOR.md` 13 con `D.45` te dejan fuera. **Tu remedio a mano es el correcto y lo vuelves a usar hoy**: archivar la vieja y sellarla con `git hash-object` |
| **`d031`** | retocar una linea de un `resumen_teorico` en cuarentena cuesta la aduana entera: `578` s medidos, lo mismo que un candidato nuevo | idem: es maquinaria. **La medida es tuya y por eso la anote con tu cita** |

### 1.d. **Lo adjudicado en la `ACTA 46` se recoge y no se reabre**

Las cuatro adjudicaciones son `46.5.a` (tu cierre corto es correcto), `46.5.b` (la arista al id
inexistente no es caida, y su arreglo va en la TAREA 2), `46.5.c` (el techo en minutos se
estima sobre pasos, y lo veras aplicado abajo) y `46.5.d` (el volumen no sube). **Recogidas,
no reabiertas.**

---

## TAREA 2. **`cap_04` SIGUE ABIERTO EN `8` DE `22`: LOS CINCO SIGUIENTES, Y NO SE TOCA `cap_05`**

> ### **LA TRAMPA DEL TABLERO SIGUE VIVA, Y HOY SE COBRARIA `8` NODOS**
>
>     $ python forja.py tablero --puedo grove_high_output
>       ... se continua desde el capitulo siguiente al ultimo minado (cap_04) ...
>
> **NO SALTES A `cap_05`.** `capitulos_minados` mide *capitulos que produjeron al menos UN
> candidato*. **`cap_04` esta en `14` de sus `22` nodos**, contado hoy por mi de las propias
> fichas y con la frontera recompuesta al digito. Esta anotado como `d028` y **`D.45` me
> impide encargarte el arreglo del codigo: lo que hago es esta linea.**

**LOS CINCO DE ESTA VUELTA, EN EL ORDEN DEL LIBRO Y CON SU TRAMO**, sacados de tu propia
frontera de `HH.2.c`:

| # | tramo | lo que el tramo trae |
|---:|---|---|
| 1 | `P34a` (`L273` a `L285`) | el calendario como herramienta de planificacion de la produccion |
| 2 | `P34b` (`L273` a `L285`) | la segunda responsabilidad del calendario: decir que no al trabajo que excede tu capacidad |
| 3 | `P36` (`L289`) | el inventario de proyectos discrecionales de materia prima, con su criterio propio y su contraste |
| 4 | `P38` (`L293` a `L301`) | seis a ocho subordinados, con la guia de medio dia por semana y el caso del reparto estrecho |
| 5 | `P39` (`L303` a `L307`) | la regularidad: los mismos bloques de tiempo para actividades iguales, coordinados con los demas |

**QUEDARAN TRES PARA LA VUELTA 49**: `P41`, `P42` y `P44`. **No los mines hoy aunque te sobre
turno**: `D.43` dice que el coste del instrumento es motivo para pedir MENOS candidatos, no
para correr dos aduanas a la vez.

### 2.a. **EL TECHO, Y SU MITAD EN MINUTOS YA SE CUENTA EN PASOS** (`d011`, adjudicado en `46.5.c`)

| | |
|---|---|
| **en candidatos** | **`5`** |
| **en PASOS** | **`44`**, y es la mitad que muerde. Sale de tu propia medida: `67` minutos son `4020` s, y a los `90,9` s por paso que mediste esta vuelta dan `44,2` pasos |
| **en minutos** | **`67`**, el mismo de siempre, para que se pueda cruzar con el anterior |
| **la estimacion de los cinco** | tus dos borradores traen `7` y `10` pasos, y los otros tres a los `7,5` por candidato de esta vuelta dan `22,5`: **unos `40` pasos, que caben en `44`** |
| **si no cabe** | **cierras corto AL PASO, lo declaras con el numero y el reloj, y nombras los que quedan por su tramo.** Es lo que hiciste en `II.2.h` y salio bien |
| **si sobra** | **no metes un sexto.** `P41`, `P42` y `P44` son de la vuelta 49 |

**POR QUE EL TECHO CAMBIA DE UNIDAD Y NO ES DOCTRINA NUEVA:** `d011` obliga a que todo techo
mio lleve su mitad en minutos y **no dice de que se estiman esos minutos**. Tu medida es la que
lo decide: entre las dos tandas del mismo capitulo, el coste por candidato subio un `34,8` por
ciento y el coste por paso solo un `12,4`. **La unidad de coste de la aduana es el paso.**

### 2.b. **LA ARISTA QUE HOY APUNTA A UN NODO QUE NO EXISTE, Y QUE ESTA VUELTA PAGA GRATIS**

`identificar_paso_limitante_jornada_desfases` declara una arista hacia
`usar_calendario_herramienta_planificacion_produccion`, **y ese id no vive hoy en ninguna
sede**, comprobado por mi sobre las `894` fichas. **No es caida** (`46.5.b`), pero queda
colgada sin que ninguna guarda lo cante, porque el gate solo mira el grafo.

**Y EL NODO QUE FALTA ES EXACTAMENTE TU CANDIDATO `1` DE HOY.** Asi que:

- **si lo escribes con ese id, la arista se resuelve sola** y lo dices en el reporte con su
  comprobacion pegada;
- **si eliges otro id, corriges la arista de `identificar_paso_limitante_jornada_desfases` por
  correccion declarada**, sin borrar el texto viejo, y **la ficha vuelve a pasar la aduana en
  el mismo acto**, que es lo que manda `EXTRACTOR.md` 16. **Cuenta su reloj aparte**, como
  hiciste con la de `P27`: no es un candidato nuevo y no entra en la media de la tanda.

**Y LA LECCION QUE SI TE PIDO ESCRITA EN LA FICHA NUEVA:** las aristas hacia nodos que aun no
existen **se declaran POR SU TRAMO** (*el nodo que sale de `L289`*) y no por un id inventado de
antemano, porque un id que nadie ha escrito puede no coincidir con el que se escriba.

### 2.c. **LAS REGLAS DE DATO QUE NO CAMBIAN, Y NO LAS REPITO MAS**

- **Un candidato por vez y en el orden del libro**, cada uno por `python forja.py informe` **en
  el mismo acto en que se escribe** (`EXTRACTOR.md` 12.3 y 16).
- **CERO INSERCIONES.** `grove_high_output` no esta en `cerrados_en_extraccion` y `D.39` manda
  que sus candidatos esperen en cuarentena. **Mide la puerta y pega la salida, no la supongas.**
- **La fidelidad `D.30` en el acto de escribir cada paso**, con el parrafo delante. **Tu `0` de
  `95` lo firme yo tras releerlos: no lo bajes de liston.**
- **Las aristas declaradas por lectura van DENTRO de la ficha**, que es donde sobreviven al
  reporte, y se cablean el dia que el lote cierre.
- **No subas el umbral para que la cola de lectura se acorte.** `cap_04` es monotematico y la
  cola larga es el precio.

### 2.d. **DOS COSAS QUE YA SE DE ESTE TRAMO Y TE AHORRAN UNA LECTURA**

- **`P34` trae tu discutible ya marcado dos vueltas seguidas a ciegas**, y esta vez lo escribes
  con el nodo delante: si la primera responsabilidad del calendario merece casa propia, dos
  nodos es lo correcto; si no, tu par seria una compresion de dos y manual 3 punto 4 lo
  prohibe. **Tu propia medida de `II.4.d` dice que la responsabilidad `1` ocupa UNA frase
  (`L281`) sin un renglon que la despliegue y la `2` tiene `L277` entero antes y `L285` entero
  despues.** Dila otra vez con las fichas escritas.
- **`P38` y `P39` traen cifras del libro** (*six to eight*, *half a day a week*). **Son del
  autor y viajan como tales**; lo que no se escribe es una cifra que el libro no da, que es
  justo la tentacion que `d027` tiene abierta desde la vuelta 46.

---

## TAREA 3. **`PASOS INVENTADOS POR CAPITULO`, CON SU DENOMINADOR Y SUS TRES FILAS**

**La fila de los cinco de hoy, la de los `14` ya minados y la de `cap_04` entero**, cada una
con su numerador, su denominador y su por ciento. **El denominador va escrito aunque el
numerador sea cero**, y la fila de los `14` la cuenta tu instrumento de las propias fichas, no
se teclea.

**Y DI OTRA VEZ LOS SITIOS DONDE ESTUVISTE A PUNTO DE ESCRIBIR UN PUENTE**, por su especie de
`EXTRACTOR.md` 15.4, como en `II.3.a`. **Uno lo tienes ya escrito de esta vuelta sin haberlo
minado:** el paso que ibas a poner en `decir_no_trabajo_excede_capacidad` mandando MEDIR la
capacidad, cuando `L277` dice lo contrario. **Ese va con nodo delante.**

**Si encuentras un `PUENTE`, no es una caida**: es la regla funcionando. Se retira o se
reescribe citando el parrafo que no lo dice, y se cuenta.

---

## TAREA 4. **EL CIERRE, CON LAS MISMAS CINCO PIEZAS DE SIEMPRE**

1. **las guardas al cierre**, corridas y pegadas: `gate`, `guiones`, la prueba de aceptacion,
   el tallado `D.41` y el censo `D.42`;
2. **la tabla de cierre `D.52`**, con la colision de la ruta viva resuelta como en `II.4.c`:
   la vieja archivada con su `hash-object` y la ruta viva para la que cierra. **Es `d030` y se
   paga a mano otra vez**;
3. **el estado recomputado al cierre**, no copiado de la apertura;
4. **la linea del tramo con su reloj**, diciendo en que paso o en que candidato cortaste y
   nombrando por su tramo los que quedan;
5. **el tablero y el credito, leidos y no anotados por ti**: esas dos sedes no son tuyas.

**Y LA DECLARACION DE COSTE DE `D.55`**, que esta vuelta no es de saneamiento. **No inventes un
USD**: este repo no tiene instrumento que lo mida. Lo que la regla persigue es **en que se
fue**, y eso lo mides de tus relojes.

**UN AVISO QUE NO ES UNA TAREA:** la ultima vuelta de saneamiento fue la `44`, asi que la `49`
es la quinta desde entonces y **le toca**. Hoy hay `14` deudas pendientes. **No pagues ninguna
en esta vuelta**, pero escribe tu cierre sabiendo que la siguiente abre con ellas.

---

## LO QUE NO HACES EN ESTA VUELTA, DICHO PARA QUE NO HAYA QUE DECIDIRLO SOBRE LA MARCHA

- **No insertas.** La puerta de `D.39` mide cerrada y se mide otra vez.
- **No saltas a `cap_05`.** `cap_04` cierra en la vuelta 49 con `P41`, `P42` y `P44`.
- **No tocas `src/`, `scripts/`, `tests/`, el banco, el arnes ni los protocolos** (`D.45` y la
  moratoria de `EXTRACTOR.md` 13). La vuelta 47 no los toco y lo comprobe por diferencia.
- **No abres doctrina.** La cola esta congelada en `11` (`D.56`). Si te encuentras una pregunta
  nueva, **registrala en tu reporte con su medida y dejala ahi.** Yo hice lo mismo con la mia
  de `46.7` y ahi se queda.
- **No pagas deuda.** Las `14` esperan a la vuelta 49.
- **No cambias la forma de tus pasos por lo que leas en `46.7`.** Es una medida mia y no una
  adjudicacion: mover la vara es decision del fundador (`6.3`).

---

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.
