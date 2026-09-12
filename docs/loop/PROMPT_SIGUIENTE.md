# ENCARGO DE LA VUELTA 18: **CERRAR LA 17 ANTES DE ABRIR NADA**, EL NODO QUE SE DEBE, Y `cap_08` A `cap_10` A TRES POR VUELTA

*Escrito por el **auditor** al cerrar la **ACTA 17** (`docs/loop/ACTA_AUDITOR.md`, la
seccion que abre con `# ACTA 17`) **y reescrito con las cuatro decisiones del fundador del
12 sep 2026**, archivadas en
`docs/loop/paradas/2026-09-12-la-fase-ciega-lee-el-acta.md`. Sede del auditor por
`AUDITOR_FORJA.md` 5.6.*

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO QUE LA PARADA DEJA DECIDIDO, EN CINCO LINEAS

- **LA PARADA FUE DEL AUDITOR Y NO TUYA.** Su racha propia llego a 3 de 3 con un
  `REMEDIO ROTO` que se escribio el mismo. **Tus tres rachas siguen lejos:** `CLASE`
  **0 de 2**, `CIFRA PUBLICADA` **0 de 2**, `REPORTE` **0 de 3**.
- **LA RACHA DEL AUDITOR SE REINICIA A 0 DE 3, Y CON CONDICION MECANICA:** `D.40`, **LO
  QUE UN AUDITOR LE DEJA AL SIGUIENTE LO ENTREGA EL ARNES, NO LA MEMORIA.** Ya corre:
  `src/herencia.py`, cableada en `apertura_ciega()`, con su caso positivo en el banco de
  pruebas del arnes y 7 pruebas de unidad. **A ti no te pide nada**, pero te lo digo
  porque el arnes ahora puede **pararse antes de que el acta se escriba**, y eso sale en
  el log.
- **EL TRAMO BAJA A TRES CAPITULOS POR VUELTA** (decision 2). **No lo bajo el freno de
  `PASOS INVENTADOS`**, que no se disparo (peor unidad `cap_04` **6,25**, tope 10): lo
  bajo `EXTRACTOR.md` 12.4, **cumplido por sus dos mitades** en la vuelta 17.
- **Y CON UNA REGLA DE PRECEDENCIA NUEVA QUE MANDA SOBRE EL TRAMO: EL TECHO DE
  CANDIDATOS POR VUELTA MANDA SOBRE EL DE CAPITULOS.** Esta escrita en
  `EXTRACTOR.md` 12.4, en mi `8.1` y en `ORDEN_DE_LOTES.md`. **Leela antes de la TAREA 3**,
  porque esta vuelta la vas a usar.
- **El lote 4 sigue ABIERTO y no se inserta nada de el** (`D.39`: solo se inserta un lote
  **CERRADO**).

---

## TAREA 0: **CIERRA LA VUELTA 17. VA PRIMERA Y NO SE SOLAPA CON NADA**

*Decision 3 del fundador, literal: **LA VUELTA 17 SE CIERRA ANTES DE ABRIR NADA.***

**El trabajo de la 17 esta hecho y esta bien. Lo que no esta es EN SU SEDE.** Mi `ACTA 17`
1.3 lo midio al abrir mi turno:

    $ git status --porcelain
      24 ??  cuarentena/scott_radical_candor/   (los 24 candidatos de cap_07)
       5 ??  .frag_disc.md .frag_t4b.md .frag_t4c.md .frag_t4d.md .frag_t4e.md
       1 M   docs/loop/REPORTE.md

**0.a. ABSORBE LOS CINCO `.frag_*.md` EN `REPORTE.md`, CON SUS ONCE DISCUTIBLES.** Un
fichero `.frag_*.md` **no es sede de nada** (`EXTRACTOR.md` 14). Los once discutibles de
`.frag_disc.md` **yo los trate como marcados y lo razone en mi `3.0`**: su marca de tiempo
es de las 04:49, **antes** de que mi fase ciega empezara a las 04:50, y mi apertura declara
que no los leyo. **Esa absolucion vale para la metrica de la 17 y no se repite:** lo que se
marca en la 18 se marca **dentro de `REPORTE.md`**.

**0.b. COMMITEA LOS 24 CANDIDATOS DE `cap_07`, UN COMMIT POR CAPITULO**, que es lo que el
encargo de la 17 ya pedia. Son todos de `cap_07`, comprobado por las dos medidas:

    $ git ls-files --others --exclude-standard cuarentena/scott_radical_candor/ | wc -l   ->  24
    $ grep -l "cap_07" cuarentena/scott_radical_candor/*.json | wc -l                     ->  24
    (los dos conjuntos comparados: identicos)

> **UNA CIFRA MIA QUE TE TRAIGO PARA QUE LA ADJUDIQUES TU, Y VA CONTRA MI** (`D.38.3`, y
> mi `5.5`): **mi propia `ACTA 17` dice `25 candidatos` en su seccion 5.2 y `24` en su
> 1.3.** El fundador firma **24** y las dos medidas de arriba dan **24**. **Remidelo tu,
> con tu instrumento pegado**, y publica cual de las dos cifras de mi acta es la falsa.
> **No cambia ninguna decision** (las dos pasan del techo de 15), **pero es cifra publicada
> en acta mia y la sede de `CIFRA PUBLICADA` la cubre.**

**0.c. ARREGLA LAS DOS CABECERAS DE PUNTERO** (`ACTA 17` 4.5). **Las lineas citadas son
buenas; lo que dice de menos es la cabecera:**

| candidato | declara | pero sus pasos citan |
|---|---|---|
| `crear_espacio_seguro_madurar_ideas_nuevas` | `L181-195` | `L177` y `L179` |
| `establecer_credibilidad_pericia_humildad` | `L349-357` | su `P1` cita `L313` |

**NO ES CAIDA DE NINGUNA ESPECIE y la sede lo decide** (mi `5.2`): vive en el
`resumen_teorico` de un candidato de `cuarentena/`, que no es sede de `CIFRA PUBLICADA`.
**Se corrige antes de insertar**, y esta vuelta no inserta: **se corrige igual, porque
insertar con la cabecera corta es lo que la deja dentro del grafo.**

**0.d. DEJA EL ARBOL LIMPIO.** `git status --porcelain` sin nada tuyo antes de abrir la
TAREA 1. **Los artefactos del arnes no se barren** (`D.33`).

> **POR QUE VA PRIMERA Y SOLA:** la vuelta 17 produjo trabajo bueno que no cabia, y esa es
> exactamente la parada madre de `EXTRACTOR.md` 12.4 (la bateria sin techo, 5 sep 2026).
> **Cerrar lo de ayer antes de abrir lo de hoy no es tramite: es lo unico que impide que la
> 18 herede el mismo problema.**

---

## TAREA 1: LOS REGISTROS, Y LAS SEDES QUE CAMBIARON

**1.a. LEE LA `ACTA 17` ENTERA** y recoge sus adjudicaciones **sin reabrirlas**, salvo que
encuentres un hecho nuevo; si lo encuentras, **lo traes con su medida y no lo resuelves
copiando** (`EXTRACTOR.md` 5).

**1.b. LEE LA PARADA ARCHIVADA**,
`docs/loop/paradas/2026-09-12-la-fase-ciega-lee-el-acta.md`, **y las cuatro decisiones
literales de su cabecera.** Es doctrina firmada y manda sobre todo lo que yo escriba aqui.

**1.c. LAS SEDES DE DOCTRINA QUE CAMBIARON, para que no las midas contra su version
vieja:**

| sede | que cambio |
|---|---|
| `docs/BANCO_DE_REGLAS.md` | **`D.40` nueva**, con su mesa de evidencia y su caso positivo |
| `docs/loop/EXTRACTOR.md` 12.4 | **la regla de precedencia de los dos techos**, escrita dentro del punto 4 |
| `docs/loop/ORDEN_DE_LOTES.md`, `docs/CALIBRACION_D4.md`, `AUDITOR_FORJA.md` 8.1 | **el tramo del lote 4 baja de CUATRO a TRES**, con correccion declarada en las tres |
| `src/herencia.py`, `forja.py`, `orquestador_forja.sh`, `tests/` | **el instrumento de `D.40`**, su cableado, su caso positivo (escenario 14b del arnes) y 7 pruebas de unidad |

**1.d. Y LO QUE NO TIENES QUE HACER, que lo digo para que no lo busques:** las cuatro
cifras de la vuelta 16 ya las remediste y yo las confirme (`ACTA 17` 2.1); **ninguna se
reabre.**

---

## TAREA 2: **EL NODO QUE SE LE DEBE A `cap_07`**

*Decision 4 del fundador, literal: **ADJUDICACION AUTORIZADA.** Adjudicada por mi en la
`ACTA 17` 4.1 y firmada por el fundador.*

> **A `L155` A `L163` DE `cap_07` (`Adapt to a culture of listening`) SE LE EXTRAE SU
> NODO.**

**LA RAZON, Y NO ES UNA SEÑAL: ES UNA LECTURA** (`D.19`, mi `6.2`). El mismo capitulo
extrajo **dos retratos identicos en forma** y dejo el tercero fuera:

| tramo | que es | salio |
|---|---|---|
| `L377`, *Don't waste your team's time* (Sheryl) | retrato en pasado, sin un imperativo en el cuerpo, rotulo imperativo, actos nombrados uno a uno | **NODO** `proteger_tiempo_equipo_jefe`, 9 pasos |
| `L415`, *Burnout* (Costolo) | lo mismo | **NODO** `cuidarse_agotamiento_centro_rueda`, 7 pasos |
| `L155`, *Adapt to a culture of listening* (Astrid Tuminez) | **lo mismo** | **fuera, por ser caso** |

**`D.27` no los separa**: en los tres el libro pone inventario de **medios**; en los tres
son actos y no metas ni fines (restriccion 1); en ninguno hay adjetivo de adecuacion en el
sitio del criterio (restriccion 2). **Y el caso ajeno tampoco los separa**, porque esta
casa admite `TRANSCRIPCION DE CASO` con el caso nombrado dentro del paso, **y tu propio
`cuidarse_agotamiento` lo hace con Costolo dentro de sus `P4` a `P7`. LA CONSISTENCIA ES LA
REGLA.**

**LOS CINCO MEDIOS QUE EL LIBRO NOMBRA UNO A UNO**, y que son los pasos: meses
escuchando, citas sueltas, acudir a los actos publicos, no encadenar gente seguida, comida
de verdad cuando invitas tu. **Con Astrid nombrada dentro de los pasos que la usen.**

> **LO QUE ESTO NO ES, y lo repito porque es la mitad que vale mas que el nodo:** **no es
> caida de ninguna especie** (ninguna regla obliga a la exhaustividad, mi `ACTA 15` 2.9) y
> **no ensancha `D.27`: lo aplica igual a tres tramos iguales.** Tu marcaste esta pieza
> como discutible **sabiendo que iba contra ti**, y eso es lo contrario de una caida.

**Y LO QUE SIGUE ESPERANDO AL CIERRE DEL LOTE 4, sin cambios:** las **cuatro colas de
arista** en su bloque titulado (`REPORTE.md` `L.4.d`, `D.29`) y las **cinco lecturas
`SANO` sin sede**. **`D.39` solo abre la insercion de un lote CERRADO**, y el lote 4 esta
abierto: **no les inventes sede.** Se repiten al cierre de tu reporte, como hasta ahora.

---

## TAREA 3: EL LOTE 4, `scott_radical_candor`. **`cap_08` A `cap_10`, A TRES POR VUELTA**

**EL TRAMO SON TRES CAPITULOS**, y estos son:

| unidad | rotulo | palabras de cuerpo |
|---|---|---:|
| `cap_08` | `Relationships` | 6.140 |
| `cap_09` | `Guidance` | **17.482** |
| `cap_10` | `Team` | 8.976 |

*Las tres salen de `sed -n '8,$p' <fichero> | wc -w`, que es la medida de CUERPO de esta
casa. **Remidelas tu antes de publicarlas**: una cifra de mi encargo no es fuente de una
cifra tuya (`EXTRACTOR.md` 5).*

> ### **Y AHORA LA REGLA QUE MANDA SOBRE ESA TABLA, QUE ES NUEVA Y ES DE ESTA VUELTA**
>
> **EL TECHO DE CANDIDATOS POR VUELTA MANDA SOBRE EL DE CAPITULOS** (`EXTRACTOR.md` 12.4,
> decision del fundador del 12 sep 2026, punto 2).
>
> **SI UN SOLO CAPITULO PASA DEL TECHO DE CANDIDATOS, LA VUELTA CIERRA EN ESE CAPITULO Y
> LO DECLARA.** Los capitulos que le quedaban al tramo **pasan a la vuelta siguiente**. No
> se parte un capitulo en dos vueltas y **no se estira el tramo para completar el numero.**
>
> **COMO SE DECLARA, en tu reporte y en una linea:** *la vuelta cierra en `cap_NN` con N
> candidatos, por encima del techo de 15; los capitulos restantes del tramo pasan a la
> vuelta siguiente.*
>
> **UNA VUELTA QUE CIERRA CORTO Y NO LO DICE NO ESTA APLICANDO ESTA REGLA:** se esta
> quedando corta sin motivo escrito, **y eso si es caida de la especie `REPORTE`.**

**TE DIGO DONDE ESPERO QUE MUERDA, Y ES UNA LECTURA MIA QUE PUEDES TUMBAR CON TU MEDIDA:**
**`cap_09` pesa 17.482 palabras de cuerpo, mas que `cap_07` (13.678), que dio 24
candidatos.** Si la densidad se parece, **`cap_09` solo ya pasa del techo.** **No te estoy
diciendo que pares en `cap_09`: te estoy diciendo que la regla existe para eso y que no
hace falta que me preguntes.** Cierra donde el techo te diga y **declara donde cerraste.**

**EL FRENO DE `PASOS INVENTADOS` SIGUE APARTE Y ENTERO**, y se publica igual: **fila por
capitulo mas total del lote**, y **la escalada se decide sobre el peor capitulo, no sobre
el promedio** (mi `8.2`). Tope **10**. **Que este otro techo se dispare no baja el volumen
del lote: el volumen lo baja su propia cifra.**

**LO DE SIEMPRE, que no cambia:** la fuente canonica ya esta; **informe en seco antes de
insertar nada**; **un candidato por vez y en el orden del libro**; las aristas que la señal
no levanta **se declaran en la misma vuelta en que insertas las partes** (`D.29`, `D.37`);
y **un capitulo entero en la misma familia no es duplicado, es un libro que trata un tema**
(`EXTRACTOR.md` 12).

---

## SON CUATRO TAREAS Y EL TOPE SON CINCO

**Y la TAREA 0 no se negocia con las otras tres:** si el cierre de la 17 se come la vuelta,
**la vuelta se cierra ahi y lo declaras.** Es la misma regla de precedencia de la TAREA 3
aplicada al principio en vez de al final: **lo que no cabe, no cabe, y lo que se declara no
es una falta.**

## LAS PARADAS

**Las de `AUDITOR_FORJA.md` 3 estan enteras y no las toca nada de este encargo.** Lo unico
nuevo es que **el arnes puede detenerse antes de que se escriba el acta** si la apertura
ciega no declara su herencia (`D.40`). **Esa parada es del auditor, no tuya**, y sale en
`docs/loop/loop.log` con lo que falta nombrado.
