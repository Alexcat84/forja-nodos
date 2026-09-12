# APERTURA CIEGA DE LA VUELTA 15

*Escrita por el **auditor** ANTES de que el arnes le exponga el reporte del
extractor (`D.34`, ampliada el 11 sep 2026; `AUDITOR_FORJA.md` seccion 1 punto 5).
Esta es la lectura que despues se compara con la del extractor. **El arnes sella
este fichero y lo commitea el: yo no lo commiteo y no lo vuelvo a tocar.***

**LAS DOS REGLAS QUE MANDAN EN ESTA SEDE, y las cito de entrada porque mis tres
ultimas caidas propias nacieron las tres aqui:**

- **`D.38.3`**: esta sede publica **CLASES Y LECTURAS**. Toda cifra sale de un
  instrumento de la casa corrido en esta misma fase, **con su salida literal
  pegada al lado**. Una cifra sin instrumento al lado no se publica.
- **`D.38.4`**: el barrido de vecinos se hace sobre **GRAFO MAS BANDEJAS**, porque
  un vecino que esta en la bandeja es vecino.

**ALCANCE DE LA VUELTA QUE ABRO:** lote 4, `scott_radical_candor`. El encargo de la
vuelta 15, TAREA 3, manda **cuatro unidades, `cap_04` a `cap_07`**. Lo que
encuentro minado es **UNA, `cap_04`**, y la medida esta en la seccion 2: la traigo
yo, no me la ha dicho nadie.

**NO HAY HUECO DE ACTA**, y lo compruebo antes que nada porque va antes que nada
(`AUDITOR_FORJA.md` seccion 1 punto 0):

    $ grep -n "^# ACTA" docs/loop/ACTA_AUDITOR.md | tail -1
    12625:# ACTA 14. VUELTA 14, cierre de la cola de la 13 y apertura del lote 4 (`scott_radical_candor`), `cap_00` a `cap_03`

La ultima acta escrita cubre la **vuelta 14**, y la vuelta que abro es la **15**.
Son consecutivas: **audito una sola vuelta y no arrastro ninguna sin acta.**

---

## 0. LOS CUATRO FICHEROS RETIRADOS, Y LO QUE NO HE HECHO POR RECUPERARLOS

    $ git status --short docs/loop/
     D docs/loop/APERTURA_CIEGA.md
     D docs/loop/REPORTE.md
     D docs/loop/loop.log
     M docs/loop/ultimo_apertura.json
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json

Los cuatro que `D.38.3` manda retirar estan retirados. **No he recuperado ninguno:
ni por `git show`, ni por `git checkout`, ni por el reflog, ni por el arbol de
ningun commit, ni por ninguna otra via.** Lo declaro yo aqui porque el arnes lo
vigila por su cuenta y lo escribe en el log.

**Y ME HE RETIRADO OCHO MAS QUE NADIE ME RETIRO, y digo cuales y por que.** El
arbol lleva, con seguimiento de git, los borradores de trabajo del propio turno
del extractor:

    $ git ls-files | grep -E "^\.(informe|insercion|cuadre|asimetria|orden)"
    .asimetria_lote3_vuelta15.txt
    .cuadre_bitacora_vuelta15.py
    .informe_lote.txt
    .informe_lote3_vuelta15.txt
    .informe_lote4.txt
    .informe_lote4_vuelta15.txt
    .insercion_lote3_vuelta15.log
    .orden_insercion_lote3.txt

**NO HE ABIERTO NINGUNO.** El peor de todos es `.informe_lote4_vuelta15.txt`: **es
el informe de la aduana sobre la misma bandeja que yo vengo a barrer**, o sea la
version del extractor de lo que ocupa mis secciones 3, 4 y 7. Abrirlo seria copiar
el examen. La razon es la misma que la de la ampliacion de `D.34`: **un borrador
escrito dentro del turno del extractor es, con alta probabilidad, un resumen de lo
que yo vengo a leer a ciegas.** Prefiero declarar que existen a leerlos y tener
que declarar que los lei. **Es el mismo remedio que aplique en la apertura de la
vuelta 14, y lo mantengo aqui para no romperlo** (`D.38.2`, especie `REMEDIO
ROTO`).

## 1. LO QUE SI HE LEIDO, Y LA RENDIJA QUE DECLARO YO MISMO

He leido: `docs/loop/AUDITOR_FORJA.md` entero; `docs/loop/PROMPT_SIGUIENTE.md`,
que es el encargo de la vuelta 15 y lo escribio Alexis; `docs/loop/ORDEN_DE_LOTES.md`;
`docs/BANCO_DE_REGLAS.md` en `D.1`, `D.27`, `D.30`, `D.35`, `D.37`, `D.38` entera y
`D.39`; `esquema/nodo.schema.json`; `censos/atribuciones.md`; `cuarentena/LEEME.md`;
la apertura ciega de la vuelta 14, que es mia; los **ocho** candidatos de
`cuarentena/scott_radical_candor/` enteros; `cap_04.md` entero; `cap_01.md` y
`cap_03.md` en las lineas que sostienen a los dos candidatos viejos; las cabeceras
de `cap_05.md`, `cap_06.md` y `cap_07.md`; `dataset/nodos.jsonl`; y los tres nodos
vecinos que mi propio barrido levanto.

> ### MI CEGUERA NO ES TOTAL Y NO LA VOY A VENDER COMO TOTAL
>
> Para saber que vuelta abro tuve que correr `git log`, y **el asunto del commit de
> cierre lleva cinco cifras dentro**:
>
>     $ git log -1 --format="%s"
>     EL CIERRE DE LA VUELTA 15: 203 nodos, 147 veredictos, 78 aristas, cinco guardas en verde y diez discutibles marcados a ciegas
>
> **Asi que he entrado sabiendo cinco numeros del extractor.** Tres los he vuelto a
> medir yo con mi instrumento en esta misma fase, y estan en la seccion 2. **Los
> otros dos NO los he medido y NO los publico como mios**, ni aqui ni por
> repeticion: ni cuantas guardas estan en verde, ni cuantos discutibles marco.
> **Los correre yo en mi turno normal.**
>
> Lo que sigue siendo ciego, que es lo que la regla protege, es **el POR QUE**: no
> se que clase le puso el extractor a ningun candidato, ni que vecinos levanto, ni
> cuales de los discutibles son de este lote, ni que piezas descarto ni con que
> razon, ni que cifra de puentes publico. **Mi clasificacion de abajo esta hecha
> contra el texto fuente y contra el grafo, no contra su cuenta.**
>
> Lo digo yo y antes de que se me pregunte, porque **una apertura que se declara
> mas ciega de lo que fue vale menos que una que declara su rendija.** Y la
> seccion `5.6` salva al asunto de un commit de ser sede de cifra publicada,
> **pero no me salva a mi de haberlo leido.**

## 2. EL ALCANCE REAL DE LA VUELTA, MEDIDO POR MI

**LAS CUATRO UNIDADES QUE EL ENCARGO MANDA, Y CUAL DE ELLAS HAY EN LA BANDEJA.** La
provenencia no la deduzco del contenido: la saco de git, que es quien sabe en que
commit nacio cada fichero.

    $ git log --diff-filter=A --format="COMMIT %h %ad %s" --date=format:"%H:%M" --name-only -- cuarentena/scott_radical_candor/
    COMMIT 81aea10 22:36 TAREA 1 CERRADA: el lote 3 entero esta en el grafo, 203 nodos, la cifra que se publico antes de insertar
    cuarentena/scott_radical_candor/ajustar_franqueza_oido_oyente.json
    cuarentena/scott_radical_candor/cuidar_persona_completa_equipo.json
    cuarentena/scott_radical_candor/delimitar_franqueza_radical_cinco_noes.json
    cuarentena/scott_radical_candor/invitar_desafio_hacia_arriba.json
    cuarentena/scott_radical_candor/manejar_enfado_tras_desafiar.json
    cuarentena/scott_radical_candor/revisar_ciclo_responsabilidades_relaciones.json
    COMMIT 6920050 15:40 cap_00 a cap_03 del lote 4 cerrados con 2 candidatos por la aduana en su propio acto, y las tres tareas que la vuelta 13 dejo abiertas recuperadas
    cuarentena/scott_radical_candor/desplegar_marco_franqueza_radical.json
    cuarentena/scott_radical_candor/repartir_semana_cuarenta_horas_jefe.json

    $ wc -w fuentes/scott_radical_candor/cap_0[4567].md
      6292 fuentes/scott_radical_candor/cap_04.md
      8786 fuentes/scott_radical_candor/cap_05.md
     11620 fuentes/scott_radical_candor/cap_06.md
     13706 fuentes/scott_radical_candor/cap_07.md
     40404 total

| fichero | unidad | titulo textual, de su propia cabecera | palabras | candidatos suyos en la bandeja |
|---|---|---|---:|---|
| `cap_04.md` | `Cap. 1` | Build Radically Candid Relationships | 6.292 | **seis, nacidos en `81aea10`** |
| `cap_05.md` | `Cap. 2` | Get, Give, and Encourage Guidance | 8.786 | **ninguno** |
| `cap_06.md` | `Cap. 3` | Understand What Motivates Each Person on Your Team | 11.620 | **ninguno** |
| `cap_07.md` | `Cap. 4` | Drive Results Collaboratively | 13.706 | **ninguno** |

**LO QUE ESTO DICE, Y LO DIGO SIN VER SU REPORTE: la vuelta 15 mino UNA de las
CUATRO unidades encargadas.** El encargo lo autorizaba expresamente (*"si no caben,
cierras los que quepan enteros y lo dices con su cifra"*), asi que **esto no es una
caida por si solo**; lo que comprobare en mi turno normal es que el reporte lo diga
con su cifra y no por omision. **Y la medida que el encargo pedia como nueva ya se
puede escribir: cuatro capitulos de este libro salieron a UNA unidad por vuelta,
no a cuatro, y el volumen del lote 5 se decide con eso delante.**

**LAS TRES CIFRAS DEL ASUNTO DE COMMIT QUE SI HE REMEDIDO YO:**

    $ wc -l dataset/nodos.jsonl
    203 dataset/nodos.jsonl
    $ wc -l bitacora/VEREDICTOS.jsonl
    147 bitacora/VEREDICTOS.jsonl
    $ python -c "import io,json; n=s=p=0
      for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
        d=json.loads(l); n+=1; s+=len(d['nodos_siguientes']); p+=len(d['nodos_previos'])
      print('nodos',n,'| nodos_siguientes',s,'| nodos_previos',p)"
    nodos 203 | nodos_siguientes 78 | nodos_previos 78

Las tres coinciden con el asunto, **y las aristas ademas cuadran en los dos
extremos**, que es lo que `D.1` exige y lo que el asunto no dice.

**UNA CIFRA VIEJA EN SEDE DURADERA, QUE REGISTRO Y NO ADJUDICO AQUI.** La fila del
lote 4 de `ORDEN_DE_LOTES.md` sigue diciendo lo que dijo al cerrar la vuelta 14:

    $ git log -1 --format="%h %ad" --date=format:"%m-%d %H:%M" -- docs/loop/ORDEN_DE_LOTES.md
    67eacdb 09-11 15:41
    $ grep -o "AL CIERRE DE LA VUELTA 14: [^*]*" docs/loop/ORDEN_DE_LOTES.md
    AL CIERRE DE LA VUELTA 14: 4 de 15 ficheros minados
    $ ls cuarentena/scott_radical_candor/*.json | wc -l
    8

La fila dice **4 de 15 y 2 candidatos**, y la bandeja tiene **8**. El encargo de la
vuelta 15 no mandaba tocar esa fila, asi que **no la cuento como caida de nadie**:
la registro, y actualizarla es trabajo de mi TAREA 1. Lo digo aqui para que quede
con fecha y no se descubra a mitad de la vuelta siguiente.

## 3. LA POBLACION DEL BARRIDO: `D.38.4` AL PIE DE LA LETRA, Y LOS DOS DEFECTOS QUE LA MEDIDA SACA

Corro la receta de `D.38.4` **tal como esta escrita**, y saco dos cosas que no son
opinion mia: son la salida del instrumento.

### 3.1. La receta literal mete 163 ficheros que la aritmetica de la propia regla deja fuera

    $ for d in cuarentena/*/; do echo "$d $(ls $d*.json 2>/dev/null | wc -l)"; done
    cuarentena/_derivadas/ 2
    cuarentena/_insertados/ 0
    cuarentena/ensayo_referencia_163/ 163
    cuarentena/onu_consumidor/ 0
    cuarentena/scott_radical_candor/ 8
    cuarentena/smart_who/ 0
    cuarentena/zhuo_manager/ 0

`D.38.4` manda descartar `_insertados` y `_derivadas` **y nada mas**. Con ese
filtro entra `cuarentena/ensayo_referencia_163/`, que **no es una bandeja de la
campaña: es el catalogo de control con el que esta casa mide la aduana** (163
candidatos, `D.25` lo cita por su cifra). Y existe desde antes de la regla:

    $ git log --diff-filter=A --format="%h %ad %s" --date=short -- "cuarentena/ensayo_referencia_163/" | tail -1
    00aecd5 2026-09-09 PASO 1: las cinco decisiones del fundador, escritas y con sus pruebas

**LA ARITMETICA DE LA PROPIA `D.38.4` LO EXCLUYE:** su ejemplar dice *"el extractor
barrio 203 titulos, 135 del grafo mas 68 de la bandeja"*, y el ensayo ya estaba en
el arbol el 9 de septiembre. **Si el glob literal se hubiera corrido aquel dia, la
cifra no habria sido 203.** O sea: **la receta y su ejemplar no dicen lo mismo.**

**NO LO RESUELVO COPIANDO NINGUNA DE LAS DOS LECTURAS: las corro las dos y publico
las dos.**

    $ wc -l .poblacion_literal_v16.jsonl      # grafo + todo cuarentena menos _insertados y _derivadas
    374 .poblacion_literal_v16.jsonl
    $ wc -l .poblacion_sin_ensayo_v16.jsonl   # lo mismo, quitando el catalogo de control
    211 .poblacion_sin_ensayo_v16.jsonl

### 3.2. Y el defecto gordo: la receta literal mete la bandeja que se esta barriendo

Corrida tal cual, la poblacion de 374 **contiene los 8 candidatos que el informe
va a juzgar**, asi que cada candidato choca consigo mismo y el barrido no devuelve
ni un vecino:

    $ FORJA_DATASET=.poblacion_literal_v16.jsonl python forja.py informe --carpeta cuarentena/scott_radical_candor
    candidatos revisados        : 8
    nodos en el grafo de destino: 374
    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 0   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 8
      CHOCAN entre si dentro del lote  : 0
    POR QUE GUARDA CAEN
         8  el id ya vive en el grafo

**OCHO DE OCHO CAEN POR EL PRIMER GUARDA Y LA COMPARACION DE VECINOS NO SE LLEGA A
CORRER.** No es un fallo del informe: la guarda `el id ya vive en el grafo` hace
bien su trabajo y para antes de medir. **Es la receta: un candidato no se puede
barrer contra una poblacion que lo contiene.**

**LA POBLACION QUE SI LEE, y es la unica lectura de `D.38.4` que produce
informacion:** grafo mas bandejas vivas **menos la bandeja del lote que se barre**.
Los choques dentro del lote no se pierden por eso, porque el informe los cuenta
aparte en su linea `CHOCAN entre si dentro del lote`.

    $ wc -l .poblacion_C_v16.jsonl     # grafo + bandejas vivas menos el lote propio, con el ensayo dentro
    366 .poblacion_C_v16.jsonl

Y como en esta vuelta la unica otra bandeja viva es el catalogo de control, **la
poblacion que de verdad aporta doctrina es el grafo solo**:

    $ ls cuarentena/*/*.json | grep -v _insertados | grep -v _derivadas | wc -l
    171

De esos 171, **163 son el catalogo de control y 8 son la bandeja que barro**. Asi
que en la vuelta 15 **la ampliacion de `D.38.4` no aporta ni un vecino real**, y eso
no lo supongo: lo mido en la seccion 4 corriendo el barrido con el ensayo dentro y
con el ensayo fuera. **`D.38.4` sigue teniendo razon como regla** (el 11 de
septiembre el vecino mas cercano de un candidato estaba en la bandeja); lo que digo
es que **hoy esa bandeja esta vacia porque el lote 3 ya entro**.

## 4. EL BARRIDO DE VECINOS, CON SU SALIDA LITERAL

### 4.1. Sobre el grafo solo, 203 titulos

    $ FORJA_DATASET=dataset/nodos.jsonl python forja.py informe --carpeta cuarentena/scott_radical_candor
    candidatos revisados        : 8
    nodos en el grafo de destino: 203
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 7
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 3
      por candidato bloqueado          : menor 3, mediana 3, mayor 3
      que señal levanta cada vecindad  : familia_id 2, paso_contra_nodo 1

    [ENTRARIA] ajustar_franqueza_oido_oyente   (ajustar_franqueza_oido_oyente.json)

    [BLOQUEARIA] cuidar_persona_completa_equipo   (cuidar_persona_completa_equipo.json)
        vecino usar_lenguaje_no_discriminatorio_entrevista  [levantada por: paso_contra_nodo]
          similitud_texto 0.228 | familia_id 0.000 | paso_contra_nodo 0.615
          paso 4 del candidato contra paso 1 de usar_lenguaje_no_discriminatorio_entrevista
        vecino gestionar_personas_equipo  [levantada por: familia_id]
          similitud_texto 0.243 | familia_id 0.400 | paso_contra_nodo 0.455
          paso 6 del candidato contra paso 5 de gestionar_personas_equipo
        vecino respetar_cuidar_persona_cargo  [levantada por: familia_id]
          similitud_texto 0.259 | familia_id 0.333 | paso_contra_nodo 0.425
          paso 2 del candidato contra paso 1 de respetar_cuidar_persona_cargo

    [ENTRARIA] delimitar_franqueza_radical_cinco_noes   (delimitar_franqueza_radical_cinco_noes.json)
    [ENTRARIA] desplegar_marco_franqueza_radical   (desplegar_marco_franqueza_radical.json)
    [ENTRARIA] invitar_desafio_reciproco_equipo   (invitar_desafio_reciproco_equipo.json)
    [ENTRARIA] manejar_enfado_persona_desafiada   (manejar_enfado_persona_desafiada.json)
    [ENTRARIA] repartir_semana_cuarenta_horas_jefe   (repartir_semana_cuarenta_horas_jefe.json)
    [ENTRARIA] revisar_ciclo_responsabilidades_relaciones   (revisar_ciclo_responsabilidades_relaciones.json)

*La lista literal de los siete `ENTRARIA` va aqui sin la linea en blanco que el
informe pone entre ellos, y es el unico retoque que le he hecho a una salida
pegada: no se ha cambiado ni un caracter de las lineas.*

### 4.2. Sobre grafo mas el catalogo de control, 366 titulos

    $ FORJA_DATASET=.poblacion_C_v16.jsonl python forja.py informe --carpeta cuarentena/scott_radical_candor
    candidatos revisados        : 8
    nodos en el grafo de destino: 366
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 7
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 3
      por candidato bloqueado          : menor 3, mediana 3, mayor 3
      que señal levanta cada vecindad  : familia_id 2, paso_contra_nodo 1

**MISMO SALDO, MISMOS TRES VECINOS, MISMAS DOS SEÑALES: los 163 ficheros del
catalogo de control no levantan ni una vecindad.** Eso cierra el punto 3.1 sin
tener que elegir lectura: **con ensayo o sin ensayo, el barrido de la vuelta 15 da
lo mismo, y la ambiguedad de `D.38.4` no cambia ni un veredicto aqui.**

> **UN RECORTE DE MI PROPIA SALIDA QUE DECLARO, porque callarlo seria justo la
> especie que `D.38.3` persigue.** Esta corrida de 4.2 la lance con un
> `| sed -n '1,30p'` al final, **puesto por mi**, asi que **lo que tengo pegado
> arriba es la CABECERA de su salida y no su salida entera**: el saldo y la cola de
> lectura estan completos, y la lista candidato por candidato quedo cortada en el
> segundo vecino. **La relance sin recorte** a
> `.barrido_C_con_ensayo_v16.txt`, y **al cerrar esta apertura seguia corriendo**:
> el informe tarda unos 45 segundos por candidato contra 200 nodos, medido, y contra
> 366 no llego a tiempo.
>
> **Lo que publico de 4.2 es por lo tanto: las cuatro cifras del saldo, las tres del
> recuento de vecinos y las dos señales, todas literales.** La identidad de los tres
> vecinos la sostengo **por esas lineas agregadas**, que son las mismas que en 4.1,
> **y no por haber visto las tres filas impresas dos veces.** Si al abrir mi turno
> normal el fichero completo dijera otra cosa, **la discrepancia se declara y no se
> resuelve copiando esta frase.**

## 5. MI FRONTERA DE `cap_04`, PIEZA A PIEZA

*Cortada por mi contra el texto, sin ver la del extractor. La unidad de cuenta es
la **linea de cuerpo no vacia**, que es la unica que se puede citar con `sed`. Las
siete primeras lineas son el frontmatter y no son cuerpo.*

    $ wc -l fuentes/scott_radical_candor/cap_04.md
    181 fuentes/scott_radical_candor/cap_04.md
    $ tail -n +8 fuentes/scott_radical_candor/cap_04.md | grep -c .
    87
    $ grep -n "^[A-Z][A-Z ,:’'\"“”-]*$" fuentes/scott_radical_candor/cap_04.md
    11:IT’S CALLED MANAGEMENT, AND IT’S YOUR JOB
    35:HOW TO BE A GOOD BOSS
    65:RELATIONSHIPS, NOT POWER, DRIVE YOU FORWARD
    79:RADICAL CANDOR
    95:CARE PERSONALLY: THE FIRST DIMENSION OF RADICAL CANDOR
    123:CHALLENGE DIRECTLY: THE SECOND DIMENSION OF RADICAL CANDOR
    143:WHAT RADICAL CANDOR IS NOT
    155:RADICAL CANDOR IS UNIVERSALLY HUMAN, BUT INTERPERSONALLY AND CULTURALLY RELATIVE
    181:GET, GIVE, AND ENCOURAGE GUIDANCE

**La ultima no es de este capitulo: `179` y `181` son el numero y el titulo del
capitulo siguiente, que el recorte arrastra.** Asi que las secciones de `cap_04`
son **ocho**, de `11` a `177`.

| lineas | pieza | mi clase, con la vara de `D.27` |
|---|---|---|
| 9 | el lema de la unidad, *Bringing your whole self to work* | **SIN NODO.** Es el mantra de `:113` puesto de lema |
| 11 a 33 | Juice Software, el transplante de rinon, el hijo en la UCI, el examen de matematicas, Leslie Koch y *it is your job*, y el trabajo emocional del jefe | **SIN NODO.** Narrativa mas tesis. Ni un imperativo, ni un inventario de medios. Es la pieza que justifica el libro entero y no encarga nada |
| 35 a 63 | las preguntas que le hacen, la semantica de jefe, directivo y lider, Tedlow y Andy Grove con la derecha y el reves, y las tres areas: guia, equipo y resultados, cada una desplegada en las preguntas que la gente teme | **SIN NODO.** Las tres areas son **FINES**, y la restriccion 1 de `D.27` las deja fuera: nombrar adonde hay que llegar sigue siendo nombrar. Lo que `:51`, `:55` y `:59` enumeran son **miedos y preguntas**, no medios |
| 65 a 77 | Ryan Smith de Qualtrics, la dificultad central del oficio, los **cinco estorbos** de `:69`, las **tres responsabilidades** numeradas de `:71`, el **ciclo virtuoso y el vicioso** de `:73`, la propagacion de `:75` | **NODO, Y ES EL MAS DISCUTIBLE DEL LOTE.** Mi adjudicacion razonada esta en 6.6 |
| 79 a 93 | *RADICAL CANDOR*: `:81` dice que ha identificado **dos dimensiones**, `:83` nombra `Care Personally`, `:85` nombra `Challenge Directly`, `:87` las junta y lista los cinco efectos numerados, `:89` y `:91` explican las dos palabras, `:93` los resultados al contrario de lo que temes | **SIN NODO, Y ES LA PIEZA QUE MAS FACIL HABRIA SIDO CONVERTIR EN UNO.** Los cinco numerados de `:87` son **FINES** (que hara la gente si confia en ti), restriccion 1. `:89` y `:91` son etimologia, y `:93` es pronostico. **No hay un solo medio.** Tiene consecuencia y esta en la seccion 8 |
| 95 a 105 | Moscu, 4 de julio de 1992, los diez talladores de diamantes, el picnic bajo la lona, la pregunta que de verdad importaba, y los cien millones al anio | **SIN NODO: ES UN CASO, no una casa.** Lo que la autora aprende ahi (*dar la cara personalmente*) es doctrina del nodo de la primera dimension, no un procedimiento para contratar talladores |
| 109 a 121 | la causa *keep it professional* de `:111`, el mantra de Fred Kofman y el espacio seguro de `:113`, el sentido de superioridad y *ser jefe es un puesto, no un juicio de valor* de `:115`, el *no basta con cuidar el trabajo ni la carrera* de `:117`, los **tres descartes y los cuatro medios** de `:119`, y el **precio** de `:121` | **NODO, Y EL MAS LIMPIO DEL LOTE.** `:119` pone **cuatro medios nombrados uno a uno en una sola linea**, que es el caso positivo textual de `D.27`, y ademas **tres descartes por su nombre**. Las dos causas y el precio son inventario propio del texto |
| 125 a 129 | Joshua Cohen y la cita de John Stuart Mill, mas los dos efectos numerados de `:129` | **SIN NODO.** Los dos numerados son **FINES** (que demuestra desafiar). Pero **aqui se pierde la unica cita verbatim atribuible del capitulo**, y eso lo digo en la seccion 9.3 |
| 131 | Colin Powell, *si nadie se enfada nunca contigo probablemente no desafias bastante*, y **cinco imperativos seguidos** sobre el enfado | **NODO.** Es el tramo mas literalmente procedimental del capitulo: el libro escribe los imperativos y transcribirlos es todo el trabajo |
| 133 | la parte dificil no es criticar, es **invitar a que te desafien a ti**, y la vara de *lo bastante como para que seas TU el que se moleste* | **NODO** (con `:139` y `:141`) |
| 137 a 141 | Russ y Elisse: el desafio reciproco, la regla de datos contra opiniones tomada de Jim Barksdale al reves, y el trozo de Jerry Maguire | **PARTE DEL NODO DE `:133`: es su caso, y aporta los dos unicos medios concretos** que esa pieza tiene. No es casa propia |
| 143 a 153 | *WHAT RADICAL CANDOR IS NOT*, cinco parrafos, un no por parrafo, con dos reglas ejecutables dentro: **tres cosas sin importancia sin decir cada dia** (`:147`) y **arriba, abajo y a los lados** (`:149`) | **NODO.** Cinco comprobaciones que alguien pasa sobre un caso concreto. Es inventario de **objetos de trabajo**, no de metas |
| 155 a 159 | la vara *en el oido del oyente y no en la boca del hablante*, las **tres cosas que no es**, la condicion de buena fe, y la **escala del ajuste** de persona a empresa a pais | **NODO** (con `:171`) |
| 163 a 167 | Jerusalen: Noam Bardin gritando al ingeniero, y la cena de Shabbat en casa de Jacob y Haviva Ner-David que se lo explica | **SIN NODO: CASO.** El texto no saca de ahi ni un medio, saca una reinterpretacion |
| 169 a 173 | Tokio: el equipo demasiado educado, *politely persistent*, la forma local de cada una de las dos dimensiones, y AdSense for Mobile Applications | **PARTE DEL NODO DE `:157`, y el unico caso del capitulo que SI produce medios**, porque es el unico donde el texto nombra la forma local de cada dimension por separado |
| 175 | Roy Zhou, Pekin, Yoyi Digital, la hipoteca de su casa para pagar al equipo | **SIN NODO: CASO.** Ejemplar de cuidar personalmente llevado al extremo, sin procedimiento propio |
| 177 | los britanicos mas francos que los neoyorquinos, y Tel Aviv, Tokio, Pekin y Berlin | **SIN NODO.** Observacion de cierre |

**MI CUENTA DE LA UNIDAD, en clases y no en un numero contado de memoria: seis
piezas dan nodo** (`65 a 77`, `109 a 121`, `131`, `133 mas 137 a 141`, `143 a 153`,
`155 a 159 mas 169 a 173`), **y las once restantes no.** Y **seis es exactamente lo
que la bandeja tiene de `cap_04`**, con su instrumento en la seccion 2. **Coincido
en el numero; lo que hay que comparar es si coincido en CUALES**, y eso es la
seccion 6.

## 6. MI CLASE DE CADA CANDIDATO, UNO POR UNO

*Los ocho de la bandeja, con la linea que los sostiene. **Ninguna de estas clases
la he comparado con nada**: el reporte no esta en el arbol y los borradores del
extractor no los he abierto.*

    $ python -c "import json,glob,io
      for p in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
        d=json.load(io.open(p,encoding='utf-8')); print(len(d['pasos_accionables']), d['id'])"
    8 ajustar_franqueza_oido_oyente
    10 cuidar_persona_completa_equipo
    8 delimitar_franqueza_radical_cinco_noes
    9 desplegar_marco_franqueza_radical
    7 invitar_desafio_reciproco_equipo
    7 manejar_enfado_persona_desafiada
    7 repartir_semana_cuarenta_horas_jefe
    7 revisar_ciclo_responsabilidades_relaciones

### 6.1. `desplegar_marco_franqueza_radical`, de `cap_01.md:35` y `:37`. **SOSTENIDO**

Los nueve pasos salen enteros de dos lineas. `:37` pone el inventario de medios uno
a uno (recortar del libro, fotocopiar, colocar en la nevera o encima de la mesa,
repartir entre colegas), mas **una regla de uso** (como brujula de conversaciones
concretas) y **dos prohibiciones expresas** (no como test de personalidad, no
escribir nombres en las casillas), mas la observacion de que todos caemos en cada
cuadrante varias veces al dia.

**Es el caso positivo de `D.27` sin discusion:** medios nombrados uno a uno por el
libro, y escribir los pasos es transcribirlos en imperativo. **Sostengo la misma
clase que le puse en mi apertura de la vuelta 14**, y esa es la unica comparacion
que puedo hacer en esta fase sin destapar nada.

### 6.2. `repartir_semana_cuarenta_horas_jefe`, de `cap_03.md:17`. **SOSTENIDO**

Los siete pasos salen de **una sola linea**, y el inventario lo numera el libro:
**tres partidas que suman la semana entera** (diez horas de gestion del equipo,
unas quince bloqueadas para pensar y ejecutar por cuenta propia, y las otras
quince que quedan de una semana de cuarenta). No son metas: son **reparticiones de
un objeto de trabajo**, el calendario, y por eso pasan la restriccion 1.

**Y trae la unica atribucion de cifra de verdad del lote**, con las tres
magnitudes y con su `fecha_corte` declarando que la unidad no data la cifra. Eso es
exactamente lo que el principio 5 pide.

### 6.3. `cuidar_persona_completa_equipo`, de `cap_04.md:111` a `:121`. **SOSTENIDO, Y EL MAS LIMPIO DEL LOTE**

`:119` es el ejemplar de libro de texto de `D.27`: **cuatro medios nombrados uno a
uno en una sola linea** (buscar tiempo para conversaciones de verdad, conocerse a
nivel humano, aprender que es importante para cada uno, compartir que os hace
querer levantaros por la maniana y que tiene el efecto contrario) **y tres
descartes por su nombre** en la linea anterior (memorizar cumpleanios y nombres de
familiares, contar los detalles sordidos de la vida personal, la charla forzada en
actos sociales). `:111` y `:115` ponen **las dos causas** de fallar en esto, `:117`
el *no basta con el trabajo ni con la carrera*, y `:121` **el precio**.

**Los diez pasos casan uno a uno con esas lineas y no sobra ninguno.** Es tambien
el unico candidato del lote con vecinos, y sus tres pares estan adjudicados en la
seccion 7.

> **UNA LECTURA QUE TRAIGO Y QUE NO ADJUDICO YO SOLO: la atribucion de Fred
> Kofman.** `:113` atribuye *Bring your whole self to work* a Fred Kofman, su
> entrenador en Google, y el capitulo lo pone de lema en `:9`. El paso 8 del
> candidato usa la formula **sin nombrarle**, y el candidato no lleva campo
> `atribuciones`.
>
> **Las dos lecturas del campo chocan y el choque no es mio:**
> `esquema/nodo.schema.json` describe `atribuciones` como *"Cifras del autor con su
> fuente"*, y un mantra no es una cifra; pero `censos/atribuciones.md` ya registra
> **maximas sin cifra** de Brene Brown, de Robert I. Sutton, de Ed Batista y de
> Marcus Buckingham. **Bajo la practica escrita en el censo, Kofman deberia estar;
> bajo la letra del esquema, no.** Lo traigo como lectura, no como caida, y lo
> resuelvo en el acta con el reporte delante.

### 6.4. `delimitar_franqueza_radical_cinco_noes`, de `cap_04.md:145` a `:153`. **SOSTENIDO, CON UNA OMISION QUE NOMBRO**

Cinco parrafos, un no por parrafo, y **dos de ellos traen su propia regla
ejecutable**: *deja tres cosas sin importancia sin decir cada dia* (`:147`) y
*arriba, abajo y a los lados* (`:149`). Eso convierte una lista de posturas en
**cinco comprobaciones que alguien pasa sobre un caso concreto**, que es inventario
de objetos de trabajo y no de metas.

**Y COMPRUEBO LO QUE EL PROPIO CANDIDATO DECLARA DE SI MISMO, que el libro no dice
la palabra cinco:**

    $ sed -n '143,153p' fuentes/scott_radical_candor/cap_04.md | grep -ci "five"
    0

**Es verdad, y tiene una consecuencia que el candidato no saca: este nodo NO es
cabeza de `D.37`.** `D.37` exige que la enumeracion diga **cuantas** partes hay
**y** las nombre; aqui la cuenta es del lector. Asi que si algun dia sus cinco noes
existen como nodos, la arista se declara por `D.29` **con razon escrita**, no por
transcripcion. Lo dejo apuntado antes de que alguien cite el titulo del candidato
como si la cifra fuera del libro.

> **LA OMISION, y es concreta: falta la salida que el texto recomienda.** `:149`
> cierra con *"if it's not possible to be Radically Candid with your boss and your
> peers, I'd recommend finding a different kind of work environment if at all
> possible"*. Los pasos 5 y 6 llevan el microcosmos y la cautela, **y esa
> recomendacion no esta en ningun paso.** Es un imperativo del propio libro
> (*"I'd recommend"*), asi que **mi lectura dice que deberia ser paso.** No es un
> puente, es lo contrario: es inventario del libro que el nodo no recogio.

### 6.5. `invitar_desafio_reciproco_equipo`, de `cap_04.md:133`, `:139` y `:141`. **SOSTENIDO**

`:133` dice cual es la parte dificil con sus palabras (*"The hardest part of
building this trust is inviting people to challenge you"*) y pone **la vara**: lo
bastante directamente como para que **tu** acabes molesto. `:139` y `:141` traen
los **dos unicos medios concretos** de la pieza, los dos del caso de Russ y Elisse:
la regla de datos contra opiniones y la señal explicita de que no se ha cruzado
ninguna raya.

**EL RENOMBRE DE ID QUE EL CANDIDATO DECLARA DENTRO DEL ACTO LO COMPRUEBO YO EN
GIT, no me lo creo:**

    $ git log --format="%h %ad %s" --date=format:"%H:%M" --name-status -- cuarentena/scott_radical_candor/invitar_desafio_hacia_arriba.json cuarentena/scott_radical_candor/manejar_enfado_tras_desafiar.json
    84bccb6 22:58 TAREA 2 y TAREA 3 de cap_04: los seis candidatos por la aduana uno por vez, dos caidas de regla 3 corregidas en el acto, y el cuadre de la bitacora
    D	cuarentena/scott_radical_candor/invitar_desafio_hacia_arriba.json
    D	cuarentena/scott_radical_candor/manejar_enfado_tras_desafiar.json
    81aea10 22:36 TAREA 1 CERRADA: el lote 3 entero esta en el grafo, 203 nodos, la cifra que se publico antes de insertar
    A	cuarentena/scott_radical_candor/invitar_desafio_hacia_arriba.json
    A	cuarentena/scott_radical_candor/manejar_enfado_tras_desafiar.json

**Los dos ids viejos nacieron y murieron dentro de la vuelta 15, y los dos llevaban
preposicion: `hacia` y `tras`.** La regla 3 de `docs/REGLAS_DE_ID.md` los tumba, y
**el candidato declara la caida en vez de esconderla**, que es lo que `D.23` pide.
Ninguno vivio en el grafo, asi que no guardarlos como alias es lo correcto y no
hay nada que resolver.

> **EL PASO DE PEOR FIDELIDAD DEL LOTE ES EL 3 DE ESTE NODO, y lo digo aunque no
> llegue a puente.** Dice *"sobre todo con quien acaba de llegar y con quien te
> tiene por jefe: el texto lo dice de los dos"*. Las dos condiciones si estan
> nombradas (`:137` dice que Elisse era nueva y que Russ era su jefe; `:139` dice
> *"irrespective of reporting relationship"*), **pero el *sobre todo* es una
> ponderacion que el texto no pone**: la ponderacion que `:133` pone es otra,
> *"particularly for more authoritarian leaders"*. **Mi clase: TRANSCRIPCION AL
> LIMITE, no puente.** Lo dejo nombrado para releerlo contra su marca.

### 6.6. `manejar_enfado_persona_desafiada`, de `cap_04.md:131`. **SOSTENIDO, Y EL MAS LITERAL DEL CAPITULO**

Una sola linea con **cinco imperativos seguidos**: reconoce el dolor, no finjas que
no duele ni digas que no deberia doler, elimina del vocabulario *don't take it
personally*, ofrecete a ayudar a arreglar el problema, y no finjas que no hay
problema. Los siete pasos son esos cinco mas las dos premisas de la misma linea
(que a veces se van a enfadar contigo, y que si nadie se enfada nunca probablemente
no desafias bastante).

**Aqui no hay nada que adjudicar: transcribir es todo el trabajo.** Es el nodo que
usaria de control si alguien dudara de que este capitulo da procedimiento.

**Y su atribucion de Colin Powell la sostengo**, aunque la descripcion del esquema
diga *cifras*: el censo ya lleva maximas sin cifra, y la practica escrita manda
sobre la descripcion de un campo. Su `fecha_corte` declara que el libro remite a
una nota numerada que el recorte no trae, **y eso se ve en el propio texto**, que
corta con un `1` pegado a *pissing people off*.

### 6.7. `ajustar_franqueza_oido_oyente`, de `cap_04.md:157`, `:159` y `:171`. **SOSTENIDO**

`:157` pone **la vara de medida** (en el oido del que escucha y no en la boca del
que habla), **las tres cosas que no es** (tipo de personalidad, talento, juicio
sobre una cultura) y **la condicion de buena fe**. `:159` pone **la escala del
ajuste**, ordenada de menos a mas. `:171` es el unico de los cuatro casos del
capitulo que produce medios, porque es el unico donde el texto nombra **la forma
local de cada una de las dos dimensiones por separado**: educados para cuidar,
persistentes para desafiar, y el nombre cambiado porque *franqueza radical* habria
sonado demasiado agresivo.

**Los otros tres casos (Jerusalen, la cena de Shabbat, Pekin) quedan fuera de los
pasos y eso es correcto**: ninguno nombra la forma local de una dimension, nombran
una reinterpretacion o un ejemplar. El candidato lo declara asi en su
`resumen_teorico` y **mi lectura independiente coincide**.

> **Los pasos 6 y 7 son el borde de la vara, y lo digo yo:** el imperativo *"Busca
> la forma local"* es del extractor y el objeto es del libro. `:171` cuenta lo que
> ella hizo en Tokio, no encarga buscarlo. **Mi clase sigue siendo TRANSCRIPCION**
> porque `D.30` marca transcripcion cuando el libro pone **el medio, la etapa o el
> objeto**, y el objeto esta nombrado. **Y el propio candidato declara el hueco que
> lo delata**: dice que el texto no dice como se averigua esa forma local antes de
> equivocarse. **Un nodo que declara lo que su libro no dice es mas facil de
> auditar que uno que lo rellena.**

### 6.8. `revisar_ciclo_responsabilidades_relaciones`, de `cap_04.md:69` a `:75`. **EL DISCUTIBLE DEL LOTE. MI CLASE: SOSTENIDO PERO DEBIL, Y DIGO SOBRE QUE SE SOSTIENE**

Este es el unico de los ocho donde la vara de `D.27` se puede leer en los dos
sentidos, asi que lo adjudico por partes y digo cual parte aguanta.

| lo que el nodo usa | mi clase de esa parte |
|---|---|
| `:69`, **los cinco estorbos nombrados uno a uno** (dinamicas de poder en primer lugar, miedo al conflicto, preocupacion por los limites de lo apropiado, miedo a perder credibilidad, presion del tiempo) | **PROCEDIMIENTO.** Es la forma exacta del parrafo 26 de la tabla de `D.27`: una lista nombrada que alguien recorre contra su propio caso |
| `:71`, **las tres responsabilidades numeradas** | **POSTURA, y la restriccion 1 la tumba.** Son FINES, y ademas **son los titulos de los tres capitulos siguientes** |
| `:73`, **el ciclo virtuoso y el vicioso, tres mas tres** | **PROCEDIMIENTO, por los pelos.** El texto los escribe como MEDIOS (*"You strengthen your relationships BY learning..., BY putting..., BY achieving..."*), y los escribe **en este capitulo y no en los siguientes** |
| `:75`, la propagacion a las relaciones de sus reportes | **POSTURA.** Consecuencia, no medio |

**LA COMPROBACION QUE DECIDE, Y NO ES UNA OPINION MIA:**

    $ grep -n "titulo_textual" fuentes/scott_radical_candor/cap_0[567].md
    fuentes/scott_radical_candor/cap_05.md:5:titulo_textual: Get, Give, and Encourage Guidance
    fuentes/scott_radical_candor/cap_06.md:5:titulo_textual: Understand What Motivates Each Person on Your Team
    fuentes/scott_radical_candor/cap_07.md:5:titulo_textual: Drive Results Collaboratively

**Dos de las tres responsabilidades de `:71` son PALABRA POR PALABRA el titulo de
un capitulo que viene despues** (*Understand What Motivates Each Person on Your
Team* y *Drive Results Collaboratively*), **y una de las tres piezas del ciclo
virtuoso de `:73` tambien** (*get, give, and encourage guidance*). O sea: **el paso
3 de este candidato es el indice del libro**, y el indice es el caso literal de
*NOMBRAR NO ES PROCEDIMENTAR*: el texto nombra el procedimiento de otro y remite.

> **MI ADJUDICACION, con su condicion escrita:** el nodo **se sostiene**, y se
> sostiene **sobre `:69` y sobre `:73`, no sobre `:71`**. Si alguien lo defendiera
> por las tres responsabilidades, **caeria**, porque esa es la mitad que remite a
> otros capitulos.
>
> **Y DIGO QUE LO HARIA CAER, para que se me pueda contradecir:** si la lectura de
> `:73` es que sus tres piezas son los mismos tres titulos dichos de otra forma,
> entonces lo que queda del nodo son **cinco estorbos y nada mas**, y cinco
> estorbos solos son un nodo delgado. **Ese es el unico camino por el que este
> nodo cae, y no veo otro.** El extractor tiene derecho a defenderlo o a tirarlo
> con esa frase delante.

**Y SOSTENGO ADEMAS UNA CORRECCION QUE EL CANDIDATO SE HIZO A SI MISMO.** Su
`resumen_teorico` declara que en el borrador emparejo cada responsabilidad con su
forma virtuosa y su forma viciosa una a una, y que **retiro el emparejamiento al
pasar la relectura de fidelidad**, porque el texto pone las tres listas en el mismo
orden pero no dice que la pieza primera de una sea la forma de la pieza primera de
otra. **Mi lectura independiente lo confirma:** la segunda responsabilidad de `:71`
es *entender que motiva a cada uno*, y la segunda pieza del ciclo virtuoso de `:73`
es *poner a la gente adecuada en el papel adecuado*, **y no son lo mismo**. Esa
correccion estaba bien hecha, y lo digo yo que vengo a buscarle fallos.

## 7. EL UNICO CANDIDATO CON VECINOS, Y MIS TRES ADJUDICACIONES

*Metodo de `AUDITOR_FORJA.md` 1.2: imprimo primero los pasos de los dos nodos del
par, adjudico con la vara, y **SOLO DESPUES** se destapa la razon escrita en
`bitacora/VEREDICTOS.jsonl`. **Aqui no hay nada que destapar, y lo compruebo en vez
de suponerlo:***

    $ for i in <los ocho ids de la bandeja>; do printf "%-46s %s\n" "$i" "$(grep -c "$i" bitacora/VEREDICTOS.jsonl)"; done
    ajustar_franqueza_oido_oyente                  0
    cuidar_persona_completa_equipo                 0
    delimitar_franqueza_radical_cinco_noes         0
    desplegar_marco_franqueza_radical              0
    invitar_desafio_reciproco_equipo               0
    manejar_enfado_persona_desafiada               0
    repartir_semana_cuarenta_horas_jefe            0
    revisar_ciclo_responsabilidades_relaciones     0

**Ninguno de los ocho ids del lote 4 aparece en la bitacora**, que es lo coherente
con que el lote este abierto y sin insertar. **Asi que mis tres adjudicaciones de
abajo no tienen con que contaminarse: no existe todavia el veredicto que releo.**

### 7.1. El par de `paso_contra_nodo 0.615`: **SANO, Y LA SEÑAL SE DISPARO CON LA PROSA DE LA CASA**

| | |
|---|---|
| candidato | `cuidar_persona_completa_equipo`, paso 4 |
| vecino | `usar_lenguaje_no_discriminatorio_entrevista` (`smart_who`), paso 1 |
| señal | `paso_contra_nodo 0.615`, la mas alta de las tres. `familia_id 0.000` |

    paso 4 del candidato : Busca tiempo para conversaciones de verdad, que es el primero de los medios que el texto nombra.
    paso 1 del vecino    : Usa lenguaje no discriminatorio durante las entrevistas, que es el primero de los dos sitios que el libro nombra.

**MI CLASE: `SANO`, y no por poco: no hay relacion de ninguna clase.** Uno es cuidar
personalmente a una persona a cargo; el otro es limpiar de sesgo los formularios de
un proceso de contratacion.

> **LO QUE ESTE PAR MIDE NO ES EL PAR: ES LA SEÑAL.** Lo que las dos lineas
> comparten no es doctrina, es **la formula de redaccion de esta casa**: *"que es el
> primero de los medios que el texto nombra"* contra *"que es el primero de los dos
> sitios que el libro nombra"*. **La señal mas fuerte del barrido se disparo con el
> estilo del extractor, no con el contenido del libro.**
>
> **Y esto va a empeorar solo, sin que nadie haga nada mal**, porque esa formula es
> justamente la que `D.27` premia: todo nodo bien extraido la lleva. `D.19` ya tiene
> medido que ninguna señal separa jerarquia de ruido; **este ejemplar aniade que el
> ruido lo fabrica la propia convencion de escritura.** Lo traigo al acta como dato,
> **sin encargar maquinaria**, que la moratoria de 5.6 prohibe.

### 7.2. El par de `familia_id 0.400`: **`CONTINUA`, madre `gestionar_personas_equipo`. DISCUTIBLE**

| | |
|---|---|
| candidato | `cuidar_persona_completa_equipo`, paso 6 |
| vecino | `gestionar_personas_equipo` (`zhuo_manager`), paso 5 |
| señal | `familia_id 0.400`, `paso_contra_nodo 0.455` por debajo del umbral |

El vecino es una **cabeza**: su `entregable_esperado` dice *"con los cuatro frentes
atendidos"* y los nombra (relaciones de confianza, fuerzas y debilidades conocidas,
decisiones sobre quien hace que, cada persona entrenada). Su paso 2 es
**desarrolla relaciones de confianza con ellos**, y ahi se queda: **lo nombra y no
lo procedimenta.**

**MI CLASE: `CONTINUA`, con la madre en el vecino y el hijo en el candidato, y
declarada por `D.29` y no por `D.37`.** No por `D.37` porque el candidato **no es
una de las cuatro partes nombradas**: es un medio para la primera. Por `D.29` con
razon escrita, y la razon es la vara: **el hijo trae procedimiento propio donde la
madre solo pone el nombre** (cuatro medios de cuidar, tres descartes, dos causas y
un precio, todos del libro de Scott, ninguno en el de Zhuo).

**LO MARCO DISCUTIBLE y digo por que:** *cuidar personalmente* no es *relacion de
confianza*, es **una de las dos dimensiones** con las que Scott la construye. La
cobertura es parcial, y una cobertura parcial es mas facil de discutir que una
total. **No la convierto en `SANO` por eso** (la parcialidad no rompe el `CONTINUA`:
lo rompe que el hijo no aniada procedimiento, y aniade).

### 7.3. El par de `familia_id 0.333`: **`CONTINUA`, madre `respetar_cuidar_persona_cargo`. EL PAR DE VERDAD DEL LOTE**

| | |
|---|---|
| candidato | `cuidar_persona_completa_equipo`, paso 2 |
| vecino | `respetar_cuidar_persona_cargo` (`zhuo_manager`), paso 1 |
| señal | `familia_id 0.333`, **la mas debil de las tres** |

**ESTE ES EL PAR QUE UNA VARA TIENE QUE ADJUDICAR, y lo levanto la señal mas floja
del barrido.** El solape es grande y real:

| lo que dicen los dos | donde |
|---|---|
| aprender que le importa a la persona | paso 5 del vecino contra paso 6 del candidato |
| no somos personas distintas en el trabajo y en casa | paso 6 del vecino contra pasos 3 y 8 del candidato |
| cuidar no es darle siempre la razon ni excusar sus errores | paso 3 del vecino contra el paso 10 del candidato, *preparado para que te odien* |

**Y AUN ASI MI CLASE ES `CONTINUA` Y NO `REPITE`, por la letra de la vara: NO HAY
BASCULA. Lo que decide es si lo que queda FUERA es procedimiento en los dos lados.**

| fuera, del lado del vecino | fuera, del lado del candidato |
|---|---|
| no intentes fingirlo, porque el cuerpo te delata | los cuatro medios de `:119`, tres de ellos sin pareja enfrente |
| el respeto incondicional, con su prueba dificil: que pasa cuando la persona se atasca | los tres descartes con nombre: cumpleanios, detalles sordidos, charla forzada |
| lo que esta en juego: si tu apoyo parece condicional, no te dira la verdad | las dos causas de fallar: el mandato de mantenerlo profesional y el sentido de superioridad |
| *gestionar es cuidar*, la leccion del directivo veterano | *ser jefe es un puesto de trabajo, no un juicio de valor* |

**Procedimiento en los dos lados, y no poco: NO ES DUPLICADO.** La direccion la
manda la vara (que aniade el HIJO a la MADRE, nunca al reves): el candidato aniade
**los medios y los descartes**, que el vecino no tiene. **Madre
`respetar_cuidar_persona_cargo`, hijo `cuidar_persona_completa_equipo`, por `D.29`
con razon escrita.**

**Y NO ES FRONTERA DECLARADA**, que era la otra salida: las dos doctrinas **no se
contradicen**, dicen lo mismo con inventarios distintos. Una frontera pide dos
posiciones incompatibles, y aqui no hay ninguna.

> **LA LECTURA QUE ESTE PAR REGALA, y es la mas util del barrido entero:** la señal
> **mas fuerte** (`0.615`) encontro **ruido de estilo**, y la señal **mas debil**
> (`0.333`) encontro **el unico par que habia que leer**. Es `D.3` y `D.19` otra vez,
> ahora con tres pares y sus tres numeros al lado: **las señales ordenan, nunca
> deciden.**

## 8. LAS ARISTAS QUE MI LECTURA VE Y QUE NINGUNA SEÑAL LEVANTA

**PRIMERO, LO QUE NO ES UN DEFECTO, para no publicar un hallazgo falso:** los ocho
candidatos no declaran ni una arista, y **esta bien que no la declaren.**

    $ python -c "import io,json,glob
      for q in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
        d=json.load(io.open(q,encoding='utf-8'))
        print('%-46s previos=%d siguientes=%d alias=%d'%(d['id'],len(d['nodos_previos']),len(d['nodos_siguientes']),len(d['ids_alias'])))"
    ajustar_franqueza_oido_oyente                  previos=0 siguientes=0 alias=0
    cuidar_persona_completa_equipo                 previos=0 siguientes=0 alias=0
    delimitar_franqueza_radical_cinco_noes         previos=0 siguientes=0 alias=0
    desplegar_marco_franqueza_radical              previos=0 siguientes=0 alias=0
    invitar_desafio_reciproco_equipo               previos=0 siguientes=0 alias=0
    manejar_enfado_persona_desafiada               previos=0 siguientes=0 alias=0
    repartir_semana_cuarenta_horas_jefe            previos=0 siguientes=0 alias=0
    revisar_ciclo_responsabilidades_relaciones     previos=0 siguientes=0 alias=0

`D.29` y `D.37` escriben la arista **en el acto de insertar**, y el lote 4 esta
**ABIERTO**, asi que por `D.39` nada suyo entra todavia. **Cero aristas en la
bandeja es el estado correcto.** Lo que sigue es la lista de lo que se va a DEBER
el dia que entren, medida ahora para que no se descubra entonces.

### 8.1. La serie de las DOS DIMENSIONES existe, dice cuantas y las nombra

    $ grep -no "two dimensions" fuentes/scott_radical_candor/cap_04.md
    81:two dimensions
    $ grep -no "BOTH DIMENSIONS" fuentes/scott_radical_candor/cap_04.md
    157:BOTH DIMENSIONS

`:81` dice **dos**, `:83` nombra `Care Personally`, `:85` nombra `Challenge
Directly`. **Eso es `D.37` al pie de la letra: dice cuantas partes hay y las
nombra.**

> **Y AQUI ESTA EL HALLAZGO ESTRUCTURAL DE MI LECTURA: la cabeza de esa serie no es
> un nodo.** `:79` a `:93` es la pieza que clasifique **SIN NODO** en la seccion 5,
> porque sus cinco numerados son fines y no tiene un solo medio. **Asi que la serie
> mejor declarada del capitulo no tiene madre que la cuelgue.**

**LA MADRE QUE SI EXISTE es `ajustar_franqueza_oido_oyente`**, porque `:157` abre
*BOTH DIMENSIONS* y sus pasos 6 y 7 dicen *la primera dimension* y *la segunda*:
**tambien dice cuantas y las nombra.** Y la parte que existe como nodo es
`cuidar_persona_completa_equipo`, **la primera dimension**.

| arista que se debera al insertar | por que regla |
|---|---|
| madre `ajustar_franqueza_oido_oyente`, hijo `cuidar_persona_completa_equipo` | **`D.37`**: la cabeza dice dos y las nombra, y la primera existe como nodo |

**Y DIGO EXPRESAMENTE LO QUE NO SE DEBE, que es la otra mitad: la SEGUNDA dimension
NO tiene nodo.** `invitar_desafio_reciproco_equipo` y
`manejar_enfado_persona_desafiada` son piezas **dentro** de `Challenge Directly`,
ninguna **es** la dimension. Asi que esa arista **no existe y no se debe**, y lo
escribo para que nadie la invente por simetria.

### 8.2. La serie de las TRES RESPONSABILIDADES tambien existe, y sus partes son tres capitulos sin minar

`:71` dice **tres** y las nombra, y la seccion 6.8 ya probo que dos de las tres son
palabra por palabra los titulos de `cap_06` y `cap_07`. **`revisar_ciclo_responsabilidades_relaciones`
es por lo tanto cabeza de `D.37` de lo que salga de `cap_05`, `cap_06` y `cap_07`.**

**Hoy no se debe nada porque esos tres capitulos no estan minados** (seccion 2).
**El dia que se minen, esa arista nace con ellos**, y el que la escriba tendra que
decidir a que nodo de cada capitulo apunta. **Lo dejo escrito con fecha: es la deuda
mas grande que este lote esta acumulando, y nace de que la vuelta corrio a una
unidad en vez de a cuatro.**

### 8.3. Y una que NO se debe, aunque el titulo del candidato invite a creerlo

`delimitar_franqueza_radical_cinco_noes` **no es cabeza de `D.37`**, porque el libro
no dice la palabra *cinco* (6.4, con su `grep -c` dando `0`). Si sus noes llegaran
a ser nodos, **la arista iria por `D.29` con razon escrita.**

## 9. LA FIDELIDAD: MI LECTURA CIEGA DE LOS PASOS, PASO POR PASO

    $ python -c "import json,io
      seis=['ajustar_franqueza_oido_oyente','cuidar_persona_completa_equipo','delimitar_franqueza_radical_cinco_noes','invitar_desafio_reciproco_equipo','manejar_enfado_persona_desafiada','revisar_ciclo_responsabilidades_relaciones']
      print(sum(len(json.load(io.open('cuarentena/scott_radical_candor/%s.json'%i,encoding='utf-8'))['pasos_accionables']) for i in seis))"
    47

**LOS PASOS ESCRITOS EN `cap_04` SON 47**, y ese es el denominador de la metrica de
`AUDITOR_FORJA.md` seccion 8. La bandeja entera, con los dos candidatos de la vuelta
14 dentro, lleva 63 (seccion 6).

### 9.1. Lo que puedo firmar ahora y lo que no

**`8.3` me obliga a decir lo que no puedo verificar, y lo digo:** el numerador de
`PASOS INVENTADOS POR CAPITULO` es **la marca TRANSCRIPCION o PUENTE que el
extractor puso paso por paso**, y esa marca vive en su reporte, que no esta en el
arbol. **No puedo firmar su cifra en esta fase y no la publico.**

**Lo que SI he hecho, y es lo que esta fase vale para:** he leido los 47 pasos
contra su linea, uno por uno, **sin su marca delante**. Y mi resultado es una clase,
no un porcentaje:

> **NI UNO DE LOS 47 PASOS LO PUEDO CITAR COMO PUENTE.** No hay ninguno del que
> pueda decir *"el libro no dice esto"* senialando una linea. Es un capitulo de
> inventario rico, y `D.30` ya lo predijo: **el puente sube cuando baja el
> inventario del parrafo**, y aqui `:119`, `:131`, `:147`, `:157` y `:171` traen su
> inventario puesto.

### 9.2. Y NOMBRO LOS TRES PASOS DEL BORDE, porque son donde el error que la metrica invita se cometeria

`8.3` avisa de que **el error que esta metrica invita es marcar un puente como
transcripcion**, porque baja la cifra y sube el volumen del lote siguiente. Si ese
error se cometio en `cap_04`, esta en uno de estos tres y en ninguno mas:

| paso | por que esta en el borde | mi clase |
|---|---|---|
| `invitar_desafio_reciproco_equipo`, paso 3 | el *sobre todo* es una ponderacion que el texto no pone, y la que si pone es otra | **TRANSCRIPCION AL LIMITE** |
| `ajustar_franqueza_oido_oyente`, paso 6 | el imperativo *Busca la forma local* es del extractor; el objeto, de `:171` | **TRANSCRIPCION** |
| `ajustar_franqueza_oido_oyente`, paso 7 | igual que el anterior, con la segunda dimension | **TRANSCRIPCION** |

**Esos tres son la muestra que voy a releer contra su marca en mi turno normal**, y
los dejo escritos AQUI, antes de ver su marca, para que la comparacion sirva de
algo. **Una muestra elegida despues de ver la respuesta no mide nada.**

### 9.3. Una perdida del capitulo que no es de nadie y que registro

`:125` y `:127` traen **la unica cita verbatim atribuible de `cap_04`**: Joshua
Cohen citando a John Stuart Mill sobre que lo respetable del hombre es que sus
errores son corregibles. **Esa pieza no produce nodo en mi lectura** (sus dos
numerados de `:129` son fines), **y una atribucion sin nodo no tiene sede**: el
censo de atribuciones lo escribe la aduana al insertar un nodo.

**No es una caida de nadie y no la cuento como tal.** Es una perdida estructural de
la forma de trabajar de esta casa, y la escribo con fecha porque **una perdida que
nadie anota se vuelve invisible en la vuelta siguiente.**

## 10. LO QUE TRAIGO AL ACTA, Y CON QUE ME VOY A COMPARAR

**Mis clases, para que la comparacion sea de una sola pasada:**

| candidato | mi clase | mi veredicto por vecino |
|---|---|---|
| `desplegar_marco_franqueza_radical` | **NODO SOSTENIDO** | sin vecino |
| `repartir_semana_cuarenta_horas_jefe` | **NODO SOSTENIDO** | sin vecino |
| `cuidar_persona_completa_equipo` | **NODO SOSTENIDO**, el mas limpio | `SANO` contra `usar_lenguaje_no_discriminatorio_entrevista`; **`CONTINUA`** bajo `respetar_cuidar_persona_cargo`; **`CONTINUA`** bajo `gestionar_personas_equipo`, discutible |
| `delimitar_franqueza_radical_cinco_noes` | **NODO SOSTENIDO**, con una omision nombrada | sin vecino |
| `invitar_desafio_reciproco_equipo` | **NODO SOSTENIDO** | sin vecino |
| `manejar_enfado_persona_desafiada` | **NODO SOSTENIDO**, el mas literal | sin vecino |
| `ajustar_franqueza_oido_oyente` | **NODO SOSTENIDO** | sin vecino |
| `revisar_ciclo_responsabilidades_relaciones` | **NODO SOSTENIDO PERO DEBIL**, y digo sobre que | sin vecino |

**Las seis piezas de `cap_04` que doy por NODO son las seis que hay en la bandeja**
(seccion 5), **y las once que doy por SIN NODO no tienen candidato.** O sea: en
CUALES coincidimos, no solo en cuantos. **Lo que no se es su razon, y eso es lo que
el reporte me va a decir.**

**LOS SEIS PUNTOS QUE LLEVO A LA RELECTURA CONJUNTA, en orden de lo que me importa:**

1. **`revisar_ciclo_responsabilidades_relaciones`**: yo lo sostengo sobre `:69` y
   `:73` y **no sobre `:71`**, que es el indice del libro. Quiero ver sobre que lo
   sostiene el.
2. **La omision de `:149`** en `delimitar_franqueza_radical_cinco_noes`: el libro
   recomienda buscar otro sitio donde trabajar y el nodo no lo lleva.
3. **La atribucion de Fred Kofman** que falta en `cuidar_persona_completa_equipo`,
   con el choque entre la letra del esquema y la practica del censo.
4. **`D.38.4` tiene dos defectos de receta**, los dos medidos en la seccion 3: mete
   un catalogo de control de 163 ficheros que su propia aritmetica excluye, y mete
   la bandeja que se esta barriendo, con lo que el barrido literal devuelve **ocho
   caidas y cero vecinos**. La lectura que lee es **grafo mas bandejas menos el lote
   propio**, y esta corrida.
5. **La señal mas fuerte del barrido se disparo con la prosa de la casa** y la mas
   debil encontro el unico par de verdad. Dato para `D.19`, **sin encargo de
   maquinaria**.
6. **La vuelta mino una unidad de las cuatro encargadas**, y eso arrastra la deuda
   de aristas de la seccion 8.2 y decide el volumen del lote 5.

**Y DOS COSAS QUE NO PUBLICO COMO MIAS, y las repito aqui para que no se me olvide
en el acta:** cuantas guardas estan en verde y cuantos discutibles marco el
extractor. **Las lei en el asunto de un commit y no las he medido.**

---

## 11. LAS CITAS DE LINEA, CON SU `sed` PEGADO AL LADO (`D.35`)

*Toda linea que esta apertura cita va aqui con la salida literal de su `sed`. **El
corte de la linea se adelanta cuando el original trae un guion largo o medio**,
porque este fichero lo barre `forja.py guiones` y `D.20` no perdona la sede propia
de la casa: el corte se declara aqui y no se sustituye el caracter por otro.*

### `cap_04.md`

    $ sed -n '9p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Bringing your whole self to work
    $ sed -n '69p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Very few people focus first on the central difficulty of management that Ryan hit on: establishing a trusting relationship with each person who reports directly to you. I
    $ sed -n '71p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Nevertheless, these relationships are core to your job. They determine whether you can fulfill your three responsibilities as a manager: 1) to create a culture of guidanc
    $ sed -n '73p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      There is a virtuous cycle between your responsibilities and your relationships. You strengthen your relationships by learning the best ways to get, give, and encourage gu
    $ sed -n '81p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      DEVELOPING TRUST IS not simply a matter of “do x, y, and z, and you have a good relationship.” Like all human bonds, the connections between bosses and the people who rep
    $ sed -n '83p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      The first dimension is about being more than “just professional.” It’s about giving a damn, sharing more than just your work self, and encouraging everyone who reports to
    $ sed -n '85p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170   [corte adelantado: la linea sigue con un guion largo]
      The second dimension involves telling people when their work isn’t good enough
    $ sed -n '87p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      “Radical Candor” is what happens when you put “Care Personally” and “Challenge Directly” together. Radical Candor builds trust and opens the door for the kind of communic
    $ sed -n '95p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      CARE PERSONALLY: THE FIRST DIMENSION OF RADICAL CANDOR
    $ sed -n '111p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Part of the reason why people fail to “care personally” is the injunction to “keep it professional.” That phrase denies something essential. We are all human beings, with
    $ sed -n '113p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Fred Kofman, my coach at Google, had a mantra that contradicted the “just professional” approach so destructive to so many managers: “Bring your whole self to work.” This
    $ sed -n '115p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      In addition to the obsessive devotion to “professionalism,” there’s another, less virtuous reason why people fail to “care personally.” When they become a boss, some peop
    $ sed -n '117p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Caring personally is the antidote to both robotic professionalism and managerial arrogance. Why do I say “caring personally” instead of just “caring”? Because it’s not en
    $ sed -n '119p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Caring personally is not about memorizing birthdays and names of family members. Nor is it about sharing the sordid details of one’s personal life, or forced chitchat at
    $ sed -n '121p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      It isn’t simply a matter of allowing your approach to your responsibilities to show that you care, however; you must also care deeply about people while being prepared to
    $ sed -n '123p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      CHALLENGE DIRECTLY: THE SECOND DIMENSION OF RADICAL CANDOR
    $ sed -n '125p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      THE PHILOSOPHER JOSHUA Cohen, who taught executives at Twitter and Apple and students at Stanford and MIT, does a great job of explaining why challenging each other is es
    $ sed -n '127p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      The source of everything respectable in man either as an intellectual or as a moral being [is] that his errors are corrigible. He is capable of rectifying his mistakes, b
    $ sed -n '129p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Challenging others and encouraging them to challenge you helps build trusting relationships because it shows 1) you care enough to point out both the things that aren’t g
    $ sed -n '131p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Former Secretary of State Colin Powell once remarked that being responsible sometimes means pissing people off.1 You have to accept that sometimes people on your team wil
    $ sed -n '133p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      The “challenge directly” part of this program can be particularly difficult, especially at the outset. You may have to criticize somebody’s work or change their role whil
    $ sed -n '139p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Building enough trust between people to enable reciprocal challenge irrespective of reporting relationship takes time and attention. I saw a winning moment in building th
    $ sed -n '141p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170   [corte adelantado: la linea sigue con un guion largo]
      Emboldened, the next time she argued her perspective she did so even more forcefully
    $ sed -n '143p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      WHAT RADICAL CANDOR IS NOT
    $ sed -n '145p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      WE TALKED ABOUT the importance of humility. Radical Candor is not a license to be gratuitously harsh or to “front-stab.” It’s not Radical Candor just because you begin wi
    $ sed -n '147p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170   [corte adelantado: la linea sigue con un guion largo]
      Radical Candor is also not an invitation to nitpick. Challenging people directly takes real energy
    $ sed -n '149p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Radical Candor is not a hierarchical thing. To be Radically Candid, you need to practice it “up,” “down,” and “sideways.” Even if your boss and peers have not bought in t
    $ sed -n '151p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Radical Candor is not about schmoozing, nor is it about endless extroversion that exhausts the introverts on your team or wears you out if you happen to be the introvert.
    $ sed -n '153p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Radical Candor is not unique to the culture in Silicon Valley, nor is it uniquely American. It’s human. In fact, it was while working for an Israeli company that I began
    $ sed -n '155p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      RADICAL CANDOR IS UNIVERSALLY HUMAN, BUT INTERPERSONALLY AND CULTURALLY RELATIVE
    $ sed -n '157p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      BOTH DIMENSIONS OF Radical Candor are sensitive to context. They get measured at the listener’s ear, not at the speaker’s mouth. Radical Candor is not a personality type
    $ sed -n '159p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      We have to be constantly aware of the fact that what seemed Radically Candid to one person or team may feel too obnoxious (or too touchy-feely) to another. Radical Candor
    $ sed -n '171p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Trying to get the team in Tokyo to challenge authority the way Noam Bardin did in Jerusalem wouldn’t have worked. The kind of argument that would be taken as a sign of re
    $ sed -n '175p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      Another of my favorite Radical Candor stories is that of Roy Zhou, who worked for Russ and led the AdSense team in China. At first he was extremely deferential to Russ an
    $ sed -n '177p' fuentes/scott_radical_candor/cap_04.md | cut -c1-170
      I’ve led teams all over the world. The most surprising thing I’ve learned is that Brits, despite all their politeness, tend to be even more candid than New Yorkers. This

### `cap_01.md`

    $ sed -n '35p' fuentes/scott_radical_candor/cap_01.md | cut -c1-170
      Since the term “Radical Candor” has entered the lexicon, I’m stuck with the task of rebranding the word “radical.” You are not. That would be a pain, and I’m trying to ma
    $ sed -n '37p' fuentes/scott_radical_candor/cap_01.md | cut -c1-170
      Use THE RADICAL CANDOR Framework like a compass to guide individual conversations to a better place. Please do NOT use it as a personality test to judge yourself or other

### `cap_03.md`

    $ sed -n '17p' fuentes/scott_radical_candor/cap_03.md | cut -c1-170
      As you read on, you might occasionally feel overwhelmed by the number of things I’m suggesting you do as a manager. Take a deep breath. My goal is to save you time, not t

---

**FIN DE LA APERTURA CIEGA DE LA VUELTA 15.** No he commiteado nada y no vuelvo a
tocar este fichero: **lo sella el arnes y lo commitea el**, y un sello roto detiene
la corrida.
