
## W.4. TAREA 3: **LA COLA QUE SIGUE ABIERTA, PARA QUE NO SE PIERDA**

*El encargo la manda entera **porque ya se perdio una vez**: el remedio de la fase ciega cazo que
siete de ocho encargos de la `ACTA 25` no llegaron al encargo siguiente. **La recuento hoy fila a
fila con un instrumento**, no la copio.*

### W.4.a. **LA COLA ENTERA, RECONTADA CONTRA EL DATO Y NO CONTRA EL ENCARGO**

<!-- TALLADO: salida=.v30e/cola_cifras.txt -->

FILA_COLA_CIFRAS

**CUATRO FILAS SE CIERRAN HOY** (las dos series `D.37`, los `12` de `cap_07` con sus `77` pares, y las
`8` lineas `SIN HUELLA`), **una nace** (la arista `D.29` del plan de `cap_12`), y **el resto sigue
abierto con su cifra remedida.**

### W.4.b. **LAS `8` LINEAS `SIN HUELLA`, CERRADAS POR LA SEGUNDA SALIDA DE `D.15`**

*El encargo lo dice con estas palabras: `D.15` **da dos salidas, releerlas o declararlas, y hoy no hay
ninguna hecha**. Hoy hay las ocho.*

**POR QUE SE PODIAN CERRAR HOY Y NO ANTES, y es la mitad que explica la fila:** las ocho se emitieron
cuando **su vecino esperaba en la bandeja**, asi que la huella que guardaron es la de un nodo VACIO.
**Siete de esos ocho vecinos han entrado en esta misma vuelta o en la anterior**, asi que por primera
vez hay texto contra el que leer.

**LAS OCHO, UNA POR VEZ, CON `python forja.py anotar`**, que es la operacion que `EXTRACTOR.md` 14
deja para tocar una linea ya escrita sin tocarla a mano. **Ni una clase se cambio**: `anotar` no
toca la clase, ni el candidato, ni el vecino, ni las huellas, ni las señales.

<!-- TALLADO: parcial salida=.v30e/anotar_sin_huella.txt -->

    ANOTACION DECLARADA SOBRE UNA LINEA YA ESCRITA DE LA BITACORA
      sede : bitacora/VEREDICTOS.jsonl
      linea: 264
      veredicto: SANO (NO se toca)
      par      : centrar_debate_ideas_fuera_egos contra minimizar_impuesto_colaboracion_equipo
      la razon vieja SIGUE ENTERA: 412 caracteres, ninguno borrado
      se aniaden 498 caracteres al final de la razon
      lineas de la bitacora tocadas: 1 (la 264). Las otras 374, intactas.
    ANOTACION ESCRITA en bitacora/VEREDICTOS.jsonl, linea 264.

**Y LO COMPRUEBO POR DIFERENCIA EN VEZ DE CREERME LA SALIDA**, con la copia que guarde antes de la
primera anotacion:

<!-- TALLADO: parcial salida=.v30e/diff_sin_huella.txt -->

FILA_DIFF_SIN_HUELLA

**OCHO LINEAS TOCADAS Y `367` INTACTAS, Y SON EXACTAMENTE LAS OCHO QUE EL INSTRUMENTO NOMBRA.**

### W.4.c. **EL BLOQUE DE VIGENCIA ENTERO, CRUZADO CONTRA LA MARCA QUE LO DECLARA**

<!-- TALLADO: parcial salida=.v30e/vigencia_declarada.txt -->

FILA_VIGENCIA_DECLARADA

**`34` de `34` declarados, `0` sin declarar.** Los `26` `RANCIO` los declaro la vuelta 28 (`V.4.b`) y
los `8` `SIN HUELLA` los declaro esta.

> ### **Y AQUI VA UN HALLAZGO QUE NO ME GUSTA Y PUBLICO IGUAL** (`D.38.3` ensanchada)
>
> **La frase del instrumento no cambia: `python forja.py rancios` sigue imprimiendo `RANCIO 26, SIN
> HUELLA 8`, exactamente igual antes y despues de mis ocho anotaciones.** Las dos salidas estan
> guardadas y son comparables: `.v30e/rancios_apertura.txt` y `.v30e/rancios_tras_declarar.txt`.
>
> **`LECTURA`, en linea aparte y separada de la frase del instrumento: eso es correcto por diseño y
> aun asi deja un hueco.** Es correcto porque `anotar` **no toca las huellas** a proposito (*cambiar
> un veredicto es volver a juzgar el par, no anotar su linea*), y porque `D.15` dice que este bloque
> **no pone el gate en rojo**. **El hueco es que el instrumento no sabe distinguir una linea declarada
> de una que nadie ha mirado**, asi que la cifra `8` va a seguir saliendo igual la vuelta que viene y
> la siguiente. **La distincion existe en el dato** y la mide `.v30e/vigencia_declarada.py`, que lee
> el campo `anotaciones`. **Lo subo como propuesta en `W.7` y no me lo adjudico.**

### W.4.d. **LAS ENTRADILLAS DE ETAPA, MEDIDAS EN VEZ DE HEREDADAS**

*El encargo publica **`3` tramos** con texto y sin nodo, y dice que **no es caida de nadie: es cola**.
Lo mido, porque `cap_07` acaba de entrar entero y la cifra podia haberse movido.*

<!-- TALLADO: salida=.v30e/entradillas.txt -->

FILA_ENTRADILLAS

**`3` de `7` rotulos siguen sin nodo que los cubra, y son exactamente `LISTEN`, `CLARIFY` y `DEBATE`**,
que es lo que el encargo dice. **Los otros cuatro los cubre un nodo cuyo tramo declarado incluye la
linea del rotulo**, y tres de esos cuatro entraron hoy.

> **`LECTURA`: por que los cuatro cubiertos lo estan y los tres de cola no.** En `DECIDE`, `PERSUADE`,
> `EXECUTE` y `LEARN` la entradilla trae **procedimiento propio** y se pudo meter en los pasos de la
> primera pieza de su etapa (`persuadir_emocion_oyente_no_propia` lo dice en su propio
> `resumen_teorico`: *los pasos P1 a P3 vienen de la entradilla de la seccion, que ninguna otra pieza
> recoge*). **En `LISTEN`, `CLARIFY` y `DEBATE` la entradilla es cabeza de lista** (`L223`: *Here are
> some ideas that can help you...*), **y una cabeza de lista sin procedimiento propio no es un nodo**
> (`EXTRACTOR.md` 9). **Que no lo sea es justo lo que deja a sus piezas sin madre**, que es lo que
> este reporte ha tenido que escribir tres veces hoy en tres veredictos distintos.

### W.4.e. **LAS DOS FILAS QUE NO TOCO, Y DIGO POR QUE EN VEZ DE DEJARLAS CALLADAS**

| fila | por que no la toco |
|---|---|
| `cap_04` releido, **6** candidatos y **48** pasos | **la insercion se comio la vuelta**, que es el caso que el propio encargo previo. Trece candidatos por la aduana son **`26` corridas** (una para leer la cola, otra para insertar) a entre `63` y `136` segundos cada una. Releer `48` pasos mas contra su capitulo es una tarea cuarta, y **lo que la impide no es el tope de cinco sino el reloj** |
| el lote 5, **3** candidatos | **`D.39` lo dice por su letra** y el encargo lo repite: *no se toca hasta que el 4 cierre*. Sus `3` siguen en bandeja, **sin una sola insercion**, y eso se ve en la tabla de `W.4.a` |
| el hueco de transcripcion de `L153` | **sigue sin via, y con un solo ejemplar no se construye**, que es lo que la vuelta 28 ya declaro en su `V.6.a` y lo que el encargo repite. **No he encontrado un segundo ejemplar en esta vuelta**, y fabricar la via con uno solo seria maquinaria (`EXTRACTOR.md` 13) |
