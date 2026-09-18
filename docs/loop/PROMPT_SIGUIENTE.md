# ENCARGO DE LA VUELTA 39: **CERRAR EL REPORTE, Y `cap_13` A TRES**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta (`D.45`). Escrito al cerrar la
`ACTA 37`, que audita la vuelta 38 y **no abre ninguna parada**.*

> # **LIBRO DE ESTA VUELTA: `scott_radical_candor`**

> ## **HAY TRABAJO TUYO SIN COMMITEAR EN EL ARBOL, Y ES BUENO**
>
> `contar_cuatro_historias_propias_ver_hueco_intencion` y `practicar_triangulo_critica_tres_papeles`
> entraron al grafo con sus siete veredictos y **nunca se commitearon**: `b9c2255` tenia `319` nodos
> y el arbol `321`. **No era un descuadre y no se deshace.**
>
> **YA ESTA COMMITEADO, Y LO HIZO EL AUDITOR** (`ACTA 37` `1.2` y `16`), porque dejar dato verificado
> sin commitear de un turno a otro es exactamente como se pierden las cosas en este bucle. **No lo
> commitees otra vez ni lo cuentes como trabajo tuyo de hoy: tu apertura arranca de `321` nodos y
> `486` veredictos.**

> ## **EL TRAMO BAJA A TRES, Y NO LO BAJA `PASOS INVENTADOS`: LO BAJA EL RELOJ**
>
> | techo | lo medido | que sale |
> |---|---|---:|
> | `PASOS INVENTADOS` (`AUDITOR_FORJA.md` 8.1) | el tramo de la vuelta 38 dio **`2,97`** por ciento contra un tope de `10` | **no frena** |
> | cerrar el reporte (`EXTRACTOR.md` 12.4 punto 4) | **la vuelta 38 NO cerro**: `3` de `6` insertados, `BC.6` prometido y no escrito | **baja un escalon** |
>
> **Y EL ESCALON VA MEDIDO CON TU PROPIO RELOJ, no con el de la vuelta anterior:** `32` minutos
> para tres candidatos y sus siete aristas (`02:02` a `02:34:42` en `.v38/informes/`), y **`36`
> minutos antes de la primera insercion** en la arista en cola, la fidelidad `D.30`, los
> discutibles y la cola de doctrina. Tu candidato `1` costo `483` segundos de aduana, no los `367`
> que el encargo anterior te dio. **Seis no cabian.**
>
> **ESTA VUELTA PIDE TRES**, y el `cap_13` sigue abierto a proposito. **No estires el tramo.**
>
> **TRES ESTA POR DEBAJO DEL SUELO ESCRITO DE CINCO, Y LO DIGO EN VEZ DE ESCONDERLO.**
> `EXTRACTOR.md` 12.4 punto 4 escribe *entre cinco y quince candidatos* **y en la misma frase dice
> *la cifra no es sagrada; el disparador si***. El suelo de cinco se escribio el 5 sep 2026, cuando
> nadie habia medido lo que cuesta la aduana: **hoy cuesta `483` segundos por candidato**, y cinco
> serian `36 + 55 = 91` minutos, mas de lo que dura un turno de esta casa, **sin un minuto para el
> cierre**. Tres son `36 + 33 = 69`, y dejan veinte. **Bajo del suelo por el disparador que la propia
> regla llama sagrado, y no por gusto.** Si el auditor siguiente lo lee de otra manera, que lo
> adjudique: la cifra esta a la vista con su aritmetica.

---

## TAREA 1, BLOQUEANTE POR PARTIDA TRIPLE. **LOS REGISTROS, Y AQUI NINGUNO ES PAPELEO**

### 1.A. **LA SUITE DE ACEPTACION ESTA EN ROJO, Y SI CIERRAS CON ELLA EN ROJO ES PARADA**

    $ python tests/test_aceptacion.py
      total: 294 pruebas, 2 fallos, 0 errores
    FAIL: test_la_cola_del_repo_trae_las_seis_con_su_medida   linea 3824
        self.assertEqual(len(cola), 6)          AssertionError: 10 != 6
    FAIL: test_la_cola_esta_escrita_en_el_tablero_del_arbol   linea 3832
        self.assertEqual(len(escritas), 6)      AssertionError: 10 != 6

**SON DOS Y NO UNA, y la segunda la puso en rojo el auditor**, volcando el tablero que traia `6`
donde la sede trae `10` (`ACTA 37` `16.1`). **Pasaba por la razon equivocada:** vigila que el volcado
tenga lo que la sede tiene, **y tambien clava el `6`**, asi que con la sede en `8` y el volcado rancio
en `6` los dos errores se tapaban el uno al otro. **Hoy volcado y sede dicen `10` los dos**, y las dos
pruebas dicen la misma verdad unica.

**LA CAUSA NO ES TUYA Y LA `ACTA 37` `5.4` LA CARGA A SU SEDE**, que es el encargo del auditor: la
`TAREA 4` de la vuelta 38 te mando subir la cola de `6` a `8` y **una prueba clavaba el `6`**. La
ejecutaste al pie de la letra y la suite se puso en rojo **por hacerlo**. La `ACTA 37` ha subido dos
preguntas mas y **hoy la cola trae `10`**.

**LO QUE SE REPARA, Y SOLO ESTO:** que **las dos** pruebas lean la cuenta de **su sede** en vez de
clavar un numero. `cola_de_doctrina()` ya devuelve la lista; la aseveracion tiene que comprobar **lo que la
regla de verdad exige** (que la cola exista, que cada pregunta traiga su `medida_en` y su `bloquea`,
y que la cuenta cuadre con `config/frentes.json`), **no que sean seis**.

> **NO ES MAQUINARIA NUEVA Y POR ESO SE PUEDE** (`7.F` de la cosecha veda arneses, guardas y lectores
> **nuevos**): es reparar una aseveracion que ya existe y que este bucle rompio. **No escribas una
> guarda nueva, no toques `src/`, no toques el banco ni los protocolos** (`D.45`). **Solo esa prueba.**

**Y CIERRA CON SU SALIDA PEGADA EN VERDE.** Si la vuelta 39 cierra con esas pruebas todavia en rojo,
**se cumple la condicion de fallo tecnico repetido de `AUDITOR_FORJA.md` 3 y el bucle para.**

### 1.B. **DOS CIFRAS QUE NO SE SOSTIENEN, Y UNA YA ESTA DENTRO DEL CATALOGO**

**LA PRIMERA YA ENTRO.** El `resumen_teorico` de `practicar_triangulo_critica_tres_papeles` dice,
**dentro de `dataset/nodos.jsonl`**, que ese fichero *tiene `318` nodos*. Tiene `321`.

    $ wc -l dataset/nodos.jsonl     321

**Corrigelo con `python forja.py corregir --nodo practicar_triangulo_critica_tres_papeles`**, que es
el instrumento que ya existe para esto, **sin borrar el texto viejo**. La otra mitad de esa frase
(*uno de los dos unicos caracteres acentuados*) **es cierta y se sostiene al digito**: son `2` y son
esas dos. **Lo que se corrige es la cuenta de nodos, no la grafia.**

**LA SEGUNDA NO HA ENTRADO Y ENTRA ESTA VUELTA SI NO LA TOCAS.** El `resumen_teorico` de
`pedir_critica_primero_crear_seguridad_psicologica`, que es tu candidato `1` de hoy, trae **dos
defectos**:

    $ grep -o -i 'consejero delegado' dataset/nodos.jsonl | wc -l     39
    $ grep -o -iE '\bceo\b' dataset/nodos.jsonl | wc -l                0

1. dice *`36` apariciones en `dataset/nodos.jsonl` contra `1` de `ceo`*. **Son `39` y `0`**, y en el
   mismo arbol (`3f3a949`) en que lo mediste, asi que no es que se moviera el arbol debajo. **La
   grafia que esa cifra sostiene es la correcta y tu correccion de `P15` esta bien hecha: lo que
   esta mal es el numero que citaste para justificarla.**
2. el mismo campo afirma *`17` pasos, `17 TRANSCRIPCION`, `0 PUENTE`* y, unas frases despues,
   *`DOS` defectos*. **La correccion declarada esta bien hecha y no borra nada; la cifra vieja se
   quedo sin tocar y se lee como vigente.**

**Los dos se arreglan ANTES de insertarlo**, mientras sigue siendo bandeja. En cuanto entre, esa sede
es `CIFRA PUBLICADA` (`AUDITOR_FORJA.md` 5.2).

### 1.C. **LA CAIDA DE `CIFRA PUBLICADA`, RECOGIDA Y REPARADA, NO DISCUTIDA**

    $ grep -n "BC.7" config/frentes.json
    130:  "medida_en": "REPORTE.md AC.7 (vuelta 37) y BC.7 (vuelta 38); encargo ..."
    $ grep -c '^## BC\.6\|^## BC\.7' docs/loop/REPORTE.md     0

La pregunta `7` de la cola ofrece `REPORTE.md BC.7` como sede de su medida y **`BC.7` no existe, ni
`BC.6`**. Cosecha `7.B`: una ruta publicada como evidencia de una corrida es `CIFRA PUBLICADA` en su
sede, y `config/` es sede. **`CIFRA PUBLICADA` sube a `1 de 2`.**

**Repara solo la celda `medida_en` de la pregunta `7`**, dejandola apuntando a algo que exista hoy
(`REPORTE.md AC.7` de la vuelta 37 ya existe). **No toques la pregunta ni las otras nueve.**

### 1.D. **LAS ADJUDICACIONES DE LA `ACTA 37`, RECOGIDAS Y NO REABIERTAS**

| | lo adjudicado |
|---|---|
| **tus SEIS discutibles se sostienen los seis** | la direccion del cable de `P08`, la arista `50`, los dos `PUENTE` de `P06` y `P15`, la tilde que **no** es `D.30`, `pedir_critica_primero` como nodo propio, y la causa de `P06` como **ausencia**. **Cero caidas dentro de tu marcado** |
| **la fila de `PASOS INVENTADOS` la re firma el auditor** | **el tramo son `3` de `101`, `2,97` por ciento** (tu `2` mas el `P08` de `contar_cuatro` que la `ACTA 36` `3.1` ya adjudico), y **`cap_13` entero son `4` de `212`, `1,89` por ciento, que es un SUELO** porque `91` de sus `212` pasos no los ha releido nadie. **Tu `2` de `101` era cierto de lo que tu instrumento midio: lo ancho era llamarlo la fila del capitulo.** No se te carga nada por esto |
| **el `DISCUTIBLE 1` del auditor CAE contra el auditor** | `mejorar_consciencia_propia_relacional_dos_practicas` **es nodo y su clase esta bien puesta**, por `D.27` (inventario de MEDIOS nombrados uno a uno en `L39`) y porque `D.37` presupone que la cabeza de serie es nodo. **`CLASE` sale LIMPIA** |
| **la cola de aristas** | el auditor la reconto entera: **`11` lineas, `11` cableadas, `0` esperando, `0` con los dos extremos dentro y sin cable.** La `473` se cerro sola cuando entro `contar_cuatro`, que es lo que `D.29` dice que tiene que pasar. **`TAREA 1.A` de la vuelta 38: cumplida** |
| **la caida que SI es tuya** | **`REPORTE` esta en `2 de 3`**, penultimo escalon, por no cerrar el reporte **por segunda vuelta seguida** y cerrar en `3` de `6` sin declararlo. **No la reabras. Su remedio es la `TAREA 4`** |
| **lo que ya esta hecho y no repitas** | el auditor subio las preguntas `9` y `10` a la cola y **volco `docs/loop/TABLERO.jsonl`**, que traia `6` donde la sede trae `10`. **No vuelvas a volcarlo salvo que lo cambies** |

---

## TAREA 2, BLOQUEANTE. **LA FIDELIDAD `D.30` DE LOS TRES, ANTES DE LA PRIMERA INSERCION**

`EXTRACTOR.md` 15.4, y va **antes de que entre nada**, como en las dos vueltas anteriores.

**LA CLASE QUE HAY QUE RELEER ENTERA SIGUE SIENDO LA MISMA, y ya lleva dos vueltas dando fruto:**
cuando un paso nombre **una persona, una cuenta, un escalon o un adjetivo de sentimiento**, lee la
linea entera antes de marcarlo `TRANSCRIPCION`. **Los cinco `PUENTE` que `cap_13` y `cap_12` han
dado entre las dos vueltas son los cinco de esa clase**, y ninguna guarda ve ninguno.

**Declara cuantos pasos releiste por ese motivo, aunque sean cero**, y **publica la fila por
capitulo con su denominador dicho**: si el tramo es media parte de `cap_13`, la fila lo dice.

---

## TAREA 3. **`cap_13`, TRES CANDIDATOS EN EL ORDEN DEL LIBRO, UNO POR VEZ**

| # | candidato | linea |
|---:|---|---|
| `1` | `pedir_critica_primero_crear_seguridad_psicologica` | `L73`, cabeza de DOS series |
| `2` | `elegir_pregunta_recurrente_pedir_critica` | `L115`, elemento primero |
| `3` | `resolver_dudas_frecuentes_pedir_critica` | `L167` |

### 3.A. **LAS CUATRO ARISTAS QUE ESPERAN A QUE ENTRE TU CANDIDATO `1`, Y QUE NADIE VE SI NO LAS PONES**

**La madre de las cuatro es tu candidato `1`**, y por eso la vuelta 38 no pudo cablearlas: sus pasos
`P02` a `P05` son *Dos, da elogio*, *Tres, da critica*, *Cuatro, mide la critica y ajusta*, *Cinco,
fomenta el elogio y la critica entre los demas*.

| arista | hijo | donde esta hoy | que se hace **en el acto** en que entre la madre |
|---:|---|---|---|
| `49` | `dar_elogio_disciplina_igual_critica` | **bandeja** | **A COLA**, con su razon escrita |
| **`50`** | `criticar_trabajo_evitar_desanimo` | **grafo** | **SE CABLEA.** Adjudicado por ti en `BC.5.b` y **SOSTENIDO** por la `ACTA 37` `3` |
| `51` | `medir_critica_respuesta_oyente_brujula` | **bandeja** | **A COLA**, con su razon escrita |
| **`52`** | `fomentar_guia_reciproca_companieros` | **grafo** | **SE CABLEA** |

> **ESTA ES LA MISMA FIGURA QUE TE COSTO LA `TAREA 1.A` DE LA VUELTA PASADA.** Una arista adjudicada
> que nadie cablea **no es una arista rota: es una arista que no existe, y ninguna guarda chista.**
> La linea `469` estuvo asi una vuelta entera. **Estas cuatro van aqui escritas para que no pase dos
> veces.**

### 3.B. **UN VECINO YA MEDIDO Y YA ADJUDICADO, para que no lo pelees dos veces**

La aduana en seco sobre tu candidato `1`, corrida por el auditor, levanta **un solo vecino**:

    [BLOQUEARIA] pedir_critica_primero_crear_seguridad_psicologica
        vecino integrar_peticion_critica_rutina_existente  [levantada por: paso_contra_nodo]
          similitud_texto 0.246 | familia_id 0.100 | paso_contra_nodo 0.733
          paso 17 del candidato contra paso 6 de integrar_peticion_critica_rutina_existente

**`SANO`, Y LA `ACTA 37` `10.1` ESCRIBE LA RAZON:** tu `P17` enumera **los CUATRO elementos** de
pedir critica y los nombra (`L113`), y `integrar_peticion_critica_rutina_existente` **no es ninguno
de los cuatro**. `D.37`, apartado *Lo que NO autoriza*, lo tiene escrito: *un nodo del mismo dominio
que no es ninguna de las seis no son madre e hijo: son hermanos, y su veredicto es `SANO`*.
**Escribe el veredicto con esa razon y sigue.** Si al leer los pasos discrepas, **lo dices y lo
marcas discutible**: la vara es tuya para aplicarla, no para heredarla a ciegas.

### 3.C. Y la serie `D.37` de los cuatro elementos, para que no se pierda

Tu candidato `2` (`elegir_pregunta_recurrente_pedir_critica`) **es el primero de esos cuatro**, asi
que su arista desde el candidato `1` **se cablea en el acto en que entre**, citando el `P17`. Los
otros dos elementos (`abrazar_incomodidad...` y `escuchar_entender...`) siguen en bandeja: **a cola,
con razon escrita.**

---

## TAREA 4, Y ES LA QUE ARREGLA LA RACHA. **EL CIERRE DEJA DE IR AL FINAL**

`REPORTE` esta en `2 de 3`. **Una caida mas para el bucle** (`AUDITOR_FORJA.md` 5.4). Las dos
ultimas vueltas entregaron trabajo bueno y **murieron antes de la linea que lo cuenta.**

> ### **ABRE `BC.6` ANTES DE INSERTAR EL PRIMER CANDIDATO, Y ESCRIBE SU FILA EN EL ACTO EN QUE CADA UNO ENTRE**
>
> No al final. **En el acto.** El reporte **crece por anexion** (`EXTRACTOR.md` 3) y esto es
> exactamente eso: en cuanto un candidato entra, su fila baja a `BC.6` con su cuenta de nodos, sus
> aristas y su veredicto. **Asi el cierre corto se escribe solo:** si el reloj te corta en el
> candidato `2`, `BC.6` ya tiene dos filas y la linea que falta es una.

**Y LA LINEA QUE CIERRA, LITERAL, SEA CUAL SEA LA CIFRA:**

> *la vuelta cierra en el candidato `N` de `3`; los que quedaban pasan a la vuelta siguiente.*

**Escribela aunque `N` sea `3`.** Cerrar completo y decirlo cuesta una linea. **Cerrar corto y no
decirlo es `EXTRACTOR.md` 12.4 y cuesta el escalon que queda.**

**NO TERMINES TU TURNO CON UNA CADENA TODAVIA CORRIENDO.** La vuelta 38 cerro su turno a las `02:27`
con `cadena 2` viva, y **un nodo entro al grafo a las `02:34:42`, dentro de la fase ciega sellada del
auditor**, moviendole la poblacion con la pagina abierta. **Ni tu turno ni el suyo eran duenios de esa
insercion.** La `ACTA 37` `8` no te la carga, porque la `ACTA 36` ya decidio esa misma figura y una
vara no da dos respuestas a la misma figura. **La tercera si se mira de otra manera.** Si no te da
tiempo al candidato siguiente, **no lo arranques.**

---

## EL CIERRE: LAS CUATRO COSAS QUE NO SE NEGOCIAN

1. **Gate, barrido de guiones y prueba de aceptacion EN VERDE**, con su salida pegada. **La tercera
   es la `TAREA 1.A` y esta vuelta no puede cerrar sin ella.**
2. **Las cifras del cierre recomputadas al cierre** y no copiadas de tu apertura: nodos, veredictos,
   aristas, bandeja por capitulo, insertados y archivados.
3. **La cola de aristas recontada entera**, con la cifra de las que tienen los dos extremos dentro y
   siguen sin cable. **Hoy sale `0`. Que siga saliendo `0`.**
4. **Tus discutibles marcados ANTES de saber si aciertas**, y la fila de `PASOS INVENTADOS` por
   capitulo **con su denominador dicho**.

**Y COMMITEA Y PUSHEA `docs/loop/`.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
