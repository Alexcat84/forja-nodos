# -*- coding: utf-8 -*-
"""Anexa la seccion DC.5 (TAREA 2, la fidelidad D.30) al reporte."""
import io


def leer(p):
    return io.open(p, encoding='utf-8').read().rstrip('\n')


def sangrar(t, n=4):
    return '\n'.join((' ' * n + l) if l.strip() else '' for l in t.split('\n'))


fid = leer('.v40/fidelidad.txt')
tabla = leer('.v40/fidelidad_tabla.txt')
clase = leer('.v40/clase.txt')
deno = leer('.v40/denominador.txt')

corte = tabla.rindex('LA CUENTA, SALIDA DE LA MISMA TABLA:')
tabla_filas = tabla[:corte].rstrip()
tabla_cuenta = tabla[corte:].strip()

bloque = u"""
## DC.5. **TAREA 2, BLOQUEANTE: LA FIDELIDAD `D.30` DE LOS CUATRO, ANTES DE LA PRIMERA INSERCION**

`EXTRACTOR.md` 15.4. **Son `58` pasos** (`12` mas `13` mas `20` mas `13`) **releidos contra su linea del
libro, no contra el grafo.** El encargo me avisa de que estos cuatro **no vienen releidos** como los tres
de la vuelta 39, y de que un `0` aqui valdria mas. **Lo doy medido y no por hecho.**

### DC.5.a. **EL DENOMINADOR, CONTADO DEL DATO Y NO COPIADO DEL ENCARGO**

<!-- TALLADO: script=.v40/denominador.py salida=.v40/denominador.txt -->

    $ python .v40/denominador.py
{deno}

**`cap_13` entero da `12` candidatos y `212` pasos, al digito contra lo que el encargo publica, y mi
tramo da `4` y `58`.** Los `8` restantes suman `154` pasos **que yo no he releido en esta vuelta**, y por
eso **la fila del capitulo no la firmo**.

### DC.5.b. **LOS `58` PASOS BAJO SU LINEA, CON EL `sed -n` PEGADO** (`D.35`)

**Las `20` lineas distintas del libro que cubren los `58` pasos van pegadas enteras**, y cada paso va
debajo de la suya. **El instrumento comprueba ademas que el reparto no deja hueco ni solape**: un paso
que no caiga en ningun tramo, o que caiga en dos, salta ahi.

> **LOS CUATRO GUIONES LARGOS DE `L197` Y `L237`, DECLARADOS Y NO ESCONDIDOS.** El barrido de esta casa
> tumba el commit si uno entra, y la vuelta 35 resolvio un caso igual **cortando la cita**. **Aqui no se
> corta**: cortar `L197` perderia `off the hook`, que es lo que sostiene su `P12`, y cortar `L237`
> perderia la enumeracion de los cuatro elementos, que es lo que sostiene el `P06` del cuarto candidato.
> **El instrumento sustituye cada guion por su token entre corchetes, los cuenta, y lo publica en su
> ultima linea: `4` en `2` de las `20` lineas.** Ni una palabra del libro se pierde.

<!-- TALLADO: script=.v40/fidelidad.py salida=.v40/fidelidad.txt -->

    $ python .v40/fidelidad.py
{fid}

### DC.5.c. **LA CLASE QUE SE RELEE ENTERA, MARCADA POR INSTRUMENTO Y NO A OJO**

<!-- TALLADO: script=.v40/clase.py salida=.v40/clase.txt -->

    $ python .v40/clase.py
{clase}

**`42` de los `58` caen en la clase** (persona, cuenta, escalon o adjetivo de sentimiento) **y los `42`
se releyeron con su linea completa delante.** La expresion hereda la de `.v39/clase.py` y **la amplia con
el vocabulario propio de estos cuatro** (`Rick`, `Hanson`, `Sara`, `Blakely`, `Spanx`, `Hawai`,
`Resilient`, `Velcro`, `Teflon`, `enfadado`, `defensiva`, `amenazante`, `agradecimiento`, `invisible`,
`ignorada`, `antinatural`), **y lo digo en el propio fichero**: ampliar la expresion solo puede SUBIR esa
cuenta, nunca bajarla.

**Y LA CUENTA HONESTA ES OTRA Y ES MAYOR: los `58`.** Las `20` lineas del libro las lei **enteras las
`20`**, porque `58` pasos repartidos sobre `20` lineas significa que leer entera cada linea cubre todos
los pasos. **El `42` es lo que el instrumento marca; el `58` es lo que de verdad relei.**

### DC.5.d. **EL LIBRO MAYOR DE LA RELECTURA: UNA FILA POR PASO**

<!-- TALLADO: script=.v40/fidelidad_tabla.py salida=.v40/fidelidad_tabla.txt -->

{tabla_filas}

<!-- TALLADO: parcial salida=.v40/fidelidad_tabla.txt -->

{cuenta}

> ## **`58` PASOS, `58` `TRANSCRIPCION`, `0` `PUENTE`. Y ESE `0` LO FIRMO YO.**

**LA COLUMNA DEL VEREDICTO ES LO UNICO QUE TECLEA LA LECTURA**, y el instrumento lo dice en su cabecera:
un paso ausente del diccionario `VEREDICTOS` queda `TRANSCRIPCION`, y **cada `PUENTE` tendria que traer
su motivo escrito**. **El diccionario esta vacio porque no encontre ninguno**, no porque no lo mirase.

**LAS TRES ESPECIES DE PUENTE QUE `D.30` NOMBRA, BUSCADAS UNA A UNA:**

| especie | lo que busque | que salio |
|---|---|---|
| **el destinatario** | un paso que mande trasladar, informar o escalar a alguien que el libro no nombra | **ninguno**. `L227` nombra la reunion de equipo y `L245` nombra al equipo, y son los dos unicos destinatarios que aparecen |
| **el periodo** | un paso que fije cada cuanto, en cuanto tiempo o durante cuanto | **ninguno inventado**. Los cuatro periodos que aparecen son del libro: `cada semana` de `L111`, `tres minutos` de `L209`, `en la ultima semana` de `L227` y `las primeras veinte o asi` de `L241` |
| **el responsable** | un paso que escriba quien responde de algo | **ninguno**. Todos los pasos hablan en segunda persona a quien pide la critica, que es el sujeto del libro |

**Y LOS CUATRO SITIOS DONDE LOS CANDIDATOS DICEN LO QUE EL LIBRO NO DICE, que es la cara positiva de lo
mismo:** cada `resumen_teorico` cierra con un tramo *LO QUE EL TEXTO NO DICE Y POR ESO NO ESTA AQUI*, y
ahi estan **cuanto se espera antes de volver a preguntar**, **cada cuanto se repite el ejercicio de los
tres minutos**, **cada cuanto se cuenta en publico** y **cuanto tiempo del final de la reunion se
reserva**. **Son exactamente los puentes que no se escribieron.**

### DC.5.e. **MIS DISCUTIBLES, MARCADOS ANTES DE INSERTAR NADA Y ANTES DE SABER SI ACIERTO** (`EXTRACTOR.md` 8)

| # | el discutible | lo que decido, y por que |
|---:|---|---|
| **1** | **la cifra de `DC.2.d`**: el comando que el nodo publica da `0` sobre `e3950c6`, `4` sobre mi apertura y `9` con mi correccion ya dentro | **lo declaro con sus tres cortes y no lo resuelvo.** Roza la pregunta `4` de la cola de doctrina y el encargo dice que esta vuelta no sube ninguna. **Si el auditor lee que una cifra con corte escrito tenia que haberse evitado del todo, la caida es mia** |
| **2** | **`abrazar_incomodidad` `P06`** escribe *lo que el texto ha medido en sus talleres*, y `L191` dice que los participantes ponen cara de extranieza y que se les encienden las bombillas: **el libro OBSERVA, no MIDE** | **lo dejo `TRANSCRIPCION`**: el contenido del paso, *parece facil y hace falta una disciplina enorme*, es literal de `L191`, y el verbo de marco no aniade objeto, destinatario, periodo ni responsable. **Pero el verbo es mio y por eso va aqui** |
| **3** | **`premiar_franqueza` `P05`** escribe *la directora de Spanx, Sara Blakely* donde `L221` escribe `Spanx CEO Sara Blakely`, y la grafia de esta casa para ese escalon es **consejero delegado**, recien reafirmada en `DC.2` | **lo dejo como esta y no toco el paso.** `EXTRACTOR.md` 15.1 es regla de **id**, no de prosa de paso, y *directora* dice lo que el libro dice. **Si la grafia de la casa manda tambien dentro del paso, esto es una caida y la cargo** |
| **4** | **`premiar_franqueza` `P04`** cita a `Rick Hanson`, autor de `Resilient`, con su frase entera, y la ficha **no lleva campo `atribuciones`**, que `70` nodos del catalogo si llevan | **no lo aniado.** `EXTRACTOR.md` 9 manda `atribuciones` para la **CIFRA del autor**, y esto es una **metafora**, no una cifra con banda ni fecha de corte. **Si la vara cubre tambien la cita literal, falta un campo y es mio** |
| **5** | **`integrar_peticion` se lleva `L111`, a `124` lineas de su rotulo `L235`** | **lo sostengo.** Es el mismo objeto que `L239` y `P.19` manda fundirlo en vez de fabricar el gemelo de su donante; la frontera no contigua **va publicada en su `resumen_teorico` antes de cortar**, que es `EXTRACTOR.md` 10 |
| **6** | **`premiar_franqueza` mete DOS ejercicios rotulados en UN nodo**, `Practice: Make Listening Tangible` de `L223` y `Practice: Reward criticism you disagree with` de `L231` | **lo sostengo con la vara de la `ACTA 20` 4.1**: una condicion de activacion y un entregable compartidos, y el segundo es el caso dificil del primero. **Si la vara los separa, es un nodo de mas y es mio** |
| **7** | **`premiar_franqueza` `P15` deja fuera el ejemplo de `L229`**, las reuniones vueltas barra libre por evitar interrumpir | **lo dejo fuera.** Es omision de un ejemplo, no invencion, y la casa no obliga a transcribir cada ejemplo. **Si el criterio es transcribir el inventario entero, falta un paso** |
| **8** | **el `SANO` de `integrar_peticion` contra la cabeza** ya esta escrito dos veces, en mi linea `488` y en la apertura sellada del auditor | **no lo peleo, lo escribo y sigo**, que es lo que la `TAREA 3.B` manda. **Al leer sus `13` pasos no discrepo**: `L237` lo pone DESPUES de los cuatro y `D.37` dice que un hermano de serie es `SANO` |
| **9** | **los `2` `SANO` rancios de `DC.3`**, que declaro vigentes por medicion de campos y no por relectura del par entero | **la medicion dice que titulo, pasos y entregable son identicos al digito**, y eso es mas fuerte que mi memoria del par. **Si `D.15` pide releer el par entero y no medir el nodo, la caida es mia** |
"""

bloque = bloque.format(
    deno=sangrar(deno),
    fid=sangrar(fid),
    clase=sangrar(clase),
    tabla_filas=tabla_filas,
    cuenta=sangrar(tabla_cuenta),
)

with io.open('docs/loop/REPORTE.md', 'a', encoding='utf-8') as f:
    f.write(bloque)
print('OK, DC.5 anexada')
