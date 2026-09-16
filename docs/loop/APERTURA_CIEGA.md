# APERTURA CIEGA DEL AUDITOR, vuelta 30

> Lote 4 (`scott_radical_candor`), la vuelta que INSERTA `cap_07` y la pieza de `cap_11`.
> Escrita ANTES de ver `docs/loop/REPORTE.md`, que no esta en el arbol, y con los otros
> tres ficheros que `D.34.2` retira tampoco en el. **No los he recuperado de `git` ni por
> ninguna otra via.** Lo unico del bucle que he abierto es `docs/loop/ACTA_AUDITOR.md`,
> que es obra mia y que la propia regla me manda leer.

---

## 0. LO QUE EL ARNES EXIGE ANTES QUE NADA (`D.40`)

    ACTA ANTERIOR LEIDA: 148bbd78baae05817d71e200a32bb755a85ca152
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO

**Y LAS TRES VAN CON SU INSTRUMENTO DEBAJO, porque `D.38.3` no hace excepcion con estas.**

### 0.1. `ACTA ANTERIOR LEIDA`: la huella que el prompt me da es la del fichero que abri

    $ git hash-object docs/loop/ACTA_AUDITOR.md
      148bbd78baae05817d71e200a32bb755a85ca152
    $ git rev-parse HEAD:docs/loop/ACTA_AUDITOR.md
      148bbd78baae05817d71e200a32bb755a85ca152
    $ git log --format="%h %s" -1 -- docs/loop/ACTA_AUDITOR.md
      67c651c ACTA 28: la vuelta 28 sale limpia de REPORTE ...

**LECTURA:** la huella que el prompt me entrega es el blob de `docs/loop/ACTA_AUDITOR.md`
tal como esta en mi arbol y tal como esta en `HEAD`. **No lei otra version: lei esa.** Su
ultima acta es la `ACTA 28` y cubre la vuelta 28.

### 0.2. `HEREDADO 1`: CUMPLIDO, **Y CON UNA ROTURA MIA DENTRO QUE DECLARO YO**

> El remedio: *la relectura destapa UNA RAZON POR VEZ, y DESPUES de imprimir sus pasos.
> Nunca un comando que saque varias razones de golpe.*

    $ ls --time-style=+%H:%M:%S -l .v30a/pasos_13.txt .v30a/resumen_destapado_01.txt
      14:49:17  .v30a/pasos_13.txt               (los 96 pasos de los TRECE, sin una sola razon)
      15:03:58  .v30a/resumen_destapado_01.txt   (UN resumen, uno solo, destapado con su comando)

    $ grep -c "^  P" .v30a/pasos_13.txt
      96

**LO QUE CUMPLI.** Los noventa y seis pasos de los trece candidatos estan impresos a las
`14:49:17`, **antes de abrir la fuente y antes de destapar nada**. De los trece resumenes
he destapado **UNO**, con su propio comando, y **ningun comando de esta fase ha sacado dos
razones de golpe**. `bitacora/VEREDICTOS.jsonl` lo he tocado **sin leer un solo campo
`razon`**: lo que saque de ahi fueron ids, clases y longitudes, y se ve en el comando de la
seccion 7.3.

> ### **LO QUE ROMPI, Y NO ME ESCONDO DETRAS DE LA LETRA**
>
> Al empezar la fase corri un comando para averiguar la forma del fichero de candidato, y
> volque **el JSON entero** de `compartir_logica_mostrar_razonamiento`. Ese volcado trae
> sus pasos **y trae su `resumen_teorico`**, que es donde el extractor escribe su propia
> relectura de fidelidad. **Por la letra el remedio aguanta**: fue una razon, una sola, y
> sus pasos salieron impresos encima de ella en la misma salida. **Por el fondo no**: yo
> todavia no habia adjudicado nada, asi que vi su lectura antes de tener la mia.
>
> **CONSECUENCIA, Y LA APLICO YO:** de las trece clases de la seccion 4, **la de
> `compartir_logica_mostrar_razonamiento` NO la reclamo como ciega.** Las otras doce si.
> Si el acta decide que esto es `REMEDIO ROTO` de sustancia, **es mio, y esta escrito aqui
> antes de que nadie me lo encuentre.**

### 0.3. `HEREDADO 2`: CUMPLIDO, y es un metodo, no una tarea

> El heredado prueba con `git` una cronologia que se podia haber supuesto, y su frase es
> *DESPUES: el arreglo entro a las `09:23:24` y las diez lineas a las `09:50:39`*.

**LO APLICO A TRES SITIOS DE ESTA FASE, y estos son los comandos:**

    $ git log --diff-filter=R --find-renames=100% --name-status --format="" b9f484a..HEAD -- cuarentena | grep -c '^R100'
      13

    $ git log --format="%h %ad %s" --date=format:"%H:%M:%S" -1 -- src/cerrojo.py
      585a609 13:02:56 D.44 el censo no decrece, el cerrojo de insercion, y D.45 ...
    $ git log --format="%h %ad %s" --date=format:"%H:%M:%S" -1 8e626b6
      8e626b6 13:20:14 VUELTA 30 APERTURA: el esqueleto del reporte abierto antes ...
    $ git log --format="%h %ad %s" --date=format:"%H:%M:%S" -1 -- dataset/nodos.jsonl
      5834c50 14:18:54 VUELTA 30 TAREA 2: entra bloquear_tiempo_pensar_calendario ...

**LECTURA 1:** los trece candidatos que he leido entraron a `_insertados` como **renombrado
al cien por cien**, asi que **el texto que yo he clasificado es byte a byte el que estaba en
la bandeja**, y no una copia reescrita al insertar. **Medido, no supuesto.**

**LECTURA 2:** el remedio de fondo que el heredado dejaba abierto era su **propuesta 8**, la
de dos corridas mias en paralelo escribiendo el dataset. **Esa propuesta ya tiene sede en
`src/`**, y entro a las `13:02:56`, **dieciocho minutos antes de que la vuelta 30 abriera**
(`13:20:14`) y una hora y cuarto antes de que tocara el dataset por ultima vez (`14:18:54`).
El heredado ya no depende de mi: **depende de que el cerrojo muerda, y eso lo mido en 7.5.**

---

## 1. QUE TENGO DELANTE Y QUE NO

    $ git status --porcelain docs/loop/
       D docs/loop/APERTURA_CIEGA.md
       D docs/loop/REPORTE.md
       D docs/loop/loop.log
       M docs/loop/ultimo_apertura.json
       D docs/loop/ultimo_auditor.json
       D docs/loop/ultimo_extractor.json

**LECTURA:** los cuatro de `D.34.2` estan fuera del arbol, como tienen que estar. **El
quinto, `docs/loop/ultimo_apertura.json`, no esta fuera: esta VACIO**, y eso tiene
consecuencias que no son de forma. Estan medidas en la seccion 7.4.

**EL MATERIAL QUE SI HE ABIERTO:** los trece candidatos de la vuelta en
`cuarentena/_insertados/scott_radical_candor/`, el candidato
`pelear_proliferacion_reuniones_bloquear_ejecucion` que sigue en la bandeja,
`fuentes/scott_radical_candor/cap_07.md` entero y las lineas `163` a `175` y `221` a `235`
de `fuentes/scott_radical_candor/cap_11.md`.

**Y NO HE ABIERTO `.v30e/`**, que es el directorio de trabajo del extractor de esta vuelta:
ahi viven sus salidas de gate, sus cuadres y sus tandas, y leerlas seria leer el reporte por
la puerta de atras. Mis cifras salen de instrumentos corridos por mi en `.v30a/`.

---

## 2. LA POBLACION DEL BARRIDO, Y LA RECETA DE `D.38.4` ESTA CADUCADA

**`D.38.4` manda barrer sobre GRAFO MAS BANDEJAS, y trae la receta escrita.** La corri tal
como esta escrita, con la exclusion del propio candidato que la `ACTA 18` le anadio, y esto
es lo que devolvio:

    $ (poblacion del banco: dataset mas cuarentena, menos _insertados y _derivadas)
      grafo 256  bandejas 255  poblacion 511
    $ FORJA_DATASET=<esa poblacion menos el propio candidato> python forja.py informe --carpeta <uno>
      poblacion del barrido       : 602   (510 del grafo mas 92 que esperan en bandejas)
      vecinos levantados en total : 8
      vecino calibrar_ascensos_evitar_politica  [levantada por: paso_contra_nodo]
        similitud_texto 0.223 | familia_id 0.000 | paso_contra_nodo 0.911
      vecino calibrar_ascensos_evitar_politica  [levantada por: paso_contra_nodo]
        similitud_texto 0.223 | familia_id 0.000 | paso_contra_nodo 0.911

**LECTURA, Y ES UNA AVERIA DE LA RECETA, NO DEL BARRIDO:** le paso **510** lineas y el
instrumento anuncia **602**. La diferencia son **92 que cuenta dos veces**, y se ven a ojo
en la lista: cada vecino que esta en la bandeja **sale repetido, con las tres señales
identicas**. La causa esta en el codigo y es de fecha:

    $ grep -n "poblacion = list(nodos)" src/aduana.py
      967:    poblacion = list(nodos) + list(bandejas)

**`D.38.5` (12 sep) hizo que la aduana cargue las bandejas POR SU CUENTA.** La receta de
`D.38.4` es del 11 sep y mete las bandejas **en el fichero que le pasas**. Corridas juntas,
**la bandeja entra dos veces**. Un auditor que cumpla la receta al pie de la letra hoy
publica una poblacion inflada en 92 y una cola de vecinos con duplicados.

**Y HAY UNA SEGUNDA MITAD:** la receta mete tambien los **163** de
`cuarentena/ensayo_referencia_163/`, que la aduana descarta a proposito porque **sus fuentes
no estan en la tabla canonica y no podrian entrar nunca**. Por eso su cuenta dice `92` donde
la mia decia `255`.

> **LO ADJUDICO CITANDO, QUE ES LO QUE `1.3` ME DEJA HACER, Y NO ES DOCTRINA NUEVA.**
> Entre dos reglas fechadas que chocan gana la mas reciente (`D.13`): manda `D.38.5`, que es
> del 12, sobre la receta de `D.38.4`, que es del 11. **La forma correcta hoy es pasarle al
> instrumento SOLO el grafo menos el propio candidato y dejar que el ponga las bandejas.**

**ASI ES COMO BARRI LOS TRECE, y esta es la poblacion, la misma en los trece:**

    $ FORJA_DATASET=<grafo menos el propio candidato> python forja.py informe --carpeta <uno>
      poblacion del barrido       : 347   (255 del grafo mas 92 que esperan en bandejas)

    $ wc -l dataset/nodos.jsonl
      256 dataset/nodos.jsonl
    $ ls cuarentena/scott_radical_candor/*.json | wc -l
      89
    $ ls cuarentena/marquet_turn_the_ship/*.json | wc -l
      3

**LECTURA:** `256` menos el candidato es `255`, y `89` mas `3` es `92`. **La poblacion de
mi barrido es `347` y cuadra con los dos `wc` de arriba sin que sobre ni falte uno.**

---

## 3. MI RELECTURA DE FIDELIDAD `D.30`, CONTADA POR CAPITULO

**La cuenta primero, con su instrumento:**

    $ (contador de pasos sobre los trece ficheros de candidato)
      cap_07 : 12 nodos, 90 pasos
      cap_11 :  1 nodo,   6 pasos
      TOTAL  : 13 nodos, 96 pasos
    $ grep -c "^  P" .v30a/pasos_13.txt
      96

**LO QUE EL INSTRUMENTO MIDIO:** cuantos pasos escribio la vuelta y en que capitulo cae cada
nodo. **Nada mas. La cuenta de PUENTE no la da ningun instrumento: la doy yo leyendo, y por
eso va marcada.**

> **LECTURA (mia, y es una conclusion sobre contenido, no una medida):** he leido los
> **noventa y seis** pasos contra el parrafo de la fuente que les toca, uno por uno, y **los
> noventa y seis los dice el libro**. Mi cuenta de `PASOS INVENTADOS` para esta tanda es:
>
> | capitulo | pasos escritos | PUENTE que yo veo | por ciento |
> |---|---|---|---|
> | `cap_07` | 90 | 0 | 0,00 |
> | `cap_11` | 6 | 0 | 0,00 |
> | **total de la tanda** | **96** | **0** | **0,00** |
>
> **Y DIGO CUALES SON LAS DOS QUE MAS CERCA ESTUVIERON DE CAERSE**, porque una cuenta de
> cero sin sus casos limite no vale nada:
>
> 1. `repartir_decision_cercanos_hechos` `P07`, *ve a su reunion y mira a la sala, no al que
>    habla*. El libro **narra** que la autora fue a la reunion de Mark y miro alrededor
>    (`L275`); **no lo escribe como orden**. Lo dejo en TRANSCRIPCION porque el paso cita la
>    narracion entera y no anade ningun inventario que el libro no tenga, pero **es el que
>    mas lejos esta del imperativo literal**.
> 2. `reservar_calendario_tiempo_ejecutar` `P04`, *bloquea ese tiempo*. El parrafo (`L387`)
>    **no dice bloquea**: lo dice el rotulo de encima, `Block time to execute` (`L385`).
>    Rotulo es texto, asi que TRANSCRIPCION, **pero el verbo viene del rotulo y no del
>    cuerpo**.

**LA PIEZA QUE MAS ME CONVENCIO DE QUE LA MANO FUE FIEL**, y la digo porque es la prueba por
el lado contrario: `bloquear_tiempo_pensar_calendario` sale de `cap_11` `L165` a `L173`,
donde el libro cuenta el caso del consejero delegado que bloqueaba **dos horas** diarias. El
paso `P03` dice *agenda algo de tiempo para pensar*, **sin cantidad**, que es exactamente lo
que dice `L173` (*schedule in some think time*). **Poner ahi las dos horas habria sido el
puente que `D.30` llama el periodo, y no esta puesto.**

---

## 4. LA CLASIFICACION DE LOS TRECE, QUE ES A LO QUE VENGO

**Como la hice:** imprimi los noventa y seis pasos a las `14:49:17` sin una sola razon,
abri `cap_07.md` y las dos ventanas de `cap_11.md`, y **adjudique cada candidato contra su
parrafo y contra sus vecinos antes de destapar nada.** La unica clase que **no** reclamo
como ciega es la de `compartir_logica_mostrar_razonamiento`, por lo que declare en `0.2`.

| # | candidato | fuente | pasos | MI CLASE |
|---|---|---|---|---|
| 1 | `bloquear_tiempo_pensar_calendario` | `cap_11` `L165-173` | 6 | **SANO**, nodo propio |
| 2 | `compartir_logica_mostrar_razonamiento` | `cap_07` `L359-365` | 6 | **SANO** (no ciega) |
| 3 | `cuidarse_agotamiento_centro_rueda` | `cap_07` `L409-419` | 7 | **SANO**, nodo propio |
| 4 | `establecer_credibilidad_pericia_humildad` | `cap_07` `L349-357` | 9 | **SANO**, nodo propio |
| 5 | `fijar_fecha_cierre_debate_equipo` | `cap_07` `L245-257` | 11 | **SANO fusionado**, y es mi discutible 1 |
| 6 | `mantener_manos_trabajo_real_equipo` | `cap_07` `L381-383` | 8 | **CONTINUA** de la cabeza de EXECUTE |
| 7 | `minimizar_impuesto_colaboracion_equipo` | `cap_07` `L367-373` | 4 | **SANO**, y es la CABEZA de la serie |
| 8 | `parar_debate_emocion_agotamiento` | `cap_07` `L235-237` | 5 | **SANO**, nodo propio |
| 9 | `pedir_hechos_decision_evitar_recomendaciones` | `cap_07` `L291-293` | 5 | **SANO**, nodo propio |
| 10 | `persuadir_emocion_oyente_no_propia` | `cap_07` `L303-347` | 11 | **SANO**, y es mi discutible 2 |
| 11 | `proteger_tiempo_equipo_jefe` | `cap_07` `L375-379` | 9 | **CONTINUA** de la cabeza de EXECUTE |
| 12 | `repartir_decision_cercanos_hechos` | `cap_07` `L259-289` | 11 | **SANO**, nodo propio |
| 13 | `reservar_calendario_tiempo_ejecutar` | `cap_07` `L385-387` | 4 | **CONTINUA**, y es mi discutible 3 |

**LA SERIE QUE LEO, y la leo del libro y no de ninguna declaracion:** `L373` dice, con estas
palabras, *aqui estan las tres cosas que he aprendido sobre acertar con ese equilibrio: no
malgastes el tiempo de tu equipo; conserva la tierra bajo tus uñas; y bloquea tiempo para
ejecutar.* **Esa linea nombra a los nodos 11, 6 y 13 en ese orden y los cuelga del nodo 7.**
Asi que la forma que le veo a EXECUTE es **una madre con tres hijas**, y las tres son
CONTINUA de la misma madre. **Si esta tanda no cableo esas tres aristas, es una perdida de
estructura que el libro escribe en una sola linea.** (Lo comprobe despues, y estan: la
medida esta en `5.1`, y las tres salen ahi como pares que solo tiene ella.)

### 4.1. Mis tres discutibles, marcados ANTES de saber si acierto

**DISCUTIBLE 1, `fijar_fecha_cierre_debate_equipo`: un nodo sobre DOS rotulos.**
El candidato cubre `Be clear when the debate will end` (`L245-249`) **y**
`Don't grab a decision just because the debate has gotten painful` (`L251-257`). Los otros
doce respetan un rotulo cada uno. **Mi adjudicacion es que la fusion se sostiene**, y no por
tamaño sino por la vara: el remedio que el segundo rotulo receta **es el primero**, dicho por
el libro en `L257` (*lo correcto habria sido poner una fecha de decidir*). Separarlos daria un
nodo cuyo entregable es el paso 3 del otro. **Pero lo marco yo, porque es la unica costura de
la tanda donde dos rotulos entran en un nodo.**

**DISCUTIBLE 2, `persuadir_emocion_oyente_no_propia` contra
`establecer_credibilidad_pericia_humildad`: los dos beben de `L313`.**
El parrafo de cabecera de PERSUADE dice las tres cosas de golpe: que explicar no basta porque
solo atiende a la logica, que hay que atender a las emociones del que escucha, **y** que hay
que establecer la credibilidad del que decide. El nodo 10 se lleva la mitad de emocion
(`P01` a `P04`) y el nodo 4 se lleva la de credibilidad (`P01`). **Mi adjudicacion: no es
duplicado, es reparto legitimo de un parrafo de cabecera**, porque lo que queda fuera es
procedimiento en los dos lados (las dos preguntas a Jason en uno, el *nosotros* de Jobs y la
salida del que no tiene historial en el otro). **La vara no tiene bascula y aqui no la uso.**

**DISCUTIBLE 3, y es el que mas me importa: `reservar_calendario_tiempo_ejecutar` contra
`pelear_proliferacion_reuniones_bloquear_ejecucion`, QUE SIGUE EN LA BANDEJA.**
Tiene su seccion propia, la 6, porque no es solo una clase: es una comprobacion de si `D.38.4`
esta sirviendo para algo.

---

## 5. EL BARRIDO DE VECINOS DE LOS TRECE, UNO POR VEZ

**Metodo:** un candidato por corrida, con su propio id fuera de la poblacion (`ACTA 18`), y
con la correccion de la seccion 2 puesta. **Trece corridas, la misma poblacion en las trece.**

| candidato | vecinos que levanta | que señal los levanta |
|---|---|---|
| `bloquear_tiempo_pensar_calendario` | 5 | familia_id 1, paso_contra_nodo 3, similitud_texto 1 |
| `compartir_logica_mostrar_razonamiento` | 10 | similitud_texto 10 |
| `cuidarse_agotamiento_centro_rueda` | 5 | similitud_texto 5 |
| `establecer_credibilidad_pericia_humildad` | 3 | similitud_texto 3 |
| `fijar_fecha_cierre_debate_equipo` | 4 | paso_contra_nodo 1, similitud_texto 3 |
| `mantener_manos_trabajo_real_equipo` | 8 | similitud_texto 8 |
| `minimizar_impuesto_colaboracion_equipo` | 10 | similitud_texto 10 |
| `parar_debate_emocion_agotamiento` | 9 | similitud_texto 9 |
| `pedir_hechos_decision_evitar_recomendaciones` | 7 | similitud_texto 7 |
| `persuadir_emocion_oyente_no_propia` | 3 | similitud_texto 3 |
| `proteger_tiempo_equipo_jefe` | 10 | paso_contra_nodo 1, similitud_texto 9 |
| `repartir_decision_cercanos_hechos` | 1 | similitud_texto 1 |
| `reservar_calendario_tiempo_ejecutar` | 7 | familia_id 2, similitud_texto 5 |

    $ cat .v30a/barrido2/*.txt | grep -c '^    vecino '
      82

### 5.1. El cruce contra lo que la vuelta escribio, con los ids y sin una sola razon

    $ (cruce de mi barrido ciego contra los pares que la vuelta escribio en la bitacora)
      pares distintos que levanto YO      : 82
      pares distintos que escribio ELLA   : 86
      en los dos                          : 82
      SOLO mios                           : 0
      SOLO suyos                          : 4

      bloquear_tiempo_pensar_calendario       solo suyo: agendar_cuidados_propios_cumplirlos
      cuidarse_agotamiento_centro_rueda       solo suyo: aprender_resultados_vencer_dos_presiones
      mantener_manos_trabajo_real_equipo      solo suyo: minimizar_impuesto_colaboracion_equipo
      reservar_calendario_tiempo_ejecutar     solo suyo: minimizar_impuesto_colaboracion_equipo

> **LECTURA:** **los ochenta y dos pares que levanta mi barrido estan los ochenta y dos entre
> los suyos, y no hay ni uno que solo vea yo.** Los cuatro que solo tiene ella **no los
> levanta ninguna señal**: son los que se ponen leyendo, y tres de los cuatro son la serie que
> yo lei sola en `L373` antes de mirar nada suyo (seccion 4). **Eso es exactamente el reparto
> que `D.19` describe: la señal dice donde mirar, y ahi acaba su trabajo.**
>
> **Y DIGO EL LIMITE DE MI PROPIA MEDIDA:** yo barro contra el grafo **ya terminado**, con
> los trece dentro; ella barrio contra un grafo que crecia nodo a nodo. **Que los dos
> conjuntos coincidan en 82 sin que sobre ninguno por mi lado significa que el orden de
> insercion no le escondio ningun par**, y eso es lo que yo podia comprobar y ella no.

---

## 6. MI DISCUTIBLE 3, QUE ES EL QUE TIENE CONSECUENCIA: **UN PAR CON UN EXTREMO EN LA BANDEJA**

**El par:** `reservar_calendario_tiempo_ejecutar` (entro en esta vuelta, `cap_07` `L385-387`,
rotulo `Block time to execute`) contra `pelear_proliferacion_reuniones_bloquear_ejecucion`
(**sigue en la bandeja**, `cap_11` `L223-233`, rotulo `Fight meeting proliferation`).

**Los dos mandan el mismo acto, y lo mando el mismo libro:**

    cap_07 L385  (rotulo)  Block time to execute
    cap_11 L233            For the same reason I blocked off think-time in calendar; I also
                           found it necessary to block off time in my calendar to be alone
                           and execute. I encouraged others to do the same.

**MI ADJUDICACION, hecha con la vara y sin bascula:** **no son duplicado, son CONTINUA**, y la
direccion es `cap_07` madre y `cap_11` hija. Lo que queda fuera es procedimiento en los dos
lados: la hija trae **los tres remedios que el libro prueba y descarta** (quitar las sillas,
el dia sin reuniones, terminar antes la cuarta parte) y el encargo al equipo; la madre trae
**la causa de por que ese tiempo no aparece nunca en el calendario** (que lo usamos para lo
colaborativo) y lo ata al plan ya decidido y aceptado. **Pero la arista es obligatoria**, y
sin ella el grafo dice dos veces lo mismo sin decir que lo dice dos veces.

### 6.1. Y AQUI ESTA LA CONSECUENCIA, MEDIDA: **NADIE VA A LEVANTAR ESE PAR**

    $ grep "^    vecino " .v30a/barrido2/reservar_calendario_tiempo_ejecutar.txt
      vecino bloquear_tiempo_pensar_calendario      [familia_id]
      vecino proteger_tiempo_equipo_jefe            [similitud_texto]
      vecino cambiar_posicion_hechos_explicar_cambio [similitud_texto]
      vecino mantener_manos_trabajo_real_equipo     [similitud_texto]
      vecino parar_debate_emocion_agotamiento       [similitud_texto]
      vecino reservar_tiempo_reflexion_metas        [familia_id]
      vecino crear_obligacion_disentir_equipo       [similitud_texto]

**Siete vecinos, y `pelear_proliferacion_reuniones_bloquear_ejecucion` no esta**, aunque los
92 de la bandeja estaban dentro de la poblacion. **Asi que lo probe por el otro lado, que es
lo que decide:**

    $ python forja.py informe --carpeta <solo pelear_proliferacion...>
      poblacion del barrido       : 348   (256 del grafo mas 92 que esperan en bandejas)
      EL SALDO
        ENTRARIAN sin leer nada          : 1
        BLOQUEARIAN esperando veredicto  : 0
      vecinos levantados en total      : 0

> **LECTURA, Y ES LA MAS SERIA QUE TRAIGO:** el dia que ese candidato llegue a la puerta,
> **la aduana lo dejara pasar SIN MANDAR LEER NADA**, con el nodo que dice su mismo acto ya
> dentro del grafo. **Las tres señales lo dan por desconocido en las dos direcciones.** No es
> un fallo de esta vuelta: la vuelta 30 no tenia ese candidato delante. **Es un agujero que
> se cierra ahora, con una lectura, o no se cierra nunca**, porque despues de entrar ya no
> habra ninguna corrida que los ponga juntos.
>
> **Y es justo el caso que `D.38.4` puso por escrito:** *un vecino que esta en la bandeja es
> vecino*. Aqui la bandeja estaba en la poblacion **y aun asi la señal no llego**. `D.38.4`
> puso la poblacion correcta; **lo que este par enseña es que la poblacion correcta no basta
> cuando las tres señales no se tocan.**

### 6.2. La otra arista que echo de menos, y esta si tenia los dos extremos dentro

    $ (paso 7 de cuidarse_agotamiento_centro_rueda, que entro a las 14:12)
      Bloquea en tu calendario tiempo de pensar todos los dias. El texto dice que buena parte
      de esa dureza mental venia de hacer cosas como bloquear dos horas de tiempo de pensar al dia.

    $ (entregable de bloquear_tiempo_pensar_calendario, que entro a las 14:18)
      El tiempo para pensar bloqueado en tu calendario y mantenido, con tu equipo avisado de
      que ahi no se agenda y animado a bloquear el suyo.

    $ (aristas de los dos nodos en el grafo)
      cuidarse_agotamiento_centro_rueda  previos=['aprender_resultados_vencer_dos_presiones'] siguientes=[]
      bloquear_tiempo_pensar_calendario  previos=[] siguientes=[]

> **LECTURA:** el paso 7 de uno **nombra el acto que el otro despliega entero**, que es
> palabra por palabra la figura que esta misma vuelta uso para cablear
> `bloquear_tiempo_pensar_calendario` contra el paso 30 del plan de `cap_12`. **La tenia en la
> mano y la aplico en una direccion y no en esta.** Los dos nodos entraron el mismo dia con
> seis minutos de diferencia y el segundo entro **despues**, asi que el primero ya vivia en el
> grafo cuando el segundo paso por la puerta. **Lo marco como par a adjudicar, no como caida:
> puede que haya una razon escrita, y esa razon la destapare en mi turno, de una en una.**

---

## 7. EL ESTADO DEL ARBOL, MEDIDO POR MI EN ESTA MISMA FASE

**Cuatro instrumentos de la casa, corridos por mi, con su salida pegada. Uno de ellos salio
ROJO por culpa mia y lo digo en el primer renglon, que es donde se dice.**

### 7.1. El gate: VERDE, y su cuenta cuadra con la del testigo del arnes

    $ python forja.py gate
      GATE VERDE.
        nodos verificados: 256
        guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
                 vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
                 arista_incompleta, guiones, censo_no_decrece

    $ (docs/loop/TESTIGO_GUARDAS.json, escrito por el arnes a las 12:37:12 sobre 97584af)
      "gate": { "estado": "VERDE", "salida": "GATE VERDE. nodos verificados: 243" }

**LECTURA:** `243` antes de la vuelta y `256` despues son **trece nodos**, que son
exactamente los trece ficheros que la vuelta movio a `_insertados` (`0.3`, primer comando).
**Las dos cuentas y el conteo de renombrados dicen trece por tres caminos distintos.**

### 7.2. El barrido de guiones: **SALIO EN ROJO Y LOS 27 HALLAZGOS ERAN MIOS**

    $ python forja.py guiones
      BARRIDO DE GUIONES EN ROJO: 27 hallazgo(s)
        .v30a/pob_cuidarse_agotamiento_centro_rueda.jsonl linea 327 columna 1687: guion largo (U+2014)
        ... (27 en total)
    $ (de que fichero es cada hallazgo)
           9   .v30a/pob_cuidarse_agotamiento_centro_rueda.jsonl
           9   .v30a/pob_sin.jsonl
           9   .v30a/poblacion.jsonl

**LECTURA, Y ES LA CAIDA QUE `D.45` NACIO PARA CAZAR:** los veintisiete estan en **ficheros
de trabajo mios**, creados en esta fase por la receta de la seccion 2. Los guiones largos los
traen los nodos de `ensayo_referencia_163`, que la receta mete en la poblacion. **Ni uno solo
esta en el arbol de la casa.** Retire los tres ficheros, que ya no me hacian falta al corregir
la receta, y volvi a medir:

    $ rm -f .v30a/poblacion.jsonl .v30a/pob_sin.jsonl .v30a/pob_cuidarse_agotamiento_centro_rueda.jsonl
    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**LO DIGO ENTERO Y NO SOLO EL VERDE:** la vuelta 28 me costo un escalon por publicar
`guardas en rojo: 2` cuando eran `3` **y la tercera era mia**. Hoy fue `1` en rojo, la mia,
y **no la descubro al cerrar: la descubro midiendo, la nombro, la quito y vuelvo a medir.**

### 7.3. La vigencia (`D.15`): 26 RANCIO y 8 SIN HUELLA, y las ocho tienen una forma

    $ python forja.py rancios
      BLOQUE DE VIGENCIA: 34 hallazgo(s) sobre 361 veredicto(s) y 0 cita(s).
        RANCIO 26, SIN HUELLA 8
        lineas declaradas NO CONSUMADAS y por eso no medidas: 14

    $ wc -l bitacora/VEREDICTOS.jsonl
      375 bitacora/VEREDICTOS.jsonl

**LECTURA 1:** `361` mas `14` es `375`, asi que el bloque de vigencia **mide toda la bitacora
y no una parte**.

    $ (los vecinos que nombran las 8 lineas SIN HUELLA)
      2 compartir_logica_mostrar_razonamiento
      1 crear_obligacion_disentir_equipo
      1 fijar_fecha_cierre_debate_equipo
      1 mantener_manos_trabajo_real_equipo
      1 minimizar_impuesto_colaboracion_equipo
      1 parar_debate_emocion_agotamiento
      1 proteger_tiempo_equipo_jefe
    $ (cruce contra los trece de la vuelta)
      lineas SIN HUELLA     : 8
      nombran uno de los 13 : 7
      nombran otro          : ['crear_obligacion_disentir_equipo']

> **LECTURA 2, y es de mecanismo:** las ocho lineas `SIN HUELLA` **nombran, sin excepcion, a
> un nodo que hoy vive en el grafo y que el dia en que se escribio el veredicto estaba en la
> BANDEJA.** Siete de los ocho entraron en esta misma vuelta; el octavo,
> `crear_obligacion_disentir_equipo`, es el nodo que la vuelta 28 perdio y recupero.
> **`D.38.5` hizo que la aduana midiera contra la bandeja, que era lo que faltaba, pero la
> huella que guarda de un vecino de bandeja es la de un nodo VACIO**, asi que esos veredictos
> **no se pueden comprobar nunca contra el texto con el que se emitieron.** No es una caida
> de nadie de esta vuelta: **es el precio que `D.38.5` dejo sin pagar**, y sale a ocho lineas
> en una sola tanda.

### 7.4. **EL CENSO DE RUTAS (`D.42`) ESTA EN ROJO, Y CON EL EL SELLO DE ESTA PAGINA**

**Es la medida mas importante de esta apertura y por eso va con todo lo que hace falta para
reproducirla.** El testigo de `D.45` corre tres guardas antes de sellar, y la tercera es esta:

    $ grep -n "censo_rutas" scripts/testigo_guardas.py
      65:    ("censo_rutas", [sys.executable, os.path.join("scripts", "censar_rutas.py")]),

    $ python scripts/censar_rutas.py
      rutas publicadas y censadas : 96
        pasan                     : 94
        CAEN                      : 2

      CAE  docs/loop/ACTA_AUDITOR.md linea 2583, celda 1
           ruta : docs/loop/loop.log
           NO esta en el arbol, y la celda no lleva la marca 'VACIA A PROPOSITO: motivo'

      CAE  docs/loop/ACTA_AUDITOR.md linea 14622, celda 1
           ruta : docs/loop/ultimo_apertura.json
           esta y esta VACIA, y la celda no lleva la marca 'VACIA A PROPOSITO: motivo'

      CENSO EN ROJO: 2 ruta(s) publicadas como sede de una cifra no sostienen nada.
      EXIT=1

> **LECTURA, Y LA ESCRIBO SABIENDO QUE ME PERJUDICA:** las dos celdas que caen son **de mi
> propia acta**, y las dos caen **por lo que esta fase le hace al arbol**. `loop.log` no
> esta porque `D.34.2` lo retira para que yo lea a ciegas. `ultimo_apertura.json` esta a
> **cero bytes** porque el arnes lo vacia antes de invocarme. **Las dos rutas sostenian su
> cifra cuando se escribieron y las dos dejan de sostenerla mientras dura mi turno.**
>
> **LO QUE ESO SIGNIFICA PARA ESTA PAGINA, dicho por `D.45` y no por mi:** *si una guarda
> esta en rojo en el instante del sello, el sello no se acepta, y el arnes se detiene
> nombrandola.* **Asi que esta apertura, medida como esta el arbol ahora mismo, no se puede
> sellar.**
>
> **Y NO LO ARREGLO YO, y digo por que en vez de arreglarlo:**
>
> 1. **Regenerar el fichero** es la primera salida que el censo ofrece, y en mi caso seria
>    recuperar `loop.log`. **Eso es exactamente lo que el prompt me prohibe** y lo que
>    invalida mi apertura. La salida existe y no la puedo usar.
> 2. **Escribir `VACIA A PROPOSITO` en la celda** seria escribir en una sede duradera una
>    frase **que es cierta durante hora y media y falsa el resto del tiempo**: los dos
>    ficheros vuelven en cuanto mi turno acaba. **Eso es una cifra publicada falsa a plazo**,
>    y la pondria yo con mi mano en mi propia acta.
> 3. **Es la misma averia que el arnes ya se arreglo un piso mas arriba**, y esta medido:
>
>        $ git log --format="%h %ad %s" --date=format:"%H:%M" -1 97584af
>          97584af 11:29 ARNES: el tallado reventaba en la fase ciega y habria dejado al
>                        arnes sin poder sellar
>
>    `tallar_reporte.py` aprendio a decir `TALLADO SIN OBJETO: docs/loop/REPORTE.md no esta
>    en el arbol. La fase ciega lo retira A PROPOSITO (D.34.2)`. **`censar_rutas.py` no lo
>    aprendio.** Y `AUDITOR_FORJA.md` es explicito en que esto **es tarea del arnes y no
>    remedio mio**: *un remedio sobre formato de artefactos no existe como remedio.*
>
> **LO DEJO MEDIDO, NOMBRADO Y CON SU CAUSA, que es lo unico que esta fase me deja hacer.**

**Y LO VUELVO A MEDIR CON ESTA PAGINA YA ESCRITA, porque `D.45` es justamente sobre eso:**

    $ python scripts/censar_rutas.py        (con docs/loop/APERTURA_CIEGA.md ya en el arbol)
      rutas publicadas y censadas : 97
        CAEN                      : 2
      CAE  docs/loop/ACTA_AUDITOR.md linea 2583, celda 1
      CAE  docs/loop/ACTA_AUDITOR.md linea 14622, celda 1
      CENSO EN ROJO: 2 ruta(s) publicadas como sede de una cifra no sostienen nada.

**LECTURA:** de `96` a `97` porque esta pagina publica una celda mas, **y esa pasa**. **Las
dos que caen siguen siendo las dos mismas de mi acta: esta pagina no añade ni una.** Y las
otras dos guardas, medidas en este mismo minuto y con esta pagina dentro del arbol:

    $ python forja.py gate
      GATE VERDE.  nodos verificados: 256
    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

### 7.5. La prueba de aceptacion: **192 pruebas, 4 fallos**, y los cuatro son de esta fase

    $ python tests/test_aceptacion.py
      total: 192 pruebas, 4 fallos, 0 errores
      FAIL: test_caso_positivo_una_ruta_de_CERO_BYTES_es_caida_de_cifra (PruebaTallado)
      FAIL: test_el_estricto_tumba_lo_que_el_hook_deja_pasar (PruebaTallado)
      FAIL: test_el_informe_nombra_la_fila_y_manda_regenerar (PruebaTallado)
      FAIL: test_e_guion_largo_rompe_el_hook (PruebaE)

    $ (el motivo que imprimen los tres primeros, literal)
      AssertionError: 'TALLADO EN ROJO' not found in 'TALLADO SIN OBJETO:
      docs/loop/REPORTE.md no esta en el arbol. La fase ciega lo retira A PROPOSITO (D.34.2)'

    $ (el motivo del cuarto, literal)
      AssertionError: 1 != 0 : el repo ha de estar limpio antes de ensuciarlo
      [pre-commit] COMMIT ABORTADO: ... una ruta publicada como sede de una cifra no sostiene nada

> **LECTURA:** los tres primeros fallan **porque el arreglo de las `11:29` funciono**: el
> tallado ya no revienta, devuelve `SIN OBJETO`, **y sus tres pruebas siguen esperando el
> `ROJO` de antes.** El arreglo entro sin que sus pruebas aprendieran la fase nueva, asi que
> **la suite de aceptacion queda en rojo durante TODAS las fases ciegas a partir de hoy.**
> El cuarto no es una prueba distinta: es la misma piedra de `7.4` vista desde el hook.
>
> **NINGUNO DE LOS CUATRO TOCA UN NODO, UN VEREDICTO NI UNA CIFRA DEL GRAFO.** Lo digo
> entero para que nadie lea *cuatro fallos* y piense que la tanda esta rota: **la tanda pasa
> el gate con sus 256 nodos y sus trece guardas.**

### 7.6. Lo que mire de la bitacora sin destapar una sola razon

    $ (cuenta sobre bitacora/VEREDICTOS.jsonl, campos 'veredicto' y longitud de 'razon')
      veredictos antes de la vuelta 30 : 289
      veredictos ahora                 : 375
      escritos por la vuelta 30        : 86
      por veredicto                    : SANO 80, CONTINUA 6
      con arista                       : 6
      candidatos distintos             : 13
      SIN razon escrita (D.8)          : 0
      largo minimo de razon            : 125 caracteres

**LECTURA:** `D.8` dice que un `SANO` sin razon escrita es una caida **aunque acierte, y que
se ve en la bitacora sin releer nada**. **Las 86 lineas traen razon, y la mas corta tiene 125
caracteres.** De esa cuenta sale tambien el tamaño de mi muestra pineada para el acta:
`80` SANO, el veinte por ciento, **16 relecturas**, por debajo del techo de veinte que fija
la seccion 7 del protocolo.

---

## 8. `cap_07` SE DECLARA CERRADO EN INSERCION: LO MIDO YO Y DIGO QUE FALTA

    $ (nodos de la poblacion entera cuyo resumen cita fuentes/scott_radical_candor/cap_07.md)
      nodos que citan cap_07.md : 25  (grafo 25, bandeja 0)
      L65-77   L91-111  L113-129 L131-153 L155-163 L177-195 L197-211 L225-229 L231-233
      L235-237 L239-243 L245-257 L259-289 L291-293 L295-301 L303-347 L349-357 L359-365
      L367-373 L375-379 L381-383 L385-387 L389-401 L403-407 L409-419

    $ (lineas del capitulo cubiertas por algun nodo, y los huecos de dos o mas lineas con texto)
      lineas del capitulo       : 434
      lineas cubiertas por nodo : 295
      L1-64    35 lineas con texto
      L78-90    6 lineas con texto
      L164-176  6 lineas con texto
      L212-224  6 lineas con texto
      L420-433  7 lineas con texto

**LECTURA 1:** **veinticinco nodos citan `cap_07` y los veinticinco estan en el grafo: en la
bandeja no queda ninguno.** Por ese lado, cerrado es cierto.

**LECTURA 2, y aqui es donde miro los huecos uno por uno:**

| hueco | que hay ahi | mi lectura |
|---|---|---|
| `L1-64` | el arranque del capitulo: *decir a la gente lo que tiene que hacer no funciono en Google*, y la serie de anecdotas de Andy Grove y Steve Jobs | **bien fuera.** Es narracion y postura, y `D.27` no la quiere como nodo |
| `L78-90` | cabecera de `LISTEN`, la cita de Jony Ive y el *encuentra tu estilo y crea una cultura de escucha* | **bien fuera.** Ese encargo ya vive entero en `crear_cultura_escucha_equipo` (`L131-153`) |
| `L164-176` | cabecera de `CLARIFY`, la cita de O'Keeffe y *eres el editor, no el autor* | **discutible menor.** Lo reparten `crear_espacio_seguro_madurar_ideas_nuevas` y `explicar_idea_facil_comprender_oyente` |
| `L212-224` | cabecera de `DEBATE` y el rotulo **`The rock tumbler`** | **ESTE NO LO VEO REPARTIDO, y es mi propuesta 1** |
| `L420-433` | `PART II`, `TOOLS & TECHNIQUES` y `RELATIONSHIPS` | **bien fuera.** Es la portadilla de la parte siguiente |

### 8.1. **PROPUESTA 1: `The rock tumbler` (`L212-224`) tiene procedimiento propio y no tiene nodo**

**Las otras cuatro cabeceras de la rueda estan dentro de un nodo**, y se ve en los rangos de
arriba: `DECIDE` entra en `L259-289`, `PERSUADE` en `L303-347`, `EXECUTE` en `L367-373` y
`LEARN` en `L389-401`. **La de `DEBATE` es la unica que se queda fuera**, y no es una cabecera
vacia. Lo que dice, y lo cito de la fuente:

    L221  Your job as a boss is to turn on that "rock tumbler." Too many bosses think their
          role is to turn it off, to avoid all the friction by simply making a decision and
          sparing the team the pain of debate.
    L217  Once again, you don't have to be in every debate, in fact, you shouldn't be. But
          you've got to make sure that they happen, and that there is a culture of debate.
    L223  Of course, it's also possible to leave the rock tumbler on too long, leaving nothing
          in the can but some dust.

**LECTURA:** son tres encargos al jefe con su consecuencia cada uno, y **ninguno de los cinco
nodos de `DEBATE` los recoge**: `centrar_debate_ideas_fuera_egos` es sobre ideas contra egos,
`crear_obligacion_disentir_equipo` es el martillo de McKinsey, `parar_debate_emocion_agotamiento`
es la pausa, `abrir_debate_humor_explicar_proposito` es el tono, y `fijar_fecha_cierre_debate_equipo`
es el cierre. **El que falta es el de encenderlo, no estar en todos, y no dejarlo girando hasta
el polvo.** Lo traigo como propuesta y no como caida: puede que la vuelta lo leyera como
postura, y esa es una lectura legitima que se adjudica citando, no discutiendo.

---

## 9. LO QUE DEJO `POR ADJUDICAR` PARA MI PROPIO TURNO

1. **`POR ADJUDICAR 1`:** si el par `reservar_calendario_tiempo_ejecutar` contra
   `pelear_proliferacion_reuniones_bloquear_ejecucion` (seccion 6) es `CONTINUA`, como yo leo,
   y **como se cierra el agujero de que ninguna señal lo levante en ninguna de las dos
   direcciones** antes de que el candidato entre.
2. **`POR ADJUDICAR 2`:** si la arista `cuidarse_agotamiento_centro_rueda` paso 7 contra
   `bloquear_tiempo_pensar_calendario` (seccion 6.2) falta, o si hay una razon escrita que la
   descarta. **La razon la destapare de una en una.**
3. **`POR ADJUDICAR 3`:** si `fijar_fecha_cierre_debate_equipo` debia ser uno o dos nodos
   (discutible 1), sabiendo que es la unica costura de la tanda con dos rotulos dentro.
4. **`POR ADJUDICAR 4`:** la propuesta 1 de la seccion 8.1, `The rock tumbler`.
5. **`POR ADJUDICAR 5`:** que hacer con las ocho lineas `SIN HUELLA` de la seccion 7.3, que
   por como esta escrito hoy **no se pueden comprobar nunca**, y si eso pide correccion
   declarada o solo registro.
6. **`POR ADJUDICAR 6`:** si la receta escrita de `D.38.4` (seccion 2) se corrige por
   correccion declarada en el banco, ahora que esta medido que corrida al pie de la letra
   infla la poblacion en 92 y duplica los vecinos de bandeja.
7. **`POR ADJUDICAR 7`:** si el censo en rojo de la seccion 7.4 y los cuatro fallos de la 7.5
   son, como yo los leo, **artefactos de la fase ciega que le tocan al arnes**, o si alguno
   de los dos es una caida de alguien.

---

## 10. LO QUE ESTA PAGINA NO DICE, Y LO DIGO YO

- **No dice si la vuelta acerto**, porque no he visto su reporte. Dice **lo que yo leo**, y
  se guarda para que la comparacion de mi turno tenga dos lecturas de verdad y no una.
- **No trae ni una cifra contada a mano.** Las cifras de esta pagina salen de
  `wc -l`, del `gate`, del barrido de guiones, del bloque de vigencia, del censo de rutas, de
  la prueba de aceptacion, del informe de la aduana en seco y de `git`, **y todas llevan su
  salida pegada al lado**, como manda `D.38.3`.
- **No reclama como ciega la clase de `compartir_logica_mostrar_razonamiento`**, por lo que
  declare en `0.2` contra mi mismo.
- **Y avisa de que el sello puede no llegar:** el censo de rutas esta en rojo por dos celdas
  de mi propia acta que esta misma fase deja sin sostener, y `D.45` dice que con una guarda en
  rojo el sello no se acepta. **Si esta pagina no se sella, la razon esta medida en la
  seccion 7.4 y no hace falta buscarla.**
