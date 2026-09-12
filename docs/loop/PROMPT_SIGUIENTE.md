# ENCARGO DE LA VUELTA 21: **`cap_10` ENTERO**, LAS TRES ARISTAS `D.37` DE `L173`, Y EL PAR DE LA LUPA POR LECTURA

*Escrito por el **auditor** al cerrar la **ACTA 20** (`docs/loop/ACTA_AUDITOR.md`, la
seccion que abre con `# ACTA 20`) **y reescrito con las cuatro decisiones del fundador
del 12 sep 2026**, archivadas en
`docs/loop/paradas/2026-09-12-el-artefacto-que-faltaba.md`. Sede del auditor por
`AUDITOR_FORJA.md` 5.6.*

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO QUE LA PARADA DEJA DECIDIDO, EN CINCO LINEAS

- **LA PARADA FUE DEL AUDITOR Y LA DECISION LE DA LA VUELTA A SU CAUSA.** Su tercera
  caida **no era `REMEDIO ROTO`: era `D.33`**, un artefacto de maquina sin exencion
  escrita. El remedio que la pedia (`ACTA 19` `8.1`, *cero guiones en mi mensaje
  final*) **se retira por correccion declarada: capa equivocada.** Su racha queda en
  **0 de 3**.
- **TU VUELTA 20 SALIO LIMPIA** de `CLASE` y de `CIFRA PUBLICADA`, con `cap_09`
  cerrado en **20 de 20** y **272 pasos**, **0 puentes** en los 95 nuevos, y las **39
  filas** de tu frontera de `cap_10` remedidas una a una **al digito**. Tu `REPORTE`
  se queda en **2 de 3** y **no sube**.
- **`D.33` SE ENSANCHA POR PATRON:** `docs/loop/ultimo_*.json` y `loop.log` quedan
  exentos del barrido y del hook, **hoy y los que nazcan mañana.** Ya no hay forma de
  que el volcado de un modelo te deje el arbol en rojo al arrancar.
- **EL INFORME DE LOTE ENTERO YA NO ES TUYO** (`D.41`): lo corre el arnes, sellado, y
  tu **lo citas**. Medido: **156,5 s por candidato**, mas de tres horas para 83.
- **LA POBLACION DEL INFORME ES AHORA GRAFO MAS BANDEJAS** (`D.38.5`): **espera mas
  `BLOQUEARIA` que antes, y no significa que tus candidatos hayan empeorado.**

---

## TAREA 1: LOS REGISTROS, Y **LO QUE CAMBIO DEBAJO DE TI**

**1.a. LEE LA `ACTA 20` ENTERA** y recoge sus adjudicaciones **sin reabrirlas**, salvo
que encuentres un hecho nuevo; si lo encuentras, **lo traes con su medida y no lo
resuelves copiando** (`EXTRACTOR.md` 5).

**1.b. LEE LA PARADA ARCHIVADA**,
`docs/loop/paradas/2026-09-12-el-artefacto-que-faltaba.md`, **y las cuatro decisiones
literales de su cabecera.** Es doctrina firmada y manda sobre todo lo que yo escriba
aqui.

**1.c. LAS SEDES QUE CAMBIARON, para que no las midas contra su version vieja:**

| sede | que cambio |
|---|---|
| `docs/BANCO_DE_REGLAS.md`, `D.33` | **se ensancha POR PATRON**, con su caso positivo |
| `docs/BANCO_DE_REGLAS.md`, `D.38.2` | **se acota**: `REMEDIO ROTO` solo en sustancia de auditoria |
| `docs/BANCO_DE_REGLAS.md`, **`D.38.5` nueva** | la poblacion del barrido es grafo mas bandejas **tambien para la aduana** |
| `docs/BANCO_DE_REGLAS.md`, **`D.41` nueva** | el informe de lote lo corre el arnes y tu lo citas |
| `src/comun.py` | `PATRONES_DE_ARTEFACTO` y `es_artefacto_de_maquina()` |
| `src/informe.py` | la poblacion, y el informe la publica **con su reparto** |
| `orquestador_forja.sh` | el paso propio del informe de lote, con su sello |
| `docs/loop/EXTRACTOR.md` 12 | los dos avisos de arriba, en tu manual |

**1.d. Y UNA CIFRA QUE SE TE DEBE Y QUE NO PUEDES PAGAR TU.** El informe de lote de
los **83** del lote 4 (con su `CHOCAN entre si dentro del lote`) **sigue sin correr**:
el de la vuelta 20 quedo en 480 bytes. **Con `D.41` lo corre el arnes cuando se lanza
con `INFORME_DE_LOTE=cuarentena/scott_radical_candor`.** Si tu prompt trae el fichero
sellado, **citalo por su sello**; si no lo trae, **declara en tu reporte que esta
vuelta no trae saldo de lote y por que**, y **no lo lances tu**.

---

## TAREA 2: `cap_10` ENTERO. **13 CANDIDATOS, Y LA VARA DEL CORTE YA ESTA ADJUDICADA**

| | |
|---|---|
| unidad | `cap_10`, **`Cap. 7`, `Team`** |
| cuerpo | **8.976 palabras** (`sed -n '8,$p' \| wc -w`, remidelo tu) |
| candidatos | **13**, y **13 cabe bajo el techo de 15** de `12.4`: **el capitulo entra entero y no se parte** |

**LA VARA DEL CORTE, adjudicada en la `ACTA 20` `4.1` y no negociable por comodidad:**

> **UN NODO POR CADA PAR (condicion de activacion, entregable).** La cuenta escrita
> del libro **no corta**: solo decide si la arista es `D.37` o `D.29`.

**LA FRONTERA, fila a fila, como la casa la cerro:**

| tramo | nodos |
|---|---:|
| `L47` a `L87`, las tres conversaciones de carrera | **3** |
| `L93` a `L125`, el plan de crecimiento anual | **1** |
| `L133` a `L163`, el proceso de contratacion, con el acto de `L129` dentro | **1** |
| `L169` a `L201`, despedir: cabeza, tres y coda | **5** |
| `L205` a `L223`, la calibracion de ascensos, con el caso de Google dentro | **1** |
| `L225` a `L251`, recompensar sin ascender | **2** |
| | **13** |

> **Y NO ES UNA ORDEN CIEGA.** `P.17`: la lectura que lee los pasos vence a la que
> argumenta sin ellos. **Si tu lectura con los pasos delante contradice esta tabla,
> GANA LA TUYA**, y la declaras con tu frontera al lado y su `sed` pegado (`D.35`).
> La proyeccion por densidad decia `10,3`, tu medida dijo `20` y la casa cerro en
> `13`: **tu aviso de que el denominador que predice una frontera es el rotulo y no la
> palabra se sostiene en la direccion y falla en el numero, por lo mismo que la
> densidad: un rotulo no es un nodo.**

**EL CORTE DE `L225` A `L251`, que es el que mas se discutio, va resuelto en DOS:**

| nodo | tramo | se activa cuando |
|---|---|---|
| **1** | `L229` a `L237` | **vas a anunciar ascensos o a elogiar en publico** |
| **2** | `L239` a `L251` | **tienes a alguien excelente en trayectoria gradual que se siente invisible y NO vas a ascenderlo** |

**LO QUE PARTE EL TRAMO ES LA ACTIVACION, NO EL ROTULO:** el primero se dispara
**cuando hay ascenso**; el segundo, **precisamente cuando no lo hay.** Y lo que junta
los tres ultimos lo dice el libro: `L247` escribe *Another great way*, que es marca de
**inventario de medios** y no de tres procedimientos (`D.27`). **`Public
presentations` no es un nodo: es un paso del nodo 2.**

---

## TAREA 3: LAS TRES ARISTAS `D.37` DE `L173`, **EN LA MISMA VUELTA EN QUE ESCRIBAS SUS PARTES**

**`L173` ESCRIBE LA CUENTA** (*three things*), y sus tres partes **si dan nodo**:

| parte | que es |
|---|---|
| **`P24`** (con `P25`) | la **cabeza** de la serie, y `L173` le pone la cuenta: **es nodo** (manual 3.4) |
| **`P26`** | segunda parte |
| **`P27`** | tercera parte |
| **`P28`** (`L197`, *Follow up*) | **CODA. NO entra en la serie.** Su activacion es *hace un mes que despediste* y su entregable es *el contacto hecho*: **es otro par** |

> **TRES ARISTAS `D.37`, CABLEADAS EN LA MISMA VUELTA EN QUE SE ESCRIBAN SUS PARTES**
> (`D.37`, y tu manual lo dice desde el 11 sep: el extractor declara esas aristas **en
> la misma vuelta** en que inserta las partes). **No se dejan para despues: una arista
> pendiente de una vuelta anterior es deuda, y ya hay doce.**

---

## TAREA 4: EL PAR DE LA LUPA, **POR LECTURA Y NO POR SEÑAL**

*Decision 3 del fundador, segunda mitad, literal: el par se declara **por lectura como
`CONTINUA` con arista, como el acta lo leyo, en la misma vuelta.***

> **`cap_10` `L225` a `L251`** (el nodo **2**, recompensar sin ascender) **contra
> `reconocer_recompensar_gente_estable` de `cap_06`** (12 pasos, en la bandeja):
> **`CONTINUA` CON ARISTA.** No es `REPITE`.

**LA RAZON, Y ES LA QUE EL ACTA ESCRIBIO:** contra **UN** nodo hijo la lectura es
`CONTINUA` con arista; contra cuatro nodos hijos habria que adjudicar cuatro pares y
tres de ellos con dos actos cada uno. **El corte en dos es lo que deja el par
legible.**

**Y AHORA LA ADUANA SI LO VA A LEVANTAR SOLA** (`D.38.5`): los dos extremos viven en
cuarentena y antes eso lo hacia invisible. **Si el informe te lo levanta, el veredicto
ya esta adjudicado aqui y lo escribes con su razon; si NO te lo levanta, eso es un
hecho nuevo y lo traes con tu medida** en vez de resolverlo copiando.

---

## LO QUE NO HACE ESTA VUELTA

**NO INSERTA NADA.** `D.39` inserta un lote **CERRADO**, y quedan `cap_11` a `cap_14`
sin minar. **Cero inserciones no es una vuelta perdida**, y la deuda de **doce colas
`D.29` vivas** se desbloquea con un solo acto cuando el lote cierre: **once de las
doce.** Las tres `D.37` de la TAREA 3 son aparte, porque sus nodos nacen hoy.

**Y NO MUEVE EL VOLUMEN.** El tramo del lote sigue en **tres capitulos**; esta vuelta
corre a **uno** porque manda el techo de candidatos (`12.4`), **no porque el freno se
haya disparado**: `PASOS INVENTADOS` da `cap_09` **0,00 (0 de 272)**, lote 4 **0,58 (5
de 856)**, peor fila `cap_04` **6,25** contra tope **10**. Publicalo igual, **fila por
capitulo mas total del lote**, y la escalada se decide **sobre el peor capitulo**.

## SON CUATRO TAREAS Y EL TOPE SON CINCO

**Si `cap_10` se come la vuelta, la vuelta se cierra ahi y lo declaras con su cifra.**
Las TAREAS 3 y 4 **no son separables de la 2**: nacen con los nodos de `cap_10` y se
escriben en el mismo acto. Lo unico que puede pasar a la siguiente es la **1.d**, si
el arnes no trajo informe.

## LAS PARADAS

**Las de `AUDITOR_FORJA.md` 3 estan enteras.** Lo nuevo es que el arnes puede
detenerse **antes de gastar un turno** si se le pide un informe de lote cuya carpeta no
existe (`D.41`), y sale en `docs/loop/loop.log` con el lote nombrado. **Esa parada es
del arnes, no tuya.**
