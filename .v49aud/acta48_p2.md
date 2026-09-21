
## 48.3. LA GUARDA QUE DECLARA MORDIENDO, VUELTA A MORDER POR MUTACION (cosecha `7.C`)

**La que su reporte declara mordiendo es la puerta de `D.39`**: `KK.0.a` la mide cerrada y de ahi
saca sus cero inserciones. La muerdo sobre una **copia**, sin tocar `config/`:

    $ ( cd .v49aud/mut && python puerta.py )    con grove anadido a cerrados_en_extraccion en la COPIA
    grove_high_output CERRADO EN EXTRACCION: True
    $ python .v48/puerta.py                     sobre el arbol de verdad, intacto
    grove_high_output CERRADO EN EXTRACCION: False
    $ git status --short -- config/
    (sin salida)

Ese bloque mide la puerta con la celda que la decide cambiada y sin cambiar, y comprueba que el
arbol de verdad no se movio. `LECTURA`: **la medida responde a su entrada, asi que la cifra que el
reporte publica es real y no una firma.**

**Y LO QUE NO ME CALLO, PORQUE `7.C` ME MANDA DECLARAR SI HAY CASO ROJO AUTOMATICO:**

    $ grep -rn "cerrados_en_extraccion" src/ forja.py hooks/ scripts/
    src/tablero.py:89:    for grupo in ("liberados", "cerrados_en_extraccion"):
    src/tablero.py:187:    cerrados = declarado.get("cerrados_en_extraccion") or {}

Ese bloque mide **quien lee esa llave en el codigo de la casa**.

`LECTURA`: **la lee el tablero y nadie mas.** Ni `forja.py` ni ningun modulo del camino de
insercion la consultan, asi que **NO HAY CASO ROJO AUTOMATICO: la puerta de `D.39` es una regla
que el extractor aplica a mano, no una guarda que tumbe sola.** Lo declaro aqui, que es
exactamente lo que `7.C` manda hacer cuando no hay nada que tumbar por su cuenta. **REGISTRO Y NO
ADJUDICO** (`D.56` congela la doctrina y `D.45` me veda `src/`), y lo anoto en `DEUDA.jsonl` para
que no se pierda.

## 48.4. LA RELECTURA CIEGA: **SEIS DISCUTIBLES MARCADOS, CINCO SE SOSTIENEN Y UNO CAE**

*Empiezo por los marcados, que es lo que `5.1` ordena. Los que pude clasificar sin el reporte los
lleve ya decididos de la fase ciega; los que dependian de el los cierro aqui con su instrumento.*

| # | el discutible, por su numero y su seccion | mi adjudicacion |
|---:|---|---|
| **1** | `KK.3.d`: corto la `TAREA 3` y no la `4` | **SE SOSTIENE.** El encargo autoriza el corte **en la pasada** con esas palabras, y la `TAREA 3` es la que se mide en pasadas. Rehice su aritmetica: quedaban `448` s utiles y la pasada mas barata del dia costo `559,4`. **Y su motivo es el bueno**: una tasa con `13` corridas es otra tasa, y `d024` nace parcial con sus restantes nombrados |
| **2** | `KK.2.e`: deja dentro de la ficha una cita que hoy no reproduce | **SE SOSTIENE, y la declaracion vale mas que el defecto.** Corri los dos `grep`: el citado da `3` porque la ficha pasa a contener la cadena, el preciso da `2`. **La afirmacion es cierta y reproducible; lo defectuoso es la linea del metodo.** Sede `cuarentena/`, que `d027` ya adjudico que **no es sede de `5.2`**: registra y no acumula. **La reparacion va ENCARGADA para la vuelta 50**, donde esa ficha pasa la aduana de todos modos y sale gratis |
| **3** | `KK.2.a`: la correccion confinada al `entregable_esperado` | **SE SOSTIENE, y lo compruebo campo a campo.** El defecto vive en el `entregable` y solo ahi: `titulo` y `condiciones_activacion` no publican cuenta, `denominaciones.nombre_largo` **enumera sin escribir el numero**, y ningun paso lo escribe. **Y la propia ficha da el motivo bueno, no el del experimento**: *tocarlo sin necesidad habria movido la cola de vecinos sin que ninguna deuda lo pidiera*, con `src/aduana.py` linea `278` citada **correctamente** |
| **4** | `KK.4.b`: cruza su banda con el punto `1` de `6` | **SE SOSTIENE, porque el mismo escribe que no es un contraste formal.** Y traigo la discrepancia que me toca declarar y no resolver copiando: **mi apertura publico `39,3`, `13,9` y `10,9` por ciento** (cota exacta de una cola, Clopper y Pearson) **y el publica `16,11`** (Wilson a dos colas). **Las dos son correctas bajo su metodo y NO son comparables entre si** |
| **5** | `KK.5.e`: su lectura del censo | **CAE.** Ver `48.6.a` |
| **6** | `KK.1.a`: la columna `nodo(s)` es pronostico de la frontera y no lo minado | **SE SOSTIENE, y lo cierro mas fuerte que el.** El lo deducia de dos filas; yo lo cuento entero: la columna pronostica **`22`** nodos sobre `44` tramos y la bandeja tiene **`19`** fichas de `cap_04`. **La diferencia es `3`, que son exactamente `P41`, `P42` y `P44`**, los tres que `47.5.d` manda a la vuelta 50 |

    $ python .v49aud/26_discutibles.py     (la mitad que cierra el discutible 6)
    tramos de la frontera             : 44
    nodos PRONOSTICADOS por la columna: 22
    fichas de cap_04 en la bandeja    : 19
    diferencia                        : 3

Ese bloque suma la columna `nodo(s)` de los `44` tramos y la compara con las fichas de `cap_04`
que hay en la bandeja.

**DENTRO CONTRA FUERA DEL MARCADO** (`5.3`, y es la cifra que mueve el credito): **`1` caida
DENTRO del marcado de `6`, `0` FUERA.** La unica caida del reporte es la que el mismo puso en su
lista antes de saber si acertaba, **que es justo lo que la metrica quiere premiar**: el extractor
sabia donde estaba su duda.

## 48.5. LAS ADJUDICACIONES

### 48.5.a. **`8` DE LAS `19` FICHAS DE `cap_04` DECLARAN PALABRAS QUE NADIE REPRODUCE**

**Mi fase ciega lo trajo como hallazgo y dijo que solo se cerraba contra la tabla de frontera, que
vive en el reporte. Hoy lo cierro.**

    $ python .v49aud/25_de_donde_sale_la_cifra.py
    ficha                                                pieza rango declarado   dice cuento  que rango daria la cifra declarada
    buscar_actividad_alta_palanca_tres_vias              P19   L203  a L213     118     76  L196 a L213
    detectar_palanca_negativa_actividad_mando            P21   L219  a L219      73     73  -- cuadra --
    detectar_palanca_negativa_actividad_mando            P24   L231  a L235     356    356  -- cuadra --
    elegir_momento_actividad_palanca_maxima              P20   L215  a L217     297    237  ninguno cercano
    empujar_persona_reunion_direccion_preferida          P13   L167  a L167     174    147  ninguno cercano
    escalonar_fuentes_informacion_gerencial              P9    L153  a L153     208    183  ninguno cercano
    programar_visita_area_observar_despachar             P10   L155  a L157     337    236  ninguno cercano
    reunir_informacion_gerencial_vias_variadas           P7    L145  a L147     356    210  ninguno cercano
    subir_productividad_gerencial_tres_vias              P18   L195  a L201      62     60  ninguno cercano
    transmitir_objetivos_prioridades_preferencias        P11   L159  a L159     197    160  ninguno cercano

    piezas declaradas leidas: 10 ; cuadran 2 ; discrepan 8

Ese bloque cuenta las palabras del rango de lineas que cada ficha declara dentro de su propio
`resumen_teorico`, las compara con la cifra que esa misma ficha escribe, y busca si algun rango
vecino daria la cifra declarada.

**Y LA FRONTERA QUE ESAS OCHO FICHAS CITAN DICE LO QUE DIGO YO, no lo que dicen ellas:**

    $ sed -n '43941p;43943p;43944p;43945p;43947p;43952p;43953p;43954p' docs/loop/REPORTE.md
    | L145 a L147 | 210 | 1 | P7  LAS VIAS POR LAS QUE LLEGA LA INFORMACION...
    | L153 a L153 | 183 | 1 | P9  LA JERARQUIA DE LA INFORMACION...
    | L155 a L157 | 236 | 1 | P10 LA VISITA AL SITIO...
    | L159 a L159 | 160 | 1 | P11 transmitir objetivos, prioridades y preferencias...
    | L167 a L167 | 147 | 1 | P13 EL EMPUJON...
    | L195 a L201 |  60 | 1 | P18 CABEZA DE SERIE: las TRES vias de subir la productividad gerencial...
    | L203 a L213 |  76 | 1 | P19 CABEZA DE SERIE: las TRES vias basicas de la actividad de alta palanca...
    | L215 a L217 | 237 | 1 | P20 la palanca depende de CUANDO...

Ese bloque imprime ocho filas de la tabla de frontera de `cap_04` publicada en la vuelta 46
(`HH.2.c`), que es la frontera que esas ocho fichas nombran dentro de si mismas.

`LECTURA`: **las ocho fichas contradicen a la frontera que citan, y mi recuento coincide con la
frontera en las ocho.** Y no es una forma distinta de contar: probe el recuento por espacios, por
palabras alfanumericas y por caracteres, **y ninguno da esas ocho cifras**; y probe todos los
rangos contiguos del capitulo entero, **y solo `P19` encuentra uno** (`L196 a L213`), que no es el
que la ficha declara. **Son ocho numeros escritos a mano.** Las dos que cuadran (`P21` y `P24`)
son las de la ficha que NO nace de ese molde, y **las tandas de las vueltas 47 y 48 cuadran todas
al digito**, medido en mi fase ciega.

**ADJUDICO, Y EN TRES PIEZAS:**

1. **NO ES CAIDA DE ESTA TANDA.** Las ocho se escribieron en la **vuelta 46**; esta vuelta toco
   dos fichas y solo una de ellas es de las ocho (`P7`), en un campo distinto. **Una racha cuenta
   tandas, y esta tanda no las escribio.**
2. **NO ES `CIFRA PUBLICADA`**, porque la sede es `cuarentena/<libro>/<id>.json` y `d027` ya
   adjudico que **una ficha de cuarentena no es sede de `5.2`**, recogido en la `ACTA 47`.
3. **PERO SE PAGA ANTES DE LA INSERCION, Y ESO SI ES MIO DE ENCARGAR.** Las `19` fichas entran al
   grafo en la vuelta 50, y en cuanto entren esas ocho cifras dejan de estar en la bandeja. **Es
   la enfermedad que el protocolo nombra en su propia cabecera** (*la vara es el instrumento,
   nunca un campo declarado a mano*), y el remedio es de una linea por ficha: **escribir el numero
   que la frontera publica, por correccion declarada y sin borrar el viejo.** Va en la `TAREA 2`
   del encargo y queda anotado en `DEUDA.jsonl`.

**Y LO QUE ESTO NO TUMBA, dicho para que no se lea de mas:** no tumba ninguna de las dos
correcciones de esta vuelta, que van por otro sitio y las verifique contra el libro; no tumba el
`0` `PUENTE` de `cap_04`, que es sobre pasos y no sobre palabras; y no tumba la tabla de frontera
de `HH.2.c`, **que es precisamente la que sale bien.**

### 48.5.b. **LO DEMAS QUE ADJUDICO, SIN REABRIR LO QUE YA ESTABA ADJUDICADO**

| # | lo que adjudico | con que |
|---:|---|---|
| `a` | **el cierre corto de `d024` en `2` de `3` es correcto y esta DECLARADO con sus tres piezas**: el numero, el reloj y los `5` que quedan nombrados uno a uno | `EXTRACTOR.md` 12.4 me manda verificar que el cierre corto se declare, **y se declara** |
| `b` | **`d024` sigue abierta y tiene que seguirlo.** Pasa de `7` sin medir a `5` sin medir, y son `5` y no `4` porque el tramo cerro en `2` | el encargo lo fijo por adelantado y `scripts/deuda.py` la lista viva |
| `c` | **`d033` NO se marca pagada aunque su tarea cerro, y hace bien**: su propio `KK.4.d` escribe que la condicion de la roja observada, el arbol en movimiento, **no se ha reproducido** | su registro sigue vivo en `scripts/deuda.py`, y `KK.4.d` razona contra su propio interes |
| `d` | **la propuesta de saltarse el recalculo cuando el `sha1` del texto de las seniales no cambia queda RECOGIDA Y NO ADJUDICADA**: vive en `src/` y `D.45` la deja fuera de toda sesion en paralelo. **Es parada de `src/`, no parada de bucle** | `D.45`, y `48.2.c` verifica que la medida que la sostiene es correcta |
| `e` | **su lectura de `KK.2.d` es correcta y la FIRMO**: las dos especies de correccion no son la misma cosa. La que no toca el texto de las seniales es **inutil de recalcular y cara de correr**, y esta demostrado con su `sha1`, no supuesto | `48.2.c` |
| `f` | **`cap_04` cierra en la vuelta 50 con `P41`, `P42` y `P44`, y NO se salta a `cap_05`**, aunque `forja.py tablero --puedo` diga *continuar desde el capitulo siguiente al ultimo minado*. **Esa es la trampa que la `ACTA 45` desenterro y sigue viva**: es `d028`, y `D.45` la deja fuera de mi alcance | `47.5.d`, y `48.4` fila `6` mide que faltan exactamente `3` |
| `g` | **la colision de `D.52` se volvio a pagar a mano por quinta vez y el sello es el bueno**: las dos huellas `9bf10e67...` que compare en la fase ciega salen de `git hash-object`, **sin leer una sola celda de ninguna de las dos tablas** | `d030`, que `D.45` tambien deja fuera de mi alcance |
| `h` | **su `KK.5.f` nombra a `d024` y a `d031` como no pagadas y omite a `d033` de esa lista.** No es caida: el registro esta bien y la aritmetica de `16` a `14` lo hace inferible, pero **una lista de lo que NO se paga que deja fuera una de las tres se lee mal**, y lo dejo escrito | `scripts/deuda.py`, que las lista vivas las tres |
