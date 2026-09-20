# APERTURA CIEGA DE LA VUELTA 53, lote 7 (`grove_high_output`), `cap_06` y la cabeza de `cap_07`

*Linea **serial** (`extraccion-mundo-11`). Escrita ANTES de ver `docs/loop/REPORTE.md`, que el arnes
retiro del arbol. **Modo austero** (`D.47`): no repito lo que el registro ya dice.*

> **TODA CIFRA DE ESTA PAGINA LLEVA SU INSTRUMENTO PEGADO** (`D.38.3`), y **toda conclusion sobre
> contenido va en linea aparte marcada `LECTURA`**. Una cifra sin instrumento al lado no se publica.

---

## 0. LO QUE EL ARNES ME PIDE DECLARAR, Y VA PRIMERO

### **ACTA ANTERIOR LEIDA: `b9d9a8855f76d735bb302aeb89021d44099f0935`**

**HEREDADOS: `0`.** No hay ningun remedio ni ninguna tarea bloqueante que declarar, y **no lo digo de
memoria: lo mide el instrumento de la casa** (`D.40`).

    $ python forja.py herencia | grep -E "su huella|heredados"
      su huella     : b9d9a8855f76d735bb302aeb89021d44099f0935
      heredados     : 0

**Y COMPRUEBO QUE LA HUELLA ES LA DEL FICHERO QUE TENGO DELANTE**, que es lo unico que distingue
haber leido el acta de decir que se leyo:

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    b9d9a8855f76d735bb302aeb89021d44099f0935

**LECTURA:** la huella que el prompt me entrega **no es un commit, es el blob del propio
`ACTA_AUDITOR.md`** (`git cat-file -t` responde `blob`), y coincide al digito con el fichero que abri.
La ultima acta escrita es la **`ACTA 51`, que cubre la vuelta `52`**; yo cubro la **`53`**, la
inmediatamente siguiente: **NO HAY HUECO DE ACTA** (`AUDITOR_FORJA.md` `1.0`).

    $ grep -n "^# ACTA" docs/loop/ACTA_AUDITOR.md | tail -1 | cut -c1-60
    38255:# ACTA 51. VUELTA 52, lote 7 (`grove_high_output`), `cap_05`

**NO HAY NINGUN `NO APLICA` QUE SOSTENER**, porque con `0` heredados no hay nada a lo que aplicar
(`D.40`, 16 sep). La salida de arriba es la que lo sostiene.

## 0.1. LO QUE SE ME RETIRO, COMPROBADO Y NO SUPUESTO

**El arnes escribio la linea de mi turno en `loop.log`, que NO se retira, y la leo ahi:**

    $ grep -n "APERTURA CIEGA" docs/loop/loop.log | tail -1
    3987:[2026-09-19 22:39:12] VUELTA 9 : APERTURA CIEGA (claude-opus-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

    $ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    ls: cannot access 'docs/loop/ultimo_extractor.json': No such file or directory
    ls: cannot access 'docs/loop/ultimo_auditor.json': No such file or directory
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory

**NO LOS RECUPERO DE `git` NI POR NINGUNA OTRA VIA**, y declaro ademas lo que SI podria haber abierto
y no abri: **la vuelta dejo `64` ficheros de trabajo en `.v53/`**, que no son ninguno de los cuatro
que `D.34.2` retira, pero **contienen su lectura**: sus salidas de aduana candidato a candidato, su
muestra y su tabla de pasos inventados.

    $ ls .v53/ | wc -l
    64

**LECTURA:** abrirlos seria leer a ciegas lo que vengo a leer a ciegas. **No abri ninguno**, y lo
escribo aqui para que se pueda comprobar contra el sello. Lo que si abri, porque es obra mia y la
regla lo dice con todas las letras, es **`ACTA_AUDITOR.md` y `PROMPT_SIGUIENTE.md`**, mis dos sedes
(`AUDITOR_FORJA.md` `5.6`).

---

## 1. EL MATERIAL QUE ABRO, MEDIDO

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl

    $ ls cuarentena/grove_high_output/*.json | wc -l
    65

    $ ls cuarentena/*/*.json | grep -v _insertados | grep -v _derivadas | grep -v ensayo_referencia_163 | wc -l
    68

**EL LOTE DE ESTA VUELTA SON `9` FICHAS**, y no me lo dice el reporte: **me lo dice el arbol**, que es
lo que el reporte tendra que reproducir.

    $ git log --oneline -6 --name-status | grep -E "^A	cuarentena/grove" | sort -u
    A	cuarentena/grove_high_output/anunciar_decision_inesperada_reconvocar_reunion.json
    A	cuarentena/grove_high_output/conducir_etapas_modelo_ideal_decision.json
    A	cuarentena/grove_high_output/cortar_discusion_libre_momento_justo.json
    A	cuarentena/grove_high_output/decidir_nivel_competente_inferior.json
    A	cuarentena/grove_high_output/ejercer_poder_posicion_etapa_decision_clara.json
    A	cuarentena/grove_high_output/planificar_tres_pasos_demanda_estado_brecha.json
    A	cuarentena/grove_high_output/tomar_mando_reunion_pares_presidente_ausente.json
    A	cuarentena/grove_high_output/vencer_sindrome_grupo_pares_autoconfianza.json
    A	cuarentena/grove_high_output/zanjar_seis_preguntas_decision_adelantado.json

**Y `0` MOVIMIENTOS DE DATO**, que es lo que mi propio encargo mandaba (`TAREA 3`, **CERO
INSERCIONES**):

    $ git log --oneline -6 --name-status | grep -E "^[AM]	(dataset|bitacora|censos)/" | wc -l
    0

### 1.1. LOS PASOS DEL LOTE, CONTADOS POR MI Y NO COPIADOS

    $ python pasos_por_capitulo.py <las nueve fichas>
    anunciar_decision_inesperada_reconvocar_reunion      cap_06    8 pasos
    conducir_etapas_modelo_ideal_decision                cap_06   12 pasos
    cortar_discusion_libre_momento_justo                 cap_06    7 pasos
    decidir_nivel_competente_inferior                    cap_06    8 pasos
    ejercer_poder_posicion_etapa_decision_clara          cap_06    7 pasos
    planificar_tres_pasos_demanda_estado_brecha          cap_07    6 pasos
    tomar_mando_reunion_pares_presidente_ausente         cap_06    6 pasos
    vencer_sindrome_grupo_pares_autoconfianza            cap_06    5 pasos
    zanjar_seis_preguntas_decision_adelantado            cap_06    9 pasos
    ---
    cap_06   8 fichas  62 pasos
    cap_07   1 fichas  6 pasos
    TOTAL    9 fichas  68 pasos

**El conteo es `len(pasos_accionables)` de cada fichero y el capitulo se lee de la `UNIDAD DE ORIGEN`
que la propia ficha escribe.** El guion vive fuera del arbol, en el directorio de trabajo de esta
sesion, **para no mover ni un byte del repo en mi fase**.

### 1.2. EL CUERPO DE LOS TRES CAPITULOS DE LA FRONTERA, MEDIDO HOY

    $ for c in cap_06 cap_07 cap_08; do sed -e '1,7d' fuentes/grove_high_output/$c.md | wc -w; done
    4122  cap_06
    3832  cap_07
    1138  cap_08

**Lo dejo medido aqui, antes de ver su tabla**, porque la `TAREA 2` que yo escribi manda que la suma
de las filas de cada frontera de el `wc -w` del cuerpo. **Estas son las tres cifras contra las que se
cierra**, y quedan selladas antes de que yo vea las suyas.

---

## 2. MI LECTURA DE `cap_06` ENTERO, PIEZA A PIEZA

**Lei `fuentes/grove_high_output/cap_06.md` entero** (`95` lineas, `Cap. 5`, `Decisions, Decisions`)
**antes de abrir ninguna ficha**, y esta es la frontera que YO levanto, por linea:

| tramo | que trae | procedimiento? | minado? |
|---|---|---|---|
| `L13` a `L19` | el problema: poder de posicion contra poder de conocimiento | **no**, es el planteamiento | no |
| `L23`, `L27`, `L29` | las tres etapas del modelo ideal, cada una con su contenido | **si** | **si**, ficha 1 |
| `L31` | por que el modelo cuesta a los mandos intermedios | no, es diagnostico | no |
| `L33` | la decision en el nivel competente mas bajo, con el temple del criterio | **si** | **si**, ficha 2 |
| `L35` | el caso del periodista y los simbolos de estatus | no, es caso del autor | no |
| `L41` | el juego de rol y el nombre `par mas uno` | **no**: es la narracion de donde sale el nombre, y **su procedimiento vive en `L51`** | no |
| `L45`, `L47` | el testimonio de John y la comparacion con el caso del automovil | no, es testimonio | no |
| `L49` | vencer el sindrome con autoconfianza | **si** | **si**, ficha 6 |
| `L51` | quien toma el mando si no hay presidente formal | **si** | **si**, ficha 7 |
| `L53` | el miedo a sonar tonto | **no**: *una advertencia es linea* (vara `6.1`). Una postura no ejecuta una busqueda | no |
| `L55` | el miedo del junior a ser desautorizado | no, es diagnostico | no |
| `L57` | la incertidumbre cuando conocimiento y posicion se separan | no, es diagnostico | no |
| `L61` | cuando es legitimo ejercer el poder de posicion, y cuando no | **si** | **si**, ficha 4 |
| `L63` | el criterio del momento de cortar la discusion libre | **si** | **si**, ficha 3 |
| `L65` a `L77` | las seis preguntas que se zanjan por adelantado | **si** | **si**, ficha 5 |
| `L79` a `L89` | el caso de la planta de Filipinas | no, es el caso del autor aplicando las seis | no |
| `L91` | aplicar la estructura antes del hecho para evitar el veto tardio | **no como ficha propia**: el procedimiento **es el mismo** que el de `L65` a `L77`, y lo que anade es el motivo | no |
| `L93` | anunciar lo inesperado, levantar la sesion y reconvocar | **si** | **si**, ficha 8 |
| `L95` | la cita de Sloan y el mando que se fue y volvio | no, es cierre | no |

> ### **LECTURA: por mi lectura, `cap_06` queda ENTERO en `8` piezas, y las `4` que no se minan las nombro yo con su motivo.**
>
> Las cuatro que un lector podria echar en falta son `L41`, `L53`, `L55` y `L91`, y **ninguna de las
> cuatro sostiene una ficha propia**: dos son diagnostico, una es advertencia (que la vara `6.1`
> llama **linea** y no procedimiento), y la cuarta **repite el procedimiento de las seis preguntas**
> cambiandole el motivo. **Si el reporte declara `cap_06` entero, mi lectura lo sostiene.**

### 2.1. Y LA CABEZA DE `cap_07`

`cap_07` es `Cap. 6`, `Planning: Today's Actions for Tomorrow's Output`, `105` lineas. **Su cabeza es
`L17` y `L19`**: `L17` recapitula los tres pasos de la fabrica y `L19` los generaliza a cualquier
organizacion (demanda del entorno, estado presente, conciliar los dos). **Eso es la ficha 9.**

> **LECTURA: `cap_07` queda ABIERTO y con mucho cuerpo por minar**, y lo digo con lo que lei: `L31`
> (por que no se mezclan los pasos), `L35` (`STEP 2`, la misma moneda y el canal de proyectos), `L39`
> (`STEP 3`, las dos preguntas de la brecha y la definicion de estrategia), `L41` (estrategia contra
> tactica), `L53` (Cindy y los desfases de tiempo) y `L57` a `L59` (la salida verdadera del proceso
> de planificacion) **traen procedimiento y no estan minados**. Un cierre corto en la cabeza del
> capitulo es lo que yo esperaria de un turno con techo de minutos, **pero el techo tiene que venir
> declarado con su cifra** (`EXTRACTOR.md` `12.4`, y mi `TAREA 3`).

---

## 3. MI CLASE PARA CADA UNA DE LAS NUEVE FICHAS

**Adjudico con la vara** (`AUDITOR_FORJA.md` `6.1`): la pregunta es si el candidato **CONTINUA** el
trabajo del existente o lo **REPITE**; tiene direccion (que anade el hijo a la madre), **no tiene
bascula** (el tamanio del solape no decide), y **decide si lo que queda fuera es procedimiento en los
dos lados**.

### FICHA 1. `conducir_etapas_modelo_ideal_decision`, `L23` `L27` `L29`, `12` pasos

- **CLASE: SANO, ficha nueva.** El libro anuncia las tres etapas y **pone el contenido de cada una**:
  la prueba del inventario se cumple entera.
- **FIDELIDAD `D.30`: `12` de `12` TRANSCRIPCION, `0` PUENTE.** Los pasos `1` a `4` salen de `L23`,
  los `5` a `8` de `L27`, los `9` a `12` de `L29`.
- **VECINO QUE YO LEVANTO, Y ES UNA FRONTERA:** `dirigir_reunion_decision` del grafo dice en su paso
  `3` **`No busques consenso`**; este dice, por `L63` del mismo capitulo, **empuja hacia un consenso y
  si no sale decide tu**. **DOS DOCTRINAS LEGITIMAS NO SON DUPLICADO: son FRONTERA DECLARADA**
  (vara `6.1`, ultima fila). **No es REPITE.**

### FICHA 2. `decidir_nivel_competente_inferior`, `L33`, `8` pasos

- **CLASE: CONTINUA**, y **es el par mas apretado del lote**. La madre es
  `repartir_decision_cercanos_hechos` (grafo): *repartir las decisiones entre los mas cercanos a los
  hechos*. El hijo **anade procedimiento propio que la madre no trae**: que el saber tecnico
  **se temple con criterio**, que la decision se situe **en el terreno intermedio** entre el
  conocimiento y los golpes, que **si nadie reune las dos cualidades se busque la mejor mezcla**, y
  que **se traiga a un rango superior solo para poner experiencia**, hablando todos como iguales.
- **Y LO QUE QUEDA FUERA EN LA MADRE TAMBIEN ES PROCEDIMIENTO**: su diagnostico del bote de basura,
  ir a la reunion y mirar a la sala, la pregunta que abre la conversacion y el reconvocar al dia
  siguiente. **Procedimiento en los dos lados: NO es REPITE** (`6.1`).
- **FIDELIDAD: `8` de `8` TRANSCRIPCION**, con **una nota mia**: el paso `7` convierte una practica
  declarada del autor (*we at Intel are likely to ask*) en un imperativo. **No es PUENTE** (no anade
  contenido que el libro no tenga), pero **lo marco yo antes de ver su reporte**.
- **ES MI DISCUTIBLE NUMERO `1`.**

### FICHA 3. `cortar_discusion_libre_momento_justo`, `L63`, `7` pasos

- **CLASE: SANO con vecindad declarada.**
- **VECINO DEL GRAFO, Y ES LA SEGUNDA FRONTERA:** `fijar_fecha_cierre_debate_equipo` manda en su
  paso `5` **resistir el impulso de cerrar el debate** y en su `6` que **a menudo el trabajo del jefe
  es mantener el debate vivo**; esta ficha pone el criterio de **cuando cortar** y avisa de la
  **busqueda interminable de consenso**. Las dos son legitimas y **miran el mismo momento desde los
  dos lados**: **FRONTERA DECLARADA, no duplicado.**
- **VECINO DEL PROPIO LOTE:** la ficha `4`. Comparten *si no hay consenso, entra y decide*. Lo que
  queda fuera es procedimiento en los dos lados (aqui, la prueba de **haber oido los asuntos de
  verdad**; alli, la **prueba de legitimidad** del poder de posicion). **NO es REPITE.**
- **FIDELIDAD: `7` de `7` TRANSCRIPCION.**
- **ES MI DISCUTIBLE NUMERO `2`.**

### FICHA 4. `ejercer_poder_posicion_etapa_decision_clara`, `L61`, `7` pasos

- **CLASE: CONTINUA sobre la ficha `1` del propio lote.** La madre pone la etapa de **decision
  clara**; el hijo pone **quien la toma cuando no hay consenso y desde que momento es legitimo**.
- **FIDELIDAD: `7` de `7` TRANSCRIPCION**, con **una nota mia**: el paso `6` recoge la reticencia a
  dar ordenes **dejando caer el sujeto que el libro le pone** (*We Americans*), con lo que una
  observacion que el autor acota a una cultura **queda escrita como universal**. **No inventa
  procedimiento**, asi que no lo llamo PUENTE, **pero lo marco**.
- **ES MI DISCUTIBLE NUMERO `3`.**

### FICHA 5. `zanjar_seis_preguntas_decision_adelantado`, `L65` a `L77`, `9` pasos

- **CLASE: SANO.** Las seis preguntas estan en el libro como lista, y los pasos `4` a `9` son las
  seis, una por una.
- **VECINO:** `montar_reunion_gran_decision` del grafo comparte **el decisor nombrado** y **el poder
  de veto**, pero es **un formato de reunion** con sus logisticas, y esta es **una lista que se zanja
  antes del hecho**. Procedimiento en los dos lados: **no duplicado.**
- **FIDELIDAD: `9` de `9` TRANSCRIPCION.**

### FICHA 6. `vencer_sindrome_grupo_pares_autoconfianza`, `L49`, `5` pasos

- **CLASE: SANO.**
- **FIDELIDAD: `4` de `5` TRANSCRIPCION limpias y `1` que yo marco.** El paso `5` escribe *haz que
  todo el mundo en tu operacion entienda esto, y no solo los que se sientan a la mesa*. El libro
  escribe *everyone in your operation should be made to understand this* **y no escribe el contraste**.
- **LECTURA: es el unico sitio de las nueve fichas donde yo dudaria entre TRANSCRIPCION y PUENTE.**
  Lo leo como transcripcion **porque `en tu operacion` ya se opone a `en la reunion` en el propio
  libro**, y el inciso explicita esa oposicion sin anadir procedimiento. **Si cae, cae DENTRO de mi
  marcado.**
- **ES MI DISCUTIBLE NUMERO `4`.**

### FICHA 7. `tomar_mando_reunion_pares_presidente_ausente`, `L51`, `6` pasos

- **CLASE: SANO**, vecino de la ficha `6` por el mismo sindrome, pero **otra operacion**: la `6`
  **previene** construyendo autoconfianza, la `7` **reparte el mando cuando ya esta pasando**.
- **FIDELIDAD: `6` de `6` TRANSCRIPCION.**

### FICHA 8. `anunciar_decision_inesperada_reconvocar_reunion`, `L93`, `8` pasos

- **CLASE: SANO con vecindad fuerte.**
- **VECINO DEL GRAFO, Y ES LA TERCERA FRONTERA:** `dar_mala_noticia_decision_tomada` manda **asumir
  la decision, ser firme y NO abrirla a discusion**; esta manda **reconvocar y pedir su opinion sobre
  la decision**. **Se concilian y lo digo con lo que leo**: la escena es otra (alli, uno a uno con la
  persona afectada; aqui, el grupo que participo en el proceso) y **el objeto tambien**: Grove **no
  reabre la decision**, pide la opinion **para que la acepten y aprendan a vivir con ella**. **No es
  REPITE**, y la arista se declara por lectura (`D.29`).
- **FIDELIDAD: `8` de `8` TRANSCRIPCION.**

### FICHA 9. `planificar_tres_pasos_demanda_estado_brecha`, `cap_07` `L19` y `L17`, `6` pasos

- **CLASE: SANO.** Es la cabeza del capitulo y **generaliza** los tres pasos de la fabrica.
- **VECINO DE BANDEJA:** `casar_flujo_fabricacion_flujo_ventas`, del `cap_02`, es **los dos flujos
  paralelos y la holgura**, no los tres pasos. **No duplicado.**
- **FIDELIDAD: `6` de `6` TRANSCRIPCION**, con **una nota mia**: el paso `1` cierra con *y no sobre
  otra cosa*, un enfasis que el libro no escribe. **Misma especie que la nota de la ficha `6`, mas
  leve.**

---

## 4. LA CIFRA DE FIDELIDAD QUE FIRMO A CIEGAS

**`PASOS INVENTADOS POR CAPITULO`, por MI lectura, con una fila por capitulo y no una media**
(`AUDITOR_FORJA.md` `8`, `8.2`):

| capitulo | pasos escritos | PUENTE por mi lectura | por ciento | de muestra o entero |
|---|---|---|---|---|
| `cap_06` | `62` | `0` | **`0,0`** | **entero**, las `8` fichas |
| `cap_07` | `6` | `0` | **`0,0`** | **entero**, la ficha unica |
| **total del lote** | **`68`** | **`0`** | **`0,0`** | |

**Denominador medido en `1.1`. Ninguna fila pasa del tope de `10`** (`8.1`), asi que **por mi lectura
no se dispara la relectura entera de `D.58` en ningun capitulo**, y **el lote siguiente no baja
escalon por esta metrica**.

**Y LAS CUATRO NOTAS QUE MARQUE ESTAN DENTRO DE ESE `0`**: las cuatro las leo como TRANSCRIPCION y
**las cuatro quedan escritas arriba con su linea**, para que si alguna cae, caiga **dentro de mi
marcado** y no fuera.

### 4.1. LA MUESTRA CON SU SEMILLA, CORRIDA POR MI ANTES DE VER LA SUYA

**Es la comprobacion que `D.58` hace auditable**: quien audita vuelve a correr el instrumento con la
misma semilla y **tiene que salirle la misma lista**.

    $ python scripts/muestra_fidelidad.py --libro grove_high_output --capitulos cap_06,cap_07,cap_08 --semilla v53
    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : grove_high_output
      semilla  : v53
      capitulos: cap_06, cap_07, cap_08

      RELEIDO ENTERO : cap_07
      POR MUESTRA    : cap_06, cap_08, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_06: 15 paso(s) en la muestra
        anunciar_decision_inesperada_reconvocar_reunio P1   Comprueba la condicion: la palabra final va a ser radicalmen
        anunciar_decision_inesperada_reconvocar_reunio P5   Levanta la sesion.
        anunciar_decision_inesperada_reconvocar_reunio P6   Reconvoca la reunion despues de que la gente haya tenido oca
        conducir_etapas_modelo_ideal_decision          P4   Cuenta con que, si los que saben se guardan su opinion, lo q
        conducir_etapas_modelo_ideal_decision          P9   Exige por ultimo que todos los implicados den pleno apoyo a
        cortar_discusion_libre_momento_justo           P4   Pero en cuanto sientas que ya lo has oido todo y que todos l
        cortar_discusion_libre_momento_justo           P7   Pasa a tomar la decision en el momento justo, que es lo deci
        decidir_nivel_competente_inferior              P3   No entiendas saber como entender tecnicamente y nada mas: es
        decidir_nivel_competente_inferior              P4   Cuenta con que ese criterio se desarrolla con la experiencia
        ejercer_poder_posicion_etapa_decision_clara    P2   Cuando eso pase, acepta que la persona de mayor rango, la de
        ejercer_poder_posicion_etapa_decision_clara    P3   Comprueba que el proceso vino bien hasta ese punto: que quie
        tomar_mando_reunion_pares_presidente_ausente   P3   Si eso no funciona, pide siempre que puedas a la persona pre
        vencer_sindrome_grupo_pares_autoconfianza      P3   Apoya otra parte en la experiencia.
        vencer_sindrome_grupo_pares_autoconfianza      P4   Cuenta con que al final la autoconfianza sale sobre todo de
        zanjar_seis_preguntas_decision_adelantado      P3   Zanja por adelantado las seis preguntas importantes, que es

      --- cap_08: 0 paso(s) en la muestra

      --- cap_07: ENTERO, 6 paso(s), no hay muestra que elegir

**MI VEREDICTO SOBRE ESOS `15`: los `15` son TRANSCRIPCION, `0` PUENTE**, cada uno contra la linea de
su tramo (`L93`, `L23`, `L29`, `L63`, `L33`, `L61`, `L51`, `L49`, `L65`). **`0,0` por ciento sobre la
muestra de `cap_06`.**

**Y `cap_08` SALE CON `0` PASOS**, que es coherente con un lote que no llego a minarlo. **Su fila
existe y dice `0` en vez de desaparecer**, que es lo que mi propia `TAREA 4` mandaba.

### 4.2. LAS CITAS DEL LOTE, COMPROBADAS UNA A UNA CONTRA EL LIBRO

**Cada ficha cita en ingles el tramo del que saca cada paso. Comprobe que esas citas EXISTEN donde
dicen**, que es lo unico que una maquina puede decidir sobre fidelidad:

    $ python citas2.py <las nueve fichas>
    anunciar_decision_inesperada_reconvocar_reunion      cap_06  fragmentos:  6   NO HALLADOS: 0
    conducir_etapas_modelo_ideal_decision                cap_06  fragmentos: 17   NO HALLADOS: 0
    cortar_discusion_libre_momento_justo                 cap_06  fragmentos: 11   NO HALLADOS: 0
    decidir_nivel_competente_inferior                    cap_06  fragmentos: 12   NO HALLADOS: 0
    ejercer_poder_posicion_etapa_decision_clara          cap_06  fragmentos: 10   NO HALLADOS: 0
    planificar_tres_pasos_demanda_estado_brecha          cap_07  fragmentos:  8   NO HALLADOS: 0
    tomar_mando_reunion_pares_presidente_ausente         cap_06  fragmentos:  7   NO HALLADOS: 0
    vencer_sindrome_grupo_pares_autoconfianza            cap_06  fragmentos:  4   NO HALLADOS: 0
    zanjar_seis_preguntas_decision_adelantado            cap_06  fragmentos:  6   NO HALLADOS: 0
    ---
    fragmentos comprobados: 81   hallados en el capitulo: 81   NO hallados: 0

> ### **Y DECLARO UN FALLO MIO DE ESTA MISMA FASE, PORQUE LA PRIMERA PASADA DIO `11` FALSOS**
>
> Mi primer comparador exigia la puntuacion literal y me marco `11` fragmentos como no hallados.
> **Los `11` eran mios, no de las fichas:** la casa **prohibe el guion largo**, asi que una cita
> verbatim que en el libro lleva raya (*it is legitimate, in fact, sometimes unavoidable, for the
> senior person*) **tiene que escribirse con coma**, y mi comparador la contaba como inventada.
> **Volvi a correrlo sordo a la puntuacion y salieron `81` de `81`.**
>
> **Lo escribo aqui y no lo borro** porque si hubiera publicado aquel `11` habria sido **CIFRA
> PUBLICADA PROPIA**, que es la especie de mi propia racha.

---

## 5. EL BARRIDO DE VECINOS (`D.38.4`)

**La poblacion es GRAFO MAS BANDEJAS**, y **por el metodo vigente no la construyo yo a mano**: se la
entrega a la aduana, que pone las bandejas por su cuenta desde que `D.38.5` llego a `src/aduana.py`
(correccion declarada del 16 sep dentro de `D.38.4`, `ACTA 29` `6.6`). **El propio candidato queda
excluido de su poblacion** por `resolutor.mismo` en `src/aduana.py:495`, que es la correccion de la
`ACTA 18`.

**CORRI LA LETRA DEL BANCO: UNA PASADA POR CANDIDATO, LAS NUEVE**, cada una con su propio proceso.

    $ python forja.py informe cuarentena/grove_high_output/<cada una de las nueve>.json

**Y LAS NUEVE MIDIERON LA MISMA POBLACION, que es lo que `D.38.5` prometia:**

    poblacion del barrido       : 414   (346 del grafo mas 68 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

**`414` cuadra al digito con lo que yo habia medido por mi cuenta en la seccion `1`**: `346` de
`wc -l dataset/nodos.jsonl` mas `68` de contar las bandejas descartando `_insertados`, `_derivadas` y
`ensayo_referencia_163`. **Mi cifra de vecinos y la de la maquina ya son comparables** (`D.38.5`).

### 5.1. EL SALDO DE LAS NUEVE

| candidato | saldo | vecinos que le levanta la maquina |
|---|---|---|
| `anunciar_decision_inesperada_reconvocar_reunion` | BLOQUEARIA | `6` |
| **`conducir_etapas_modelo_ideal_decision`** | **ENTRARIA sin leer nada** | **`0`** |
| `cortar_discusion_libre_momento_justo` | BLOQUEARIA | `4` |
| `decidir_nivel_competente_inferior` | BLOQUEARIA | `3` |
| `ejercer_poder_posicion_etapa_decision_clara` | BLOQUEARIA | `2` |
| `planificar_tres_pasos_demanda_estado_brecha` | BLOQUEARIA | `1` |
| `tomar_mando_reunion_pares_presidente_ausente` | BLOQUEARIA | `4` |
| `vencer_sindrome_grupo_pares_autoconfianza` | BLOQUEARIA | `9` |
| `zanjar_seis_preguntas_decision_adelantado` | BLOQUEARIA | `1` |

**`0` CAERIAN por una guarda y `0` CHOCAN entre si**, en las nueve pasadas.

### 5.2. DONDE VIVEN ESAS `30` VECINDADES, Y ES LA MEDIDA QUE MAS VALE DE MI FASE

    $ (clasificando cada vecino levantado por donde vive)
    vecindades levantadas en total : 30
      del propio lote              24
      de bandeja, fuera del lote   4
      del grafo                     2
    por senial:
      similitud_texto              28
      familia_id                    1
      paso_contra_nodo              1

    LAS QUE TOCAN EL GRAFO:
      anunciar_decision_inesperada_reconvocar_reunion -> dirigir_reunion_decision            [familia_id]
      vencer_sindrome_grupo_pares_autoconfianza       -> aprender_resultados_vencer_dos_presiones [paso_contra_nodo]

> ### **LECTURA: `28` de las `30` vecindades las levanta `similitud_texto`, y NINGUNA de esas `28` llega al grafo.**
>
> De `346` nodos vivos, **la senial de texto no levanta ni uno**. Las dos unicas vecindades que
> tocan el grafo las levantan las **otras dos** seniales. **El `80` por ciento de la cola que este
> lote abre (`24` de `30`) son las nueve fichas mirandose entre ellas**, que es lo esperable en un
> lote escrito el mismo dia con la misma mano sobre el mismo capitulo.

### 5.3. Y LO QUE ESO LE HACE A MI LECTURA: `0` DE `6`

**Mi lectura de la seccion `3` levanta `6` pares contra material que ya existe.** Comprobe uno por
uno si la maquina los levanta tambien, **y la respuesta es que no levanta ninguno**:

| par que YO levanto por lectura | lo levanta la senial? |
|---|---|
| ficha `1` contra `dirigir_reunion_decision` (grafo), **frontera del consenso** | **NO**: esa ficha sale con `0` vecinos |
| ficha `2` contra `repartir_decision_cercanos_hechos` (grafo), **el par mas apretado del lote** | **NO** |
| ficha `3` contra `fijar_fecha_cierre_debate_equipo` (grafo), **frontera de cuando cortar** | **NO** |
| ficha `5` contra `montar_reunion_gran_decision` (grafo) | **NO** |
| ficha `8` contra `dar_mala_noticia_decision_tomada` (grafo), **frontera de como se anuncia** | **NO** |
| ficha `9` contra `casar_flujo_fabricacion_flujo_ventas` (bandeja) | **NO** |

**Y AL REVES TAMBIEN: de las `2` que la maquina levanta contra el grafo, ninguna es de las mias.**
La de `familia_id` (`anunciar` contra `dirigir_reunion_decision`) **apunta al nodo que yo levanto,
pero desde otra ficha**: yo lo levanto contra la ficha `1` por la doctrina del consenso.

> ### **LECTURA: esto NO es una caida de la vuelta, y digo por que con su cita.**
>
> **Es la averia que la propia vuelta anoto hoy como `d058`**, *la senial 1 compara mi prosa, no los
> pasos del libro*, que yo leo en `scripts/deuda.py` y no en su reporte. **Mi fase le pone un
> segundo ejemplar medido y una cifra: `0` de `6` por lectura, `0` de `28` por texto contra el
> grafo.**
>
> **Y LO QUE SI TENDRA QUE ESTAR EN SU REPORTE, porque mi propio encargo lo mandaba** (`TAREA 3`):
> *las aristas que la senial no levanta se declaran por lectura* (`D.29`) **con su razon escrita**.
> **Si esas seis, o las que el leyera, no estan declaradas por lectura en ningun sitio, lo que se
> pierde no es una arista: es la frontera.** Eso lo adjudico en el acta, con el reporte delante.
>
> **Y HAY UNA QUE MIRAR ANTES QUE NINGUNA:** `conducir_etapas_modelo_ideal_decision` es **la ficha
> mas grande del lote** (`12` pasos, las tres etapas del modelo) y **la maquina la dejaria entrar
> sin leer nada**. Hoy no entra, porque `D.39` tiene el lote cerrado y **lo mido**: `0` cambios en
> `dataset/` (seccion `1`). **Pero el dia de la insercion, esa es la ficha que entra a ciegas.**

---

## 6. LO QUE SELLO ADEMAS, MEDIDO ANTES DE VER EL REPORTE

**Son cifras del estado que el reporte va a declarar, y las dejo aqui para que se comparen contra
las mias y no al reves.**

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

**LECTURA: `gate` es la primera de las cuatro guardas que bloquean** (`D.55`) **y esta VERDE**, con
`censo_no_decrece` corriendo dentro de ella. **Por esta no hay averia.**

    $ python scripts/deuda.py
    DEUDA DE LA LINEA (D.55): la deuda no bloquea la produccion
      pendientes: 20    pagadas: 18
      ...
      d058   53      aduana             LA SENIAL 1 COMPARA MI PROSA, NO LOS PASOS DEL LIBRO
      ultima vuelta de saneamiento: 49

**LECTURA: la deuda sube de `19` a `20` y la que la sube es de esta vuelta**, `d058`. Mi encargo
mandaba **no pagar deuda hoy** y **anotar lo que apareciera**: por el registro, eso es lo que paso.
**Y `ultima vuelta de saneamiento: 49` confirma al digito que la de saneamiento es la `54`**, que es
lo que la `TAREA 1` fila `7` ya adjudicaba.

    $ ids del lote contra el grafo
    ids del lote: 9   distintos: 9   ya vivos en el grafo: 0
    nodos en el grafo: 346

**LECTURA: ninguna de las nueve colisiona por id**, ni entre ellas ni contra el grafo, asi que la
guarda `el id ya vive en el grafo` (que es **solo del grafo** por `D.38.5`) **no tiene que morder en
ninguna.**

### 6.1. UNA TENSION MEDIDA QUE NO ES CAIDA DE NADIE, Y LA REGISTRO SIN ABRIR COLA

**`D.58` ata el regimen a `MODO_INSERCION`**, y dice que en una vuelta de extraccion **no hay fase
ciega, ni sello, ni testigo**. **Mi encargo declaro `CLASE DE ESTA VUELTA: EXTRACCION`.** Y sin
embargo estoy escribiendo una fase ciega, porque **la corrida no esta en modo cuarentena**:

    $ grep -n "arranque: rama" docs/loop/loop.log | tail -1
    2632:[2026-09-19 00:12:29] arranque: rama extraccion-mundo-11, MODO_INSERCION=insertar

    $ grep -n "CLASE DE ESTA VUELTA" docs/loop/PROMPT_SIGUIENTE.md
    7:> # **CLASE DE ESTA VUELTA: EXTRACCION**

**LECTURA: el arnes hizo lo que `D.58` dice a la letra** (el modo es `insertar`, luego abre fase
ciega), **y la vuelta hizo lo que mi encargo dice a la letra** (extraer y no insertar). **Las dos
cosas son correctas y aun asi no coinciden**, porque `D.58` decide el regimen por **el modo del
arnes** y el encargo lo decide por **la clase de trabajo**. **No es caida de nadie, no la adjudico y
no abro cola**: la doctrina esta congelada en `11` (`D.55`, 18 sep) y lo que manda ahi es
**registrarla con su medida y dejarla ahi**. Queda registrada.

**Y LO DIGO SIN COBRARME NADA A FAVOR:** la fase ciega de mas **no me estorba**, me da la lectura
independiente que despues firma o tumba sus cifras. **Lo que senalo es que el disparador no esta
donde el trabajo esta.**

---

## 7. LO QUE NO PUEDO COMPROBAR EN ESTA FASE, Y LO ESCRIBO EN VEZ DE AFIRMARLO

**`AUDITOR_FORJA.md` `1.1`: una busqueda negativa no se puede citar.** Estas son las cosas que mi
turno normal tendra que medir, y que **hoy no afirmo en ningun sentido**:

| lo que no compruebo hoy | por que |
|---|---|
| **el reloj de aduana de la vuelta** y si el cierre corto en `cap_07` cae dentro del techo de `90` minutos | el dato vive en su reporte y en `.v53/`, y **no abro ninguno de los dos** |
| **la tabla de frontera de `cap_06`, `cap_07` y `cap_08`** celda a celda | tengo los tres `wc -w` de `1.2` **sellados**, pero su tabla esta en el reporte retirado |
| **la racha de credito de la linea** | `CREDITO_serial.jsonl` es uno de los cuatro retirados, y **no corro `forja.py credito` para rodear la retirada** |
| **si sus `SANO` llevan `RAZON` escrita** (`D.8`) | esta vuelta **no escribe veredictos**: `bitacora/VEREDICTOS.jsonl` sigue en `740` lineas y la insercion es de otro dia |
| **sus cifras de palabras por pieza** | mismo motivo: viven en su tabla |

---

## 8. LO QUE SELLO, EN UNA TABLA

| lo que firmo a ciegas | mi cifra | de donde sale |
|---|---|---|
| **ACTA ANTERIOR LEIDA** | `b9d9a8855f76d735bb302aeb89021d44099f0935` | `forja.py herencia` y `git hash-object`, seccion `0` |
| **HEREDADOS** | `0` | `forja.py herencia`, seccion `0` |
| **HUECO DE ACTA** | **NO HAY**: la `51` cubre la `52` y yo cubro la `53` | `grep "^# ACTA"`, seccion `0` |
| **fichas del lote** | `9` | `git log --name-status`, seccion `1` |
| **pasos del lote** | `68` (`62` de `cap_06`, `6` de `cap_07`) | `pasos_por_capitulo.py`, seccion `1.1` |
| **PUENTE por mi lectura** | **`0` de `68`**, `0,0` por ciento en las dos filas | seccion `4` |
| **citas del lote halladas en el libro** | **`81` de `81`** | `citas2.py`, seccion `4.2` |
| **`cap_06`** | **ENTERO en `8` piezas**, con las `4` no minadas nombradas y motivadas | seccion `2` |
| **`cap_07`** | **ABIERTO por la cabeza**, con `6` tramos de procedimiento sin minar que nombro | seccion `2.1` |
| **mis discutibles marcados** | **`4`**, los cuatro escritos antes de ver el reporte | fichas `2`, `3`, `4`, `6`, `9` |
| **fronteras que levanto contra el grafo** | **`3`** (`dirigir_reunion_decision`, `fijar_fecha_cierre_debate_equipo`, `dar_mala_noticia_decision_tomada`) | seccion `3` |
| **poblacion del barrido** | **`414`** (`346` del grafo mas `68` de bandejas), igual en las nueve pasadas | `forja.py informe`, seccion `5` |
| **saldo del barrido** | `8` BLOQUEARIAN, **`1` ENTRARIA sin leer nada**, `0` CAERIAN, `0` CHOCAN | seccion `5.1` |
| **vecindades levantadas** | **`30`**: `24` del propio lote, `4` de bandeja, **`2` del grafo** | seccion `5.2` |
| **pares que yo levanto y la senial no** | **`6` de `6`** | seccion `5.3` |
| **`gate`** | **VERDE**, `346` nodos | seccion `6` |
| **deuda** | **`20` pendientes**, `18` pagadas, la nueva es `d058` | seccion `6` |
| **dato movido en mi fase** | **`0` bytes del repo**: mis guiones viven fuera del arbol | seccion `1.1` |
| **fallo propio declarado en esta fase** | **`1`**: mi primer comparador de citas dio `11` falsos y no lo publique | seccion `4.2` |

> **NO COMMITEO ESTA PAGINA.** La sella el arnes y la commitea el, y **no la vuelvo a tocar despues
> del sello** (`D.34`).
