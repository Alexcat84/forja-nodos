# ENCARGO DE LA VUELTA 75: **PRIMERO LOS DOS PUENTES DE `dar_elogio_disciplina_igual_critica` SALEN DEL GRAFO POR `D.54`, QUE ES LA UNICA TAREA BLOQUEANTE. DESPUES, LAS `7` FICHAS QUE QUEDAN DE GROVE ENTRAN UNA POR VEZ, CON LAS LINEAS Y LAS ARISTAS QUE LA `73` DEJO LISTAS** (`ACTA 73` `73.5`, `73.1`)

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 73`, que audito la vuelta `74`.
`AUDITOR_FORJA.md` seccion `1.4`. **Toda cifra de medida de esta pagina va dentro de un bloque `$` con su salida, o lleva en
su misma linea la seccion de la `ACTA 73` donde esta pegada** (`R8`, `ACTA 73` `73.11`).*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA CLASE, EL LIBRO Y LA REGLA DEL TURNO**

    $ python scripts/deuda.py --clase 75
    LIBRE
      van 1 de 5 desde la ultima de saneamiento (la 74), con 51 deuda(s) esperando
    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_18), citando su frontera. D.50.

**La frase de *continuar desde `cap_18`* es de extraccion y no aplica: Grove esta minado entero**, y lo que se hace es insertar lo
que queda en su bandeja. **El orden de la campania es Grove, Gerber, Marquet** (`PARALELO.md` `8` punto `4`).
`dar_elogio_disciplina_igual_critica` es de `scott_radical_candor`, que esta `INSERTADO`: **corregir un nodo suyo que vive en el
grafo no es tomar ese libro.**

> **UN `insertar` POR VEZ, Y NINGUNO EN VUELO CUANDO TU TURNO TERMINE.** Cada candidato entra entero o no entra. **Al volver cada
> `insertar`: su fila en el reporte, commit y push.**

**El metodo de la `72` vale**: cada `insertar` por una copia de `.v72ext/insertar.py` con la sede de las lineas cambiada a
`.v73ext/veredictos_listos.txt` y la salida a `.v75ext/`, y tu bloqueado en primer plano con una copia de `.v72ext/esperar.py` hasta
su `.fin`, **sin lanzar el siguiente ni tocar el dataset ni la bandeja en medio**. **NO LANZAS NADA EN SEGUNDO PLANO QUE SIGA VIVO AL
CERRAR TU TURNO.** Si algo no te cabe, no lo lances: lo dices en el reporte con las filas que faltan, y entran en la `76`. El reloj
de los `insertar` de la `72`, que es lo que costo y no un techo:

    $ tail -1 .v72ext/relojes_resumen.txt
    insertar: 20 | minimo 274.4 s | mediana 560.0 s | maximo 976.5 s | suma 10920.8 s (3.03 h)

---

## TAREA 1: **REGISTROS DE LA `ACTA 73`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Tu vuelta, reproducida**: no movio dato; tus instrumentos dan lo que pegaste y tus cuatro `como` estan en el registro como sus ficheros | `ACTA 73` `73.1` |
| **Tus ocho discutibles se sostienen**, `D74.1` a `D74.8`; en `D74.6` gana tu `P` y cae la lectura ciega del auditor | `73.5` |
| **Un PUENTE que no viste**: `dar_elogio_disciplina_igual_critica` paso `8`, *y la critica no*, fuera de tu marcado. **Tu cuenta es `2` de `70` y no `1`**, y los `como` de `d084` y `d006` quedan corregidos por correccion declarada en el acta | `73.5` |
| **`REPORTE` cae y sube a `2 de 3`**: la cifra vive en tu tabla de `74.3.2`, en tu cabecera y en tu tabla de cierre. **La siguiente caida de `REPORTE` que acumule para la linea** | `73.2`, `73.7` |
| **Tu remedio nuevo, `R9`**, y `R5` sigue vivo | `73.11` |

## TAREA 2: **BLOQUEANTE (`D.55`), CON LA GUARDA `D.30` EN ROJO: LOS DOS PUENTES DE `dar_elogio_disciplina_igual_critica` SALEN DEL CAMPO** (`73.6`)

**Antes de ningun `insertar`.** La guarda, los dos pasos y sus lineas estan en la `ACTA 73` `73.5` y `73.6`. **La via es la que la
casa ya tiene y no otra** (`D.30`, `D.54`; el precedente es el `P13` de `practicar_franqueza_radical_jefe_propio`): ningun instrumento
reescribe un paso de un nodo insertado, asi que **el paso sale entero y su literal queda escrito en el nodo**.

1. **`python forja.py corregir --nodo dar_elogio_disciplina_igual_critica --anade "CORRECCION DECLARADA ..." --razon "..."`**, una
   vez, **antes de retirar nada**. El texto dice, sin borrar nada de lo que hay: **los pasos `8` y `17` son PUENTE de clausula** por la
   `ACTA 73` `73.5`, con su linea del libro (`L273` y `L283` de `fuentes/scott_radical_candor/cap_13.md`) pegada de un `grep -n -o`;
   **que parte de cada paso si es del libro** (del `8`, *el elogio ayuda a la gente a centrarse en sus fuerzas y a hacer mas del
   trabajo que disfruta y menos del que odia*; del `17`, *en ese ejercicio la gente sale sintiendose vista, conectada e inspirada, y
   dice cosas como llevo anios haciendo esto y no sabia que nadie se hubiera dado cuenta, lo que lleva a mas implicacion*); **que la
   cuenta de fidelidad de su propio resumen**, *20 pasos, 20 TRANSCRIPCION, 0 PUENTE*, **vale** *18 TRANSCRIPCION, 2 PUENTE* (`73.5`); y
   **la tabla de numeros de paso**, porque la bitacora nombra este nodo y sus lineas citan pasos por numero: los pasos `1` a `7` no se
   mueven, **del `9` al `16` pasan a ser del `8` al `15`, y del `18` al `20` pasan a ser del `16` al `18`**; lo que la bitacora cite
   antes de hoy va con la numeracion vieja.
2. **`python scripts/retirar_paso.py --nodo dar_elogio_disciplina_igual_critica --paso 17 --razon "..."` y DESPUES `--paso 8`**, en
   ese orden, para que el numero del segundo no se mueva con el primero. **La `--razon` cita la `ACTA 73` `73.5` y la linea del libro.**
   El instrumento escribe en su frase la fecha de `D.54`, que no es la de hoy: **tu razon lleva la de hoy.**
3. **Despues de cada una de las tres operaciones, `python forja.py gate`, pegado.** Al terminar, **pegados**: los pasos del nodo
   (tienen que ser `18`, `73.5`), `python scripts/retirar_paso.py --ver` en `0`, y el censo con lo que cada operacion movio, **medido y no a
   ojo** (el grafo sigue con los mismos nodos; lo que `corregir` escriba en la bitacora lo dice su salida).
4. **Si el gate sale en rojo, o cualquier instrumento se niega, PARAS la tarea, no insertas nada y lo traes.** No lo arreglas en `src/`
   ni en `scripts/` (`7.F`, `D.55`).
5. **`R9` sobre los `18` que quedan** (`ACTA 73` `73.11`): el `grep` de clausulas que comparan o califican la prueba del libro, pegado
   con lo que encuentre, y cada hallazgo con su tramo literal del libro al lado o traido como PUENTE. **No corriges nada mas en este
   nodo**: si aparece otro puente, lo traes a la `ACTA 74`.

## TAREA 3: **LO QUE ENTRA ES LO QUE SE LEYO**

Antes del primer `insertar`, `python .v73ext/pasos_y_huellas.py`, con su salida **identica** a `.v73ext/pasos_y_huellas.txt` (como en
la `74` al abrir y al cerrar, `ACTA 73` `73.1`), pegada. Si una ficha sale distinta, **no entra**, se relee entera contra su capitulo
y se dice.

## TAREA 4: **LAS FILAS DE `.v73ext/orden.txt`, UNA POR VEZ**

    $ sed -n '2,8p;17,20p' .v73ext/orden.txt | cut -c1-140
    1   usar_banco_nueve_preguntas_entrevista                        cap_15 P11       -                                                         
    2   responder_primer_aviso_renuncia_subordinado                  cap_15 P26       -                                                         
    3   gestionar_retencion_subordinado_valioso_renuncia             cap_15 P27       responder_primer_aviso_renuncia_subordinado               
    4   reciclar_empleado_ascendido_mas_alla_capacidad               cap_16 P21       -                                                         
    5   priorizar_lista_entrenamiento_subordinados                   cap_17 P21       -                                                         
    6   desarrollar_primer_curso_entrenamiento                       cap_17 P22       priorizar_lista_entrenamiento_subordinados                
    7   pedir_critica_anonima_curso_entrenamiento_dictado            cap_17 P23       desarrollar_primer_curso_entrenamiento                    
      CONTINUA   desarrollar_primer_curso_entrenamiento                   > pedir_critica_anonima_curso_entrenamiento_dictado
      CONTINUA   priorizar_lista_entrenamiento_subordinados               > desarrollar_primer_curso_entrenamiento
      CONTINUA   responder_primer_aviso_renuncia_subordinado              > gestionar_retencion_subordinado_valioso_renuncia
      CONTINUA con madre= (aristas distintas): 3 | SOSTENGO por lectura: 0 | solapes entre las dos: 0 | aristas esperadas: 3
    $ grep -v '^#' .v73ext/veredictos_listos.txt | grep -c '|'
    29

1. **En su orden, de la fila `1` a la ultima.** Las lineas `--veredicto` son las del bloque de cada candidato en
   `.v73ext/veredictos_listos.txt`, **tal cual, sin las `#`**. Las `CONTINUA` con `madre=` cablean su arista en el acto: son las de
   las filas `3`, `6` y `7`. **No hay aristas por lectura** (`SOSTENGO`, en el bloque). `priorizar_lista` con `pedir_critica_anonima`
   es `SANO`, abuela y nieta (`D73.9`, `ACTA 72` `72.5`).
2. **La puerta es la aduana de `insertar`, no la lista** (`d031`). **Al volver cada uno, su vecindad de hoy contra la del barrido de
   la `73`** con una copia de `.v72ext/contra_barrido.py` que lea `.v73ext/vecinos_<id>.json`, pegada en su fila. Si levanta un vecino
   sin linea, lo lees con los pasos de los dos delante, escribes su veredicto por la vara `6.1` y solo esa, **y lo marcas en el reporte
   como lectura tuya de esta vuelta**, discutible si dudas. Si levanta `CAERIA` o un error, no fuerces: no entra, y se declara.
3. **Al volver cada `insertar`, su fila en el reporte** como las de la `72`: la aduana de hoy con sus vecinos, la comparacion con la
   `73`, las lineas que pasaste, la arista que cableo y su commit. Cada insertado a `cuarentena/_insertados/grove_high_output/` (`D.31`).
4. **Al terminar la ultima fila que entre: las aristas de la tanda por instrumento**: cuantas se esperaban (bloque de arriba), cuantas
   viven en el grafo, ninguna sin adjudicar, y que ningun nodo viejo cambio fuera del `nodos_siguientes` de sus madres **y de
   `dar_elogio_disciplina_igual_critica` por la TAREA 2**. Si alguna fila no entro, la cuenta dice cuales quedan pendientes con ella.

## TAREA 5: **EL CIERRE**

- **El censo antes y despues de cada tarea**, con una copia de `.v74ext/censo.sh`. Al abrir son los de la `ACTA 73` `73.1`. **Lo que
  se mueve, medido**: el grafo gana una fila por ficha que entre y ninguna por la TAREA 2; la bandeja de Grove pierde las mismas y
  `_insertados` las gana; la bitacora gana las lineas de veredicto de lo que entre (bloque de la TAREA 4) mas lo que la TAREA 2 escriba.
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo, de lo que ENTRO**: `cap_15`, `cap_16` y `cap_17`, contados desde
  `.v73ext/fidelidad.tsv` con los PUENTE ya corregidos en la bandeja, que la `ACTA 72` `72.4` firmo en cero que entran. **Y la fila de
  `cap_13` de Scott** despues de la TAREA 2, con los dos pasos fuera (`73.4`, `73.5`). No a ojo.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera
  cambiada a la `75`, y pegado. **Y `R9`**, donde marques fidelidad.
- **La cabecera y la tabla de cierre se reescriben al cerrar contra lo que se hizo** (la letra del `R4` de la `ACTA 59` `59.18`): **tu `REPORTE` esta a un escalon de la
  parada**, y las dos ultimas caidas vivieron en celdas de tabla (`73.7`).
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`,
  **pegados**. **El cierre estricto tiene que salir en verde: cualquier rojo es tuyo.**
- Commitea `docs/loop/`, `dataset/`, `bitacora/`, `censos/`, los movidos a `_insertados` y tu carpeta `.v75ext/`. **Si nada te obliga
  a parar, no escribas `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO INSERTAS NADA ANTES DE CERRAR LA TAREA 2**, y **NO TERMINAS TU TURNO CON NADA VIVO**, ni un `insertar` ni un barrido.
- **NO CORRIGES NINGUN OTRO NODO DEL GRAFO** ni otro paso de `dar_elogio` que no sean el `8` y el `17`.
- **NO CAMBIAS NINGUNA LINEA PREPARADA NI NINGUNA FICHA** fuera de lo que la aduana levante en el acto (TAREA 4.2). Su fidelidad y sus
  clases estan firmadas.
- **NO TOCAS `cuarentena/gerber_emyth/` NI `cuarentena/marquet_turn_the_ship/`**: van despues de Grove, en ese orden.
- **NO TOCAS `src/`, `scripts/`, el banco, el arnes, el tablero ni los protocolos** (`7.F`, `D.55`), **ni `APERTURA_CIEGA.md`**. Los
  procesos del fundador que veas vivos en otra copia no son tuyos: ni los tocas ni los esperas.
- **NO REORDENAS LA COLA A MANO**, **NO PAGAS NINGUNA DEUDA** y **NO ABRES NINGUN LIBRO.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
