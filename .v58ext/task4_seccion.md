## XX.4. TAREA 4. LA FIDELIDAD, POR MUESTRA Y CON SU SEMILLA `v58`

**La semilla de esta vuelta es `v58`, la que el encargo fijo.** La reparte el instrumento, no yo:

<!-- TALLADO: salida=.v58ext/muestra_fidelidad.txt -->

    $ python scripts/muestra_fidelidad.py --libro grove_high_output \
             --capitulos cap_14,cap_15,cap_16 --semilla v58

    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : grove_high_output
      semilla  : v58
      capitulos: cap_14, cap_15, cap_16

      RELEIDO ENTERO : cap_16
      POR MUESTRA    : cap_14, cap_15, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_14: 15 paso(s) en la muestra
        entregar_evaluacion_desempeno_tres_claves      P1   Se totalmente franco con el subordinado al entregarle la rev
        entregar_evaluacion_desempeno_tres_claves      P2   Recuerda que el objetivo de la comunicacion es hacer llegar 
        entregar_evaluacion_desempeno_tres_claves      P3   Observa al subordinado mientras hablas y sigue insistiendo h
        entregar_evaluacion_desempeno_tres_claves      P4   Emplea toda tu capacidad sensorial, no solo el oido, para co
        entregar_evaluacion_desempeno_tres_claves      P5   Deja fuera tus propias inseguridades, ansiedades o culpa: la
        entregar_evaluacion_desempeno_tres_claves      P6   Controla esas emociones propias para que no afecten tu tarea
        guiar_subordinado_etapas_resistencia_desempeno P1   Reconoce en que etapa esta el subordinado frente al problema
        guiar_subordinado_etapas_resistencia_desempeno P2   Si el subordinado ignora el problema, aportale hechos y ejem
        guiar_subordinado_etapas_resistencia_desempeno P5   Lleva la cuenta de en que etapa esta el subordinado en cada 
        guiar_subordinado_etapas_resistencia_desempeno P6   Si el subordinado no logra avanzar mas alla de culpar a otro
        preparar_resena_mixta_hoja_trabajo             P1   Reune tantos aspectos del desempeno del subordinado como pue
        preparar_resena_mixta_hoja_trabajo             P2   Sientate con una hoja en blanco y, sin editar en tu cabeza, 
        preparar_resena_mixta_hoja_trabajo             P3   Cuando hayas agotado los items, guarda toda la documentacion
        preparar_resena_mixta_hoja_trabajo             P4   Busca relaciones entre los distintos items anotados en la ho
        preparar_resena_mixta_hoja_trabajo             P6   Preguntate si el subordinado sera capaz de recordar todos lo

      --- cap_15: 15 paso(s) en la muestra
        gestionar_retencion_subordinado_valioso_renunc P2   Persigue con energia cada via disponible para retener al sub
        gestionar_retencion_subordinado_valioso_renunc P3   Si la transferencia parece la salida mas probable, asume tu 
        gestionar_retencion_subordinado_valioso_renunc P5   Ayudalo a sentirse comodo con el nuevo arreglo, dejando clar
        gestionar_retencion_subordinado_valioso_renunc P6   Si el subordinado dice que ya acepto un puesto en otra empre
        responder_primer_aviso_renuncia_subordinado    P1   Deja lo que estas haciendo en cuanto el subordinado te avisa
        responder_primer_aviso_renuncia_subordinado    P2   Sientalo y preguntale por que se va.
        responder_primer_aviso_renuncia_subordinado    P5   No discutas, no sermonees y no entres en panico durante esta
        usar_banco_nueve_preguntas_entrevista          P2   Preguntale cuales son sus debilidades y que esta haciendo pa
        usar_banco_nueve_preguntas_entrevista          P3   Preguntale que te convenceria de que tu empresa deberia cont
        usar_banco_nueve_preguntas_entrevista          P4   Preguntale que problemas esta encontrando en su puesto actua
        usar_banco_nueve_preguntas_entrevista          P5   Preguntale por que cree que esta listo para este nuevo puest
        usar_banco_nueve_preguntas_entrevista          P6   Preguntale cuales considera sus logros mas importantes y por
        usar_banco_nueve_preguntas_entrevista          P7   Preguntale cuales considera sus fracasos mas importantes y q
        usar_banco_nueve_preguntas_entrevista          P8   Si el puesto lo justifica, preguntale por que cree que deber
        usar_banco_nueve_preguntas_entrevista          P9   Preguntale cual fue el curso o proyecto mas importante que c

      --- cap_16: ENTERO, 4 paso(s), no hay muestra que elegir

**La semilla reparte `cap_16` para releer ENTERO** (solo tiene un candidato, `4` pasos) **y
`cap_14` y `cap_15` por muestra de `15` pasos cada uno.** No lo elijo yo.

### XX.4.1. LA RELECTURA CONTRA EL LIBRO, PASO POR PASO

| candidato | paso | capitulo | linea | el texto del libro que lo sostiene | veredicto |
|---|---|---|---|---|---|
| `entregar_evaluacion_desempeno_tres_claves` | P1 | `cap_14` | `L109` | You must level with your subordinate, the credibility and integrity of the entire system depend on your being totally frank. | **TRANSCRIPCION** |
| `entregar_evaluacion_desempeno_tres_claves` | P2 | `cap_14` | `L111` | The aim of communication is to transmit thoughts from the brain of person A to the brain of person B. | **TRANSCRIPCION** |
| `entregar_evaluacion_desempeno_tres_claves` | P3 | `cap_14` | `L113` | you should watch the person you are talking to ... it is your responsibility to keep at it until you are satisfied that you have been hea... | **TRANSCRIPCION** |
| `entregar_evaluacion_desempeno_tres_claves` | P4 | `cap_14` | `L115` | employing your entire arsenal of sensory capabilities to make certain your points are being properly interpreted. | **TRANSCRIPCION** |
| `entregar_evaluacion_desempeno_tres_claves` | P5 | `cap_14` | `L119` | your own insecurities, anxieties, guilt, or whatever should be kept out of it. At issue are the subordinate's problems, not the superviso... | **TRANSCRIPCION** |
| `entregar_evaluacion_desempeno_tres_claves` | P6 | `cap_14` | `L119` | You should work to control these emotions so that they don't affect your task. | **TRANSCRIPCION** |
| `guiar_subordinado_etapas_resistencia_desempeno` | P1 | `cap_14` | `L167` | A poor performer has a strong tendency to ignore his problem ... denies the existence of a problem ... admits that there is a problem, bu... | **TRANSCRIPCION** |
| `guiar_subordinado_etapas_resistencia_desempeno` | P2 | `cap_14` | `L167` | a manager needs facts and examples so that he can demonstrate its reality. | **TRANSCRIPCION** |
| `guiar_subordinado_etapas_resistencia_desempeno` | P5 | `cap_14` | `L171` | The supervisor should keep track of what stage things are in. | **TRANSCRIPCION** |
| `guiar_subordinado_etapas_resistencia_desempeno` | P6 | `cap_14` | `L179` | you will have to assume the formal role of the supervisor, endowed with position power, and say, This is what I, as your boss, am instruc... | **TRANSCRIPCION** |
| `preparar_resena_mixta_hoja_trabajo` | P1 | `cap_14` | `L129` | consider as many aspects of your subordinate's performance as possible. You should scan material such as progress reports, performance ag... | **TRANSCRIPCION** |
| `preparar_resena_mixta_hoja_trabajo` | P2 | `cap_14` | `L129` | sit down with a blank piece of paper ... write everything down on the paper. Do not edit in your head. | **TRANSCRIPCION** |
| `preparar_resena_mixta_hoja_trabajo` | P3 | `cap_14` | `L129` | When you have run out of items, you can put all of your supporting documentation away. | **TRANSCRIPCION** |
| `preparar_resena_mixta_hoja_trabajo` | P4 | `cap_14` | `L131` | look for relationships between the various items listed. | **TRANSCRIPCION** |
| `preparar_resena_mixta_hoja_trabajo` | P6 | `cap_14` | `L131` | ask yourself if your subordinate will be able to remember all of the messages you have chosen to deliver. If not, you must delete the les... | **TRANSCRIPCION** |
| `gestionar_retencion_subordinado_valioso_renuncia` | P2 | `cap_15` | `L115` | You now must vigorously pursue every avenue available to you to keep him with the firm, even if it means transferring him to another depa... | **TRANSCRIPCION** |
| `gestionar_retencion_subordinado_valioso_renuncia` | P3 | `cap_15` | `L115` | If it seems that is the likely solution, you must become the project manager of that solution until the whole thing is settled. | **TRANSCRIPCION** |
| `gestionar_retencion_subordinado_valioso_renuncia` | P5 | `cap_15` | `L119` | You now have to make him feel comfortable with the new arrangement ... We are just doing what we should have done without any of this hap... | **TRANSCRIPCION** |
| `gestionar_retencion_subordinado_valioso_renuncia` | P6 | `cap_15` | `L121` | You have to make him quit again ... he's really made two commitments: first to a potential employer he only vaguely knows, and second to ... | **TRANSCRIPCION** |
| `responder_primer_aviso_renuncia_subordinado` | P1 | `cap_15` | `L111` | Drop what you are doing. | **TRANSCRIPCION** |
| `responder_primer_aviso_renuncia_subordinado` | P2 | `cap_15` | `L111` | Sit him down and ask him why he is quitting. | **TRANSCRIPCION** |
| `responder_primer_aviso_renuncia_subordinado` | P5 | `cap_15` | `L111` | Don't argue, don't lecture, and don't panic. | **TRANSCRIPCION** |
| `usar_banco_nueve_preguntas_entrevista` | P2 | `cap_15` | `L41` | What are your weaknesses? How are you working to eliminate them? | **TRANSCRIPCION** |
| `usar_banco_nueve_preguntas_entrevista` | P3 | `cap_15` | `L43` | Convince me why my company should hire you. | **TRANSCRIPCION** |
| `usar_banco_nueve_preguntas_entrevista` | P4 | `cap_15` | `L45` | What are some of the problems you are encountering in your current position? How are you going about solving them? What could you have do... | **TRANSCRIPCION** |
| `usar_banco_nueve_preguntas_entrevista` | P5 | `cap_15` | `L47` | Why do you think you're ready for this new job? | **TRANSCRIPCION** |
| `usar_banco_nueve_preguntas_entrevista` | P6 | `cap_15` | `L49` | What do you consider your most significant achievements? Why were they important to you? | **TRANSCRIPCION** |
| `usar_banco_nueve_preguntas_entrevista` | P7 | `cap_15` | `L51` | What do you consider your most significant failures? What did you learn from them? | **TRANSCRIPCION** |
| `usar_banco_nueve_preguntas_entrevista` | P8 | `cap_15` | `L53` | Why do you think an engineer should be chosen for a marketing position? (Vary this one according to the situation.) | **TRANSCRIPCION** |
| `usar_banco_nueve_preguntas_entrevista` | P9 | `cap_15` | `L55` | What was the most important course or project you completed in your college career? Why was it so important? | **TRANSCRIPCION** |
| `reciclar_empleado_ascendido_mas_alla_capacidad` | P1 | `cap_16` | `L49` | management was at fault for misjudging the employee's readiness for more responsibility ... management ought to face up to its own error ... | **TRANSCRIPCION** |
| `reciclar_empleado_ascendido_mas_alla_capacidad` | P2 | `cap_16` | `L49` | take forthright and deliberate steps to place the person into a job he can do. | **TRANSCRIPCION** |
| `reciclar_empleado_ascendido_mas_alla_capacidad` | P3 | `cap_16` | `L49` | Management should also support the employee in the face of the embarrassment that he is likely to feel. | **TRANSCRIPCION** |
| `reciclar_empleado_ascendido_mas_alla_capacidad` | P4 | `cap_16` | `L49` | If recycling is done openly, all will be pleasantly surprised how short-lived that embarrassment will be. | **TRANSCRIPCION** |

### XX.4.2. EL TALLY, CON SU DENOMINADOR AL LADO (`D.59`)

La tabla la calcula `.v58ext/formatear_tarea4.py` de la relectura fila por fila de `XX.4.1`,
no se teclea:
| capitulo | pasos revisados | PUENTE | por ciento inventado | dispara relectura entera (>10%%) |
|---|---:|---:|---:|---|
| `cap_14` | 15 de 15 | 0 | 0.0 por ciento | NO |
| `cap_15` | 15 de 15 | 0 | 0.0 por ciento | NO |
| `cap_16` | 4 de 4 | 0 | 0.0 por ciento | NO (releido ENTERO por diseno de la muestra, no por disparador) |
| **total del tramo** | **34 de 34** | **0** | **0.0 por ciento** | **NO** |

**`34` de `34` pasos revisados, `34` TRANSCRIPCION y `0` PUENTE: `0,0` por ciento inventado,**
**bien por debajo del `10` por ciento que dispara la relectura entera de un capitulo** (el
disparador de `EXTRACTOR.md` 15, modo austero). `cap_16` ya se releyo entero porque la propia
semilla lo eligio para eso, no porque haya disparado nada: su `0` de `4` esta limpio igual.