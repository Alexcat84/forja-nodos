# PARA ALEXIS. EL BUCLE SE DETIENE: **CREDITO ROTO, Y LA RACHA ROTA ES LA DEL AUDITOR**

*Escrito por el auditor al cerrar la `ACTA 26`, que audita la **vuelta 26**.
`AUDITOR_FORJA.md` `3`, condicion **credito roto**. `PROMPT_SIGUIENTE.md` queda **VACIO**.*

---

## 1. EL MOTIVO, EN UNA LINEA

> **Mi propia racha llega a `3 de 3`.** `AUDITOR_FORJA.md` `5.5` y `D.38.2`: **tres seguidas
> paran**, y la mia venia en `2 de 3` desde la `ACTA 24` sin ninguna tanda limpia en medio.

**NO ES LA DEL EXTRACTOR.** La vuelta 26 sale **limpia de `CLASE` y de `CIFRA PUBLICADA`**, con las
siete cifras de su cierre reproducidas al digito por mis comandos, sus nueve discutibles sostenidos
y siete relecturas ciegas mias que coinciden las siete. **Su unica caida es de especie `REPORTE` y
su racha queda en `1 de 3`.** Lo digo primero porque es lo que el estado de verdad dice.

### 1.1. Las dos caidas mias, y las dos estan en la apertura que el arnes sello

| # | la caida | especie | donde |
|---:|---|---|---|
| **1** | **Publique que *ningun nodo del grafo y ningun candidato de la bandeja dice de que capitulo sale*. `33` de `234` lo dicen, y los DOCE de esta vuelta estan entre ellos**, en `resumen_teorico`. Corri un censo de CAMPOS y saque una conclusion sobre CONTENIDO | **`CIFRA PUBLICADA PROPIA`** | `APERTURA_CIEGA.md` `10`, sellada |
| **2** | **Declare `NO APLICA` el `HEREDADO 3` punto 2** (*que mis instrumentos saneen los guiones al volcar texto del libro al arbol*) **con el motivo de que ninguno escribe en el arbol.** Seis de ellos escribian, la tabla `1.4` de mi propia apertura los lista, **y el barrido de guiones estaba en ROJO con ocho hallazgos mios al empezar mi turno normal** | **herencia con motivo falso** | `APERTURA_CIEGA.md` `0.4`, sellada |

**Las dos son del mismo turno, asi que suben UN escalon y no dos** (`ACTA 25` `8.2`: las rachas
cuentan tandas, no piezas). **Ese escalon era el ultimo.**

**Y LA CAIDA `1` ES EL EJEMPLAR LITERAL DE DOS REGLAS QUE ME GOBIERNAN:** `AUDITOR_FORJA.md` `0`
(*contar bien un campo y sacar la conclusion equivocada sigue siendo una caida: la fuente hay que
elegirla antes de contarla*) y `1.1` (*una busqueda negativa no se puede citar*). **No hay lectura
benevola que la salve, y no la busco.**

### 1.2. La lectura que me salvaria, escrita por mi y no tomada por mi

`D.38.1` dice que **una tanda limpia pone el contador a cero**. La `ACTA 25` **no tuvo ninguna caida
que acumulase**. Si *limpia* significara *sin caidas que acumulen*, la 25 habria puesto mi contador
a `0`, lo de hoy seria `1 de 3` **y no habria parada**.

**No la tomo, por dos motivos, y los dos estan en la doctrina:**

1. **La `ACTA 25` ya decidio lo contrario sobre si misma**, con las dos lecturas delante: *que
   ninguna acumule por la letra no la vuelve limpia... La dejo en `2 de 3` y digo que existe la otra
   lectura, para que cualquiera pueda decir que me absolvi si cree que lo hice.*
2. **`5.4`:** *La racha NO se reinicia sola. La reinicia una decision de Alexis escrita en
   `docs/loop/paradas/`... **Un auditor que pone su propia racha a cero se esta absolviendo.***

> **ES TUYA PARA TOMARLA SI LA CREES BUENA. NO ES MIA PARA TOMARLA HOY.**

---

## 2. LO SEGUNDO QUE TRAIGO, Y QUE SOLO HABRIA PARADO EL BUCLE IGUAL

> **`D.38.5` LLEVA CUATRO DIAS ESCRITA Y NO HA LLEGADO A `src/aduana.py`.**
> Es *contradiccion con una regla vigente* (`AUDITOR_FORJA.md` `3`) y **ninguna regla de correccion
> existente la resuelve**, porque arreglarla es tocar codigo y la moratoria de maquinaria (`5.6`) me
> lo prohibe sin una caida de dato consumada.

**Lo levantamos los dos, a ciegas y por caminos distintos:** yo con un barrido dirigido
(`APERTURA_CIEGA.md` `5.3`), el extractor con un rechazo de la aduana (`T.6` propuesta 3).

**La regla**, `docs/BANCO_DE_REGLAS.md` linea 1573, cuyo titular es literalmente *TAMBIEN PARA LA
ADUANA*:

    | **el barrido de vecinos** (las tres seniales) | **grafo mas bandejas** |
    | **la guarda `el id ya vive en el grafo`**     | **solo el grafo.** ...

**El arbol:**

    src/informe.py:222     poblacion = list(nodos) + list(bandejas)
    src/aduana.py:785      nodos = comun.leer_jsonl(ruta_dataset)
    src/aduana.py:797      vecinos = buscar_vecinos(candidato, nodos, umbrales)
    $ grep -n "poblacion_de_bandejas" src/aduana.py     ->  cero coincidencias

    $ python forja.py informe cuarentena/scott_radical_candor/cuidarse_agotamiento_centro_rueda.json
    poblacion del barrido       : 348   (234 del grafo mas 114 que esperan en bandejas)
    (su salida de la vuelta 26, .v26/ins_c01.txt)
    blocking multi señal contra 222 nodo(s) del dataset

**EL COSTE, MEDIDO:** cinco pares por encima de umbral **sin veredicto**, y los cinco con un extremo
en la bandeja; el sexto, el unico con los dos extremos en el grafo, **si lo tiene**. El ejemplar de
esta vuelta: cuando `cambiar_posicion_hechos_explicar_cambio` entro, la aduana no vio a
`cuidarse_agotamiento_centro_rueda`, que da `similitud_texto 0.402` en el informe.

**No es perdida: es aplazamiento.** El par se paga cuando entre el segundo. **Pero `D.38.5` nacio
para que un par no dependa de que alguien se acuerde.**

---

## 3. EL ESTADO EXACTO, MEDIDO HOY CON MIS COMANDOS

| | |
|---|---:|
| **rama** | `extraccion-mundo-11` |
| **commit al detenerse** | `2e22ed9` (mas el commit de `docs/loop/` de esta acta) |
| **nodos en el grafo** | **234** (`python forja.py gate`) |
| **veredictos en bitacora** | **240** |
| **pares mutuos** | **1** (la cabecera; cero pares) |
| **bandeja del lote 4** (`scott_radical_candor`) | **111** de `142` |
| **insertados del lote 4** | **31** |
| **bandeja del lote 5** (`marquet_turn_the_ship`) | **3** |
| **aristas vivas** | **84**, de ellas **0 entre libros** |
| **deuda de arista con algun extremo fuera** | **44** |
| **deuda con los dos extremos dentro y por cablear** | **0** |
| **pares bloqueados esperando veredicto** | **0** |
| **unidades del lote 5 por minar** | **15** de 17 |

**LAS GUARDAS, LAS CINCO CORRIDAS POR MI EN ESTA VUELTA Y LAS CINCO EN VERDE:**

    $ python forja.py gate            -> VERDE, 234 nodos verificados, 12 guardas
    $ python forja.py guiones         -> VERDE, cero guiones largos y cero medios
    $ python forja.py resolutor       -> 234 vivos, 0 deprecados, 0 alias
    $ python forja.py rancios         -> VERDE, 240 veredictos comprobados
    $ python tests/test_aceptacion.py -> 130 pruebas, 0 fallos, 0 errores
    $ python scripts/tallar_reporte.py-> VERDE, 42 tablas comprobables
    $ python scripts/censar_rutas.py  -> VERDE, 353 rutas, 0 caen

**EL ARBOL ESTA SANO. Lo que esta roto es mi credito, no el dato.**

### 3.1. Las rachas al detenerse

    CLASE            (extractor) : 0 de 2
    CIFRA PUBLICADA  (extractor) : 0 de 2
    REPORTE          (extractor) : 1 de 3   (reiniciada por tu decision 2 del 15 sep)
    la del auditor, una sola     : 3 de 3   <- LA QUE PARA

---

## 4. LO QUE NECESITO DE TI

### 4.1. OBLIGATORIA: mi racha

**`5.4`: la racha no se reinicia sola. La reinicia una tanda limpia o una decision tuya escrita en
`docs/loop/paradas/`, y ninguna de las dos soy yo.**

| opcion | que significa |
|---|---|
| **reiniciar y seguir** | **es la segunda vez que mi racha llega a `3`** (la primera fue la `ACTA 20`, reiniciada el 12 sep). **Esa repeticion es dato, no ruido** |
| **reiniciar con condicion mecanica encima**, como hiciste con `D.40`, `D.41` y `D.42` | **la que yo recomendaria**, y la condicion que le pega a las dos caidas de hoy es **la misma**: *toda afirmacion universal sobre el dato (`ningun`, `todos`, `cero`) que publique en mi apertura o en mi acta se corre como comando sobre el CONTENIDO y no sobre los campos, con su salida pegada.* Es barata: es un `grep`, y hoy me habria cazado las dos |
| **resolver la ambiguedad de `tanda limpia`** (`1.2`) | **la decide la casa de una vez y deja de decidirla el auditor cada vuelta.** Dos actas seguidas han tenido que razonarla contra si mismas |

### 4.2. OBLIGATORIA: `D.38.5` contra `src/aduana.py`

Tres salidas posibles, y **ninguna es mia**:

| opcion | que implica |
|---|---|
| **cablear la aduana a `grafo mas bandejas`** | es la que el titular de la regla dice. Toca `src/aduana.py`, **con su caso positivo**, y la moratoria (`5.6`) pide que lo autorices tu |
| **estrechar `D.38.5` por correccion declarada** | que la regla diga que **solo el informe** mide grafo mas bandejas, **y que la aduana mide solo el grafo por diseño**. Es gratis y quita la contradiccion. **Pero deja el hueco que la regla vino a tapar** |
| **dejarla como esta y declararlo** | la peor: una regla que dice una cosa y un codigo que hace otra **es la enfermedad que `7.C` de la cosecha llama por su nombre** |

### 4.3. TRABAJO YA ADJUDICADO, QUE NO HAY QUE REHACER

*Esta seccion existe porque mi remedio de la fase ciega cazo que **siete de los ocho puntos
adjudicados en la `ACTA 25` no llegaron al encargo de la vuelta 26** (`APERTURA_CIEGA.md` `6`). Los
de hoy quedan aqui escritos para pegar.*

1. **LA PRIMERA ARISTA ENTRE LIBROS DE ESTA CASA, ADJUDICADA Y VENCIDA** (`ACTA 26` `2.3`):

       python forja.py arista --madre despedir_persona_respeto_franqueza \
                              --hijo  despedir_persona_franqueza_radical --paso 8 \
                              --razon "D.29 por lectura: el paso 8 de la madre NOMBRA (ayuda a tu
                              persona a cargo a ponerse en el mejor camino posible hacia su capitulo
                              siguiente) y el hijo lo PROCEDIMENTA en sus pasos 5, 6 y 8. El libro lo
                              escribe literal en cap_06 L299: Can I help by making an introduction?
                              Admisible entre libros por ACTA 15 3.4, que ninguna parada retira."

   **Los dos extremos viven en el grafo desde la vuelta 26**, que era la condicion 1 de `ACTA 15`
   `3.4` y que en su dia no se cumplia. **Si te reservas el estreno de la primera arista entre dos
   libros, lo escribes en `docs/loop/paradas/` y el encargo siguiente la retira**, que es como
   aquella acta dejo dicho que se retiraria.

2. **DOS ARISTAS MAS QUE MI LECTURA CIEGA LEVANTO Y QUE NINGUNA SEÑAL VE** (`APERTURA_CIEGA.md`
   `4.3` y `4.4`), **con los dos extremos ya dentro del grafo**:
   - `decidir_momento_despedir_persona > despedir_persona_franqueza_radical`: **el entregable del
     primero es la condicion de activacion del segundo, escrito con esas palabras en los dos
     ficheros**, y los cuatro campos de arista de los dos estan vacios.
   - `aprender_resultados_vencer_dos_presiones > cambiar_posicion_hechos_explicar_cambio`: **`D.37`
     en su forma fuerte**, la madre nombra *las dos enormes presiones* y el libro imprime los dos
     rotulos (`cap_07` `L403` `Pressure to be consistent`, y `Burnout`). **La segunda mitad vence
     cuando entre `cuidarse_agotamiento_centro_rueda`, que sigue en la bandeja.**

3. **LOS NUEVE DISCUTIBLES DE LA VUELTA 26 ESTAN ADJUDICADOS Y LOS NUEVE SE SOSTIENEN**
   (`ACTA 26` `2.1`). **El discutible `2` no estaba pendiente de doctrina**: lo adjudico la
   `ACTA 15` `3.4` hace once vueltas. **No se relee nada de eso.**

4. **`PASOS INVENTADOS POR CAPITULO` DE LA VUELTA 26 ESTA FIRMADO** (`ACTA 26` `4.3`):
   **`cap_06` `0,00` por ciento** (43 de 79 pasos releidos contra su parrafo) y **`cap_07` `0,00`
   por ciento** (40 de 40, el capitulo entero). **`0` puentes sobre `83` pasos leidos.**
   **El tramo del lote 5 se queda en TRES** y no sube, razonado en `4.4`.

5. **LA COLA HEREDADA DE `decidir_momento_despedir_persona` ESTA PAGADA AL DIGITO**: eran `4` pares
   y son `4`, con los cuatro nombres (`APERTURA_CIEGA.md` `5.2`). **Era la cifra que costo la parada
   de la vuelta 25.**

6. **LAS TRES PROPUESTAS DEL EXTRACTOR** (`T.6`): la `1` **queda contestada por cita** en `ACTA 26`
   `2.2` (`EXTRACTOR.md` 11 publica su cifra con su poblacion, asi que no hace falta doctrina nueva
   ni mover ningun umbral); la `3` **es la de `4.2` de este documento**; y la `2` sigue viva y **es
   trabajo del encargo siguiente**: *meter `recorrer_rueda_hacer_cosas_equipo` ANTES que sus partes
   en el orden de `cap_07`*, porque sus partes estan las tres en la bandeja y si entran antes que la
   cabeza sus aristas `D.37` no las podra cablear la aduana.

---

## 5. COMO SE RETOMA

1. **Escribes tu decision en `docs/loop/paradas/`** con la fecha en el nombre, como las anteriores.
2. **Borras o archivas `docs/loop/PARA_ALEXIS.md`**, que es lo unico que el arnes mira para saber si
   el bucle esta detenido.
3. **El acta que retome cita ese fichero por su nombre y dice en que queda cada racha y por que**
   (`5.4`).
4. **El encargo siguiente**, si decides que el bucle siga, es corto y esta claro: **seguir
   insertando el lote 4**, que tiene `111` candidatos en bandeja y se paro dentro de `cap_07` en
   `centrar_debate_ideas_fuera_egos`, **con la cabeza de la rueda por delante de sus partes**
   (punto `4.3.6`), y **el lote 5 por su orden si la insercion deja sitio**.

**EL BUCLE NO FUNDE RAMAS Y NO CREA REMOTOS. No pido merge**: el lote 4 no esta insertado entero,
asi que esto **no es la parada feliz**.

---

    rama            : extraccion-mundo-11
    nodos           : 234
    veredictos      : 240
    fase            : lote 4 EN INSERCION (31 de 142), lote 5 abierto y sin insertar (3 en bandeja)
    guardas         : las siete en VERDE
    motivo de parada: CREDITO ROTO, racha del AUDITOR en 3 de 3 (AUDITOR_FORJA.md 3 y 5.5)
    segundo motivo  : CONTRADICCION, D.38.5 vigente contra src/aduana.py (AUDITOR_FORJA.md 3)
