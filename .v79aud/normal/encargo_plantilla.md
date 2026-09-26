# ENCARGO DE LA VUELTA 80: **LAS `20` FICHAS DE MARQUET DENTRO, UNA POR VEZ, EN SU ORDEN, CON LAS LINEAS Y LA ARISTA QUE LA `78` DEJO LISTAS; `d183` Y `d104` PAGADAS; Y SI ENTRAN TODAS CON TODO EN VERDE, EL TAG `primer-equipo-completo`. ES LA ULTIMA TANDA DE LA CAMPANIA** (`ACTA 78` `78.3`, `78.10`)

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 78`, que audito la vuelta `79`.
`AUDITOR_FORJA.md` seccion `1.4`. **Toda cifra de medida de esta pagina va dentro de un bloque `$` con su salida, o lleva en
su misma linea la seccion de la `ACTA 78` o de la `ACTA 77` donde esta pegada** (`R8`, `ACTA 78` `78.11`).*

> # **LIBRO DE ESTA VUELTA: `marquet_turn_the_ship`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA CLASE, EL LIBRO Y LA REGLA DEL TURNO**

@@CMD python scripts/deuda.py --clase 80@@
@@CMD python forja.py tablero --puedo marquet_turn_the_ship@@

**La frase de *continuar desde `cap_17`* es de extraccion y no aplica: el frente de Marquet esta cosechado y la extraccion del mundo
`11` esta cerrada** (`PARALELO.md` seccion `8` punto `3`). Lo que se hace es insertar lo que la `78` dejo listo en su bandeja. **El orden
de la campania es Grove, Gerber, Marquet** (`PARALELO.md` seccion `8` punto `4`), y Grove y Gerber ya estan dentro (`ACTA 78` `78.10`).

> **UN `insertar` POR VEZ, Y NINGUNO EN VUELO CUANDO TU TURNO TERMINE.** Cada candidato entra entero o no entra. **Al volver cada
> `insertar`: su fila en el reporte, commit y push.**

**El metodo de la `77` vale**, con copias en `.v80ext/` que digan en su cabecera que cambiaron y nada mas:

- `insertar.py` de `.v77ext/`, con la sede de las lineas en `.v78ext/veredictos_listos.txt`, la bandeja en
  `cuarentena/marquet_turn_the_ship/`, la tanda en las filas de `.v78ext/orden.txt` y la salida en `.v80ext/`; y `esperar.py`,
  `contra_barrido.py` (que lea `.v78ext/vecinos_<id>.json`), `relojes.py` y `tras_insertar.sh` (con `_insertados/marquet_turn_the_ship`),
  con sus rutas cambiadas.
- `arista.py`, con la sede en `.v78ext/aristas_lectura.txt`, la cita a la `ACTA 77` `77.4` y `77.5`, y **una regla de veredicto mas**: la
  fila `SOSTENGO` de esta tanda **empieza por *D.29, con el criterio de la ACTA 75 seccion 75.4***, que la copia de la `77` no reconoce y
  no cablearia. **Su veredicto de lectura es `CONTINUA`**, como el de `fingir` a `recorrer` en la `77` (`D.53`: el de la lectura, no el de
  la arista): el hijo parte del producto de un paso de la madre, que es lo que la `ACTA 77` `77.4` sostuvo. La copia lo dice en su
  cabecera.
- `aristas_vuelta.py`, con la linea de apertura en la `1172` (`ACTA 78` `78.1`: lo que escriba la `80` en la bitacora son las lineas
  `1173` en adelante), las sedes en `.v78ext/` y la tanda en las filas de `.v78ext/orden.txt`.

Tu bloqueado en primer plano con tu copia de `esperar.py` hasta su `.fin`, **sin lanzar el siguiente ni tocar el dataset ni la bandeja en
medio**. **NO LANZAS NADA EN SEGUNDO PLANO QUE SIGA VIVO AL CERRAR TU TURNO.** Si algo no te cabe, no lo lances: lo dices en el reporte con
las filas que faltan, y entran en la `81`. El reloj de los `insertar` de la `77` y de la `75`, que es lo que costo y no un techo:

@@CMD tail -1 .v77ext/relojes.txt; tail -1 .v75ext/relojes.txt@@

---

## TAREA 1: **REGISTROS DE LA `ACTA 78`, Y EL PAGO DE `d104`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Tu vuelta, reproducida**: no movio ni un byte de dato; `53` de tus `55` comandos corridos dan hoy su salida pegada, y las `2` que no, con su motivo | `ACTA 78` `78.0`, `78.1` |
| **La conjunta de Zhuo, cerrada**: gana la lectura de la `ACTA 77`; no hay frontera de Zhuo y `d183` se paga solo con la de Grove | `78.3` |
| **Tu texto de Grove es el de las dos posiciones del auditor**, y queda listo tal cual | `78.3` |
| **Tus cuatro discutibles se sostienen**, `D79.1` a `D79.4`; **`d104`, adjudicada**: ni `D.37` ni `D.29` dan arista, y se paga aqui | `78.3` |
| **`d150`, `d180`, `d098`, `d099` y `d135` se sostienen como pagadas** | `78.4` |
| **Una caida tuya de `REPORTE` que no acumula**: el bloque de `79.3.1` pega un `grep` con comillas invertidas entre comillas dobles que, corrido tal cual, no da su salida; las cifras eran ciertas. **Un comando con comillas invertidas se pega con comillas simples.** Las cinco rachas siguen en cero | `78.1`, `78.2`, `78.7` |

**`d104` la pagas tu** con `python scripts/deuda.py --pagar d104 --vuelta 80 --como "$(cat .v80ext/como_d104.txt)"`, pegado, y su `como`
cita la `ACTA 78` `78.3`: la cabeza de `cap_12` `L21` no nacio y no nacera, y el paso `5` de `distinguir_tres_tipos_sistemas_negocio`
nombra las actividades sin procedimentarlas, asi que tampoco hay arista por `D.29`. **No toques el grafo por ella.**

## TAREA 2: **LO QUE ENTRA ES LO QUE SE LEYO**

Antes del primer `insertar`, `python .v78ext/pasos_y_huellas.py`, con su salida **identica** a `.v78ext/pasos_y_huellas.txt` (el auditor la
reprodujo, `ACTA 78` `78.1`), pegada. Si una ficha sale distinta, **no entra**, se relee entera contra su capitulo y se dice. Y
`sha1sum -c --quiet .v78aud/huellas_al_barrer.txt`, pegado: la bandeja y el grafo que barrio el auditor en su fase ciega de la `78`.

## TAREA 3: **LAS `20` FILAS DE `.v78ext/orden.txt`, UNA POR VEZ** (`ACTA 77` `77.4`)

@@CMD sed -n '2,21p' .v78ext/orden.txt | cut -c1-80@@
@@CMD sed -n '/^ARISTAS ESPERADAS/,$p' .v78ext/orden.txt; grep -v '^#' .v78ext/veredictos_listos.txt | grep -c '|'@@

1. **En su orden, de la fila `1` a la ultima.** Las lineas `--veredicto` son las del bloque de cada candidato en
   `.v78ext/veredictos_listos.txt`, **tal cual, sin las `#`**. Ninguna es `CONTINUA` con `madre=`.
2. **La arista por lectura se declara EN EL ACTO DE INSERTAR EL HIJO** (`D.29`), con los dos extremos ya vivos: `observar_reunion_rutinaria_senales_plantilla`
   a `seguir_frustrado_preguntar_implantacion_ideas`, **paso `7` de la madre**, por tu copia de `arista.py`, **justo despues de que entre la
   fila `5`**.
3. **La puerta es la aduana de `insertar`, no la lista** (`d031`). **Al volver cada uno, su vecindad de hoy contra la del barrido de la
   `78`** con tu copia de `contra_barrido.py`, pegada en su fila. Si levanta un vecino sin linea, lo lees con los pasos de los dos delante,
   escribes su veredicto por la vara `6.1` y solo esa, **y lo marcas en el reporte como lectura tuya de esta vuelta**, discutible si
   dudas. Si levanta `CAERIA` o un error, no fuerces: no entra, y se declara.
4. **Al volver cada `insertar`, su fila en el reporte** como las de la `77`: la aduana de hoy con sus vecinos, la comparacion con la `78`,
   las lineas que pasaste, la arista si la hay y su commit. Cada insertado a `cuarentena/_insertados/marquet_turn_the_ship/` (`D.31`).
5. **Al terminar la ultima fila que entre: las aristas de la tanda por instrumento** (tu copia de `aristas_vuelta.py`): cuantas se
   esperaban, cuantas viven por los dos lados, ninguna sin adjudicar, y que ningun nodo viejo cambio fuera del `nodos_siguientes` de su
   madre. Si alguna fila no entro, la cuenta dice cuales quedan pendientes con ella.

## TAREA 4: **`d183`: LA FRONTERA DE GROVE, ESCRITA DESPUES DE QUE ENTRE SU NODO** (`ACTA 77` `77.5`, `ACTA 78` `78.3`)

**Cuando `eliminar_seguimiento_descendente_responsabilizar_dueno` (fila `16`) viva en el grafo, y no antes**: `python forja.py corregir --nodo
eliminar_seguimiento_descendente_responsabilizar_dueno --anade "<la linea de ANADE>" --razon "<la linea de RAZON>"` con las dos lineas de
`.v79ext/frontera_grove.txt` **tal cual**, leidas del fichero por un guion y no copiadas a mano, pegado con su salida. Despues, `d183` con
`python scripts/deuda.py --pagar d183 --vuelta 80 --como "..."`, citando la linea de la bitacora que `corregir` escribio y la `ACTA 78`
`78.3`. **Si la fila `16` no entra, `d183` no se paga** y lo dices.

## TAREA 5: **EL CIERRE, Y SI TODO ENTRO, EL DE LA CAMPANIA** (`PARALELO.md` seccion `8` puntos `4` y `5`)

- **El censo antes y despues de cada tarea**, con una copia de `.v79ext/censo.sh`. Al abrir son los de la `ACTA 78` `78.1`. **Lo que se
  mueve, medido**: el grafo gana una fila por ficha que entre; la bandeja de Marquet pierde las mismas y `_insertados` las gana; la
  bitacora gana las lineas de veredicto de lo que entre, mas una por la arista y una por `corregir`.
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo, de lo que ENTRO**, contado desde `.v78ext/fidelidad.tsv` con los PUENTE ya
  corregidos en la bandeja, que la `ACTA 77` `77.3` firmo en cero que entran. No a ojo.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera cambiada a
  la `80`, y pegado. **Y `R9`**, donde marques fidelidad.
- **LA CABECERA, LAS TABLAS DE TAREAS Y LA TABLA DE CIERRE: cada cifra de sus celdas sale de un instrumento corrido en esta vuelta**, y se
  reescriben al cerrar contra lo que se hizo.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`, **pegados**.
  **El cierre estricto tiene que salir en verde: cualquier rojo es tuyo.**
- **SI ENTRARON LAS `20` DE LA BANDEJA (`78.1`), `d183` ESTA PAGADA Y TODO LO DE ARRIBA SALIO VERDE:**
  1. **`python forja.py tablero`, pegado**, con Marquet `INSERTADO` y la linea del mundo `11` completa. Si no sale asi, no hay tag y lo
     traes.
  2. **El censo por libro y las aristas entre libros**, con un guion de `.v80ext/` que lea `dataset/nodos.jsonl` y cuente los nodos por
     su clave de `fuentes` **con su suma**, y las aristas cuya madre y cuyo hijo son de libros distintos, **nombradas**, pegado.
  3. **El tag**: `git tag -a primer-equipo-completo -m "..." <hash>` sobre el commit en que el grafo quedo completo (la ultima fila o
     `d183`, el que sea posterior), **despues** de comprobar con `git diff --stat <hash> HEAD -- dataset bitacora censos cuarentena config src`
     vacio, pegado; y `git push origin primer-equipo-completo`, pegado. **No lo muevas despues.**
  4. **Tu tramo del reporte abre con `PRIMER EQUIPO COMPLETO`**, ese hash y el censo por libro, en la linea de cabecera y en la primera
     seccion.
- **SI NO ENTRARON LAS `20` DE LA BANDEJA (`78.1`)**, no hay tag: lo dices con las filas que faltan, y la `81` las mete.
- Commitea `docs/loop/`, `dataset/`, `bitacora/`, `censos/`, los movidos a `_insertados` y tu carpeta `.v80ext/`. **No escribes
  `PARA_ALEXIS.md` salvo que algo te obligue a parar**: el de cierre es de la `ACTA 79`, que audita esta tanda y, si la sostiene, lo
  escribe y deja `PROMPT_SIGUIENTE.md` vacio (`PARALELO.md` seccion `8` punto `5`).

---

## LO QUE NO HACES

- **NO TERMINAS TU TURNO CON NADA VIVO**, ni un `insertar` ni un barrido.
- **NO CORRIGES NINGUN NODO DEL GRAFO** fuera de `d183` (TAREA `4`). Si una lectura de vecino te ensenia un defecto en uno, lo traes al
  reporte y no lo corriges.
- **NO CAMBIAS NINGUNA LINEA PREPARADA NI NINGUNA FICHA** fuera de lo que la aduana levante en el acto (TAREA `3.3`). Su fidelidad y sus
  clases estan firmadas.
- **NO TOCAS `src/`, `scripts/`, `config/`, el banco, el arnes, el tablero ni los protocolos** (`7.F`, `D.55`), **ni `APERTURA_CIEGA.md`**.
  Los procesos del fundador que veas vivos en otra copia no son tuyos: ni los tocas ni los esperas.
- **NO REORDENAS LA COLA A MANO**, **NO PAGAS NINGUNA DEUDA** fuera de `d104` y `d183`, **NO ABRES NINGUN LIBRO**, y **NO CREAS EL TAG** si
  falta una fila, `d183` o una guarda en verde.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
