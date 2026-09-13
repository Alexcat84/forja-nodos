# APERTURA CIEGA DEL AUDITOR, VUELTA 25

*Lote 5 (`marquet_turn_the_ship`), `cap_01` y `cap_02`, mas la tanda de insercion del lote 4.
Escrita ANTES de ver `docs/loop/REPORTE.md`, que no esta en el arbol y que no he recuperado.
Todas mis salidas de esta fase quedan en `.t1_v26_auditor/`.*

---

## 0. LA DECLARACION QUE `D.40` EXIGE, Y VA PRIMERA

    ACTA ANTERIOR LEIDA: 840f4ca3ba40a4503fb8a4df8e89c4c875cd6337

**Y no lo afirmo, lo mido**, porque `D.40` dice que decir que leiste otra version no es haberla
leido:

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    840f4ca3ba40a4503fb8a4df8e89c4c875cd6337

**HEREDADO 1: CUMPLIDO.**
**HEREDADO 2: CUMPLIDO.**
**HEREDADO 3: CUMPLIDO.**
**HEREDADO 4: CUMPLIDO.**
**HEREDADO 5: CUMPLIDO.**

### 0.1. Y uno por uno, porque una lista de cinco `CUMPLIDO` no es una declaracion

| heredado | que pedia | como quedo hoy |
|---|---|---|
| **1**, `REMEDIO ROTO` de la vuelta 24 | no volver a leer razones antes de imprimir pasos | **CUMPLIDO. Lo primero que corri en esta fase, antes de abrir un solo fichero de trabajo, fue el extractor de pares sin la columna `razon` y el impresor de pasos** (`1`). **No he abierto `bitacora/VEREDICTOS.jsonl` con `razon` en ninguna lectura de esta fase**, ni con `veredicto` |
| **2**, declarar tambien los remedios que aguantan | decir cuando un remedio aguanta, no solo cuando cae | **CUMPLIDO**, y va en `9` con los ocho que aguantan y con **una debilidad mia que nadie me habia encargado declarar** (`5.0`) |
| **3**, el encabezado de la seccion `11` de la `ACTA 24` | el arnes me lo entrega como heredado y **no tiene cuerpo propio**: es el titulo bajo el que viven el `4` y el `5` | **CUMPLIDO por lectura, y lo digo en vez de callarlo**: los dos remedios con cuerpo son el `HEREDADO 4` y el `HEREDADO 5`, **y los dos van declarados uno a uno**. Dejarlo en blanco por obvio seria perderlo, que es lo que `D.40` vino a impedir |
| **4**, la tarea bloqueante de cinco puntos | punto 1 el orden del turno, punto 2 remedir toda cifra propia, punto 3 ninguna arista sin el paso de la madre, punto 4 el barrido y la herencia una a una, punto 5 la muestra con su banda | **CUMPLIDO los cinco**, cada uno con su sitio en `9`. **Y el punto 2 se cobro una pieza: cazo un instrumento MIO mal escrito** (`5.3`) |
| **5**, la relectura ancha recortada | tres filas encargadas, tres en cola escritas para que la vuelta 26 no las redescubra | **CUMPLIDO: la cola la remido hoy con su comando** (`5.3`) **y no la copio de mi propia acta**, que es exactamente lo que el punto 2 del heredado 4 prohibe. Salio igual al digito |

---

## 1. LO PRIMERO QUE CORRI, Y POR QUE VA PRIMERO

**`HEREDADO 4` punto 1 no cambia la promesa: cambia CUANDO se cumple.** Un fichero que ya existe no
se puede contaminar despues. Al empezar no sabia cual era la tanda, asi que hice lo que el propio
remedio manda en ese caso: **los pares de todo lo que la bitacora movio hoy, sacados SIN tocar la
columna `razon`.**

    $ python -c "... d.get('candidato'), d.get('vecino'), d.get('fecha') ..."
      ->  .t1_v26_auditor/pares_hoy.txt
    (el lector proyecta esos tres campos y NINGUN otro: ni razon, ni veredicto,
     ni detalle_paso, ni texto_citado)

    lineas de bitacora          : 203
    filas con fecha 2026-09-13  : 55
    ids distintos en esas filas : 20

Y con esos veinte ids, **antes de abrir un candidato, un capitulo o mi propio encargo**:

    $ python .t2_v24_acta/imprimir_pasos_corto.py 260 <los 20 ids>
      >  .t1_v26_auditor/pasos_pares_hoy.txt
    $ wc -l .t1_v26_auditor/pasos_pares_hoy.txt                     ->  262
    $ grep -c "NO ENCONTRADO" .t1_v26_auditor/pasos_pares_hoy.txt   ->  0

**Los veinte estan, y sus pasos estaban en disco antes que cualquier otra cosa de esta fase.**

### 1.1. Y la primera cosa que ese fichero me dijo, sin abrir ninguna razon

    $ python -c "... Counter de (candidato, vecino) ..."  ->  .t1_v26_auditor/pares_repetidos.txt
    FILAS DE HOY EN LA BITACORA : 55
    PARES DISTINTOS DE HOY      : 49
    PARES REPETIDOS             : 6   filas de mas: 6
       x2  L174,191   pedir_critica_equipo_premiarla || cambiar_potencial_trayectoria_crecimiento
       x2  L176,193   pedir_critica_equipo_premiarla || desplegar_marco_franqueza_radical
       x2  L179,196   pedir_critica_equipo_premiarla || elogiar_trabajo_especifico_contexto
       x2  L177,194   pedir_critica_equipo_premiarla || empezar_cultura_franqueza_radical
       x2  L175,192   pedir_critica_equipo_premiarla || equilibrar_elogio_critica_equipo
       x2  L178,195   pedir_critica_equipo_premiarla || manejar_enfado_persona_desafiada

**Los seis repetidos son los seis del MISMO nodo**, y ese nodo es el unico que hoy entro dos veces.
**La bitacora lleva la huella de una reparacion, y la lleva bien: nada se borro.** Lo que dejo
apuntado para el turno normal es **una sola pregunta de cifra**: si alguna sede publica `55` donde
la poblacion de pares distintos es `49`. **Hoy no la contesto porque no he visto ninguna sede que
publique esa cifra**, y una cifra que no he visto no se acusa.

---

## 2. LAS GUARDAS, CON SU SALIDA LITERAL

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 222
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
               vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
               arista_incompleta, guiones

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py resolutor
    nodos vivos: 222
    nodos deprecados (archivo): 0
    alias registrados: 0

    $ python tests/test_aceptacion.py
      total: 111 pruebas, 1 fallos, 0 errores

### 2.1. **EL UNICO ROJO ES DEL ARNES, NO DE LA VUELTA, Y LO DIGO CON SU TRAZA**

    FAIL: test_e_guion_largo_rompe_el_hook
    AssertionError: 1 != 0 : el repo ha de estar limpio antes de ensuciarlo:
    [pre-commit] gate de integridad          GATE VERDE.
    [pre-commit] barrido de guiones          BARRIDO DE GUIONES VERDE.
    [pre-commit] tallado del reporte (D.41)
      File "...\scripts\tallar_reporte.py", line 315, in revisar
        texto = io.open(ruta_reporte, encoding="utf-8").read()
    FileNotFoundError: ... 'docs\loop\REPORTE.md'
    CIERRE EN ROJO. No pasa: tallado del reporte (D.41)

> **DOS REGLAS DE LA CASA CHOCAN AQUI, Y NINGUNA DE LAS DOS ESTA MAL ESCRITA.** `D.34.2` retira
> `docs/loop/REPORTE.md` del arbol para que mi apertura sea ciega. `D.41` pone en el gancho de
> `pre-commit` un tallador que **abre ese mismo fichero sin comprobar que existe**. Mientras dura mi
> fase ciega, **el gancho esta en rojo y cualquier commit queda bloqueado.**

**LO QUE NO HAGO CON ESTO, Y ES LO IMPORTANTE: no recupero el reporte para poner la prueba en
verde.** Recuperarlo invalidaria mi apertura entera, y **una prueba verde comprada asi vale menos
que una roja explicada.**

**LO QUE SI DIGO:**

| | |
|---|---|
| **no es caida del extractor** | su turno tuvo el fichero en el arbol. **El rojo aparece solo dentro de la ventana que el arnes abre**, y se cierra solo cuando el arnes devuelva el reporte |
| **no es parada** | `AUDITOR_FORJA.md` `3` pide *dos vueltas seguidas por la misma causa*. **Es la primera vez que lo mido** |
| **no es moratoria rota si se arregla** | la cosecha `7.F` prohibe encargar maquinaria nueva. **Esto no es maquinaria nueva: es una linea de guarda en un tallador que ya existe.** Lo subo al turno normal, no lo encargo aqui |
| **las otras 110 pruebas pasan** | y `gate`, `guiones` y `resolutor` estan los tres en verde por su cuenta, fuera del gancho |

---

## 3. LA POBLACION, MEDIDA Y NO SUPUESTA

    $ python -c "... cuenta dataset/nodos.jsonl y agrupa por clave de fuente ..."
    NODOS EN GRAFO: 222
      zhuo_manager 136
      smart_who 59
      scott_radical_candor 19
      onu_consumidor 6
      manual_sistema_conocimiento 2

    $ for d in cuarentena/*/; do ls "$d"*.json | wc -l; done
    cuarentena/ensayo_referencia_163/  163
    cuarentena/marquet_turn_the_ship/    3
    cuarentena/scott_radical_candor/   123
    cuarentena/onu_consumidor/           0
    cuarentena/smart_who/                0
    cuarentena/zhuo_manager/             0

**Cero nodos de `marquet_turn_the_ship` dentro del grafo.** El lote 5 esta entero en la bandeja, que
es donde `D.39` dice que tiene que estar mientras el lote siga abierto.

---

## 4. MI FRONTERA DE `cap_01` Y `cap_02`, CORTADA POR MI Y CERRADA AL DIGITO

*Mi encargo pedia publicar la frontera de cada capitulo y cerrarla contra el cuerpo al digito, como
en `cap_14`. Aqui esta la MIA. El instrumento es `.t1_v26_auditor/frontera_auditor_v26.py`: cuenta
palabras por rango de linea y resta contra el cuerpo entero, de modo que **ninguna linea puede
quedarse fuera sin salir impresa.***

### 4.1. `cap_01`, unidad `Introduction`

**El rotulo sale de la cabecera, no de mi memoria** (`HEREDADO 3` punto 2 de la vuelta 23):

    $ sed -n "1,7p" fuentes/marquet_turn_the_ship/cap_01.md
    libro: Marquet, Turn the Ship Around!
    unidad: Introduction
    titulo_textual: Introduction
    fidelidad: verbatim

    $ python .t1_v26_auditor/frontera_auditor_v26.py fuentes/marquet_turn_the_ship/cap_01.md ...
    CUERPO (linea 8 al final, sin blancos): 2472 palabras
    ROT    L9  -L9    ROTULO           1 palabras
    A1     L11 -L21   POSTURA_CASO   407 palabras
    A2     L23 -L31   POSTURA_CASO   206 palabras
    A3     L33 -L33   POSTURA         22 palabras
    A4     L35 -L55   POSTURA        523 palabras
    A5     L57 -L61   POSTURA        135 palabras
    A6     L63 -L85   CASO           665 palabras
    A7     L87 -L95   POSTURA_CASO   239 palabras
    A8     L97 -L97   PROCEDIMIENTO  142 palabras
    A9     L99 -L103  POSTURA        132 palabras
    SUMA DE PIEZAS: 2472
    CUERPO        : 2472
    RESIDUO (cuerpo - piezas): 0
    LINEAS DE CUERPO NO ASIGNADAS: []

**NUEVE piezas y UNA sola con procedimiento, `L97`.** Cerrada al digito: `2472 = 2472`, residuo
`0`, cero lineas sin asignar.

**POR QUE LAS OTRAS OCHO NO LO SON, con `D.27` delante y una razon por pieza:**

| pieza | por que no es procedimiento |
|---|---|
| **A1** y **A2** | diagnostico con dos casos nombrados (Ian, Scott Mesh). **No hay inventario de medios: hay sintomas y una cifra de Gallup** |
| **A3** | una frase de causa raiz. Nombra el problema, no lo procedimenta |
| **A4** | la definicion del manual de la Academia Naval y su critica. **Es analisis, y `NOMBRAR NO ES PROCEDIMENTAR`** |
| **A5** | *achieves great improvements*, *significantly more resilient*. **Adjetivo de adecuacion en el sitio del criterio**, que es el caso literal que `D.27` excluye |
| **A6** | narracion autobiografica: Sunfish, Pelaez, Will Rogers, Santa Fe. **CASO** |
| **A7** | el entorno del submarino y el resultado de peor a primero. **Sin medios nombrados** |
| **A9** | la vision, el manifiesto y una direccion de correo. **POSTURA** |

> **UNA PIEZA QUE ME HIZO DUDAR Y QUE DEJO FUERA CON SU RAZON: `A6`, la escena de `L69`.** El capitan
> Pelaez dice, en estilo directo, *"Why don't you just say, 'Captain, I intend to go active on sonar
> for training'?"*. **Es una instruccion en imperativo en boca del jefe, que es exactamente el argumento
> con el que `cap_02` `L25` si entro.** La dejo fuera porque `D.27` pide **el inventario nombrado uno a
> uno**, y aqui el libro nombra **una sola formula** y ningun medio mas: como usarla, que contesta el
> jefe y que cambia con ella no estan en esta linea. **Nombrar una formula es nombrar.**
>
> **Y por eso mismo lo escribo: el criterio que separa `L69` de `L25` es `D.27`, NO el estar en
> imperativo ni en boca del jefe.** Si ese fuera el criterio, `cap_01` debia haber dado un candidato
> mas. **Lo subo al turno normal como pregunta de metodo, no como caida.**

### 4.2. `cap_02`, unidad `Cap. 3`

    $ sed -n "1,7p" fuentes/marquet_turn_the_ship/cap_02.md
    unidad: Cap. 3
    titulo_textual: Change of Course

    $ python .t1_v26_auditor/frontera_auditor_v26.py fuentes/marquet_turn_the_ship/cap_02.md ...
    CUERPO (linea 8 al final, sin blancos): 1454 palabras
    ROT    L9  -L9    ROTULO           3 palabras
    B1     L11 -L11   POSTURA         20 palabras
    B2     L13 -L13   ROTULO           5 palabras
    B3     L15 -L23   CASO           458 palabras
    B4     L25 -L25   PROCEDIMIENTO   61 palabras
    B5     L27 -L27   CASO            12 palabras
    B6     L29 -L29   PROCEDIMIENTO   49 palabras
    B7     L31 -L31   CASO           106 palabras
    B8     L33 -L33   PROCEDIMIENTO   42 palabras
    B9     L35 -L45   CASO           389 palabras
    B10    L47 -L47   SEPARADOR        3 palabras
    B11    L49 -L49   PROCEDIMIENTO   84 palabras
    B12    L51 -L53   CASO            95 palabras
    B13    L55 -L67   PREGUNTAS      127 palabras
    SUMA DE PIEZAS: 1454
    CUERPO        : 1454
    RESIDUO (cuerpo - piezas): 0
    LINEAS DE CUERPO NO ASIGNADAS: []

**CUATRO piezas con procedimiento: `L25`, `L29`, `L33` y `L49`.** Y una pieza, `B13`, que no cae en
ninguna de las tres clases de siempre: **las seis `QUESTIONS TO CONSIDER` del cierre.** La declaro
como pieza propia y **no la mino**: seis preguntas de reflexion no traen medios ni objetos de
trabajo, y `D.27` restriccion 1 deja fuera lo que solo nombra adonde hay que llegar.

### 4.3. **LO QUE MI CORTE DICE DEL SUYO, ANTES DE VER SU REPORTE**

**Las cuatro piezas con procedimiento que yo corte son las cuatro lineas que sus tres candidatos
usan.** No me sobra ninguna y no me falta ninguna en `cap_02`. **En `cap_01` coincidimos en que la
unica es `L97`.** Y las tres cuentas de palabras que sus ficheros declaran (`142` en `L97`, `49` en
`L29`, `84` en `L49`) **me salieron a mi las tres, por separado y con otro instrumento.**

**PERO HAY UNA ASIMETRIA DE ROTULO Y LA DIGO:** sus propios ficheros llaman `R3` a `L25` y `R4` a
`L33`, es decir **residuo**, y despues **las dos lineas dan pasos a un nodo**. Una linea que
alimenta un nodo **no es residuo**, y si la frontera publicada las cuenta como residuo, **el residuo
de `cap_02` esta inflado en `61 + 42 = 103` palabras.** Lo dejo escrito como lo que es: **una
pregunta a la frontera publicada**, no una acusacion, **porque la frontera publicada no esta en el
arbol y no la he visto.**

---

## 5. LOS TRES CANDIDATOS, CLASIFICADOS POR MI

### 5.0. **LA CONTAMINACION QUE TENGO QUE DECLARAR, Y LA DECLARO ANTES DE LA TABLA**

**Abrir los candidatos es lo que este turno me manda hacer, y el `resumen_teorico` de los tres trae
dentro las afirmaciones del extractor**: los rotulos de sus piezas, sus cuentas de palabras, su
`RELECTURA DE FIDELIDAD D.30 EN EL ACTO` y **los discutibles que el marco.** **No puedo abrirlos y
no leer eso.** Asi que digo exactamente que vale cada cosa que escribo aqui:

| lo que escribo | de que es |
|---|---|
| **mi frontera de `4`** | **corte MIO contra el libro**, con instrumento y cerrado al digito |
| **mi fidelidad de `5.2`** | **VERIFICACION, no lectura ciega**: sus tres cuentas ya estaban delante cuando la hice. **Vale por lo que encuentra, no por ser ciega** |
| **mis clases de `5.1` y de `7`** | **mias contra el libro y contra los pasos**, y donde coinciden con las suyas lo digo |

**Y UNA DEBILIDAD DE ORDEN QUE ES MIA Y QUE NADIE ME HABIA ENCARGADO DECLARAR: abri los tres
candidatos ANTES de leer `cap_01` y `cap_02` enteros.** El corte de la frontera lo hice despues, ya
sabiendo que lineas habia minado el. **Debi leer el libro y cortar primero.** No es `REMEDIO ROTO`,
porque ningun remedio mio ordenaba ese orden; **es la misma enfermedad que el `HEREDADO 4` punto 1
cura para las razones y no cura todavia para las fuentes**, y por eso me la dejo escrita en `11`.

### 5.1. Mi clase de cada candidato

| candidato | unidad | mi clase | por que, con `D.27` y `6.1` |
|---|---|---|---|
| **`ceder_control_reforzar_competencia_claridad`** | `cap_01`, `L97` | **PROCEDIMIENTO, y entra** | el libro pone **su propio inventario**: nombra el puente (*the bridge is control*), la operacion (*divesting control to others while keeping responsibility*), la condicion que la limita (*only works with a competent workforce that understands the organization's purpose*) y los dos pilares (*technical competence and organizational clarity*). **Son medios y objetos de trabajo, no metas: la restriccion 1 de `D.27` se cumple** |
| **`cambiar_forma_trabajar_conservar_plantilla`** | `cap_02`, `L25` mas `L29` | **PROCEDIMIENTO, y entra** | el plazo, la gente que ya esta, el canal de excepcion, el mensaje y el objeto sobre el que se trabaja. **Inventario nombrado uno a uno** |
| **`encargar_meta_especifica_dejar_libre_metodo`** | `cap_02`, `L49` mas `L33` | **PROCEDIMIENTO, y entra** | meta especifica, no decir como, mismos recursos, **y una consecuencia que el texto saca el mismo**. El caso entra como ejemplo nombrado dentro de la doctrina (manual `3.5`) y **el entregable no lleva ni un dato del caso** |

### 5.2. **LA RELECTURA DE FIDELIDAD `D.30`, PASO A PASO Y CON LA LINEA PEGADA**

*Instrumento: `.t1_v26_auditor/fidelidad_auditor_v26.py`, que pega cada paso a la linea del libro
que lo tiene que sostener **y no juzga**: el veredicto lo pongo yo. Salidas en `fidelidad_cap01.txt`,
`fidelidad_cap02_a.txt` y `fidelidad_cap02_b.txt`.*

**`ceder_control_reforzar_competencia_claridad`, 7 pasos, los siete de `L97`: 7 TRANSCRIPCION, 0
PUENTE. FIRMO SU `0,00`.** Los pasos 3, 4, 5 y 6 son practicamente literales de la linea.

**`encargar_meta_especifica_dejar_libre_metodo`, 5 pasos: 5 TRANSCRIPCION, 0 PUENTE. FIRMO SU
`0,00`.**

**`cambiar_forma_trabajar_conservar_plantilla`, 5 pasos: 4 TRANSCRIPCION Y UNO QUE NO FIRMO.**

    PASO 3> Pide igualmente el canal abierto para cambiar a alguien si hace falta, que es como
            el texto lo deja dicho: avisame si necesitas cambiar a alguien.
    --- L25 del libro ---
      "Look, here's the deal. If you need to change out some people, let me know, but I'm not
      interested in a lot of turnover. I don't think that will help the crew. I think a better
      focus would be on working with what you've got. ..."

> **ES `PUENTE`, Y DE LA ESPECIE ACTO.** El libro tiene al jefe **concediendo** el canal sin que
> nadie se lo pida. El paso ordena al que recibe el encargo **pedirlo**. Son dos actos distintos:
> *avisa cuando lo necesites* no es *pide que exista el aviso*. **Y el propio paso se desmiente
> solo**: escribe el verbo `Pide` y a continuacion cita el libro como *avisame si necesitas cambiar
> a alguien*, que es la version correcta.
>
> **QUIEN EJECUTA ESTE NODO ES EL QUE RECIBE EL ENCARGO, y eso no lo deduzco**: lo dice su propia
> `condiciones_activacion` (*cuando te haces cargo de un equipo que va mal*). Con ese actor, **el
> libro no contiene el acto de pedir.**
>
> **LA LECTURA CONTRARIA EXISTE Y LA ESCRIBO:** quien lea *Pide el canal abierto* como *quedate con
> la puerta de salida* lo llamara transcripcion floja. **No lo firmo asi porque `8.3` dice que el
> error que esta metrica invita a cometer es exactamente ese**, y porque **la correccion es de una
> palabra**: cambiar `Pide` por `Avisa a tu jefe`.

**Y UN CASI, QUE DIGO Y NO FIRMO COMO PUENTE:** el paso 1 escribe *antes de decidir nada sobre la
gente*, y el libro pone el plazo como **razon** al final de la frase, no como orden de ejecucion.
**Lo dejo en TRANSCRIPCION** porque la logica del libro es justamente que el plazo restringe la
decision de personal, **pero va marcado como discutible mio** (`10`).

### 5.3. **`PASOS INVENTADOS POR CAPITULO` DEL LOTE 5, FIRMADA POR MI**

    $ python .t1_v26_auditor/freno_v26.py marquet_turn_the_ship
      (atribucion por UNIDAD DE ORIGEN, la misma que .t2_v24_acta/freno_auditor.py)
    unidad      candidatos   pasos   ids
    cap_01               1       7   ceder_control_reforzar_competencia_claridad
    cap_02               2      10   cambiar_forma_trabajar_conservar_plantilla,
                                     encargar_meta_especifica_dejar_libre_metodo
    TOTAL                3      17
    ficheros leidos: 3

    $ python -c "... 100.0*puentes/pasos por fila ..."
    unidad    puentes   pasos  por cien
    cap_01          0       7      0.00
    cap_02          1      10     10.00
    LOTE 5          1      17      5.88

> ### **LA FILA QUE DECIDE EL VOLUMEN ES `cap_02` CON `10,00`, Y NO DISPARA EL FRENO POR UN PASO**
>
> `8.1` dice **por encima del 10 por ciento se baja un escalon**. **`10,00` no esta por encima de
> `10,00`.** Y digo lo fino que es: **si `cap_02` hubiera traido nueve pasos en vez de diez, la fila
> seria `11,11` y el freno mordia.** Una cifra que decide el tamanio de un lote entero y que depende
> de un solo paso **se publica con esa fragilidad escrita al lado, no sin ella.**
>
> **Y VA POR CAPITULO Y NO POR MEDIA** (`8.2`): la media del lote es `5,88` **y esconderia el
> `10,00`.** Publico las dos, **y manda la fila.**

#### La cola heredada del lote 4, **REMEDIDA HOY Y NO COPIADA** (`HEREDADO 4` punto 2)

    $ python .t2_v24_acta/freno_auditor.py
    cap_06             10     117
    cap_07             25     225
    cap_08             12     102
    TOTAL             142    1688
    ficheros leidos: 142
    sin unidad: []

    3 filas, 47 candidatos, 444 pasos

**Coincide al digito con lo que mi propia `ACTA 24` dejo escrito.** La cola sigue siendo esa.

> ### **Y EL PUNTO 2 DEL `HEREDADO 4` SE COBRO UNA PIEZA, PERO NO LA QUE YO ESPERABA: SE COBRO UN INSTRUMENTO MIO**
>
> **Mi primer `freno_v26.py` atribuia la unidad al PRIMER `cap_NN` que apareciese en cualquier parte
> del JSON.** Corrido sobre el lote 4 dio **`cap_06` 13 y 167, `cap_07` 34 y 320, `cap_08` 10 y
> 82**, o sea **57 candidatos y 569 pasos** donde la cola son **47 y 444**.
>
> **La cifra heredada era la buena y el instrumento nuevo era el malo**, porque un `resumen_teorico`
> que menciona otro capitulo le corria el rotulo al candidato entero. **Lo arregle poniendo la misma
> atribucion que ya usaba `.t2_v24_acta/freno_auditor.py`: la unidad sale de la ruta declarada en
> `UNIDAD DE ORIGEN`, no del primer `cap_NN` que pase por delante.**
>
> **POR QUE LO CUENTO EN VEZ DE BORRARLO:** el remedio dice *remide antes de escribir*, y lo que se
> supone que caza es una cifra vieja. **Hoy cazo lo contrario, y el remedio funciono igual.** Si
> hubiera confiado en mi instrumento nuevo por ser nuevo, **habria publicado `57` y `569` en un acta
> mia**, que es `CIFRA PUBLICADA PROPIA` **con mi racha en `2 de 3`.** Los dos repartos suman lo
> mismo, `142` y `1688`, **y ese cuadre es lo que dice cual de los dos es el bueno.**

---

## 6. EL BARRIDO `D.38.4`, SOBRE GRAFO MAS BANDEJAS

*Instrumento reusado tal cual de la vuelta 24, `.t1_v24_auditor/barrido_vecinos_auditor_v24.py`,
para que las dos vueltas sean comparables y para no encargarme maquinaria nueva (cosecha `7.F`).*

    POBLACION DEL BARRIDO: 348 = 222 del grafo + 126 de las bandejas
      (fuera _insertados y _derivadas, y fuera los 163 cuyas fuentes NO estan todas en
       FUENTES_CANONICAS.json, que es el mismo criterio que src/informe.py aplica)

    CANDIDATO ceder_control_reforzar_competencia_claridad   [bandeja]
      maximo cabecera pasos     vecino
      0.076  0.029    0.076     bandeja   trazar_plan_dieciocho_meses_aprendizaje
      0.075  0.018    0.075     bandeja   minimizar_impuesto_colaboracion_equipo
      0.071  0.000    0.071     grafo     responder_tres_preguntas_vocacion_directiva

    CANDIDATO cambiar_forma_trabajar_conservar_plantilla   [bandeja]
      0.136  0.136    0.126     bandeja   encargar_meta_especifica_dejar_libre_metodo
      0.100  0.100    0.073     grafo     ayudar_personas_jugar_fortalezas
      0.098  0.098    0.057     grafo     dar_opinion_critica_directa_desapasionada

    CANDIDATO encargar_meta_especifica_dejar_libre_metodo   [bandeja]
      0.136  0.136    0.126     bandeja   cambiar_forma_trabajar_conservar_plantilla
      0.109  0.109    0.052     bandeja   elogiar_publico_criticar_privado_sus_tres_matices
      0.098  0.098    0.058     grafo     avisar_pronto_incumplimiento_expectativas

**LOS TRES ESTAN LEJOS DE TODO. El maximo contra los 348 es `0,136`**, y `ceder_control` no llega a
`0,08` contra nadie: es el primer nodo de un libro nuevo con vocabulario propio.

**Y EL VECINO MAS PROXIMO DE CADA UNO DE LOS DOS DE `cap_02` ES EL OTRO**, que es exactamente el par
que el extractor marco como discutible. **Mi instrumento, que no es el suyo, pone el mismo par
arriba.** Eso no dice que tenga razon: **dice que marco donde estaba su duda**, que es lo unico que
`5.1` pide del marcado.

### 6.1. **MI VEREDICTO SOBRE ESE PAR, CON LA VARA Y SIN BASCULA**

**`cambiar_forma_trabajar_conservar_plantilla` contra `encargar_meta_especifica_dejar_libre_metodo`:
NO SON DUPLICADO, y no hace falta ni frontera declarada.**

| | |
|---|---|
| **actores distintos** | uno es **el que encarga** (*cuando le encargas a alguien que deje lista una organizacion*), el otro **el que recibe** (*cuando te haces cargo de un equipo que va mal*) |
| **lo que queda fuera del solape** | **procedimiento en los dos lados**: el plazo, la no rotacion, el canal y el mensaje a la tripulacion de un lado; la meta especifica, el no decir como y la oferta de apoyo del otro |
| **el solape que hay es DEL LIBRO** | *the only thing we could change was how we acted and interacted* (`L49`) y *by changing the way they interacted and behaved* (`L29`) **son dos frases del propio libro, en dos lineas, dichas desde los dos lados.** El extractor no la duplico: **la encontro duplicada** |

**SOSTENGO SU SEPARACION.**

### 6.2. **LA ADUANA EN SECO, Y UN CRUCE QUE CUADRA AL DIGITO** (`D.38.5`)

    $ python forja.py informe --carpeta cuarentena/marquet_turn_the_ship
      (18:51:28 a 18:57:58 del 13 sep 2026: SEIS MINUTOS Y MEDIO para TRES candidatos)

    candidatos revisados        : 3
    poblacion del barrido       : 348   (222 del grafo mas 126 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60
    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 3   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0
    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 7
      por candidato bloqueado          : menor 2, mediana 2, mayor 3
      que senial levanta cada vecindad : paso_contra_nodo 1, similitud_texto 6

> **`348 = 222 + 126` POR LAS DOS MEDIDAS, LA MIA Y LA DE LA MAQUINA, AL DIGITO.** Es lo que `D.38.5`
> prometio el 12 sep: **durante nueve vueltas el informe cargaba solo el grafo y mi barrido y el suyo
> median poblaciones distintas.** Hoy miden la misma, **y por eso las diferencias que queden ya son
> de verdad y no de metodo.**

**Y QUEDA UNA, Y ES CONTRA MI INSTRUMENTO.** El unico vecino de todo el lote levantado por
`paso_contra_nodo`, que es la senial fuerte, **mi barrido no lo saca ni entre los seis primeros**:

    vecino escuchar_entender_critica_dominar_defensa  [levantada por: paso_contra_nodo]
      similitud_texto 0.261 | familia_id 0.000 | paso_contra_nodo 0.612
      paso 2 del candidato contra paso 4 de escuchar_entender_critica_dominar_defensa

    $ python .t2_v24_acta/imprimir_pasos_corto.py 300 escuchar_entender_critica_dominar_defensa
        4. Y sobre todo practica con otros, que es lo que el texto pone por encima de lo demas.

    (paso 2 de cambiar_forma_trabajar_conservar_plantilla)
        2. Centrate en trabajar con lo que tienes, que es lo que el texto recomienda por
           encima de mucha rotacion.

> **LOS DOS PASOS NO TIENEN NADA QUE VER: uno es trabajar con la tripulacion que ya tienes y el otro
> es practicar la escucha de tres minutos.** Lo que comparten es **`que es lo que el texto ... por
> encima de ...`, que es una FORMULA DE LA CASA**, no contenido de ningun libro.
>
> **MI CLASE PARA ESE PAR: `SANO`, sin duda.** Y la leccion es de `D.19` medida otra vez: **la senial
> dijo donde mirar y ahi acabo su trabajo.** Pero esta vez **la senial mira su propio reflejo**: el
> unico `paso_contra_nodo` del lote lo dispara el estilo con que esta casa escribe sus pasos, **y va
> a costar una lectura de par en el turno de insercion.**
>
> **POR QUE MI BARRIDO NO LO VIO, y no es que sea mejor:** el mio compara **nodo contra nodo** con
> bolsa de palabras, y una coincidencia de una frase en un paso se diluye; **el suyo compara paso
> contra paso**, y ahi la formula pesa entera. **Son dos granos distintos y hoy hacen falta los dos.**

---

## 7. LOS PARES DE LA TANDA, LEIDOS A CIEGAS

**La eleccion de cuales releo la hace un instrumento y no mi ojo** (`7`: *elegir a ojo mide lo que el
auditor ya sospecha*). Ordene los 55 pares por solape mio y lei los de arriba:

    $ python .t1_v26_auditor/pares_orden_v26.py   ->  .t1_v26_auditor/pares_orden.txt
    PARES DE LA TANDA ORDENADOS POR SOLAPE DEL AUDITOR: 55
    0.123  pedir_critica_equipo_premiarla        ||  empezar_cultura_franqueza_radical
    0.115  ajustar_franqueza_oido_oyente         ||  delimitar_franqueza_radical_cinco_noes
    0.114  cuidar_persona_completa_equipo        ||  delimitar_franqueza_radical_cinco_noes
    0.099  acompaniar_mejores_equipo_socio       ||  cambiar_potencial_trayectoria_crecimiento
    0.093  elogiar_trabajo_especifico_contexto   ||  criticar_trabajo_evitar_desanimo
    0.093  cuidar_persona_completa_equipo        ||  respetar_cuidar_persona_cargo

**LA PRIMERA LECTURA ES DE LA TANDA ENTERA: `0,123` ES EL MAXIMO DE LOS 55.** Ningun par de esta
tanda esta cerca de la zona de duplicado por mi medida.

| par | **mi clase, escrita antes de mirar la bitacora y antes de mirar las aristas del grafo** |
|---|---|
| `pedir_critica_equipo_premiarla` con `empezar_cultura_franqueza_radical` | **CONTINUA, madre `empezar_cultura`.** Su paso 3 **nombra** el trabajo (*pide a tu gente que sea radicalmente franca contigo*) y ahi se para; el hijo lo **procedimenta** entero: como pedir, que hacer con el silencio, como premiar la primera queja. **`NOMBRAR NO ES PROCEDIMENTAR` corta hacia el hijo** |
| `ajustar_franqueza_oido_oyente` con `delimitar_franqueza_radical_cinco_noes` | **SANO.** Uno delimita el concepto con cinco noes, el otro lo traduce entre culturas con ocho pasos. **Procedimiento en los dos lados** |
| `cuidar_persona_completa_equipo` con `delimitar_franqueza_radical_cinco_noes` | **SANO.** El solape es una lista negativa sobre confraternizar. Uno acota el concepto, el otro procedimenta la primera dimension con cuatro medios nombrados |
| `acompaniar_mejores_equipo_socio` con `cambiar_potencial_trayectoria_crecimiento` | **CONTINUA, madre `cambiar_potencial`.** Su paso 10 imprime las dos columnas y **pone el nombre `superestrella`**; el paso 1 del hijo arranca *antes de distinguir entre estrellas de rock y superestrellas*, o sea **da por hecha la clasificacion de la madre.** Primero se clasifica, despues se acompania |
| `elogiar_trabajo_especifico_contexto` con `criticar_trabajo_evitar_desanimo` | **SANO.** Se nombran mutuamente (paso 9 de uno, paso 6 del otro) **y ninguno procedimenta al otro.** `6.1`: **la arista no exculpa**, y el nombrado mutuo sin continuacion tampoco la crea |
| `cuidar_persona_completa_equipo` con `respetar_cuidar_persona_cargo` | **SANO, y es el que mas me costo.** Son **libros distintos** (`scott` y `zhuo`) sobre el mismo deber. Fuera del solape: `zhuo` tiene el *no lo finjas porque el cuerpo te delata*, el *cuidar no es darle la razon* y la apuesta de la honestidad; `scott` tiene las dos causas nombradas, **cuatro medios uno a uno**, el ejemplo de vulnerabilidad y el precio de que te odien. **`6.1` sin bascula: procedimiento en los dos lados** |

**LOS 49 PARES DISTINTOS DE HOY NO ESTAN TODOS RELEIDOS, Y LO DIGO CON SU CIFRA: relei SEIS.** El
resto queda para el turno normal, cuando sepa cuales marco el como discutibles, que es por donde
`5.1` manda empezar. **Un recorte declarado no es una omision silenciosa** (`5.5`).

---

## 8. LAS ARISTAS, CON EL PASO DE LA MADRE IMPRESO (`HEREDADO 4` punto 3)

    $ python -c "... suma nodos_siguientes sobre dataset/nodos.jsonl ..."
    NODOS: 222
    ARISTAS (suma de nodos_siguientes): 81
    NODOS CON ALGUNA ARISTA: 102

    $ python -c "... previos y siguientes de los cuatro implicados ..."
    criticar_trabajo_evitar_desanimo      previos: ['empezar_cultura_franqueza_radical']
    pedir_critica_equipo_premiarla        previos: ['empezar_cultura_franqueza_radical']
    empezar_cultura_franqueza_radical     siguientes: ['criticar_trabajo_evitar_desanimo',
                                                       'pedir_critica_equipo_premiarla']
    elogiar_trabajo_especifico_contexto   previos: []   siguientes: []

**Las dos aristas nuevas salen de la misma madre.** Y **mi clase del primer par de `7`, escrita
antes de correr esto, es la primera de las dos.** No lo digo como acierto: lo digo porque **es la
comprobacion de que la lectura de los pasos y el cable llevan al mismo sitio.**

### 8.1. **Y AHI HAY UN HUECO QUE MIDO HOY**, con el paso impreso y su numero, que es lo que mi propio remedio exige

    $ python .t2_v24_acta/imprimir_pasos_corto.py 400 empezar_cultura_franqueza_radical
    empezar_cultura_franqueza_radical [ grafo ]
      ENTREGABLE: El arranque hecho en el orden del texto: la idea explicada, la critica pedida
                  antes que dada, el elogio dado antes que la critica, y la frontera peligrosa
                  entendida antes de empezar a criticar.
        3. Y despues pide a tu gente que sea radicalmente franca contigo.
        5. Cuando empieces a darla, empieza por el elogio y no por la critica.
        6. Cuando pases a la critica, asegurate de entender donde esta la frontera peligrosa
           entre la franqueza radical y la agresion odiosa.

> **EL PASO 5 NOMBRA EL ELOGIO EXACTAMENTE COMO EL 6 NOMBRA LA CRITICA, Y SOLO LA CRITICA TIENE
> CABLE.** `elogiar_trabajo_especifico_contexto` esta dentro del grafo, **entro hoy**, y tiene
> **cero aristas por los dos lados**. Y **el propio entregable de la madre lo pone en su secuencia**:
> *el elogio dado antes que la critica*.
>
> **Es una arista `D.29` de la misma familia, con la misma madre y con su paso numerado delante.**
> **No la escribo yo en ninguna sede hoy**, porque escribir aristas no es de esta fase. **La mido, la
> dejo aqui con su paso, y la subo al turno normal** para ver si el reporte la declaro y no pudo
> cablearla, o si no la vio.

---

## 9. LOS REMEDIOS QUE AGUANTAN, PORQUE UN REMEDIO SOLO INFORMA SI TAMBIEN SE DECLARA CUANDO AGUANTA

*Es `HEREDADO 2`, y es la unica forma de que la lista no sea una lista de derrotas.*

| remedio | como quedo hoy |
|---|---|
| `HEREDADO 4` punto 1, **el orden del turno** | **AGUANTA, y es la primera vez.** Los pasos de los 20 estaban en disco antes de que yo abriera un candidato, un capitulo o mi propio encargo |
| `HEREDADO 4` punto 2, **remedir toda cifra propia** | **AGUANTA, y cazo un instrumento MIO** (`5.3`). Es el mejor ejemplar que ha dado |
| `HEREDADO 4` punto 3, **ninguna arista sin el paso de la madre** | **AGUANTA.** La unica arista que nombro hoy (`8.1`) va con el paso `5` impreso y numerado, **y no la escribo en ninguna sede** |
| `HEREDADO 4` punto 4, **el barrido y la herencia una a una** | **AGUANTA:** barrido en `6`, herencia una a una en `0.1`, **y cero `NO APLICA`** |
| `HEREDADO 4` punto 5, **la muestra con su banda** | **AGUANTA por la via de decirlo:** no publico banda **porque no he leido un solo `veredicto` de la bitacora en esta fase**, asi que hoy no se cuantos `SANO` hay. **La muestra pineada va en el turno normal, con su semilla escrita** |
| `HEREDADO 5`, **la cola del hueco del freno** | **AGUANTA y se remide**: `47` candidatos y `444` pasos, iguales al digito (`5.3`) |
| `D.38.3`, **ninguna cifra sin instrumento** | **AGUANTA**, y hoy tuvo que esperar seis minutos y medio a que el informe cerrase antes de que yo pudiera publicar su saldo (`6.2`) |
| `D.38.4`, **grafo mas bandejas** | **AGUANTA**, con el instrumento de la vuelta 24 reusado tal cual, **y cuadra al digito contra la maquina** (`6.2`) |
| `D.34.2`, **no recuperar los cuatro retirados** | **AGUANTA, y hoy tuvo precio**: la prueba de aceptacion esta en rojo por eso (`2.1`) **y no la puse en verde recuperando el reporte** |

---

## 10. MIS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

| # | lo que marco | por que puedo estar equivocado |
|---:|---|---|
| **1** | **el `PUENTE` del paso 3 de `cambiar_forma_trabajar_conservar_plantilla`** (`5.2`) | es un verbo. Quien lea *Pide el canal abierto* como *quedate el canal* dira que es transcripcion floja. **Y decide la fila del freno: sin el, `cap_02` es `0,00` y el lote entero es `0,00`** |
| **2** | **`cap_02` en `10,00` y no por encima** | esta a un paso de morder. **Si el reporte declara un puente mas en `cap_02`, el freno dispara y el lote 5 baja de dos capitulos a uno** |
| **3** | **los pasos 1 y 7 de `ceder_control...` no son procedimiento del lector: son la ESTRUCTURA DEL LIBRO** | *cuenta con las cuatro fases y con como reparte sus partes* no es algo que nadie haga con su organizacion. **Como fidelidad `D.30` son transcripcion, y por eso firmo el `0,00`**; **como `D.27` restriccion 1 son inventario de PARTES DE UN LIBRO, no de medios.** Puedo estar estrechando la vara, **y estrechar la vara es parada, asi que lo marco y no lo adjudico** (`6.3`) |
| **4** | **su discutible de `D.37` sobre ese mismo nodo lo contesto de una tercera manera** | el dice *cabeza de serie `D.37` o nodo suelto*. **Mi lectura: ninguna de las dos hoy.** El texto **si** escribe la cuenta (*essentially four phases*) y **si** nombra cuatro cosas (soltar las ideas viejas, el control, la competencia tecnica, la claridad organizativa), **pero nunca las rotula como las cuatro fases**, y `D.37` esta corregido a la lectura conservadora. **Cae a `D.29` con razon escrita.** Y ademas **`D.37` pide que las partes EXISTAN COMO NODOS, y hoy no existe ninguna**: el lote 5 tiene tres candidatos y cero nodos en el grafo. **Es una cabeza cuyas aristas son deuda futura** |
| **5** | **`SANO` para `cuidar_persona_completa_equipo` con `respetar_cuidar_persona_cargo`** | es el par entre libros distintos con mas solape de sentido de la tanda, **y el mio es el voto mas discutible de los seis** |
| **6** | **`CONTINUA` para `acompaniar_mejores` con `cambiar_potencial`** | quien lea las dos columnas como taxonomia y no como trabajo dira que no hay nada que continuar |
| **7** | **el *antes de decidir nada sobre la gente* del paso 1** (`5.2`) | lo dejo en transcripcion **y podria ser un orden que el libro no da** |
| **8** | **que las `QUESTIONS TO CONSIDER` de `cap_02` no se minan** | son seis preguntas en imperativo. **Digo que no traen medios**, pero la ultima (*Do you give employees specific goals as well as the freedom to meet them in any way they choose?*) **es el nodo `encargar_meta_especifica` en forma de pregunta**, y eso se puede leer como que el libro devuelve ahi su propia doctrina |
| **9** | **`R3` y `R4` contados como residuo** (`4.3`) | no he visto la frontera publicada. **Puedo estar acusando a un rotulo que en su sede esta bien puesto** |
| **10** | **que las `55` filas de bitacora son `49` pares** (`1.1`) | **si ninguna sede publica `55` como poblacion de pares, no hay nada que corregir y esto es ruido mio** |
| **11** | **que `cap_01` `L69` se queda fuera** (`4.1`) | por `D.27` la dejo fuera, **pero es la misma forma que `L25`, que si entro**, y quien aplique el criterio escrito del extractor en vez del mio saca un candidato mas de `cap_01` |

---

## 11. EL REMEDIO QUE ME DEJO A MI MISMO EN ESTA FASE

*Uno solo, y sale de `5.0`, que es la unica debilidad nueva que esta apertura encontro en mi.*

> **LEER EL LIBRO Y CORTAR LA FRONTERA VA ANTES DE ABRIR EL PRIMER CANDIDATO.**
>
> El `HEREDADO 4` punto 1 curo el orden para las razones de la bitacora **y no lo curo para las
> fuentes.** Hoy abri los tres candidatos antes de leer `cap_01` y `cap_02` enteros, asi que **cuando
> corte mi frontera ya sabia que lineas habia minado el.** Mi corte salio limpio y cerrado al digito,
> **y eso no arregla que el orden fuera el malo**: un corte hecho despues **no se distingue leyendolo**
> de uno hecho antes, igual que una razon dada despues no se distingue de una dada antes.
>
> **LA VERSION EJECUTABLE, que es la unica que sobrevive:** el corte de frontera de cada unidad del
> lote **se escribe en disco antes de abrir `cuarentena/`**, exactamente como hoy se escribieron los
> pasos antes de abrir nada.

---

*Fin de la apertura ciega. No he abierto `docs/loop/REPORTE.md`, `docs/loop/loop.log`,
`docs/loop/ultimo_extractor.json` ni `docs/loop/ultimo_auditor.json`, y no los he recuperado de git
ni por ninguna otra via. No commiteo: el arnes sella este fichero.*
