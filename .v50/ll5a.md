
## LL.5. TAREA 5. **EL CIERRE, CON LAS MISMAS PIEZAS DE SIEMPRE**

### LL.5.a. **EL ESTADO AL CIERRE, RECOMPUTADO AL CIERRE Y NO COPIADO DE LA APERTURA** (`EXTRACTOR.md` 4)

<!-- TALLADO: parcial salida=.v50/cierre_estado.txt -->

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1087 total
    $ ls cuarentena/grove_high_output/*.json | wc -l
    44
    $ ls cuarentena/_insertados/grove_high_output/*.json | wc -l
    1
    $ grep -l "unidad Cap. 3" cuarentena/grove_high_output/*.json | wc -l   (las fichas de cap_04)
    22

**LAS CUATRO CIFRAS QUE EL ENCARGO FIJO POR ADELANTADO, Y LAS CUATRO SALEN:**

| lo que el encargo predijo en su `TAREA 5.3` | lo medido al cierre | |
|---|---:|---|
| `cuarentena/grove_high_output/` pasa de `41` a **`44`** | **`44`** | **sale** |
| `dataset/nodos.jsonl` sigue en **`346`** | **`346`** | **sale** |
| `bitacora/VEREDICTOS.jsonl` sigue en **`740`** | **`740`** | **sale** |
| `config/pares_mutuos.jsonl` sigue en **`1`** | **`1`** | **sale** |

**LAS TRES QUE TENIAN QUE QUEDARSE QUIETAS SE QUEDARON QUIETAS**, que es lo que el encargo llamaba
*la caida que buscar*: **esta vuelta no inserto**, asi que **ni un veredicto nuevo, ni un nodo
nuevo en el grafo, ni un par mutuo nuevo.** Las nueve fichas corregidas en `LL.3` **siguen en la
bandeja**: corregir una ficha no la mueve de sitio.

### LL.5.b. **LOS ARBOLES QUE NO PODIA TOCAR, MEDIDOS POR DIFERENCIA Y NO PROMETIDOS** (`D.45`)

<!-- TALLADO: parcial salida=.v50/arbol_intacto.txt -->

    $ git status --short -- src/ tests/ scripts/ dataset/ forja.py hooks/ config/ bitacora/ censos/ docs/BANCO_DE_REGLAS.md
    (sin salida: ninguno de esos arboles cambio en esta vuelta)

**`src/` ENTRA EN ESA LISTA Y SALE LIMPIO, Y ESO ES LO QUE HACE VERIFICABLE LO DE `LL.2.a`:** corri
`forja.py tablero`, `forja.py informe`, `forja.py gate`, `forja.py guiones` y la suite entera, y
**no toque ni un byte de ninguno de esos arboles.** `d028`, `d030` y `d037` siguen abiertas por eso
mismo.

### LL.5.c. **LA COLISION DE `D.52` CON `D.41`, PAGADA A MANO POR SEXTA VEZ SEGUIDA** (`d030`)

**Al escribir mi tabla en la ruta viva dejaba en rojo la de la vuelta 49 sin tocar ni una celda de
su reporte.** La salida de la vuelta 49 **se saco de git byte a byte y se archivo**, y la linea de
`KK.5.c` pasa a nombrar la copia archivada con su correccion declarada al lado.

<!-- TALLADO: parcial salida=.v50/sello_v49.txt -->

    $ git show HEAD:docs/loop/TABLA_DE_CIERRE.txt | git hash-object --stdin
    f33c8d9cb7f3b639a5aec81cc8ec2d26782d8631
    $ git hash-object docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v49.txt
    f33c8d9cb7f3b639a5aec81cc8ec2d26782d8631

**EL MISMO `hash-object` ANTES Y DESPUES: la copia es la salida, no una transcripcion.** `42`, `46`,
`47`, `48`, `49` y hoy la `50`: **sexto ejemplar seguido**, y eso es lo que la hace deuda de
maquinaria y no descuido. `d022` y `d030` la tienen abierta y `D.45` me deja fuera de arreglarla.
