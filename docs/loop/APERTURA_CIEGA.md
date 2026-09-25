# APERTURA CIEGA DE LA VUELTA 69, lote 7 (`grove_high_output`), **CLASE SANEAMIENTO**

*Auditor `claude-opus-5-5`, fase ciega, 25 sep 2026, la que el arnes numera `VUELTA 5` en la corrida que arranco el
23 a las `21:50`. Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de
`.v69aud/`, escrito y corrido en esta fase; cada bloque `$` lo pega `.v69aud/generar_apertura.py` corriendo el
comando en el momento de escribirla. **No hay ninguna tabla en esta pagina**, a proposito, como en la `66` y la `68`.
**En esta fase no corro `git`** (ni `log`, ni `diff`, ni `status`): mido el arbol por sus ficheros, sus huellas y sus
fechas, y donde eso no alcanza lo digo como limitacion.*

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: 1c91f518d8ca311aa937caa91c8f8ec27366fbde

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su
reporte de la `69`** (`ACTA 67` `67.11`: *el reporte de la `69`, con `.v64ext/pegado64.py` y
`.v64aud/normal/bloques_mudos.py`, los dos con la cabecera del tramo cambiada a la `69`*), y el reporte **no esta
en el arbol**: el arnes lo retiro para esta fase (`D.34.2`) y no lo he recuperado por ninguna via. **Se mide en mi
turno normal**, con los dos instrumentos sacados otra vez de los originales. Lo que si esta en mi mano lo cumplo en
mi pagina: cada bloque `$` lleva la salida del comando que abre, y nada mas.

    $ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    ls: cannot access 'docs/loop/ultimo_extractor.json': No such file or directory
    ls: cannot access 'docs/loop/ultimo_auditor.json': No such file or directory
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory
    $ grep -n "VUELTA 5 : APERTURA CIEGA" docs/loop/loop.log | tail -1
    6255:[2026-09-25 02:24:24] VUELTA 5 : APERTURA CIEGA (claude-opus-5-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 67` `67.11`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no enseña `previos` ni `siguientes`, y **todos los bloques de pasos de esta
pagina lo corren** (secciones `3`, `4` y `5`). Ningun instrumento mio de esta fase nombra esas claves:

    $ grep -l -E "previos|siguientes" .v69aud/*.py | wc -l
    0
    $ cat .v69aud/pasos_conjunta.txt | grep -c -E "previos|siguientes"
    0

**LECTURA:** no vi ninguna clave de relacion de un nodo tocado en esta fase. `.v69aud/pasos_conjunta.txt` es la
salida de `pasos_ciego.py` para los diez nodos que leo aqui, guardada para mi turno normal. Y el cumplimiento de la
pagina entera lo mide un `grep` sobre ella antes de cerrarla (seccion `9`).

HEREDADO 3: CUMPLIDO. **`R7`, mio** (`ACTA 67` `67.11`): toda linea de esta pagina que reparte un total en clases la
imprime un instrumento que cuenta **todas** las clases con el mismo predicado y **dice su `suma`**. Los instrumentos que
copie de la `68` y no la decian los he copiado a `.v69aud/` con la suma dentro (`cruce_clases.py`,
`contar_fidelidad.py`, `restricciones_orden.py`), y los nuevos la traen desde que nacen (`poblacion.py`,
`cabeza_d68_7.py`, `d053_mitades.py`, `d68_15.py`, `aristas_70.py`). **Medido sobre la pagina misma** en la seccion `9`,
con `.v69aud/r7_pagina.py`.

**LA HUELLA** es la que el prompt me entrega, comprobada solo contra el propio prompt: **no la recomputo**, porque
`forja.py herencia` lee en esta fase un fichero retirado (`d146`).

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los cuatro commits del extractor, y dos
traen sus conclusiones de esta vuelta**, que lei antes de leer nada:

- `3721928` *Vuelta 69, T1 y T2: los registros de la ACTA 67 y la relectura conjunta (D68.7 a SANO y NO SOSTENGO en
  los ocho, D68.15 a NO en espera; 118 lineas sin hueco, orden en cero, 7 aristas esperadas en la 70)*;
- `4ec8c16` *Vuelta 69, T3 a T5: d053 decidida sin partir la ficha (la mitad de L37 no pasa 9.1 sola), d056 pagada
  citando el recorrido de la 68 (118 de 118), saneamiento declarado, 7 aristas esperadas en la 70 y las 20 huellas
  iguales, censo igual en el dato (390, 904, 1, 47, 45), guardas y cierre estricto en verde*;
- y `0715b58` y `4b17f8b`, sin cifras.

**Y al leer las tres deudas de esta vuelta en `docs/loop/DEUDA.jsonl`** para copiar su letra, vi que `d053` y `d056`
tienen **cada una una segunda linea con `vuelta` `69` y una clave `como`**, que es la forma de un pago; **su `como` no lo
imprimi**. Tambien lei la cola de `docs/loop/loop.log`, que no se retira. Es el mismo hueco de `d146` que declararon las
aperturas de la `65` a la `68`, y no lo arreglo yo (`D.45`).

**LO QUE ESO LE HACE A ESTA PAGINA, SIN REBAJARLO:**

1. **`D68.7` y `D68.15` no las decido hoy: las decidi y las selle en la `68`** (`.v68aud/mis_clases.tsv` y
   `.v68aud/aristas_lectura.tsv`, que no toco, y mi caso en la `ACTA 67` `67.4.d`), antes de que existiera su
   relectura. Aqui las releo con los pasos delante y digo si las mantengo; **la coincidencia con su asunto la digo
   como coincidencia y no como fuente**.
2. **`d053` SI la leo hoy por primera vez con la vara `9.1`, y la leo despues de haber visto su decision en el asunto
   de `4ec8c16`.** Esa lectura **no es ciega** y no la presento como tal: escribo la linea de cada lado para que se
   pueda juzgar sin mi, y **si coincide con la suya no cuenta como una segunda lectura independiente**.
3. **Ninguna cifra de esta pagina sale de esos asuntos**; todas salen de un instrumento corrido en esta fase.
4. **No he abierto nada de `.v68ext/` ni de `.v69ext/`**, ni `bitacora/VEREDICTOS.jsonl` por dentro: de ella solo cuento
   lineas.

## 2. **EL ALCANCE, Y EL DATO QUE NO SE MOVIO**

La vuelta es de **saneamiento sin insercion** (encargo de la `69`, seccion `0`): la relectura conjunta de `D68.7` y
`D68.15`, `d053` (se parte o no `fijar_duracion_lugar_reunion_individual`) y `d056` (la cola de lectura de la tanda
`52`). **Lo que puede mover en el dato es una sola cosa: si parte la ficha, la bandeja sube a `48`.**

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        390 dataset/nodos.jsonl
        904 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1295 total
    $ ls cuarentena/grove_high_output/*.json | wc -l
    47
    $ ls cuarentena/_insertados/grove_high_output/*.json | wc -l
    45
    $ ls -A procesos/ | wc -l
    0
    $ python forja.py gate | head -2
    GATE VERDE.
      nodos verificados: 390

**Y sin `git`, lo que cambio desde mi barrido de la `68`**, por dos instrumentos: las `50` huellas que tome al lanzarlo
(la bandeja de Grove, las dos filas de `cap_04` en `_insertados` y el grafo), y **cualquier fichero de `cuarentena/`,
`dataset/`, `bitacora/`, `censos/` o `config/` con fecha posterior a ese fichero de huellas**:

    $ ls -l --time-style=full-iso .v68aud/huellas_al_barrer.txt | awk '{print $6, $7, $9}'
    2026-09-24 21:59:13.578070900 .v68aud/huellas_al_barrer.txt
    $ wc -l < .v68aud/huellas_al_barrer.txt
    50
    $ sha1sum -c --quiet .v68aud/huellas_al_barrer.txt && echo "bandeja de grove, las dos filas y el grafo: mismas huellas que al barrer en la 68"
    bandeja de grove, las dos filas y el grafo: mismas huellas que al barrer en la 68
    $ find cuarentena dataset bitacora censos config -type f -newer .v68aud/huellas_al_barrer.txt | wc -l
    0
    $ python .v69aud/poblacion.py
    poblacion: 479 | por sede: {'grafo': 390, 'bandeja': 89} | suma: 479

**LECTURA:** `390`, `904`, `1`, `47` y `45`, **los de mi `ACTA 67` `67.1`**; el grafo y las `47` fichas de Grove son
byte a byte las que barri, **ningun fichero del dato ni de ninguna bandeja tiene fecha de escritura posterior a mis
huellas**, y la poblacion del
barrido es hoy `479`, la de la `68`. **La vuelta no partio la ficha** (la bandeja sigue en `47` y ninguna ficha de Grove
cambio), **no escribio en la bitacora** y **no toco ninguna otra bandeja**. `procesos/` esta vacio. **Coincide con el
censo del asunto de `4ec8c16`, y lo digo como coincidencia.** Lo que estos instrumentos NO ven: lo que la vuelta
cambio en `.v68ext/` y `.v69ext/`, que no abro.

## 3. **`D68.7`: LA CABEZA DE LAS TRES CLASES, RELEIDA** (`6.1`, y solo la vara `6.1`)

Los pasos de la cabeza y de los ocho que el extractor le colgo en la `68` (los cuatro pares que el barrido levanta:
`cubrir_indicadores`, `fijar_duracion`, `fijar_frecuencia`, `preparar_guion`; y las cuatro aristas por lectura:
`acumular`, `alentar`, `facilitar`, `programar`), por `pasos_ciego.py` (`R6`):

    $ python .v67aud/normal/pasos_ciego.py usar_tres_clases_reunion_proceso fijar_frecuencia_reunion_individual_madurez_tarea fijar_duracion_lugar_reunion_individual preparar_guion_reunion_individual_subordinado cubrir_indicadores_problemas_reunion_individual facilitar_expresion_subordinado_pregunta_mas acumular_asuntos_importantes_fichero_espera alentar_asuntos_corazon_vigilar_final_reunion programar_reunion_individual_cadena
    ===== usar_tres_clases_reunion_proceso | cuarentena\grove_high_output\usar_tres_clases_reunion_proceso.json
      titulo: Usar las tres clases de reunion de proceso que el libro cuenta y nombra: el uno a uno, la reunion de personal y la revision de operaciones
      fuente: ['grove_high_output']
      cond: Cuando vas a montar las reuniones de proceso de tu organizacion y necesitas saber cuantas clases hay y cuales son, antes de entrar en como se lleva cada una.
      P1. Cuenta con que las reuniones de proceso que se usan son de tres clases, y con que el libro las nombra una a una.
      P2. Primera clase: el uno a uno.
      P3. Segunda clase: la reunion de personal.
      P4. Tercera clase: la revision de operaciones.
    ===== fijar_frecuencia_reunion_individual_madurez_tarea | cuarentena\grove_high_output\fijar_frecuencia_reunion_individual_madurez_tarea.json
      titulo: Fijar cada cuanto tienes la reunion individual con cada subordinado segun su madurez relevante para la tarea, y ajustarla por lo deprisa que cambia su area
      fuente: ['grove_high_output']
      cond: Cuando tienes que decidir cada cuanto te reunes a solas con cada uno de los profesionales que te reportan, y no sabes con que criterio separar a unos de otros.
      P1. Decide cada cuanto necesita reunion individual cada persona, en vez de poner la misma frecuencia para todas.
      P2. Contesta a esa pregunta con la madurez relevante para el puesto o para la tarea de cada uno de tus subordinados, que es la respuesta que el libro da.
      P3. Mide esa madurez por cuanta experiencia tiene ese subordinado con la tarea concreta que tiene entre manos.
      P4. No la confundas con la experiencia que tiene en general ni con lo mayor que sea.
      P5. Cuenta con que el estilo de mando mas eficaz en un caso concreto va de la supervision muy estrecha a la muy suelta a medida que sube la madurez de tarea del subordinado.
      P6. Ten reuniones individuales con frecuencia, por ejemplo una vez por semana, con el subordinado que es inexperto en una situacion concreta.
      P7. Tenlas con menos frecuencia, quiza una vez cada pocas semanas, con el veterano experimentado.
      P8. Ten en cuenta ademas una segunda consideracion: lo deprisa que cambian las cosas en el area del puesto.
      P9. Cuenta con que en un area de ritmo muy rapido, y el libro pone como ejemplo la de marketing, el supervisor necesita reuniones individuales frecuentes para seguir al dia de lo que pasa.
      P10. Cuenta con que en un entorno mas tranquilo, y el libro pone como ejemplo el de investigacion, pueden bastar reuniones menos frecuentes para un mismo nivel de madurez relevante para la tarea.
    ===== fijar_duracion_lugar_reunion_individual | cuarentena\grove_high_output\fijar_duracion_lugar_reunion_individual.json
      titulo: Fijar cuanto dura la reunion individual y donde se tiene: una hora como minimo, y en el area de trabajo del subordinado o cerca de ella
      fuente: ['grove_high_output']
      cond: Cuando vas a programar la reunion individual con un subordinado y tienes que poner en el calendario cuanto va a durar y en que sitio se tiene.
      P1. Cuenta con que a cuanto tiene que durar no hay de verdad una respuesta, pero con que el subordinado tiene que sentir que hay tiempo suficiente para sacar los asuntos espinosos y meterse en ellos.
      P2. Comprueba ese criterio poniendote en su sitio: si tuvieras un problema grande al que quisieras dar vueltas con tu supervisor, que es la persona cuyo interes profesional en el asunto solo va por detras del tuyo, no querrias sacarlo en una reunion programada para durar solo quince minutos.
      P3. Haz que la reunion individual dure una hora como minimo.
      P4. Cuenta con que cualquier cosa menos que eso tiende a hacer que el subordinado se limite a las cosas sencillas que se despachan deprisa.
      P5. Ten la reunion en el area de trabajo del subordinado o cerca de ella siempre que se pueda, y no en la del supervisor ni en otro sitio.
      P6. Aprovecha que un supervisor aprende mucho con solo ir al despacho de su subordinado.
      P7. Mira si esta organizado o no.
      P8. Mira si tiene que pasar tiempo una y otra vez buscando un documento que quiere.
      P9. Mira si lo interrumpen todo el rato, o si no lo interrumpen nunca.
      P10. Mira en general como se enfrenta el subordinado a su trabajo.
    ===== preparar_guion_reunion_individual_subordinado | cuarentena\grove_high_output\preparar_guion_reunion_individual_subordinado.json
      titulo: Tratar la reunion individual como reunion del subordinado y hacer que sea el quien prepare el guion y pasee al supervisor por el material
      fuente: ['grove_high_output']
      cond: Cuando ya tienes programada la reunion individual y hay que decidir de quien es la reunion y quien la prepara.
      P1. Ten la reunion individual por reunion del subordinado, con su agenda y su tono puestos por el.
      P2. Cuenta con la razon que lo sostiene: alguien tiene que preparar la reunion, y el supervisor que tiene ocho subordinados tendria que prepararla ocho veces mientras que el subordinado solo una.
      P3. Pidele por eso al subordinado que prepare un guion.
      P4. Cuenta con lo que ese guion consigue en el, que es lo que lo hace muy importante: le obliga a pensar de antemano todos los asuntos y puntos que piensa plantear.
      P5. Cuenta con lo que consigue en ti: con un guion, el supervisor sabe desde el principio que se va a tratar y puede por tanto ayudar a marcar el ritmo de la reunion segun lo sustancioso de cada punto de la agenda.
      P6. Aprovecha que el guion da ademas un armazon para la informacion de apoyo, que el subordinado tiene que preparar por adelantado.
      P7. Haz que el subordinado pasee despues al supervisor por todo el material.
    ===== cubrir_indicadores_problemas_reunion_individual | cuarentena\grove_high_output\cubrir_indicadores_problemas_reunion_individual.json
      titulo: Cubrir en la reunion individual los indicadores del subordinado, lo ocurrido desde la anterior y el problema potencial, con el criterio de que sean los asuntos que le preocupan
      fuente: ['grove_high_output']
      cond: Cuando estas dentro de la reunion individual, o preparando su guion, y hay que decidir que asuntos se tratan en ella.
      P1. Empieza por las cifras de rendimiento, o sea los indicadores que usa el subordinado, como los ritmos de pedidos entrantes, la produccion o el estado de los proyectos.
      P2. Pon el enfasis en los indicadores que avisan de un problema.
      P3. Cubre ademas cualquier cosa importante que haya ocurrido desde la reunion anterior.
      P4. Trata dentro de eso los problemas de contratacion del momento.
      P5. Trata los problemas de personas en general.
      P6. Trata los problemas de organizacion y los planes futuros.
      P7. Y trata, muy muy importante, los problemas potenciales.
      P8. Cuenta con que aunque un problema no sea tangible, aunque sea solo una intuicion de que algo va mal, el subordinado se lo debe a su supervisor y tiene que decirselo, porque eso dispara una mirada dentro de la caja negra de la organizacion.
      P9. Rige todo lo anterior por el criterio mas importante de los asuntos que se hablan: que sean cuestiones que preocupan al subordinado y le dan la lata.
      P10. Cuenta con que esas cuestiones suelen ser oscuras y tardan en aflorar, en considerarse y en resolverse.
    ===== facilitar_expresion_subordinado_pregunta_mas | cuarentena\grove_high_output\facilitar_expresion_subordinado_pregunta_mas.json
      titulo: Hacer del supervisor en la reunion individual el que facilita, aprende y orienta, y sacar lo que falta aplicando el principio de preguntar una vez mas
      fuente: ['grove_high_output']
      cond: Cuando estas dentro de la reunion individual como supervisor y hay que decidir que papel juegas tu en ella y como sacas lo que el subordinado todavia no ha dicho.
      P1. Facilita que el subordinado exprese lo que esta pasando y lo que le molesta.
      P2. Ponte en la reunion para aprender y para orientar.
      P3. Cuenta con como resume Drucker el trabajo del supervisor aqui: los que usan bien el tiempo entre los mandos no hablan con sus subordinados de los problemas de ellos mismos, sino que saben como hacer que los subordinados hablen de los suyos.
      P4. Aplica para conseguirlo el principio de direccion didactica de Grove, que es preguntar una vez mas.
      P5. Cuando creas que el subordinado ha dicho ya todo lo que queria sobre un asunto, hazle otra pregunta.
      P6. Manten el flujo de ideas pinchando al subordinado con preguntas hasta que los dos os deis por satisfechos de haber llegado al fondo de un problema.
    ===== acumular_asuntos_importantes_fichero_espera | cuarentena\grove_high_output\acumular_asuntos_importantes_fichero_espera.json
      titulo: Abrir un fichero de espera compartido donde las dos partes acumulan lo importante que no es del todo urgente, para tratarlo en la reunion siguiente
      fuente: ['grove_high_output']
      cond: Cuando entre una reunion individual y la siguiente aparecen asuntos importantes que no son del todo urgentes y hay que decidir si se interrumpe al otro o se esperan.
      P1. Usa un fichero de espera compartido por el supervisor y el subordinado.
      P2. Acumula ahi los asuntos importantes pero no del todo urgentes, para tratarlos en la reunion siguiente.
      P3. Cuenta con que esa clase de fichero aplica el principio de produccion del agrupamiento.
      P4. Cuenta con que el ahorro de tiempo para los dos implicados sale de reducir al minimo la necesidad de contacto improvisado, como las llamadas de telefono o las visitas sin avisar, que son las interrupciones que el libro considero antes.
    ===== alentar_asuntos_corazon_vigilar_final_reunion | cuarentena\grove_high_output\alentar_asuntos_corazon_vigilar_final_reunion.json
      titulo: Alentar en la reunion individual los asuntos de corazon a corazon con las tres preguntas del libro, y ponerse en guardia contra el que se suelta cerca del final
      fuente: ['grove_high_output']
      cond: Cuando la reunion individual esta en marcha y hay que decidir si se abre la puerta a los problemas sutiles y profundos del subordinado, y como se gobierna el momento en que salen.
      P1. Alienta que en la reunion individual se hablen los asuntos de corazon a corazon.
      P2. Cuenta con la razon que lo sostiene: es el foro perfecto para llegar a los problemas sutiles y profundos del trabajo que afectan al subordinado.
      P3. Preguntale si esta satisfecho con su propio rendimiento.
      P4. Preguntale si alguna frustracion o algun obstaculo le esta carcomiendo.
      P5. Preguntale si tiene dudas sobre adonde va.
      P6. Ponte en guardia contra el asunto de corazon a corazon sacado en un momento inoportuno.
      P7. Cuenta con que la mayoria de las veces esos llegan cerca del final de la reunion.
      P8. Cuenta con lo que pasa si lo dejas correr: el subordinado puede decirte algo como que no esta contento y que lleva tiempo buscando trabajo fuera, y dejarte solo cinco minutos para lidiar con ello.
    ===== programar_reunion_individual_cadena | cuarentena\grove_high_output\programar_reunion_individual_cadena.json
      titulo: Programar la reunion individual en cadena, fijando la siguiente en el momento en que termina la que se esta teniendo
      fuente: ['grove_high_output']
      cond: Cuando hay que poner en el calendario la reunion individual siguiente y se elige entre un horario fijo y fijarla al terminar la que se esta teniendo.
      P1. Programa las reuniones individuales en cadena.
      P2. Fija la siguiente en el momento en que termina la reunion que se esta teniendo.
      P3. Cuenta con lo que eso consigue: asi se pueden tener en cuenta los demas compromisos y se evitan las cancelaciones.
      P4. Cuenta con el caso contrario que el libro pone: si el supervisor usa un horario fijo para la reunion individual, por ejemplo la manana de cada segundo miercoles, y las vacaciones del subordinado caen en esa fecha, la reunion no se va a celebrar.
      P5. Cuenta con que programando en cadena eso se evita facilmente.

**Lo que la cabeza produce y de donde parten los ocho, medido:**

    $ python .v69aud/cabeza_d68_7.py
    cabeza: pasos 4 | por forma: {'Cuenta con': 1, 'rotulo de clase': 3} | suma: 4
    pasos de la cabeza que dicen uno a uno: [2]
      fijar_frecuencia_reunion_individual_madurez_tarea    | palabras de la cabeza: -          | dice reunion individual: False
      fijar_duracion_lugar_reunion_individual              | palabras de la cabeza: -          | dice reunion individual: True
      preparar_guion_reunion_individual_subordinado        | palabras de la cabeza: -          | dice reunion individual: True
      cubrir_indicadores_problemas_reunion_individual      | palabras de la cabeza: -          | dice reunion individual: True
      facilitar_expresion_subordinado_pregunta_mas         | palabras de la cabeza: -          | dice reunion individual: True
      acumular_asuntos_importantes_fichero_espera          | palabras de la cabeza: -          | dice reunion individual: True
      alentar_asuntos_corazon_vigilar_final_reunion        | palabras de la cabeza: -          | dice reunion individual: True
      programar_reunion_individual_cadena                  | palabras de la cabeza: -          | dice reunion individual: True
    hijos: 8 | por condicion: {'sin palabra del producto de la cabeza': 8} | suma: 8

**Y los pares que mi barrido de la `68` levanta con la cabeza, con mi clase sellada:**

    $ python .v69aud/cruce_clases.py | sed -n '/cabeza/,$p'
    pares con la cabeza usar_tres_clases_reunion_proceso: 5 | por clase: {'SANO': 5} | suma: 5
      SANO      cubrir_indicadores_problemas_reunion_individual
      SANO      fijar_duracion_lugar_reunion_individual
      SANO      fijar_frecuencia_reunion_individual_madurez_tarea
      SANO      infundir_regularidad_reunion_proceso
      SANO      preparar_guion_reunion_individual_subordinado

**LECTURA, Y LA MANTENGO: `SANO` EN LOS CUATRO PARES Y `NO` EN LAS CUATRO ARISTAS.**

*(El bloque de arriba trae **cinco** pares con la cabeza: el quinto, `infundir_regularidad_reunion_proceso`, **no esta en
`D68.7`**, que son los cuatro del barrido mas las cuatro aristas que nombra el encargo.)*

- **La cabeza no manda nada sobre el uno a uno.** De sus cuatro pasos, uno es un *Cuenta con* y tres son rotulos
  (*Primera clase: el uno a uno*); su producto es **saber que hay tres clases y como se llaman**, que es lo que dice
  `cap_05` L23 (*At Intel we use three kinds of process-oriented meetings: the one-on-one, the staff meeting, and the
  operation review*). Su propia condicion lo dice: *antes de entrar en como se lleva cada una*.
- **Ninguna de las ocho condiciones parte de ese producto.** Ninguna trae una palabra de el (`clase`, `tres`,
  `proceso`), y cada una arranca de su propia situacion con el uno a uno (fijarlo, prepararlo, llevarlo, seguirlo) y contesta **su** pregunta del libro:
  L33 (*How often*), L37 y L39 (*How long*, *Where*), L41 (*the subordinate's meeting*), L43 (*What should be covered*),
  L45 (*What is the role of the supervisor*), L51 (*hold file*), L53 (*heart-to-heart*), L57 (*rolling basis*).
- **Nombrar no es procedimentar** (`6.1`): el unico hilo es el rotulo del paso `2`. Y **el encabezado `ONE-ON-ONES`
  (L25) es formato**: dice donde estan los ocho en el libro, no que continuen el trabajo de la cabeza (`6.2`, `P.17`).
- **La contraria, escrita para que se vea:** los ocho son aspectos del uno a uno y la cabeza es el unico nodo que lo
  nombra como pieza. Pero colgarlos de ella **se salta el escalon que falta**: la parte *el uno a uno* no existe como
  nodo (`D.37`, mi `APERTURA_CIEGA.md` de la `68` seccion `7`), y la cabeza produce un nombre, no el uno a uno.

**LO QUE MI LECTURA ESPERA DE SU RELECTURA** (sin haberla abierto): las `8` lineas `CONTINUA` con
`madre=usar_tres_clases_reunion_proceso` pasadas a `SANO` y las cuatro filas `SOSTENGO` de la cabeza pasadas a `NO
SOSTENGO`, por correccion declarada y con la vieja encima; **ninguna ficha cambia**. **Coincide con el asunto de
`3721928`, y lo digo como coincidencia**: el texto de sus lineas lo leo en mi turno normal.

## 4. **`D68.15`: `elegir_estilo` Y `fijar_frecuencia`, RELEIDA**

    $ python .v67aud/normal/pasos_ciego.py elegir_estilo_direccion_madurez_relevante_tarea
    ===== elegir_estilo_direccion_madurez_relevante_tarea | cuarentena\grove_high_output\elegir_estilo_direccion_madurez_relevante_tarea.json
      titulo: Elegir el estilo de direccion de un subordinado segun su madurez relevante para la tarea concreta: estructurado si es baja, comunicador si es media, minimo si es alta, y siempre con vigilancia para no abandonar
      fuente: ['grove_high_output']
      cond: Cuando tienes que decidir con que estilo dirigir a un subordinado en una tarea concreta y no sabes si conviene darle instrucciones detalladas, acompanarlo con comunicacion y apoyo, o dejarlo actuar con poca supervision.
      P1. Evalua la madurez relevante para la tarea (TRM) de tu subordinado: la combinacion de su orientacion al logro, su disposicion a asumir responsabilidad, su educacion, su formacion y su experiencia.
      P2. Trata esa TRM como especifica de la tarea concreta y no como la madurez general de la persona: puede ser alta en un puesto y baja en otro.
      P3. Cuenta con que la TRM de una persona puede caer si el ritmo del puesto se acelera o si el puesto cambia de golpe, aunque antes fuera alta para ese nivel de complejidad, incertidumbre y ambiguedad.
      P4. Si la TRM es baja, usa un estilo estructurado y orientado a la tarea: dile al subordinado que hay que hacer, cuando y como, con instrucciones precisas y detalladas.
      P5. Si la TRM del subordinado crece, mueve el estilo hacia uno mas dado a la comunicacion, el apoyo emocional y el animo, prestando mas atencion al subordinado como individuo que a la tarea misma.
      P6. Si la TRM se vuelve todavia mayor, mantén tu involucramiento al minimo y limitate sobre todo a asegurar que los objetivos hacia los que trabaja el subordinado esten acordados mutuamente.
      P7. Sea cual sea la TRM, vigila siempre el trabajo del subordinado lo bastante de cerca para evitar sorpresas: la presencia o ausencia de esa vigilancia es la diferencia entre delegar una tarea y abandonarla.
      P8. No juzgues un estilo estructurado como menos valioso que uno orientado a la comunicacion, ni dejes que lo que te parezca mas simpatico decida tu eleccion: lo que importa es cual de los dos es mas eficaz.
    $ python .v69aud/d68_15.py
    pasos con estilo  : [5] | por forma: {'Cuenta con': 1} | suma: 1
    pasos con madurez : [2, 3, 5, 10] | por forma: {'otro imperativo': 2, 'Cuenta con': 2} | suma: 4

**LECTURA, Y LA MANTENGO: `NO`.** El producto de la madre es **un estilo elegido para un subordinado** (sus pasos `4` a
`6`: estructurado, comunicador, minimo). En `fijar_frecuencia` la palabra *estilo* sale **una vez, en un *Cuenta con***
(paso `5`), y ningun paso usa un estilo elegido: la madurez que usa **la mide el mismo** (paso `3`, *por cuanta
experiencia tiene con la tarea concreta*) y de ella saca la frecuencia (pasos `6` y `7`). *As we will see later* (L33)
es una remision del libro, y una remision es metadato (`6.2`). **No toca a la `70`**: la madre es de `cap_13` y no entra
antes que el hijo, y `d170` guarda las dos lecturas para la vuelta que la inserte. **Si el la cambio a `NO` en espera,
como dice el asunto de `3721928`, coincide.**

## 5. **`d053`: SE PARTE O NO `fijar_duracion_lugar_reunion_individual`** (`EXTRACTOR.md` `9`, `9.1`)

**Esta lectura NO es ciega** (seccion `1`, punto `2`). La deuda pone el corte entre el paso `4` y el paso `5`; sus pasos
estan arriba, en la seccion `3`. Cada mitad contra su linea:

    $ python .v69aud/d053_mitades.py
    pasos en la ficha: 10
    mitad duracion: pasos [1, 2, 3, 4] | por forma: {'Cuenta con': 2, 'otro imperativo': 2} | suma: 4
      L37: 628 caracteres | signos de interrogacion: 2 | empieza: How long should a one-on-one meeting last? There really is n
      P2. Comprueba ese criterio poniendote en su sitio: si tuvieras un problema grande al que quisieras dar vueltas con tu supervisor, que es la persona cuyo interes profesional en el asunto solo va por detras del tuyo, no querrias sacarlo en una reunion programada para durar solo quince minutos.
      P3. Haz que la reunion individual dure una hora como minimo.
    mitad lugar: pasos [5, 6, 7, 8, 9, 10] | por forma: {'otro imperativo': 2, 'Mira': 4} | suma: 6
      L39: 475 caracteres | signos de interrogacion: 7 | empieza: Where should a one-on-one take place? In the supervisor’s of
      P5. Ten la reunion en el area de trabajo del subordinado o cerca de ella siempre que se pueda, y no en la del supervisor ni en otro sitio.
      P6. Aprovecha que un supervisor aprende mucho con solo ir al despacho de su subordinado.

**LECTURA: NO SE PARTE**, con `DUDA` escrita.

- **La mitad del lugar (L39) pasaria sola**: el libro pone **su propio inventario de objetos** que mirar en el despacho
  del subordinado (*Is he organized or not? Does he repeatedly have to spend time looking for a document ...? Does he
  get interrupted all the time? Never? ... how does the subordinate approach his work?*), y sus pasos `7` a `10` lo
  transcriben uno a uno. Es la cara positiva de `9.1`.
- **La mitad de la duracion (L37) no pasa sola**: lo que el libro pone es **un criterio con adjetivo de adecuacion**
  (*the subordinate must feel that there is **enough** time*), **una prueba de pensamiento** (el problema grande en
  quince minutos) y **una cifra** (*an hour at a minimum*). De sus cuatro pasos, dos son *Cuenta con*, uno es la prueba y
  **uno solo manda algo** (paso `3`, *dure una hora como minimo*). **No hay inventario de medios, etapas ni objetos**
  (restriccion `1` de `9.1`): sola seria **una linea con un umbral**, no un procedimiento (`9`, *un procedimiento real
  por nodo*), y un nodo de un paso es una advertencia con numero.
- **Y juntas son un solo procedimiento**: su condicion es una (*programar la reunion individual ... cuanto va a durar y
  en que sitio*), las dos son las dos casillas que se rellenan al ponerla en el calendario, y ninguna de las dos usa el
  producto de la otra, asi que tampoco hay madre e hija dentro.
- **LA DUDA, la contraria:** L37 si pone una cifra del autor y un criterio que se comprueba, y se podria leer como un
  procedimiento corto de *decidir la duracion*. **No la sigo** porque la cifra y el criterio son un solo acto (fijarla
  en una hora), y el paso `2` es la razon del paso `3`, no otro acto.

**Si no se parte, nada cambia en la bandeja, en el barrido ni en la fidelidad**, y la seccion `2` mide que no se partio.
**Coincide con el asunto de `4ec8c16`**, y por el punto `2` de la seccion `1` **no la cuento como confirmacion**.

## 6. **`d056`: LA COLA DE LECTURA DE LA TANDA `52`**

La deuda se cobra *recorriendo la cola sobre la poblacion de ese dia y veredictando lo que falte*. **Mi barrido de la
`68`** (sobre la poblacion de entonces, `479`) **contra mis clases selladas**, par a par:

    $ python .v69aud/cruce_clases.py | sed '/cabeza/,$d'
    pares del barrido: 78 | filas de clase: 78 | pares sin fila: [] | filas sin par: []
    todas las filas por clase: {'SANO': 76, 'CONTINUA': 2} | suma: 78
    filas de vecino (dirigidas) de los 20: 118
    pares sin orden que tocan a los 20: 70 | por clase: {'SANO': 68, 'CONTINUA': 2} | suma: 70
      CONTINUA  tomar_notas_copia_guion_reunion_individual ~ conducir_reunion_individual_telefono_distancia | madre tomar_notas_copia_guion_reunion_individual
      CONTINUA  preparar_guion_reunion_individual_subordinado ~ tomar_notas_copia_guion_reunion_individual | madre preparar_guion_reunion_individual_subordinado

**LECTURA:** los `118` vecinos de los `20` son `70` pares sin orden, **cada uno con su fila de clase** y ninguna fila sin
par; y la seccion `2` mide que **la poblacion de hoy es la de ese barrido**, byte a byte en Grove y en el grafo y sin
ningun fichero de ninguna bandeja escrito despues. **Asi que el recorrido de la `68` sigue siendo el recorrido de la
cola sobre la poblacion de hoy, y `d056` SE PAGA CITANDOLO**, con su comprobacion (cero vecinos sin linea) pegada. **Lo
que queda para la `70` es otra cosa y no se paga aqui:** la aduana de `insertar` mide sobre la poblacion del dia de
cada fila, y lo que levante sin linea preparada se lee en el acto (`d031`). **Que su comprobacion salga en cero lo
cruzo en mi turno normal**, contra su copia de `comprobar_veredictos.py`.

## 7. **LO QUE MI LECTURA ESPERA DE LA TANDA, PARA LA `70`**

**Las aristas**, de mis dos ficheros sellados de la `68` con la unica correccion que yo mismo adjudique en la `ACTA 67`
`67.4.d` (`agrupar_tareas` a `infundir`, **gana el**), declarada dentro del instrumento:

    $ python .v69aud/aristas_70.py
    filas de aristas_lectura.tsv: 17 | por clase (sin la marca DUDA, con ACTA 67 67.4.d aplicada): {'SOSTENGO': 5, 'EN VEREDICTO': 2, 'NO': 10} | suma: 17
    aristas esperadas en la 70: 7 | por origen: {'CONTINUA de veredicto': 2, 'SOSTENGO por lectura': 5} | suma: 7
      CONTINUA   tomar_notas_copia_guion_reunion_individual           > conducir_reunion_individual_telefono_distancia
      CONTINUA   preparar_guion_reunion_individual_subordinado        > tomar_notas_copia_guion_reunion_individual
      SOSTENGO   buscar_regularidad_bloques_iguales_trabajo_mando     > infundir_regularidad_reunion_proceso
      SOSTENGO   agrupar_tareas_semejantes_aprovechar_preparacion     > infundir_regularidad_reunion_proceso   (ACTA 67 67.4.d)
      SOSTENGO   agrupar_interrupciones_subordinados_reuniones_regulares > acumular_asuntos_importantes_fichero_espera
      SOSTENGO   conducir_etapas_modelo_ideal_decision                > ejercer_poder_posicion_etapa_decision_clara
      SOSTENGO   conducir_etapas_modelo_ideal_decision                > cortar_discusion_libre_momento_justo
    de ellas con madre usar_tres_clases_reunion_proceso: 0

**El orden**, por las restricciones que mi lectura pone, y cuantas cumple el orden de pieza del libro:

    $ python .v69aud/restricciones_orden.py | tail -4
    restricciones: 6 | por clase: {'obligan (madre antes que hijo)': 4, 'D.36 de un solo lado, informativas': 2} | suma: 6
    de las que obligan, violadas por el orden del libro: 0
    con madre usar_tres_clases_reunion_proceso: 0
    ultimas dos del orden del libro: ['zanjar_seis_preguntas_decision_adelantado', 'anunciar_decision_inesperada_reconvocar_reunion']

**La fidelidad**, mi lectura sellada contra los pasos de las fichas de hoy:

    $ python .v69aud/contar_fidelidad.py
    fichas con descuadre entre sus pasos de hoy y mis filas: 0 []
    cap_05: candidatos 12 | pasos en ficha 84 | mis marcas selladas: {'T': 81, 'P': 0, 'D': 3} | suma: 84 | PUENTE 0 de 84 = 0.00 por ciento | con las D adjudicadas T (ACTA 67 67.4.a): T 84, P 0, suma 84
    cap_06: candidatos 8 | pasos en ficha 62 | mis marcas selladas: {'T': 61, 'P': 0, 'D': 1} | suma: 62 | PUENTE 0 de 62 = 0.00 por ciento | con las D adjudicadas T (ACTA 67 67.4.a): T 62, P 0, suma 62

**LECTURA:**

- **`7` aristas esperadas en la `70`, ninguna con madre `usar_tres_clases_reunion_proceso`**: las `2` `CONTINUA` de las
  notas y `5` por lectura. Son las `15` que el extractor esperaba en la `68` **menos las `8` de `D68.7`**, que es lo que
  mi `ACTA 67` `67.4.d` predijo si la conjunta me daba la razon. **Coincide con el `7` de sus dos asuntos**, y lo digo
  como coincidencia: **par a par lo cruzo en mi turno normal**, y ahi es donde un `7` igual con pares distintos se veria.
- **El orden no depende de la cabeza**: ninguna restriccion la tiene de madre, las `4` que obligan las cumple el orden de
  pieza, y las `2` de `D.36` son informativas. Quitar las ocho madres no rompe nada.
- **`PASOS INVENTADOS POR CAPITULO` no se mueve**: las `20` fichas tienen hoy los pasos que lei, uno por fila, y siguen
  en **`cap_05` `0` de `84`** y **`cap_06` `0` de `62`**, las cifras firmadas en la `ACTA 67` `67.5`.

## 8. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los
   originales y con la cabecera cambiada a la `69`.
2. **Su relectura de `D68.7`, par a par**: que las `8` lineas de la cabeza y sus `4` filas `SOSTENGO` esten cambiadas
   por correccion declarada, con la vieja encima como `# vuelta 69`, **las dos lineas de cada par juntas**, y que no
   haya cambiado **ninguna otra** linea de `.v68ext/veredictos_listos.txt` ni de `.v68ext/aristas_lectura.txt`. Y **que
   punto de mi caso sostiene o tumba**, contra la seccion `3`.
3. **`D68.15`**: su comentario `EN ESPERA` con las dos lecturas, y `d170` sin pagar.
4. **`d053`**: su razon contra la seccion `5`, con la linea de cada lado; y como mi lectura no es ciega, **la leo buscando
   lo que su razon diga y la mia no**.
5. **`d056`**: su salida de `comprobar_veredictos.py` contra mi seccion `6`, y que el pago cite el recorrido de la `68`.
6. **Sus `7` aristas esperadas contra mis `7`, par a par**, y su orden contra mis `4` restricciones.
7. **La huella de las `20`** que su cierre dice tomar, contra `.v68aud/huellas_al_barrer.txt`, y el censo contra la
   seccion `2`.
8. **La clase de la vuelta**: que declaro el saneamiento en el registro (`d085`) y que pago solo lo que pago.
9. **La muestra pineada de los SANO**: esta vuelta no escribe en la bitacora (seccion `2`), asi que **no hay poblacion
   que muestrear** (`7`); los de `cap_05` y `cap_06` se muestrean cuando entren, en la `70`.

## 9. **ESTA PAGINA CONTRA `R6` Y `R7`, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos dos bloques de la segunda pasada leen la pagina que escribio la primera,
identica salvo ellos. El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion (las que la
nombran en mis frases y comandos no cuentan, porque la nombran para decir que no la imprimo); el segundo, las lineas de
bloque que reparten en clases, y cuantas traen su `suma`:

    $ grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md
    0
    $ python .v69aud/r7_pagina.py
    lineas de bloque que reparten en clases: 16 | por estado: {'con suma': 16} | suma: 16
