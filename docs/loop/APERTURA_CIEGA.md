# APERTURA CIEGA. VUELTA 19 del bucle, lote 4 (`scott_radical_candor`), `cap_09` (Cap. 6, `Guidance`)

*Fase ciega del turno de auditor. Escrita ANTES de ver `docs/loop/REPORTE.md`, que no esta
en el arbol. Esta es la lectura que despues se compara con la del extractor.*

---

## 0. LA HERENCIA, DECLARADA ANTES DE NADA (`D.40`)

> ### **ACTA ANTERIOR LEIDA: `80fd74cdf15bb0b1ff02bcbe560ba03f11f22472`**

**LA HUELLA NO ME LA CREO, LA REMIDO.** La que el prompt me entrega y la que da el
instrumento sobre el fichero que tengo delante son la misma:

    $ git hash-object docs/loop/ACTA_AUDITOR.md
      80fd74cdf15bb0b1ff02bcbe560ba03f11f22472

    $ wc -l docs/loop/ACTA_AUDITOR.md
      17295 docs/loop/ACTA_AUDITOR.md

**Y LA ABRI**, que es lo que `D.40` vino a arreglar despues de que tres actas seguidas
perdieran el mismo remedio. De ella salen la seccion `7.5` y la `7.6` que cito abajo, y de
ella sale que la ultima acta escrita es la `ACTA 18` y cubre la vuelta 18: **no hay hueco de
acta**, y la vuelta que me toca auditar es la inmediatamente siguiente, la 19.

    $ grep -n "^# ACTA " docs/loop/ACTA_AUDITOR.md | tail -1
      16581:# ACTA 18. VUELTA 18, lote 4 (`scott_radical_candor`), `cap_08`: la vuelta que
      cerro donde debia, la errata de mi propio metodo, y una cifra falsa mia en la frontera

### `HEREDADO 1`: **CUMPLIDO**

**QUE ERA.** La seccion `7.6` de la `ACTA 18` (linea 17197 del acta), *los remedios mios que
SI aguantaron, porque `REMEDIO ROTO` solo informa si tambien se declara cuando aguanta*. **El
remedio no es una tabla: es la obligacion de volver a publicarla**, con cada remedio mio
vivo, su comprobacion EN ESTA VUELTA y su resultado, tambien cuando aguanta. **Aqui esta,
rehecha contra esta vuelta y no copiada de la anterior:**

| remedio mio | comprobacion EN ESTA VUELTA | resultado |
|---|---|---|
| `D.40`, leer `ACTA_AUDITOR.md` en la fase ciega antes de escribir | esta misma seccion `0`, con la huella remedida por `git hash-object` y el heredado resuelto | **CUMPLIDO** |
| `D.38.4`, barrido sobre grafo mas bandejas | seccion `6`: `444 = 203 + 241`, y `443` por candidato al excluirse a si mismo, las tres cifras con su instrumento pegado | **CUMPLIDO, y esta vez decidio el resultado**: los 8 vecinos estan los 8 en la bandeja y 0 en el grafo |
| `D.38.3`, toda cifra de la fase ciega con su instrumento al lado | todas las cifras de este fichero llevan su comando y su salida literal pegados | **CUMPLIDO** |
| `D.34`, no recuperar de git los cuatro ficheros retirados | no corri `git show` ni `git checkout` sobre ninguno de los cuatro. **La contaminacion que si hubo la declaro entera en `1.2`**, y es mia | **CUMPLIDO, con una falta propia declarada al lado** |
| `D.34`, no tocar `APERTURA_CIEGA.md` tras el sello | no aplica todavia en esta fase: el sello lo pone el arnes cuando yo termine. **Lo que si declaro es que no abri la apertura anterior de esta misma vuelta** (`1.3`) | **PENDIENTE DE COMPROBAR AL CERRAR EL TURNO**, y lo digo en vez de darlo por hecho |
| `ACTA 18` `7.5`, las tres ordenes | seccion `0.bis`, una por una y con sus salidas | **DOS CUMPLIDAS, UNA IMPOSIBLE DE CUMPLIR EN LA LETRA Y DECLARADA** |
| `5.5`, re correr por mutacion toda guarda declarada mordiendo | **NO APLICA EN ESTA FASE, y este es el motivo escrito:** esa orden muerde sobre las guardas que EL REPORTE declara mordiendo, y el reporte no esta en el arbol. Es trabajo de mi turno normal, no de la fase ciega | **NO APLICA, con motivo** |

---

## 0.bis. LA TAREA BLOQUEANTE QUE ME DEJE YO MISMO, Y QUE EL ARNES NO ME ENTREGO

**EL ARNES ME ENTREGO UN HEREDADO Y LA `ACTA 18` ME DEJO DOS COSAS.** Su seccion `7.5` se
titula **TAREA BLOQUEANTE DEL AUDITOR DE LA VUELTA 19, ESCRITA POR EL DE LA 18**, y ese
auditor de la vuelta 19 soy yo. **La cumplo, y digo que la encontre leyendo el acta y no en el
prompt:** es exactamente el trabajo que `D.40` quiere que no dependa de la memoria, y esta vez
dependio de que yo abriera el fichero.

### ORDEN 1. **LA FRONTERA SE CIERRA CONTRA EL CUERPO, O NO SE PUBLICA.** CUMPLIDA

    $ python .barrido_v20/cerrar_frontera.py
      CIERRE DE LA FRONTERA CONTRA EL CUERPO (ORDEN 1, ACTA 18 seccion 7.5)
        cuerpo medido        : lineas 8 a 433
        lineas con contenido NO cubiertas      : 0
        SOLAPES                                : 0
        suma de las filas                      : 17482 palabras
        cuerpo medido aparte (sed 8,$ | wc -w) : 17482 palabras
        LOS DOS N SON EL MISMO                 : SI

        piezas de la frontera (wc -l del tsv)  : 28
        piezas que DAN NODO                    : 19
        piezas que NO dan nodo                 : 9
        19 + 9 = 28

**Y EL SEGUNDO `N` MEDIDO POR EL INSTRUMENTO LITERAL QUE LA ORDEN NOMBRA, aparte del script:**

    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_09.md | wc -w
      17482

**Los dos `17482` salen de dos caminos distintos:** uno suma las 28 filas de mi frontera una
por una, el otro mide el cuerpo entero sin mirar la frontera. **Por eso la cuenta de piezas se
publica.**

### ORDEN 2. **TODA CIFRA MIA LLEVA SU DENOMINADOR EN LA MISMA FRASE.** CUMPLIDA, Y CON UNA CAIDA MIA CAZADA POR ELLA

**LA ORDEN ME MORDIO A MI, EN ESTA MISMA FASE, Y LO DIGO PORQUE ES SU UNICA PRUEBA UTIL.** El
primer script con el que reparti el cuerpo por clases imprimia la etiqueta
`piezas que dan nodo Y tienen candidato (11 de 19)`. **La cifra de palabras era buena y la
etiqueta era falsa: son 15 de 19, no 11 de 19.** Lo vi al leer la salida antes de pegarla,
**rehice el script con el denominador correcto y no pegue la version mala.** La cifra que se
publica en `5.1` es la de la segunda corrida.

**NO ES `CIFRA PUBLICADA PROPIA`, y digo por que en vez de dejarlo a interpretacion:** la
especie de `D.38.2` vive en *mi acta o mi apertura sellada*, y esa etiqueta **no llego a
ninguna de las dos.** Pero es la misma familia de las tres caidas que la `ACTA 18` se apunto,
**y la orden que la caza es justamente la que aquella acta escribio.**

**Y NO FUE LA UNICA. Las ordenes 1 y 2 me cazaron CUATRO cosas mias en esta fase, todas antes
del sello**, y las cuatro estan declaradas donde salieron:

| lo que estaba mal | donde lo declaro |
|---|---|
| la etiqueta `11 de 19` por `15 de 19` | aqui arriba |
| un `grep` citado que **no reproducia su propia cifra** (le faltaba un termino del patron) | `5.3` |
| *los 8 vecinos* donde la lista tenia **6 nodos distintos** | `6.3` |
| *mas de hora y media* de barrido donde el fichero dice **50 minutos y 14 segundos** | `6.2` |

**LAS CUATRO SALIERON DE RE CORRER MIS PROPIOS COMANDOS Y RELEER MIS PROPIAS CIFRAS CONTRA SU
SALIDA, y ninguna de las cuatro la habria visto releyendo el texto.** Eso es lo que valen las
dos ordenes.

### ORDEN 3. **EL BARRIDO DE GUIONES SE CORRE DOS VECES.** CUMPLIDA LA PRIMERA MITAD. **LA SEGUNDA NO SE PUEDE CUMPLIR EN LA LETRA Y LO DECLARO**

**La primera corrida, antes del sello, en verde:**

    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**Y VERDE DESPUES DE ARREGLAR ALGO QUE ROMPI YO, que es lo que la orden vino a cazar.** Mis
volcados de poblacion de usar y tirar (`.barrido_v20/pob*.jsonl`) copiaban los 163 nodos del
catalogo de control dentro de una carpeta que el barrido SI mira, y pusieron el repo en rojo:

    $ python forja.py guiones      (con los tres volcados en el arbol)
      BARRIDO DE GUIONES EN ROJO: 27 hallazgo(s)
      ... los 27 hallazgos, en .barrido_v20/pob.jsonl, pob_total.jsonl y pob_sin_control_tmp.jsonl

**LOS TRES VOLCADOS SE BORRARON y la guarda volvio a verde.** Comprobado ademas que **el
original no esta en rojo y que esto no es una grieta de la casa**: los cinco ficheros con
guion largo viven en `cuarentena/ensayo_referencia_163/`, y `src/comun.py` L268 a L285 salta
las bandejas **a proposito y con su motivo escrito** (*dentro de una bandeja solo se barre lo
que esta casa escribe*). **Es material ajeno, y la regla ya lo dice.** No publico un hallazgo
donde no lo hay.

**LO QUE NO SE PUEDE CUMPLIR EN LA LETRA.** La orden pide:

    $ git status --porcelain | grep -v "docs/loop/APERTURA_CIEGA.md"   (VACIO antes del sello)

**Y EN ESTA FASE ESO ES IMPOSIBLE POR CONSTRUCCION, porque quien ensucia el arbol es el arnes:**

    $ git status --porcelain
       D docs/loop/APERTURA_CIEGA.md
       D docs/loop/REPORTE.md
       D docs/loop/loop.log
       M docs/loop/ultimo_apertura.json
       D docs/loop/ultimo_auditor.json
       D docs/loop/ultimo_extractor.json
      ?? .barrido_v19/
      ?? .barrido_v20/

**ESA SALIDA ES DE ANTES DE ESCRIBIR ESTE FICHERO**, y por eso `APERTURA_CIEGA.md` sale ahi
como `D` y no como `M`. Corrida despues de escribirlo, la primera linea pasa a
`M docs/loop/APERTURA_CIEGA.md` **y las otras siete no se mueven**, que es lo que la orden
queria mirar.

**Las seis primeras lineas son obra del arnes** (`D.34.2` retira cuatro ficheros y toca
`ultimo_apertura.json`), **no mias, y no puedo dejarlas vacias sin recuperar justo lo que
`D.34` me prohibe recuperar.** **MI REMEDIO SE ESCRIBIO SUPONIENDO UN ARBOL LIMPIO Y LA FASE
CIEGA NO LO TIENE NUNCA.** Ese es un defecto del remedio, es mio, y lo declaro aqui en vez de
apuntarme la orden como cumplida.

**LO QUE SI PUEDO HACER Y HAGO: separar mi suciedad de la del arnes, y declarar la mia.**

| entrada | de quien es | que hago |
|---|---|---|
| los seis `D` y `M` de `docs/loop/` | **del arnes** (`D.34.2`) | nada. Tocarlos seria romper `D.34` |
| `?? .barrido_v20/` | **mia, de esta vuelta** | **se queda**, y lo declaro: son los testigos de las cifras que publico, y `7.B` de la cosecha dice que una ruta que promete prueba es cifra. Sus tres `.jsonl` ya estan borrados |
| `?? .barrido_v19/` | **mia, de la corrida de esta misma vuelta que el arnes rechazo** | **no lo borro y no lo abro** (`1.3`). Borrar contenido que ninguna regla ordena lo reserva Alexis (`AUDITOR_FORJA.md` 3) |

**LA SEGUNDA CORRIDA DE `guiones`, la del cierre del turno normal, no es de esta fase** y va
cuando toque.

---

## 1. QUE ESTOY AUDITANDO, Y LA CONTAMINACION QUE DECLARO YO

### 1.1. La vuelta

**VUELTA 19, lote 4 (`scott_radical_candor`), `cap_09.md`, unidad `Cap. 6`, titulo textual
`Guidance`.** La cabecera del propio fuente lo dice, y no lo deduzco:

    $ sed -n '1,7p' fuentes/scott_radical_candor/cap_09.md
      ---
      libro: Scott, Radical Candor
      edicion: Fully Revised & Updated Edition, St. Martin's Press, First Edition October 2019
      unidad: Cap. 6
      titulo_textual: Guidance
      fidelidad: verbatim
      ---

### 1.2. **CONTAMINACION QUE DECLARO, Y ES MIA**

**CORRI `git log --format="%h %ad %s" -15` PARA SABER EN QUE VUELTA ESTABA, Y ESO ME TRAJO LOS
ASUNTOS DE LOS COMMITS DEL EXTRACTOR.** El asunto de `a692c26` dice **cap_09 del lote 4 (Cap.
6, Guidance): 15 candidatos, 177 pasos, cero puentes, y la vuelta cierra ahi por el techo de
candidatos**, y el de `0dcb431` dice **la frontera de cap_09 publicada ANTES de cortar: 30
piezas, 20 dan nodo, 10 no con su motivo**.

**QUE SIGNIFICA Y QUE NO.** No es ninguno de los cuatro ficheros que `D.34.2` retira, y el
asunto de un commit no es sede de cifra (`5.6`). **Pero son cifras del extractor que yo tenia
delante antes de escribir las mias, y callarlo seria peor que haberlas visto.** La `ACTA 18`
declaro una contaminacion de la misma familia (un `git show --stat` sin `--format=""`), asi
que **es la segunda vuelta seguida que la puerta del `git log` me ensucia la fase ciega.**

**LO QUE HICE CON ELLO.** Mi frontera de la seccion `3` esta construida **leyendo el capitulo
entero y cerrandola contra el cuerpo**, no ajustandola a `30 / 20 / 10`. **Y no cuadra con la
suya: yo publico 28 piezas, 19 que dan nodo y 9 que no.** Si hubiera estado copiando, habria
copiado bien. **La discrepancia entre las dos lecturas es justo lo que la fase ciega existe
para producir**, y va a mi turno normal.

### 1.3. **LA APERTURA ANTERIOR DE ESTA MISMA VUELTA EXISTE, Y NO LA ABRI**

**Esta vuelta ya tuvo una fase ciega mia.** El arnes la rechazo por un falso positivo de la
guarda de `D.40`, el fundador lo dictamino en
`docs/loop/paradas/2026-09-12-d40-falso-positivo.md` (*la guarda era mas estricta que la
letra, la apertura estaba bien*), **y el arnes me relanzo con `APERTURA_CIEGA.md` retirado del
arbol.** Aquel texto vive en el commit `a653ffd`.

**NO CORRI `git show` NI `git checkout` SOBRE EL, Y ESTA CLASIFICACION ESTA HECHA DE NUEVO**,
leyendo el capitulo y los candidatos otra vez. **No estaba prohibido abrirlo** (es obra mia y
no del extractor), **pero el arnes lo retiro del arbol para que yo clasifique, no para que me
copie.** Lo digo para que se pueda comprobar contra `a653ffd` si alguien quiere: **dos
lecturas ciegas mias de la misma vuelta, hechas por separado, valen mas que una repetida.**

**Y NO HAY SELLO ROTO QUE MIRAR:** `SELLOS_APERTURA.jsonl` termina en `8774c59f...`, que es el
sello de la apertura de la vuelta 18, **porque la de la 19 no llego a sellarse nunca.**

    $ tail -1 docs/loop/SELLOS_APERTURA.jsonl
      {"vuelta": 1, "fecha": "2026-09-12 09:47:56", "sello": "8774c59fc95f21483daae2fdabc185199635db26"}

---

## 2. EL MATERIAL QUE TENGO DELANTE, MEDIDO

### 2.1. El fuente

    $ wc -l fuentes/scott_radical_candor/cap_09.md
      433 fuentes/scott_radical_candor/cap_09.md
    $ wc -w fuentes/scott_radical_candor/cap_09.md
      17508 fuentes/scott_radical_candor/cap_09.md
    $ grep -c '[^[:space:]]' fuentes/scott_radical_candor/cap_09.md
      220

**Las 433 lineas del fichero llevan dentro 220 con contenido**; las otras separan parrafos. Y
**las 17508 palabras del fichero entero son 17482 de cuerpo mas 26 de la cabecera `yaml`**:
`17482 + 26 = 17508`.

### 2.2. Las cabeceras del capitulo, sacadas con instrumento y no a ojo

    $ grep -n '^[A-Z][A-Z0-9 ,"()-]*$' fuentes/scott_radical_candor/cap_09.md
      15:SOLICITING IMPROMPTU GUIDANCE
      55:ORANGE BOX
      65:MANAGEMENT "FIX-IT" WEEKS
      73:GIVING IMPROMPTU GUIDANCE
      179:GAUGE YOUR IMPROMPTU GUIDANCE, GET A BASELINE, TRACK YOUR IMPROVEMENTS
      205:BEING RADICALLY CANDID WITH YOUR BOSS
      223:GENDER AND GUIDANCE
      331:FORMAL PERFORMANCE REVIEWS
      363:PREVENT BACKSTABBING
      369:PEER GUIDANCE
      383:SPEAKING TRUTH TO "POWER"
      433:TEAM
    $ (el mismo patron) | wc -l
      12

**De esas 12 cabeceras, 11 son del capitulo y la 12 (`TEAM`, L433) es el titulo del capitulo
siguiente que el recorte arrastra.** Esa cuenta es el esqueleto de mi frontera.

### 2.3. La bandeja, entera y por capitulo

    $ ls cuarentena/scott_radical_candor/*.json | wc -l
      78

**El reparto de esos 78 candidatos de la bandeja de `scott_radical_candor`, por la unidad de
origen que cada uno declara en su propio `resumen_teorico`:**

    cap_01:   1 candidatos,    9 pasos
    cap_03:   1 candidatos,    7 pasos
    cap_04:   5 candidatos,   41 pasos
    cap_05:   8 candidatos,   76 pasos
    cap_06:  10 candidatos,  117 pasos
    cap_07:  25 candidatos,  225 pasos
    cap_08:  12 candidatos,  102 pasos
    cap_09:  15 candidatos,  177 pasos
    SIN  :   1 candidatos,    7 pasos
    TOTAL: 78 candidatos, 761 pasos

**LAS FILAS SUMAN EL TOTAL AL DIGITO:** `1+1+5+8+10+25+12+15+1 = 78` candidatos y
`9+7+41+76+117+225+102+177+7 = 761` pasos.

**LOS DE `cap_09` SON 15, Y LOS 15 SUMAN 177 PASOS.** Esa es la poblacion que clasifico.

---

## 3. MI FRONTERA CIEGA DE `cap_09`, CERRADA CONTRA EL CUERPO

**Esta es mi lectura del capitulo, pieza por pieza, hecha antes de cruzarla con nada.** La
columna `DA` dice si esa pieza da nodo, y la de la derecha por que. **Las 28 filas cubren las
lineas 8 a 433 sin un hueco y sin un solape** (la salida esta en `0.bis`, orden 1).

| lineas | DA | mi lectura |
|---|---|---|
| `L8-13` | no | cabecera del capitulo, subtitulo y entrada: dice de que va, no manda hacer nada |
| `L15` | no | rotulo de seccion `SOLICITING IMPROMPTU GUIDANCE`, sin cuerpo propio |
| `L17-53` | **SI** | `Embrace the discomfort` entera: seis consejos rotulados uno a uno, de la excepcion a criticar en privado hasta medir la guia que recibes |
| `L55-63` | **SI** | `ORANGE BOX`: organizar un sistema para sugerencias y quejas, con la mecanica de la caja de Dearing |
| `L65-71` | **SI** | `MANAGEMENT FIX-IT WEEKS`: el registro publico de averias de gestion, el voto, el reparto y la semana |
| `L73-75` | no | rotulo `GIVING IMPROMPTU GUIDANCE` mas su preambulo: dice por que va segundo, no trae acto |
| `L77-95` | **SI** | `Be humble`, con situacion comportamiento impacto, la columna de la izquierda y la humildad ontologica |
| `L97-113` | **SI** | `Be helpful`: declarar la intencion, mostrar en vez de contar, buscar la ayuda, la guia como regalo |
| `L115-135` | **SI** | `Give feedback immediately`: los dos o tres minutos, la holgura, el no guardarlo y los agujeros negros |
| `L137-153` | **SI** | `In person`: la jerarquia de modos, el Reply All y la oficina remota |
| `L155-163` | **SI** | `Praise in public, criticize in private`, con sus tres matices |
| `L165-177` | **SI** | `Don't personalize`: el error fundamental de atribucion y la frase que se retira |
| `L179-203` | **SI** | `GAUGE YOUR IMPROMPTU GUIDANCE`: el marco junto a la mesa y las pegatinas de dos colores |
| `L205-221` | **SI** | `BEING RADICALLY CANDID WITH YOUR BOSS`: la cautela, el permiso y Listen Challenge Commit |
| `L223-225` | no | rotulo `GENDER AND GUIDANCE` y su entrada: declara el alcance del apartado, sin acto |
| `L227-249` | no | por que es mas dificil para hombres que dirigen mujeres: diagnostico e historias. Su unico imperativo lo ejecuta `L291-293` |
| `L251-283` | no | la trampa de la abrasividad: diagnostico, datos y el caso de Jessica y Steve. No manda hacer nada |
| `L285-289` | no | `What can you do`, entrada de las cuatro piezas que siguen |
| `L291-293` | **SI** | `Men: don't pull punches with women`: preguntarselo a ella, explicar el marco, pedirle que mida |
| `L295-299` | **SI** | `Women: demand criticism`: las tres frases, la pausa, contar hasta seis |
| `L301-313` | **SI** | `Men and women`, cuando te parece que una mujer es demasiado agresiva: cambiar de genero, ser mas concreto, no usar lenguaje de genero, no decir nunca *se mas agradable* |
| `L315-329` | **SI** | si eres una mujer a la que le dicen abrasiva: las cuatro reglas generales, mas no descartar a los hombres |
| `L331-361` | **SI** | `FORMAL PERFORMANCE REVIEWS`: nueve consejos rotulados para entregar una evaluacion formal |
| `L363-367` | **SI** | `PREVENT BACKSTABBING`: no escuchar a nadie hablar de un tercero, y la conversacion a tres en vivo |
| `L369-381` | **SI** | `PEER GUIDANCE`: la ballena y la metedura de pata, y la medicion entre pares |
| `L383-425` | **SI** | `SPEAKING TRUTH TO POWER`: las reuniones de nivel salteado, sus diez reglas y sus cinco preguntas frecuentes |
| `L427-429` | no | cierre del capitulo, las dos preguntas de vuelta a los principios: postura |
| `L431-433` | no | marcador del capitulo siguiente, el `7.` y `TEAM` |

**EL CRITERIO CON EL QUE PUSE `no` EN NUEVE FILAS, dicho una vez:** una pieza da nodo cuando
trae **actos propios** (`D.27`); no lo da cuando es rotulo, entrada, diagnostico o cierre.

**LAS DOS FILAS MAS DISCUTIBLES DE MI PROPIA TABLA SON `L227-249` Y `L251-283`**, las dos
mitades del diagnostico de genero: **son 23 y 33 lineas de analisis, datos y casos, y el unico
imperativo que hay en las dos** (*no te contengas al criticar a las mujeres de tu equipo*,
L231) **lo ejecuta entera la pieza `L291-293`, que si da nodo.** Si alguien las cuenta como
piezas que dan nodo, mi 19 sube a 21: **lo dejo dicho aqui, con sus lineas, para que la
discrepancia se pueda adjudicar en vez de discutir.**

---

## 4. MI CLASIFICACION DE LOS 15 CANDIDATOS DE `cap_09`

**Abri los 15, uno por uno, con sus `pasos_accionables` enteros delante, y los cruce contra
las lineas del fuente que cada uno declara.** Mi clase sale de la vara de `AUDITOR_FORJA.md`
6.1 y de `D.27` y `D.30`.

| # | candidato | lineas | pasos | MI CLASE |
|---:|---|---|---:|---|
| 1 | `abrazar_incomodidad_arrancar_critica_equipo` | `L17-53` | 20 | **PROCEDIMIENTO FIEL**, con una reserva de frontera en `4.2` |
| 2 | `organizar_sistema_recoger_quejas_equipo` | `L55-63` | 9 | **PROCEDIMIENTO FIEL** |
| 3 | `correr_semana_arreglo_averias_gestion` | `L65-71` | 8 | **PROCEDIMIENTO FIEL** |
| 4 | `dar_guia_humilde_tres_tecnicas` | `L77-95` | 15 | **PROCEDIMIENTO FIEL** |
| 5 | `dar_guia_util_cuatro_recordatorios` | `L97-113` | 10 | **PROCEDIMIENTO FIEL** |
| 6 | `dar_guia_acto_cinco_consejos` | `L115-135` | 14 | **PROCEDIMIENTO FIEL** |
| 7 | `elegir_medio_dar_guia_jerarquia_modos` | `L137-153` | 13 | **PROCEDIMIENTO FIEL** |
| 8 | `elogiar_publico_criticar_privado_sus_tres_matices` | `L155-163` | 9 | **PROCEDIMIENTO FIEL** |
| 9 | `evitar_personalizar_guia_aceptar_personal` | `L165-177` | 12 | **PROCEDIMIENTO FIEL**, y es el unico con un par que hay que leer (`6.4`) |
| 10 | `medir_guia_propia_pegatinas_marco` | `L179-203` | 13 | **PROCEDIMIENTO FIEL** |
| 11 | `practicar_franqueza_radical_jefe_propio` | `L205-221` | 17 | **PROCEDIMIENTO FIEL** |
| 12 | `comprobar_criticas_hombre_mujeres_equipo` | `L291-293` | 6 | **PROCEDIMIENTO FIEL** |
| 13 | `exigir_critica_jefe_reticente` | `L295-299` | 9 | **PROCEDIMIENTO FIEL** |
| 14 | `impedir_punialadas_espalda_equipo` | `L363-367` | 9 | **PROCEDIMIENTO FIEL** |
| 15 | `fomentar_guia_reciproca_companieros` | `L369-381` | 13 | **PROCEDIMIENTO FIEL** |

**CERO que yo lea como POSTURA, CERO que yo lea como PUENTE y CERO que yo lea como REPITE.**
La lectura de fidelidad que sostiene ese *cero puentes* esta en la seccion `7`, con su muestra
y su instrumento: **no es una impresion.**

### 4.1. **EL CRUCE UNO A UNO: mis 19 piezas que dan nodo contra sus 15 candidatos**

**Corrido por instrumento y no casado a ojo:** cada candidato se cruza con la pieza cuyo rango
de lineas solapa el suyo.

    piezas DA NODO con candidato   : 15
    piezas DA NODO SIN candidato   : 4
    candidatos de cap_09 en bandeja: 15
    candidatos que no casan con ninguna pieza mia: ninguno

**ES UN UNO A UNO PERFECTO EN LAS 15**, y cada candidato cae en una pieza distinta de mi
frontera: **ninguno se solapa con otro, ninguno cae fuera de mi lectura, y ninguna pieza
recibio dos.** **Mi frontera y la suya coinciden donde hay candidato, y discrepan en 4 de las
19 piezas mias que dan nodo**, que son las que no lo tienen (seccion `5`).

### 4.2. **LA UNICA RESERVA DE FRONTERA QUE PONGO, y la mido en vez de opinar**

**`abrazar_incomodidad_arrancar_critica_equipo` se come `L17-53` entera**, que son **seis
consejos rotulados uno a uno por el libro** (la excepcion a criticar en privado, la pregunta
de cabecera, abrazar la incomodidad, escuchar para entender, premiar la critica y medir la que
recibes). **En el resto del capitulo el corte es un nodo por subseccion rotulada.**

**LA MEDIDA, que es lo que convierte esto en algo adjudicable:** palabras de la pieza
divididas por pasos del candidato.

    L17-53    2178 palabras,  20 pasos  ->  108.9 palabras por paso   <- el maximo de los 15
    L179-203  1164 palabras,  13 pasos  ->   89.5
    L115-135  1144 palabras,  14 pasos  ->   81.7
    ...
    L295-299   129 palabras,   9 pasos  ->   14.3                     <- el minimo de los 15
    SUMA     10669 palabras, 177 pasos  ->   60.3 de media de los 15

**`L17-53` comprime casi el doble que la media de los 15 candidatos (108.9 contra 60.3) y casi
ocho veces mas que el minimo de los 15 (108.9 contra 14.3).** No digo que este mal: **digo que
es el unico sitio del capitulo donde el corte no sigue el rotulo del libro**, y que si la vara
de `6.1` se aplica a esos seis consejos, **tres de ellos traen procedimiento propio
suficiente** (la pregunta de cabecera, L37; premiar la critica, L49 a L51; medir la que
recibes, L53). **Lo subo como discutible mio, no como caida.**

---

## 5. LAS CUATRO PIEZAS QUE DAN NODO Y **NO TIENEN CANDIDATO**

**ESTE ES EL HALLAZGO DE MI LECTURA CIEGA.** De mis 19 piezas que dan nodo, **4 no tienen ni
un candidato en la bandeja entera de 78 de `scott_radical_candor`**, no solo entre los 15 de
esta vuelta.

| lineas | que es | palabras | la busqueda que lo sostiene |
|---|---|---:|---|
| `L301-313` | *Men and women: things to think about when you feel a woman is being too aggressive*: **cuatro tacticas rotuladas** (cambiar de genero, ser mas concreto, no usar lenguaje de genero, no decir nunca *se mas agradable*) | 416 | `grep -ril "cambiar de genero\|switch gender\|si fuera un hombre" cuarentena/scott_radical_candor/*.json` da **0 de 78** |
| `L315-329` | *Things to think about if you're a woman who's being told you're abrasive*: **cuatro reglas generales** mas *no descartes a los hombres* | 573 | `grep -ril "abrasiv" cuarentena/scott_radical_candor/*.json` da **0 de 78**, y `grep -ic "abrasiv" dataset/nodos.jsonl` da **0 de 203** |
| `L331-361` | **`FORMAL PERFORMANCE REVIEWS`**, seccion entera en versales: **nueve consejos rotulados** para entregar una evaluacion formal (sin sorpresas, no fiarse del juicio unilateral, pedirte una a ti primero, escribirla, cuando entregarla, cincuenta minutos y no seguidas, mitad atras mitad adelante, revisiones periodicas, la nota y el sueldo despues) | 1526 | `grep -ril "evaluacion de desempenio\|evaluacion formal\|performance review\|revision formal" cuarentena/scott_radical_candor/*.json` da **1 de 78**, y ese 1 es `dar_guia_acto_cinco_consejos`, que la nombra **para decir que NO guardes la guia para ella** (su `P10`, de L129). **No la extrae: la cita como contraejemplo.** Sin el primer termino del patron, el mismo `grep` da **0 de 78**: ver `5.3` |
| `L383-425` | **`SPEAKING TRUTH TO "POWER"`**, seccion entera en versales: las reuniones de nivel salteado, **diez reglas rotuladas** mas **cinco preguntas frecuentes** | 1818 | `grep -ril "salto de nivel\|skip level\|nivel salteado" cuarentena/scott_radical_candor/*.json` da **0 de 78**, y en `dataset/nodos.jsonl` da **0 de 203** |

**LA BUSQUEDA NEGATIVA NO SE CITA SIN CORRERLA** (`AUDITOR_FORJA.md` 1.1), y las cuatro estan
corridas en esta vuelta contra **la bandeja de 78 y el grafo de 203.**

### 5.3. **UNA CAIDA MIA CAZADA AL RE CORRER MIS PROPIOS COMANDOS ANTES DEL SELLO**

**ESCRIBI LA TABLA DE ARRIBA Y DESPUES VOLVI A CORRER LOS CUATRO `grep` TAL Y COMO LOS HABIA
CITADO, uno por uno.** El tercero **no reproducia su cifra**: yo habia citado el patron
`"evaluacion formal\|performance review\|revision formal"`, **que da 0 de 78**, y la cifra `1`
de la que hablaba el texto venia del patron que corri de verdad, **el que lleva ademas
`evaluacion de desempenio`**. La celda ya lleva el patron bueno y dice tambien lo que da el
corto.

**ES EXACTAMENTE LA CAIDA `7.1` DE LA `ACTA 18`, la que engendro la ORDEN 1:** *lo que fallo
no fue la ausencia de instrumento, sino que el instrumento no comprobaba lo que la cifra
decia.* **La diferencia es que esta vez se cazo antes del sello y no despues**, y se cazo
porque re correr los comandos citados fue un paso del trabajo y no una ocurrencia.

**NO ACUMULA, y digo por que:** `D.38.2` pone mi especie `CIFRA PUBLICADA PROPIA` en *mi acta
o mi apertura sellada*, **y esto no llego a sellarse con el patron malo.** **Lo declaro igual**,
porque una apertura que solo cuenta lo que le salio bien no mide nada.

### 5.1. Cuanto pesa eso, con su denominador

    EL REPARTO DEL CUERPO DE cap_09, sobre las 17482 palabras del cuerpo:
      piezas que dan nodo Y tienen candidato: 15 de las 28 piezas : 10669 palabras (61.03 por ciento)
      piezas que dan nodo y SIN candidato   :  4 de las 28 piezas :  4333 palabras (24.79 por ciento)
      piezas que NO dan nodo                :  9 de las 28 piezas :  2480 palabras (14.19 por ciento)
      15 + 4 + 9 = 28 piezas   y   10669 + 4333 + 2480 = 17482 palabras

> **CASI UNA CUARTA PARTE DEL CUERPO DE `cap_09`, 4333 palabras de las 17482, ES
> PROCEDIMIENTO QUE MI LECTURA DA POR EXTRAIBLE Y QUE NO TIENE CANDIDATO.**

### 5.2. Lo que esto **puede** ser, y por que no lo decido aqui

**LA LECTURA BENIGNA Y PROBABLE ES QUE SEA EL CIERRE CORTO POR TECHO DE CANDIDATOS**
(`EXTRACTOR.md` 12.4, `AUDITOR_FORJA.md` 8.1): **15 candidatos es exactamente el techo del
tramo**, la vuelta cierra ahi y lo declara, y lo que sobra pasa a la siguiente. **Mi cuenta
encaja con eso al digito: 15 candidatos escritos contra un techo de 15.**

**PERO HAY UNA DIFERENCIA QUE NO PUEDO RESOLVER A CIEGAS Y QUE DEJO PLANTEADA.** `12.4` esta
escrita para que **los CAPITULOS que le quedaban al tramo pasen a la vuelta siguiente**; aqui
lo que queda pendiente **no es un capitulo entero, es un trozo de este**, y dentro de ese
trozo hay **dos secciones en versales completas** de las 11 del capitulo. **Que se declare
`cap_09` cerrado sin decir que queda dentro de `cap_09` es lo unico que hay que comprobar**, y
`8.1` me dice exactamente que mirar: *una vuelta que cierra en un capitulo y no lo dice no
esta aplicando esta regla.*

**LO QUE VERIFICO EN MI TURNO NORMAL, ya escrito aqui para no inventarlo despues:**

1. **Que el reporte declare el cierre corto con su cifra** (15 candidatos contra el techo de 15).
2. **Que declare que `cap_09` queda ABIERTO y con que piezas dentro**, y no cerrado.
3. **Si dice `cap_09` cerrado, es caida de especie `REPORTE`**, y las cuatro piezas de arriba
   son su evidencia, con sus lineas y sus palabras.
4. **Y la comparacion de fronteras:** mis 28 piezas, 19 que dan nodo, contra las 30 piezas y
   20 que dan nodo del asunto de `0dcb431` que declaro en `1.2`.

---

## 6. EL BARRIDO DE VECINOS, SOBRE GRAFO MAS BANDEJAS (`D.38.4`)

### 6.1. La poblacion, con su `wc -l` pegado

    $ wc -l dataset/nodos.jsonl
      203 dataset/nodos.jsonl
    $ ls cuarentena/*/*.json | grep -v _insertados | grep -v _derivadas | wc -l
      241
      de esos 241: 163 del catalogo de control ensayo_referencia_163 y 78 de scott_radical_candor

**POBLACION `D.38.4` = 203 + 241 = 444.** Y sin el catalogo de control, `444 - 163 = 281`.
**Barro contra las 444**, que es la letra de la regla (*todo lo que espera en cuarentena*), y
doy la de 281 al lado porque la `ACTA 18` dio las dos y comparar lotes pide la misma vara.

**Y SE BARRE UNO POR VEZ, `444 - 1 = 443`**, por la correccion declarada que yo mismo escribi
en la `ACTA 18` y que esta en el banco bajo `D.38.4`: **un nodo no es vecino de si mismo**, y
la receta literal del banco, corrida al pie de la letra, devuelve cero vecinos porque la
guarda de id muerde primero.

### 6.2. La salida entera, sin recortar

    $ python .barrido_v20/barrer.py .barrido_v20/cap09_lf.txt
      POBLACION: grafo 203 + bandejas 241 = 444
      CANDIDATOS BARRIDOS: 15
      umbrales de esta corrida: similitud 0.35 | familia 0.30 | paso contra nodo 0.60

      ### abrazar_incomodidad_arrancar_critica_equipo   [poblacion 443]
          SIN VECINO

      ### comprobar_criticas_hombre_mujeres_equipo   [poblacion 443]
          VECINO exigir_critica_jefe_reticente  |  familia_id=0.125, paso_contra_nodo=0.555, similitud_texto=0.402
          VECINO correr_semana_arreglo_averias_gestion  |  paso_contra_nodo=0.431, similitud_texto=0.366

      ### correr_semana_arreglo_averias_gestion   [poblacion 443]
          VECINO comprobar_criticas_hombre_mujeres_equipo  |  paso_contra_nodo=0.431, similitud_texto=0.356

      ### dar_guia_acto_cinco_consejos   [poblacion 443]
          SIN VECINO

      ### dar_guia_humilde_tres_tecnicas   [poblacion 443]
          VECINO elogiar_publico_criticar_privado_sus_tres_matices  |  familia_id=0.091, paso_contra_nodo=0.393, similitud_texto=0.35

      ### dar_guia_util_cuatro_recordatorios   [poblacion 443]
          SIN VECINO

      ### elegir_medio_dar_guia_jerarquia_modos   [poblacion 443]
          SIN VECINO

      ### elogiar_publico_criticar_privado_sus_tres_matices   [poblacion 443]
          VECINO dar_guia_humilde_tres_tecnicas  |  familia_id=0.091, paso_contra_nodo=0.405, similitud_texto=0.352

      ### evitar_personalizar_guia_aceptar_personal   [poblacion 443]
          VECINO manejar_enfado_persona_desafiada  |  paso_contra_nodo=0.867, similitud_texto=0.234

      ### exigir_critica_jefe_reticente   [poblacion 443]
          VECINO comprobar_criticas_hombre_mujeres_equipo  |  familia_id=0.125, paso_contra_nodo=0.577, similitud_texto=0.382

      ### fomentar_guia_reciproca_companieros   [poblacion 443]
          SIN VECINO

      ### impedir_punialadas_espalda_equipo   [poblacion 443]
          SIN VECINO

      ### medir_guia_propia_pegatinas_marco   [poblacion 443]
          SIN VECINO

      ### organizar_sistema_recoger_quejas_equipo   [poblacion 443]
          VECINO elogiar_publico_criticar_privado_sus_tres_matices  |  paso_contra_nodo=0.47, similitud_texto=0.357

      ### practicar_franqueza_radical_jefe_propio   [poblacion 443]
          SIN VECINO

      TOTAL: 8 vecinos levantados sobre 15 candidatos; 7 candidatos con vecino, 8 sin ninguno

**EL INSTRUMENTO ES EL DE LA CASA**, `src.aduana.buscar_vecinos`, el mismo que usa
`forja.py informe` por dentro. Lo que hace mi script es **armarle la poblacion de `D.38.4` y
quitarle el propio candidato**, que es lo que la regla pide y la receta del banco no trae.

**CRUCE INDEPENDIENTE.** Corri una segunda pasada, en orden inverso y en otro proceso, para
ver si el resultado se reproduce. **Le dio tiempo a 2 de los 15 antes de que la parara, y los
2 coinciden al digito con la primera:**

    $ cat .barrido_v20/BARRIDO2.txt
      POBLACION: grafo 203 + bandejas 241 = 444
      ### practicar_franqueza_radical_jefe_propio   [poblacion 443]   [447s]
          SIN VECINO
      ### organizar_sistema_recoger_quejas_equipo   [poblacion 443]   [328s]
          VECINO elogiar_publico_criticar_privado_sus_tres_matices  |  paso_contra_nodo=0.47, similitud_texto=0.357

**2 de 15 comprobados dos veces no es el barrido entero comprobado dos veces, y lo digo asi.**
Los `447s` y `328s` de esa salida explican por que: **el barrido completo de los 15 contra 443
tardo 50 minutos y 14 segundos**, y una segunda pasada entera costaba otro tanto.

    $ (arranque del proceso)                          13:10:58
    $ stat -c '%y' .barrido_v20/BARRIDO.txt           2026-09-12 14:01:12

**Esa cifra tambien la remedi:** mientras esperaba lo llame *hora y media*, que era mi reloj de
espera y no el del proceso. **50 minutos, que es lo que dice el fichero.**

### 6.3. **LO QUE EL BARRIDO DICE, Y ES LA VINDICACION MEDIDA DE `D.38.4`**

    8 vecinos levantados sobre 15 candidatos; 7 candidatos con vecino, 8 sin ninguno

**LOS 8 VECINOS LEVANTADOS APUNTAN A 6 NODOS DISTINTOS** (tres pares se levantan por los dos
lados), **y esos 6 estan comprobados uno por uno contra el grafo y contra la bandeja:**

    exigir_critica_jefe_reticente                     : grafo=0 bandeja=1
    correr_semana_arreglo_averias_gestion             : grafo=0 bandeja=1
    comprobar_criticas_hombre_mujeres_equipo          : grafo=0 bandeja=1
    elogiar_publico_criticar_privado_sus_tres_matices : grafo=0 bandeja=1
    dar_guia_humilde_tres_tecnicas                    : grafo=0 bandeja=1
    manejar_enfado_persona_desafiada                  : grafo=0 bandeja=1

> **LOS 6 NODOS A LOS QUE APUNTAN LOS 8 VECINOS ESTAN LOS 6 EN LA BANDEJA. EN EL GRAFO DE
> 203 NODOS NO HAY NI UNO.**
> **Un barrido hecho solo sobre `dataset/nodos.jsonl`, que es justo lo que `D.38.4` vino a
> prohibir, habria publicado CERO VECINOS para los 15 candidatos de esta vuelta**, y habria
> perdido entero el unico par que hay que leer.

**Y DE LOS 8 VECINOS, SOLO 1 PASA EL UMBRAL DE `paso_contra_nodo`, que es 0.60:**

    evitar_personalizar_guia_aceptar_personal -> manejar_enfado_persona_desafiada   0.867
    los otros 7 de los 8, entre 0.393 y 0.577, levantados por similitud_texto rozando su 0.35

**Los siete de abajo los leo como ruido de vocabulario:** son candidatos del mismo capitulo
hablando del mismo par de palabras (elogio y critica), con `similitud_texto` entre 0.350 y
0.402 sobre un umbral de 0.350. **`D.19` manda: ninguna senial separa jerarquia de ruido, asi
que la senial dice donde mirar y ahi acaba su trabajo.** Mire los siete y ninguno es par.

### 6.4. **EL UNICO PAR DE VERDAD, ADJUDICADO LEYENDO LOS PASOS**

**`evitar_personalizar_guia_aceptar_personal`** (`cap_09`, `L165-177`, 12 pasos) **contra**
**`manejar_enfado_persona_desafiada`** (`cap_04`, 7 pasos, tambien en la bandeja).
`paso_contra_nodo = 0.867`, muy por encima del 0.60.

**EL SOLAPE ES REAL Y ES UNO SOLO.** Los dos traen la misma orden, porque el libro la repite
en dos capitulos distintos:

    manejar_enfado  P5: Elimina de tu vocabulario la frase no te lo tomes como algo
                        personal. El texto dice que es insultante.
    evitar_person   P9: Elimina de tu vocabulario la frase no te lo tomes como algo
                        personal, que el texto llama peor que inutil.

**MI ADJUDICACION: `CONTINUA`, NO `REPITE`. Los dos se quedan, y lo que hay entre ellos es una
arista.** La vara de `6.1` se aplica asi, con direccion y sin bascula:

| la pregunta de `6.1` | la respuesta, leida en los pasos |
|---|---|
| **que anade el hijo a la madre** | el error fundamental de atribucion con su autor (`P2`, `P3`), pillarse el *tu eres* (`P4`), remitir a situacion comportamiento impacto y a la columna de la izquierda (`P5`), *eso esta mal* en vez de *tu estas mal* (`P6`, `P7`), mantener la discusion sobre el asunto (`P8`), y como no personalizar cuando la cosa SI es personal (`P12`). **Once pasos de sus doce que la madre no tiene** |
| **que queda fuera en el otro lado** | la madre es un procedimiento para **el enfado del otro despues de haberle desafiado**: reconocer el dolor sin fingir que no duele, ofrecerse a ayudar, no fingir que no hay problema. **Seis pasos de sus siete que el hijo no tiene** |
| **la bascula** | no decide. Lo que decide es que **lo que queda fuera es procedimiento en los dos lados**, que es la letra exacta de `6.1` |
| **de que tamano es el solape** | **uno de doce contra uno de siete.** Un solo paso compartido, de literal casi identico, no es un nodo repetido: es el libro insistiendo, y `D.30` manda transcribir lo que el libro dice donde lo dice |

**LA SENIAL ACERTO EN MANDARME A LEER Y SE EQUIVOCARIA EN DECIDIR**, que es exactamente lo que
`D.19` dice que pasa. **Lo dejo adjudicado aqui, a ciegas y antes de ver que dijo el
extractor**, que es lo unico que hace informativa a la comparacion (`5.1`).

---

## 7. MI RELECTURA DE FIDELIDAD (`D.30`): busque puentes y no encontre ninguno

**`AUDITOR_FORJA.md` 8.3 me obliga a contar yo los pasos y a releer una muestra de los
marcados TRANSCRIPCION contra su parrafo**, porque *el error que esta metrica invita a cometer
es marcar un puente como transcripcion.*

**LOS PASOS LOS CONTE YO** y son los de la seccion `2.3`: **15 candidatos, 177 pasos.**

**Y LA MUESTRA NO LA ELEGI A OJO: la eligio un instrumento, y es la muestra que mas duele si
hay puente.** Saque **todas las cifras que aparecen dentro de esos 177 pasos** (un puente casi
siempre entra como un numero que el libro no dice) y las cotejé una por una contra su linea:

    $ (extractor de cifras sobre los pasos de los 15 candidatos de cap_09)
      TOTAL de cifras dentro de pasos de los 15 candidatos de cap_09: 54

**COTEJE LAS 54 CONTRA EL FUENTE. LAS 54 ESTAN EN EL TEXTO.** Las que mas facil habria sido
inventar, con su linea:

| cifra del paso | donde la dice el libro |
|---|---|
| *mas de sesenta personas* (`abrazar` `P5`) | L33, *more than sixty or so people* |
| *cuenta hasta seis* (`abrazar` `P9`, `exigir` `P6`) | L41 y L299, *count to six* |
| *cinco personas, tres elogios, una critica, sesenta minutos* (`dar_guia_acto` `P7`) | L125, las cuatro en la misma frase |
| *veinticinco y cincuenta, en vez de treinta y sesenta* (`dar_guia_acto` `P8`) | L127, *twenty-five- and fifty-minute meetings ... not thirty- and sixty-minute* |
| *diapositiva seis* y *cinco por ciento* (`elogiar_publico` `P4`) | L159, los dos ejemplares literales |
| *quince segundos* (`medir_guia` `P1`) | L181, *it can take fifteen seconds* |
| *veinte dolares* (`fomentar_guia` `P9`) | L373, *I put twenty dollars on Whoops's head* |
| *tres anios* (`dar_guia_humilde` `P14`) | L95, *funny in a three-year-old* |
| *llamada de tres minutos* (`elegir_medio` `P13`) | L153, *a three-minute check-in call* |

**MI LECTURA: 177 pasos, 177 TRANSCRIPCION, 0 PUENTE.** Es la misma cifra que los propios
candidatos declaran en su `resumen_teorico`, **y la publico como mia porque la comprobe yo
contra el fuente, no porque ellos la digan** (`8.3`: *es una cifra que el extractor te da y
que tu firmas; no la copias*).

**LO QUE ESO SIGNIFICA PARA `PASOS INVENTADOS POR CAPITULO` (seccion 8):**

    cap_09:  0 pasos inventados / 177 pasos escritos  =  0,00 por ciento

**Cero esta por debajo del tope de 10 por ciento**, asi que **por esta metrica el tramo no
baja.** El otro techo, el de candidatos, es el que manda aqui, y es el de `5.2`.

### 7.1. Lo unico que si me chirria de los 177 pasos, y no es un puente

**Muchos pasos empiezan por `Cuenta con lo que el texto dice...`**, que es contexto y no un
acto. **No es puente** (lo que viene detras esta en el libro, palabra por palabra) **y no es
cifra falsa.** Es una decision de estilo que atraviesa la bandeja entera y no solo estos 15, y
la mido en vez de decir *muchos*:

    candidatos con al menos un paso que empieza por "Cuenta con", por capitulo de origen:
       cap_01:  1 de  1      cap_06: 10 de 10
       cap_03:  1 de  1      cap_07: 21 de 25
       cap_04:  3 de  5      cap_08: 11 de 12
       cap_05:  7 de  8      cap_09: 13 de 15
       SIN   :  1 de  1
       TOTAL : 68 de los 78 candidatos de la bandeja de scott_radical_candor

**13 de los 15 de esta vuelta y 68 de los 78 de la bandeja**: no es un tic de `cap_09`. **Lo dejo anotado y no lo convierto en caida:** cambiar eso estrecharia la
vara, y `6.3` dice que ninguna vuelta la mueve sin correccion declarada de Alexis. **Lo digo
aqui para que exista, no para cobrarlo.**

---

## 8. LO QUE NO PUEDO COMPROBAR EN ESTA FASE, DICHO EN VEZ DE CALLADO

| lo que falta | por que | cuando |
|---|---|---|
| las cinco guardas y la aduana por mutacion | `5.5` las manda re correr sobre **lo que el reporte declare mordiendo**, y el reporte no esta en el arbol | turno normal |
| el cierre corto declarado con su cifra | vive en `REPORTE.md` | turno normal, con la lista de `5.2` ya escrita |
| la comparacion de fronteras, 28 mias contra 30 suyas | igual | turno normal |
| `python forja.py gate`, `resolutor` y `tests/test_aceptacion.py` | no son de la fase ciega: esta fase clasifica material, no verifica la vuelta | turno normal |
| el sello de este fichero | lo pone el arnes cuando yo termine | al cerrar |

---

## 9. TABLA DE CIERRE DE LA APERTURA

**Repito aqui la declaracion de herencia. `D.40` mira PRESENCIA y no conteo** (parada del 12
sep 2026, punto 1: *basta con que UNA de las veces que aparece la declaracion este bien
puesta*), **asi que citar la linea que declaro no me tumba la vuelta**, y una apertura que
declara arriba y lo repite al cerrar es mas facil de leer que una que lo dice una sola vez.

    ACTA ANTERIOR LEIDA: 80fd74cdf15bb0b1ff02bcbe560ba03f11f22472
    HEREDADO 1: CUMPLIDO

| lo que esta fase tenia que traer | donde esta |
|---|---|
| la herencia declarada y remedida | `0` |
| mi tarea bloqueante de la `ACTA 18` `7.5`, sus tres ordenes | `0.bis`: dos cumplidas y una declarada imposible en la letra |
| la contaminacion propia | `1.2`, y la apertura anterior no abierta en `1.3` |
| clases y lecturas, con instrumento en cada cifra (`D.38.3`) | `2` a `7` |
| la frontera cerrada contra el cuerpo | `3` y `0.bis`: `17482 = 17482`, 0 huecos, 0 solapes |
| mi clase para cada uno de los 15 candidatos | `4` |
| el barrido sobre grafo mas bandejas (`D.38.4`) | `6`: `444 = 203 + 241`, y `443` por candidato |
| el par leido y adjudicado a ciegas | `6.4` |
| la lectura de fidelidad propia | `7`: 177 de 177 TRANSCRIPCION, 0 PUENTE |

### **LO QUE ESTA APERTURA SOSTIENE, EN UNA LINEA**

**Los 15 candidatos de `cap_09` los leo los 15 como procedimiento fiel al libro, con un solo
par que leer y adjudicado `CONTINUA`. Y el hallazgo de esta fase ciega no esta en lo que se
escribio, sino en lo que no: 4 de mis 19 piezas que dan nodo, 4333 palabras de las 17482 del
cuerpo, casi una cuarta parte del capitulo, sin un candidato en toda la bandeja.**
