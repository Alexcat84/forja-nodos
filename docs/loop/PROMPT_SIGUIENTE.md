# ENCARGO DE LA VUELTA 28: **LAS TRES PARADAS ESTAN ADJUDICADAS Y NINGUNA ERA PARADA**, el cableado que `D.29` ya mandaba, la vigencia devuelta a lo que `D.15` dice que es, y `cap_07` hasta el final

*Escrito por el **auditor** al cerrar la `ACTA 27`. Sede del auditor por `AUDITOR_FORJA.md` 5.6.*

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO QUE LA `ACTA 27` DEJA RESUELTO, EN SEIS LINEAS

- **TU VUELTA 27 SALE LIMPIA DE `CLASE` Y DE `CIFRA PUBLICADA`.** Tus cinco cifras de cierre,
  tus `24` veredictos linea a linea, tus `3` aristas por los dos extremos y las `8` cadenas del
  ancla **me salen al digito**. Los `13` pares que leiste **son exactamente los `13` que mi
  barrido ciego levanto por su cuenta**, y **los trece se sostienen**.
- **TUS TRES PARADAS ESTAN MEDIDAS Y REPRODUCIDAS.** Las dos primeras las reproduje yo con tus
  comandos sobre copia. **Pero NINGUNA de las tres es parada**: a las tres las cubre una regla
  escrita, y la tercera la cubre `D.15` **negando expresamente el rojo**.
- **`D.29` YA DECIA QUE EL CABLEADO SE DIFIERE** cuando un extremo espera en cuarentena. Lo que
  falta no es doctrina: **es que esa mitad de `D.29` llegue a `src/aduana.py`**.
- **`D.15` DICE, CON ESTAS PALABRAS, QUE LA VIGENCIA NO PONE NADA EN ROJO**, y te da dos salidas:
  *se relee con el texto de hoy, **o se declara por que sigue valiendo***. **Quien te imprimio
  `CIERRE EN ROJO` fue `scripts/cerrar_reporte.py`, y contradice a `D.15`.**
- **`REPORTE` SUBE A `2 de 3`**, por dos afirmaciones que no movieron ni un dato: **`16` lineas
  de `NODO IDO` que son `16` hallazgos sobre `12` lineas**, y **declarar que la salida no estaba
  escrita cuando `D.15` la escribe**. Las dos en TABLA. Estas en el penultimo escalon.
- **Y UNA CAIDA ES MIA Y LA TIENES QUE SABER:** mi apertura sellada levanto una arista `D.29`
  (`fijar_fecha_cierre_debate_equipo` madre de `centrar_debate_ideas_fuera_egos`) **y la
  adjudicacion de hoy la retira. Tu `SANO` era el bueno.**

---

## TAREA 1: **LOS REGISTROS**

*Van primeros y no se solapan.*

| # | que hay que recoger | donde esta |
|---:|---|---|
| **1** | **las `13` adjudicaciones de la `ACTA 27`**: los `7` discutibles y las `6` propuestas tuyas | `ACTA 27` `2` y `7` |
| **2** | **las tres paradas, adjudicadas y NO sostenidas**, cada una con la regla que la cubre | `ACTA 27` `5` |
| **3** | **tus dos caidas de `REPORTE`**, con su especie y su sede escritas | `ACTA 27` `6.1` y `6.2` |
| **4** | **mi arista retirada por correccion declarada**, que es una caida mia y no tuya | `ACTA 27` `2.2` y `8.1` |
| **5** | **la razon de tu linea `256` dice *la misma etapa de persuadir* y tus dos nodos declaran `CLARIFY` y `PERSUADE`.** La clase es correcta y no se toca; **la premisa falsa se corrige por correccion declarada** en la razon, sin borrar | `ACTA 27` `2.1` y `6.4` |

> ### **Y EL REMEDIO QUE TE DEJO LA `ACTA 27`, QUE ES BLOQUEANTE Y SE COMPRUEBA CON UN COMANDO**
>
> **ANTES DE ESCRIBIR UNA CONCLUSION QUE DIGA QUE ALGO NO ESTA ESCRITO EN NINGUN SITIO, LO BUSCAS
> CON UN `grep` Y PEGAS LA SALIDA.**
>
>     $ grep -n "<lo que crees que falta>" docs/BANCO_DE_REGLAS.md docs/loop/*.md docs/*.md
>
> **Tus dos caidas de hoy son de esa familia**: una cifra contada de una salida sin volver a
> contarla, y una regla declarada inexistente que estaba **en el parrafo siguiente al que citaste**.
> **Es un comando, no la memoria.**

---

## TAREA 2, BLOQUEANTE: **`D.29` LLEGA A `src/aduana.py`, Y CON ELLA ENTRA LA CABEZA DE LA RUEDA**

*Adjudicado en `ACTA 27` `5.1` y `5.2`. **No es maquinaria nueva: es una regla escrita que no llego
al codigo**, la misma figura del `9ef933b` del 16 sep. La moratoria de `EXTRACTOR.md` 13 se levanta
**con su cita**: `4` candidatos parados, la cabeza de la rueda fuera con `10` de sus `24` partes ya
dentro y `0` aristas tocandola, y `4` lineas fantasma en la bitacora.*

**LAS DOS MITADES, Y LAS DOS SON DEL MISMO FICHERO Y DEL MISMO ACTO:**

**2.a. LA INSERCION ES ATOMICA: UNA CORRIDA QUE IMPRIME `RECHAZADO` NO ESCRIBE NADA.**

    $ sed -n '1169,1171p' src/aduana.py     (agregar_jsonl va DENTRO del bucle por vecino)
    $ sed -n '1195,1198p' src/aduana.py     (el rechazo por extremos llega DESPUES)

**La regla que lo manda:** `EXTRACTOR.md` 14 pone `bitacora/` bajo la aduana, y **la bitacora
registra lo que la aduana HIZO.** Una corrida que no inserto no hizo nada.

**2.b. UN `CONTINUA` CUYO OTRO EXTREMO ESPERA EN LA BANDEJA SE ESCRIBE, Y LA ARISTA QUEDA EN COLA.**

**`D.29` lo tiene escrito y solo hay que cumplirlo:** *una arista se cablea contra ids que ya viven,
y en cuarentena todavia no vive ninguno... Mientras el candidato espera en cuarentena, la arista vive
en un bloque propio y titulado del reporte.* **El veredicto se escribe AHORA; el cableado es DESPUES,
y el instrumento del despues ya existe y lo usaste tres veces: `forja.py arista`.**

**LO QUE NO SE MUEVE, y si tu diseno lo mueve paras y lo traes:**

- **la vara de `6.1`**: la clase sigue siendo `CONTINUA`. Escribir `SANO` seria caida de `CLASE`.
- **ningun umbral de `config/umbrales.json`.**
- **la guarda sigue mordiendo**: un `CONTINUA` sin razon escrita se sigue rechazando (`D.8`).

**2.c. LAS CUATRO LINEAS YA ESCRITAS SE DECLARAN NO CONSUMADAS, Y NO SE BORRAN.**

Son las lineas `248` a `251` de `bitacora/VEREDICTOS.jsonl`. **Esta casa corrige sin borrar** (manual
principio 6), **y la bitacora no se toca a mano** (`EXTRACTOR.md` 14): **se marcan por operacion**,
con su razon, igual que hiciste con `corregir`.

**CON LAS TRES HECHAS, INSERTA LA CABEZA DE LA RUEDA Y SU MADRE**, que es lo que llevan dos vueltas
esperando: `recorrer_rueda_conscientemente_cultura_equipo` **primero** (`D.29`: la madre entra
primero) y `recorrer_rueda_hacer_cosas_equipo` **despues**, con su arista **por `--paso 4`**, que es
la direccion que la `ACTA 25` `3.3` adjudico y que **no se reabre**.

**CADA MITAD CON SU CASO POSITIVO**, como los siete que escribiste para `corregir`: la prueba buena
que solo prueba que el comando escribe no prueba nada.

---

## TAREA 3: **LA VIGENCIA, DEVUELTA A LO QUE `D.15` DICE QUE ES**

*Adjudicado en `ACTA 27` `5.3`. **Las tres mitades son tres problemas distintos y por eso van
separadas**, que es lo que tu mismo pediste al repartir los `42` en vez de resumirlos.*

**3.a. `scripts/cerrar_reporte.py` CONTRADICE LA LETRA DE `D.15`, Y MANDA `D.15`.**

    $ sed -n '61p;75p' scripts/cerrar_reporte.py

`D.15` dice: *y por eso esto **NO** pone el gate en rojo: el gate vigila lo que es cierto o falso hoy;
esto vigila lo que fue cierto ayer y nadie ha vuelto a mirar.* **La vigencia sale de la lista de
guardas cuyo fallo devuelve `CIERRE EN ROJO`, por correccion declarada en el codigo y con el motivo
al lado.**

> **Y NO LA AFLOJAS:** `rancios` sigue mordiendo, sigue imprimiendo sus hallazgos, **y el cierre
> TIENE QUE SEGUIR PUBLICANDO SU CUENTA** en su salida. *La guarda que no muerde es cifra* (cosecha
> `7.C`). **Lo unico que cambia es que contar una cola no es caerse.** Si tu arreglo hace que la
> cuenta deje de imprimirse, **esta mal hecho.**

**3.b. LOS `26` `RANCIO`: SE DECLARA POR QUE SIGUEN VALIENDO, QUE ES LA SEGUNDA SALIDA DE `D.15`.**

**Y aqui se puede declarar con evidencia y no con una promesa:** las cuatro correcciones **solo
tocaron `resumen_teorico`**, por construccion de la operacion y por sus siete pruebas. **Ni un paso,
ni un titulo, ni un entregable, ni una fuente cambiaron**, y una lectura de par se emitio sobre eso.
**La declaracion va en sede duradera, no en el reporte**, y dice contra que huella se emitio y por
que el cambio no la invalida.

**3.c. LOS `8` HALLAZGOS DE `NODO IDO` SOBRE VECINOS DE BANDEJA: LA POBLACION DE LA VIGENCIA ES GRAFO
MAS BANDEJAS.**

**Es la misma mitad sin cablear que `D.38.5` ya arreglo en la aduana**, y la vigencia es el ultimo
sitio de la casa que mide solo el grafo. Un vecino de bandeja **no es texto muerto**: su texto vive
en `cuarentena/` y su huella se comprueba ahi. `D.38.4` y `D.38.5` dan la poblacion, descartando
`_insertados` y `_derivadas`.

**LOS OTROS `8` HALLAZGOS (las lineas `248` a `251`) NO SE TOCAN AQUI: los resuelve la `TAREA 2.c`.**

> **LO QUE NO TE AUTORIZO, y lo digo para que no lo hagas de paso:** **no cambies lo que la guarda
> considera `RANCIO`.** Tu propuesta `5` (que la vigencia distinga aniadir prosa declarada de tocar
> un paso) **es mover la vara de `D.15`, y eso se propone a Alexis**, no se hace en una vuelta. **Si
> tu arreglo de `3.c` necesita tocar eso, paras y lo traes.**

---

## TAREA 4: **SEGUIR INSERTANDO `cap_07` HASTA EL FINAL DEL CAPITULO**

| | |
|---|---:|
| candidatos del lote 4 en bandeja | **106** de 142 |
| ya insertados y archivados | **36** |
| candidatos de `cap_07` en bandeja | **15** |
| nodos en el grafo | **239** |
| veredictos en bitacora | **264** |

**DONDE SE PARO:** en `crear_obligacion_disentir_equipo` (`L231`), con sus `10` vecinos por leer.

**EL TRAMO ES EL CAPITULO Y NO MAS**, y la aritmetica lo cierra sola: `cap_07` trae **`15`**, que es
**exactamente el techo de candidatos** de `EXTRACTOR.md` 12.4 y todo el tramo de la vuelta. **No se
toca `cap_08`.** `PASOS INVENTADOS` de `cap_07` mide **`0,00` por ciento** sobre `64` pasos leidos uno
a uno (`ACTA 27` `4.2`), **asi que el freno de volumen no se activa**: lo que manda aqui es el techo.

**EL ORDEN LO SIGUE PONIENDO EL LIBRO** (`EXTRACTOR.md` 12.3), **con una excepcion que la `TAREA 2`
te habilita**: la cabeza de la rueda y su madre entran **antes** que el resto, porque cada parte que
entra sin ellas es una arista `D.29` que nadie va a poder cablear. Hoy son **`10` partes dentro y `0`
aristas tocando la cabeza**.

**Y LA SERIE QUE LEVANTASTE LEYENDO Y NINGUNA SEÑAL DECLARA SIGUE VIVA**:
`minimizar_impuesto_colaboracion_equipo` con sus **tres** partes nombradas
(`proteger_tiempo_equipo_jefe`, `mantener_manos_trabajo_real_equipo`,
`reservar_calendario_tiempo_ejecutar`). **Es `D.37` en su forma fuerte y las cuatro entran por el
orden del libro** (`L367` a `L387`).

**PUBLICA `PASOS INVENTADOS POR CAPITULO` EN TU REPORTE, con su fila de `cap_07` y su total**
(`AUDITOR_FORJA.md` 8.3): **es una cifra que tu das y yo firmo**, y si no la desglosas por capitulo
**la cifra agregada ya no se puede desglosar despues.** La vuelta 27 no la trajo y la tuve que contar
entera yo.

---

## TAREA 5: **EL HUECO DE TRANSCRIPCION DE `L153`, Y EL RESTO DE LA COLA CON SU CIFRA**

**5.a. EL HUECO NUEVO, con su linea** (`ACTA 27` `4.3`):

    $ sed -n '153p' fuentes/scott_radical_candor/cap_07.md
    153: ... I would stop and go around the table ... Other times, I would stand up in the
         next meeting and walk around, physically blocking a person who was talking too
         much. Sometimes I would have a quick conversation with people before a meeting ...

**El libro da TRES maneras y `crear_cultura_escucha_equipo` recoge DOS** (sus pasos `16` y `17`).
**Falta la segunda.** **Un paso que falta NO es un paso inventado** y no sube `PASOS INVENTADOS`:
es un hueco de transcripcion, **y el nodo ya vive en el grafo**, asi que se arregla por donde la casa
tenga escrito y **no aniadiendo un paso a mano**. Si lo unico que hay para eso es `corregir`, que solo
toca `resumen_teorico`, **entonces no alcanza y lo dices con su cifra en vez de improvisar**
(`EXTRACTOR.md` 7).

**5.b. LA COLA QUE VIENE DE LA VUELTA 27, CON SU CIFRA Y SU SEDE:**

| lo que queda | cifra | cuando vence |
|---|---:|---|
| la arista de la correccion 9, `recorrer_rueda_conscientemente_cultura_equipo --paso 4--> recorrer_rueda_hacer_cosas_equipo` | **1** | **la desbloquea la `TAREA 2`** |
| la mitad `Burnout` de la serie `D.37` de `aprender_resultados_vencer_dos_presiones` | **1** | cuando entre `cuidarse_agotamiento_centro_rueda` |
| la serie `D.37` de `minimizar_impuesto_colaboracion_equipo` | **3** partes | `TAREA 4` |
| `cap_04` releido antes que las tres filas de hueco (punto 5 de la `TAREA 1` de la vuelta 27) | **6** candidatos, **48** pasos | **sigue sin caber**, y lo declaras otra vez con su motivo si tampoco cabe |
| la frontera por capitulo con las `QUESTIONS TO CONSIDER` y su clase escrita | **14** de **17** unidades | la vuelta que mine un capitulo del lote 5 |
| el lote 5 por su orden | **3** candidatos en bandeja | **no en esta vuelta**: el lote 4 esta al `25` por ciento de insercion |

---

## LO QUE MANDA EN COMO ESCRIBES

**`D.41`:** toda tabla que presentes como salida de un instrumento **se anexa desde su fichero**, y el
hook la compara celda a celda.

**`D.42`:** toda ruta que publiques como sede de una cifra **tiene que sostenerla**, con sus tres
formas y solo tres.

**`D.38.3` ensanchada:** **la linea que acompania a una cifra dice lo que el instrumento MIDIO.** Toda
conclusion sobre contenido va en **linea aparte marcada `LECTURA`**. **Y una cifra que sale de contar
una salida se vuelve a contar con un comando**, que es la mitad que te costo `6.1` de mi acta.

**Al cerrar la vuelta:** `python scripts/cerrar_reporte.py`. **Si la `TAREA 3.a` esta hecha, la
vigencia ya no lo tumbara; su cuenta tiene que seguir saliendo impresa.**

## SON CINCO TAREAS Y EL TOPE SON CINCO

**La `TAREA 2` es BLOQUEANTE y va antes que la `4`**, porque la `4` mete mas partes de la rueda en un
grafo donde la cabeza no puede entrar. **Si la `TAREA 2` se come la vuelta, la vuelta se cierra ahi y
lo declaras con su cifra**: insertar cinco nodos mas sin desbloquear el cableado solo agranda la cola.

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
