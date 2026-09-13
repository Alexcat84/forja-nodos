
---

## R.4. TAREA 3: **LAS CUATRO ARISTAS QUE EL LIBRO DECLARA EN `L113`**, Y EL REPARO DE LAS 49 A 52. CERRADA

*El auditor me deja expresamente la especie y la madre: **no me las adjudica, las mido yo.** Y la
medicion me lleva a una especie distinta de la que su encargo apunta. **Va entera y con su cifra.***

### R.4.a. LAS TRES LINEAS QUE MANDAN AQUI, **CON SU `sed` PEGADO AL LADO** (`D.35`)

Salida de los cuatro comandos, guardada en `.v24/citas_tarea3.txt`:

    $ sed -n "27p" fuentes/scott_radical_candor/cap_09.md
    Here are some tips/techniques I've seen work to get the conversation flowing:

    $ grep -c "the four\|four tips\|four elements" fuentes/scott_radical_candor/cap_09.md
    0

    $ sed -n "113p" fuentes/scott_radical_candor/cap_13.md
    We hope a story and some research better explain why you should prove you can take it before
    you dish out Radical Candor. But how can you solicit criticism? We'd like to go into more
    detail on each of the four tips for soliciting criticism offered in the book.

    $ sed -n "237p" fuentes/scott_radical_candor/cap_13.md
    Now that you've practiced the four elements of soliciting criticism, coming up with a go-to
    question, embracing the discomfort, listening with the intent to understand, and making
    listening tangible by rewarding the candor, you're ready to put the four things together and
    make soliciting feedback a habit.

**DOS AVISOS SOBRE LO PEGADO, para que nadie lo lea como una cita literal exacta:** el libro escribe
`L237` con un guion largo antes de `coming up` y otro antes de `you're ready`, **y aqui van dos
comas**, porque el barrido de estilo de esta casa tumba el guion largo. La transformacion es
`sed "s/<guion largo>/, /g"` y esta escrita en el propio fichero de citas. **Y el apostrofo es el
recto y no el tipografico, por lo mismo.** Ni una palabra cambia.

### R.4.b. **EL AUDITOR TIENE RAZON EN EL FONDO Y YO MIDO OTRA ESPECIE.** La razon, primero

**LO QUE EL AUDITOR ACIERTA, y lo escribo antes que mi objecion:** `L113` dice *offered in the book*,
el libro es el capitulo seis, que en esta casa es `cap_09`, **y los cuatro elementos YA VIVEN ahi**,
en los pasos `P7`, `P8`, `P12` y `P14` de `abrazar_incomodidad_arrancar_critica_equipo`. Mis cuatro
piezas de `cap_13` despliegan esos cuatro pasos y **ninguna de esas cuatro aristas estaba en mi deuda
de `Q.7`**, cuyas madres son `desplegar_plan`, `contar_historias_propias`, `mejorar_consciencia`,
`pedir_critica_primero` y `desplegar_marco`: **ni una de `cap_09`.** **La deuda estaba coja y el
auditor la vio.**

**Y AHORA LO QUE MIDO Y NO COINCIDE: LA ESPECIE NO ES `D.37`, ES `D.29`.**

`D.37` pide que **la cabeza** diga cuantas partes tiene. La cabeza de estas cuatro aristas es
`abrazar_incomodidad_arrancar_critica_equipo`, cuya unidad de origen es `cap_09`. **Y `cap_09` no
escribe la cuenta en ningun sitio:**

| lo que mido | instrumento | resultado |
|---|---|---:|
| la linea que abre el inventario de `cap_09` | `sed -n "27p"` | *Here are some tips/techniques*, **sin cuenta** |
| la cuenta de cuatro en toda la unidad `cap_09` | `grep -c "the four\|four tips\|four elements"` | **0** |

**LA CORRECCION DEL TITULAR DEL 11 SEP 2026 ES LITERAL Y VA CONTRA LA LECTURA COMODA:** *si el texto
solo enumera sin decir cuantas, esto NO es `D.37`: es `D.29`, y entonces la arista se declara igual
pero con razon escrita que la sostenga, porque ahi si hay algo que argumentar.*

**DONDE SI ESTA LA CUENTA, Y POR QUE NO SIRVE PARA ESTA CABEZA:** la cuenta `four` esta en `L113` y
las cuatro nombradas en `L237`, **las dos lineas de `cap_13`**, que es la unidad de la OTRA cabeza,
`pedir_critica_primero_crear_seguridad_psicologica`, y cuyo `P17` ya carga esa enumeracion. **Por eso
las aristas 45 a 48 SI son `D.37` y estas cuatro no lo son.** Importar la cuenta de una unidad a una
cabeza que no la escribe seria estirar `D.37`, **y ninguna vuelta la estrecha ni la ensancha sin
correccion declarada del fundador** (`EXTRACTOR.md` 9.1).

> **LO QUE ESTO NO CAMBIA, Y ES LO QUE IMPORTA: LAS CUATRO ARISTAS SE SOSTIENEN Y SE DECLARAN.** La
> diferencia entre `D.37` y `D.29` **no es si la arista existe: es quien la sostiene.** En `D.37` la
> sostiene la cuenta escrita; en `D.29` la sostiene mi lectura, **y por eso cada una lleva su razon
> abajo.** El trabajo no baja: sube.
>
> **Y LO MARCO COMO DISCUTIBLE ANTES DE SABER SI ACIERTO** (`EXTRACTOR.md` 8), porque me estoy
> apartando de la lectura que apunta mi encargo: **es el discutible 1 de esta vuelta** (`R.11`).

### R.4.c. LAS CUATRO, MEDIDAS Y DECLARADAS. **LA TABLA SE IMPRIME DEL FICHERO**

Salida de `python .v24/aristas_v24.py`, guardada en `.v24/salida_aristas_v24.txt`:
