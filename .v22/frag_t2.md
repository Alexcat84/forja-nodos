
---

## P.3. TAREA 2, **BLOQUEANTE Y PRIMERA**: LA PIEZA QUE `cap_10` DEBE, Y LAS DOS CORRECCIONES DE FICHERO. **CERRADA**

### P.3.a. LA PIEZA 14, ESCRITA: `desplegar_tres_conversaciones_carrera`

**EL MATERIAL, REMEDIDO POR MI COMO EL ENCARGO MANDA, CON SU `sed` PEGADO** (`D.35`):

    $ sed -n '19p;21p;43p' fuentes/scott_radical_candor/cap_10.md | wc -w
      254

| linea | palabras | la salida, pegada (principio de la linea) |
|---|---:|---|
| `L19` | 99 | `19:AS DESCRIBED IN Chapter Three, all people have their own growth trajectories, and it's a mistake to push everyone to be either a "superstar" or a "rock star."` |
| `L21` | 82 | `21:Once you've gotten the hang of these conversations, you'll look forward to them.` |
| `L43` | 73 | `43:Realizing he'd come up with a good methodology for having career conversations, Russ held an off-site and taught his managers how to talk to their direct reports...` |
| | **254** | **la cifra del encargo REPRODUCE al digito** |

**Y LA CUENTA QUE HACE DE ESTO UNA SERIE `D.37` Y NO UNA `D.29`, ESCRITA DOS VECES POR EL LIBRO:**

    $ sed -n '43p' fuentes/scott_radical_candor/cap_10.md   (final de la linea)
      ...a succession of three forty-five-minute conversations with each direct report
      over the course of three to six weeks.
    $ sed -n '91p' fuentes/scott_radical_candor/cap_10.md   (principio)
      THIS IS A high-level overview of three conversations that on the surface seem
      pretty straightforward.

**LA REGLA QUE LA MANDA, Y NO LA PROHIBE:** manual 3.4, *si es serie numerada de un libro: un nodo
por paso **mas UNA cabeza**, jamas dos compresiones de la misma numeracion.* **La cabeza esta
prescrita; lo prohibido es la SEGUNDA**, y esta es la primera y unica: las tres partes no estan
resumidas aqui en sus pasos, solo nombradas por su materia en el paso 11.

### P.3.b. LOS ONCE PASOS, IMPRESOS DEL FICHERO Y NO TECLEADOS (`EXTRACTOR.md` 5), CON SU RELECTURA DE FIDELIDAD `D.30` AL LADO

*Salida en `.t1_v22/salida_pasos_pieza14.txt`, generada con `json.load` sobre el propio candidato.*

| paso | linea | **`D.30`** | la salida, pegada |
|---:|---|---|---|
| P1 | `L19` | TRANSCRIPCION | `Ten estas conversaciones de carrera con cada persona que te reporta directamente, sea cual sea el sitio que ocupe en el marco de equipo descrito en el capitulo tres.` |
| P2 | `L19` | TRANSCRIPCION | `Parte de lo que el texto pone debajo: todas las personas tienen su propia trayectoria de crecimiento, y es un error empujar a todo el mundo a ser o una superestrella o una roca...` |
| P3 | `L19` | TRANSCRIPCION | `Tenlas para entender la trayectoria de crecimiento de la persona, que es el motivo por el que el texto dice que son importantes.` |
| P4 | `L19` | TRANSCRIPCION | `Persigue en ellas los tres propositos que el texto enumera: conocer mejor a cada persona a tu cargo, aprender cuales son sus aspiraciones, y planear como ayudarla a alcanzar esos suenios.` |
| P5 | `L21` | TRANSCRIPCION | `Ponlas como lo primerisimo que haces al desplegar la franqueza radical en tu equipo, que es donde el texto las recomienda.` |
| P6 | `L21` | TRANSCRIPCION | `Cuenta con que llevan tiempo, y metelas en tus huecos de 1:1 de siempre: el texto dice que ahi pueden ocurrir.` |
| P7 | `L21` | TRANSCRIPCION | `Cuenta con lo que el texto dice que son: tu mayor oportunidad, la unica mas grande, de subir en el eje de importarte personalmente del marco de la franqueza radical.` |
| P8 | `L21` | TRANSCRIPCION | `Y cuenta con lo que el texto dice que pasa cuando les coges el tranquillo: las esperaras con ganas, y generaran algunas de las conversaciones mas disfrutables que tienes como jefe.` |
| P9 | `L43` | TRANSCRIPCION | `Dales la cadencia que el texto escribe: una sucesion de tres conversaciones de cuarenta y cinco minutos con cada persona a tu cargo, en el curso de tres a seis semanas.` |
| P10 | `L43` | **TRANSCRIPCION con transposicion de persona, DECLARADA** | `Ensenia a cada jefe de tu equipo a tenerlas con las personas a su cargo. Es lo que el texto cuenta que hizo Russ...: reunio a sus jefes fuera de la oficina y se lo ensenio.` |
| P11 | `L43` | **TRANSCRIPCION con transposicion de persona, DECLARADA** | `Y ensenia a hablar con las personas a su cargo no solo de sus metas de carrera o de como ascender, sino tambien de sus historias de vida y de sus suenios.` |
| | | **11 TRANSCRIPCION, 0 PUENTE** | |

> ### **LOS DOS PASOS CON TRANSPOSICION LOS DECLARO YO ANTES DE QUE NADIE LOS BUSQUE, Y VAN MARCADOS COMO DISCUTIBLE 1.**
>
> `L43` escribe **en pasado y sobre otro** (*He taught every manager on his team...*) y aqui van en
> **imperativo dirigido al lector**. Es la transposicion que manual 3.5 prescribe (*la doctrina vive
> en su nodo*) mas manual seccion 2 (*pasos accionables, en imperativos*). **No anaden ni un medio,
> ni una etapa ni un objeto que `L43` no nombre.** Si el auditor lee que esto es puente, **son dos
> puentes y el numerador de `cap_10` sube de 17 a 19** (`19 / 205 = 9,27`, que sigue bajo el tope de
> 10). Lo digo con la cuenta hecha en los dos sentidos para no tener que elegir la que me favorece.

**LAS CUATRO COSAS QUE EL TEXTO NO DICE Y POR ESO NO ESTAN ESCRITAS, y son literalmente las tres
especies de puente de `D.30`:** quien convoca la reunion fuera de la oficina (**el responsable**),
cada cuanto se repite la serie con la misma persona (**el periodo**), que se hace si una de las tres
no cabe en el hueco de 1:1, y **como compruebas que un jefe al que ensenaste las esta teniendo**
(**el destinatario del rastro**). Ninguna esta en `L19`, `L21` ni `L43`.

**LA SENIAL BARATA DE MANUAL 3.5, CORRIDA Y NO PROMETIDA** (el entregable no puede llevar un dato
del caso):

    Russ False | Google False | Todd False | Sarah False | Laraway False | encuesta False | off-site False

### P.3.c. LA ADUANA, EN EL MISMO ACTO EN QUE SE ESCRIBIO (`EXTRACTOR.md` 16)

    $ python forja.py informe cuarentena/scott_radical_candor/desplegar_tres_conversaciones_carrera.json
      poblacion del barrido       : 300   (203 del grafo mas 97 que esperan en bandejas)
      umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

      [BLOQUEARIA] desplegar_tres_conversaciones_carrera
          vecino conversar_historia_vida_descubrir_motivadores  [levantada por: paso_contra_nodo]
            similitud_texto 0.252 | familia_id 0.000 | paso_contra_nodo 0.647
            paso 1 del candidato contra paso 1 de conversar_historia_vida_descubrir_motivadores

      real  2m45.031s

**`0 CAERIA` AL PRIMER INTENTO, asi que el candidato cuenta como escrito** (`EXTRACTOR.md` 16 punto
4). La salida entera esta en `.aduana_v22/14_desplegar_tres_conversaciones.txt`.

> ### **HECHO NUEVO 1, Y ES DEL INSTRUMENTO: POR PRIMERA VEZ EN ESTA CASA UNA SENIAL LEVANTA SOLA UNA ARISTA DE CABEZA A PARTE.**
>
> La `ACTA 21` `5.1` midio que las vecindades que una lectura encuentra viven **por debajo** de los
> umbrales, y `D.19` midio que la señal 3 levanta el **3 por ciento** de las aristas declaradas.
> **Hoy la señal 3 levanta una de las tres `D.37` de esta cabeza**, con `paso_contra_nodo 0,647`
> contra umbral `0,60`. **Y NO CAMBIA NADA DE LO QUE HAGO:** las otras dos hijas **no** se levantan
> (no aparecen en el informe), asi que **las tres se declaran por lectura igual**, que es lo que
> `D.37` manda. Lo traigo porque es una medida que corrige el tono de mi propia vuelta 21, no porque
> me favorezca: **una de tres no es la señal haciendo el trabajo de la lectura.**
>
> **Y la razon de que esta si se levante esta en la propia salida:** `paso 1 del candidato contra
> paso 1 de conversar_historia_vida`. Los dos pasos empiezan con el mismo acto (*ten esta
> conversacion con cada persona que te reporta directamente*), **porque la cabeza transcribe `L19` y
> la parte lo repite en su primer paso.** Es proximidad de redaccion, no de procedimiento.

> ### **HECHO NUEVO 2, TAMBIEN DEL INSTRUMENTO: EL INFORME DE UN CANDIDATO COSTO HOY `165` SEGUNDOS, NO LOS `453` DE MI VUELTA 21 NI LOS `156,5` DE `D.41`.**
>
> `real 2m45.031s`, medido con `time` y pegado arriba. **Las tres cifras son ciertas cada una en su
> corrida** y la poblacion ademas crecio (`299` a `300`), asi que **la discrepancia se declara y no
> se resuelve copiando** (`EXTRACTOR.md` 5). Lo que si cambia es una decision practica mia: con
> `165` s por candidato **los informes de `cap_11` caben en la vuelta**, y por eso los corro todos.

### P.3.d. **EL VEREDICTO DEL VECINO QUE LA ADUANA LEVANTO, CON SU RAZON ESCRITA** (`EXTRACTOR.md` 2)

| | |
|---|---|
| **par** | `desplegar_tres_conversaciones_carrera` (madre) contra `conversar_historia_vida_descubrir_motivadores` (hija) |
| **clase** | **`CONTINUA` con arista `D.37`** |
| **razon** | **es la cabeza de la serie contra su primera parte, y la cuenta la escribe el libro dos veces** (`L43` *a succession of three forty-five-minute conversations*, `L91` *three conversations*). **El solape es de una frase y no de procedimiento:** el paso 1 de las dos transcribe `L19` (*con cada persona que te reporta directamente*), y a partir de ahi **no comparten ni un acto**: la cabeza pone con quien, para que, donde caben y cual es la cadencia de las TRES; la hija pone la apertura literal de la PRIMERA (*empezando por la guarderia, cuentame tu vida*), el foco en los cambios y el limite de no presionar donde la persona senializa incomodidad. **La cabeza no despliega ninguna conversacion y la hija no pone la cadencia de la serie** |
| **sede** | **hoy solo `REPORTE.md`**, porque no hay insercion (`P.0.1`). **`bitacora/VEREDICTOS.jsonl` es su sede y lo sera el dia de la insercion** (`D.39`) |

### P.3.e. LAS TRES ARISTAS `D.37` DE ESTA CABEZA, **DECLARADAS ENTERAS** (y NO cableadas, por la correccion de `2.b` del encargo)

**LA CORRECCION QUE EL ENCARGO TRAE Y QUE RECOJO:** `D.37` y `EXTRACTOR.md` 15.6 dicen *declaras
esas aristas en la misma vuelta en que **INSERTAS** las partes*. **Hoy no se inserta**, asi que **se
declaran y se cablean el dia de la insercion**. Y **no corro `forja.py arista` contra ids que viven
en cuarentena**: la `ACTA 21` `2.3` volvio a morder esa guarda por los dos extremos y yo la medi en
mi `O.4.b` de la vuelta 21. **No repito un rechazo ya medido dos veces.**

**EL PASO DE LA MADRE QUE ENUMERA LAS PARTES, IMPRESO DEL FICHERO:**

    paso 11: Y ensenia a hablar con las personas a su cargo no solo de sus metas de carrera o
             de como ascender, sino tambien de sus historias de vida y de sus suenios.

| # | madre | hijo | `--paso` | razon |
|---:|---|---|---:|---|
| 1 | `desplegar_tres_conversaciones_carrera` | `conversar_historia_vida_descubrir_motivadores` | **11** | el paso 11 de la madre nombra **las historias de vida** en una linea, y el hijo la despliega en **15 pasos** que la cabeza no tiene: la apertura literal, el foco en los cambios, los cuatro ejemplares y el limite de la incomodidad |
| 2 | `desplegar_tres_conversaciones_carrera` | `conversar_suenios_cruzar_habilidades` | **11** | el paso 11 de la madre nombra **los suenios** en una linea, y el hijo los despliega en **15 pasos** que la cabeza no tiene: cruzar los suenios con las habilidades y sacar lo que la persona quiere y puede |
| 3 | `desplegar_tres_conversaciones_carrera` | `trazar_plan_dieciocho_meses_aprendizaje` | **11** | el paso 11 de la madre nombra **las metas de carrera y el como ascender** en una linea, y el hijo los despliega en **14 pasos** que la cabeza no tiene: el plan de dieciocho meses con su aprendizaje |
| | | | | **y la CUENTA que las hace `D.37` y no `D.29` esta escrita en `L43` y en `L91`** |

**LA DEUDA DE ARISTAS SUBE A `19`** y **dieciocho de las diecinueve se desbloquean con el mismo
acto**, el cierre del lote 4. Van repetidas enteras en el cierre, sin resumirlas.

### P.3.f. LAS DOS CORRECCIONES DE FICHERO, DECLARADAS Y SIN BORRAR EL TEXTO VIEJO

**CORRECCION 1, `facilitar_despido_tres_cosas.json`, campo `entregable_esperado`** (`ACTA 21` `4.4`):

| | |
|---|---|
| **decia** | `Las tres cosas del texto identificadas y encargadas como el plan del despido, y tu empresa situada respecto a los dos errores opuestos que el texto describe.` |
| **dice** | `Las tres cosas del texto identificadas y encargadas como el plan del despido.` |
| **por que** | `L169` y `L171` **describen** dos errores de empresa y **no encargan situar ninguna**. Situar una empresa no deja fichero |
| **lo que NO se toco** | **los 11 pasos**, contados del fichero antes y despues: `11` y `11`. **La mitad retirada NO es un paso, asi que esta correccion no mueve `PASOS INVENTADOS`**, y lo digo para que nadie la busque alli |
| **el texto viejo** | **no se borra**: queda escrito literal dentro del `resumen_teorico` del propio fichero, con su cita a la `ACTA 21` `4.4` |

**CORRECCION 2, `reconocer_excelencia_trayectoria_gradual.json`, la razon del par en su
`resumen_teorico`** (`ACTA 21` `4.6`):

| | |
|---|---|
| **decia** | `Su paso 2 nombra las vias en una linea (...) y este nodo despliega dos de ellas en trece pasos que la madre no tiene.` |
| **dice** | `la madre nombra las vias Y DESPLIEGA LA DEL EXPERTO DE REFERENCIA EN CUATRO PASOS, que son sus pasos 7, 8, 9 y 10; la hija anade la via del agradecimiento entera, con la distincion escrita frente al elogio, y el plazo de preparacion de la clase que la madre no tiene; y el acto del honor y no la obligacion es COMPARTIDO por las dos y no es lo que separa el par.` |
| **por que** | la razon vieja decia que la madre *nombra las vias en una linea*, y el auditor la leyo entera y **no es cierto** |
| **lo que NO cambia** | **la clase**: sigue `CONTINUA` con arista, `--paso 2` de la madre. Y **los 13 pasos**, contados antes y despues: `13` y `13` |
| **el texto viejo** | **no se borra**: la razon vieja queda escrita literal al lado de la nueva dentro del mismo campo |
| **por que era duradera** | porque **esa razon se cablea al grafo el dia de la insercion**, y desde ese minuto vive en sede duradera |

### P.3.g. LA FRONTERA DE `cap_10`, RECOMPUTADA ENTERA CON LA PIEZA 14 DENTRO Y CERRADA CONTRA EL CUERPO

*No copio la tabla de mi vuelta 21: la pieza 14 saca TRES lineas del resto, asi que la frontera se
vuelve a cerrar contra el cuerpo o no se publica (`ACTA 18` `7.5` orden 1). Salida de
`python .t1_v22/frontera_cap10.py`, guardada en `.t1_v22/salida_frontera_cap10.txt`.*

    tramos que dan nodo                    : 9
    tramos de resto                        : 6
    lineas con contenido de L8 en adelante : 128
    lineas NO cubiertas                    : 0  []
    SOLAPES                                : 0  []
    suma de las filas                      : 8976 palabras
    cuerpo medido aparte (sed 8,$ | wc -w) : 8976 palabras
    IGUALES                                : True
    la pieza 14, sus tres lineas           : 254 palabras

| tramo | palabras | nodos | que es | la salida, pegada |
|---|---:|---:|---|---|
| `L19` | 99 | **0** | pieza 14, tramo a: con quien y para que | `19:AS DESCRIBED IN Chapter Three, all people have their own growth trajectories, ` |
| `L21` | 82 | **0** | pieza 14, tramo b: cuando y donde caben | `21:Once you've gotten the hang of these conversations, you'll look forward to the` |
| `L43` | 73 | **1** | pieza 14, tramo c: la cadencia y el encargo a los jefes | `43:Realizing he'd come up with a good methodology for having career conversations` |
| `L47 a L87` | 1862 | **3** | las tres conversaciones de carrera | `47:Conversation one: life story` |
| `L93 a L125` | 1095 | **1** | el plan anual de gestion del crecimiento | `93:GROWTH MANAGEMENT` |
| `L127 a L163` | 1501 | **1** | el proceso de contratacion, con el acto de L129 dentro | `127:HIRING: YOUR MENTALITY AND YOUR PROCESS` |
| `L165 a L201` | 1372 | **5** | despedir: cabeza, tres partes y coda | `165:FIRING` |
| `L203 a L223` | 638 | **1** | la calibracion de ascensos, con el caso de Google dentro | `203:PROMOTIONS` |
| `L225 a L251` | 568 | **2** | recompensar sin ascender | `225:REWARD YOUR ROCK STARS` |
| | **7290** | **14** | **los tramos que dan nodo** | |

**LA FILA DE RESTO, NOMBRADA LINEA A LINEA** (`ACTA 19` `7.4` ORDEN A, que es la orden que cazo esta
misma pieza). **La fila de 1.641 palabras que decia *entrada, rotulos y el caso* ya no existe: se
parte en cuatro y cada trozo dice que es.**

| tramo de resto | palabras | nodos | que es, nombrado |
|---|---:|---:|---|
| `L9 a L18` | 206 | **0** | subtitulo, resumen del cap. 3 y los dos rotulos de seccion |
| `L20` | 0 | **0** | linea en blanco entre L19 y L21 |
| `L22 a L42` | 1136 | **0** | EL CASO DE RUSS LARAWAY entero: Google, Todd, Sarah y el plan de Sarah |
| `L44 a L45` | 45 | **0** | linea en blanco y el cierre del caso: la encuesta interna de Google |
| `L88 a L92` | 101 | **0** | cierre de seccion que remite a una web y a un libro de otro |
| `L253 a L263` | 198 | **0** | el cuadro que no esta en el recorte, el resumen y la cabecera del cap siguiente |
| | **1686** | **0** | |

**LOS CATORCE CANDIDATOS DE `cap_10`, CON SUS PASOS CONTADOS DEL FICHERO:**

| # | id | pasos |
|---:|---|---:|
| 1 | `desplegar_tres_conversaciones_carrera` | **11** |
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
| | **catorce candidatos** | **205** |

> ### **`cap_10` QUEDA CERRADO EN `14` PIEZAS Y `205` PASOS, CON LA FRONTERA AL DIGITO Y LA FILA DE RESIDUO EN CERO. LA ADJUDICACION `4.1` DE LA `ACTA 21` ESTA CUMPLIDA.**

> **TAREA 2 CERRADA.** La pieza 14 escrita y por la aduana al primer intento, sus tres aristas
> `D.37` declaradas enteras con su paso citado, las dos correcciones de fichero hechas sin borrar el
> texto viejo y sin tocar ni un paso, y la frontera de `cap_10` recerrada contra el cuerpo en 14.
