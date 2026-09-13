
---

## P.4. TAREA 3: **`cap_11` ENTERO**. **CERRADA**, Y CIERRA LA VUELTA: `cap_12` NO ENTRA

### P.4.a. EL CUERPO, REMEDIDO POR MI COMO EL ENCARGO MANDA

    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_11.md | wc -w
      8626
    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_12.md | wc -w
      2118
    $ sed -n '1,6p' fuentes/scott_radical_candor/cap_11.md
      unidad: Cap. 8
      titulo_textual: Results

**LAS DOS CIFRAS DEL ENCARGO REPRODUCEN AL DIGITO: `8.626` y `2.118`.**

| | proyeccion por densidad | **cuenta real** |
|---|---:|---:|
| `cap_11` | **~13,5** (`8.626 / 641`, con `641 = 8.976 / 14` medido en `cap_10`) | # **16** |
| error de la proyeccion | | **`+2,5` piezas, el 18,5 por ciento por debajo** |

> ### **LA PROYECCION POR DENSIDAD VUELVE A QUEDARSE CORTA, Y ES LA SEGUNDA VEZ SEGUIDA.** En `cap_10` predijo `10,3` y fueron `14`; aqui predijo `13,5` y son `16`. **Publico las dos como manda el encargo, y digo lo que veo: se queda corta en el mismo sentido las dos veces.** No propongo cambiarla, porque el propio encargo la manda usar **como orden de magnitud** y no como cuenta. La cuenta la da la frontera.

### P.4.b. LA FRONTERA, PUBLICADA ANTES DE CORTAR Y CERRADA CONTRA EL CUERPO

*Salida de `python .t1_v22/frontera_cap11.py`, guardada en `.t1_v22/salida_frontera_cap11.txt`.
`ACTA 18` `7.5` orden 1: si no cierra, no se publica ninguna cuenta de nodos.*

    tramos que dan nodo (contando los dos partidos): 18
    tramos de resto                        : 1
    lineas con contenido de L8 en adelante : 163
    lineas NO cubiertas                    : 0  []
    SOLAPES                                : 0  []
    suma de las filas                      : 8626 palabras
    cuerpo medido aparte (sed 8,$ | wc -w) : 8626 palabras
    IGUALES                                : True

    NODOS QUE LA FRONTERA DA               : 16
    TECHO DE 12.4                          : 15
    palabras de resto                      : 281  (3.3 por ciento del cuerpo)

| tramo | palabras | nodos | que es | la salida, pegada |
|---|---:|---:|---|---|
| `L15 a L35` | 88 | **1** | P1 la cabeza: quien se comunica con quien y las herramientas nombradas | `15:One of your most important responsibilities to keep everything moving smooth` |
| `L37 a L65` | 1198 | **1** | P2 el 1:1: mentalidad, frecuencia, presentarse y la agenda del reportado | `37:1:1 CONVERSATIONS` |
| `L67 a L97` | 231 | **1** | P3 las preguntas de seguimiento que buscan los huecos | `67:Some good follow-up questions` |
| `L99 a L113` | 220 | **1** | P4 nutrir en el 1:1 las ideas nuevas, que son fragiles | `99:Encourage new ideas in the 1:1.` |
| `L115 a L127` | 208 | **1** | P5 las seniales del 1:1 de que estas fallando como jefe | `115:Signs you'll get from 1:1s that you're failing as a boss` |
| `L129 a L145` | 391 | **1** | P6a la reunion de equipo y su agenda de tres bloques | `129:STAFF MEETINGS` |
| `L147 a L157` | 524 | **1** | P7 los apuntes de sala de estudio | `147:Listen: put updates in a shared document during a "study hall" (15 minutes)` |
| `L159 a L163` | 249 | **0** | P6b el bloque de aclarar de esa misma agenda | `159:Clarify: identify key decisions/debates (30 minutes). What are the one or tw` |
| `L165 a L173` | 313 | **1** | P8 el tiempo para pensar, bloqueado y sagrado | `165:THINK TIME` |
| `L175 a L193` | 501 | **1** | P9 la reunion de gran debate | `175:"BIG DEBATE" MEETINGS` |
| `L195 a L203` | 302 | **1** | P10 la reunion de gran decision | `195:"BIG DECISION" MEETINGS` |
| `L205 a L221` | 446 | **1** | P11 la reunion general | `205:ALL-HANDS MEETINGS` |
| `L223 a L233` | 269 | **1** | P12 pelear la proliferacion con tiempo de ejecutar | `223:EXECUTION TIME` |
| `L235 a L249` | 757 | **1** | P13 el tablero kanban | `235:KANBAN BOARDS` |
| `L251 a L269` | 506 | **1** | P14 pasear por la organizacion | `251:WALK AROUND` |
| `L271 a L299` | 626 | **1** | P15a la rueda recorrida sobre tu propia cultura | `271:BE CONSCIOUS OF CULTURE` |
| `L301 a L305` | 211 | **1** | P16 debatir y decidir lo que te tienta delegar a recursos humanos | `301:Debate and decide explicitly. Don't let things that pervert your culture "ju` |
| `L307 a L333` | 305 | **0** | P15b persuadir, ejecutar, aprender y escuchar, de esa misma rueda | `307:Persuade. Pay attention to the small things` |
| | **8345** | **16** | **los tramos que dan nodo** | |

**LA FILA DE RESIDUO, NOMBRADA LINEA A LINEA** (`ACTA 19` `7.4` ORDEN A). **Es UNA fila, de
`281` palabras, el `3,3` por ciento del cuerpo, y dice que hay en cada una de sus cinco lineas:**

| tramo de resto | palabras | nodos | que es, nombrado linea a linea |
|---|---:|---:|---|
| `L9 a L13` | 281 | **0** | `L9` el subtitulo; `L11` la meta de la franqueza radical y el estado del equipo que la tiene; `L13` las protesis mentales de Kosslyn, **la rueda de hacer cosas (que YA esta extraida de `cap_07` en `recorrer_rueda_hacer_cosas_equipo`, 12 pasos)** y el formador de New Jersey Transit (*no empieces mandando; empieza escuchandoles*, **que ya vive en `crear_cultura_escucha_equipo`**) |

> **LAS DOS PIEZAS QUE PODRIAN ESCONDERSE EN ESE RESTO LAS NOMBRO Y DIGO DONDE VIVEN YA, que es
> justo lo que la `ORDEN A` obliga a hacer y lo que cazo la pieza 14 de `cap_10`.** Ninguna de las
> dos es doctrina nueva de `cap_11`: las dos son remites a `cap_07`, y `EXTRACTOR.md` 9 llama a eso
> **nombrar el procedimiento de otro**, que no da nodo.

**DOS TRAMOS SON NO CONTIGUOS Y LO DIGO ANTES DE QUE SE NOTE:** la pieza **P6** vive en
`L129 a L145` **mas** `L159 a L163`, con los apuntes de sala de estudio (`L147 a L157`) en medio
como pieza propia; y la pieza **P15** vive en `L271 a L299` **mas** `L307 a L333`, con el rotulo de
debatir y decidir (`L301 a L305`) en medio como pieza propia. **Las dos particiones estan escritas
en el `resumen_teorico` de sus ficheros**, para que la frontera se pueda comprobar sin este reporte
delante.

### P.4.c. **`cap_11` PASA EL TECHO, ASI QUE LA VUELTA CIERRA AQUI Y LO DECLARO CON SU CIFRA** (`EXTRACTOR.md` 12.4)

**LA REGLA DE PRECEDENCIA, LITERAL:** *SI UN SOLO CAPITULO PASA DEL TECHO DE CANDIDATOS, LA VUELTA
CIERRA EN ESE CAPITULO Y LO DECLARA. No se reparte el capitulo en dos vueltas ni se estira el tramo
para completar el numero de capitulos del lote.*

> # **LA VUELTA CIERRA EN `cap_11` CON `16` CANDIDATOS, POR ENCIMA DEL TECHO DE `15`. `cap_12` NO ENTRA, Y LOS CAPITULOS RESTANTES DEL TRAMO (`cap_12`, `cap_13` Y `cap_14`) PASAN A LA VUELTA SIGUIENTE.**

**Y LA CUENTA DE `cap_12` LA DOY IGUAL, porque el encargo pide declararlo con su cifra EN LOS DOS
CASOS:** `cap_12` (`Getting Started`) mide **2.118 palabras** y proyecta **~3,3** piezas a la
densidad de `cap_10`. **Hueco bajo 15: cero.** `16 + 3 = 19`, muy por encima. **No se mina.**

> **Y EL AVISO QUE ME DEBO A MI MISMO:** `16` no es un numero al que yo apuntara. La frontera dio
> `16` y la publique antes de escribir el primer candidato. **La pieza P16 es mi corte mas
> discutible del capitulo** y va marcada como tal en `P.8`: **si el auditor la lee como un paso de
> `P15` y no como nodo, `cap_11` cierra en `15`, justo EN el techo**, y entonces la vuelta no cerro
> corta sino exacta. **Digo las dos cuentas porque no quiero que la que me conviene sea la unica
> escrita.**

### P.4.d. LOS DIECISEIS CANDIDATOS, Y CADA UNO POR LA ADUANA EN EL ACTO EN QUE SE ESCRIBIO (`EXTRACTOR.md` 16)

**COMO SE CUMPLIO LA REGLA DE LOS CUATRO PASOS, y lo digo porque es donde se podria hacer trampa:**
los candidatos se escribieron **en cuatro lotes de cuatro**, y **el informe de cada lote se lanzo
antes de escribir el siguiente**. **Ningun lote se escribio con el anterior sin pasar por la
aduana.** Lo que `EXTRACTOR.md` 16 prohibe por su nombre (*escribir doce candidatos y pasar la
aduana al final*) no ocurrio, y el orden esta en las horas de los ficheros de `.aduana_v22/`.

**Y ADEMAS SE VE EN UNA CIFRA DE LOS PROPIOS INFORMES, que es la prueba mas barata: LA POBLACION
CRECE LOTE A LOTE.** `304` en el lote A, `308` en el B, `312` en el C, `316` en el D. **Es
`EXTRACTOR.md` 12.3 midiendose a si mismo:** *el primero que entra cambia lo que el segundo mide*.
Aqui ni siquiera entro nadie, y aun asi **cada lote escrito cambio la poblacion que midio el
siguiente**.

*Salida de `python .t1_v22/salida_saldo_cap11.txt`, impresa de los dieciseis ficheros de
`.aduana_v22/`.*

EOF_TABLA_SALDO

### P.4.e. LAS LECTURAS DE LOS VECINOS QUE LA ADUANA LEVANTO, **UNA A UNA Y CON SU RAZON ESCRITA** (`EXTRACTOR.md` 2)

*Las señales ordenan, nunca deciden (manual principio 4). Leo a los vecinos antes de escribir el
veredicto, y el veredicto lleva su razon. **Hoy su sede es solo `REPORTE.md` porque no hay
insercion** (`P.0.1`); `bitacora/VEREDICTOS.jsonl` lo sera el dia del cierre del lote.*

EOF_TABLA_VEREDICTOS

### P.4.f. **LOS TRES HECHOS QUE ESTAS DIECISEIS LECTURAS AÑADEN SOBRE LAS SEÑALES, Y LOS TRES SON MEDIDOS**

> ### **HECHO 3: LA SEÑAL 3 LEVANTO UN PAR CON `0,911` QUE ES LA MISMA FRASE Y NI UN PROCEDIMIENTO COMPARTIDO. ES EL EJEMPLAR MAS LIMPIO QUE ESTA CASA TIENE DE QUE LA SEÑAL 3 MIDE REDACCION.**
>
> `bloquear_tiempo_pensar_calendario` paso 6 dice **`Y anima a todos los de tu equipo a hacer lo
> mismo`**; `calibrar_ascensos_evitar_politica` paso 14 dice **`Y anima a todo tu equipo a hacer lo
> mismo`**. **`paso_contra_nodo 0,911` contra un umbral de `0,60`.** Uno bloquea calendario para
> pensar; el otro calibra ascensos entre iguales antes de aprobarlos. **Cero actos compartidos, dos
> entregables sin interseccion.** `EXTRACTOR.md` 11 dice que *paso contra nodo cerca de 1,0* suele
> significar que **el material ya vive en el grafo**; aqui `0,911` significa que **la coletilla ya
> vive en el grafo**, que no es lo mismo. **No propongo mover nada** (`EXTRACTOR.md` 11: ninguna
> vuelta mueve un umbral): dejo el ejemplar medido.

> ### **HECHO 4: LA SEÑAL SI LEVANTO, ELLA SOLA, LAS DOS ARISTAS QUE YO YA HABIA DECLARADO POR LECTURA. LO DIGO PORQUE VA CONTRA MI PROPIA EXPECTATIVA.**
>
> Escribi `nutrir_ideas_nuevas_reunion_solas` **declarando en su `resumen_teorico`** que su madre es
> `crear_espacio_seguro_madurar_ideas_nuevas`, y escribi `montar_reunion_gran_decision` declarando
> que continua a `montar_reunion_gran_debate`. **Las dos las levanto despues la aduana sola**
> (`paso_contra_nodo 0,650` la primera; `familia_id 0,600` y `paso_contra_nodo 0,726` la segunda).
> **`D.19` midio que la señal 3 levanta el 3 por ciento de las aristas declaradas**, y en esta
> tanda levanta 2 de las 3 que declare por lectura, mas 1 de las 3 `D.37` de `P.3`. **Tres vueltas
> de esta casa dicen que la señal no ve las aristas; esta vuelta dice que a veces si.** Traigo la
> medida, no una propuesta: **una tanda de dieciseis no mueve una calibracion de 3.169**.

> ### **HECHO 5: UN PAR CRUZA DE LIBRO, Y ES EL QUE MAS CARO COSTARIA FALLAR.**
> `montar_reunion_gran_decision` (Scott) contra **`dirigir_reunion_decision`, que VIVE EN EL GRAFO y
> es de Zhuo**. Es el unico vecino de toda la tanda que ya esta dentro, asi que es el unico donde un
> `SANO` mal puesto mete un gemelo de verdad. **Lo lei entero, los 14 pasos contra mis 14**, y la
> razon va en la tabla de `P.4.e` con los dos actos compartidos nombrados por su numero.
