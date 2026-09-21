# DECISION DEL FUNDADOR, 17 SEP 2026: **UN CERROJO NO ES DATO, Y LA CIEGA NO VE EL CREDITO**

*Archivo de `docs/loop/PARA_ALEXIS.md` de la linea serial, escrito por el auditor al
cerrar la `ACTA 32` sobre la vuelta 33. **La decision va arriba, literal. El cuerpo de la
parada va debajo sin tocar una coma.***

---

## LA DECISION, LITERAL

> SESION DE CHAT en forja-nodos. DECISION DEL FUNDADOR (17 sep 2026)
> sobre la parada de la vuelta 33. Archiva su PARA_ALEXIS en
> docs/loop/paradas/2026-09-17-dato-movido-y-la-ciega-que-ve-DECISION.md
> con esto literal, aplicalo y relanza el principal:
>
> 1. UN CERROJO DE PROCESO NO ES DATO, Y NO VIVE EN dataset/. Regla al
>    banco: dataset/ contiene el catalogo y nada mas; los ficheros de
>    coordinacion (cerrojo, marcas de proceso) viven fuera, con su ruta
>    escrita. El cerrojo se MUDA fuera de dataset/ en esta vuelta, con su
>    caso positivo re-corrido (dos procesos, el segundo espera), y su
>    ejemplar de la racha se RECLASIFICA de DATO MOVIDO a ARNES: no
>    acumula. La racha DATO MOVIDO queda en 1 de 2.
> 2. EL EJEMPLAR QUE SI ES DATO SE REPARA ANTES DE SEGUIR, como TAREA 1:
>    el nodo que afirma que tres capitulos no estan minados cuando uno
>    tiene 16 nodos y 187 pasos dentro se corrige contra la medicion del
>    dia, con correccion declarada y la cifra citada; y se mide si hay
>    mas nodos con afirmaciones de estado de mineria dentro de su texto
>    (esa especie no deberia existir: un nodo describe conocimiento, no
>    el estado de la campaña), nombrando lo que salga.
> 3. LA FASE CIEGA NO VE EL REGISTRO DE CREDITO, y el defecto es del
>    fundador por D.48: correccion declarada. El arnes RETIRA
>    docs/loop/CREDITO_<linea>.jsonl durante la fase ciega, como ya
>    retira los otros cuatro, y le entrega al ciego SOLO la herencia que
>    D.40 exige (remedios pendientes con su motivo y su salida pegada),
>    sin cifras ni conclusiones. Y el campo cita del registro se escribe
>    como REFERENCIA (ruta y linea del acta), nunca como resultado
>    copiado: con su prueba, un cita con conclusion dentro no pasa el
>    sello. Caso positivo con claude falso.
> 4. Las otras seis preguntas de doctrina quedan EN COLA declarada: se
>    resuelven cuando el mundo 11 cierre, salvo que alguna bloquee a una
>    linea, y entonces sube sola. Escribelas en una seccion COLA DE
>    DOCTRINA del TABLERO para que no se pierdan.
> 5. Escribe el PROMPT_SIGUIENTE de la vuelta 34 con la TAREA 1 delante,
>    luego la continuacion del lote 4 (79 de 142) por el tablero y su
>    prioridad, y relanza el principal.

---

## LO QUE SE APLICO, Y DONDE QUEDO CADA COSA

| punto | donde vive ahora |
|---|---|
| **1. el cerrojo no es dato** | **`D.52`** en `docs/BANCO_DE_REGLAS.md`. `comun.DIR_PROCESOS` y `cerrojo.ruta_de()`: la sede pasa de `dataset/nodos.jsonl.cerrojo` a **`procesos/nodos.jsonl.<huella>.cerrojo`**, con la huella de la ruta en el nombre **porque el taller de las pruebas usa un dataset que se llama igual** |
| **el caso positivo, re corrido** | `.v34/cerrojo_dos_procesos.py`, dos procesos de verdad: el primero retiene `3` s, **el segundo espera `2,51` s y entra**, y el cerrojo queda suelto al final |
| **la reclasificacion** | suceso `reinicio` en `docs/loop/CREDITO_serial.jsonl` con la cita a este fichero: **`DATO MOVIDO` vuelve a `1 de 2`** |
| **2. el ejemplar que si es dato** | **`TAREA 1` del encargo de la vuelta 34**, con las dos mitades: corregir el nodo por `D.13` y **medir si hay mas nodos con estado de mineria dentro de su texto** |
| **3. la ciega no ve el credito** | el arnes **retira `CREDITO_<linea>.jsonl` alrededor del turno del ciego**, y el orden importa: la herencia `D.40` se calcula ANTES, porque `forja.py herencia` pregunta al registro de que linea es |
| **la cita como referencia** | `credito.cita_es_referencia()` y `forja.py credito --citas`, **en `anotar` y en el SELLO**. El testigo tiene ahora **cuatro guardas** |
| **4. la cola de doctrina** | seccion `COLA DE DOCTRINA` de `docs/loop/TABLERO.jsonl`, **las seis con su medida y su sitio** |
| **5. el encargo y el relanzamiento** | `docs/loop/PROMPT_SIGUIENTE.md`, vuelta 34 |

### La mudanza del cerrojo, con su medida

    $ python .v34/cerrojo_dos_procesos.py
    sede del cerrojo : procesos/nodos.jsonl.66c1fadb.cerrojo
    dentro de dataset/ : NO

    proceso 1: TOMADO por pid 28360 tras esperar 0.00 s
    proceso 2: TOMADO por pid 7396 tras esperar 2.51 s

    el segundo tardo 2.56 s en entrar, y el primero retuvo 3 s
    VEREDICTO: ESPERO, no fallo

### Y CINCO CITAS YA ESCRITAS CAYERON AL ESTRENAR LA GUARDA

**La escribio el auditor de esta misma parada**, y es el ejemplar de lo que el levanto:
`11 SANO`, `en verde`, `13 de 13 pares adjudicados`. **No se borro ninguna:** el texto
entero pasa a `cita_original` y `cita` se queda con la referencia que ese mismo texto ya
traia delante (`REPORTE.md Z.3.a`, `ACTA 32 5.3`). **Se tacha y se pone al lado, que es
como corrige esta casa.**

**Y EL VOCABULARIO SE AFINO ANTES DE ESTRENARLO:** `de 2` y `de 3` **se quedaron fuera a
proposito**, porque cazarian `punto 2 de 3` en una referencia legitima. Esta casa ya pago
dos veces el precio de una guarda con falsos positivos: **se aprende a no mirarla.**

---

# EL CUERPO DE LA PARADA, SIN TOCAR

# PARA ALEXIS. **EL BUCLE SE DETIENE: `DATO MOVIDO` LLEGA A `2 de 2` Y EL CREDITO QUEDA ROTO**

*Escrito por el **auditor** al cerrar la `ACTA 32`, el 17 sep 2026, sobre la vuelta 33 de la linea
`serial` (`extraccion-mundo-11`). Sede del auditor por `AUDITOR_FORJA.md` 5.6. La condicion que lo
dispara es `AUDITOR_FORJA.md` 3, **credito roto**.*

> **`docs/loop/PROMPT_SIGUIENTE.md` queda VACIO**, como manda `AUDITOR_FORJA.md` 3. **El bucle no
> arranca otra vuelta hasta que tu decidas.**

---

## 1. EL MOTIVO, EN CUATRO LINEAS

    $ python forja.py credito
      DATO MOVIDO        2 de 2     ACTA 32  TOPE
      CREDITO ROTO: DATO MOVIDO en su tope.

**`DATO MOVIDO` cae en la vuelta 32 y vuelve a caer en la 33, dos tandas seguidas y sin ninguna
limpia en medio** (`D.38.1`). Su fila la escribiste tu el 16 sep 2026 y dice que **acumula como
las demas: cambia el nombre, no el escalon**, y el escalon de la especie que reclasifico son **dos
tandas**.

**LAS DOS CAIDAS, CON UNA LINEA CADA UNA:**

| tanda | que paso |
|---|---|
| **`ACTA 31`**, vuelta 32 | la `TAREA 4` escribio **`17 sep 2026` dentro de `dataset/` y de `bitacora/` el dia `16`**. Adjudicada por mi predecesor, y **la vuelta 33 la reparo por `D.13` en su tarea bloqueante** |
| **`ACTA 32`**, vuelta 33 | **un cerrojo VIVO entro en `git` dentro de `dataset/`**, y ademas **el grafo afirma hoy, en un nodo que entro en esa vuelta, que un capitulo no esta minado teniendo `16` nodos dentro** |

---

## 2. **LO QUE NO ES EL MOTIVO, Y VA ANTES QUE NADA**

> ### **LA VUELTA 33 ENTREGA SUS TRES TAREAS, Y SUS VEINTE CIFRAS ME SALEN AL DIGITO.**

| lo que recompute con mis comandos | resultado |
|---|---|
| las `10` cifras de apertura y las `10` de cierre | **las `20` al digito**, recontadas del fichero y de `git show` |
| `gate`, `guiones`, aceptacion, resolutor | **VERDES**: `282` nodos, cero guiones, `251` pruebas y `0` fallos |
| los `13` pares de la tanda, adjudicados **a ciegas** antes de ver su reporte | **`13` de `13` COINCIDEN** |
| los `102` pasos de `cap_08`, releidos por mi contra su linea del libro | **`102` TRANSCRIPCION, `0` PUENTE**, igual que su relectura |
| los `11` `SANO` de la tanda, releidos enteros | **`0` caen de `11`** |
| sus `8` discutibles | **`7` se sostienen, y el octavo cae CONTRA MI** |
| mi barrido de vecinos contra el suyo | **`11` y `11`, los mismos ids, poblacion `347` los dos** |

**Y SE DECLARO DOS CAIDAS EL SOLO, SIN QUE NADIE SE LAS PIDIERA:** la especie de esta parada (eligio
la lectura que le costaba el escalon y me dejo a mi la decision) y un orden de `D.30` que rompio.
**Esta parada no es por un trabajo malo: es por una racha que llego a su tope con la ultima caida
declarada por el propio caido.**

---

## 3. EL ESTADO EXACTO, MEDIDO HOY

| pieza | valor | de donde sale |
|---|---|---|
| rama | `extraccion-mundo-11`, linea `serial` | `git rev-parse --abbrev-ref HEAD` |
| `HEAD` al escribir esto | `6a4f694ff420dd2b3b66ad1f38d6b7d1ea8372ee` | `git rev-parse HEAD` |
| fase | **`cap_08` CERRADO EN INSERCION**, `12` de `12`. El lote 4 sigue abierto | `Z.3` del reporte, verificado |
| nodos en el grafo | **282** | recuento mio de `dataset/nodos.jsonl` |
| lineas de bitacora | **410** | recuento mio de `bitacora/VEREDICTOS.jsonl` |
| aristas | **107** por los dos extremos, cero sin reciproco | recuento mio del dataset |
| lote 4 en bandeja | **63**, y **79** archivados de `142`, el `55,63` por ciento | recuento de `cuarentena/` |
| lote 5 en bandeja, en esta rama | **3** | recuento de `cuarentena/` |
| guardas | **`gate` VERDE, `guiones` VERDE, `251` pruebas y `0` fallos** | corridas por mi hoy |
| credito | **`DATO MOVIDO 2 de 2` TOPE**; `REPORTE 1 de 3`, `CIFRA PUBLICADA 1 de 2`, `CLASE 0 de 2`, **`AUDITOR 1 de 3`** | `python forja.py credito` |
| el siguiente capitulo | **`cap_09`, con `20` candidatos en bandeja contra un techo de `15`** | recuento de los JSON |
| los tres frentes | `grove_high_output` **EN CURSO**; `gerber_emyth` y `marquet_turn_the_ship` **PAUSADOS** | `python forja.py tablero` |

---

## 4. LO QUE NECESITO DE TI

### 4.1. **LA DECISION QUE DESBLOQUEA, Y ES UNA SOLA**

**Si la racha sigue o se reinicia**, y con que motivo escrito. `AUDITOR_FORJA.md` 5.4 dice que la
reinicia **una decision tuya archivada en `docs/loop/paradas/`**, y que **un auditor que se reinicia
la racha se esta absolviendo**. Yo no la toco.

**Y AL DECIDIRLO TIENES DELANTE UNA PREGUNTA QUE CAMBIA LA CUENTA:**

> **¿UN CERROJO DE PROCESO QUE VIVE DENTRO DE `dataset/` ES DATO?**
>
> El extractor me ofrecio la lectura contraria y **no la tome**: la fila habla de *una operacion que
> cambia `dataset/`, `bitacora/` o `censos/`*, y `git add -A` cambio lo que `dataset/` contiene en el
> repositorio, con el daño medido y escrito por quien lo reparo (un `checkout` entrega un cerrojo de
> un proceso muerto y la insercion siguiente se queda bloqueada). **Si lees que no lo es, ese
> ejemplar se cae.**
>
> **PERO LA TANDA CAE IGUAL**, y por eso lo pongo aqui: **el segundo ejemplar de la misma tanda no
> lo marco nadie y es contenido puro del dataset.** `dataset/nodos.jsonl` dice hoy, dentro de un
> nodo que entro en la vuelta 33, que *esos tres capitulos NO estan minados todavia*, y **uno de los
> tres tiene `16` nodos y `187` pasos en el grafo**, metidos por la vuelta 32. **La misma vuelta 33
> lo probo**: cablo la arista a ese capitulo. Es la misma figura, la misma sede y la misma fila que
> la caida de la `ACTA 31`.

### 4.2. LAS SIETE PREGUNTAS DE DOCTRINA QUE SUBEN, PORQUE `D.45` NO ME DEJA TOCARLAS

*Ninguna es urgente para retomar. Las siete estan medidas, con su sitio en el acta.*

| # | la pregunta | medida en |
|---:|---|---|
| 1 | **`D.48` contra `D.34.2`, y es la mas seria**: la apertura ciega esta OBLIGADA a leer el registro de credito, y el campo `cita` de ese registro trae **conclusiones del reporte copiadas dentro**. Hoy me dijo `11 SANO` antes de que yo contara los mios. **El arnes retira cuatro ficheros por una puerta y `D.48` abre otra** | `APERTURA_CIEGA.md` 9.1 |
| 2 | **`EXTRACTOR.md` 11 y la banda de `0,4`**: dice que por encima hay gemelos y cero ajenos, acotado al catalogo de la otra casa. Hoy esta casa tiene su **primer par propio a `0,405` leido `SANO`**, por mi y por el, por separado. La medicion no se contradice; **la generalizacion escrita encima si pide su primer contraejemplo** | `ACTA 32` 3.7 |
| 3 | **`src/arista.py:187` teclea `(D.37)`** en toda arista declarada por lectura, y se estampa igual sobre las que son `D.29`. **Quien cuente aristas `D.37` en la bitacora cuenta tambien las `D.29`** | `APERTURA_CIEGA.md` 9.2 |
| 4 | **una cifra en `denominaciones.nombre_largo` que el libro no escribe**: *las cuatro conversaciones* donde `L95` nombra tres. **Segunda vuelta seguida con la figura**, y las dos veces la registre sin cargarla, porque `D.30` cuenta **pasos** | `ACTA 32` 4, fila 2 |
| 5 | **un `resumen_teorico` del dataset que cita `EL REPORTE DE ESTA VUELTA`**: sede duradera apuntando a una que se reescribe cada vuelta | `APERTURA_CIEGA.md` 5.4 |
| 6 | **un orden roto no tiene casillero**: el extractor corrio la relectura de fidelidad con tres nodos ya dentro, contra la letra de `D.30`. No mueve dato, no publica cifra falsa y no mueve veredicto, asi que **lo registre con su nombre y no lo cargue**. Es la tercera vez que aparece un daño sin fila | `ACTA 32` 5.4 |
| 7 | **¿la regla de la busqueda negativa vale para el extractor?** *Una busqueda negativa no se puede citar* esta escrita en `AUDITOR_FORJA.md` 1.1 y **no en `EXTRACTOR.md`**. Su discutible `8` publica *no he encontrado ejemplar previo* y **habia dos en el grafo**. No se lo cargue por eso | `ACTA 32` 3.8 |

### 4.3. **Y UNA COSA QUE NO ES DOCTRINA Y CUESTA CADA VUELTA**

**Dos sesiones escribieron el mismo arbol a la vez.** El cerrojo de `D.44` protege
`dataset/nodos.jsonl` y funciono; **lo que nadie protege es el indice de git**, y por ahi dos
commits del extractor se llevaron **ocho ficheros de otro frente** bajo su mensaje, y un tercero se
llevo el cerrojo. La otra sesion lo declaro en `1954005` y **cortaron la causa los dos**. Lo traigo
porque **es la causa comun de esta parada y del lio de atribucion**, y porque el remedio, si lo
quieres, toca el arnes.

---

## 5. COMO SE RETOMA

1. **Escribe tu decision en `docs/loop/paradas/`** y di si la racha sigue o vuelve a cero, citando
   ese fichero. **El acta siguiente la cita y el registro la anota como `reinicio`**, que es lo que
   `5.4` manda desde siempre.
2. **El trabajo esta limpio y listo:** el lote 4 sigue **CERRADO EN EXTRACCION**, con `63`
   candidatos en bandeja y el grafo en verde. **La vuelta que retome no mina: inserta.**
3. **El capitulo que toca es `cap_09`, y viene con su aviso medido:** tiene **`20` candidatos** y el
   techo son `15`, asi que por `EXTRACTOR.md` 12.4 **la vuelta cerrara corta dentro de `cap_09` y
   tiene que declararlo con su cifra.** Por volumen no hay freno: `PASOS INVENTADOS` de `cap_08`
   dio **`0,00` por ciento** contra un tope de `10`.
4. **Tres deudas pequeñas que no bloquean nada**, para que el encargo que escribas las pueda
   recoger:
   - los **`6` rancios** que la `TAREA 1` de la vuelta 33 produjo al cambiar una huella. `D.15`:
     cola de trabajo, no guarda.
   - la frase del dataset de `4.1`, que pide **una `CORRECCION DECLARADA` por `D.13`, sin borrar**.
   - el **`LEEME.md` que `D.31` pide en `_insertados`** y que `scott_radical_candor` no tiene, ya
     con `79` ficheros dentro.
5. **Y una que es mia:** la `ACTA 31` `4.2` y el encargo de la vuelta 33 publican **`119` fechas
   escritas a mano** en las dos sedes de dato. **No son `119`**: el propio grep pegado ahi suma
   `120` y la poblacion que la frase nombra suma `148`. **Esta corregido en la `ACTA 32` 6 y contado
   en mi racha, que va a `1 de 3`.**

**EL BUCLE NO FUNDE RAMAS Y EL BUCLE NO CREA REMOTOS.** Aqui no se pide ningun merge: los tres
frentes siguen como estaban y `scott_radical_candor` sigue teniendo un solo dueño.
