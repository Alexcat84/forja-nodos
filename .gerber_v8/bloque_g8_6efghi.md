
### G8.6.e. El tallado y el censo, corridos HOY

Salida de `python scripts/tallar_reporte.py`, guardada en `.gerber_v8/tallado.txt`:

<!-- TALLADO: parcial salida=.gerber_v8/tallado.txt -->

    TALLADO VERDE: las 176 tabla(s) comprobables son las de su instrumento, celda a celda.

Salida de `python scripts/censar_rutas.py`, guardada en `.gerber_v8/censo_rutas.txt`:

<!-- TALLADO: parcial salida=.gerber_v8/censo_rutas.txt -->

    CENSO VERDE: las 1123 rutas publicadas sostienen lo que dicen sostener.

**LOS DOS VERDES AL PRIMER INTENTO, SIN CORRECCION QUE DECLARAR ESTA VEZ** (a diferencia de la vuelta
`7`, que tuvo que regenerar dos tablas de frontera y corregir un patron de censo mal declarado): las
tres tablas de frontera de esta vuelta (`cap_20`, `cap_21`, `cap_22`) se pegaron desde el instrumento
sin resumir a mano, y cada ruta de evidencia se cito por su ruta exacta, no por patron compartido.

### G8.6.f. La deuda, recomputada al cierre

Salida de `python scripts/deuda.py`, guardada en `.gerber_v8/deuda_cierre.txt`:

<!-- TALLADO: parcial salida=.gerber_v8/deuda_cierre.txt -->

    pendientes: 44    pagadas: 39

**DE `45`/`38` A LA APERTURA (`G8.1.b`) A `44`/`39` AL CERRAR LA VUELTA: `1` PAGADA** (`d123`), **`0`
NUEVAS CONTRAIDAS por mi.** Coincide al digito con la aritmetica de `G8.1.c`.

### G8.6.g. Cero averia de dato: nada de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` se movio

    $ git status --porcelain dataset/ bitacora/ censos/ config/pares_mutuos.jsonl
    (sin salida: ningun fichero de esas cuatro sedes aparece modificado)

**`0` FICHEROS DEL GRAFO MOVIDOS.** Esta vuelta no lo toco, tal como manda `MODO_INSERCION=cuarentena`
(`D.39`): los tres capitulos cerraron con cero candidatos, asi que ni siquiera hay JSON nuevo que sumar
a `cuarentena/gerber_emyth/` (sigue en los `22` ficheros ya escritos en vueltas anteriores).

### G8.6.h. Las condiciones de parada, repasadas una a una (`EXTRACTOR.md` 7)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| una pregunta de doctrina | ninguna nueva abierta: la cola de doctrina se queda en `11` (`D.55`), sin tocar | **NO ES PARADA** |
| una caida de dato | ninguna: `0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` movidos (`G8.6.g`), gate/guiones/tests/tallado/censo VERDES (`G8.6.d`, `G8.6.e`) | **NO ES PARADA** |
| algo contradice una regla vigente o una cifra publicada con su corte | nada: la correccion de `d123` se tachó sin borrar en vez de reescribirse por encima (`G8.1.c`), y el unico discutible se cerro con su cita y su motivo (`G8.4.c`) | **NO ES PARADA** |
| una guarda en rojo | ninguna al cierre: las tres guardas de `EXTRACTOR.md` 6 mas el tallado y el censo, las cinco VERDES sin correccion que declarar esta vez | **NO ES PARADA** |
| una operacion cuyo texto no alcance para ejecutarse sin decidir | ninguna: las cinco tareas del encargo traian su orden completo, incluida la `TAREA 4` con instruccion explicita de declarar el estado del lote sin ejecutarlo, que es justo lo que `G8.4.e` hizo | **NO ES PARADA** |

**NINGUNA DE LAS CINCO SE CUMPLE. ESTE TURNO CIERRA SIN PARADA**, y `docs/loop/PARA_ALEXIS.md` sigue sin
tocar y no es mio (`EXTRACTOR.md` 14): la declaracion de parada es del auditor, no del extractor.

### G8.6.i. `D.61` repasada contra el reporte entero, credito medido, y lo que propongo

#### G8.6.i.1. `D.61`, la segunda pasada, al cierre

El unico discutible de esta vuelta (`G8.4.c`, la pieza `Rb` de `cap_22`) se marco ANTES de escribir el
veredicto y se cerro en el mismo acto, sin candidato: `SANO`, con su cita pegada. **`0` discutibles
abiertos al cierre, por debajo del tope de `2`.** No se abrio ningun discutible en `cap_20` ni en
`cap_21`.

#### G8.6.i.2. Credito: solo se mide, no se anota

Salida de `python forja.py credito`, guardada en `.gerber_v8/credito_cierre.txt`:

<!-- TALLADO: salida=.gerber_v8/credito_cierre.txt -->

    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 8, en 32 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G7
      CIFRA PUBLICADA    0 de 2     ACTA G7
      CLASE              0 de 2     ACTA G7
      DATO MOVIDO        0 de 2     ACTA G7
      REPORTE            0 de 3     ACTA G7

      CREDITO ENTERO: ninguna especie en su tope.

**Identica a la de apertura (`G8.1.a`): este registro lo mueve el auditor con `--anotar` al cerrar su
propia acta, no yo (`EXTRACTOR.md` 14 y 15).** No uso `--anotar` en esta vuelta.

#### G8.6.i.3. Lo que propongo al auditor, todo en mi sede y nada adjudicado por mi

1. **La raiz de `d123` fue mia (nacio en mi propia `ACTA G7`, seccion "Y LO QUE CORRIJO ES MIO, NO
   TUYO") y queda corregida en la celda de `G7.4.e`**, tachada sin borrar, con `ORDEN_DE_LOTES.md` `L27`
   citado al lado (`G8.1.c`).
2. **`cap_20`, `cap_21` y `cap_22` cierran minados los tres, con CERO CANDIDATOS y su razon escrita en
   cada uno** (`G8.2`, `G8.3`, `G8.4.d`): son la carta de cierre a Sarah, el Epilogue y el Afterword mas
   el back matter editorial, y ninguno trae inventario propio de medios, etapas u objetos bajo la vara
   de `9.1`.
3. **El lote `9` queda medido minado entero salvo `d094`**: de las `22` unidades de
   `fuentes/gerber_emyth/`, solo `cap_01` a `cap_03` siguen sin minar, apartadas por decision del
   fundador (`G8.4.e`). **Esto se declara, no se ejecuta**: la cosecha del lote es del fundador y la
   insercion es serial (`D.45`).
4. **Un solo discutible en toda la vuelta, cerrado en el acto sin candidato**: la pieza `Rb` de `cap_22`
   (`L19` a `L26`, el llamado a "dar el primer paso" y "determinar la brecha"), leida como el adjetivo de
   adecuacion de `9.1` disfrazado de instruccion, sin inventario propio nuevo (`G8.4.c`).
5. **Cero correcciones declaradas de instrumento esta vuelta**: las tres tablas de frontera se pegaron
   directamente del instrumento, sin resumen a mano, y el tallado y el censo salieron VERDES al primer
   intento (`G8.6.e`), a diferencia de la vuelta `7`.
6. **El frente tiene ahora `cap_04` a `cap_22` minados sin hueco** (diecinueve capitulos), mas el
   apartado `cap17_reservado` que entra el ultimo (lote `11`, `ORDEN_DE_LOTES.md` `L27`). Solo quedan
   `cap_01` a `cap_03` sin minar, en `d094`, sin tocar por decision del fundador.
7. **La cadencia de saneamiento sigue en `2` de `5` desde la vuelta `6`** (`G8.1.b`): si nada cambia, las
   vueltas `9` y `10` salen `LIBRE` y la `11` es la siguiente de saneamiento, tal como el propio encargo
   ya lo anticipa en su seccion `1`.

#### G8.6.i.4. Cola declarada

Ninguna nueva. `d098`, `d104` y `d111` siguen publicados para la vuelta que inserte (`G8.5.c`), sin que
yo decida nada sobre ellos.
