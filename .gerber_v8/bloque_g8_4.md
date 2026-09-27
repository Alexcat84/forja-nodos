
## G8.4. TAREA 4: `cap_22`, el `Afterword`, Y EL LOTE QUE CIERRA

### G8.4.a. El borde de arriba, comparado contra `wc -l`

    $ wc -l fuentes/gerber_emyth/cap_22.md
    129 fuentes/gerber_emyth/cap_22.md

**`129` LINEAS, AL DIGITO CON LAS `129` QUE EL ENCARGO CUENTA EN SU CABECERA.**

### G8.4.b. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_22.md .gerber_v8/piezas_cap22.txt`,
guardada en `.gerber_v8/frontera_cap22.txt`:

<!-- TALLADO: salida=.gerber_v8/frontera_cap22.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_22.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L129.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L12 | **5** | el rotulo AFTERWORD y el titulo TAKING THE FIRST STEP | **RESIDUO: rotulo** |
| `Ra` | L13 a L18 | **54** | la pregunta de cierre (que haces ahora que el fuego esta encendido) y la afirmacion de que, como Sarah, el lector debe dar el primer paso | **POSTURA: bridge** |
| `Rb` | L19 a L26 | **125** | debes dar un paso atras y mirar tu negocio con tus nuevos ojos E-Myth; debes analizar tu negocio como es hoy, decidir como debe verse cuando este terminado, y determinar la brecha entre donde estas y donde necesitas estar; esa brecha te dira que hace falta hacer, y la brecha siempre nace de la ausencia de sistemas | **DISCUTIBLE: llamado de cierre sin inventario propio de que analizar** |
| `Rc` | L27 a L32 | **125** | desde 1986 E-Myth Worldwide ha ayudado a miles de duenos a dar ese primer paso, invita al lector a la experiencia gratuita E-Myth, y pide completar el formulario al final del libro y seguir las instrucciones provistas alli | **POSTURA: invitacion comercial, remite a un formulario fuera del libro** |
| `Rd` | L33 a L42 | **32** | recuerda el proverbio chino (oir se olvida, ver se recuerda, hacer se entiende) y cierra con Let's get started | **POSTURA: proverbio de cierre** |
| `R3` | L43 a L50 | **10** | la firma: Michael E. Gerber, E-Myth Worldwide, Santa Rosa California, junio 2001 | **RESIDUO: firma** |
| `R4` | L51 a L60 | **225** | ABOUT THE AUTHOR: biografia del autor, su rol en E-Myth Worldwide, y los datos de contacto para invitarlo a hablar o recibir informacion del E-Myth Mastery Program | **RESIDUO: biografia y contacto comercial del autor** |
| `R5` | L61 a L129 | **328** | OTHER WORKS, BACK AD y COPYRIGHT: el listado de otros libros de Michael Gerber con sus ISBN, el aviso legal de copyright de HarperCollins, los datos de edicion, y la publicidad de contraportada de otros titulos (E-Myth Mastery, The E-Myth Physician, The E-Myth Manager, The E-Myth Revisited) con su resena de mercadeo cada uno | **RESIDUO: back matter editorial, ISBN, copyright y publicidad de otros libros** |
| **el cuerpo entero** | **L8 a L129** | **904** | **suma de las piezas: 904** | **residuo sin asignar: 0** |

    piezas: 8   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 904   suma 904   residuo 0

**`904` PALABRAS, AL DIGITO CON LAS `904` QUE EL ENCARGO CUENTA EN SU CABECERA. `8` PIEZAS, `0` SOLAPES,
`0` LINEAS SIN CUBIERTAS, RESIDUO `0`.** Fichero completo en `.gerber_v8/piezas_cap22.txt` (D.42).

### G8.4.c. El unico discutible, marcado ANTES de saber si acierto y cerrado en el mismo acto (tope `2`, `D.61`)

**Discutible `1`: `Rb`, `cap_22` `L19` a `L25`.** Cuatro oraciones en imperativo de segunda persona en
secuencia (*step back*, *analyze*, *decide*, *determine the gap*) que podrian leerse como un
procedimiento de cuatro pasos: dar un paso atras, analizar el negocio como es hoy, decidir como debe
verse terminado, determinar la brecha. Cita, con su `sed` pegado (`D.35`), guardada en
`.gerber_v8/cita_cap22_Rb.txt`:

<!-- TALLADO: salida=.gerber_v8/cita_cap22_Rb.txt -->

    You must step back from your business and look at it through your new E-Myth eyes.
    You must analyze your business as it is today, decide what it must look like when you have finally got it just like you want it, and then determine the gap between where you are and where you need to be in order to make your dream a reality.
    That gap will tell you exactly what needs to be done to create the business of your dreams.
    And what you will discover when you look at your business through your E-Myth eyes is that the gap is always created by the absence of systems, the absence of a proprietary way of doing business that successfully differentiates your business from everyone else's.

**CERRADO, NO EJECUTADO: no escribo candidato.** Leido contra la vara madre (seccion `9`) y la prueba
del inventario (`9.1`, `D.27`): el libro NO nombra uno a uno los medios, etapas u objetos que hay que
revisar en "tu negocio como es hoy". *Look at it through your new E-Myth eyes* y *analyze your business
as it is today* son el adjetivo de adecuacion de la restriccion `2` de `9.1` disfrazado de instruccion
(no dice QUE mirar ni QUE analizar: eso ya lo desplego el libro entero en los capitulos anteriores, con
sus propios candidatos ya minados uno a uno, Primary Aim, Strategic Objective, Organizational Strategy,
People Strategy, Systems Strategy). Sin un inventario propio de este tramo, escribir pasos aqui seria
inventar el detalle que el libro no pone (`15.4`, la relectura de fidelidad): un paso como *revisa tus
Hard Systems, tus Soft Systems y tus Information Systems* no esta en estas cuatro lineas, esta en
`cap_19`, ya minado. **VEREDICTO: `SANO`, no candidato.** Es el resumen motivacional de cierre del libro
entero (la misma voz de *this call to arms is not a call to do battle, it is a call to learning*, pieza
`R2` de `cap_21`), no un procedimiento nuevo. Si el auditor lee lo contrario, la cita queda pegada arriba
para que la relectura ciega la encuentre primero.

**`D.61` REPASADA: UN DISCUTIBLE, CERRADO EN ESTA MISMA VUELTA CON SU MOTIVO Y SU LINEA. `0` ABIERTOS,
POR DEBAJO DEL TOPE DE `2`.**

### G8.4.d. Veredicto de `cap_22`: cero candidatos

`R1`, `R3`, `R4` y `R5` son rotulo, firma, biografia del autor y back matter editorial (ISBN, copyright,
publicidad de otros libros): ninguno trae procedimiento. `Ra` y `Rd` son postura de apertura y cierre
retorico. `Rc` es una invitacion comercial que remite a "el formulario al final de este libro", fuera del
propio texto (el corolario de `9.1`: un paso que cierra un bucle que el libro deja abierto es PUENTE, y
aqui ni siquiera hay paso que escribir, es una remision completa a un formulario ajeno al fichero).
`Rb`, el unico tramo con forma de procedimiento, se cierra `SANO` en `G8.4.c`.

**VEREDICTO: `cap_22` SE REGISTRA MINADO CON CERO CANDIDATOS.** Es el Afterword del libro (llamado a la
accion y remision al formulario de inscripcion) seguido de la biografia del autor y el back matter
editorial completo: ninguna pieza trae inventario propio. **Cero candidatos con su razon escrita.**

### G8.4.e. El estado del lote `9`, declarado con su medida, sin decidir nada

Contado contra `fuentes/gerber_emyth/`:

    $ ls fuentes/gerber_emyth/*.md | wc -l
    22

**`22` UNIDADES EN LA BANDEJA DE ENTRADA.** De ellas, `cap_01` a `cap_03` siguen en `d094` por decision
del fundador y NO se tocan; `cap_04` a `cap_19` ya estaban minados antes de esta vuelta (`16` capitulos,
`ACTA G7` y actas anteriores); `cap_20`, `cap_21` y `cap_22` quedan minados en esta misma vuelta (`G8.2`,
`G8.3`, `G8.4.d`). **QUEDAN `3` UNIDADES DEL LOTE `9` SIN MINAR: `cap_01`, `cap_02` y `cap_03`, LAS TRES
EN `d094`.**

**LOS TRES CAPITULOS DE ESTA VUELTA CUPIERON EN EL TRAMO** (`cap_20` + `cap_21` + `cap_22` = `0`
candidatos, muy por debajo del techo de `30`), **ASI QUE EL LOTE `9` QUEDA MINADO ENTERO SALVO `d094`.**
**ESTO SE DECLARA, NO SE EJECUTA:** la insercion es serial y de ningun frente (`D.45`), y la cosecha del
lote es del fundador. No inserto, no cierro el lote yo: dejo la medida para quien lea este reporte.
