# ENCARGO DE LA VUELTA 8: CERRAR EL LOTE 2, `smart_who`

*Escrito por **Alexis** el 10 sep 2026, al levantar la parada de la vuelta 7
(`docs/loop/paradas/2026-09-10-credito-punteros-de-linea.md`).*

---

## LO PRIMERO: TU RACHA ESTA EN CERO, Y LO QUE LA REINICIO

**La racha `REPORTE` estaba en 3 de 3 y paro el bucle. La reinicia una decision
escrita, no el tiempo ni una promesa.** Esta escrita, con fecha, en
`docs/loop/paradas/2026-09-10-credito-punteros-de-linea.md`.

    racha REPORTE   : 0
    racha CLASE     : 0
    racha CIFRA     : 0

**Y VIENE CON SU REMEDIO, QUE ES `D.35` Y ES MECANICO:**

> **NINGUNA CITA DE LINEA SE TECLEA EN UNA TABLA DE TU REPORTE SIN QUE LA SALIDA
> LITERAL DE `sed -n '<n>p'` O `grep -n` QUEDE PEGADA AL LADO.**

    | pieza | linea | la salida, pegada |
    |---|---:|---|
    | serie de diez | L253 | `253:1. Make people a top priority...` |

**El remedio anterior decia que reabrieras la cita antes de teclearla, y se
rompio.** Este obliga a **pegar algo**, que es lo unico que ha funcionado en esta
casa. Esta en `EXTRACTOR.md` **15.5**.

**Y LO QUE LA VUELTA 7 COSTO, para que sepas que no es celo:** tres citas con el
mismo desfase de ocho lineas, y una tabla que declaraba una seccion de L43 a L73
cuando corria hasta L81. **Cuatro bloques del capitulo no aparecieron en ninguna
de las diecinueve piezas de una tabla que se anunciaba completa.**

---

## LO QUE HA CAMBIADO EN TU TURNO, Y ES MUCHO

1. **`D.33`:** los artefactos del arnes (`loop.log`, `ultimo_extractor.json`,
   `ultimo_auditor.json`) **ya no se barren**. Tu mensaje final ya no puede tumbar
   la vuelta siguiente. **Escribelo igual sin guiones largos**, pero si se cuela
   uno ya no rompe nada.
2. **`D.34`:** la apertura ciega del auditor **la cumple el arnes**, no su
   promesa. A ti no te cambia el trabajo; te cambia que **su lectura de tu lote
   se escribe y se sella ANTES de que vea tu reporte.** Escribe pensando en eso.
3. **`D.36`, EL ORDEN QUE LEE:** cuando la asimetria de una señal decide si un par
   se lee, se inserta en el orden que lo lee. **Ya se aplico** a
   `sostener_contacto_oferta_aceptacion` y `celebrar_aceptacion_primer_dia`.
4. **`who` esta en `INGLES_CON_EQUIVALENTE`.** No lo uses en un id. Su equivalente
   es `quien`, y el titulo del libro viaja en `denominaciones.otros_idiomas`.
5. **`D.37`, LA SERIE DECLARADA POR EL TITULO ES ARISTA POR LECTURA.** Cuando
   un nodo enumera sus partes y esas partes existen, **la arista se declara sin
   esperar a la señal**, citando el paso que la nombra. Esta en `EXTRACTOR.md`
   **15.6**, y **desde ahora la declaras en la MISMA vuelta en que insertas las
   partes**. Su aplicacion sobre lo ya insertado es tu **TAREA 0**.
6. **La A de *jugador A* NO sobrevive en el id**, y la regla vigente se sostiene:
   `vender_puesto_jugador` esta bien escrito. **La A viaja entera en `titulo` y en
   `denominaciones`.** No es una perdida: es donde le toca.

**Y EL LOTE 2 YA TIENE 44 NODOS DENTRO.** El fundador autorizo su insercion el 10
sep 2026. El grafo pasa de 8 a **52 nodos**, asi que **la aduana va a levantar
vecinos de verdad**: es la primera vez que escribes contra un grafo con material
de tu propio libro.

---

## LO QUE QUEDA DEL LIBRO, MEDIDO Y CON SU `grep -n` AL LADO

**Tres tramos, y el tercero hay que JUZGARLO antes de cortarlo.**

### TRAMO A. La cola del Cap. 5: `cap_06.md` **L247 a L455**

    247:HOW TO INSTALL THE A METHOD FOR HIRING IN YOUR COMPANY
    297:LEGAL TRAPS TO AVOID
    319:THOUGHTS ON BUILDING YOUR TEAM
    333:RIDING THE RISING TIDE
    395:BEYOND HIRING
    417:YOU CAN DO IT

**Y TRAE DOS SERIES NUMERADAS**, que son `manual seccion 3.4` y piden **un nodo
por paso mas UNA cabeza, jamas dos compresiones de la misma numeracion**:

| serie | de | a | la salida, pegada |
|---|---:|---:|---|
| **la de diez**, dentro de `HOW TO INSTALL` | L253 | L277 | `253:1. Make people a top priority...` y `277:10. Celebrate wins and plan for more change...` |
| **la de cuatro**, dentro de `LEGAL TRAPS TO AVOID` | L307 | L313 | `307:1. Relevance. Do not reject candidates...` y `313:4. Avoid asking candidates illegal questions...` |

**Al entrar, las dos se registran en `censos/series_y_cabezas.md`**, y eso lo hace
la aduana al insertar, no tu a mano.

### TRAMO B. El Cap. 6: `cap_07.md` **L9 a L41**

    9:Imagine the excitement of that!
    41:We wish you great success as you shift your focus from chasing the what, to solving the who.

**EL BORDE `cap_06`/`cap_07` NO SE TOCA** *(decision del fundador, 10 sep 2026)*.
El Cap. 6 empieza en un fichero y su cabecera quedo en el anterior. **Se lee como
UNIDAD y se DECLARA en el reporte**, con las lineas de los dos ficheros. No se
renumera nada, no se mueve nada, y **no es una parada**: es un borde de recorte y
se dice.

### TRAMO C. El material de cierre: `cap_07.md` **L43 a L429**

    43:FOOTNOTES
    79:BIOGRAPHIES OF CAPTAINS OF INDUSTRY
    261:ACKNOWLEDGMENTS
    297:ACCLAIM FOR
    425:LIBRARY OF CONGRESS CATALOGING-IN-PUBLICATION DATA

> **ESTE TRAMO SE JUZGA PRIMERO COMO MINABLE O NO, CON LA VARA, Y ANTES DE
> CORTAR** *(decision del fundador)*.

**NO lo des por no minable porque se llame FOOTNOTES.** Y **NO lo mines porque
tenga 387 lineas.** Pasa `D.27` sobre cada pieza y **publica el fallo con su
cita**, pieza a pieza. **Un tramo descartado con su razon escrita es trabajo
hecho; descartado por su titulo, no.**

**Lo que ya se ve desde fuera, y aun asi se comprueba:** `ACKNOWLEDGMENTS`,
`ACCLAIM FOR` y los datos de catalogacion son paratexto. **`BIOGRAPHIES OF
CAPTAINS OF INDUSTRY` son 180 lineas y es el que de verdad hay que leer**: si ahi
hay procedimiento, es del libro.

---

## TAREA 0, BLOQUEANTE: LAS ARISTAS DE SERIE DEL LOTE 2, ANTES DE EXTRAER

*Aplicacion UNICA de `D.37` sobre lo ya insertado. Decision del fundador del 10
sep 2026. **Va delante de todo lo demas y no se salta.***

**EL LOTE 2 METIO 44 NODOS Y LA ADUANA SOLO LEVANTO SIETE ARISTAS.** Las demas no
faltan porque nadie mirase: **faltan porque ninguna señal las levanta**, que es lo
que `D.19` tiene medido. Y el texto de varias cabezas **enumera sus partes**, asi
que la lectura ya esta hecha por el libro: solo hay que transcribirla.

**LA HERRAMIENTA, y su cita es lo que hace la arista verificable:**

    python forja.py arista --madre <cabeza> --hijo <parte> --paso <n> --razon "..."

**`--paso <n>` es el paso DE LA MADRE que nombra la parte.** El comando lo imprime
entero al declararla. **Pega esa salida en tu reporte**: es el remedio de `D.35`
en esta sede, y sustituye al `sed` porque la linea no vive en un fichero de texto
sino dentro del nodo.

### 0.a. PUBLICA LAS ARISTAS ESPERADAS ANTES DE DECLARAR NINGUNA

**Primero la lista, despues los comandos.** Una cuenta que se escribe despues de
hacer el trabajo se parece demasiado a lo que salio.

**LAS TRES CABEZAS QUE EL HALLAZGO NOMBRA, con sus partes ya comprobadas contra
los 52 vivos. Son TRECE aristas y es tu SUELO, no tu techo:**

| cabeza | paso | parte, que ya vive |
|---|---:|---|
| `abastecer_flujo_candidatos`, *"con sus seis vias"* | 1 | `pedir_referencias_red_personal` |
| | 2 | `pedir_referencias_empleados` **YA DECLARADA, no la repitas** |
| | 3 | `nombrar_delegados_amigos_casa` |
| | 4 | `contratar_reclutadores_externos` |
| | 5 | `contratar_investigadores_reclutamiento` |
| | 6 | `crear_sistema_captura_seguimiento_candidatos` |
| `abordar_cinco_efes_venta`, *"las cinco efes"* | 2 | `vender_encaje_candidato_empresa` |
| | 3 | `vender_cambio_trabajo_familia` |
| | 4 | `vender_libertad_candidato` |
| | 5 | `vender_fortuna_candidato` |
| | 6 | **la efe de la diversion NO tiene nodo.** Compruebalo y dilo |
| `aplicar_metodo_ghsmart_contratacion`, *"los cuatro pasos"* | 1 | `crear_tarjeta_puntuacion_puesto` |
| | 2 | `abastecer_flujo_candidatos` |
| | 3 | `seleccionar_jugador_cuatro_entrevistas` |
| | 4 | `vender_puesto_jugador` |

**TRECE por declarar de estas tres** (cinco, cuatro y cuatro), **con una ya
declarada y una parte ausente**, las dos dichas arriba para que no las cuentes de
mas ni las busques de menos.

### 0.b. EL BARRIDO DE LOS 52, PARA NO DEJAR LA ESPECIE A MEDIAS

**Las tres de arriba son las que el hallazgo nombro, no las que hay.** Barre los
**52 vivos** buscando **toda cabeza cuyo titulo o texto enumere partes**, y
comprueba cuales de esas partes existen como nodo.

**EL METODO, y sirve tal cual:**

    python -c "import io,json; [print(n['id'],'|',n['titulo']) for n in
      (json.loads(l) for l in io.open('dataset/nodos.jsonl',encoding='utf-8'))]"

**Busca en los titulos las marcas de enumeracion**: *con sus N*, *los N pasos*,
*las N efes*, *en N pasos*, *sus N vias*. **Y no te quedes en el titulo:** un
texto puede enumerar sin anunciarlo en la cabecera.

**DOS QUE YA SE VEN DESDE FUERA Y QUE TIENES QUE MIRAR:**

- **`seleccionar_jugador_cuatro_entrevistas`**, *"en seis pasos"*. Dos de sus
  pasos ya estan declarados (`decidir_contratacion_final` y
  `calificar_tarjeta_puntuacion_habilidad_voluntad`). **Los otros cuatro pasos
  nombran entrevistas que parecen tener nodo.** Compruebalo.
- **`planificar_cinco_olas_venta`**, *"las cinco olas"*. **Las cinco olas parecen
  tener nodo cada una.** Compruebalo.

**Y `crear_tarjeta_puntuacion_puesto` ya esta completa**: sus cuatro pasos se
cablearon al insertar. **No la toques.**

### 0.c. DECLARA, Y CUENTA DESPUES

**Una por una, con su razon escrita y su paso citado**, y **pegando la salida del
comando**. La razon dice **que añade el hijo a la madre**, no que se parecen.

**AL TERMINAR, LA CUENTA CONTRA LA PREVISION:**

    aristas esperadas, publicadas en 0.a y 0.b : N
    aristas declaradas                        : M
    y si N no es M, POR QUE, una a una

**Que sobren o falten no es un fallo; no explicarlo si.**

**Y COMPRUEBA EL ESTADO ANTES Y DESPUES:**

    python forja.py gate            antes: 52 nodos, 9 aristas
    python tests/test_aceptacion.py antes: 72 de 72
    python forja.py rancios         antes: verde, 32 veredictos

**Las tres tienen que seguir en verde al acabar**, con el gate contando **9 mas M**
aristas y la bitacora **32 mas M** veredictos.

### 0.d. LO QUE ESTA TAREA NO ES

**No es extraer.** No toca `fuentes/`, no escribe candidatos, no abre capitulo.

**Y NO ES UNA INVITACION A CABLEAR POR PARECIDO.** `D.37` solo cubre la parte que
**el paso de la cabeza NOMBRA**. Si dudas de si un nodo es la parte que ese paso
nombra, **no la declares**: marcala como discutible y sigue. Una arista de mas es
mas cara que una de menos, porque la de menos se ve y la de mas se hereda.

---

## LAS TAREAS

**Tope de cinco, y la TAREA 0 va aparte porque no es extraccion: es la
aplicacion unica de `D.37` sobre lo ya insertado.**

### TAREA 1. El tramo A, capitulo como unidad atomica

Frontera publicada antes de cortar, con las dos series identificadas y **cada cita
con su `sed` pegado**. Despues los candidatos, uno a uno, **con la relectura de
fidelidad DENTRO del acto de escribir** (`D.30`, `EXTRACTOR.md` 15.4).

### TAREA 2. El tramo B, con el borde declarado

Igual, y **el borde `cap_06`/`cap_07` declarado en un bloque propio del reporte**,
con las lineas de los dos ficheros y su `grep -n`.

### TAREA 3. El tramo C, JUZGADO antes que cortado

**Primero el fallo pieza a pieza: minable o no, con la vara y con la cita.**
Solo entonces, si algo es minable, se extrae.

### TAREA 4. El informe del lote y los commits

    python forja.py informe --carpeta cuarentena/smart_who

**Los 44 ya insertados estan archivados** en `cuarentena/_insertados/smart_who/` y
**el informe no los cuenta** (`D.31`): lo que veas es lo nuevo.

**Un commit por tramo**, con los JSON dentro. **NO INSERTAS NADA:**
`MODO_INSERCION=cuarentena`, y **la insercion del resto del lote 2 se autoriza al
leer su informe.**

### TAREA 5. El cierre del lote 2, con sus cuatro medidas por capitulo

**Desglosadas por capitulo, no por vuelta** (`AUDITOR_FORJA.md` 8): candidatos por
mil palabras, **pasos inventados sobre pasos escritos**, veredictos escritos, y
cuanto tardo.

**Y LA CIFRA DEL LOTE ENTERO, que decide el volumen del lote 3:** si tus pasos
inventados por capitulo se mantienen o bajan respecto al **36 por ciento** del
lote 1, el lote 3 sube a tres capitulos por vuelta; si suben, el techo vuelve a
uno.

---

## LAS PARADAS

**Paras, lo declaras en TU REPORTE y te detienes si:**

- una regla de la casa te obliga a algo que rompe otra regla de la casa;
- necesitas mover un umbral, una regla de id, el esquema, `D.27` o la vara de
  continua contra repite;
- alguna de las comprobaciones de apertura falla.

**TU NO ESCRIBES `docs/loop/PARA_ALEXIS.md`** (`D.28`). Eso lo hace el auditor.
**Un encargo asigna trabajo, no mueve una sede.**

**NO paras por:** que un candidato caiga en la aduana (lo corriges y pegas la
salida), que la aduana levante vecinos ahora que hay 52 nodos (**eso es la aduana
funcionando**, lees y escribes el veredicto), que el tramo C no de ni un
procedimiento (se dice con su razon), ni por el borde `cap_06`/`cap_07` (esta
decidido: se lee como unidad y se declara).

**Y NO FABRICAS MAQUINARIA** (seccion 13). En particular: **no propongas una
guarda que compruebe punteros de linea.** El remedio de `D.35` es pegar una salida
que ya corres, y esa es toda la maquinaria que hay.

---

**Cero guiones largos y cero guiones medios. Si algo contradice una regla vigente,
paras y lo traes. No adivines.**
