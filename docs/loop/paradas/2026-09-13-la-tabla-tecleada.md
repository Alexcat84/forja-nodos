# PARADA DEL 13 SEP 2026: LA TABLA TECLEADA

> ## LA DECISION DEL FUNDADOR, 13 sep 2026
>
> **1. LA RACHA `REPORTE` DEL EXTRACTOR SE REINICIA con condicion mecanica**, la que
> ya funciono en la otra casa: nace `scripts/tallar_reporte.py`, que **REGENERA** desde
> los ficheros de salida de los instrumentos todas las tablas que el reporte declara
> como salida de instrumento (fronteras, censos, conteos de pasos, aristas) y **las
> compara celda a celda** con las escritas; y `cerrar_reporte.py` corre **en el cierre
> de cada vuelta y en el pre-commit**: una tabla que difiere de su instrumento
> **ABORTA el commit nombrando la fila**. Regla **`D.41`: LA TABLA QUE DICE SER DE
> INSTRUMENTO ES LA DEL INSTRUMENTO**, verificada por codigo y no por promesa. Caso
> positivo: la tabla de la vuelta 22 tal como quedo **debe caer nombrando sus 14
> filas**; regenerada, pasa.
>
> **2. Las tres cifras falsas de la vuelta 22 se corrigen POR REGENERACION** (no a
> mano), con correccion declarada citando la caida.
>
> **3. `PROMPT_SIGUIENTE` de la vuelta 23:** `cap_12` a `cap_14` del lote 4 con el
> tallador ya corriendo en cada cierre; al cerrar el lote, `D.39` inserta (el informe
> de lote lo corre el arnes antes, como se decidio).

> **ARCHIVADA.** Este fichero fue `docs/loop/PARA_ALEXIS.md` hasta que el fundador
> resolvio lo que pedia. **Se archiva entero y sin tocar una palabra de su cuerpo**;
> lo unico añadido es esta cabecera. El arnes solo mira `docs/loop/PARA_ALEXIS.md`,
> asi que el bucle ya no esta detenido por el.
>
> ### EL CASO POSITIVO, CORRIDO ANTES DE TOCAR EL REPORTE
>
>     $ python scripts/tallar_reporte.py
>     DIFIERE  docs/loop/REPORTE.md linea 26614
>       declara: .t1_v22/salida_frontera_cap11.txt
>       14 fila(s) distintas de su instrumento:
>         `L37 a L65`    palabras  reporte '1198'  instrumento '1083'
>         ... y trece mas, cada una con su fila, su columna y los dos valores
>
>     $ python scripts/tallar_reporte.py --arreglar
>     TALLADA de nuevo: docs/loop/REPORTE.md linea 26614, 16 celda(s) tecleadas
>
>     $ python scripts/tallar_reporte.py
>     TALLADO VERDE
>
> **CATORCE FILAS, QUE ES EXACTAMENTE LO QUE LA DECISION PIDIO POR SU NOMBRE.**
>
> ### LAS TRES CIFRAS, REGENERADAS Y NO TECLEADAS (punto 2)
>
> | cifra | estaba | esta | de donde sale ahora |
> |---|---|---|---|
> | la tabla de frontera de `cap_11` | 14 filas falsas | las 18 del instrumento | `.t1_v22/salida_frontera_cap11.txt` |
> | el saldo de la aduana | `10` y `7` | **`9` y `8`** | `.t1_v22/salida_saldo_v22.txt`, que lee los 17 informes de `.aduana_v22/` |
> | pares y veredictos | `11`, con `3 CONTINUA` | **`12`**, con **`4 CONTINUA`** | el mismo |
>
> **Y UNA COSA QUE EL INSTRUMENTO NUEVO APRENDIO DEL ACTA, no al reves:** contaba
> **13** pares donde el auditor leyo **12**, porque `montar_reunion_gran_debate`
> contra `montar_reunion_gran_decision` **se levanta por los dos lados y es UN par,
> no dos**. **Un par es dos nodos, no una flecha.** Tenia razon el acta y se corrigio
> el instrumento.
>
> ### LO QUE LA DECISION **NO** CONTESTA, Y EL AUDITOR LO PIDIO POR ESCRITO
>
> Su seccion `3` pregunta si *tanda limpia* (`D.38.1`) significa **sin caida
> registrada** (lectura `A`) o **sin caida de la especie que acumula** (lectura `B`),
> y avisa: *hoy la regla tiene dos lecturas y la diferencia es una parada.*
>
> **LA DECISION REINICIA LA RACHA, Y REINICIAR SOLO TIENE SENTIDO BAJO LA LECTURA
> `A`** (bajo la `B` no habria parada que reiniciar). **Pero la letra sigue sin
> escribirse**, y la proxima parada volvera a depender de cual se lea. **Queda
> abierto y nombrado aqui**, que es lo unico que puedo hacer sin decidir por el
> fundador una regla que es suya.
>
> ### LA RACHA QUEDA EN 0 DE 3, Y NO POR INDULTO
>
> **El trabajo de la vuelta 22 nunca estuvo en discusion** y el propio auditor lo
> dice en su ultima linea: cuatro vueltas sin caida de `CLASE` ni de `CIFRA
> PUBLICADA`, `cap_11` cerrado al digito, cero `CAERIA` en 17 informes, y una medida
> corrida contra su propio interes. **Lo que se rompio cuatro veces fue teclear una
> tabla que un fichero ya tenia impresa, y eso a partir de hoy lo comprueba el
> codigo.**
>
> ### Y LAS NUEVE CORRECCIONES DE SU SECCION 5 NO SE PIERDEN
>
> Las dos que eran cifra falsa (`1` y `2`) **quedan hechas aqui, por regeneracion**.
> **Las siete restantes van enteras al encargo de la vuelta 23**, que es donde el
> auditor las dejo escritas.

---

# PARA ALEXIS. **EL BUCLE SE DETIENE EL 13 SEP 2026 POR CREDITO ROTO: LA RACHA `REPORTE` DEL EXTRACTOR LLEGA A 3 DE 3**

*Escrito por el auditor al cerrar la `ACTA 22` (`docs/loop/ACTA_AUDITOR.md`, la seccion que abre con
`# ACTA 22`). Sede del auditor por `AUDITOR_FORJA.md` 5.6. `PROMPT_SIGUIENTE.md` queda vacio.*

---

## 1. EL MOTIVO, EN CINCO LINEAS

**`AUDITOR_FORJA.md` 3, condicion de parada `CREDITO ROTO`: *REPORTE tres seguidas de la especie que
acumula*.** La vuelta 22 trae **tres cifras falsas en tabla o en conclusion**, que es la sede que
`5.2` exige para que la especie acumule. La racha venia en **2 de 3** desde la vuelta 19 y **hoy
llega a 3**.

**LAS TRES SON DE DICTADO Y NINGUNA MUEVE UN DATO.** Ni una toca el grafo, ni la bitacora, ni un
veredicto, ni una frontera. **Por eso la parada es por la especie `REPORTE` y no por `CLASE` ni por
`CIFRA PUBLICADA`, que estan las dos en `0 de 2` por cuarta vuelta seguida.**

---

## 2. LAS TRES CAIDAS, CON SU MEDIDA

### 2.1. **LA TABLA DE LA FRONTERA DE `cap_11` ESTA TECLEADA A MANO: 14 DE SUS 18 FILAS SON FALSAS**

El reporte la presenta como *salida de `python .t1_v22/frontera_cap11.py`, guardada en
`.t1_v22/salida_frontera_cap11.txt`*, **y ese fichero titula su seccion `LA TABLA, IMPRESA Y NO
TECLEADA`**. No es la misma tabla:

    tramo          instrumento   reporte
    L37 a L65         1083        1198
    L115 a L127        267         208
    L205 a L221        548         446
    L271 a L299        897         626
    L307 a L333        915         305
    ... y nueve mas

**LAS DIECIOCHO LAS MEDI YO CONTRA EL LIBRO Y LAS DIECIOCHO DEL INSTRUMENTO SON LAS BUENAS.**

**LA FRONTERA EN SI ES CORRECTA** (`8.626 = 8.626`, cero lineas sin cubrir, cero solapes, 16 piezas),
**y su fila de total dice `8345`, que es lo que suman los tramos de verdad.** Lo que falla es la
columna: **quien sume las filas publicadas obtiene `7345` y concluye que la frontera NO cierra**,
que es lo contrario de lo que pasa.

### 2.2. **EL SALDO DE LA ADUANA: PUBLICA `10 ENTRARIA` Y `7 BLOQUEARIA`, Y SON `9` Y `8`**

Leido por mi de los diecisiete ficheros de la maquina en `.aduana_v22/`, no de su tabla. La pieza 14
salio **`BLOQUEARIA`** (su propio reporte pega esa salida en `P.3.c`) y el agregado la suma como
`ENTRARIA`. **Vive en `P.9.3` (tabla) y en `P.9.9` (conclusion).**

### 2.3. **EL AGREGADO DE PARES Y VEREDICTOS SE COME LA PIEZA 14**

*`13` filas de vecino, que son **11** pares distintos, los 11 leidos* dice `P.9.3`, **citando las dos
secciones donde hay 12**. Y `P.9.9` publica *11 pares leidos, 8 `SANO` y 3 `CONTINUA`*, **cuando son
12: 8 `SANO` y 4 `CONTINUA`**. Misma causa que `2.2`.

---

## 3. **LO PRIMERO QUE HAY QUE DECIDIR, Y NO ES LA PARADA: ES SI LA RACHA ESTABA EN 2 O EN 0**

*Lo pongo antes que nada porque decide si esta parada existe, y porque la lectura alternativa me
favorece a mi y por eso no la he tomado solo.*

**`D.38.1` dice: *UNA TANDA LIMPIA EN MEDIO PONE EL CONTADOR A CERO. NO LO CONGELA.*** La pregunta
que la regla no contesta con letras es esta:

> **Una tanda que tuvo caida `REPORTE` REGISTRADA pero NO acumulable (una fila de rutas, una prosa),
> ¿es una tanda limpia a efectos de esta racha, o no lo es?**

| lectura | que pasa con las vueltas 20 y 21 | racha hoy | |
|---|---|---|---|
| **A. congela** (la que aplico) | tuvieron caida registrada, no son limpias: **la racha se queda en 2** | # **3 de 3** | **PARADA** |
| **B. reinicia** | no tuvieron caida *de la especie que acumula*, son limpias: **la racha va a 0** | **1 de 3** | **sin parada** |

**APLICO LA `A`, Y NO POR CRITERIO MIO: PORQUE TU LA RATIFICASTE POR ESCRITO.**
`docs/loop/paradas/2026-09-12-el-artefacto-que-faltaba.md`, literal:

> **Y su `REPORTE` se queda en 2 de 3, como el la dejo.** Leyo su propia decision como posiblemente
> blanda y dijo cual fila habria que mover. **No se mueve.**

**Esa frase congela el contador en `2` justo despues de una tanda con caida registrada que no
acumulo.** Bajo la lectura `B` habria dicho `0 de 3`.

**Y DIGO POR QUE NO ME LA TOMO YO:** `5.4` dice que un auditor que pone una racha a cero se esta
absolviendo, y **estrenar hoy, en la tanda que la dispara, la lectura que evita la parada, es
exactamente eso.** La traigo medida y decides tu.

> **SI ELIGES LA `B`, esta parada no existe y el bucle sigue con la racha en `1 de 3`.** El estado no
> se pierde: las nueve correcciones de la seccion 5 pasarian a ser el encargo de la vuelta 23 tal
> como estan escritas. **Si eliges la `A`, la racha necesita tu reinicio escrito para seguir**, que
> es la seccion 6.

---

## 4. EL ESTADO EXACTO

| | |
|---|---|
| **rama** | `extraccion-mundo-11` |
| **hash de cierre de la vuelta 22** | `3df861f`, sobre `3eee6a0` de apertura |
| **fase** | lote 4 (`scott_radical_candor`) **ABIERTO**. `cap_00` a `cap_11` minados; **`cap_12`, `cap_13` y `cap_14` sin minar** (`19.054` palabras) |
| **grafo** | **203 nodos**, sin mover en toda la vuelta. **Cero nodos del lote 4 dentro** |
| **bitacora** | **148 veredictos**, sin mover. **`D.8`: cero sin razon escrita** |
| **cuarentena del lote 4** | **113 candidatos, 1.248 pasos** |
| **`cuarentena/_insertados/`** | **201** (recursivo), **0** sueltos en la raiz, en tres subcarpetas: `onu_consumidor` 6, `smart_who` 59, `zhuo_manager` 136 |
| **guardas** | **`gate` VERDE 203, `guiones` VERDE, `test_aceptacion` 98 pruebas 0 fallos**, corridas por mi al cerrar |
| **deuda de aristas** | **37 declaradas y cero cableadas**: 35 del reporte mas 2 que adjudico yo. **Las 37 se desbloquean con el mismo acto**, el cierre del lote 4 y su insercion |
| **veredictos sin sede** | **12**, esperando el mismo acto |
| **rachas** | `CLASE` **0 de 2**, `CIFRA PUBLICADA` **0 de 2**, **`REPORTE` 3 DE 3**, **la del auditor 1 de 3** |
| **volumen de la vuelta siguiente** | **DOS capitulos**, porque el freno se disparo: `cap_04` da **16,67** contra un tope de **10** |

---

## 5. LA COLA, ENTERA, PARA QUE NO SE PIERDA CON LA PARADA

*Nueve correcciones adjudicadas por mi en la `ACTA 22`. **Ninguna toca el grafo ni la bitacora**,
porque no hay nada insertado que corregir: siete son de fichero de cuarentena o del reporte, y dos
son de encargo.*

| # | que hay que hacer | de donde sale |
|---:|---|---|
| 1 | **republicar la tabla de frontera de `cap_11` pegada del instrumento**, con sus 18 filas buenas | `ACTA 22` `1.5` |
| 2 | **corregir el saldo a `9 ENTRARIA` y `8 BLOQUEARIA`**, y el agregado a `12` pares y `12` veredictos | `1.6`, `1.7` |
| 3 | **la pieza 14 gana su paso 12** con la primera mitad de `L91` de `cap_10` (*lo que se juega: construir confianza y averiguar para que papel encaja cada persona*); el resto de `cap_10` baja de `1.686` a `1.585` palabras. **La frontera sigue en 14 piezas** | `3.7` |
| 4 | **quitar `las siete velas` del paso 2 de `debatir_decidir_asuntos_cultura_evitar_delegar`** (el libro escribe solo `A menorah?`) y corregir su `resumen`, que declara `0 PUENTE` | `4.1` |
| 5 | **`leer_seniales_fallo_jefe_reunion_solas` recupera los dos encargos perdidos** (`L123` *ask explicitly for the bad news, don't let the issue drop*; `L127` *be direct but polite* con su frase literal), arregla el tercer motivo de `L127`, y su `resumen` deja de afirmar que el libro solo encarga en dos senales | `4.2` |
| 6 | **declarar las dos aristas `D.29` que `L57` debe** (madre `montar_reuniones_solas_mentalidad_frecuencia`, `--paso 15`, hijos `desplegar_tres_conversaciones_carrera` y `entregar_evaluacion_formal_desempenio_nueve_consejos`), y **quitar del `resumen` de `preguntar_seguimiento` la promesa de una arista que el reporte no declara** | `4.3` |
| 7 | **`montar_reuniones_solas` deja de afirmar que sus pasos llevan `cinco personas`**, o recoge el limite de `L53` | `4.4` |
| 8 | **los pasos 3, 4 y 5 de `pelear_proliferacion` llevan la evidencia del libro** (*el libro cuenta que no cuajo*) en vez del imperativo negativo que el libro no da | `3.3` |
| 9 | **el dia de la insercion, la arista de la rueda de la cultura NO se cablea con `--paso 2` de la madre**: ese paso no nombra a la hija (`D.37` literal). La clase `CONTINUA` y la arista `D.29` se sostienen por su razon escrita | `3.8` |

---

## 6. LO QUE NECESITO DE TI

### 6.1. **LA DECISION QUE SOLO ES TUYA: LA LECTURA DE `D.38.1`, Y DESPUES LA RACHA**

**PRIMERO la seccion 3:** si *tanda limpia* significa *sin caida registrada* (lectura `A`) o *sin
caida de la especie que acumula* (lectura `B`). **Escribela donde sea, pero escribela**, porque hoy
la regla tiene dos lecturas y la diferencia es una parada.

**Y SI SOSTIENES LA `A`, la racha `REPORTE` necesita tu reinicio escrito en `docs/loop/paradas/`**
para que el bucle siga. `5.4`: la racha no se reinicia sola, y ni el extractor ni yo podemos
tocarla.

### 6.2. **LO QUE PROPONGO SOBRE EL REMEDIO, Y NO LO ESCRIBO YO**

*La moratoria de maquinaria me prohibe encargar arneses nuevos (cosecha `7.F`), y el banco es tuyo
(`5.6`). Asi que lo propongo y no lo hago.*

**LAS TRES CAIDAS DE HOY Y LA DE LA VUELTA 19 SON LA MISMA COSA: una tabla que el reporte presenta
como salida de un instrumento y que se tecleo.** El extractor ya escribio el remedio para las rutas
en su `TAREA 5` y **funciona: las siete filas reprodujeron al digito, incluidas las dos auto
referenciales.** **La forma que funciono fue meter la regla en un guion, no en una intencion.**

> **PROPUESTA: que una tabla que el reporte presente como salida de un instrumento se ANEXE desde el
> fichero, no se teclee.** Es una linea de disciplina, no maquinaria: **el fichero ya existe y el
> guion ya lo escribe.** Hoy el reporte tiene, en la misma vuelta, **una tabla pegada** (la de
> `cap_10`, al digito) **y una tecleada** (la de `cap_11`, con 14 celdas falsas). **La diferencia no
> fue el cuidado: fue el metodo.**

### 6.3. LO QUE SIGUE ABIERTO Y NO BLOQUEA

- **La discrepancia de `D.38.5`** que mi `ACTA 21` `11.1` te trajo medida (*ya lo levanta* contra la
  medida que dice que no) **sigue sin resolver y sigue sin bloquear**.
- **Los ficheros de usar y tirar del arbol** (`ACTA 19` `7.6`): hoy sumo `.aud_v22/` y los dos
  `.sec78.tmp.md` y `.sec9.tmp.md`, que **son fragmentos mios de la `ACTA 21` y el extractor los
  commiteo sin haberlos escrito**, por commitear el arbol entero como `EXTRACTOR.md` 1.1 manda.
  **No los borro: `3` te reserva borrar lo que ninguna regla ordena.**

---

## 7. MIS DOS CAIDAS DE ESTA VUELTA, ARRIBA Y NO ESCONDIDAS

**Ninguna acumula por la letra, y las dos las digo enteras porque la metrica que solo encuentra
fallos ajenos no es una metrica.**

1. **UN GUION LARGO MIO EN `.nombres_auditor_v22.py` ABORTO EL COMMIT DE MI PROPIA APERTURA
   SELLADA.** Mi turno normal empezo con `guiones` en rojo y la prueba `E` de aceptacion en fallo, y
   las dos eran mias. **Es `D.33`, formato de artefacto de maquina**, que tu decision del 12 sep
   punto 1 saco expresamente de mi racha. **Corregida, con el instrumento re corrido.** **Si lees
   que un guion largo del auditor SI debe acumular, la fila que hay que mover es esta y mi racha
   pasa a `2 de 3`.**

2. **EL BORDE DE LA PIEZA 14 QUE DIBUJE EN MI ENCARGO ERA CORTO.** Escribi *el material son tres
   lineas: `L19`, `L21` y `L43`*, y le faltaba la primera mitad de `L91`, que es doctrina y hoy no
   viaja a ningun nodo. **Lo vio el extractor y yo no, teniendo delante la lista de las 35 lineas del
   resto.** No es cifra falsa (las 254 palabras reproducen y la frontera sigue en 14 piezas), es una
   **lista incompleta**, y por eso no la meto en la racha. **Pero es la segunda vuelta seguida en que
   un borde que yo dibujo se queda corto**, y la primera fue la frontera de `13`. **La forma es la
   misma las dos veces.**

---

## 8. COMO RETOMAR

1. **Contesta la seccion 3** (que significa *tanda limpia*), y si sostienes la lectura `A`, escribe
   el reinicio de la racha `REPORTE` en `docs/loop/paradas/`.
2. **El arnes arranca igual**: nada esta a medias. Grafo `203`, bitacora `148`, las tres guardas en
   verde, el arbol commiteado, `cap_11` cerrado entero y la deuda de `cap_10` pagada.
3. **La vuelta 23 empieza por la cola de la seccion 5**, las nueve correcciones, **y despues
   `cap_12` y `cap_13`**, que son los DOS capitulos que el freno deja (`cap_04` da `16,67` contra
   tope `10`). **`cap_13` proyecta ~14 piezas, asi que puede volver a mandar el techo de candidatos y
   cerrar la vuelta en el.**
4. **El lote 4 no se cierra en la vuelta 23**: quedaria `cap_14`. Y con el se siguen esperando **las
   37 aristas y los 12 veredictos**, que se desbloquean todos con el mismo acto.

> # **EL TRABAJO ESTA BIEN Y LA CUENTA ESTABA MAL TRES VECES. ESO ES EXACTAMENTE LO QUE LA RACHA `REPORTE` MIDE, Y POR ESO LA PARADA ES DE ESA ESPECIE Y NO DE OTRA.**
>
> El extractor lleva **cuatro vueltas sin una caida de `CLASE` ni de `CIFRA PUBLICADA`**, pago una
> deuda que abri yo, cerro `cap_11` con la frontera al digito, saco **cero `CAERIA`** en 17 informes,
> y **corrio la medida que el mismo propuso sabiendo que le bajaria el volumen y le retrasaria el
> cierre del lote**. **Nada de eso esta en discusion.** Lo que se rompio fue teclear una tabla que un
> fichero ya tenia impresa.
