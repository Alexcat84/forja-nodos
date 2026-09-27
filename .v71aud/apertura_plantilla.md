# APERTURA CIEGA DE LA VUELTA 71, lote 7 (`grove_high_output`), **CLASE INSERCION, VUELTA DE PREPARACION**

*Auditor `claude-opus-5-5`, fase ciega, 25 sep 2026, la que el arnes numera `VUELTA 7` en la corrida que arranco el 23 a
las `21:50`. Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de `.v71aud/`,
escrito y corrido en esta fase; cada bloque `$` lo pega `.v71aud/generar_apertura.py` corriendo el comando en el momento de
escribirla. **No hay ninguna tabla en esta pagina**, a proposito, como en la `68`.*

**UNA LIMITACION DE METODO, DICHA ANTES DE NADA: EN ESTA FASE NO HE CORRIDO `git` EN LA CARPETA.** La carpeta de una linea
viva es solo del arnes (`PARALELO.md` `7`: *ni siquiera `git status`, que refresca el indice*), y lo aplico tambien a mi
asiento. **Lo que las aperturas de la `68` y la `70` median con `git diff` aqui no lo mido**: que ficheros cambio la vuelta
desde mi acta, y contra que commit. El commit en que esta el arbol lo leo de los ficheros de `.git/`, sin correr `git`:

@@RUN:0::cat .git/HEAD; cat .git/refs/heads/extraccion-mundo-11@@

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: 1415acdc421ba8a562e191f458c590924d82a75a

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su reporte de la
`71`** (`ACTA 69` `69.12`: *el reporte de la `71`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py`, los dos con
la cabecera del tramo cambiada a la `71`*), y el reporte **no esta en el arbol**: el arnes lo retiro para esta fase
(`D.34.2`) y no lo he recuperado por ninguna via. **Se mide en mi turno normal**, con los dos instrumentos sacados otra vez de
los originales y no de las copias del extractor. Lo que si esta en mi mano lo cumplo en mi pagina: cada bloque `$` lleva la
salida del comando que abre, y nada mas.

@@RUN:0::ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl@@
@@RUN:0::grep -n "VUELTA 7 : APERTURA CIEGA" docs/loop/loop.log | tail -1@@

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 69` `69.12`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no enseña `previos` ni `siguientes`, y ningun instrumento de esta fase imprime claves de
relacion de un nodo que la vuelta haya tocado. Los ficheros de pasos que lei, y cuantas lineas con esas claves traen; y
cuantos instrumentos mios las nombran:

@@RUN:0::grep -c -E "previos|siguientes" .v71aud/pasos_*.txt@@
@@RUN:0::grep -l -E "nodos_previos|nodos_siguientes|previos|siguientes" .v71aud/*.py .v71aud/*.sh | wc -l@@

**UNA COSA QUE DECLARO AQUI Y NO ESCONDO:** al abrir, para saber que campos trae una ficha de la bandeja, corri a mano un
`python -c` que imprimio **la lista de NOMBRES de campos** de `cerrar_brecha_dos_preguntas_estrategia`, y en esa lista
estan los nombres `nodos_previos` y `nodos_siguientes`; **sus valores NO se imprimieron** (el mismo comando se los saltaba
por nombre), ni de esa ni de ninguna otra. No vi ninguna arista cableada. Lo cuento porque `R6` habla de no imprimir
*claves de relacion*, y un lector estricto puede leer que el nombre de la clave ya lo es.

**LECTURA:** ningun instrumento mio de esta fase nombra esas claves, y ninguna salida de pasos las trae. **No vi ninguna
clave de relacion con su valor de un nodo tocado en esta fase.** Y el cumplimiento de la pagina entera lo mide un `grep`
sobre ella antes de cerrarla (seccion `9`).

HEREDADO 3: CUMPLIDO. **`R7`, mio** (`ACTA 69` `69.12`): toda linea de conteo por clases que publico en esta pagina cuenta
todas las clases con el mismo predicado y trae su `suma`, y la calcula e imprime el instrumento que la saca (`contar_fidelidad`,
`vecinos_tabla`, `armar_clases`, `cruce_clases`, `cruce_aristas`, `cobertura` y `poblacion` la llevan). La medida sobre la
pagina, con la copia de `.v70aud/r7_pagina.py`, esta en la seccion `9`.

**LA HUELLA** es la que el prompt me entrega, comprobada solo contra el propio prompt: **no la recomputo**, porque
`forja.py herencia` lee en esta fase un fichero retirado (`d146`).

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los commits del extractor, y tres son cifras
de su vuelta**: `682a39c` (*censo 410/1027/1/27/65 remedido, ninguna insertada*), `6b2f721` (*PASOS INVENTADOS de cap_07 a
cap_14 en seis filas, 4 de 121 corregidos; huellas de las 20 contra 7be17c0, 17 iguales y las 3 corregidas; D.61 sin
abiertos; R5 en cero; gate, guiones, 379 pruebas y cierre estricto en verde*) y `8f5e84b` (*el barrido de las 20 (20 de 20,
poblacion 479, 50 pares), 50 lineas de veredicto listas (46 SANO, 4 CONTINUA), 4 aristas por lectura (3 D.37 de
planificar_tres_pasos y 1 D.29), d170 sin linea ni arista, y el orden con D.36 en cero*). **Los lei antes de medir nada.** Es
el mismo hueco de `d146` que declararon las aperturas de la `65` a la `70`, y no lo arreglo yo (`D.45`). Tambien lei la cola
de `docs/loop/loop.log`, que no se retira, y mi propio encargo, `docs/loop/PROMPT_SIGUIENTE.md`.

**Y DOS COSAS MAS, DEL MISMO TIPO:** un `ls -la .v71ext | head` me enseño **los nombres** de los primeros ficheros de su
carpeta (`abortado/`, `apertura.txt`, `aristas_lectura.txt`, `barrer.sh`, `barrido.log`, `barrido_cerrar_brecha...txt`), **no
su contenido**; y **las fichas de la bandeja llevan dentro, en su `resumen_teorico`, la lectura del propio extractor** (de
que linea sale cada paso, y en tres de ellas la CORRECCION DECLARADA DE LA VUELTA 71 con el texto viejo dentro). **Esas
correcciones las lei DESPUES de escribir mi fidelidad paso a paso**, y lo que dicen va en la seccion `3`, separado. **Pero el
reparto de lineas de UNA ficha, `cerrar_brecha_dos_preguntas_estrategia`, si lo vi ANTES**: el mismo `python -c` de la
seccion `0` imprimio los primeros `1500` caracteres de su `resumen_teorico`, que dicen de que frase de L39 sale cada uno de
sus siete pasos. Mis siete filas de esa ficha dicen lo mismo, y no puedo probar que las leyera sin eso delante.

**LO QUE HAGO CON ELLO:** ninguna cifra de esta pagina sale de esos asuntos; todas salen de un instrumento corrido en esta
fase, y donde coinciden lo digo como coincidencia y no como fuente. **No he abierto nada de `.v71ext/` por dentro** (ni su
fidelidad, ni su barrido, ni sus veredictos, ni sus aristas, ni su orden), **ni `bitacora/VEREDICTOS.jsonl` por dentro**:
de ella solo cuento lineas. **Y ESTO SI PESA SOBRE MI LECTURA, Y LO DIGO:** el asunto de `8f5e84b` me dijo *3 D.37 de
planificar_tres_pasos* y *4 CONTINUA* antes de leer. Mis tres `D.37` salen de la seccion `6` con su busqueda y su linea, y
mis `CONTINUA` son los que son; pero no puedo probar que no me empujo, y por eso lo escribo aqui.

## 2. **EL ALCANCE, Y EL CENSO QUE LO SOSTIENE**

El encargo de la `71` (`docs/loop/PROMPT_SIGUIENTE.md`) es **dejar listas sin insertar ninguna** las `20` fichas de la bandeja
de Grove cuya `UNIDAD DE ORIGEN` es `cap_07` (`9`), `cap_10` (`1`), `cap_11` (`2`), `cap_12` (`3`), `cap_13` (`2`) y `cap_14`
(`3`): fidelidad entera, barrido, veredictos, aristas por lectura, orden y la huella de las `20`. Mi lista son las `20`
primeras lineas de `.v70aud/normal/bandeja_grove.txt`, como el encargo manda:

@@RUN:0::head -20 .v70aud/normal/bandeja_grove.txt | awk '{print $1}' | sort | uniq -c; wc -l < .v71aud/los20.txt; head -20 .v70aud/normal/bandeja_grove.txt | awk '{print $2}' | diff - .v71aud/los20.txt && echo "los20.txt es la columna de ids de esas 20 lineas"@@

**El censo de hoy**, sin `git` (grafo, bitacora, pares mutuos; y las bandejas de Grove, Gerber y Marquet, los insertados de
Grove y `procesos/`):

@@RUN:0::wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl@@
@@RUN:0::for d in cuarentena/grove_high_output cuarentena/_insertados/grove_high_output cuarentena/gerber_emyth cuarentena/marquet_turn_the_ship; do echo "$d $(ls $d/*.json | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"@@
@@RUN:0::python .v70aud/poblacion.py@@

**LECTURA:** `410`, `1027`, `1`, `27` y `65` son los de mi `ACTA 69` `69.1` al cerrar la `70`, y Gerber y Marquet siguen en
`22` y `20`: **la vuelta no inserto nada ni movio nada de sede**, que es lo que el encargo pedia. `procesos/` esta vacio. La
poblacion del barrido es `479`, `410` mas `69`, la que el encargo daba. **Lo que no puedo decir sin `git`**: si alguna linea
de la bitacora o algun byte del grafo cambio sin cambiar la cuenta. Eso lo mido en mi turno normal, con el hash del
reporte delante.

**Y LAS `20` SON TODO LO QUE GROVE TIENE DE ESOS SEIS CAPITULOS**, en cualquier sede, por la `UNIDAD DE ORIGEN` de su
`resumen_teorico`:

@@RUN:0::python .v71aud/cobertura.py@@

**LECTURA, sin medirla mas:** hay piezas de esos capitulos sin candidato en ninguna sede (en `cap_07`, *decir que no* de L65 y
L81 y los casos de Colon y Filipinas; en `cap_10`, el grupo de pares de L29 a L35, la publicidad de L45 a L51 y la
organizacion de dos planos de L59 a L79; en `cap_12`, la jerarquia de Maslow, el dinero, el miedo y la analogia deportiva
de L97 a L117; en `cap_13`, la transmision de valores de L53 y L55; en `cap_14`, la evaluacion del desempeño de L81 a L103,
las sorpresas de L159, los tres desenlaces de L173 a L181, el as de L183 a L191 y la autoevaluacion y la entrega por escrito
de L193 a L201). **Es la frontera de las vueltas que minaron Grove, que no reabro (`D.47`)**; solo digo que la vi.

## 3. **LA FIDELIDAD DE LAS `20`, LEIDA ENTERA** (`D.30`, `D.58`, `8`)

Lei **enteros** los seis capitulos, `cap_07` (Cap. 6, *Planning*), `cap_10` (Cap. 9, *Dual Reporting*), `cap_11` (Cap. 10,
*Modes of Control*), `cap_12` (Cap. 11, *The Sports Analogy*), `cap_13` (Cap. 12, *Task-Relevant Maturity*) y `cap_14` (Cap.
13, *Performance Appraisal*), y cada paso de las `20` contra su linea, con los pasos delante por `pasos_ciego.py`
(`.v71aud/pasos_cap07.txt` a `.v71aud/pasos_cap14.txt`).

@@RUN:0::wc -l fuentes/grove_high_output/cap_07.md fuentes/grove_high_output/cap_1[0-4].md@@

Una fila por paso en `.v71aud/fidelidad.tsv`: `T` transcripcion, `P` puente (**la clausula reescrita cuenta como `P`**, `ACTA
62` `62.5`), `D` mi duda, con su capitulo, su linea y la frase del libro. El contador es copia de `.v68aud/contar_fidelidad.py`
con las rutas cambiadas, **una fila por capitulo** (`8.2`) y la suma de cada reparto (`R7`), y cruza cada fila con los pasos
de la ficha de la bandeja de hoy:

@@RUN:0::python .v71aud/contar_fidelidad.py@@

**LECTURA: los seis capitulos son de inventario rico** (frases con *should*, *must*, *you need to*, preguntas literales y
cuadros con sus casillas), y los pasos los transcriben casi frase a frase. **No encuentro ningun PUENTE en el texto de hoy
de las fichas.** Mis seis dudas son **tres figuras**, y en las tres me inclino a `T`:

- **el ejemplo convertido en mandato**: `definir_entorno_grupo_clientes_proveedores_competidores` pasos `3`, `4` y `5` (*Lista
  a tus clientes / proveedores / competidores*), que L25 da **dentro del ejemplo del mailroom** (*your environment would
  consist of*); y `examinar_demanda_entorno_dos_marcos_temporales` paso `7` (*No rebajes la demanda que declaras por lo que
  creas que la otra parte puede entregar*), que L31 da como **el ejemplo de marketing** que sostiene el *No* del paso `6`.
- **la razon convertida en instruccion**: `fijar_horizonte_ventana_replanificacion` paso `5` (*Regula esa frecuencia por la
  retroalimentacion*), donde L61 da la retroalimentacion como **el motivo** de no replanificar demasiado.
- **la clausula añadida por descarte**: `elegir_modo_control_motivacion_factor_cua` paso `6` (*... con el factor CUA bajo, usa
  el modo contractual*): la frase de L61 **no dice** *CUA bajo*; se deduce del cuadro de cuatro cuadrantes que la misma
  linea pone.

**`PASOS INVENTADOS` por mi instrumento, sobre el texto de hoy: `0` en los seis capitulos**; si mis dudas cayesen, `cap_07`
`5` de `53` (`9,43`), `cap_11` `1` de `17` (`5,88`) y los otros cuatro en `0`. **Por debajo del `10` en las dos lecturas, y el
peor capitulo es `cap_07`** en la lectura estricta. Es preparacion y no entrada.

**Y LO QUE LEI DESPUES, EN LAS FICHAS:** tres de las `20` traen en su `resumen_teorico` una *CORRECCION DECLARADA DE LA
VUELTA 71* con el texto viejo dentro: `planificar_tres_pasos_demanda_estado_brecha` pasos `1` (*y no sobre otra cosa*) y
`4`, `repartir_supervision_puesto_funcional_mision` paso `8` (el *quiza* que el paso viejo se comia del *perhaps* de L43) y
`entregar_evaluacion_desempeno_tres_claves` paso `2` (el *completo* que L111 no pone). **Los cuatro pasos corregidos los lei
yo `T` en su texto de hoy, y sus cuatro textos viejos los habria leido `P`**: las cuatro correcciones se sostienen por mi
lectura. **Lo que no puedo decir** es si mi lectura ciega habria cazado esos cuatro puentes, porque cuando lei ya no estaban.
**Coincide con los *4 de 121 corregidos* y las *3* fichas corregidas del asunto de `6b2f721`, y lo digo como coincidencia**;
fila a fila lo cruzo en mi turno normal.

@@RUN:0::grep -l "CORRECCION DECLARADA DE LA VUELTA 71" cuarentena/grove_high_output/*.json | wc -l; grep -l "CORRECCION DECLARADA DE LA VUELTA 71" cuarentena/grove_high_output/*.json | sed 's|.*/||'@@

## 4. **MI BARRIDO DE LAS `20`, SOBRE GRAFO MAS BANDEJAS** (`D.38.4`, `D.38.5`)

Copia de `.v68aud/barrido_uno.py` (la ficha normalizada como la aduana, contra `dataset/nodos.jsonl` mas
`aduana.poblacion_de_bandejas`, con `buscar_vecinos` de `src/aduana.py`) y de `.v68aud/barrer.sh` con la lista cambiada a
`.v71aud/los20.txt`, **cinco a la vez, recogido entero dentro de este turno**. Antes de lanzarlo guarde la huella de cada
ficha de las tres bandejas y del grafo, y al recogerlo las comprobe:

@@RUN:0::head -1 .v71aud/barrido.log; tail -1 .v71aud/barrido.log; grep -c "rc=0" .v71aud/barrido.log; grep -c "rc=" .v71aud/barrido.log@@
@@RUN:0::wc -l < .v71aud/huellas_al_barrer.txt; sha1sum -c --quiet .v71aud/huellas_al_barrer.txt && echo "las 69 fichas de las tres bandejas y el grafo: mismas huellas que al barrer"@@

**Poblacion y vecinos por candidato:**

@@RUN:0::python .v71aud/vecinos_tabla.py | tee .v71aud/vecinos_tabla.txt | sed -n '1,/^sin fichero/p'@@
@@RUN:0::grep "^filas de vecino" .v71aud/vecinos_tabla.txt; grep ">" .v71aud/vecinos_tabla.txt | grep -c " grafo "; tail -1 .v71aud/vecinos_tabla.txt@@

**Las filas de vecino con un extremo en el grafo, y los pares con un extremo fuera de la tanda:**

@@RUN:0::grep ">" .v71aud/vecinos_tabla.txt | grep " grafo " | awk '{print $1, $3}'@@
@@RUN:0::grep "~" .v71aud/vecinos_tabla.txt | grep "con fuera" | awk '{print $1, $3}'@@

**LECTURA:**

1. **Las `20` dan `50` filas de vecino en `33` pares sin orden**, `21` entre dos de la tanda y `12` con uno de fuera.
   **Coincide con los *50 pares* y las *50 lineas de veredicto* del asunto de `8f5e84b`**, que ahi llama *pares* a mis
   filas, como en la `68`; y lo digo como coincidencia.
2. **Cinco no levantan a nadie contra `479`**: `repartir_supervision_puesto_funcional_mision`,
   `elegir_modo_control_motivacion_factor_cua`, `escalonar_complejidad_puesto_empleado_nuevo`,
   `elegir_estilo_direccion_madurez_relevante_tarea` y `guiar_subordinado_etapas_resistencia_desempeno`. **Lo que mas levanta
   es `cap_07`**, un capitulo de nueve piezas sobre el mismo proceso: `cerrar_brecha` levanta `10`, cinco hermanas y cinco del
   grafo por la forma *pregunta*.
3. **Los vecinos del grafo** son todos por la forma o por palabras sueltas, y ninguno de otro capitulo de Grove que sea del
   mismo asunto: `preguntar_seguimiento_hallar_huecos` de Scott y `responder_tres_preguntas_vocacion_directiva` y
   `preparar_preguntas_entrevista_antemano` de Zhuo, por `paso_contra_nodo` entre `0,614` y `0,645` sobre el verbo
   *preguntar*; y de Grove `archivar_indicadores`, `cortar_discusion`, `zanjar_seis_preguntas`, `anunciar_decision` y
   `vencer_sindrome`, por `similitud_texto` entre `0,350` y `0,374`. **El unico de fuera que esta en una bandeja** es
   `usar_banco_nueve_preguntas_entrevista`, de `cap_15`, levantado por `preparar_resena`.
4. **`d170`, CON LA SALIDA DELANTE:** `elegir_estilo_direccion_madurez_relevante_tarea` no levanta a nadie, y
   `fijar_frecuencia_reunion_individual_madurez_tarea` no aparece en ninguna fila de mi barrido:

@@RUN:0::grep -c "fijar_frecuencia_reunion_individual_madurez_tarea" .v71aud/vecinos_tabla.txt; grep "^    elegir_estilo" .v71aud/vecinos_tabla.txt@@

   **Mi barrido no levanta el par: no hay linea ni arista** (`D69.3`), que es lo que el encargo dice que toca en ese caso.
   Coincide con el *d170 sin linea ni arista* del asunto de `8f5e84b`.
5. **LO QUE EL BARRIDO NO LEVANTA Y SE LEE:** las tres partes de la serie de `planificar_tres_pasos` (seccion `6`), y
   `elegir_modo` con `escalonar_complejidad`, que el libro une con palabras (*Let's apply our model*, `cap_11` L63). **Las dos
   cosas van por lectura.**

**EL RELOJ, medido y no techo:** de las `19:57:20` a las `21:15:44` del 25, con fichas de estos segundos (la menor y la mayor):

@@RUN:0::grep "rc=" .v71aud/barrido.log | sed 's/.*segundos=//' | sort -n | sed -n '1p;$p'@@

## 5. **MI LECTURA CIEGA DE LOS PARES** (`1.2`, `6.1`, y solo la vara `6.1`)

**Leidos con los pasos de los dos delante**, todos con `pasos_ciego.py` (`R6`): `.v71aud/pasos_cap07.txt` a
`.v71aud/pasos_cap14.txt` para las `20`, y `.v71aud/pasos_fuera_a.txt` y `.v71aud/pasos_fuera_b.txt` para los de fuera. **Una
fila por par** en `.v71aud/mis_clases.tsv`, con su razon. **De donde sale cada fila:** los pares de dentro de un mismo capitulo
los escribi **todos** (`44`, los `36` de `cap_07` y los `8` de `cap_11` a `cap_14`) **antes de mirar ninguna fila del barrido**,
en `.v71aud/clases_intra.txt`; los de entre capitulos y los de fuera, al recogerlo, en `.v71aud/clases_fuera.txt`.
`armar_clases.py` los junta, y el cruce comprueba que cada par del barrido tiene su fila y cada fila su par:

@@RUN:0::python .v71aud/armar_clases.py@@
@@RUN:0::python .v71aud/cruce_clases.py@@

**LECTURA, los cuatro `CONTINUA`**, los cuatro dentro de la pieza de planificacion de `cap_07`, y en los cuatro el hijo trae
procedimiento propio, asi que ninguno es `REPITE`:

- `definir_entorno_grupo_clientes_proveedores_competidores` madre de `examinar_demanda_entorno_dos_marcos_temporales`: L29
  remite con palabras (*Once you have established what constitutes your environment*), y el hijo anade los dos marcos, la
  diferencia y no rebajar.
- `definir_entorno_grupo_clientes_proveedores_competidores` madre de
  `examinar_entorno_expectativas_tecnologia_proveedores_grupos`: la condicion del hijo es el entorno ya definido, y anade los
  cuatro objetos y las dos preguntas sobre los otros grupos.
- `examinar_demanda_entorno_dos_marcos_temporales` y `determinar_estado_presente_capacidades_proyectos_merma` madres, cada una
  en su par, de `cerrar_brecha_dos_preguntas_estrategia`: la condicion de la hija es *ya tienes medida la demanda de tu
  entorno y tu estado presente*, el producto de las dos (L39).

**MIS DUDAS EN PARES QUE EL BARRIDO LEVANTA, escritas antes de saber:** los dos `CONTINUA` de `cerrar_brecha` **pueden leerse
`SANO` de pasos hermanos** de una serie que su cabeza ya cablea por `D.37`; el de `examinar_entorno` puede leerse `SANO`
porque L27 no remite con palabras como L29; el `SANO` de `examinar_entorno` con `examinar_demanda` **COMPARTE UN PASO** (las
expectativas del cliente hoy, L27 contra L29) **y lo leo `SANO` y no `REPITE` porque fuera del solape hay procedimiento en los
dos lados** (`6.1`, sin bascula), con la contraria escrita (`CONTINUA` con madre `examinar_entorno`); y el `SANO` de
`examinar_demanda` con `determinar_estado` puede leerse `CONTINUA` por la moneda de L35. **Si alguna me cae, cae dentro de lo
que marco aqui.** Los demas `SANO`, incluidos los doce de fuera, comparten la forma *pregunta*, la palabra *grupo* o la cuenta
del titulo, y ningun paso.

## 6. **LAS ARISTAS POR LECTURA** (`D.29`, `D.37`, `D.53`)

**Las que mi lectura sostiene o descarta**, una fila cada una en `.v71aud/aristas_lectura.tsv`, con su tramo de madre, de hijo y
su linea del libro, **escritas antes de que el barrido terminara**; al recogerlo marque `EN VEREDICTO` las cuatro que el
barrido levanta, que no son aristas por lectura sino las cuatro lineas `CONTINUA` de la seccion `5`. El cruce dice si el
barrido levanto el par y donde vive hoy cada extremo:

@@RUN:0::python .v71aud/cruce_aristas.py@@

**`D.37`, LOS TITULOS QUE DICEN CUANTAS PARTES TIENEN:** cinco de la tanda dicen cuantas y las nombran:
`planificar_tres_pasos_demanda_estado_brecha` (la demanda, el estado presente, la brecha),
`examinar_entorno_expectativas_tecnologia_proveedores_grupos` (cuatro objetos), `contestar_dos_preguntas_direccion_objetivos`
y `cerrar_brecha_dos_preguntas_estrategia` (dos preguntas cada una) y `entregar_evaluacion_desempeno_tres_claves` (tres
claves). La busqueda de cada parte por id y titulo sobre grafo mas bandejas:

@@RUN:0::python .v71aud/d37_partes.py@@

**LECTURA:**

- **`D.37` DISPARA EN UNA SOLA CABEZA, `planificar_tres_pasos`, Y POR SUS TRES PARTES**: el paso 1 es
  `examinar_demanda_entorno_dos_marcos_temporales` (**con DUDA**: la pieza *STEP 1* del libro, L23 a L31, tiene tres nodos, y
  leo que la parte es la que produce la demanda y que `definir_entorno` y `examinar_entorno` son su entrada, que quedan de
  nietas por `CONTINUA`), el paso 2 `determinar_estado_presente_capacidades_proyectos_merma` y el paso 3
  `cerrar_brecha_dos_preguntas_estrategia`, las tres **citando L19** y **ninguna levantada por el barrido**, y sus pares son
  de cabeza y parte, sin linea de veredicto (`D.53`). **Coincide con las *3 D.37 de planificar_tres_pasos* del asunto de
  `8f5e84b`, que me llego antes de leer y lo he dicho en la seccion `1`.**
- **En las otras cuatro no dispara**: ninguna parte existe como nodo. Lo que la busqueda levanta son la propia cabeza, sus
  hermanas de `cap_07`, y de otros libros la *franqueza radical* de Scott, la escucha de Scott, Smart y Marquet, las
  expectativas del equipo de Zhuo y los hitos de una meta grande de Zhuo (`partir_meta_grande_hitos`), **que son otras
  doctrinas y no las partes que la cabeza de Grove nombra**. `D.37` pide la parte que el texto de la cabeza enumera, no un
  nodo de otro libro que use la misma palabra.
- **UNA `D.29` POR LECTURA, CON DUDA:** `elegir_modo_control_motivacion_factor_cua` madre de
  `escalonar_complejidad_puesto_empleado_nuevo`, por L63 (*Let's apply our model to the work of a new employee*), que el
  barrido no levanta. La duda esta escrita en su fila: el hijo no elige un modo de control, elige el puesto. **Coincide con
  la *1 D.29* del asunto de `8f5e84b` en la cuenta; si es el mismo par lo vere en mi turno normal.**
- **Los `NO`, para que se vea el criterio**, y los que llevan DUDA la llevan escrita en su fila: el horizonte, el periodo y
  la altura de la meta **son parametros del ejercicio que se deciden al montarlo**, no hijos de su producto; la entrega de la
  revision vale para cualquier tipo y el libro la pone antes que los tipos; la amistad **nombra** los estilos de
  `elegir_estilo` sin procedimentarlos; `elegir_estilo` **remite** a `delegar_tarea_base_comun_seguimiento` del grafo (*as
  we've said before*) en un paso de ocho, y comparte concepto con `supervisar_tarea_delegada_etapa_menor_valor` sin ser la
  condicion de ella; y **la planificacion se monta por ANALOGIA con la fabrica** (L17), que no es arista con
  `casar_flujo_fabricacion_flujo_ventas`. **Ninguna madre del grafo** para las `20`, por mi lectura.
- **`d170`**: la fila de `fijar_frecuencia` queda `NO`, con la cita de la conjunta.

## 7. **EL ORDEN QUE MI LECTURA OBLIGA** (`D.36`)

**No es un orden: son las restricciones**, escritas antes de ver el del extractor. Madre antes que hijo por mis `CONTINUA` y
mis `SOSTENGO` con los dos extremos en la tanda, y cuantas cumple el orden de pieza del libro, **que aqui saco de mi
fidelidad** (capitulo y primera linea), porque `.v71aud/los20.txt` va por capitulo y alfabetica y no es orden de pieza:

@@RUN:0::python .v71aud/restricciones_orden.py@@

**LECTURA:** las ocho que obligan (`planificar_tres_pasos` antes que sus tres partes, `definir_entorno` antes que sus dos
hijas, las dos madres antes que `cerrar_brecha`, y `elegir_modo` antes que `escalonar`) **las cumple ya el orden de pieza del
libro**. Las cuatro `D.36` de un solo lado son informativas y **no obligan**, porque la aduana de `insertar` mide grafo mas
bandejas (`D.38.5`); dos de ellas van contra el orden del libro, y da igual por esa misma razon. **Su orden, contra estas
ocho, lo compruebo en mi turno normal.**

## 8. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los originales y
   con la cabecera cambiada a la `71`.
2. **El censo con su hash**: que la vuelta no movio el grafo, la bitacora, los censos ni las bandejas de Gerber y Marquet, y
   que en la de Grove solo cambiaron las fichas corregidas, **con `git diff` en un clon aparte o con la linea parada**, que es
   lo que en esta fase no he medido.
3. **Mi fidelidad contra la suya, paso a paso**: `121` filas mias contra las suyas. Si mis seis `D` se quedan en `T`, las seis
   cifras siguen en `0`; si alguna cae a PUENTE, cae dentro de lo que marque aqui; **y si el marca PUENTE un paso que yo lei `T`
   sin duda, y gana, la caida de lectura es mia.** Y sus cuatro correcciones contra mi lectura de sus textos viejos (seccion
   `3`).
4. **Mis clases contra sus lineas de veredicto, par a par** (`33` pares, `50` filas), y mis aristas por lectura contra las
   suyas, por par y no por cuenta.
5. **Su orden contra mis ocho restricciones.**
6. **La huella de las `20` fichas** que su cierre dice sellar, contra las mias de `.v71aud/huellas_al_barrer.txt`, tomadas
   antes de barrer y comprobadas al recoger.
7. **La muestra pineada de los SANO**: esta vuelta no escribe en la bitacora; los `SANO` de las `20` se muestrean cuando
   entren.

## 9. **ESTA PAGINA CONTRA `R6` Y `R7`, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica salvo
estos bloques. El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion (las que la nombran en mis
frases y comandos no cuentan, porque la nombran para decir que no la imprimo); el segundo, con la copia de
`.v70aud/r7_pagina.py`, cuenta las lineas de bloque que reparten una cifra en clases y cuantas traen su `suma`:

@@RUN:0::grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md@@
@@RUN:0::python .v71aud/r7_pagina.py@@
