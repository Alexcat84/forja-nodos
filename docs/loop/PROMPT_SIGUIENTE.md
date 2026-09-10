# ENCARGO DE LA VUELTA 5. Lote 2, `smart_who`: `cap_03` y `cap_04`

*Escrito por el **auditor** el 10 sep 2026 al cerrar el ACTA 4, que es su sede
(`AUDITOR_FORJA.md` 5.6). El ACTA 4 verifico la vuelta 4, **adjudico los seis
discutibles y las tres propuestas**, y **no hubo parada**.*

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO, Y NO ES UNA TAREA: LAS TRES COMPROBACIONES DE APERTURA

**Una condicion medida es la que mediste tu.** Las corres antes de leer una linea de
libro, y **su resultado va en el reporte como su propia fila, antes de la TAREA 1**
(es la propuesta que el ACTA 3 adjudico a favor y que la vuelta 4 ya cumplio):

    ls fuentes/smart_who/                       tiene que dar cap_01.md a cap_07.md
    python -c "import json,io; print('smart_who' in json.load(io.open('fuentes/FUENTES_CANONICAS.json',encoding='utf-8')))"
    head -8 fuentes/smart_who/cap_03.md         la cabecera del capitulo que abres hoy

**El auditor las midio hoy y las tres estan en verde.** `cap_03.md` declara
`unidad: Cap. 2` y `titulo_textual: Scorecard: A Blueprint for Success`. **Si tu las
mides en rojo, manda tu medida y paras.**

---

## EL ESTADO CONTRA EL QUE ABRES, MEDIDO POR EL AUDITOR EN `6e2946a`

| medida | cifra |
|---|---:|
| nodos vivos en el dataset | **8** |
| pasos vigentes en el grafo | **43** |
| aristas declaradas | **2 relaciones**, 4 extremos |
| veredictos en bitacora | **2**, los dos CONTINUA |
| **candidatos en `cuarentena/smart_who/`** | **2**, los dos ENTRARIAN, **cero insertados** |
| fuentes canonicas registradas / en uso | **13** (12 libros mas `_lea_esto`) / **2** |
| capitulos del lote 2 leidos | **2 de 7**. Quedan **39.500 palabras, el 89,1 por ciento** |

**Mide tu la apertura igual, antes de la primera operacion, y si discrepas de esta
tabla manda tu medicion y declara la discrepancia.**

---

## TAREA 1. LOS REGISTROS DEL ACTA 4

*Va primero porque un registro que no se escribe en la vuelta siguiente se pierde.
**No toca ningun dato del grafo**, y ninguna pide maquinaria.*

### 1.a. LA CORRECCION DECLARADA, sin borrar el texto viejo

Anotala **al lado** de la seccion 3.c del `REPORTE.md` de la vuelta 4, sin tocarle
una palabra al bloque original:

> **CORRECCION DECLARADA (auditor, ACTA 4 seccion 4.1, 10 sep 2026).** El bloque de
> 3.c publica `similitud_texto 0.126` (c2 contra c1) y `0.117` (c1 contra c2).
> **Esas dos cifras son del candidato ANTES de corregir el puente del paso 11.**
> Sobre el fichero que viaja en `6e2946a`, `src.aduana.medir` da **0,123** y
> **0,114**. **Las otras cuatro cifras del bloque (`familia_id` 0,333 en los dos
> sentidos, `paso_contra_nodo` 0,405 y 0,409) reproducen exactas, y la conclusion
> entera se sostiene:** el auditor verifico por mutacion con su control que el
> segundo candidato **bloquea por `familia_id` en cuanto entre el primero**.

### 1.b. LA ESPECIE NUEVA DE PUENTE, al banco

**`D.30` tiene tres especies escritas y esta casa acaba de medir la cuarta.**
Registrala **con su ejemplar pegado**, que es lo que impide que una especie se
estreche sola:

> **EL PUENTE DE LA CONCLUSION.** Las tres viejas (destinatario, periodo,
> responsable) son **cosas que el libro no nombra** y se cazan por ausencia. Esta no:
> **el libro habla, deja la duda abierta, y el paso la cierra.**
>
>     smart_who/cap_02.md L81 : "The answer sounds nice, but we question how many
>                                people would actually do those things."
>                                (dos frases antes: "Maybe. Then again, maybe not.")
>     lo escrito              : "La respuesta suena bien y por eso no dice nada."
>
> **Es la mas peligrosa de las cuatro porque no se detecta por ausencia: el parrafo
> esta ahi, dice casi eso, y la comprobacion superficial da verde.** Se caza leyendo
> **si el libro cerro la frase o la dejo abierta.**

### 1.c. LAS NUEVE ADJUDICACIONES DEL AUDITOR

**Las nueve se resolvieron con reglas escritas y ninguna pidio doctrina nueva.**
Registralas donde el banco registra las adjudicaciones del auditor, **con su cita**:

| # | lo adjudicado | con que regla |
|---:|---|---|
| 1 | **no parar con el `cap_01` en cero fue correcto.** La parada es POR VUELTA | precedente publicado del `cap_03` del lote 1 (`CIERRE_LOTE_1.md` 3.1) mas la clausula *no paras por un capitulo de pocos nodos* |
| 2 | **el parrafo 20 del `cap_01` fuera**, por DOS caminos | vara madre (*nombrar no es procedimentar*) **y** manual lineas 81 y 82: **seria la segunda compresion de la misma numeracion** |
| 3 | **la arista de L53 NO se cablea.** **La arista es de DESPLIEGUE, no de calendario** | `esquema/nodo.schema.json` (*madre e hijo, secuencia dirigida*), `EXTRACTOR.md` 11 y `D.29`. La precedencia ya vive en `condiciones_activacion` y en el paso 12 |
| 4 | **la definicion del jugador A fuera** | `EXTRACTOR.md` 9: *una definicion sin nada que hacer*. **Y el criterio: si el `entregable_esperado` hay que inventarlo, no habia procedimiento** |
| 5 | **el puente corregido SE CUENTA** | `AUDITOR_FORJA.md` 8.4 mas la comparabilidad: la linea base del 36,11 son **pasos ESCRITOS**, y los 13 del lote 1 tambien se corrigieron |
| 6 | **un nodo de los diez metodos de vudu, no once** | manual lineas 81 y 82 (*un nodo por PASO*) mas manual 4 (*una advertencia es linea*). **Y es LA UNICA compresion permitida de esa numeracion** |
| 7 | **el puente de la conclusion entra en `D.30`** como cuarta especie | es un CASO añadido a un catalogo, no una frontera movida |
| 8 | **el disparador del tramo NO se lee en los dos sentidos** | `EXTRACTOR.md` 12.4: *la cifra no es sagrada; el disparador si*. **El volumen ya tiene su escalera, que es la cifra de puentes** |
| 9 | **una vineta es un BLOQUE y se cuenta como tal** | y si una frontera prefiere plegarla en su parrafo introductor, **la fila lo dice y el total lleva las dos cifras** |

### 1.d. LAS DOS ARISTAS PENDIENTES, que llevas contigo toda la campaña

**`D.29`: una arista que solo vive en la prosa de un reporte se pierde.** Estas dos
van en **un bloque propio y titulado** de tu reporte, esta vuelta y todas las que
sigan hasta que se resuelvan:

1. **`aplicar_metodo_ghsmart_contratacion` es CABEZA de serie y espera cuatro
   hijos**: `cap_03` (Scorecard), `cap_04` (Source), `cap_05` (Select) y `cap_06`
   (Sell). **Esta vuelta le trae los DOS primeros.** No se cablea todavia: **una
   arista se cablea contra ids que ya viven**, y la cabeza sigue en cuarentena.
2. **`detectar_metodos_vudu_contratacion` va antes en el tiempo por L53, y NO SE
   CABLEA NUNCA.** Adjudicado: la arista es de despliegue, no de calendario.

---

## TAREA 2. EL `cap_03` ENTERO (*Cap. 2*, `Scorecard: A Blueprint for Success`)

**LA UNIDAD ATOMICA ES EL CAPITULO.** Frontera del `cap_03`, candidatos del
`cap_03`, relectura de fidelidad del `cap_03`, informe del `cap_03`, **commit del
`cap_03`**. Y solo entonces el `cap_04`. **Nunca los dos juntos.**

**1. LA FRONTERA, PUBLICADA ANTES DE CORTAR.** Que hay dentro, que es procedimiento
y que no, con la prueba del inventario (`D.27`) y sus tres restricciones, y el saldo:
cuantos procedimientos y cuantas posturas. **Con la columna de linea del propio
fichero**, como hiciste en la vuelta 4: eso es lo que hizo tu frontera auditable.

**2. LOS CANDIDATOS, CON EL CICLO DE CINCO PASOS**, sin cambiar ni el orden ni una
pieza:

    1. escribes el candidato en cuarentena/smart_who/<id_propuesto>.json
    2. RELECTURA DE FIDELIDAD, con el parrafo delante:
         marcas cada paso como TRANSCRIPCION o como PUENTE
         cada PUENTE se retira o se reescribe, citando el parrafo que NO lo dice
    3. python forja.py informe cuarentena/smart_who/<id>.json
    4. si CAERIA, lo corriges y vuelves al 3
    5. solo entonces cuenta como escrito

**EL PASO 2 VA ANTES QUE EL 3 Y NO ES INTERCAMBIABLE.** La aduana no tiene el libro
delante.

**3. EL INFORME Y EL COMMIT:** `python forja.py informe --carpeta cuarentena/smart_who`,
pegas el saldo entero, y commiteas el capitulo con los JSON dentro. El mensaje dice
que capitulo y cuantos candidatos.

### LO QUE ESTE CAPITULO TIENE DE ESPECIAL, y conviene saberlo antes

**ES EL PRIMER HIJO DE LA CABEZA.** Scorecard es el paso 1 de los cuatro que
`aplicar_metodo_ghsmart_contratacion` comprime. **Ese nodo es la UNICA compresion
permitida de esa numeracion**, asi que lo que salga del `cap_03` **es su hijo, no
otra compresion**: un procedimiento propio con sus pasos, no un resumen de los
cuatro pasos otra vez.

**Y ES EL CAPITULO DONDE LA CIFRA DE PUENTES SE JUEGA DE VERDAD.** El `cap_02` era
rico en inventario (dos mandatos con sus listas, diez y cuatro). **Un capitulo que
enseña a escribir un documento puede ser mucho mas delgado en inventario y mucho mas
grueso en prosa**, y `D.30` dice donde salen los puentes: *un parrafo pobre no
produce un nodo pobre, produce un nodo inventado.* **Cuando el inventario del libro
sea delgado, desconfia de tus propios pasos.**

---

## TAREA 3. EL `cap_04` ENTERO (*Cap. 3*, `Source: Generating a Flow of A Players`)

**Las mismas tres partes, enteras y por separado**, y solo si el `cap_03` quedo
cerrado con su commit dentro.

**EL AVISO DE VOLUMEN, CON SU CIFRA DELANTE Y NO COMO ADORNO:**

    cap_03   10.696 palabras      casi TRES VECES el cap_02
    cap_04    6.441 palabras
    la vuelta 17.137 palabras     TRES VECES Y MEDIA las 4.824 de la vuelta 4

**La vuelta 4 gasto 11 minutos y medio en las 3.863 palabras del `cap_02`.** No es
una prediccion, es la unica cifra que hay.

> **SI EL `cap_03` SE COME LA VUELTA, LO CIERRAS ENTERO Y PARAS AHI.** Reporte
> parcial, nunca vacio, diciendo donde te quedaste. **Un capitulo cerrado vale mas
> que dos a medias**, y la razon no es comodidad: **la cifra que esta vuelta existe
> para medir es POR CAPITULO**, y dos capitulos leidos a medias no dejan ni una fila
> honesta.

**Y SI EL `cap_03` SOLO YA LLENA EL TRAMO** (entre cinco y quince candidatos), **el
`cap_04` no se empieza**. Eso no es un fallo: es el tramo funcionando.

---

## TAREA 4. LAS CUATRO MEDIDAS DEL CIERRE, DESGLOSADAS POR CAPITULO

**Las dos primeras con una fila por capitulo**, y todas **recomputadas al cierre**:

| medida | como la das |
|---|---|
| **candidatos por mil palabras** | una fila por capitulo, mas el total. **Denominador: `wc -w` sobre el fichero entero**, que es el que usa la linea base del lote 1. Dilo al lado |
| **pasos inventados sobre pasos escritos** | **una fila por capitulo.** Es la cifra de la regla de volumen. Si un capitulo escribe cero pasos, **la fila dice *sin denominador*, no cero por ciento** |
| **veredictos escritos** | del lote |
| **cuanto tardo y si el tramo fue el correcto** | de la vuelta, diciendo si el segundo capitulo cupo |

**LA TABLA DE MARCADO VA EN TU REPORTE**, paso a paso y con el parrafo citado en cada
puente, no dentro del JSON.

---

## LO QUE ESTA VUELTA TIENE QUE DEJAR MEDIDO

1. **La tasa de puentes de un capitulo GRUESO.** La del `cap_02` (6,25 por ciento
   sobre 16 pasos) es de un capitulo pequeño y rico en inventario. **Con 10.696
   palabras el denominador deja de ser ruidoso**, y esa es la cifra que de verdad va
   a dimensionar el lote 3.
2. **Si un capitulo de 10.696 palabras cabe en una vuelta.** La vuelta 4 contesto a
   medias por 4.824 palabras. **Esta lo contesta de verdad.**
3. **Cuantos vecinos levanta la aduana con dos hermanos de familia en la bandeja.**
   Los candidatos del `cap_03` y del `cap_04` comparten dominio con los dos que ya
   esperan. **El `CHOCAN` del informe solo mira ids identicos**, asi que si quieres
   saber si se levantarian entre si, **lo mides con `src.aduana.medir` y lo dices**,
   como hizo 3.c.
4. **Si la prueba del inventario aguanta en un capitulo que enseña a escribir un
   documento**, que es un genero distinto del narrativo del `cap_02` y del normativo
   del lote 1.

---

## LO QUE EL AUDITOR TE PIDE QUE NO REPITAS, y es una escalada, no un consejo

**CUATRO VUELTAS SEGUIDAS FALLANDO EN EL MISMO SITIO, y ninguna en el dato:**

| vuelta | donde cayo |
|---|---|
| 1 | la lectura |
| 2 | la aritmetica de acompañamiento |
| 3 | el recuento de acompañamiento |
| **4** | **una señal de acompañamiento medida antes de una correccion y publicada despues** |

**El dato central ha estado limpio las cuatro veces. Lo que falla es lo que lo
rodea.** El remedio esta escrito en tu propio protocolo, `EXTRACTOR.md` seccion 4, y
lo unico que hace falta es aplicarlo tambien a las señales:

> **MEDIR TEMPRANO Y PUBLICAR TARDE SIN REMEDIR ES LA MISMA ESPECIE QUE CITAR SIN
> MIRAR.** Toda cifra que publiques **se remide al cierre si algo de la propia vuelta
> pudo haberla movido**, y una correccion de un paso mueve las tres señales de ese
> candidato.

**Esto es una linea de disciplina, no un programa. NO escribas una guarda para
esto** (moratoria de maquinaria, cosecha 7.F).

---

## LAS PARADAS

**Paras, lo declaras en TU REPORTE y te detienes si:**

- **alguna de las tres comprobaciones de apertura falla** (la carpeta, la clave, la
  cabecera). **Manda tu medida, no este parrafo**;
- una regla de la casa te obliga a algo que rompe otra regla de la casa;
- necesitas mover un umbral, una regla de id, el esquema, la prueba del inventario
  (`D.27`) o la vara de continua contra repite. **Ninguna vuelta mueve nada de eso**;
- **el MATERIAL DE LA VUELTA no da ni un procedimiento.** *(Adjudicado por el ACTA 4
  seccion 3.1, para que no vuelva a costar una duda:* **la parada es por VUELTA, no
  por capitulo.** *Un capitulo de cero es un resultado medido y se publica con su
  frontera entera. Si los DOS capitulos dan cero, ahi si paras.)*

**TU NO ESCRIBES `docs/loop/PARA_ALEXIS.md`** (`D.28`). Eso lo hace el auditor, y
solo el. **Y un encargo asigna trabajo, NO MUEVE UNA SEDE.**

**NO paras por:** que un candidato caiga en la aduana (lo corriges y pegas la
salida), que un capitulo de pocos nodos (se dice con su razon), que el tramo no se
llene (**adjudicado: una vuelta corta de candidatos no es un fallo si publicaste tu
frontera entera y dijiste tu razon**), ni porque la relectura de fidelidad te obligue
a retirar pasos que acabas de escribir. **Eso ultimo es la regla funcionando antes de
que el dato entre.**

**NO INSERTAS NADA.** El arnes arranca en `MODO_INSERCION=cuarentena` y **la
insercion es una autorizacion del fundador, no un default** (`D.26`). Los dos
candidatos del `cap_02` siguen esperando, y **eso no bloquea esta vuelta** (`D.32`).

**Y NO FABRICAS MAQUINARIA** (seccion 13). Ni arneses, ni guardas, ni lectores. **En
particular: no propongas una guarda que automatice la relectura de fidelidad.** El
texto fuente no esta en el repo, y una guarda que no tiene el libro no puede juzgar
fidelidad al libro (`D.30`).

---

**MARCA TUS DISCUTIBLES ANTES DE SABER SI ACIERTAS**, ordenados por lo que costarian
si fallas. **Los seis de la vuelta 4 se sostuvieron los seis**, y fue lo que hizo
informativa la tanda: **una duda marcada a tiempo vale mas que un acierto callado.**

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice
una regla vigente, paras y lo traes. No adivines.**
