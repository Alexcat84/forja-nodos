# APERTURA CIEGA DEL AUDITOR, VUELTA 23, lote 4 (`scott_radical_candor`)

**Escrita ANTES de ver `docs/loop/REPORTE.md`**, que no esta en el arbol, como tampoco
`loop.log`, `ultimo_extractor.json` ni `ultimo_auditor.json` (`D.34.2`). **No los he recuperado
de git ni por ninguna otra via**: ni un `git show`, ni un `git checkout`, ni un `git log` sobre
ninguno de los cuatro. Lo que si he abierto, porque es obra mia y no del extractor, es
`docs/loop/ACTA_AUDITOR.md`.

---

## 0. LA HERENCIA `D.40`, DECLARADA ANTES QUE NADA

    ACTA ANTERIOR LEIDA: 830c512c41df21924a291955b7b2db4e04999324
    HEREDADO 1: CUMPLIDO

**La huella la he remedido yo, no la he copiado del prompt:**

    $ git hash-object docs/loop/ACTA_AUDITOR.md
      830c512c41df21924a291955b7b2db4e04999324
    $ wc -l docs/loop/ACTA_AUDITOR.md
      20849 docs/loop/ACTA_AUDITOR.md

**Coincide con la que el arnes me entrega.** Es la `ACTA 22`, que arranca en la linea `19889` y
cubre la vuelta 22.

### 0.1. `HEREDADO 1` ES UNA LISTA DE NUEVE REMEDIOS MIOS, Y LOS DECLARO UNO A UNO

`REMEDIO ROTO` solo informa si tambien se declara cuando aguanta, asi que no basta con escribir
`CUMPLIDO` en una linea. Van los nueve con lo que los sostiene **hoy**.

| remedio heredado | como queda hoy | |
|---|---|---|
| `D.40`, leer `ACTA_AUDITOR.md` en la fase ciega **antes** de escribir | leida de estructura entera y leida de cuerpo en la `ACTA 22`; huella remedida con `git hash-object` y pegada arriba | **CUMPLIDO** |
| `D.40`, declarar la herencia con `CUMPLIDO` o `NO APLICA` **con su motivo** | esta tabla, con sus nueve lineas y su parrafo detras cuando hace falta | **CUMPLIDO** |
| **`HEREDADO 4` de la 21, el barrido `D.38.4` corrido y con su seccion existiendo** | **la seccion `4` de esta apertura EXISTE**, con poblacion `330 = 203 + 127` y `14` candidatos barridos con sus seis vecinos mas cercanos impresos uno a uno | **CUMPLIDO** |
| `ACTA 19` `7.4` **ORDEN A**, la fila de residuo es cero o trae los nombres | los dos residuos nombrados tramo a tramo en `2.2` y `3.2`, con sus palabras y su primera linea | **CUMPLIDO** |
| `ACTA 19` `7.4` **ORDEN B**, el rotulo se escribe DESPUES del instrumento | las dos tablas de frontera salen de `.t1_v23_auditor/frontera_auditor_v23.py`, corrido antes de teclear una sola fila | **CUMPLIDO** |
| `ACTA 18` `7.5` orden 1, la frontera se cierra contra el cuerpo o no se publica | `2.118 = 2.118` en `cap_12` y `9.298 = 9.298` en `cap_13`, con `0` solapes en los dos | **CUMPLIDO** |
| `D.34`, no recuperar de git los cuatro ficheros retirados | ni un `git log`, `git show` ni `git checkout` sobre ninguno | **CUMPLIDO** |
| `5.5`, toda guarda declarada mordiendo se re corre por mutacion | **NO APLICA EN ESTA FASE, y el motivo es mecanico**: la sede donde una guarda se declara mordiendo es `REPORTE.md`, y `REPORTE.md` esta retirado del arbol por `D.34.2`. **No puedo re correr una declaracion que no he leido.** Lo cumplo en mi turno normal, cuando el arnes me exponga el reporte, y ahi es donde acumula si lo rompo | **NO APLICA, con motivo** |
| `8.3`, la cifra de volumen se verifica y no se copia | **los `262` pasos contados por mi de los ficheros**, los `262` pasados por `fidelidad_auditor_v23.py`, y la lectura a mano de los `43` con marca de periodo o cantidad (seccion `5`) | **CUMPLIDO** |

**Y HAY UNA COSA DE LA HERENCIA QUE NO ES UN REMEDIO Y LA DIGO IGUAL.** La `ACTA 22` cerro con
`la racha REPORTE llega a 3 de 3: EL BUCLE SE DETIENE`. El bucle **no** esta detenido hoy, y no
lo esta por decision mia: `docs/loop/paradas/2026-09-13-la-tabla-tecleada.md` es aquel
`PARA_ALEXIS.md` archivado, y su punto 1 **reinicia la racha `REPORTE` con condicion mecanica**
(`D.41`, `scripts/tallar_reporte.py` mas `cerrar_reporte.py`). **La reinicia una decision escrita
del fundador y no yo** (`5.4`), y la cito porque `5.4` manda citarla.

---

## 1. QUE MATERIAL TENGO DELANTE, MEDIDO Y NO SUPUESTO

    $ ls cuarentena/scott_radical_candor/*.json | wc -l
      127
    $ python - (agrupa por el fichero fuente que cada candidato declara en resumen_teorico)
      cap_01  1     cap_07 25     cap_12   2
      cap_03  1     cap_08 12     cap_13  12
      cap_04  5     cap_09 20     SIN_CAP  1
      cap_05  8     cap_10 14
      cap_06 10     cap_11 16     TOTAL  127

**LOS DE ESTA VUELTA SON `14`: `2` de `cap_12` y `12` de `cap_13`.** Los otros `113` son la cola
del lote que ya estaba en la bandeja, y `113 + 14 = 127` cuadra con el conteo de ficheros.

**`cap_14` TIENE CERO CANDIDATOS.** El material esta (`fuentes/scott_radical_candor/cap_14.md`,
`243` lineas) y la bandeja no tiene ni una pieza suya. **Al lote 4 le falta un capitulo y solo
uno.**

    $ wc -l fuentes/scott_radical_candor/cap_12.md   ->  65
    $ wc -l fuentes/scott_radical_candor/cap_13.md   -> 347
    $ wc -l fuentes/scott_radical_candor/cap_14.md   -> 243

---

## 2. MI FRONTERA CIEGA DE `cap_12` (unidad `Getting Started`)

He leido el capitulo entero antes de abrir un solo candidato. Es corto: `65` lineas, cuerpo de
`L8` a `L65`.

### 2.1. LA TABLA, QUE SALE DEL INSTRUMENTO Y NO DE MI MANO

    $ python .t1_v23_auditor/frontera_auditor_v23.py
    ==============================================================================
    cap_12  cuerpo = lineas 8 a 65   palabras del cuerpo = 2118
    ------------------------------------------------------------------------------
      P1 desplegar_plan_orden_operaciones_franqueza_radical    L13-L13,L15-L15,L19-L49   1306 palabras
      P2 contar_historias_propias_explicar_franqueza_radical   L17-L17    116 palabras
    ------------------------------------------------------------------------------
      SUMA DE LOS TRAMOS         = 1422 palabras en 2 piezas
      RESIDUO (lineas no cubiertas) = 696 palabras en 24 lineas
      SUMA + RESIDUO = 2118   CUERPO = 2118   CIERRA AL DIGITO
      SOLAPES = 0

### 2.2. EL RESIDUO, NOMBRADO Y NO RESUMIDO (`ACTA 19` `7.4` ORDEN A)

    L8   a L12     47 pal   GETTING STARTED | CONGRATULATIONS! YOU'VE TAKEN AN IMPORTANT step...
    L14  a L14      0 pal
    L16  a L16      0 pal
    L18  a L18      0 pal
    L50  a L65    649 pal   That's a lot of things to do... | In other words, Radically Candid...

**`L50` a `L65` son `649` palabras, casi un tercio del capitulo.** Lo leo entero y lo clasifico:
`L51` es el reparto de la semana; `L53` y `L55` son cierre de la unidad; `L57` es un separador;
`L59` a `L65` son la peroracion final del libro, postura pura y sin un solo medio. **La unica
pieza del residuo que me hace dudar es `L51`, y la trato aparte en `2.4`.**

### 2.3. **LA CAIDA QUE MI LECTURA CIEGA ENCUENTRA EN `cap_12`: LOS DOS ROTULOS DE LINEA NO ESTAN TRATADOS IGUAL**

`cap_12` tiene **dos** rotulos en versal, tipograficamente del mismo rango, y **los dos traen
cuerpo propio detras**:

    $ python - (mide las dos lineas con el mismo contador que la frontera)
      L15 rotulo : SHARE YOUR STORIES
      L17 cuerpo :  116 palabras  -> es la PIEZA 2, nodo propio
      L19 rotulo : PROVE YOU CAN TAKE IT BEFORE YOU START DISHING IT OUT
      L21 cuerpo :   98 palabras
      L23 cuerpo :   95 palabras
      L21+L23    :  193 palabras  -> NO es pieza: son los pasos P5 a P11 de la PIEZA 1

**El cuerpo del primer rotulo se hace nodo. El cuerpo del segundo se queda de pasos dentro de la
cabeza.** Y no puede ser cuestion de tamanio, porque **el que no se hace nodo es el grande**
(`193` contra `116`), y porque la vara de manual `4` **no tiene bascula**.

**LA RAZON ESCRITA DEL PROPIO CANDIDATO SE VUELVE CONTRA EL.** `contar_historias_propias`
justifica su existencia asi: *la cabeza NOMBRA la etapa por su rotulo y no la despliega, y esta
linea trae su propio inventario de MEDIOS*. **Apliquemos ese mismo criterio a `L21` y `L23`**, que
es lo que un criterio es: no dejar que la gente se libre cuando no dice gran cosa, abrazar la
incomodidad, prestar atencion si no llega ninguna critica, copiar el marco del capitulo dos y
llevar ahi la cuenta de quien te dice que, la tecnica de la caja naranja de Michael Dearing, y la
cadencia diaria de uno a dos minutos que no se agenda. **Son cinco medios y una cadencia, la
misma forma que los seis medios de `L17`.**

**MI LECTURA CIEGA: la frontera de `cap_12` es de `3` piezas y no de `2`.** La pieza que falta es
`L19` a `L23`. **No es doctrina nueva y por eso no es parada** (`3`): es el criterio que el propio
lote ya usa, aplicado al segundo rotulo con la misma mano que al primero. Lo dejo escrito aqui
**antes** de saber si el extractor lo marco discutible.

**Y DIGO LO QUE DEBILITA MI PROPIA LECTURA, porque si no la escribo yo no la escribe nadie:**
`L21` es el tramo mas cargado de remites de todo el capitulo (manda al capitulo seis dos veces y
al capitulo dos una). Quien sostenga las `2` piezas puede decir que `L21` **nombra** y no
**procedimenta** (`P.5.1`). **Contra eso pongo que la caja naranja y la cuenta de quien te dice
que no viven en ningun otro sitio de este capitulo**, y que nombrar no es procedimentar corta en
los dos sentidos: si `L21` solo nombra, tampoco deberian salir de ahi los siete pasos `P5` a
`P11` que la pieza 1 si se lleva.

### 2.4. `L51`, EL REPARTO DE LA SEMANA: **NO ES NODO, Y EL DONANTE TIENE QUE ABSORBER TRES COSAS**

`L51` cifra diez horas de gestion, quince de pensar y ejecutar, y quince de lo imprevisible.
**Eso ya esta extraido**, y lo verifico contra el grafo y las bandejas en vez de citar una
busqueda negativa:

    $ python - (busca el id en dataset/nodos.jsonl y en cuarentena/*/*.json)
      repartir_semana_cuarenta_horas_jefe  [BANDEJA cuarentena/scott_radical_candor/...]
        P4 Cuenta diez horas a la semana de gestion de tu equipo...
        P6 Bloquea unas quince horas a la semana para pensar y ejecutar por tu cuenta...
        P7 Cuenta las otras quince horas que quedan en una semana laboral de cuarenta...

**EXISTE Y DICE LO QUE SE DICE QUE DICE.** Es el mismo objeto y `L51` no funda nodo: `P.19` manda
no fabricar el gemelo de su propio donante.

**PERO `L51` NO ES REDUNDANTE DEL TODO, Y ESO NO PUEDE PERDERSE.** Anade tres cosas que
`repartir_semana_cuarenta_horas_jefe` no tiene: que **cinco de esas diez** son reuniones a solas
que probablemente ya estabas teniendo; que las conversaciones de crecimiento, las reuniones de
salto de nivel y las calibraciones **vienen a rachas y no se reparten por semana**; y que por eso
**hay semanas de ocho horas, otras de doce y otras de cinco**. **Mi adjudicacion ciega: no es un
nodo nuevo, es una correccion declarada sobre el donante**, que se lleva esos tres pasos citando
`cap_12` `L51` como segunda fuente. Dejarlo fuera es perder catalogo por la puerta de atras.

---

## 3. MI FRONTERA CIEGA DE `cap_13` (unidad `Afterword`)

`347` lineas, cuerpo de `L8` a `L347`. Lo he leido entero, de la cabecera al `BONUS CHAPTER`.

### 3.1. LA TABLA, DEL INSTRUMENTO

    $ python .t1_v23_auditor/frontera_auditor_v23.py
    ==============================================================================
    cap_13  cuerpo = lineas 8 a 347   palabras del cuerpo = 9298
    ------------------------------------------------------------------------------
      P1  mejorar_consciencia_propia_relacional_dos_practicas  L17-L22,L35-L40      307 palabras
      P2  contar_cuatro_historias_propias_ver_hueco_intencion  L41-L58              687 palabras
      P3  practicar_triangulo_critica_tres_papeles             L59-L72              510 palabras
      P4  pedir_critica_primero_crear_seguridad_psicologica    L73-L86,L105-L110,L113-L114   457 palabras
      P5  elegir_pregunta_recurrente_pedir_critica             L115-L120,L129-L166  801 palabras
      P6  resolver_dudas_frecuentes_pedir_critica              L167-L186            501 palabras
      P7  abrazar_incomodidad_silencio_contar_seis             L187-L198            272 palabras
      P8  escuchar_entender_critica_dominar_defensa            L199-L214            282 palabras
      P9  premiar_franqueza_hacer_escucha_tangible             L215-L234            590 palabras
      P10 integrar_peticion_critica_rutina_existente           L111-L112,L235-L246  402 palabras
      P11 dar_elogio_disciplina_igual_critica                  L247-L252,L267-L288  816 palabras
      P12 medir_critica_respuesta_oyente_brujula               L289-L322           1519 palabras
    ------------------------------------------------------------------------------
      SUMA DE LOS TRAMOS         = 7144 palabras en 12 piezas
      RESIDUO (lineas no cubiertas) = 2154 palabras en 86 lineas
      SUMA + RESIDUO = 9298   CUERPO = 9298   CIERRA AL DIGITO
      SOLAPES = 0

### 3.2. EL RESIDUO, NOMBRADO TRAMO A TRAMO

    L8   a L16     92 pal   AFTERWORD... | Rolling Out Radical Candor | by Jason Rosoff, Amy Sandler, and Kim Scott | SINCE THIS BOOK was published...
    L23  a L34    121 pal   For example, a venture capitalist asked Kim how to help one of his associates...
    L87  a L104   347 pal   The first edition describes this order of operations... | Kim's Soliciting Feedback Story...
    L121 a L128   334 pal   Jason's Story | As I became a manager, I made most of the classic mistakes...
    L253 a L266   487 pal   When Jason was early in his career... | Jason's Story | These calls were done in pairs...
    L323 a L347   773 pal   DIVERSITY AND INCLUSION | ... | WHAT'S NEXT? | ...

**CUATRO DE LOS SEIS TRAMOS SON CASOS Y SALEN BIEN.** `L23` a `L34` (el capitalista de riesgo y
su asociado), `L87` a `L104` (la historia de la hija de Kim y la Senora de la Franqueza Radical),
`L121` a `L128` (la historia de Jason y Ann) y `L253` a `L266` (la historia de Jason y Dave) son
**el caso, y el caso no es la casa**. Sus medios ya viajan dentro de la pieza que los enmarca.
`L8` a `L16` es cabecera y proposito. **Sobre esos cinco no tengo reparo.**

### 3.3. **EL TRAMO DEL RESIDUO QUE SI ME HACE DUDAR: `L323` a `L347`, `773` PALABRAS Y DOS ROTULOS EN VERSAL ENTEROS**

`DIVERSITY AND INCLUSION` (`L323`) y `WHAT'S NEXT?` (`L333`) son rotulos del mismo rango que
`GAUGE CRITICISM` o que `EMBRACE THE DISCOMFORT`, **y se quedan los dos sin una sola pieza**.

**MI LECTURA, Y VOTO QUE NO SON NODO:**

- `WHAT'S NEXT?` (`L333` a `L345`) es hoja de ruta de la consultora y peticion de critica a los
  lectores. **Cero medios que el lector ejecute.** Fuera sin discusion.
- `DIVERSITY AND INCLUSION` (`L323` a `L331`) es el caso dificil. Lo que trae es: el problema
  (te quedas sin respuesta ante algo ofensivo), una cita de Claudia Rankine, **un medio de
  verdad** (la cena de practica mensual de la participante del taller, donde se comparten esas
  historias y se ensaya lo que se podria haber dicho), y despues **la descripcion de un producto
  propio** (el taller `Improvising Radical Candor` montado con Second City). **Un medio suelto
  dentro de una narracion de como se monto un taller no es el inventario de medios que `D.27`
  pide**, y la parte que si tiene forma de procedimiento es la que el lector **no puede ejecutar**
  porque es contratar a los autores.

**PERO LO MARCO DISCUTIBLE Y DIGO POR QUE**, porque es el unico rotulo de primer rango del
capitulo que se cae entero: si esta casa decide que la **cena de practica** es medio suficiente,
entonces sale de aqui un nodo pequenio y honesto (juntar a unos companieros de confianza con
cadencia mensual, traer cada uno lo que le dijeron, y ensayar en voz alta la respuesta que no
supiste dar). **No lo escribo yo porque no me toca escribir nodos**, pero dejo el borde dibujado
para que la discrepancia se pueda leer.

### 3.4. LO QUE MI LECTURA CIEGA CONFIRMA, Y ES LA MAYOR PARTE

**Los doce cortes de `cap_13` los adjudico buenos, y los adjudico habiendo leido los pasos.** El
capitulo es un afterword que va rotulo a rotulo, y el corte por rotulo de linea es el que esta
casa lleva usando desde `cap_05`. Tres cosas me convencen de que no es corte mecanico:

1. **`P10` se lleva `L111` y `L112`, que estan a `124` lineas de su otro tramo.** `L111` es el
   parrafo de *ver al jefe pedirla una vez no basta... cuando un jefe aparta tiempo cada semana
   para reuniones a solas y pide critica al final de cada una*. **Eso es `BUILD IT INTO YOUR
   EXISTING SCHEDULE` dicho ciento veinticuatro lineas antes de su rotulo**, y darselo a `P10` en
   vez de a `P4` es una lectura, no un barrido. **Lo leo y estoy de acuerdo.**
2. **`P11` salta `L253` a `L266` por dentro** y aun asi cierra: se lleva `L247` a `L252` y `L267`
   a `L288`, dejando la historia de Dave fuera. **La pieza no se parte por el caso que lleva
   dentro.**
3. **`P4` deja fuera `L87` a `L104`** por la misma razon, y se queda con el orden de operaciones
   de cinco pasos (`L77` a `L85`) y la investigacion de seguridad psicologica (`L105` a `L110`).

### 3.5. **EL PAR QUE EL PROPIO LIBRO DECLARA, Y QUE POR ESO NO PUEDE QUEDARSE SIN VEREDICTO**

`cap_13` `L43` dice, con sus palabras:

> *Storytelling is a great way to develop both self-awareness and relational awareness. **There's
> a brief paragraph about this in the final Getting Started section**, but we have been asked for
> more detail about how to do this and why it works.*

**El `brief paragraph` de `Getting Started` es `cap_12` `L17`, que es exactamente la pieza `2` de
`cap_12`.** Es decir: `contar_historias_propias_explicar_franqueza_radical` y
`contar_cuatro_historias_propias_ver_hueco_intencion` **son el mismo objeto a dos profundidades,
y lo dice el libro, no una senial.**

**MI ADJUDICACION CIEGA, con la vara de manual `4` y su direccion:** que anade el **hijo**
(`cap_13`, el detallado) a la **madre** (`cap_12`, el parrafo breve): el inventario de las
**cuatro** historias (franqueza radical, agresion odiosa, empatia ruinosa, insinceridad
manipuladora), las dos cosas que la vulnerabilidad consigue a la vez, y el hueco entre intencion
e impacto. Que queda fuera del solape **en el lado de la madre**: explicarlo con tus palabras,
pedirles que lean el libro, ensenarles los videos de la web. **Queda procedimiento en los dos
lados, asi que es `CONTINUA` y no `REPITE`**, y pide arista declarada con `L43` citada como razon,
que es la razon mas barata que un par va a tener nunca. **La arista no exculpa** (vara `6.1`),
pero aqui no hace falta que exculpe: la lectura ya separo los dos.

**Y UNA COSA MAS QUE SE ME OCURRE MIRANDO LAS DOS A LA VEZ.** `cap_12` `L17` manda buscar **tu
version de la historia del `um` y de la historia de `Bob`**. `cap_13` `L45` y `L51` mandan
exactamente lo mismo con otras palabras (*it will be a thousand times more powerful than Kim's
story about... "um"*, *Don't tell Kim's Bob story from Chapter Two, tell yours*). **Las dos
historias del libro viajan por su nombre y no por su contenido en los dos sitios**, que es manual
`3.5` bien aplicado por las dos piezas. **Eso no lo discuto: lo confirmo.**

---

## 4. EL BARRIDO `D.38.4`, SOBRE GRAFO MAS BANDEJAS, CORRIDO POR MI HOY

### 4.1. **LA POBLACION, Y UNA CAIDA MIA QUE ME CACE ANTES DE PUBLICARLA**

**Mi primera corrida del barrido midio `493 = 203 + 290`, y esa cifra es FALSA.** Me habia
tragado los `163` de `cuarentena/ensayo_referencia_163/`, que son catalogo de referencia ajeno
puesto ahi para calibrar la aduana y que **no espera juicio**. **La cace antes de escribir una
sola fila de este documento**, corregi el instrumento con el mismo criterio que `src/informe.py`
aplica desde el 12 sep (*entra el candidato cuyas fuentes estan TODAS en la tabla canonica
vigente*), y **la contraste contra el instrumento de la casa**:

    $ python .t1_v23_auditor/barrido_vecinos_auditor_v23.py
      POBLACION DEL BARRIDO: 330 = 203 del grafo + 127 de las bandejas
        (bandejas: cuarentena/*/*.json, fuera _insertados y _derivadas, y fuera
         los 163 cuyas fuentes NO estan todas en FUENTES_CANONICAS.json, que es el
         mismo criterio que src/informe.py aplica desde el 12 sep 2026)

    $ python -c "from src import informe; print(len(informe.poblacion_de_bandejas()))"
      127

**`127` contra `127`.** Mi mitad de bandejas y la de la maquina son **la misma**, que es lo que
`D.38.5` promete desde el 12 sep, asi que si mi barrido y el informe discrepan en un vecino,
**es discrepancia de verdad y no de metodo**. La corregi en el instrumento y no en la prosa.
**No llega a sede y no acumula**, pero la escribo porque `5.3` pide que mis errores se escriban
igual que los suyos, y porque es exactamente la especie de cifra que `D.38.3` vino a impedir.

**Y CUADRA CON LA VUELTA ANTERIOR:** la `ACTA 22` publico `316 = 203 + 113`. `113 + 14 = 127`, que
son los catorce de esta vuelta entrando en la bandeja. **El grafo sigue en `203`: esta vuelta no
ha insertado nada, y eso es coherente con que el lote no haya cerrado.**

### 4.2. LOS CATORCE, CON SUS SEIS VECINOS MAS CERCANOS CADA UNO

Mi instrumento es **distinto del de la aduana a proposito**: mide solape de palabras de contenido
de `titulo + condiciones + entregable` por un lado, y solape de los conjuntos de pasos por otro.
**E imprime los que se quedan por debajo de cualquier umbral**, que es justo lo que un informe de
aduana no imprime (`umbral_similitud_texto` esta en `0,35` y `umbral_paso_contra_nodo` en `0,60`,
leidos de `config/umbrales.json`).

| candidato | vecino mas cercano | max | sede del vecino |
|---|---|---|---|
| `mejorar_consciencia_propia_relacional_dos_practicas` | `contar_cuatro_historias_propias_ver_hueco_intencion` | **0,255** | bandeja |
| `contar_cuatro_historias_propias_ver_hueco_intencion` | `mejorar_consciencia_propia_relacional_dos_practicas` | **0,255** | bandeja |
| `contar_historias_propias_explicar_franqueza_radical` | `contar_cuatro_historias_propias_ver_hueco_intencion` | **0,195** | bandeja |
| `desplegar_plan_orden_operaciones_franqueza_radical` | `contar_historias_propias_explicar_franqueza_radical` | 0,182 | bandeja |
| `pedir_critica_primero_crear_seguridad_psicologica` | `desplegar_plan_orden_operaciones_franqueza_radical` | 0,180 | bandeja |
| `practicar_triangulo_critica_tres_papeles` | `contar_cuatro_historias_propias_ver_hueco_intencion` | 0,180 | bandeja |
| `resolver_dudas_frecuentes_pedir_critica` | `resolver_dudas_frecuentes_reuniones_salto_nivel` | 0,152 | bandeja |
| `elegir_pregunta_recurrente_pedir_critica` | `abrazar_incomodidad_arrancar_critica_equipo` | 0,149 | bandeja |
| `medir_critica_respuesta_oyente_brujula` | `abrazar_incomodidad_arrancar_critica_equipo` | 0,144 | bandeja |
| `dar_elogio_disciplina_igual_critica` | `decidir_momento_despedir_persona` | 0,136 | bandeja |
| `integrar_peticion_critica_rutina_existente` | `elegir_pregunta_recurrente_pedir_critica` | 0,125 | bandeja |
| `premiar_franqueza_hacer_escucha_tangible` | `abrazar_incomodidad_arrancar_critica_equipo` | 0,122 | bandeja |
| `abrazar_incomodidad_silencio_contar_seis` | `elegir_pregunta_recurrente_pedir_critica` | 0,118 | bandeja |
| `escuchar_entender_critica_dominar_defensa` | `decidir_momento_despedir_persona` | 0,117 | bandeja |

**LOS CATORCE VECINOS MAS CERCANOS VIVEN EN LA BANDEJA Y NINGUNO EN EL GRAFO.** El primero del
grafo que aparece en toda la corrida es `facilitar_gente_diga_verdad`, quinto de
`pedir_critica_primero` con `0,116`. **Eso es exactamente el agujero que `D.38.5` cerro el 12 sep**:
con el informe cargando solo el grafo, **esta vuelta entera no habria levantado un solo par**.

### 4.3. **LO QUE MI BARRIDO NO VE, Y ES LO MAS IMPORTANTE DE ESTA SECCION**

**Ningun candidato de los catorce llega a `0,26`.** Con los umbrales vigentes (`0,35` y `0,60`)
**la aduana no va a levantar ni uno solo de los pares de esta vuelta por la senial de texto.** Y
sin embargo el par de `3.5` existe, **lo declara el propio libro en `L43`**, y mi propia senial lo
puso en `0,195`, muy por debajo de su umbral.

**Y HAY UN CASO QUE ME DEJA PEOR TODAVIA, Y ES MIO.** `cap_13` `L113` dice que el afterword va a
profundizar en **los cuatro elementos de pedir critica que el libro ya daba en el capitulo seis**.
Esos cuatro son, uno a uno, las piezas `P5`, `P7`, `P8` y `P9` de `cap_13`. Y el capitulo seis de
esta casa es `cap_09`, cuyo `abrazar_incomodidad_arrancar_critica_equipo` lleva **los seis
consejos** dentro, incluidos esos cuatro. **Son cuatro pares de cabeza contra parte declarados por
el libro. Mi barrido levanta ese vecino para `elegir_pregunta` (`0,149`), para `medir_critica`
(`0,144`) y para `premiar_franqueza` (`0,122`), pero para `abrazar_incomodidad_silencio_contar_seis`
NO LO PONE NI ENTRE LOS SEIS PRIMEROS**, y es el par mas obvio de los cuatro: **los dos se llaman
igual en el libro, `Embrace the discomfort`.**

**Esa es una errata de mi instrumento y la declaro como tal**, no como hallazgo contra nadie: mide
vocabulario, y dos piezas del mismo rotulo escritas con tres anios de diferencia comparten idea y
no palabras. **Es `D.19` en vivo: ninguna senial separa jerarquia de ruido, y por eso una
discrepancia no se adjudica citando una senial.**

**Y LO DIGO ENTERO PORQUE ME QUITA LA RAZON A MI:** he ido a ver, uno a uno, que vecinos nombra
cada candidato en su `resumen_teorico`, y **`abrazar_incomodidad_silencio_contar_seis` SI cita
`abrazar_incomodidad_arrancar_critica_equipo`**. Lo vio la lectura del extractor donde mi
instrumento no llegaba. Lo escribo aqui, antes de ver su reporte, porque `5.3` no me deja
publicar solo los fallos ajenos.

    $ python - (cruza cada resumen_teorico contra los 330 ids de la poblacion)
      los 14 candidatos citan al menos un vecino de la poblacion en su resumen
      los 14 tienen nodos_previos = 0 y nodos_siguientes = 0

**LOS CATORCE TIENEN `nodos_previos` Y `nodos_siguientes` VACIOS.** No lo llamo caida: el cableado
de aristas lo hace `forja.py arista` al insertar, y `D.39` no ha insertado porque el lote no ha
cerrado. **Pero lo dejo medido**, porque es la fila que hay que volver a mirar cuando `cap_14`
cierre el lote: **una arista que vive solo en prosa no es una arista.**

---

## 5. `PASOS INVENTADOS POR CAPITULO` (`8`), CONTADO POR MI Y NO COPIADO

### 5.1. LO QUE CORRI ANTES DE FIRMAR NADA

**Punto 1 de `8.3`, cuento yo los pasos:**

    $ python - (len de pasos_accionables de cada fichero de cuarentena)
      cap_12: desplegar_plan 42 + contar_historias 8            = 50 pasos en 2 candidatos
      cap_13: 13+17+15+17+24+15+12+13+20+13+20+33               = 212 pasos en 12 candidatos
      TOTAL DE LA VUELTA = 262 pasos en 14 candidatos

**Y el numero de pasos que cada candidato DECLARA en su relectura de fidelidad cuadra con el
numero de pasos que tiene: `14` de `14` `OK`, `0` descuadres.**

**Punto 2 de `8.3`, releo los marcados `TRANSCRIPCION` contra su parrafo.** Los `262` estan
marcados `TRANSCRIPCION` y `0` `PUENTE`, que es la cifra que mas facil seria falsear porque baja
el numerador y sube el lote siguiente. **No la firmo por lectura de muestra: la ataco con un
instrumento y despues leo.**

    $ python .t1_v23_auditor/fidelidad_auditor_v23.py
      desplegar_plan_orden_operaciones_franqueza_radical      42 pasos   TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO
      contar_historias_propias_explicar_franqueza_radical      8 pasos   TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO
      mejorar_consciencia_propia_relacional_dos_practicas     13 pasos   NO ENCONTRADO: [(10, 'nombre propio', 'DOS')]
      contar_cuatro_historias_propias_ver_hueco_intencion     17 pasos   TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO
      practicar_triangulo_critica_tres_papeles                15 pasos   TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO
      pedir_critica_primero_crear_seguridad_psicologica       17 pasos   TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO
      elegir_pregunta_recurrente_pedir_critica                24 pasos   TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO
      resolver_dudas_frecuentes_pedir_critica                 15 pasos   TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO
      abrazar_incomodidad_silencio_contar_seis                12 pasos   TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO
      escuchar_entender_critica_dominar_defensa               13 pasos   TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO
      premiar_franqueza_hacer_escucha_tangible                20 pasos   TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO
      integrar_peticion_critica_rutina_existente              13 pasos   TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO
      dar_elogio_disciplina_igual_critica                     20 pasos   TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO
      medir_critica_respuesta_oyente_brujula                  33 pasos   TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO

**EL METODO, PORQUE UN INSTRUMENTO SIN SU METODO ES UNA CIFRA A MANO CON DISFRAZ.** El fuente esta
en ingles y los pasos en castellano, asi que el solape de palabras no vale. **Lo que si cruza la
traduccion sin cambiar son los numeros y los nombres propios**, y son la especie de puente mas
cara: una cantidad inventada o una autoridad anadida. El instrumento saca los de cada paso y
comprueba que aparecen en el **tramo de lineas que el propio candidato declara** como su origen.

**EL UNICO `NO ENCONTRADO` ES UN FALSO POSITIVO MIO Y LO DIGO.** `P10` de `mejorar_consciencia`
escribe *las `DOS` practicas* en versal por enfasis; mi expresion regular la leyo como nombre
propio. `L39` dice *We have developed **two** practices, storytelling and role plays*. **Es
transcripcion y el fallo es de mi tamiz.**

**Y DESPUES LEI A MANO**, porque el tamiz no sustituye a la lectura: **los `43` pasos que llevan
marca de periodo o de cantidad**, que son los que pueden esconder un periodo inventado, la
especie que el lote 1 ya pago. Van los que mas me preocupaban, con su linea:

| paso | lo que escribe | su linea | |
|---|---|---|---|
| `desplegar_plan` `P14` | una ronda de conversaciones de carrera **al anio** | `cap_12` `L27`, *one round... a year* | **TRANSCRIPCION** |
| `desplegar_plan` `P15` | **de tres a seis semanas**, dejando **una o dos** entre cada una | `cap_12` `L29`, *at least three to six weeks... a week or two between* | **TRANSCRIPCION** |
| `desplegar_plan` `P41` | **una vez al anio**, agrupadas en **dos semanas** | `cap_12` `L47`, *only once a year... a two-week period* | **TRANSCRIPCION** |
| `elegir_pregunta` `P12` | **una vez cada seis meses**, **una semana**, **tres meses** | `cap_13` `L137`, *once every six months... a week ago... three months ago* | **TRANSCRIPCION** |
| `abrazar_incomodidad_silencio` `P10` | la mayoria **no aguanta hasta seis** | `cap_13` `L195`, *Most people won't hold out till six* | **TRANSCRIPCION** |
| `escuchar_entender` `P13` | **mas de diez anios**, **tres minutos**, **una decada** | `cap_13` `L213`, *more than ten years... three minutes... a decade* | **TRANSCRIPCION** |
| `premiar_franqueza` `P3` | **nueve de cada diez veces** | `cap_13` `L219`, *nine times out of ten* | **TRANSCRIPCION** |
| `integrar_peticion` `P11` | las primeras **veinte o asi** | `cap_13` `L241`, *the first twenty or so times* | **TRANSCRIPCION** |
| `pedir_critica_primero` `P13` | las **cinco** dinamicas, nombradas | `cap_13` `L109`, *Psychological Safety, Dependability, Structure & Clarity, Meaning, and Impact* | **TRANSCRIPCION** |
| `dar_elogio` `P16` | emparejarse y **un** elogio concreto cada uno | `cap_13` `L283`, *Pair up... share one specific piece of praise* | **TRANSCRIPCION** |

### 5.2. LA TABLA, Y EL TECHO DE CANDIDATOS

    $ python .t1_v23_auditor/volumen_auditor_v23.py
    capitulo candidatos pasos      puentes    pasos inventados
    ------------------------------------------------------------------
    cap_12   2          50         0          0.00 por ciento
    cap_13   12         212        0          0.00 por ciento
    ------------------------------------------------------------------
    LOTE v23 14         262        0          0.00 por ciento

**FIRMO EL `0,00` DE LAS DOS FILAS**, con el instrumento de `5.1` y la lectura de los `43` detras,
y con la advertencia de `8.3` punto 2 delante de los ojos todo el rato. **Si aparece un puente en
mi turno normal, la cifra que cae es MIA y no suya**, porque acabo de firmarla.

**EL TECHO DE CANDIDATOS (`EXTRACTOR.md` `12.4`), MEDIDO:** `cap_12` dio `2` y `cap_13` dio `12`.
**Ninguno de los dos pasa de `15`**, asi que **el disparador del cierre corto por techo no se
cumple en ninguno de los dos capitulos**, y una vuelta que hubiera cerrado en `cap_13` tendria que
declarar otro motivo. **Lo dejo medido aqui porque `12.4` me manda verificar que el cierre corto
se DECLARE**, y eso solo lo puedo comprobar cuando vea el reporte.

**Y LA FILA QUE MANDA NO ES NINGUNA DE ESTAS DOS.** `8.2` decide la escalada **sobre el peor
capitulo del lote**, y el peor del lote 4 sigue siendo `cap_04` con `16,67`, que ya disparo el
freno en la `ACTA 22`. **Dos capitulos a `0,00` no lo borran**, y no soy yo quien reinicia eso.

---

## 6. LO QUE ESTA APERTURA CLASIFICA, EN UNA TABLA

| pieza | mi clase ciega | sobre que la digo |
|---|---|---|
| `cap_12` frontera | **`3` piezas, no `2`** | `L19` a `L23` tiene rotulo del mismo rango y mas cuerpo (`193` contra `116`) que la pieza que si se hizo nodo (`2.3`) |
| `cap_12` `L51` reparto de la semana | **no es nodo, pero el donante absorbe tres pasos** | `repartir_semana_cuarenta_horas_jefe` verificado en la bandeja; `L51` anade las cinco horas de reuniones a solas, las rachas y el `8/12/5` (`2.4`) |
| `cap_12` `L50` a `L65` resto | **fuera, y bien fuera** | cierre de unidad y peroracion, cero medios (`2.2`) |
| `cap_13` las `12` piezas | **las `12` se sostienen** | leidas contra su tramo; `P10` con su salto de `124` lineas y `P11` con su hueco interno son lectura y no barrido (`3.4`) |
| `cap_13` `L323` a `L331` `DIVERSITY AND INCLUSION` | **no es nodo, y lo marco DISCUTIBLE** | un medio suelto (la cena de practica) dentro de la narracion de como se monto un taller propio; no es el inventario que `D.27` pide (`3.3`) |
| `cap_13` `L333` a `L345` `WHAT'S NEXT?` | **fuera sin reparo** | hoja de ruta comercial, cero medios ejecutables (`3.3`) |
| `cap_13` los cuatro casos narrados | **fuera, y bien fuera** | el caso no es la casa; sus medios viajan en la pieza que los enmarca (`3.2`) |
| `contar_historias_propias` contra `contar_cuatro_historias_propias` | **`CONTINUA`, no `REPITE`** | queda procedimiento en los dos lados, y el par lo declara el libro en `L43` (`3.5`) |
| las cuatro piezas de pedir critica contra `abrazar_incomodidad_arrancar_critica_equipo` | **pares que hay que resolver, y la senial no los levanta** | `L113` dice que el afterword profundiza los cuatro consejos de `cap_09`; mi mayor senial es `0,149` contra un umbral de `0,35` (`4.3`) |
| `PASOS INVENTADOS` `cap_12` | **`0,00` por ciento**, `0` de `50` | firmada por mi con instrumento y lectura (`5`) |
| `PASOS INVENTADOS` `cap_13` | **`0,00` por ciento**, `0` de `212` | firmada por mi con instrumento y lectura (`5`) |
| cobertura del lote 4 | **falta `cap_14` y solo `cap_14`** | `cap_14.md` existe con `243` lineas y la bandeja tiene `0` piezas suyas (`1`) |

### 6.1. MIS PROPIAS CAIDAS DE ESTA FASE, CAZADAS ANTES DE PUBLICAR (`5.3`)

1. **La poblacion del barrido en `493` en vez de `330`**, por tragarme los `163` del ensayo de
   referencia. Corregida en el instrumento, contrastada contra `informe.poblacion_de_bandejas()`
   y cuadrada contra el `316` de la `ACTA 22` (`4.1`). **Ninguna version falsa llego a este
   documento.**
2. **El falso positivo `DOS` de mi tamiz de fidelidad** (`5.1`), que es errata de mi expresion
   regular y no del paso.
3. **Mi barrido no levanta el par mas obvio de la vuelta** (`abrazar_incomodidad` contra
   `abrazar_incomodidad`), y el extractor si lo cito (`4.3`). **Errata de mi instrumento,
   declarada con su nombre.**

### 6.2. LO QUE NO HE PODIDO CORRER, Y NO PUBLICO NINGUNA CIFRA SUYA

`python forja.py informe` sobre los catorce **se lanzo y no habia terminado** cuando cerre esta
apertura: la corrida cruza `14` candidatos contra `330` de poblacion y pasa de los limites de
tiempo que tengo aqui. **No publico ni una cifra suya** (`D.38.3`), y el saldo de aduana de la
vuelta lo mido en mi turno normal. **Lo que `D.38.4` me pedia es MI barrido, y ese esta corrido
entero en la seccion `4` con su poblacion cuadrada contra la de la casa.**

---

**Escrito sin abrir `REPORTE.md`, `loop.log`, `ultimo_extractor.json` ni `ultimo_auditor.json`, y
sin recuperar ninguno de los cuatro de git. No lo commiteo: lo sella el arnes.**
