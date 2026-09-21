# PARA ALEXIS: **LA EXTRACCION DEL MUNDO `11` ESTA CONSUMADA. EL BUCLE PARA Y PIDE**

*Escrito por el auditor al cerrar la `ACTA 61`, que audito la vuelta `62` de la linea serial
(`extraccion-mundo-11`). `AUDITOR_FORJA.md` seccion `3`.*

> ## **ESTA ES LA PARADA FELIZ, NO UNA AVERIA. Las cuatro guardas de dato estan en VERDE, el credito esta entero, y lo que falta no lo puede hacer el bucle.**

---

## 1. EL MOTIVO, EN UNA TABLA, CON LAS SEIS CONDICIONES MEDIDAS UNA A UNA

| condicion de la seccion `3` | se cumple | la medida |
|---|---|---|
| doctrina NUEVA necesaria | **NO** | todo lo que la `ACTA 61` adjudica cita regla escrita. La cola de doctrina sigue en `11` (`D.56`) y no la he tocado |
| contradiccion con regla o cifra publicada | **NO** | la unica tension viva (`tablero --puedo` manda continuar desde `cap_17` y no hay `cap_19`) **ya tiene casillero: es `d088`**, y se declara y se sigue |
| **decision de Alexis** | **SI** | **la insercion del lote `7`** (`D.39`) y **cualquier cambio de alcance de la extraccion**, las dos reservadas a ti |
| fallo tecnico repetido | **NO** | `gate`, `guiones`, `339` pruebas y `cerrar_reporte.py` en VERDE, corridos por mi, y en VERDE tambien la vuelta anterior |
| credito roto | **NO** | `CLASE` `0 de 2`, `CIFRA PUBLICADA` `0 de 2`, `DATO MOVIDO` `0 de 2`, `REPORTE` `1 de 3`, `AUDITOR` `0 de 3`. **Ninguna en su tope** |
| **campania consumada** | **SI** | **`18` de `18` capitulos de `grove_high_output` leidos y adjudicados**, contados por mi, y **no hay lote siguiente que el bucle pueda abrir** |

**LAS DOS QUE SE CUMPLEN SON LAS DOS BUENAS.** No paro porque algo este roto: paro porque **el bucle
hizo lo que tenia que hacer y lo que queda no es suyo.**

---

## 2. EL ESTADO EXACTO, MEDIDO HOY CON MIS PROPIOS COMANDOS

    $ git rev-parse HEAD && git rev-parse --abbrev-ref HEAD
    7aa69a7619e58fc735a19cdd2ea093c8f6b0ce40
    extraccion-mundo-11

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta,
               cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones,
               censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py
    Ran 339 tests in 135.362s
    OK (skipped=1)

    $ python scripts/cerrar_reporte.py
    CIERRE VERDE: las cuatro guardas que muerden, el tallado y el censo. La vigencia corrio y publico
    su cuenta arriba: es cola, no guarda (D.15).

    $ wc -l bitacora/VEREDICTOS.jsonl dataset/nodos.jsonl config/pares_mutuos.jsonl
        740 bitacora/VEREDICTOS.jsonl
        346 dataset/nodos.jsonl
          1 config/pares_mutuos.jsonl
       1087 total

| | |
|---|---|
| **fase** | la vuelta `62` cerro. La `63` no se abre |
| **rama** | `extraccion-mundo-11`, commiteada y pusheada |
| **modo** | `MODO_INSERCION=cuarentena`. **Cero inserciones en toda la corrida** |
| **nodos en el grafo** | `346` |
| **veredictos** | `740` |
| **pares mutuos** | `1` |
| **bandeja de `grove_high_output`** | `91` fichas, PATRON: `cuarentena/grove_high_output/*.json` |

---

## 3. LA CUENTA DEL LIBRO, CONTADA POR DOS INSTRUMENTOS INDEPENDIENTES Y CUADRANDO

**La firmo yo despues de contarla desde cero con un script mio distinto del del extractor, y las `18`
filas por capitulo me salen las `18` al digito** (`ACTA 61` `61.2`):

    $ python .v62aud2/cuenta2.py
    capitulos del libro                     : 18
    candidatos en la bandeja                : 91
    pasos_accionables en la bandeja         : 636
    insertados en el grafo                  : 1
    pasos en los insertados                 : 7
    TOTAL cosechado del libro               : 92
    TOTAL pasos cosechados del libro        : 643
    capitulos CON al menos un candidato: 15
    capitulos que DIERON CERO          : 3 ['cap_08', 'cap_09', 'cap_18']
    suma de control (por capitulo)     : 92 candidatos, 643 pasos
    fichas sin capitulo legible        : 0
    (recortado, entero en .v62aud2/cuenta_libro_aud2.txt con las 18 filas)

**LOS TRES CEROS SON ADJUDICACION FIRMADA, NO HUECO:** `cap_08` y `cap_09` los releyo enteros la
`ACTA 55`; `cap_18` lo cerro la `ACTA 59` `59.4` comprobando sus `35` citas de nodo una a una.

> **LA MINERIA DE `grove_high_output` ESTA CERRADA.** Y con ella, **la extraccion del mundo `11`**.

---

## 4. LO QUE NECESITO DE TI, Y SON TRES COSAS

### 4.a. **LA INSERCION DEL LOTE `7`. Es la que de verdad falta, y es tuya** (`D.39`, `D.32`)

**Hoy `0` de los `92` candidatos de Grove estan en el grafo.** La extraccion cerro; la insercion no ha
empezado, y `D.39` la reserva a tu autorizacion con el informe del lote delante.

**No la pido como tramite y te doy la cifra que decide su precio**, medida en `10` corridas directas
(`ACTA 61` `61.3.a`): **un `forja.py informe` de un solo candidato tarda entre `388,6` y `1062,0` s,
mediana `508,5`**, sobre una poblacion de `440`. **`92` candidatos a uno por informe son muchas horas**,
y eso es una decision de gasto antes que de doctrina.

**LO QUE YA ESTA HECHO Y NO HAY QUE REHACER:** `47` de los `91` de la bandeja tienen ya su informe de
aduana corrido y guardado en las carpetas de trabajo de esta linea, y **tres pares estan adjudicados
por lectura de los pasos** (`ACTA 60` `60.5`, los tres de `cap_17`) **mas uno mas hoy** (`ACTA 61`
`61.5`, `detectar_arreglar_fallo_etapa_menor_valor` contra `supervisar_tarea_delegada_etapa_menor_valor`:
**`CONTINUA`, no `REPITE`**).

### 4.b. **EL MERGE. LO PIDO Y NO LO HAGO**

`AUDITOR_FORJA.md` seccion `3`: **el bucle no funde ramas y el bucle no crea remotos.**

**Pido el merge de `extraccion-mundo-11` con el estado verde delante**, que es el del punto `2`:
`gate` VERDE con `346` nodos, `guiones` VERDE, `339` pruebas con `0` fallos, `cerrar_reporte.py` en
VERDE y **el grafo exactamente donde lo encontro la corrida**.

### 4.c. **EL RELEVO DE LOS DOS FRENTES PAUSADOS, NOMBRANDO RAMA Y ESTADO** (`D.50`)

**`D.50` me manda escribir esta peticion nombrando la rama y el estado, y parar. Es lo que hago.**

    $ python forja.py tablero --puedo gerber_emyth
    LINEA 'serial', LIBRO 'gerber_emyth': NO
      'gerber_emyth' esta PAUSADO y NO COSECHADO: tiene 10 candidato(s) en C:/Users/AlexDesk/Documents/forja-gerber_emyth/cuarentena/gerber_emyth que todavia no han llegado a esta rama. D.50 manda RELEVARLO ENTERO antes de tocarlo, y el relevo empieza por cosechar su rama (extraccion-gerber_emyth).

    $ python forja.py tablero --puedo marquet_turn_the_ship
    LINEA 'serial', LIBRO 'marquet_turn_the_ship': NO
      'marquet_turn_the_ship' esta PAUSADO y NO COSECHADO: tiene 9 candidato(s) en C:/Users/AlexDesk/Documents/forja-marquet_turn_the_ship/cuarentena/marquet_turn_the_ship que todavia no han llegado a esta rama. D.50 manda RELEVARLO ENTERO antes de tocarlo, y el relevo empieza por cosechar su rama (extraccion-marquet_turn_the_ship).

| frente | rama | estado | candidatos |
|---|---|---|---:|
| `gerber_emyth` | `extraccion-gerber_emyth` | `PAUSADO`, `4` de `22` capitulos | `10` |
| `marquet_turn_the_ship` | `extraccion-marquet_turn_the_ship` | `PAUSADO`, `3` de `17` capitulos | `9` |

**TU DECISION DEL `21` SEP YA DIJO QUE HACER CON ELLOS** (`PARALELO.md` `4.d`, punto `4`): quedan con
sus `19` candidatos en bandeja, enteros y sin insertar, **como material para cuando la aduana trabaje
sin campania**. **Lo unico que falta es el paso de fundir, que es tuyo.**

---

## 5. POR QUE NO ABRO UN LOTE SIGUIENTE, MEDIDO Y NO SUPUESTO (`D.32`)

`AUDITOR_FORJA.md` `1.4` me obliga a medir las dos condiciones de apertura del lote que toca y a
publicarlas **antes** de escribir una parada, no a suponer que no hay siguiente:

    $ python .v62aud2/apertura_lotes.py
    gerber_emyth              : material en fuentes/gerber_emyth/ = 22 fichero(s) .md | clave en la tabla canonica = SI
    marquet_turn_the_ship     : material en fuentes/marquet_turn_the_ship/ = 17 fichero(s) .md | clave en la tabla canonica = SI
    bernerslee_bananas        : material en fuentes/bernerslee_bananas/ = 19 fichero(s) .md | clave en la tabla canonica = SI
    openstax_business_ethics  : material en fuentes/openstax_business_ethics/ = 17 fichero(s) .md | clave en la tabla canonica = SI
    openstax_org_behavior     : material en fuentes/openstax_org_behavior/ = 32 fichero(s) .md | clave en la tabla canonica = SI

> **LAS DOS CONDICIONES DE `D.32` SALEN VERDES PARA LOS CINCO. Y NINGUNO DE LOS CINCO ES MIO PARA
> ABRIR**, que es justamente la diferencia entre medir y adjudicar.

- **`gerber_emyth` y `marquet_turn_the_ship`**: `D.50`, y el instrumento dice `NO` con su motivo.
- **`bernerslee_bananas`, `openstax_business_ethics` y `openstax_org_behavior`**: **FUERA DE CAMPANIA**
  en el tablero. Abrirlos es **cambiar el alcance de la extraccion**, y la seccion `3` lo reserva a ti.
  Ademas, `bernerslee_bananas` tiene **la ficha de fuente incompleta** (sin ISBN ni editorial
  verificados, el ano en `PENDIENTE`), y `ORDEN_DE_LOTES.md` dice con esas palabras que **esa ficha no
  la cierra el bucle**.

---

## 6. LO QUE COSTO, PORQUE CONVIENE TENERLO DELANTE AL DECIDIR (`D.56`)

    $ python .v62aud2/coste_corrida.py
    arranque: [2026-09-20 17:16:34] arranque: rama extraccion-mundo-11, MODO_INSERCION=cuarentena
      turnos: 13 | TOTAL 203.6359 USD | extractor 87.7118 | auditor 115.9241 | media 15.6643
    (recortado, entero en .v62aud2/coste_corrida.txt con los 13 turnos uno a uno)

**`203,6359` USD en `13` turnos, con el grafo exactamente donde lo encontro.** El turno del extractor
de esta ultima vuelta costo `8,4868` USD en `1947` s, **por debajo del umbral de `10` de `D.56`**, y es
el primero de la corrida que lo hace estando el trabajo cerrado.

**Y UNA MEDIDA SOBRE LA FORMA DEL BUCLE, NO SOBRE ESTA VUELTA: el auditor se llevo `115,92` de esos
`203,64`, mas que el extractor.** Lo digo porque es la clase de cifra que solo se ve al cerrar una
campania, y porque la vas a necesitar si decides hacer la insercion con este mismo arnes.

---

## 7. LA ULTIMA VUELTA, EN DOS LINEAS, PARA QUE NO TENGAS QUE LEER EL ACTA ENTERA

**LO QUE SE LE FIRMA, Y ES CASI TODO** (`ACTA 61` `61.1` a `61.6`): las guardas, el estado, **la cuenta
del libro identica fila a fila contra un segundo instrumento**, el tablero sin diferencia, el relevo de
la tabla `D.52` por hash, y **el informe de aduana que corrio, que sale identico byte a byte al que
corri yo hoy**.

**LO QUE SE CAE** (`61.4`, `61.7`, `61.8`): el candidato al que le corrio el informe **ya lo tenia
corrido desde la vuelta `54`** y su grep empezaba una carpeta demasiado tarde (el fallo de diseno de esa
tarea es mio y lo cargo en `61.4.a`); **`5` de sus `29` bloques abiertos con `$` no traen lo que el
comando imprime**, que es un remedio escrito roto y **sube `REPORTE` a `1 de 3`**; y cita
`EXTRACTOR.md` `9.1` para adjudicar un duplicado cuando esa misma seccion dice que no sirve para eso.

**Y LO QUE SU EQUIVOCACION PRODUJO SIN QUERER VALE MAS QUE EL ESCALON QUE NO LE CARGUE** (`61.4.b`):
**tres corridas del mismo candidato en dos fechas y con la poblacion movida de `414` a `440` dan el
mismo vecino y las mismas tres cifras al milesimo**, difiriendo en **una sola linea de `30`**. Es la
prueba de determinismo de la aduana mas fuerte que esta casa tiene, y queda anotada como `d092`.

---

## 8. COMO RETOMAR

**SI AUTORIZAS LA INSERCION DEL LOTE `7`**, el bucle se relanza con el modo cambiado y con un encargo
escrito para insertar, no para extraer:

    RAMA=extraccion-mundo-11 MODO_INSERCION=insertar \
    MAX_VUELTAS=20 bash orquestador_forja.sh

**Antes de eso hace falta que alguien escriba `docs/loop/PROMPT_SIGUIENTE.md`, que hoy esta VACIO a
proposito**, y **ese encargo no es mio**: una vuelta de insercion decide veredictos sobre `92`
candidatos, y **el que mide no adjudica** (manual principio `10`) funciona igual de mal al reves.

**SI PREFIERES NO INSERTAR TODAVIA**, no hay nada que hacer: la rama esta verde, commiteada y
pusheada, la bandeja esta intacta con sus `91` fichas, y **`D.32` dice que un lote cerrado y sin
insertar no bloquea nada**.

**LO QUE NO HAY QUE HACER EN NINGUNO DE LOS DOS CASOS** es relanzar el bucle tal cual: `D.49` haria que
el arnes buscase el encargo, lo encontrase vacio y **no abriese la vuelta**, que es exactamente lo que
esta parada quiere.

---

## 9. LOS REGISTROS, AL CERRAR

| sede | que queda escrito |
|---|---|
| `docs/loop/ACTA_AUDITOR.md` | **`ACTA 61`**, con sus `17` secciones y sus instrumentos pegados |
| `docs/loop/CREDITO_serial.jsonl` | las **cinco** lineas de la tanda `ACTA 61`, con `--cae` solo en `REPORTE` |
| `docs/loop/DEUDA.jsonl` | **`d092`** (la triple reproduccion del informe) y **`d093`** (el alcance del barrido de bandeja). Quedan **`27`** deudas agendadas, **ninguna es una guarda en rojo** |
| `docs/loop/PROMPT_SIGUIENTE.md` | **VACIO**, que es lo que la seccion `3` manda |
| `.v62aud2/` | los **`34`** ficheros de mi evidencia: instrumentos, salidas y el informe que corri yo |
