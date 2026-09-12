# APERTURA CIEGA DE LA VUELTA 19, lote 4 (`scott_radical_candor`), `cap_09`

**Escrita ANTES de ver `docs/loop/REPORTE.md`, que no esta en el arbol.** Toda cifra de este
documento sale de un instrumento corrido en esta misma fase y lleva su salida literal pegada
al lado (`D.38.3`). El barrido de vecinos va sobre grafo mas bandejas (`D.38.4`).

---

## 0. `D.40`: LA HERENCIA, DECLARADA ANTES DE NADA

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    80fd74cdf15bb0b1ff02bcbe560ba03f11f22472

    $ wc -l docs/loop/ACTA_AUDITOR.md docs/loop/AUDITOR_FORJA.md
      17295 docs/loop/ACTA_AUDITOR.md
        574 docs/loop/AUDITOR_FORJA.md

> ### **ACTA ANTERIOR LEIDA: `80fd74cdf15bb0b1ff02bcbe560ba03f11f22472`**
>
> Es la huella que el propio prompt me entrega y es la que `git hash-object` me devuelve
> sobre el fichero que abri. **Son la misma.**

### `HEREDADO 1`: **CUMPLIDO**

El arnes me entrega como `HEREDADO 1` la seccion `7.6` del acta anterior (linea 17197), que es
la tabla de **los remedios mios que SI aguantaron**. La cumplo re corriendo cada fila de esa
tabla en esta vuelta, y la cumplo tambien en su fondo, que es no perder el remedio:

| fila heredada de `7.6` | como la cumplo HOY | donde esta |
|---|---|---|
| `D.40`, leer `ACTA_AUDITOR.md` en la fase ciega antes de escribir | esta seccion 0, con la huella remedida y el heredado resuelto | `0` |
| `D.38.4`, barrido sobre grafo mas bandejas | poblacion `444 = 203 + 241`, y `281` sin el catalogo de control, las dos con su instrumento | `6` |
| `D.38.3`, toda cifra de la fase ciega con su instrumento al lado | toda cifra de este documento lleva su comando pegado, **y una de ellas es una comprobacion que contradice lo que otra decia** (`4.2`) | todo |
| `D.34`, no recuperar de git los cuatro ficheros retirados | no corri `git show` ni `git checkout` sobre ninguno de los cuatro. **La contaminacion que si hubo la declaro yo entera** | `1.1` |
| `D.34`, no tocar `APERTURA_CIEGA.md` tras el sello | se comprueba al cerrar mi turno normal, no aqui | `8` |
| `5.5`, re correr por mutacion toda guarda declarada mordiendo | va en mi turno normal, que es donde tengo el reporte que declara cuales muerden | `8` |

### **Y UNA COSA QUE EL ARNES NO ME ENTREGO Y QUE ENCONTRE YO AL ABRIR EL ACTA**

**El prompt me da `heredados: 1` y me da la `7.6`. La `7.5` NO me llego**, y la `7.5` se titula
literalmente **`TAREA BLOQUEANTE DEL AUDITOR DE LA VUELTA 19, ESCRITA POR EL DE LA 18`**, con
**tres ordenes numeradas**. `AUDITOR_FORJA.md` dice que el arnes saca del acta anterior *la
`TAREA BLOQUEANTE DEL AUDITOR` y cualquier `REMEDIO`*: **me saco el remedio y no me saco la
tarea bloqueante.**

**NO ES UNA EXCUSA SINO LO CONTRARIO: la tengo y la cumplo**, y esta en la seccion `2` con su
salida. **Lo digo porque `D.40` nacio de que un remedio se perdiera tres vueltas seguidas**, y
esta vez lo que casi se pierde es la mitad que mas manda. **Que yo lo encontrara leyendo el
acta es exactamente lo que `D.40` queria que pasara**; que el arnes no lo entregara es una
averia de la entrega, y va a mi acta como propuesta, no como parada.

---

## 1. LO QUE NO ESTA EN EL ARBOL, Y LA CONTAMINACION QUE DECLARO YO

    $ git status --porcelain
     D docs/loop/APERTURA_CIEGA.md
     D docs/loop/REPORTE.md
     D docs/loop/loop.log
     M docs/loop/ultimo_apertura.json
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json

    $ wc -c docs/loop/ultimo_apertura.json
    0 docs/loop/ultimo_apertura.json

**Los cuatro de `D.34.2` no estan y no los recupero.** No corri `git show` ni `git checkout`
sobre ninguno de ellos.

### 1.1. **MI CONTAMINACION, ENTERA Y CON SU COMANDO**

**Corri `git log --oneline -12` para saber que vuelta me tocaba auditar**, porque
`ultimo_apertura.json` esta a cero bytes y no lo dice. **Los asuntos de commit que eso me trajo
llevan cifras del extractor**, y las transcribo aqui para no fingir que no las lei:

    10a2b5b CIERRE DE LA VUELTA 19: las cinco guardas en verde, el grafo donde abrio, ...
    a692c26 cap_09 del lote 4 (Cap. 6, Guidance): 15 candidatos, 177 pasos, cero puentes,
            y la vuelta cierra ahi por el techo de candidatos
    0dcb431 La frontera de cap_09 publicada ANTES de cortar: 30 piezas, 20 dan nodo,
            10 no con su motivo, ...

**LAS CIFRAS QUE ESO ME ADELANTO SON `15`, `177` Y `30 / 20 / 10`.** Las dos primeras las he
remedido yo por instrumento propio antes de escribirlas (`4` y `5`), y coinciden. **La tercera
NO la he podido remedir**, porque una frontera es una particion y la mia es mia: **mi particion
da `29 / 19 / 10`**, y la comparacion de las dos es trabajo de mi turno normal y no de aqui.

**LA SEDE DE UN ASUNTO DE COMMIT NO ES SEDE DE CIFRA** (`5.6`), asi que esto no le cuenta a
nadie como caida. **Pero es informacion del extractor que entro en mi fase ciega por mi mano**,
y el auditor de la vuelta 18 declaro la suya igual: se declara, no se disimula.

### 1.2. **LO QUE SI PUEDO ABRIR Y ABRI**

`docs/loop/ACTA_AUDITOR.md` entero (obra mia, `D.40`), los 78 candidatos de
`cuarentena/scott_radical_candor/`, el texto fuente `fuentes/scott_radical_candor/cap_09.md`,
`docs/loop/AUDITOR_FORJA.md` entero, `docs/loop/ORDEN_DE_LOTES.md`, `config/umbrales.json`,
`dataset/nodos.jsonl` y el codigo de `src/`.

---

## 2. LAS TRES ORDENES DE LA `7.5`, CORRIDAS SIN LEERME

### ORDEN 1. **LA FRONTERA SE CIERRA CONTRA EL CUERPO, O NO SE PUBLICA**

**Cumplida.** La salida que la orden exige, con sus cuatro renglones, esta pegada al pie de la
seccion `3`, y **los dos `N` son el mismo `N`: 17.482 palabras contra 17.482 palabras.**

### ORDEN 2. **TODA CIFRA MIA LLEVA SU DENOMINADOR EN LA MISMA FRASE**

**Cumplida** a lo largo del documento. No escribo *15 candidatos* sino **15 candidatos de
`cap_09`, de los 78 que hoy esperan en la bandeja del lote 4**; no escribo *444* sino **444 de
poblacion de barrido, que son 203 del grafo mas 241 de bandeja**.

### ORDEN 3. **EL BARRIDO DE GUIONES, DOS VECES, Y LA SEGUNDA SOBRE LO QUE YO ESCRIBO FUERA**

Corrida la primera. **Y salio en ROJO POR MI MANO**, exactamente por la puerta que el auditor de
la 18 se dejo abierta: mis propios ficheros de trabajo.

    $ python forja.py guiones
    BARRIDO DE GUIONES EN ROJO: 18 hallazgo(s)
      .barrido_v19/bandejas.jsonl linea 150 columna 1687: guion largo (U+2014)
      ... (9 hallazgos en bandejas.jsonl y los mismos 9 en pob.jsonl)

**LOS DIECIOCHO SON MIOS Y DE ESTE TURNO**, y los nueve distintos vienen copiados del catalogo
de control al construir la poblacion del barrido. **Se remedian antes del sello y la salida en
verde va en la seccion `8.2`.** La segunda pasada, sobre mi mensaje final, es la regla que me
llevo puesta al cerrar.

---

## 3. LA FRONTERA DE `cap_09`, MEDIDA POR MI Y CERRADA CONTRA EL CUERPO

**El instrumento es una particion escrita por mi y comprobada por programa**: el programa
recorre las piezas, marca cada linea con contenido que cubre, detecta hueco y solape, suma las
palabras de cada fila y las cruza contra el cuerpo medido aparte.

    $ wc -l fuentes/scott_radical_candor/cap_09.md                   ->    433
    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_09.md | wc -w    ->  17482
    lineas con contenido desde L8                                    ->    213

| lineas | palabras | da nodo | pieza |
|---|---:|:---:|---|
| 9 | 6 | NO | rotulo de la lamina de la balanza elogio y critica |
| 11-13 | 108 | NO | marco del capitulo: que es guidance y que hace falta |
| 15 | 3 | NO | rotulo `SOLICITING IMPROMPTU GUIDANCE` |
| 17-53 | 2178 | **SI** | `Embrace the discomfort` |
| 55-63 | 330 | **SI** | `ORANGE BOX` |
| 65-71 | 325 | **SI** | `MANAGEMENT FIX-IT WEEKS` |
| 73-75 | 98 | NO | rotulo `GIVING IMPROMPTU GUIDANCE` mas bisagra |
| 77-95 | 699 | **SI** | `Be humble` |
| 97-113 | 647 | **SI** | `Be helpful` |
| 115-135 | 1144 | **SI** | `Give feedback immediately` |
| 137-153 | 793 | **SI** | `In person (if possible)` |
| 155-163 | 450 | **SI** | `Praise in public, criticize in private` |
| 165-177 | 886 | **SI** | `Dont personalize` |
| 179-203 | 1164 | **SI** | `GAUGE YOUR IMPROMPTU GUIDANCE` |
| 205-221 | 848 | **SI** | `BEING RADICALLY CANDID WITH YOUR BOSS` |
| 223-225 | 75 | NO | rotulo `GENDER AND GUIDANCE` mas marco |
| 227-249 | 884 | NO | `Why RC may be harder for men managing women` |
| 251-283 | 1006 | NO | `Why gender bias makes RC harder for women`, el `Abrasive Trap` |
| 285-289 | 168 | NO | `What can you do?`, bisagra |
| 291-293 | 126 | **SI** | `Men: dont pull punches with women` |
| 295-299 | 129 | **SI** | `Women: demand criticism` |
| 301-313 | 416 | **SI, Y NO ESTA ESCRITO** | `Men and women: when you feel a woman is too aggressive` |
| 315-329 | 573 | **SI, Y NO ESTA ESCRITO** | `Things to think about if youre a woman told youre abrasive` |
| 331-361 | 1526 | **SI, Y NO ESTA ESCRITO** | `FORMAL PERFORMANCE REVIEWS` |
| 363-367 | 212 | **SI** | `PREVENT BACKSTABBING` |
| 369-381 | 738 | **SI** | `PEER GUIDANCE` |
| 383-425 | 1818 | **SI, Y NO ESTA ESCRITO** | `SPEAKING TRUTH TO POWER`, con sus preguntas frecuentes |
| 427-429 | 130 | NO | cierre del capitulo |
| 431-433 | 2 | NO | marca del capitulo siguiente, `7. TEAM` |

**LA SALIDA QUE LA ORDEN 1 EXIGE, PEGADA:**

    piezas                                 : 29
    de ellas SI dan nodo                   : 19
    de ellas NO dan nodo                   : 10
    lineas con contenido NO cubiertas      : 0 []
    SOLAPES                                : 0 []
    suma de las filas                      : 17482 palabras
    cuerpo medido aparte (sed 8,$ | wc -w) : 17482 palabras
    CUADRAN

    piezas SI dan nodo SIN candidato escrito: [(301, 313), (315, 329), (331, 361), (383, 425)]
    palabras de esas cuatro                 : 4333

**EL BLOQUE DE ARRIBA ES LA SALIDA DEL PROGRAMA, SIN TOCAR.** La glosa es mia y va fuera: **de
las 19 piezas que dan nodo, 15 tienen candidato escrito y 4 no lo tienen**, y esas cuatro suman
**4.333 palabras de las 17.482 del cuerpo**, que es el 24,8 por ciento del capitulo.

### 3.1. **LAS CUATRO PIEZAS QUE DAN NODO Y NO TIENEN CANDIDATO: 4.333 palabras de las 17.482**

**Es el hallazgo mas caro de mi lectura ciega y lo escribo antes de saber si el extractor lo
declaro.** Las cuatro son procedimiento explicito y no postura, y el libro pone el anuncio de
inventario delante de cada una:

| pieza | por que digo que da nodo, leido por mi |
|---|---|
| `301-313` (416 pal) | `L303` abre *try these tactics*, y detras van cuatro tacticas rotuladas con su acto: `Switch genders`, `Be more specific`, `Dont use gendered language`, `Never just say Be more likeable`. **Es la misma forma que sus dos hermanas de 126 y 129 palabras, que si dieron nodo** |
| `315-329` (573 pal) | `L317` escribe *consider the following four rules of thumb*, y **la cuenta la pone el libro y no yo**. Cuatro reglas rotuladas mas `Dont write men off` |
| `331-361` (1526 pal) | `L339` escribe *here is my advice for delivering a performance review well*, y detras van nueve consejos rotulados uno a uno, cada uno con su acto. **Es el bloque mas procedimental del capitulo entero** |
| `383-425` (1818 pal) | `L391` escribe *here are a few rules of thumb I learned for conducting them*, y detras van once consejos rotulados mas un bloque de preguntas frecuentes. **Es la pieza mas larga del capitulo** |

> ### **Y LO QUE DE VERDAD MARCO ES QUE EL CORTE NO VA EN ORDEN DE LECTURA**
>
> Si el capitulo se hubiera cortado por el techo de quince candidatos, el corte seria un
> **truncamiento**: se escribe hasta donde se llega y lo de mas abajo queda para la vuelta
> siguiente. **No es lo que veo.** El candidato mas tardio del capitulo sale de `369-381`, y
> `331-361`, que va ANTES y es mas larga, se quedo sin escribir. **Eso no es un truncamiento:
> es una seleccion.**
>
> **NO DIGO QUE ESTE MAL.** Digo que **un cierre corto por techo y una seleccion de piezas son
> dos cosas distintas con dos motivos distintos**, y que la letra de `EXTRACTOR.md` 12.4 tal
> como `AUDITOR_FORJA.md` 8.1 la cita solo cubre la primera. **Lo subo como discutible 1.**
>
> **Y ARRASTRA UNA CONSECUENCIA DE REGISTRO QUE SI ES MIA DE VIGILAR:** si el acta escribe
> *`cap_09` minado* a secas, **esa cifra sera falsa**, porque quedan cuatro piezas y 4.333
> palabras de las 17.482 sin pasar. La fila de `ORDEN_DE_LOTES.md` tiene que decir **`cap_09`
> minado en parte**, con su cifra.

---

## 4. LOS QUINCE CANDIDATOS DE `cap_09`, CLASIFICADOS POR MI A CIEGAS

**El conjunto lo fija un instrumento y no mi ojo:** son los candidatos de
`cuarentena/scott_radical_candor/` cuyo `resumen_teorico` cita
`fuentes/scott_radical_candor/cap_09.md`.

    $ ls cuarentena/scott_radical_candor/*.json | wc -l                ->  78
    $ (programa) candidatos que citan cap_09.md                        ->  15
    $ (programa) suma de sus pasos_accionables                         -> 177

    reparto de la bandeja del lote 4 por unidad de origen (candidatos / pasos):
      cap_01   1 /   9        cap_06  10 / 117
      cap_03   1 /   7        cap_07  25 / 225
      cap_04   6 /  48        cap_08  12 / 102
      cap_05   8 /  76        cap_09  15 / 177
      TOTAL   78 / 761

| # | candidato | pieza | pasos | **mi clase, a ciegas** |
|---:|---|---|---:|---|
| 1 | `abrazar_incomodidad_arrancar_critica_equipo` | 17-53 | 20 | **ENTRARIA** |
| 2 | `organizar_sistema_recoger_quejas_equipo` | 55-63 | 9 | **ENTRARIA** |
| 3 | `correr_semana_arreglo_averias_gestion` | 65-71 | 8 | **ENTRARIA** |
| 4 | `dar_guia_humilde_tres_tecnicas` | 77-95 | 15 | **ENTRARIA** |
| 5 | `dar_guia_util_cuatro_recordatorios` | 97-113 | 10 | **ENTRARIA** |
| 6 | `dar_guia_acto_cinco_consejos` | 115-135 | 14 | **ENTRARIA, con una cifra suya que no reproduzco** (`4.2`) |
| 7 | `elegir_medio_dar_guia_jerarquia_modos` | 137-153 | 13 | **ENTRARIA** |
| 8 | `elogiar_publico_criticar_privado_sus_tres_matices` | 155-163 | 9 | **ENTRARIA**, con una tension interna menor (`4.3`) |
| 9 | `evitar_personalizar_guia_aceptar_personal` | 165-177 | 12 | **ENTRARIA** |
| 10 | `medir_guia_propia_pegatinas_marco` | 179-203 | 13 | **ENTRARIA** |
| 11 | `practicar_franqueza_radical_jefe_propio` | 205-221 | 17 | **ENTRARIA** |
| 12 | `comprobar_criticas_hombre_mujeres_equipo` | 291-293 | 6 | **ENTRARIA**, y no es gemela de la 13 (`4.4`) |
| 13 | `exigir_critica_jefe_reticente` | 295-299 | 9 | **ENTRARIA**, y no es gemela de la 12 (`4.4`) |
| 14 | `impedir_punialadas_espalda_equipo` | 363-367 | 9 | **ENTRARIA** |
| 15 | `fomentar_guia_reciproca_companieros` | 369-381 | 13 | **ENTRARIA** |

**LAS QUINCE PIEZAS QUE ELIGIERON SON LAS QUINCE QUE YO HABRIA ELEGIDO**, y mi particion de la
seccion `3` les da **los mismos limites de linea, pieza a pieza, sin una sola discrepancia de
corte**. No es un cumplido: **es el dato que hace informativa la comparacion**, porque significa
que donde discrepamos (`3.1`) no discrepamos por leer distinto el capitulo.

### 4.1. **LAS DOS PIEZAS LARGAS DE GENERO QUE NO DAN NODO: COINCIDO, Y DIGO POR QUE**

`227-249` (884 pal) y `251-283` (1.006 pal) son **diagnostico y casos**, y las dos rematan en
una META y no en un acto: *We must stop gender politics* (`L249`) y *We must stop this madness,
too* (`L283`). **`D.27` restriccion 1 excluye exactamente eso.** Lo unico accionable que hay en
las dos, no contenerse al criticar a las mujeres del equipo, **es el acto que `291-293` si
procedimenta**, y por eso el nodo esta ahi y no aqui.

### 4.2. **DISCUTIBLE 2, Y ES UNA CIFRA: `dar_guia_acto_cinco_consejos` DICE CINCO Y EL LIBRO ROTULA SEIS**

El id del candidato dice `cinco_consejos`, y su `resumen_teorico` escribe *son CINCO consejos
rotulados uno a uno por el libro* y los enumera: decirlo en dos o tres minutos, dejar holgura en
el calendario, no guardarlo para la reunion uno a uno, la vida media corta y los agujeros
negros.

**Falta uno, y el propio candidato lo transcribe en su paso `P12`.** Instrumento, con el
criterio escrito delante y su salida entera:

    INSTRUMENTO: primera frase de cada linea con contenido de L117 a L135, con su cuenta
    de palabras. CRITERIO: rotulo de consejo = primera frase de 12 palabras o menos.

    L117   38 pal              Giving guidance as quickly and as informally as possible ...
    L119   13 pal              If you wait too long to give guidance, everything about it ...
    L121   14 pal              Of course, there are times when you should wait to praise ...
    L123    7 pal  <-- ROTULO  Say it in 2-3 minutes between meetings.
    L125   21 pal              So let me reiterate: impromptu guidance really, truly is ...
    L127   12 pal  <-- ROTULO  Keep slack time in your calendar, or be willing to be late.
    L129   11 pal  <-- ROTULO  Dont save up guidance for a 1:1 or a performance review.
    L131    5 pal  <-- ROTULO  Guidance has a short half-life.
    L133    7 pal  <-- ROTULO  Unspoken criticism explodes like a dirty bomb.
    L135    3 pal  <-- ROTULO  Avoid black holes.

    rotulos de consejo en L115-135: 6 [123, 127, 129, 131, 133, 135]

**EL QUE FALTA ES `L133`, `Unspoken criticism explodes like a dirty bomb`**, que tiene la misma
forma que los otros cinco y que el candidato transcribe entero en su `P12`.

**DIGO LO QUE MI INSTRUMENTO NO PRUEBA, porque esa es justamente la caida que el auditor de la
18 se declaro a si mismo:** el umbral de doce palabras es un **FILTRO y no un juez**. Corrido
sobre `L77-95` tambien recoge `Heres how it works.`, que es un conector y no un rotulo. **En el
tramo `L115-135` no hay ningun conector entre los seis**, y por eso aqui el filtro y el juicio
coinciden. **Quien quiera tumbar mi seis tiene los seis renglones delante para hacerlo.**

**LOS PASOS NO ESTAN MAL: ESTA MAL LA CUENTA.** Los catorce pasos transcriben los seis consejos.
Lo que dice cinco es **el id del nodo y su resumen**, y las dos cosas viajan al grafo.

### 4.3. La tension interna de `elogiar_publico_criticar_privado_sus_tres_matices`, que **NO** subo a caida

Su titulo y su id dicen **tres**, y su resumen dice *detras van DOS consejos rotulados*. Las dos
lecturas son defendibles y el propio resumen explica la suya: cuenta `L161` y `L163` como
rotulos y trata `L159` como el parrafo que pone la frontera. **El titulo cuenta las tres cosas
que `L157` anuncia (*Here are some things to think about*), y ahi hay tres.** No reproduzco
ninguna cifra falsa: reproduzco **dos criterios distintos dentro del mismo fichero**. Lo dejo
anotado y **no lo cuento como caida.**

### 4.4. `comprobar_criticas_hombre_mujeres_equipo` y `exigir_critica_jefe_reticente` **NO son gemelas**

Mi barrido las levanta la una contra la otra (`6`). **Las lei antes de mirar la senial** y las
sostengo las dos, con la vara de `6.1`:

| | `comprobar_criticas...` | `exigir_critica...` |
|---|---|---|
| **quien actua** | el jefe, hombre | quien recibe la guia |
| **hacia donde** | hacia abajo | hacia arriba |
| **el acto** | preguntar como cae tu guia y pedir que te midan | decir una de tres frases, parar, contar hasta seis |
| **el entregable** | saber si te estas conteniendo | arrancar una valoracion franca |

**El libro pone las dos caras del mismo problema con un rotulo cada una**, y eso es
`DOS DOCTRINAS LEGITIMAS NO SON DUPLICADO` de la vara, no un gemelo. **La arista entre ellas es
otra cosa y no la adjudico aqui.**

---

## 5. LOS 177 PASOS CONTRA SU PARRAFO (`D.30`), LEIDOS UNO A UNO

**Lei los 177 y el capitulo entero.** Los dos instrumentos que corri buscan las especies de
puente que el lote 1 pago caras:

    $ (programa) pasos totales de los 15 candidatos de cap_09 : 177
    $ (programa) pasos con marca de periodo                   :   9
    $ (programa) pasos con cifra                              :  29

**LOS NUEVE PERIODOS SON DEL LIBRO, uno a uno:**

| paso | el periodo | donde lo escribe el libro |
|---|---|---|
| `abrazar` P14 | cada vez que interrumpiera | `L49` *every time I interrupted him* |
| `abrazar` P17 | por semana | `L53` *How many times each week* |
| `dar_guia_acto` P07 | tres veces por semana, sesenta minutos por semana | `L125` *three times a week ... sixty minutes per week* |
| `dar_guia_acto` P10 | cada dia | `L129` *what we do every day* |
| `dar_guia_humilde` P03 | cada vez que des guia | `L83` *when giving feedback* |
| `elegir_medio` P13 | cada dia | `L153` *calling me every day* |
| `medir_guia` P02 | cada semana | `L183` *gauge your guidance each week* |
| `medir_guia` P08 | a diario | `L189` *exposes people daily* |
| `medir_guia` P12 | a diario | `L197` *manage yourself, daily* |

**Y LAS CIFRAS DE CONTENIDO TAMBIEN SON DEL LIBRO:** los sesenta del `L33`, el contar hasta seis
del `L41` y del `L299`, los dos o tres minutos y los veinticinco y cincuenta del `L123` y del
`L127`, la diapositiva seis y el cinco por ciento y el cien por cien del `L159`, los quince
segundos del `L181`, el `One, Two, Three, Four` del `L189`, los veinte dolares del `L373`.

> **MI VEREDICTO DE FIDELIDAD, A CIEGAS: `177 de 177 TRANSCRIPCION, 0 PUENTE`.** No encontre un
> solo paso que ponga periodo, destinatario, responsable ni cifra que el capitulo no escriba.
> **La unica cuenta que no reproduzco no vive en ningun paso: vive en el id y en el resumen del
> candidato 6** (`4.2`).

**Y DIGO LO QUE NO PUEDO FIRMAR AQUI:** `PASOS INVENTADOS POR CAPITULO` es una cifra mia
(`8.3` de mi protocolo) y su numerador lo declara el reporte, que no tengo. **Lo que firmo hoy
es el denominador, 177 pasos de `cap_09`, y mi propia lectura de fidelidad.** El porcentaje va
en el acta.

---

## 6. EL BARRIDO DE VECINOS SOBRE **GRAFO MAS BANDEJAS** (`D.38.4`)

**La poblacion la construyo yo y la mido antes de usarla.** Es `dataset/nodos.jsonl` mas todo lo
que espera en `cuarentena/<libro>/`, descartando `_insertados` y `_derivadas`:

    $ wc -l dataset/nodos.jsonl                                            ->  203
    $ ls cuarentena/scott_radical_candor/*.json | wc -l                     ->   78
    $ ls cuarentena/ensayo_referencia_163/*.json | wc -l                    ->  163
    $ ls cuarentena/smart_who cuarentena/onu_consumidor cuarentena/zhuo_manager  ->    0

    POBLACION D.38.4 total                   : 444 = 203 del grafo + 241 de bandeja
    POBLACION sin el catalogo de control     : 281 = 203 del grafo +  78 del lote 4

**Cada candidato se barre contra 443, que es la poblacion menos el propio candidato**, con
`python forja.py informe` y `FORJA_DATASET` apuntando a la poblacion construida: **el
instrumento es el de la casa y no uno mio.**

Y una medida que enmarca todo el barrido:

    $ (programa) nodos del grafo con fuente scott_radical_candor  ->  0
    $ (programa) reparto del grafo por fuente:
        zhuo_manager 136 | smart_who 59 | onu_consumidor 6 | manual_sistema_conocimiento 2

**Ni un nodo del lote 4 esta en el grafo**, asi que todo vecino de un candidato de `cap_09` que
no sea ruido tiene que salir de la bandeja. **Es exactamente el caso que `D.38.4` vino a
cubrir**, y el motivo por el que barrer solo contra el grafo habria dado quince ceros.

### 6.1. La salida del barrido, los quince, entera

**Fichero testigo: `.barrido_v19/BARRIDO_TOTAL.txt`**, que existe y no esta a cero bytes
(`7.B` de la cosecha: una ruta que promete prueba es cifra).

    $ wc -c .barrido_v19/BARRIDO_TOTAL.txt   ->  6412
    $ grep -c "^### " .barrido_v19/BARRIDO_TOTAL.txt   ->  15

| candidato | la aduana en seco dice | vecinos por encima de umbral |
|---|---|---|
| `abrazar_incomodidad_arrancar_critica_equipo` | **ENTRARIA** | ninguno |
| `organizar_sistema_recoger_quejas_equipo` | BLOQUEARIA | `elogiar_publico...` 0,357 |
| `correr_semana_arreglo_averias_gestion` | BLOQUEARIA | `comprobar_criticas...` 0,356 |
| `dar_guia_humilde_tres_tecnicas` | BLOQUEARIA | `elogiar_publico...` 0,350 |
| `dar_guia_util_cuatro_recordatorios` | **ENTRARIA** | ninguno |
| `dar_guia_acto_cinco_consejos` | **ENTRARIA** | ninguno |
| `elegir_medio_dar_guia_jerarquia_modos` | **ENTRARIA** | ninguno |
| `elogiar_publico_criticar_privado_sus_tres_matices` | BLOQUEARIA | `dar_guia_humilde...` 0,352 |
| `evitar_personalizar_guia_aceptar_personal` | BLOQUEARIA | **`manejar_enfado_persona_desafiada`, paso contra nodo 0,867** |
| `medir_guia_propia_pegatinas_marco` | **ENTRARIA** | ninguno |
| `practicar_franqueza_radical_jefe_propio` | **ENTRARIA** | ninguno |
| `comprobar_criticas_hombre_mujeres_equipo` | BLOQUEARIA | `exigir_critica...` 0,402 y `correr_semana...` 0,366 |
| `exigir_critica_jefe_reticente` | BLOQUEARIA | `comprobar_criticas...` 0,382 |
| `impedir_punialadas_espalda_equipo` | **ENTRARIA** | ninguno |
| `fomentar_guia_reciproca_companieros` | **ENTRARIA** | ninguno |

    8 de 15 ENTRARIA limpios, 7 de 15 BLOQUEARIA, 5 pares distintos levantados

> ### **Y AQUI ESTA EL DATO QUE JUSTIFICA `D.38.4` ENTERA, MEDIDO EN ESTA VUELTA**
>
> **LOS CINCO PARES TIENEN LOS DOS EXTREMOS EN LA BANDEJA. NI UNO SOLO DE LOS VECINOS ESTA EN
> EL GRAFO.** Es aritmetica y no opinion: el grafo tiene 203 nodos y **cero** con fuente
> `scott_radical_candor`.
>
> **BARRIENDO SOLO CONTRA `dataset/nodos.jsonl`, los quince habrian salido `ENTRARIA` limpios
> y los cinco pares no existirian.** El acta 14 lo dijo con un caso; esta vuelta lo dice con
> **cinco de cinco.**

### 6.2. **DISCUTIBLE 6: el par mas fuerte del barrido, y es de dos capitulos distintos**

    vecino manejar_enfado_persona_desafiada  [levantada por: paso_contra_nodo]
      similitud_texto 0.234 | familia_id 0.000 | paso_contra_nodo 0.867
      paso 9 del candidato contra paso 5 de manejar_enfado_persona_desafiada

**Los dos pasos, uno al lado del otro:**

| | |
|---|---|
| `evitar_personalizar...` **P9** (`cap_09`, `L175`) | *Elimina de tu vocabulario la frase no te lo tomes como algo personal, que el texto llama **peor que inutil**.* |
| `manejar_enfado...` **P5** (`cap_04`, `L131`) | *Elimina de tu vocabulario la frase no te lo tomes como algo personal. El texto dice que es **insultante**.* |

**LAS DOS TRANSCRIPCIONES SON CORRECTAS Y LO COMPROBE EN LOS DOS CAPITULOS**, que es lo primero
que habia que descartar:

    $ (cap_09 L175) The phrase "don't take it personally" is worse than useless.
    $ (cap_04 L131) Eliminate the phrase "don't take it personally" from your
                    vocabulary - it's insulting.

**EL LIBRO DICE EL MISMO ACTO DOS VECES, EN DOS CAPITULOS, CON DOS MOTIVOS DISTINTOS.**

**MI ADJUDICACION A CIEGAS: NO SON GEMELOS**, con la vara de `6.1` y sin bascula:

| la vara | que veo |
|---|---|
| **direccion** | `cap_04` (`Cap. 1`) va primero y `cap_09` (`Cap. 6`) vuelve sobre ello. La pregunta es que aniade el de `cap_09`, y aniade once pasos mas |
| **sin bascula** | el solape es **un paso de doce contra uno de siete**. Lo que decide no es el tamanio |
| **lo que queda fuera** | **es procedimiento en los dos lados**: en `cap_04`, la secuencia de manejar el enfado ya declarado; en `cap_09`, el error fundamental de atribucion, situacion mas comportamiento mas impacto, y el cambio de *tu estas mal* por *creo que eso esta mal* |
| **condicion de activacion** | distintas y sin solape: *alguien ya esta enfadado contigo* frente a *vas a dar guia y la explicacion que te sale es un rasgo de caracter* |

**NO ES FUSION Y TAMPOCO ES `MUTUO`:** ninguno de los dos DESPLIEGA el paso del otro, que es lo
que `MUTUO` pide; **los dos escriben el mismo acto en una linea.** Lo que corresponde es
**arista declarada**, y la declara quien inserte, no yo aqui.

> **Y LO DIGO CON LA LETRA QUE ME INCOMODA DELANTE:** *LA ARISTA NO EXCULPA* (`6.1`). No estoy
> usando el cable para absolver el par: **estoy leyendo los pasos, que es lo que `D.19` obliga**,
> y lo que queda fuera del solape es procedimiento en los dos lados. **Si el reporte lo adjudico
> al reves, la discrepancia se lee en mi turno normal y no aqui.**

### 6.3. Los otros cuatro pares, despachados con su motivo

| par | senial | mi lectura |
|---|---|---|
| `comprobar_criticas` con `exigir_critica` | 0,402 y paso 1 contra paso 1 a 0,577 | **el paralelismo es del libro**: `L293` escribe *it can be helpful to become aware of how the woman feels* y `L297` abre con *Similarly*. Dos caras, dos rotulos, dos nodos (`4.4`) |
| `dar_guia_humilde` con `elogiar_publico` | 0,350 | los dos hablan de elogio arrogante frente a elogio especifico. **Actos distintos: la tecnica de situacion mas comportamiento mas impacto no es la regla de donde se dice** |
| `organizar_sistema` con `elogiar_publico` | 0,357 | **ruido de vocabulario**: reunion general, publico, equipo. Nada comun en el acto |
| `correr_semana` con `comprobar_criticas` | 0,356 | **ruido**: una semana de arreglo de averias de gestion contra comprobar si te contienes al criticar. **Ninguna senial separa jerarquia de ruido** (`D.19`), y aqui se ve |

---

## 7. LOS DISCUTIBLES QUE MARCO **ANTES** DE SABER SI ACIERTO

| # | que marco | por que |
|---:|---|---|
| **1** | **El corte de `cap_09` es una seleccion y no un truncamiento** (`3.1`) | quedan cuatro piezas que dan nodo, 4.333 palabras de 17.482, y una de ellas (`331-361`) va ANTES de la ultima escrita. **La regla que cubre el cierre corto por techo no cubre saltarse una pieza de en medio**, y el registro del lote no puede decir `cap_09` minado a secas |
| **2** | **`dar_guia_acto_cinco_consejos` dice cinco y el libro rotula seis** (`4.2`) | la cifra vive en el id y en el resumen, que viajan los dos al grafo. **Los pasos estan bien: los seis estan transcritos** |
| **3** | **La sede de la cifra del discutible 2** | un id y un `resumen_teorico` en cuarentena, ¿son sede de `CIFRA PUBLICADA` de `5.2`? La tabla nombra `docs/`, `config/`, `esquema/` y el codigo de una guarda, **y el dataset aparece en la fila de `CLASE`, no en la de `CIFRA`.** Lo traigo sin resolverlo |
| **4** | **La `7.5` no me llego por el arnes** (`0`) | la tarea bloqueante escrita para mi vuelta no venia en `REMEDIOS PENDIENTES QUE HEREDAS`. La cumplo igual porque abri el acta. **Es averia de la entrega de `D.40`, no de la regla** |
| **5** | **`forja.py guiones` no barre lo que esta casa escribe dentro de una bandeja** (`8.1`) | lo comprobe, **y lo comprobe porque casi publico que era una guarda rota.** No lo es: el acotamiento esta escrito en el codigo con su motivo. **Lo subo porque la frontera importa, no porque muerda hoy** |

---

## 8. EL ESTADO DEL ARBOL AL CERRAR ESTA FASE

### 8.1. **LA COMPROBACION QUE ME HABRIA HECHO PUBLICAR UNA GUARDA ROTA, Y NO LA PUBLICO**

Al limpiar mi propio rojo de guiones encontre que `cuarentena/ensayo_referencia_163/` tiene
**nueve guiones largos literales repartidos en cinco ficheros**, y que `forja.py guiones` da
**VERDE** sobre esa misma carpeta:

    $ python forja.py guiones cuarentena/ensayo_referencia_163/
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ (programa, contando el caracter U+2014 fichero a fichero)
    estrategia_multicanal_bienvenida.json        largo U+2014 2
    metas_vs_proposito.json                      largo U+2014 2
    mitos_stage_gate.json                        largo U+2014 2
    restricciones_extremas_como_innovacion.json  largo U+2014 2
    sistemas_alta_confiabilidad_hro.json         largo U+2014 1
    total: 9

**PARECE UNA GUARDA QUE NO MUERDE, QUE ES `CIFRA PUBLICADA` POR `7.C` DE LA COSECHA. NO LO ES**,
y el instrumento que lo dice es el propio codigo:

    $ (programa) src.guiones.barrer_archivo(metas_vs_proposito.json)
      -> los DOS hallazgos, uno a uno, con su linea y su columna
    $ (programa) len(list(comun.archivos_del_repo(None)))  ->  164 ficheros en todo el repo
    $ (programa) de ellos, de ensayo_referencia_163        ->    1
    $ (programa) de ellos, de scott_radical_candor         ->    0

`src/comun.py` L261-285 lo dice con sus palabras y con su motivo escrito: **dentro de una
bandeja solo se barre lo que esta casa escribe, y eso tiene un nombre fijo, `LEEME.md`.** El
material ajeno que la rodea, no. **La guarda no esta rota: esta acotada, y el acotamiento esta
declarado en el sitio donde vive.**

**Y COMPRUEBO QUE EL ACOTAMIENTO NO ESCONDE NADA NUESTRO:**

    $ (programa) guiones largos o medios en cuarentena/scott_radical_candor/  ->  0
    $ (programa) guiones largos o medios en dataset/nodos.jsonl               ->  0
    $ (programa) guiones largos o medios en bitacora/                         ->  0

> **LO ESCRIBO PORQUE ESTUVE A UN PASO DE PUBLICARLO COMO CAIDA AJENA.** La cifra era cierta
> (los nueve guiones estan ahi) y la conclusion habria sido falsa. **Es la misma averia que la
> `7.1` del acta anterior vista desde el otro lado: un instrumento que no comprueba lo que la
> cifra dice.** Esta vez la comprobacion la corri ANTES de escribir, y por eso lo que se publica
> es el acotamiento y no una caida inventada.

### 8.2. El arbol antes del sello

**Los dieciocho guiones largos de la seccion `2` eran mios y estan retirados.** Los ficheros de
trabajo que los llevaban (`grafo.jsonl`, `bandejas.jsonl`, `pob.jsonl` y los `pob_N.jsonl`) se
borran despues de usarlos, y en su lugar queda el guion que los reconstruye,
`.barrido_v19/construir_poblacion.py`, para que el barrido sea repetible sin dejar el arbol en
rojo.

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ git status --porcelain
     M docs/loop/APERTURA_CIEGA.md
     D docs/loop/REPORTE.md
     D docs/loop/loop.log
     M docs/loop/ultimo_apertura.json
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json
    ?? .barrido_v19/

    $ wc -c .barrido_v19/BARRIDO_TOTAL.txt
    6412 .barrido_v19/BARRIDO_TOTAL.txt

**LO QUE QUEDA EN EL ARBOL Y ES MIO:** `docs/loop/APERTURA_CIEGA.md`, que es lo que el arnes
sella, y `.barrido_v19/`, que son los cuatro ficheros del barrido mas su testigo. **Lo demas
son las cuatro retiradas del arnes y el `ultimo_apertura.json` a cero bytes**, y ninguna de las
dos cosas es mia.

> **NO BORRO `.barrido_v19/`.** `7.B` de la cosecha dice que una ruta publicada como evidencia
> es cifra, y yo publico `.barrido_v19/BARRIDO_TOTAL.txt` como la prueba del barrido de la
> seccion `6`. **Borrarlo convertiria mi propia seccion 6 en una firma en vez de una prueba.**
>
> **Y NO REPITO LA CAIDA DEL AUDITOR ANTERIOR:** su rojo entro DESPUES del sello, por su mensaje
> final. **El mio entro antes, lo vio el instrumento, y por eso esta remediado aqui y no
> declarado en la proxima acta.** La segunda pasada, la de mi mensaje final, me la llevo puesta
> al cerrar: **cero guiones largos y cero guiones medios en lo que yo escriba fuera de este
> fichero.**

---

## 9. LO QUE ESTA APERTURA AFIRMA, EN UNA TABLA

| | |
|---|---|
| **vuelta que abro** | **19**, lote 4 (`scott_radical_candor`), `cap_09` (`Cap. 6`, *Guidance*) |
| **acta anterior leida** | `80fd74cdf15bb0b1ff02bcbe560ba03f11f22472`, remedida por `git hash-object` |
| **herencia `D.40`** | **`HEREDADO 1`: CUMPLIDO**, fila a fila, **mas la `7.5` que el arnes no entrego y que cumplo igual** |
| **frontera** | **29 piezas, 19 dan nodo, 10 no. Cero huecos, cero solapes, 17.482 = 17.482** |
| **lo que falta del capitulo** | **4 piezas y 4.333 palabras de 17.482** que dan nodo y no tienen candidato |
| **candidatos clasificados** | **15 de 15** candidatos de `cap_09`, todos `ENTRARIA` por mi lectura |
| **coincidencia de corte** | **15 de 15 piezas con los mismos limites de linea** que mi particion independiente |
| **pasos releidos** | **177 de 177** contra su parrafo. **Cero puentes de periodo, cifra, destinatario o responsable** |
| **barrido `D.38.4`** | **444 de poblacion** (203 del grafo mas 241 de bandeja), **281 sin el catalogo de control** |
| **discutibles marcados a ciegas** | **5** |
| **contaminacion propia declarada** | **1**: `git log --oneline` me adelanto tres cifras del extractor (`1.1`) |
| **rojo propio detectado y remediado en esta fase** | **1**: 18 guiones largos de mis ficheros de trabajo (`2` y `8.2`) |
