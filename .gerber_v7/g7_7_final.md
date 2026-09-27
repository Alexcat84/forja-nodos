
### G7.6.f. La deuda, recomputada al cierre

Salida de `python scripts/deuda.py`, guardada en `.gerber_v7/deuda_cierre.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/deuda_cierre.txt -->

    pendientes: 40    pagadas: 38

**DE `42`/`36` A LA APERTURA DE ESTA TAREA (`G7.1.b`) A `40`/`38` AL CERRAR LA VUELTA: `2` PAGADAS**
(`d117`, `d110`), **`0` NUEVAS CONTRAIDAS por mi.** Coincide al digito con la aritmetica de `G7.1.c` y
`G7.2.d`.

### G7.6.g. Cero averia de dato: nada de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` se movio

    $ git status --porcelain dataset/ bitacora/ censos/ config/pares_mutuos.jsonl
    (sin salida: ningun fichero de esas cuatro sedes aparece modificado)

**`0` FICHEROS DEL GRAFO MOVIDOS.** Esta vuelta no lo toco, tal como manda `MODO_INSERCION=cuarentena`
(`D.39`): los seis candidatos se quedan en `cuarentena/gerber_emyth/` a la espera de que el lote cierre.

### G7.6.h. Las condiciones de parada, repasadas una a una (`EXTRACTOR.md` 7)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| una pregunta de doctrina | ninguna nueva abierta: `d119` (vuelta `6`) sigue registrada y sin tocar, la cola de doctrina se queda en `11` (`D.55`) | **NO ES PARADA** |
| una caida de dato | ninguna: `0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` movidos (`G7.6.g`), gate/guiones/tests/tallado/censo VERDES (`G7.6.d`, `G7.6.e`) | **NO ES PARADA** |
| algo contradice una regla vigente o una cifra publicada con su corte | nada: la discrepancia de `39` contra `42` deuda(s) esperando se declaro en el acto (`G7.1.b`) en vez de resolverse copiando, y las dos tablas de frontera que el hook marco `DIFIERE` se corrigieron regenerando, no tecleando (`G7.6.e`) | **NO ES PARADA** |
| una guarda en rojo | ninguna al cierre: las tres guardas de `EXTRACTOR.md` 6 mas el tallado y el censo, las cinco VERDES tras sus correcciones declaradas | **NO ES PARADA** |
| una operacion cuyo texto no alcance para ejecutarse sin decidir | ninguna: las cinco tareas del encargo traian su orden completo, incluida `d111` con instruccion explicita de medir y no decidir (`TAREA 4`), que es justo lo que `G7.4.e` hizo | **NO ES PARADA** |

**NINGUNA DE LAS CINCO SE CUMPLE. ESTE TURNO CIERRA SIN PARADA**, y `docs/loop/PARA_ALEXIS.md` sigue sin
tocar y no es mio (`EXTRACTOR.md` 14): la declaracion de parada es del auditor, no del extractor.

### G7.6.i. `D.61` repasada contra el reporte entero, credito medido, y lo que propongo

#### G7.6.i.1. `D.61`, la segunda pasada, al cierre

Los dos discutibles de esta vuelta (`G7.3.d`) se marcaron ANTES de escribir sus candidatos y los dos se
ejecutaron o cerraron en el mismo acto: el `1` (`C2`) se ejecuto escribiendo el candidato entero; el `2`
(Hierarchy of Systems) se cerro sin escribir candidato, con su linea citada. **`0` discutibles abiertos
al cierre, por debajo del tope de `2`.** No se abrio ningun discutible en `cap_19` ni en el resto de la
vuelta.

#### G7.6.i.2. Credito: solo se mide, no se anota

Salida de `python forja.py credito`, guardada en `.gerber_v7/credito_cierre.txt`:

<!-- TALLADO: salida=.gerber_v7/credito_cierre.txt -->

    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 7, en 27 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G6
      CIFRA PUBLICADA    0 de 2     ACTA G6
      CLASE              0 de 2     ACTA G6
      DATO MOVIDO        0 de 2     ACTA G6
      REPORTE            2 de 3     ACTA G6

      CREDITO ENTERO: ninguna especie en su tope.

**Identica a la de apertura (`G7.1.a`): este registro lo mueve el auditor con `--anotar` al cerrar su
propia acta, no yo (`EXTRACTOR.md` 14 y 15).** No uso `--anotar` en esta vuelta.

#### G7.6.i.3. Lo que propongo al auditor, todo en mi sede y nada adjudicado por mi

1. **La raiz de `d117` fue del auditor y queda corregida en la cabecera de esta misma vuelta**
   (`G7.1.c`), tachada sin borrar, con `python .g6aud/clase_de_vuelta.py` reproducido al digito.
2. **`d110` se paga con el veredicto opuesto al que la vuelta `5` dejo abierto**: leida la continuacion
   de la escena en `cap_18`, el autor SI saca el Operations Manual del caso, y el candidato que lo
   prueba (`construir_estrategia_gente_cuatro_componentes`) nace en `cap_18` (`G7.2`).
3. **`cap_18` y `cap_19` cierran minados, seis candidatos entre los dos, `0 CAERIA` en las seis aduanas,
   `0` PUENTE en los `51` pasos escritos** (`G7.3`, `G7.4`, `G7.5.a`).
4. **La cabeza de serie de `cap_13` (`recorrer_siete_pasos_programa_desarrollo_negocio`) tiene ya sus
   seis pasos alcanzables minados y sigue en `0` de `7`**: ninguno de los seis capitulos produjo un nodo
   que se llame a si mismo el paso entero, todos dieron metodo dentro del paso (`G7.4.e`). Queda medido
   para la vuelta que inserte, sin que yo decida que se hace con ella.
5. **Dos correcciones declaradas de instrumento en esta misma vuelta, las dos regenerando y no
   tecleando**: las dos tablas de frontera que el hook marco `DIFIERE` (`G7.6.e`), y el censo de rutas
   que marco `CAE` un patron mal declarado (`G7.6.e`).
6. **El frente tiene ahora `cap_04` a `cap_19` minados sin hueco** (dieciseis capitulos), mas el
   apartado `cap_17` reservado que no se toca nunca. Quedan `cap_20`, `cap_21` y `cap_22` sin minar.
   `cap_01` a `cap_03` siguen en `d094`, sin tocar por decision del fundador.
7. **La cadencia de saneamiento va `1` de `5` desde la vuelta `6`** (`G7.1.b`): si nada cambia, las
   vueltas `8`, `9` y `10` salen `LIBRE` y la `11` es la siguiente de saneamiento.

#### G7.6.i.4. Cola declarada

Ninguna nueva. `d111` queda medida y no decidida, tal como el encargo lo pide (`G7.4.e`), y no es cola
mia: es la instruccion explicita de la `TAREA 4`.

---

**LA VUELTA 7 CIERRA. CINCO TAREAS CERRADAS (`G7.1` a `G7.5`, CON EL CIERRE EN `G7.6`), CERO PARADA
(`G7.6.h`), CERO INSERCION (`MODO_INSERCION=cuarentena`), DOS CAPITULOS NUEVOS MINADOS (`cap_18`,
`cap_19`), SEIS CANDIDATOS ESCRITOS Y SEIS ADUANAS EN EL ACTO CON `0 CAERIA`, DOS DISCUTIBLES MARCADOS Y
CERRADOS EN EL ACTO (`G7.3.d`), CINCO GUARDAS VERDES (`gate`, `guiones`, `tests`, tallado, censo, tras
sus correcciones declaradas en `G7.6.d` y `G7.6.e`), CERO AVERIA DE DATO (`G7.6.g`), DOS DEUDAS PAGADAS
(`d117`, `d110`), SALDO `40`/`38`.**
