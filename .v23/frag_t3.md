
---

## Q.4. TAREA 3: `cap_12` Y `cap_13`. **CERRADA, Y LA VUELTA CIERRA AHI**

### Q.4.a. LOS TRES CUERPOS, REMEDIDOS POR MI, Y **UNA DISCREPANCIA CON MI ENCARGO QUE DECLARO**

*`EXTRACTOR.md` 5: una cifra del encargo no es fuente de una cifra mia. Las tres se remiden.*

Salida de los comandos, guardada en `.t1_v23/cuerpos_cap12_14.txt`:

    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_12.md | wc -w
    2118
    $ sed -n '1,7p' fuentes/scott_radical_candor/cap_12.md
    unidad: Getting Started
    titulo_textual: Getting Started
    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_13.md | wc -w
    9298
    $ sed -n '1,7p' fuentes/scott_radical_candor/cap_13.md
    unidad: Afterword
    titulo_textual: Afterword to the Revised Edition: Rolling Out Radical Candor
    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_14.md | wc -w
    7638
    $ sed -n '1,7p' fuentes/scott_radical_candor/cap_14.md
    unidad: Bonus Chapter
    titulo_textual: Bonus Chapter: A Radically Candid Performance Review

> ### **LAS TRES CIFRAS DEL ENCARGO SE CONFIRMAN AL DIGITO. DOS DE SUS TRES ROTULOS NO.**
>
> | unidad | rotulo que mi encargo escribe | rotulo que el fichero escribe hoy | palabras |
> |---|---|---|---:|
> | `cap_12` | `Getting Started` | `Getting Started` | **2.118** |
> | `cap_13` | `Afterword to the Revised Edition` | `Afterword to the Revised Edition: Rolling Out Radical Candor` | **9.298** |
> | `cap_14` | `Bonus Chapter: A Radical Respect Framework` | `Bonus Chapter: A Radically Candid Performance Review` | **7.638** |
>
> **LA DE `cap_14` NO ES UN RECORTE: ES OTRO TITULO.** *A Radical Respect Framework* y *A Radically
> Candid Performance Review* no son la misma cosa. **No la resuelvo copiando** (`EXTRACTOR.md` 5):
> declaro la discrepancia, publico lo que mide mi instrumento hoy, y **la traigo como pregunta**
> en `Q.10`. No me bloquea, porque `cap_14` no entra en esta vuelta por el techo de candidatos.

### Q.4.b. LA FRONTERA DE `cap_12`, PUBLICADA ANTES DE CORTAR

Salida de `python .t1_v23/frontera_cap12.py`, guardada en `.t1_v23/salida_frontera_cap12.txt`:

    tramos que dan nodo                    : 4
    tramos de resto                        : 8
    lineas con contenido de L8 en adelante : 29
    lineas NO cubiertas                    : 0  []
    SOLAPES                                : 0  []
    suma de las filas                      : 2118 palabras
    cuerpo medido aparte (sed 8,$ | wc -w) : 2118 palabras
    IGUALES                                : True

**LA TABLA, PEGADA DEL MISMO FICHERO Y NO TECLEADA** (`D.41`):

| tramo | palabras | nodos | que es | la salida, pegada |
|---|---:|---:|---|---|
| `L13` | 103 | **1** | pieza 1, tramo a: el plan se anuncia y su pregunta, el orden de operaciones | `13:Now it's time to start putting the suggestions in this book into practice.` |
| `L15` | 3 | **0** | pieza 1, tramo b: el rotulo de la primera etapa, que la cabeza nombra | `15:SHARE YOUR STORIES` |
| `L17` | 116 | **1** | pieza 2: contar tus propias historias para explicar la idea | `17:EXPLAIN RADICAL CANDOR to your team so they understand what you're up to. ` |
| `L19 a L49` | 1200 | **0** | pieza 1, tramo c: las etapas del plan, una a una y en su orden | `19:PROVE YOU CAN TAKE IT BEFORE YOU START DISHING IT OUT` |
| | **1422** | **2** | **los tramos que dan nodo** | |

| tramo de resto | palabras | nodos | que es, nombrado |
|---|---:|---:|---|
| `L9 a L11` | 47 | **0** | el rotulo y la felicitacion de apertura: no hay nada que ejecutar |
| `L14` | 0 | **0** | linea en blanco entre L13 y L15 |
| `L16` | 0 | **0** | linea en blanco entre L15 y L17 |
| `L18` | 0 | **0** | linea en blanco entre L17 y L19 |
| `L50` | 0 | **0** | linea en blanco entre L49 y L51 |
| `L51 a L53` | 165 | **0** | EL REPARTO DE LA SEMANA DEL JEFE: ya extraido de cap_03 en repartir_semana_cuarenta_horas_jefe, leido contra el y declarado REPITE |
| `L55` | 76 | **0** | remite a la comunidad y a las preguntas de seguimiento: promocion |
| `L57 a L65` | 408 | **0** | el cierre exhortativo del libro: postura, no procedimiento |
| | **696** | **0** | |

| # | id | pasos |
|---:|---|---:|
| 1 | `desplegar_plan_orden_operaciones_franqueza_radical` | **42** |
| 2 | `contar_historias_propias_explicar_franqueza_radical` | **8** |
| | **2 candidatos** | **50** |

> ### **EL CAPITULO MAS DIFICIL DE CORTAR DE TODO EL LOTE, Y DIGO POR QUE**
>
> **`cap_12` es un indice de si mismo: casi todas sus etapas remiten a otro capitulo** (*Review
> "Career Conversations" in Chapter Seven*, *See "Staff Meetings" in chapter eight*). Y
> `EXTRACTOR.md` 9 es literal: **nombrar el procedimiento de otro no es procedimentar.**
>
> **LO QUE DECIDE QUE SI ES NODO ES `D.27`, Y LO DECIDE POR UNA SOLA COSA: EL ORDEN.** El libro no
> pone aqui un mandato con un adjetivo de adecuacion: pone **su propio inventario de ETAPAS EN SU
> ORDEN**, nombradas una a una de `L15` a `L49`, con lo que va en paralelo (`L29`), donde hay que
> pararse (`L33`) y **las tres condiciones que hay que cumplir para seguir**. **Ese orden no lo tiene
> ninguno de los nodos a los que remite**, y recorrerlo deja fichero: dice que etapa toca.
>
> **Y LOS PASOS NO COPIAN EL PROCEDIMIENTO AJENO: LO NOMBRAN.** Es la linea entera del corte.
>
> **`L51` NO DA NODO Y SE DICE CON SU DONANTE DELANTE:** el reparto de la semana ya esta extraido de
> `cap_03` en `repartir_semana_cuarenta_horas_jefe` (diez horas, quince y quince). Lo unico que
> `L51` anade es que cinco de esas diez son reuniones a solas que ya tenias. **`P.19` manda fundir,
> no fabricar el gemelo de su propio donante.** El par va en `Q.6` con su veredicto.

### Q.4.c. LA FRONTERA DE `cap_13`, PUBLICADA ANTES DE CORTAR

Salida de `python .t1_v23/frontera_cap13.py`, guardada en `.t1_v23/salida_frontera_cap13.txt`:

    tramos que dan nodo                    : 19
    tramos de resto                        : 7
    lineas con contenido de L8 en adelante : 170
    lineas NO cubiertas                    : 0  []
    SOLAPES                                : 0  []
    suma de las filas                      : 9298 palabras
    cuerpo medido aparte (sed 8,$ | wc -w) : 9298 palabras
    IGUALES                                : True

**LA TABLA, PEGADA DEL MISMO FICHERO Y NO TECLEADA** (`D.41`):

| tramo | palabras | nodos | que es | la salida, pegada |
|---|---:|---:|---|---|
| `L17 a L22` | 69 | **1** | pieza 1, tramo a: el rotulo YOU, el de las dos practicas y el aviso del cap. 5 | `17:YOU` |
| `L35 a L40` | 238 | **0** | pieza 1, tramo b: las dos consciencias definidas y las dos practicas con su cuenta | `35:Much is written about self-awareness-the ability to recognize your own` |
| `L41 a L58` | 687 | **1** | pieza 2: la practica de las cuatro historias propias | `41:Practice: What's your story?` |
| `L59 a L72` | 510 | **1** | pieza 3: la practica del triangulo de la critica | `59:Practice: The Feedback Triangle` |
| `L73 a L86` | 35 | **1** | pieza 4, tramo a: el orden de operaciones numerado de cinco pasos | `73:SOLICIT CRITICISM FIRST` |
| `L105 a L110` | 373 | **0** | pieza 4, tramo b: por que pedir critica va primero, con la seguridad psicologica | `105:IN ADDITION TO a story, we thought we'd offer you some research on why` |
| `L111 a L112` | 153 | **1** | pieza 10, tramo a: el habito regular, porque verlo una vez no basta | `111:Seeing the boss solicit feedback once isn't enough. Fear of offending ` |
| `L113 a L114` | 49 | **0** | pieza 4, tramo c: el anuncio de los cuatro elementos de pedir critica | `113:We hope a story and some research better explain why you should prove ` |
| `L115 a L120` | 155 | **1** | pieza 5, tramo a: la pregunta recurrente y por que no vale la de si o no | `115:A GO-TO QUESTION YOU CAN ACTUALLY IMAGINE ASKING` |
| `L129 a L166` | 646 | **0** | pieza 5, tramo b: los cuatro atributos, las nueve preguntas de ejemplo y su practica | `129:Here are some attributes of good go-to questions:` |
| `L167 a L186` | 501 | **1** | pieza 6: las cuatro dudas frecuentes de pedir critica, con su respuesta | `167:FAQ` |
| `L187 a L198` | 272 | **1** | pieza 7: abrazar la incomodidad, con la practica de contar hasta seis | `187:EMBRACE THE DISCOMFORT` |
| `L199 a L214` | 282 | **1** | pieza 8: escuchar para entender, con la practica de escuchar tres minutos | `199:LISTEN WITH THE INTENT TO UNDERSTAND, NOT TO REPLY` |
| `L215 a L234` | 590 | **1** | pieza 9: hacer tangible la escucha y premiar la franqueza, con sus dos practicas | `215:MAKE LISTENING TANGIBLE: REWARD THE CANDOR` |
| `L235 a L246` | 249 | **0** | pieza 10, tramo b: meterlo en la rutina que ya tienes, con su practica | `235:BUILD IT INTO YOUR EXISTING SCHEDULE` |
| `L247 a L252` | 125 | **1** | pieza 11, tramo a: el elogio es el acelerador y la critica el freno | `247:PRAISE: FOCUS ON THE GOOD STUFF. REALLY.` |
| `L267 a L288` | 691 | **0** | pieza 11, tramo b: la disciplina del elogio, su concrecion y su practica | `267:SOMETIMES PEOPLE ARE reluctant to praise others because it's much easi` |
| `L289 a L318` | 1164 | **1** | pieza 12, tramo a: medir la critica en el oido del otro, con el marco de brujula | `289:GAUGE CRITICISM` |
| `L319 a L322` | 355 | **0** | pieza 12, tramo b: no ir a las consecuencias antes de tiempo, y los varios ejemplares | `319:ONE MISTAKE THAT people often make is to draw attention to consequence` |
| | **7144** | **12** | **los tramos que dan nodo** | |

| tramo de resto | palabras | nodos | que es, nombrado |
|---|---:|---:|---|
| `L9 a L16` | 92 | **0** | los dos rotulos, los tres autores y por que existe este epilogo |
| `L23 a L34` | 121 | **0** | EL CASO DEL CAPITALISTA DE RIESGO Y SU ASOCIADO entero: manual 3.5, la doctrina que deja (la humildad y las dos consciencias) vive en L35 y L37 |
| `L87 a L104` | 347 | **0** | LA HISTORIA DE KIM Y SU HIJA entera, con el aviso de por que la escribe: manual 3.5, es el ejemplar de pedir critica y no doctrina nueva |
| `L121 a L128` | 334 | **0** | LA HISTORIA DE JASON Y ANN entera: manual 3.5, su doctrina es la pregunta recurrente, que ya viaja en la pieza 5 |
| `L253 a L266` | 487 | **0** | LA HISTORIA DE JASON Y DAVE entera: manual 3.5, es el ejemplar de dar elogio despues de meter la pata |
| `L323 a L332` | 382 | **0** | DIVERSIDAD E INCLUSION: la cita de Claudia Rankine, el caso de las cenas de ensayo de una participante y el taller que los autores montaron con Second City. NO hay procedimiento para el lector: el libro cuenta lo que ELLOS hicieron. Va marcado como discutible |
| `L333 a L347` | 391 | **0** | QUE VIENE AHORA: la hoja de ruta de sus programas, la cita de Mill, la peticion de critica, el contacto y la cabecera del capitulo siguiente |
| | **2154** | **0** | |

| # | id | pasos |
|---:|---|---:|
| 1 | `mejorar_consciencia_propia_relacional_dos_practicas` | **13** |
| 2 | `contar_cuatro_historias_propias_ver_hueco_intencion` | **17** |
| 3 | `practicar_triangulo_critica_tres_papeles` | **15** |
| 4 | `pedir_critica_primero_crear_seguridad_psicologica` | **17** |
| 5 | `elegir_pregunta_recurrente_pedir_critica` | **24** |
| 6 | `resolver_dudas_frecuentes_pedir_critica` | **15** |
| 7 | `abrazar_incomodidad_silencio_contar_seis` | **12** |
| 8 | `escuchar_entender_critica_dominar_defensa` | **13** |
| 9 | `premiar_franqueza_hacer_escucha_tangible` | **20** |
| 10 | `integrar_peticion_critica_rutina_existente` | **13** |
| 11 | `dar_elogio_disciplina_igual_critica` | **20** |
| 12 | `medir_critica_respuesta_oyente_brujula` | **33** |
| | **12 candidatos** | **212** |

> ### **LOS DOS CORTES DE `cap_13` QUE NO SON OBVIOS, DICHOS ANTES DE QUE NADIE PREGUNTE**
>
> **UNO, LA PIEZA 10 SE LLEVA `L111`, QUE ESTA A CIENTO VEINTICUATRO LINEAS DE SU OTRO TRAMO Y
> DENTRO DE OTRA SECCION.** No es un descuido: `L111` (*meter la peticion de critica al final de la
> reunion a solas para que se vuelva rutina*) y `L239` **son el mismo objeto**, y `P.19` manda
> fundir el objeto repetido dentro del propio material en un solo procedimiento **en vez de mandarlo
> a nodo propio y fabricar el gemelo de su propio donante**. **La frontera lo declara como tramo no
> contiguo y lo publica antes de cortar**, que es `EXTRACTOR.md` 10.
>
> **DOS, CINCO TRAMOS DE CASO SE QUEDAN FUERA Y SUMAN `1.671` PALABRAS**, que es el 18 por ciento
> del capitulo. Son manual 3.5 puro: el capitalista de riesgo, la hija de Kim, Jason y Ann, Jason y
> Dave, y el taller de diversidad. **La senial barata de manual 3.5 sale limpia en las doce piezas:
> ningun `entregable_esperado` lleva un dato de un caso.**

### Q.4.d. **EL TECHO DE CANDIDATOS CIERRA LA VUELTA AQUI, Y LO DECLARO CON SU CIFRA**

*`EXTRACTOR.md` 12.4, la regla de precedencia del 12 sep 2026: el techo de candidatos por vuelta
manda sobre el de capitulos.*

| | |
|---|---|
| **techo de candidatos por vuelta** | **15** (`EXTRACTOR.md` 12.4: entre cinco y quince) |
| **candidatos de `cap_12`** | **2** |
| **candidatos de `cap_13`** | **12** |
| **suma de la vuelta** | **14** |
| **hueco que queda bajo 15** | **1** |
| **`cap_14`** | **NO ENTRA.** Su frontera no esta ni abierta, y cortarla daria muy por encima de un candidato |

> # **LA VUELTA CIERRA EN `cap_13` CON 14 CANDIDATOS, POR DEBAJO DEL TECHO DE 15, Y `cap_14` PASA A LA VUELTA SIGUIENTE.**
>
> **Y NO ME ESCONDO DETRAS DE LA REGLA: DIGO LA CUENTA QUE HICE.** `cap_14` tiene **7.638** palabras,
> que es cuatro veces `cap_12`, y `cap_12` con **2.118** dio dos piezas solo porque es un indice.
> **Un capitulo de contenido de ese tamanio no cabe en el hueco de uno.** `EXTRACTOR.md` 12.4 es
> ademas literal en que **no se reparte un capitulo en dos vueltas**, asi que la salida no es
> empezarlo: es declararlo.
>
> **LO QUE ESTO CUESTA, Y LO DIGO ENTERO PORQUE ES LO QUE MAS DUELE DE ESTA VUELTA:** el lote 4
> **NO cierra**, asi que `D.39` **no inserta**, y **las 37 aristas y los 12 veredictos sin sede
> siguen esperando**. Es la sexta vuelta con la puerta abierta y cero entradas. **El encargo lo
> anticipa por su nombre** (*es probable que la vuelta cierre ahi... eso no es incumplir el encargo,
> es la regla de precedencia funcionando*), y la TAREA 4 se declara sin hacerse en `Q.5`.
>
> **Y LA DIFERENCIA CON LA VUELTA 22 ES DE UN SOLO CAPITULO:** entonces faltaban tres, ahora falta
> **uno**.
