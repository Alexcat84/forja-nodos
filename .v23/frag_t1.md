
---

## Q.2. TAREA 1: LA COLA DE SIETE DEL AUDITOR. **CERRADA**

*El encargo la pone PRIMERA y sin solape. Las nueve correcciones de `PARA_ALEXIS` 5 llegan a mi
turno en siete: las dos primeras eran cifra falsa y el auditor ya las rehizo por regeneracion
(`P.9.3` de la vuelta 22), asi que **no las toco**. Las siete llevan aqui su numero original.*

**LAS SEIS QUE TOCAN FICHERO VUELVEN A PASAR POR LA ADUANA**, porque una correccion vuelve a
escribir el candidato (`EXTRACTOR.md` 16). **La septima, la numero 9, es un encargo para el dia de
la insercion y no toca fichero ninguno.**

### Q.2.a. LAS LINEAS DEL LIBRO QUE MANDAN EN ESTAS SIETE, **CON SU `sed` PEGADO AL LADO** (`D.35`)

Salida de los siete comandos, guardada en `.t1_v23/citas_tarea1.txt`:

    $ sed -n "91p" fuentes/scott_radical_candor/cap_10.md | cut -c1-301
    THIS IS A high-level overview of three conversations that on the surface seem pretty
    straightforward. There's a lot riding on your ability to get them right: building trust with
    the people who report to you, figuring out what role each person is best suited for so that
    your team can achieve results

    $ sed -n "123p;127p" fuentes/scott_radical_candor/cap_11.md
    Good news only. ... In these cases, you need to ask explicitly for the bad news. Don't let
    the issue drop till you hear some.
    No agenda. ... or that they don't consider it useful. Be direct but polite: "This is your
    time, but you don't seem to come with much to talk about. Can you tell me why?"

    $ sed -n "53p" fuentes/scott_radical_candor/cap_11.md | grep -o "I like to limit myself to five direct reports"
    I like to limit myself to five direct reports

    $ sed -n "57p" fuentes/scott_radical_candor/cap_11.md
    Finally, to avoid meeting proliferation, I recommend that managers use the 1:1 time to have
    "career conversations" (see chapter seven) and, if relevant, to do formal performance reviews.

    $ grep -n -i -c "candle" fuentes/scott_radical_candor/cap_11.md
    0

    $ grep -o "A menorah?" fuentes/scott_radical_candor/cap_11.md
    A menorah?

    $ sed -n "229p;231p" fuentes/scott_radical_candor/cap_11.md | grep -o -E "it never really works|None was ever able to stick to it|I don.t think he ever hit the goal"
    it never really works
    None was ever able to stick to it
    I don't think he ever hit the goal

### Q.2.b. CORRECCION 3: **LA PIEZA 14 GANA SU PASO 12**, Y EL RESTO DE `cap_10` BAJA A `1.585`

Salida de `python .t1_v23/correccion_3.py`, guardada en `.t1_v23/salida_correccion_3.txt`:

| | |
|---|---|
| **fichero** | `cuarentena/scott_radical_candor/desplegar_tres_conversaciones_carrera.json` |
| **pasos antes** | **11** |
| **pasos despues** | **12** |
| **paso 12, impreso del fichero** | `Y ten presente lo que el texto dice que se juega tu capacidad de hacerlas bien: construir confianza con la gente que te reporta, y averiguar para que papel encaja mejor cada persona, para que tu equipo pueda conseguir resultados.` |

**Y LA FRONTERA DE `cap_10` SE RECIERRA CONTRA EL CUERPO, NO SE RETOCA A MANO.** El tramo
`L88 a L92` deja de ser resto y pasa a ser el **tramo d** de la pieza 14, con **0 nodos** porque la
pieza ya esta contada en su tramo c. Salida de `python .t1_v23/frontera_cap10.py`, guardada en
`.t1_v23/salida_frontera_cap10.txt`:

    tramos que dan nodo                    : 10
    tramos de resto                        : 5
    lineas con contenido de L8 en adelante : 128
    lineas NO cubiertas                    : 0  []
    SOLAPES                                : 0  []
    suma de las filas                      : 8976 palabras
    cuerpo medido aparte (sed 8,$ | wc -w) : 8976 palabras
    IGUALES                                : True
    la pieza 14, sus cuatro tramos         : 355 palabras

**LA TABLA, PEGADA DEL MISMO FICHERO Y NO TECLEADA** (`D.41`):

| tramo | palabras | nodos | que es | la salida, pegada |
|---|---:|---:|---|---|
| `L19` | 99 | **0** | pieza 14, tramo a: con quien y para que | `19:AS DESCRIBED IN Chapter Three, all people have their own growth trajectories, ` |
| `L21` | 82 | **0** | pieza 14, tramo b: cuando y donde caben | `21:Once you've gotten the hang of these conversations, you'll look forward to the` |
| `L43` | 73 | **1** | pieza 14, tramo c: la cadencia y el encargo a los jefes | `43:Realizing he'd come up with a good methodology for having career conversations` |
| `L88 a L92` | 101 | **0** | pieza 14, tramo d: lo que se juega en hacerlas bien (correccion 3) | `91:THIS IS A high-level overview of three conversations that on the surface seem ` |
| `L47 a L87` | 1862 | **3** | las tres conversaciones de carrera | `47:Conversation one: life story` |
| `L93 a L125` | 1095 | **1** | el plan anual de gestion del crecimiento | `93:GROWTH MANAGEMENT` |
| `L127 a L163` | 1501 | **1** | el proceso de contratacion, con el acto de L129 dentro | `127:HIRING: YOUR MENTALITY AND YOUR PROCESS` |
| `L165 a L201` | 1372 | **5** | despedir: cabeza, tres partes y coda | `165:FIRING` |
| `L203 a L223` | 638 | **1** | la calibracion de ascensos, con el caso de Google dentro | `203:PROMOTIONS` |
| `L225 a L251` | 568 | **2** | recompensar sin ascender | `225:REWARD YOUR ROCK STARS` |
| | **7391** | **14** | **los tramos que dan nodo** | |

| tramo de resto | palabras | nodos | que es, nombrado |
|---|---:|---:|---|
| `L9 a L18` | 206 | **0** | subtitulo, resumen del cap. 3 y los dos rotulos de seccion |
| `L20` | 0 | **0** | linea en blanco entre L19 y L21 |
| `L22 a L42` | 1136 | **0** | EL CASO DE RUSS LARAWAY entero: Google, Todd, Sarah y el plan de Sarah |
| `L44 a L45` | 45 | **0** | linea en blanco y el cierre del caso: la encuesta interna de Google |
| `L253 a L263` | 198 | **0** | el cuadro que no esta en el recorte, el resumen y la cabecera del cap siguiente |
| | **1585** | **0** | |

| # | id | pasos |
|---:|---|---:|
| 1 | `desplegar_tres_conversaciones_carrera` | **12** |
| 2 | `conversar_historia_vida_descubrir_motivadores` | **15** |
| 3 | `conversar_suenios_cruzar_habilidades` | **15** |
| 4 | `trazar_plan_dieciocho_meses_aprendizaje` | **14** |
| 5 | `armar_plan_anual_crecimiento_equipo` | **29** |
| 6 | `montar_proceso_contratacion_reducir_sesgo` | **32** |
| 7 | `facilitar_despido_tres_cosas` | **11** |
| 8 | `admitir_pronto_mal_desempenio_cuatro_razones` | **9** |
| 9 | `calibrar_decision_despido_documentarla` | **13** |
| 10 | `sopesar_consejo_legal_despedir_humildad` | **8** |
| 11 | `contactar_despedido_mes_despues` | **6** |
| 12 | `calibrar_ascensos_evitar_politica` | **19** |
| 13 | `evitar_obsesion_ascenso_estatus` | **10** |
| 14 | `reconocer_excelencia_trayectoria_gradual` | **13** |
| | **catorce candidatos** | **206** |

> **LAS TRES CIFRAS DEL AUDITOR SE CONFIRMAN AL DIGITO, Y LAS TRES SALEN DE MI INSTRUMENTO Y NO DE
> SU ENCARGO** (`EXTRACTOR.md` 5): la frontera **sigue en 14 piezas**, el resto baja de `1.686` a
> **`1.585`**, y la pieza 14 pasa de `11` a **`12`** pasos. **`cap_10` pasa de `205` a `206` pasos.**
>
> **Y UNA COSA QUE MI INSTRUMENTO MEJORA Y LO DIGO, porque cambia una celda:** la columna de cita
> del tramo imprimia la PRIMERA linea del tramo, y la primera de `L88 a L92` es la raya de
> separacion `* * *`. **Una celda de prueba que imprime una raya no prueba nada**, asi que el
> instrumento imprime ahora la primera linea CON CONTENIDO del tramo. Ninguna otra fila se mueve.

### Q.2.c. CORRECCION 4: **EL CANDELABRO PIERDE LAS SIETE VELAS QUE YO LE PUSE**

Salida de `python .t1_v23/correccion_4.py`, guardada en `.t1_v23/salida_correccion_4.txt`:

| | |
|---|---|
| **fichero** | `cuarentena/scott_radical_candor/debatir_decidir_asuntos_cultura_evitar_delegar.json` |
| **el paso 2 decia** | `si va a haber candelabro de las siete velas` |
| **el paso 2 dice** | `si va a haber candelabro` |
| **pasos, contados del fichero antes y despues** | **6** y **6** |
| **la relectura de fidelidad de la ficha** | de `6 TRANSCRIPCION, 0 PUENTE` a `5 TRANSCRIPCION, 1 PUENTE cazado y retirado` |

> **ES MIA Y LA CUENTO COMO MIA.** El libro escribe `A menorah?` y nada mas, `candle` sale **0**
> veces en el capitulo, y las tres de `seven` estan en `L57`, `L61` y `L153`, **ninguna en el tramo
> `L301` a `L305`**. Las siete velas las puse yo. **Y la frase de mi propio `resumen` que declaraba
> `0 PUENTE` era la que mas lo escondia**, porque afirmaba que las dos referencias culturales *se
> transcriben por lo que son* **en la misma frase en que una estaba inventada**.
>
> **`cap_11` pasa de `0 de 187` a `1 de 187`, o sea `0,53`.** No mueve el freno: la fila que decide
> sigue siendo `cap_04`.

### Q.2.d. CORRECCION 5: **LOS DOS ENCARGOS PERDIDOS VUELVEN, Y EL TERCER MOTIVO SE CORRIGE**

Salida de `python .t1_v23/correccion_5.py`, guardada en `.t1_v23/salida_correccion_5.txt`:

| senial | lo que el paso traia | lo que el paso trae |
|---|---|---|
| `L123`, solo buenas noticias | `e siente comoda trayendote sus problemas, o de que cree que no vas a hacer nada con ellos.` | ` pide explicitamente las malas noticias, y no dejes caer el asunto hasta que oigas alguna.` |
| `L127`, sin agenda | `esbordados, que no entienden para que es esta reunion, o que no la estan tomando en serio.` | ` este es tu tiempo, pero no pareces venir con mucho de que hablar. Puedes decirme por que?` |
| **pasos, contados del fichero** | **6** | **6** |

> **Y EL `resumen` DEJA DE AFIRMAR LO QUE NO ERA.** Decia que *la unica accion encargada que el
> texto da es la de la segunda senial... las otras tres solo traen su lectura*. **El libro encarga
> en CUATRO de las cinco** (`L121`, `L123`, `L125`, `L127`), y la unica que solo trae lectura es la
> primera, la de las cancelaciones de `L119`. **La especie no es puente: es lo contrario, no
> escribir lo que el libro si dice**, y `D.30` no la cubre.

### Q.2.e. CORRECCION 6: **LAS DOS ARISTAS QUE `L57` DEBE, Y LA PROMESA QUE SOBRABA**

**LA MITAD DE FICHERO.** Salida de `python .t1_v23/correccion_6.py`, guardada en
`.t1_v23/salida_correccion_6.txt`:

| | |
|---|---|
| **fichero** | `cuarentena/scott_radical_candor/preguntar_seguimiento_hallar_huecos.json` |
| **decia** | `Ese procedimiento ya vive en la bandeja como impedir_punialadas_espalda_equipo, y la arista va declarada en docs/loop/REPORTE.md de la vuelta 22.` |
| **dice** | `Ese procedimiento ya vive en la bandeja como impedir_punialadas_espalda_equipo, y EL PAR SE DECLARA COMO LECTURA SIN ARISTA: sin paso en la madre no hay linea que citar, y una arista sin su linea es una afirmacion sin cita.` |
| **pasos, contados del fichero antes y despues** | **16** y **16** |

**LA MITAD DE ARISTA**, que no es de fichero y va a la deuda de `Q.7`:

| # | madre | hijo | `--paso` | especie | el paso de la madre, impreso del fichero |
|---:|---|---|---:|---|---|
| 36 | `montar_reuniones_solas_mentalidad_frecuencia` | `desplegar_tres_conversaciones_carrera` | **15** | `D.29` | `Para evitar que las reuniones se multipliquen, usa el tiempo de la reunion a solas para tener las conversaciones de carrera y, si toca, para hacer las evaluaciones formales de desempenio.` |
| 37 | `montar_reuniones_solas_mentalidad_frecuencia` | `entregar_evaluacion_formal_desempenio_nueve_consejos` | **15** | `D.29` | *(el mismo paso 15, que nombra los dos)* |

**LA DEUDA PASA DE `35` A `37`**, y las dos se cablean con el mismo acto que las otras 35.

### Q.2.f. CORRECCION 7: **`montar_reuniones_solas` RECOGE EL LIMITE DE `L53` EN VEZ DE CALLARLO**

Salida de `python .t1_v23/correccion_7.py`, guardada en `.t1_v23/salida_correccion_7.txt`:

| | |
|---|---|
| **fichero** | `cuarentena/scott_radical_candor/montar_reuniones_solas_mentalidad_frecuencia.json` |
| **el paso 10 acababa en** | `lendario, porque escuchar es trabajo duro y no hay capacidad infinita para ello.` |
| **el paso 10 acaba en** | `; y por esa misma razon el texto dice que se limita a cinco personas a su cargo.` |
| **pasos en los que ya aparece `cinco personas`** | **[10]** |
| **pasos, contados del fichero antes y despues** | **22** y **22** |

> **EL AUDITOR DEJA DOS SALIDAS Y ELIJO LA SEGUNDA, Y DIGO POR QUE.** La primera (que el `resumen`
> deje de afirmarlo) arregla la frase y **pierde una linea del libro**; la segunda arregla la frase
> **y devuelve al nodo el limite que `L53` escribe**. La cuenta de pasos **no se mueve** porque la
> correccion alarga un paso existente en vez de anadir uno nuevo: **`cap_11` sigue en 187 pasos.**

### Q.2.g. CORRECCION 8: **LOS TRES `No pruebes` PASAN A LLEVAR LA EVIDENCIA DEL LIBRO**

Salida de `python .t1_v23/correccion_8.py`, guardada en `.t1_v23/salida_correccion_8.txt`:

| paso | como empezaba | como empieza | la evidencia del libro, y su linea |
|---:|---|---|---|
| 3 | `No pruebes el primer r` | `Ten delante el primer ` | `it never really works`, `L229` |
| 4 | `No pruebes el segundo,` | `Ten delante el segundo` | `None was ever able to stick to it`, `L231` |
| 5 | `Ni el tercero, ponerse` | `Y ten delante el terce` | `I don't think he ever hit the goal`, `L231` |
| | **8 pasos** | **8 pasos** | **la cuenta no se mueve** |

> **EL LIBRO NO PROHIBE: CUENTA QUE NO CUAJARON.** Convertir un informe de fracaso en un imperativo
> negativo mueve el modo del libro. **El numerador de `PASOS INVENTADOS` no se mueve** (no se anade
> medio, etapa ni objeto) y `L233` sigue ordenando entre ellos, asi que el paso 6 conserva su
> imperativo y manual seccion 2 sigue satisfecha: `Ten delante` es imperativo.

### Q.2.h. CORRECCION 9: **EL ENCARGO PARA EL DIA DE LA INSERCION, ESCRITO Y NO EJECUTADO**

**No toca fichero y no se puede ejecutar hoy**, porque hoy no se cablea ninguna arista (`Q.7`).
Queda escrita aqui y repetida en la deuda:

> **LA ARISTA DE LA RUEDA DE LA CULTURA NO SE CABLEA CON `--paso 2` DE LA MADRE.** El paso 2 de
> `recorrer_rueda_hacer_cosas_equipo` dice *escucha las ideas que tiene la gente de tu equipo, y
> crea una cultura en la que se escuchen entre ellos*, y **eso es contenido de la etapa `Listen`, no
> el nombre de la hija**. La clase `CONTINUA` y la arista `D.29` **se sostienen por su razon
> escrita** (la hija anade la prueba de la conducta propia de `L299`, el cafe y el te verde de
> `L311`, el entorno de oficina de `L313` y la senial de `L329`, y la madre no tiene ninguna de las
> cuatro), y **la prueba cuelga del `P4` de la hija**, no de un paso de la madre.

### Q.2.i. LAS SEIS CORRECCIONES DE FICHERO, DE VUELTA POR LA ADUANA

*`EXTRACTOR.md` 16: una correccion vuelve a escribir el candidato, asi que vuelve a pasar por la
puerta. Los seis informes de un candidato estan en `.aduana_v23/`, uno por fichero.*

| candidato corregido | veredicto de su informe | vecinos levantados |
|---|---|---:|
| `desplegar_tres_conversaciones_carrera` | **BLOQUEARIA** | 1 |
| `debatir_decidir_asuntos_cultura_evitar_delegar` | **ENTRARIA** | 0 |
| `leer_seniales_fallo_jefe_reunion_solas` | **ENTRARIA** | 0 |
| `montar_reuniones_solas_mentalidad_frecuencia` | **ENTRARIA** | 0 |
| `pelear_proliferacion_reuniones_bloquear_ejecucion` | **ENTRARIA** | 0 |
| `preguntar_seguimiento_hallar_huecos` | **BLOQUEARIA** | 1 |

<!-- TALLADO: parcial salida=.t1_v23/salida_saldo_v23.txt -->

**CERO `CAERIA` EN LAS SEIS.** Los dos `BLOQUEARIA` son cola de lectura y sus dos pares van leidos
con su razon escrita en `Q.6`. **La tabla entera de saldos, con su poblacion y sus pares, se publica
en `Q.5.d` desde el fichero de su instrumento.**

---

## Q.3. TAREA 2: EL TALLADOR. **CERRADA, Y NO COMO TRAMITE**

*`D.41`. No es una tarea de trabajo: es como se trabaja a partir de hoy. La pongo con numero porque
mi racha `REPORTE` se reinicio contra ella.*

**LO QUE HE HECHO, Y ES LO UNICO QUE VALE:** cada tabla de este reporte que dice venir de un
instrumento **tiene su fichero de salida en el arbol** y **esta pegada de ahi**. Los ficheros son:

| tabla | instrumento | salida guardada |
|---|---|---|
| la apertura | los nueve comandos de `Q.0` | `.t1_v23/apertura_tabla.txt` |
| la frontera de `cap_10` recerrada | `python .t1_v23/frontera_cap10.py` | `.t1_v23/salida_frontera_cap10.txt` |
| la frontera de `cap_12` | `python .t1_v23/frontera_cap12.py` | `.t1_v23/salida_frontera_cap12.txt` |
| la frontera de `cap_13` | `python .t1_v23/frontera_cap13.py` | `.t1_v23/salida_frontera_cap13.txt` |
| las seis correcciones de fichero | `python .t1_v23/correccion_N.py` | `.t1_v23/salida_correccion_N.txt` |
| el saldo de la aduana | `python .t1_v23/saldo_v23.py` | `.t1_v23/salida_saldo_v23.txt` |
| las tres guardas del cierre | `gate`, `guiones`, `test_aceptacion` | `.t1_v23/salida_*_cierre.txt` |

**Y LAS QUE RESUMEN EN VEZ DE REPRODUCIR VAN DECLARADAS `parcial`** con su marcador encima, que es
lo que `D.41` manda decir en vez de callar. **En esta vuelta son tres**, y estan en `Q.0`, `Q.2.i` y
`Q.9`.

> **LO QUE ESTA TAREA ME CAMBIA DE VERDAD, y lo escribo porque es la leccion y no el tramite:** en
> la vuelta 22 mi reporte llevaba **una tabla pegada** (`cap_10`, al digito) **y una tecleada**
> (`cap_11`, 14 de 18 celdas falsas). **La diferencia no fue el cuidado: fue el metodo.** Esta
> vuelta **ninguna tabla de instrumento se ha tecleado**, y eso no lo digo yo: lo comprueba el hook
> celda a celda en cada commit, y **si difiere, aborta**.
