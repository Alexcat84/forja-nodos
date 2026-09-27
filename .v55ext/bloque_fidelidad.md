
---

## VV.4. TAREA 4: **LA FIDELIDAD `D.30`, SU MUESTRA CON LA SEMILLA `v55`, Y LA MORDIDA QUE ME LLEVE**

**LA SEMILLA ES `v55` Y LA MUESTRA NO LA ELIJO YO.** Quien audite vuelve a correr esta linea y
**tiene que salirle esta misma lista**; si le sale otra, es caida de cifra (`D.58`).

<!-- TALLADO: script=scripts/muestra_fidelidad.py salida=.v55ext/muestra.txt -->

    $ python scripts/muestra_fidelidad.py --libro grove_high_output --capitulos cap_07,cap_09,cap_10 --semilla v55
    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : grove_high_output
      semilla  : v55
      capitulos: cap_07, cap_09, cap_10

      RELEIDO ENTERO : cap_09
      POR MUESTRA    : cap_07, cap_10, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_07: 15 paso(s) en la muestra
        cerrar_brecha_dos_preguntas_estrategia         P1   Emprende tareas nuevas o modifica las que ya tienes para cer
        cerrar_brecha_dos_preguntas_estrategia         P2   Contesta la primera pregunta: que necesitas hacer para cerra
        contestar_dos_preguntas_direccion_objetivos    P3   Toma la respuesta de esa primera pregunta como tu objetivo.
        contestar_dos_preguntas_direccion_objetivos    P4   Contesta la segunda pregunta: como voy a marcarme el ritmo p
        definir_entorno_grupo_clientes_proveedores_com P4   Lista a tus proveedores, que son quienes pueden darte determ
        examinar_demanda_entorno_dos_marcos_temporales P2   Contesta que quieren de ti tus clientes ahora.
        examinar_demanda_entorno_dos_marcos_temporales P5   Concentrate en la diferencia entre lo que tu entorno te dema
        fijar_horizonte_ventana_replanificacion        P1   Mira hacia delante mas alla del periodo que vas a implementa
        fijar_horizonte_ventana_replanificacion        P2   Implementa unicamente la parte del plan que cae dentro de la
        fijar_horizonte_ventana_replanificacion        P3   Deja todo lo demas para volver a mirarlo, contando con que t
        fijar_periodo_direccion_objetivos_retroaliment P5   Contrastalo con la base sobre la que planificas: si planific
        planificar_tres_pasos_demanda_estado_brecha    P1   Monta tu proceso general de planificacion sobre un razonamie
        planificar_tres_pasos_demanda_estado_brecha    P2   Da el paso 1 estableciendo la necesidad o demanda proyectada
        planificar_tres_pasos_demanda_estado_brecha    P4   Formula ese paso 2 tambien de la otra manera, que es la que 
        planificar_tres_pasos_demanda_estado_brecha    P6   Convierte esa conciliacion en la pregunta concreta: que mas,

      --- cap_10: 8 paso(s) en la muestra
        repartir_supervision_puesto_funcional_mision   P1   Parte de lo que hace falta para que la organizacion hibrida 
        repartir_supervision_puesto_funcional_mision   P2   Deja que el grupo funcional al que el puesto pertenece fije 
        repartir_supervision_puesto_funcional_mision   P3   Haz en consecuencia que ese puesto dependa de alguien de la 
        repartir_supervision_puesto_funcional_mision   P4   Ajusta el tipo de supervision de cada uno de los dos a las n
        repartir_supervision_puesto_funcional_mision   P5   Encarga al jefe de la unidad de mision que le de las priorid
        repartir_supervision_puesto_funcional_mision   P6   Encarga al jefe funcional que se asegure de que esta formado
        repartir_supervision_puesto_funcional_mision   P7   Encarga a ese mismo jefe funcional que supervise y vigile su
        repartir_supervision_puesto_funcional_mision   P8   Encarga al jefe funcional que cuide su carrera dentro de la 

      --- cap_09: ENTERO, 0 paso(s), no hay muestra que elegir


> **EL REPARTO QUE SALIO, y conviene decir lo que tiene de raro:** la semilla mando releer
> **ENTERO `cap_09`**, que es precisamente el capitulo al que **mi frontera le da CERO nodos**.
> Releer entero un capitulo sin candidatos **no cuesta nada y no prueba nada**: su fila sale
> `0` de `0` y lo digo con esas palabras, en vez de publicar un `0,0 por ciento` que parezca un
> aprobado. **`cap_10` cae en el cubo de la muestra pero solo tiene `8` pasos escritos, asi que
> se relee ENTERO de todas formas**: la muestra pide `15` y no hay `15`.

### VV.4.a. **LA RELECTURA NO SE PROMETE: EL INSTRUMENTO BUSCA EL FRAGMENTO EN EL FICHERO**

**Es el remedio mecanico de `D.35` llevado a `D.30`.** Para cada paso de la muestra escribo el
fragmento ingles del que sale, y `.v55ext/pasos_inventados.py` **lo busca en
`fuentes/grove_high_output/<cap>.md`**. Un paso cuyo fragmento no aparezca **se marca `PUENTE`
solo, sin que yo pueda salvarlo.** Es el instrumento de la vuelta `53` con esa pieza anadida,
y la pieza la ordena la TAREA 4 de este encargo (`EXTRACTOR.md` 13).

<!-- TALLADO: script=.v55ext/pasos_inventados.py salida=.v55ext/pasos_inventados.txt -->
LA RELECTURA, PASO A PASO: EL FRAGMENTO SE BUSCA EN EL FICHERO DEL CAPITULO
==============================================================================
| capitulo | candidato | paso | marca | linea del libro donde el instrumento lo encuentra |
|---|---|---:|---|---|
| `cap_07` | `cerrar_brecha_dos_preguntas_estrategia` | 1 | TRANSCRIPCION | `L39`: `The final step of planning consists of undertaking new tasks or modifyin` |
| `cap_07` | `cerrar_brecha_dos_preguntas_estrategia` | 2 | TRANSCRIPCION | `L39`: `The first question is, What do you need to do to close the gap?` |
| `cap_07` | `contestar_dos_preguntas_direccion_objetivos` | 3 | TRANSCRIPCION | `L73`: `The answer provides the objective` |
| `cap_07` | `contestar_dos_preguntas_direccion_objetivos` | 4 | TRANSCRIPCION | `L75`: `How will I pace myself to see if I am getting there?` |
| `cap_07` | `definir_entorno_grupo_clientes_proveedores_com` | 4 | TRANSCRIPCION | `L25`: `vendors who are able to provide you with certain capabilities` |
| `cap_07` | `examinar_demanda_entorno_dos_marcos_temporales` | 2 | TRANSCRIPCION | `L29`: `What do my customers want from me now?` |
| `cap_07` | `examinar_demanda_entorno_dos_marcos_temporales` | 5 | TRANSCRIPCION | `L29`: `You need to focus on the difference between what your environment demand` |
| `cap_07` | `fijar_horizonte_ventana_replanificacion` | 1 | TRANSCRIPCION | `L61`: `But what is really being influenced here? It is the next year` |
| `cap_07` | `fijar_horizonte_ventana_replanificacion` | 2 | TRANSCRIPCION | `L61`: `you implement only that portion of a plan that lies within the time wind` |
| `cap_07` | `fijar_horizonte_ventana_replanificacion` | 3 | TRANSCRIPCION | `L61`: `Everything else you can look at again` |
| `cap_07` | `fijar_periodo_direccion_objetivos_retroaliment` | 5 | TRANSCRIPCION | `L79`: `if we plan on a yearly basis, the corresponding MBO system` |
| `cap_07` | `planificar_tres_pasos_demanda_estado_brecha` | 1 | TRANSCRIPCION | `L19`: `Your general planning process should consist of analogous thinking` |
| `cap_07` | `planificar_tres_pasos_demanda_estado_brecha` | 2 | TRANSCRIPCION | `L19`: `Step 1 is to establish projected need or demand` |
| `cap_07` | `planificar_tres_pasos_demanda_estado_brecha` | 4 | TRANSCRIPCION | `L19`: `where will your business be if you do nothing different from what you ar` |
| `cap_07` | `planificar_tres_pasos_demanda_estado_brecha` | 6 | TRANSCRIPCION | `L19`: `what more (or less) do you need to do to produce what your environment w` |
| `cap_10` | `repartir_supervision_puesto_funcional_mision` | 1 | TRANSCRIPCION | `L43`: `you need a way to coordinate the mission-oriented units and the function` |
| `cap_10` | `repartir_supervision_puesto_funcional_mision` | 2 | TRANSCRIPCION | `L43`: `His professional methods, practices, and standards are set by the functi` |
| `cap_10` | `repartir_supervision_puesto_funcional_mision` | 3 | TRANSCRIPCION | `L43`: `should report to someone in both the functional and the mission-oriented` |
| `cap_10` | `repartir_supervision_puesto_funcional_mision` | 4 | TRANSCRIPCION | `L43`: `with the type of supervision reflecting the varying needs of the two` |
| `cap_10` | `repartir_supervision_puesto_funcional_mision` | 5 | TRANSCRIPCION | `L43`: `gives the controller mission-oriented priorities by asking him to work o` |

### VV.4.b. **LA MORDIDA, DECLARADA Y NO BORRADA**

> **LA PRIMERA CORRIDA ME MARCO UN `PUENTE`, y era mio.** Sale en
> `.v55ext/pasos_inventados_mordida.txt`, que guardo entero:

    | `cap_07` | `planificar_tres_pasos_demanda_estado_brecha` | 6 | **PUENTE** | **el fragmento NO esta en el fichero** |
    | capitulo | candidatos | pasos escritos | regimen `D.58` | pasos releidos | PUENTE | `PASOS INVENTADOS` |
    EL NUMERADOR ES `pasos marcados PUENTE` Y EL DENOMINADOR `pasos releidos`,

> **QUE FALLO, exactamente:** el paso `6` de `planificar_tres_pasos_demanda_estado_brecha` dice
> *que mas, o que menos, necesitas hacer*. **El paso esta bien.** Lo que estaba mal era **mi
> fragmento de cita**: escribi `what more or less do you need to do` y el libro pone
> `what more (or less) do you need to do`, **con los parentesis**. Lo compruebo contra el
> fichero, con la salida pegada (`D.35`, sede `.v55ext/cita_paso6.txt`):

    $ sed -n '19p' fuentes/grove_high_output/cap_07.md | tr " " "
" | tail -16 | tr "
" " "
    what more (or less) do you need to do to produce what your environment will demand?

> **CORRECCION DECLARADA, SIN BORRAR:** corrijo **el fragmento**, no el paso, y dejo la corrida
> que mordio en su fichero. **Y anoto lo que esto ensena, porque no es una anecdota:** una
> relectura de fidelidad que se firma *lo mire y esta bien* no habria visto nada, ni en un
> sentido ni en el otro. **La que obliga a teclear el fragmento y lo busca, muerde.** Es
> literalmente el argumento de `D.35`: *los dos remedios que han funcionado obligan a teclear
> algo, y los dos que se rompieron eran intenciones.*

### VV.4.c. **`PASOS INVENTADOS POR CAPITULO` (`D.59`): UNA FILA POR CAPITULO, CON SU NUMERADOR Y SU DENOMINADOR**

<!-- TALLADO: script=.v55ext/pasos_inventados.py salida=.v55ext/pasos_inventados.txt -->
| capitulo | candidatos | pasos escritos | regimen `D.58` | pasos releidos | PUENTE | `PASOS INVENTADOS` |
|---|---:|---:|---|---:|---:|---:|
| `cap_07` | 9 | 53 | MUESTRA de 15 | 15 | **0** | **0,0 por ciento, 0 de 15** |
| `cap_09` | 0 | 0 | ENTERO | 0 | **0** | **0,0 por ciento, 0 de 0** |
| `cap_10` | 1 | 8 | ENTERO, 8 de 8 | 8 | **0** | **0,0 por ciento, 0 de 8** |

<!-- TALLADO: parcial script=.v55ext/pasos_inventados.py salida=.v55ext/pasos_inventados.txt -->

    EL NUMERADOR ES `pasos marcados PUENTE` Y EL DENOMINADOR `pasos releidos`,
    no los pasos escritos: la muestra de D.58 no relee todos los pasos del capitulo.
    cap_07      0,0 por ciento contra un tope de 10 : NO DISPARA
    cap_09      0,0 por ciento contra un tope de 10 : SIN SUPERFICIE: 0 candidatos y 0 pasos, no hay que releer
    cap_10      0,0 por ciento contra un tope de 10 : NO DISPARA
    LA CUARTA GUARDA DE DATO DE D.55, la fidelidad D.30 con puente: 0 puente(s).
    EN VERDE.

> **EL DISPARADOR NO SE ACTIVA EN NINGUNA DE LAS TRES FILAS, y la guarda de dato de `D.55`
> queda en VERDE por esta via.**
