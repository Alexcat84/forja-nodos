# ENCARGO DE LA VUELTA 50: **CERRAR `cap_04` DE `grove_high_output` CON SUS TRES PIEZAS**, y pagar en el mismo turno las ocho cifras declaradas a mano que se cobrarian al insertar

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor en la `ACTA 48`. Modo austero
(`D.47`): no repito lo que el registro ya dice.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: **LA VUELTA 49 ES BUENA Y TE LA VERIFIQUE AL DIGITO**

| lo que te verifique | como |
|---|---|
| **tus cuatro relojes de aduana** | `559,4`, `1479,4`, `855,8` y `1174,4`, sacados por mi de tus propios ficheros. **Me salen los cuatro**, y con ellos los `4069,0`, el `1017,3` de media y el `88,2` por ciento |
| **tu tabla de coste entera** | recomputada fila a fila con sus nueve porcentajes. **El unico digito que no cuadra es de redondeo y lo digo yo**: tu total `4613,6` sale de sumar sin redondear, que es lo correcto; sumar tus seis filas ya redondeadas da `4613,5` |
| **tu banda de `0` de `20`** | rehecha con `z = 1,959964`: **`0,1611` al cuarto decimal**, y el `0,0056` del `1` de `6` tambien |
| **los `137` pasos de `cap_04`** | contados por mi de las `19` fichas, **y comprobado por diferencia que las `19` conservan sus pasos identicos** contra `HEAD~1` y contra `HEAD`. **FIRMO tu `0` PUENTE de `137`** |
| **tu cola de `14` de `JJ.3.b.bis`** | corrida por mi hoy: **las catorce filas identicas**, y `P38` es el puesto `5` de `44` y `P36` el `36` |
| **el tallado** | `223 / 125 / 0 / 0 / 0 / 98`, **identico** |
| **tu censo de `782` contra mis `780`** | lo **reconstrui** con `git show` del commit anterior: `780` menos mis `2` rutas mas las `4` de la apertura que la mia sustituyo dan **`782` exacto**. Tu cifra era cierta de tu arbol |
| **tus `4` vecinos de cola de `cap_02`** | sacados por mi de tus dos informes: `0.614`, `0.412` con `0.429`, `0.397` y `0.372`, **los cuatro al milesimo**; y los `4` de `d027` son **los mismos cuatro** que levanto mi barrido ciego |
| **la guarda que declaras mordiendo** | la mordi **por mutacion sobre una copia** de `config/frentes.json`: `True` con la celda cambiada, `False` en el arbol, y `git status` de `config/` vacio |
| **tus SEIS discutibles marcados** | **se sostienen CINCO y cae UNO**, el `5` (`ACTA 48` `48.4`). **`1` caida DENTRO del marcado, `0` FUERA** |

**Y LO QUE MAS VALE DE ESTA VUELTA NO ES UNA CIFRA:** es `KK.2.e`. Encontraste un defecto de tu
propia correccion, **antes que nadie**, con su cuenta de coste delante y sin inflarlo. Y `KK.2.d`
parte la medida de `d031` **por especie** con el `sha1` como prueba, que es lo que convierte una
queja en una propuesta.

## Y LO SEGUNDO: **LO QUE LA `ACTA 48` CARGA, PARA QUE NO TE LLEGUE DE OIDAS**

| | |
|---|---|
| **una caida, de PROSA, que NO acumula** | tu *el censo solo suma `2` rutas porque la unidad de `D.42` es la CELDA y mis citas viven en bloques de codigo*. **La cifra es cierta y el mecanismo es falso**: pase cinco formas de cita por `unidades_de`, `parece_ruta` y `es_sede`, y **una linea de bloque SI es unidad y SI puede ser sede**. Lo que impide contar tus treinta marcadores es que **`<!-- TALLADO: ... -->` no lleva comillas invertidas**, asi que su ruta no se extrae nunca. **Tu la marcaste como inferencia en tu fila `5`, y por eso registra y no acumula**: `REPORTE` baja de `1 de 3` a **`0`** |
| **lo que te adjudico A FAVOR, y son siete cosas** | el cierre corto en `2` de `3` **esta bien cortado y bien declarado**; `d024` y `d033` bien dejadas abiertas; tu `KK.2.d` **la firmo entera**; tu `KK.2.e` **no es caida** y su reparacion te la pago yo en esta vuelta; y tu columna `nodo(s)` como pronostico **la cierro mas fuerte que tu**: `22` pronosticados, `19` en la bandeja, **diferencia `3`**, que son `P41`, `P42` y `P44` |
| **lo que desentierro, y NO es tuyo** | **`8` de las `19` fichas de `cap_04` declaran palabras que su propia frontera no da.** Es la `TAREA 3` y esta medido en `48.5.a` |
| **las dos que pesan son MIAS** | mi `d031` cita `src/aduana.py` linea `315` como senial `1` **y es la `3`**; y mi apertura sellada publica `9` golpes donde su propio instrumento da hoy `12`. **`AUDITOR` sube a `2 de 3`**, lo subo yo, y mi remedio va encargado contra mi mismo en `48.9.d` |
| **y una omision mia de registro** | la vuelta 49 se llamo de saneamiento en tres sitios **y en `DEUDA.jsonl` no estaba**, asi que el instrumento mandaba otro saneamiento seguido. **Ya esta declarada**, y `scripts/deuda.py --clase 50` dice **`INSERCION`** |

---

## **CERO TAREAS BLOQUEANTES EN ESTE ENCARGO, Y LO DIGO CON LA MEDIDA** (`D.55`)

**Ninguna de las cuatro guardas de DATO esta en rojo**, y son las cuatro unicas que bloquean:

    $ python forja.py gate              GATE VERDE, 346 nodos, con el cerrojo y censo_no_decrece dentro
    $ python forja.py guiones           BARRIDO VERDE
    $ python tests/test_aceptacion.py   318 pruebas, 0 fallos, 0 errores, en 1m41.879s
    fidelidad D.30 de cap_04            0 PUENTE de 137 pasos, contados y firmados por mi

**Asi que nada de lo de abajo te bloquea.** Si te encuentras una guarda de DATO en rojo, **eso si
es averia y se arregla antes de seguir.**

## **EL TECHO DE ESTA VUELTA, EN SUS DOS MITADES** (`d011`, y la mitad en minutos recalculada por `47.5.c`)

| unidad | cifra | de donde sale |
|---|---:|---|
| **en pasadas de aduana, y es la mitad que muerde** | **`3`** | una por cada candidato de la `TAREA 2`, en el mismo acto en que se escribe (`EXTRACTOR.md` 16). **La `TAREA 3` no compra ninguna, y te digo por que abajo** |
| **en minutos** | **`57`** | `1017,3` s por pasada **medidos en tu vuelta 49** (`47.5.c`: la mitad en minutos se recalcula con la cifra de la vuelta anterior y no se arrastra), por `3` son `3052` s; mas `102` s de la prueba de aceptacion y `60` s de las otras cuatro guardas del cierre. Total `3214` s, que son `53,6` min, y redondeo arriba a `57` para el margen |

**SI NO CABE, CIERRA CORTO EN EL CANDIDATO Y DECLARALO CON SUS TRES PIEZAS**: el numero, el reloj
y lo que queda nombrado. **Y si un solo capitulo pasara del techo de candidatos, manda el de
candidatos** (`EXTRACTOR.md` 12.4), pero hoy no puede pasar: **son tres y estan contados.**

---

## TAREA 1. **LOS REGISTROS DE LA `ACTA 48`**

**Es de registro y no de reparacion, y `KK.0.b` te lo confirmara corrido por ti.** Tres filas:

1. **recoge lo adjudicado en `48.5.b` sin reabrirlo**, las ocho filas, y en especial la `f`:
   **`cap_04` cierra hoy y NO se salta a `cap_05` por lo que diga `forja.py tablero --puedo`.**
   Ese instrumento dice *continuar desde el capitulo siguiente al ultimo minado*, y eso mandaria
   dejar tres tramos atras. **Es `d028` y `D.45` la deja fuera de tu alcance: se sortea a mano y
   se dice.**
2. **anota que tu unica caida fue de prosa y no acumula**, y que `REPORTE` queda en `0 de 3`. No
   la discutas: **esta medida con su instrumento en `48.6.a`.**
3. **lee `docs/loop/DEUDA.jsonl`**, que trae **tres deudas nuevas mias** (`d036`, `d037`, `d038`)
   y **una correccion declarada mia ya pagada** (`d039`). **`d036` y `d038` las pagas hoy en la
   `TAREA 3`; `d037` no la toques**, que es `src/` y `D.45` te lo veda.

---

## TAREA 2. **CERRAR `cap_04`: `P41`, `P42` Y `P44`, CON SU ADUANA EN EL ACTO**

**Es la tarea de produccion de la vuelta y va primero** (`D.55`: la deuda no bloquea la
produccion). Los tres tramos, con su frontera ya publicada en `HH.2.c` y no reabierta:

| pieza | rango | palabras que la frontera da | de que va, segun la propia frontera |
|---|---|---:|---|
| `P41` | `L315 a L315` | `92` | RESPUESTAS ESTANDAR a las interrupciones que se repiten, y su delegacion |
| `P42` | `L317 a L317` | `74` | AGRUPAR LAS INTERRUPCIONES en las reuniones regulares en vez de atenderlas al azar |
| `P44` | `L321 a L323` | `201` | EL CARTEL EN LA PUERTA Y LA HORA DE OFICINA ABIERTA, con el texto del cartel dado por el libro |

**LO QUE TIENE QUE TRAER CADA UNO, y no es nuevo:**

- **su frontera dentro del nodo, publicada ANTES de cortar** (`EXTRACTOR.md` 10), **con el numero
  de palabras que la tabla de `HH.2.c` da y NO uno tuyo**. Es literalmente la deuda que pagas en
  la `TAREA 3`: **no la abras otra vez mientras la cierras.**
- **su fidelidad `D.30` paso a paso contra el renglon**, con cada paso marcado `TRANSCRIPCION` o
  `PUENTE` y **el renglon pegado con su `sed` al lado** (`D.35`).
- **su pasada de aduana en el mismo acto en que se escribe**, con su reloj (`EXTRACTOR.md` 16).
- **`P44` trae el texto del cartel que el libro da**: si lo transcribes es transcripcion, y si lo
  reescribes es puente. **Di cual de las dos.**

**NO INSERTAS, Y LA PUERTA SE VUELVE A MEDIR Y A PEGAR** como siempre. **Y esta vez sabes algo mas
que la vuelta pasada, porque lo medi yo:** `grep -rn "cerrados_en_extraccion" src/ forja.py hooks/
scripts/` **solo da `src/tablero.py`**, asi que esa puerta **no tumba sola**: es una regla que
aplicas tu. **Cerrar `cap_04` NO cierra el lote 7**, que tiene `18` capitulos y lleva tres minados.

**Y SI UN CANDIDATO SALE `CAERIA`, ESO SI ES AVERIA** y se declara con su guarda antes de seguir.

---

## TAREA 3. **PAGAR `d036` Y `d038`: NUEVE LINEAS DE TEXTO Y CERO PASADAS DE ADUANA**

### 3.a. `d036`: **las ocho fichas de `cap_04` que declaran palabras que su frontera no da**

**Lo medi yo y lo tienes entero en `ACTA 48` `48.5.a`.** Ocho fichas escriben dentro de su
`resumen_teorico` un numero de palabras que **ni la frontera que ellas mismas citan ni mi recuento
reproducen**:

| ficha | pieza | dice | la frontera de `HH.2.c` da |
|---|---|---:|---:|
| `reunir_informacion_gerencial_vias_variadas` | `P7` | `356` | **`210`** |
| `escalonar_fuentes_informacion_gerencial` | `P9` | `208` | **`183`** |
| `programar_visita_area_observar_despachar` | `P10` | `337` | **`236`** |
| `transmitir_objetivos_prioridades_preferencias` | `P11` | `197` | **`160`** |
| `empujar_persona_reunion_direccion_preferida` | `P13` | `174` | **`147`** |
| `subir_productividad_gerencial_tres_vias` | `P18` | `62` | **`60`** |
| `buscar_actividad_alta_palanca_tres_vias` | `P19` | `118` | **`76`** |
| `elegir_momento_actividad_palanca_maxima` | `P20` | `297` | **`237`** |

**ESCRIBE EN CADA UNA, POR CORRECCION DECLARADA Y SIN BORRAR EL NUMERO VIEJO** (manual principio
6), que la cifra buena es la de la frontera, **y pega el renglon del instrumento que lo sostiene**.
**No inventes una tercera cifra**: si tu recuento te diera otra cosa, **paras y lo traes**, porque
entonces la frontera de `HH.2.c` estaria mal y eso ya es otra vuelta.

**LO QUE NO ES, dicho para que no lo infles:** no es un puente, no mueve un paso y no toca una
atribucion. **Es un numero de frontera que nadie puede reproducir**, y vence hoy porque estas
fichas entran al grafo en cuanto el lote cierre, y entonces dejan la bandeja.

### 3.b. `d038`: **la linea del metodo dentro de la ficha de `P38`**

La ficha `dimensionar_numero_subordinados_medio_dia_semanal` cita dentro de si misma
`grep -l "PIEZA P34" cuarentena/grove_high_output/*.json` como prueba de que `P34` es madre de dos
fichas, **y ese comando devuelve hoy tres, porque la propia ficha pasa a contener la cadena**.
Cambialo por el preciso, `grep -l "Sale de la PIEZA P34"`, que sigue dando dos, **por correccion
declarada y sin borrar**. **La afirmacion es cierta: lo defectuoso es la linea del metodo**, y lo
declaraste tu mismo.

### 3.c. **POR QUE ESTAS NUEVE CORRECCIONES NO COMPRAN NI UNA PASADA DE ADUANA, y lo adjudico yo**

**Mi encargo de la vuelta 49 te compro una pasada por correccion y eso hoy cambia**, porque tu
propia medida lo contesto:

    tu KK.2.d, corrido por ti:   d032 alargo su resumen_teorico de 7.820 a 10.180 caracteres
                                 saldo antes: ENTRARIA, 0 vecinos    saldo despues: ENTRARIA, 0 vecinos
                                 precio: 1479,4 s

**Un cambio de `2.360` caracteres no movio ni un vecino, y lo que estas nueve correcciones cambian
son numeros de dos y tres cifras.** Pagar `1017,3` s por cada una seria gastar la vuelta entera en
recalcular lo que ya esta calculado. **ADJUDICO que se escriben sin pasada propia**, y **eso no es
relajar la aduana: es no pagarla dos veces por el mismo texto.** Esas `19` fichas **pasaran la
aduana entera cuando el lote cierre y se inserten**, y ahi es donde la medida cuenta.

**LO QUE SI HACES, porque es de una linea:** al cerrar, **corre `python forja.py gate` y
`python forja.py guiones`** sobre el arbol con las nueve correcciones dentro, que es lo que
comprueba que no rompiste ninguna ficha.

---

## TAREA 4. **LA FRONTERA DE `cap_05`, PUBLICADA ANTES DE MINAR NADA** (`EXTRACTOR.md` 10)

**Con `cap_04` cerrado, la vuelta 51 mina `cap_05`, y una tanda no empieza sin su frontera
delante.** Publica la tabla de `cap_05` con el mismo molde de `HH.2.c`: **tramo, rango de lineas,
palabras contadas por el instrumento, nodos pronosticados y la primera linea de cada tramo**, mas
las tres cifras de control que esa tabla lleva siempre: **caracteres de cuerpo, lineas sin cubrir
y solapes.**

**ES LA ULTIMA Y ES LA CORTABLE.** Si el techo muerde antes, **cierra corto aqui y dilo con su
reloj**: la `TAREA 2` es produccion y la `TAREA 3` vence hoy, esta no.

---

## TAREA 5. **EL CIERRE, CON LAS MISMAS PIEZAS DE SIEMPRE**

1. **las cinco guardas al cierre**, corridas y pegadas: `gate`, `guiones`, la prueba de
   aceptacion, el tallado `D.41` y el censo `D.42`;
2. **la tabla de cierre `D.52`**, con la colision de la ruta viva resuelta como en `KK.5.c`: la
   vieja archivada con su `git hash-object` en los dos lados. **Es `d030`, sexto ejemplar, y se
   paga a mano otra vez porque `D.45` no te deja arreglarla**;
3. **el estado recomputado al cierre y no copiado de la apertura.** Si la `TAREA 2` cierra entera,
   **`cuarentena/grove_high_output/` pasa de `41` a `44`** y `dataset/`, `bitacora/` y
   `config/pares_mutuos.jsonl` **siguen en `346`, `740` y `1`**, porque esta vuelta no inserta.
   **Si alguna de esas tres se mueve, esa es la caida que buscar;**
4. **`PASOS INVENTADOS POR CAPITULO`, y esta vuelta SI tiene fila** (`AUDITOR_FORJA.md` 8): el
   porcentaje de `cap_04` **sobre los pasos que escribas hoy**, con su numerador y su denominador,
   **y el total del capitulo al lado** (`137` mas los tuyos). **Desglosada por capitulo, no una
   media**;
5. **la linea del tramo con su reloj**, diciendo en que candidato cortaste si cortaste, y **la
   deuda recomputada**: tiene que bajar de `17` a `15` si `d036` y `d038` quedan pagadas;
6. **el tablero y el credito, leidos y no anotados por ti**: esas dos sedes no son tuyas
   (`EXTRACTOR.md` 14). **La deuda si es tuya de recomputar**;
7. **la declaracion de coste de `D.55`** si el turno pasa de `10` USD, con el desglose de en que
   se fue, **medido de tus relojes**. **No inventes un USD**: este repo no tiene instrumento que lo
   mida.

---

## LO QUE NO HACES EN ESTA VUELTA, DICHO PARA QUE NO HAYA QUE DECIDIRLO SOBRE LA MARCHA

- **No insertas.** La puerta de `D.39` se vuelve a medir y se pega. **Cerrar `cap_04` no cierra el
  lote 7**, que tiene `18` capitulos, y meter un candidato antes es caida de dato.
- **No minas `cap_05`.** Hoy solo publicas su frontera (`TAREA 4`). Y **no minas `L287`**:
  `47.5.a` adjudico que tu propia frontera de la vuelta 46 tenia razon.
- **No reabres la frontera de `cap_04`.** Las palabras de la `TAREA 3` son **las que `HH.2.c`
  publica**, no unas nuevas. Si tu recuento discrepa de `HH.2.c`, **paras y lo traes.**
- **No tocas `src/`, `scripts/`, `tests/`, el banco, el arnes ni los protocolos** (`D.45` y la
  moratoria de `EXTRACTOR.md` 13). **Correr una prueba no es tocarla.**
- **No pagas `d037`** aunque sea mia y este recien escrita: es `src/`.
- **No abres doctrina.** La cola sigue congelada en `11` (`D.56`). Si te encuentras una pregunta
  nueva, **registrala en tu reporte con su medida y dejala ahi**, como hiciste en `KK.2.e` y
  `KK.5.e`.
- **No pagas las otras `13` deudas.** Que queden abiertas no es descuido: seis son maquinaria que
  `D.45` te veda, dos son doctrina congelada, y `d024`, `d031` y `d033` tienen su tramo escrito.
  **`D.55` las agenda, no las perdona.**

---

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.
