# ENCARGO DEL LOTE 2, ARCHIVADO SIN EJECUTAR (10 sep 2026)

> **ARCHIVADO POR EL AUDITOR AL CERRAR LA VUELTA 3**, con el ACTA 3 delante.
>
> Este es el texto integro de `docs/loop/PROMPT_SIGUIENTE.md` tal y como Alexis lo
> escribio en el commit `db88620`, **sin tocarle una palabra al cuerpo.** Lo unico
> añadido es esta cabecera.
>
> **POR QUE ESTA AQUI.** La vuelta 3 corrio contra este encargo y se detuvo en sus
> dos condiciones de apertura: `fuentes/smart_who/` no existe y la clave
> `smart_who` no esta en `fuentes/FUENTES_CANONICAS.json`. El ACTA 3 declara
> PARADA por DECISION DE ALEXIS, **y una parada exige `PROMPT_SIGUIENTE.md`
> vacio**, que es la mitad ejecutable de la parada.
>
> **Vaciarlo habria borrado un encargo que nadie ha ejecutado y que sigue siendo
> valido entero.** Asi que se archiva aqui: **retomar es copiar de vuelta, no
> volver a escribir.**
>
>     cp docs/loop/paradas/2026-09-10-encargo-lote-2-sin-libro.md docs/loop/PROMPT_SIGUIENTE.md
>     (y se le quita esta cabecera)
>
> **LO UNICO QUE HAY QUE AÑADIRLE AL RETOMARLO** es la adjudicacion favorable del
> ACTA 3 seccion 3.6: **la comprobacion de las dos condiciones de apertura se
> publica como su propia linea del reporte, antes de la TAREA 1.** Esta vuelta
> las comprobo por suerte y no por regla, porque estaban escritas arriba del todo.
>
> **El bucle NO esta detenido por este fichero:** vive en `docs/loop/paradas/` y
> el arnes solo mira `docs/loop/PARA_ALEXIS.md`.

---

# ENCARGO DEL LOTE 2: `smart_who`, 7 capitulos, DOS POR VUELTA

*Escrito por **Alexis** el 10 sep 2026, con el `docs/CIERRE_LOTE_1.md` delante.
`docs/loop/PROMPT_SIGUIENTE.md` es sede del auditor en el curso normal
(`EXTRACTOR.md` seccion 14); **lo escribe el fundador cuando abre un lote nuevo**,
como ya paso en la vuelta 1.*

---

## ANTES DE NADA: LAS DOS CONDICIONES QUE NO DEPENDEN DE TI

**1. EL LIBRO TIENE QUE ESTAR EN LA MAQUINA.** Este encargo no sirve de nada sin

    fuentes/smart_who/cap_01.md ... cap_07.md

**`fuentes/*/` esta fuera de git a proposito** (texto con derechos de otro autor),
asi que **el material no llega por `git pull`: lo pone Alexis a mano.** Si al
empezar esa carpeta no existe o esta vacia, **no improvises: declaralo en tu
reporte y detente.** No es una parada de doctrina: es que falta la materia prima.

**2. LA FUENTE CANONICA, ANTES DEL PRIMER NODO.** La clave `smart_who` **no esta**
en `fuentes/FUENTES_CANONICAS.json`. **La registra Alexis con la ficha del libro
delante**, no tu, y la aduana rechazara tu primer candidato hasta que este. **Ese
rechazo es deliberado** (manual seccion 7.1).

---

## LO QUE HA CAMBIADO DESDE TU ULTIMA VUELTA, Y ES MUCHO

**LEE `docs/loop/EXTRACTOR.md` ENTERO Y `docs/CIERRE_LOTE_1.md`.** El lote 1
cerro, **sus seis nodos ESTAN EN EL GRAFO**, y dejo cuatro reglas nuevas en el
banco que te obligan.

| | |
|---|---|
| nodos vivos en el dataset | **8** (eran 2) |
| aristas declaradas | **2** |
| veredictos en bitacora | **2** |
| fuentes canonicas en uso | **2** |

**`D.30` ES LA QUE MAS TE CAMBIA EL TRABAJO, y esta en `EXTRACTOR.md` seccion
15.4.** El lote 1 midio que **13 de sus 36 pasos los habia escrito el extractor y
no el libro**, y que **la aduana dio 6 de 6 verdes antes y despues de
corregirlos.**

> **NINGUNA GUARDA DE ESTA CASA VE UN PASO QUE TU ESCRIBISTE Y EL LIBRO NO DICE.**
> Un informe verde certifica que la ficha esta bien construida, **no que sus pasos
> sean del libro.**

**Las otras tres:** `D.27` la prueba del inventario con sus tres restricciones,
`D.28` la sede de `PARA_ALEXIS.md`, `D.29` la arista que la señal no levanta.

---

## EL PROTOCOLO DE CANDIDATO, CON LA RELECTURA DE FIDELIDAD DENTRO

**ESTE ES EL CAMBIO DE ESTE LOTE.** En el lote 1 la relectura se hizo en una
vuelta posterior y **costo una vuelta entera**. Aqui va **dentro del acto de
escribir**, y el ciclo por candidato tiene cinco pasos y no tres:

    1. escribes el candidato en cuarentena/smart_who/<id_propuesto>.json
    2. RELECTURA DE FIDELIDAD, con el parrafo delante:
         marcas cada paso como TRANSCRIPCION o como PUENTE
         cada PUENTE se retira o se reescribe, citando el parrafo que NO lo dice
    3. python forja.py informe cuarentena/smart_who/<id>.json
    4. si CAERIA, lo corriges y vuelves al 3
    5. solo entonces cuenta como escrito

**EL PASO 2 VA ANTES QUE EL 3 Y NO ES INTERCAMBIABLE.** La aduana no puede
ayudarte ahi: **no tiene el libro delante.** Si dejas la relectura para despues
del informe, el informe verde te va a decir que todo esta bien **y va a tener
razon en lo suyo.**

**LA TABLA DE MARCADO VA EN TU REPORTE**, no dentro del JSON: un candidato con
`TRANSCRIPCION` escrito dentro seria un nodo que habla de su propia extraccion.

**LAS TRES ESPECIES DE PUENTE QUE EL LOTE 1 PAGO**, y son las que vas a volver a
escribir sin darte cuenta:

| especie | ejemplar |
|---|---|
| **el destinatario** | *traslada el expediente a la autoridad*, donde el libro solo alienta a vigilar |
| **el periodo** | *fija cada cuanto se examina*, donde el libro dice *periodicamente* |
| **el responsable** | *escribe quien responde de cada regla*, donde el libro pone tres etapas y ningun responsable |

**Y EL AVISO QUE DICE DONDE MIRAR:** en el lote 1 el parrafo mas rico dio **0 por
ciento** de puentes y el mas pobre dio **83 por ciento**. **Un parrafo pobre no
produce un nodo pobre: produce un nodo inventado.** Cuando el inventario del libro
sea delgado, **desconfia de tus propios pasos.**

---

## EL RITMO DEL LOTE

**`smart_who` son 7 capitulos y 44.324 palabras: veinticinco veces el lote 1.**
Sus capitulos promedian **6.332 palabras**, contra las 439 de `onu_consumidor`.

> **UN CAPITULO DE ESTE LIBRO NO ES UN APARTADO DE LA ONU.** No es un fallo tuyo
> si el segundo no cabe: es la primera vez que esta casa mide un capitulo de
> verdad, y la vuelta se dimensiono sin ese dato.

- **DOS CAPITULOS POR VUELTA** *(decision del fundador, 10 sep 2026)*. El lote 1
  corrio a uno; este sube a dos, y el lote 3 se decide con la cifra que dejes
  (ver **la regla de volumen** mas abajo).
- **Y LOS DOS CAPITULOS NO SE MEZCLAN NUNCA.** Ver **la unidad atomica**, que es
  la parte de esta decision que no se puede negociar.
- **Si el segundo no cabe, cierras el primero entero y lo dices**: reporte
  parcial, nunca vacio. **Un capitulo cerrado vale mas que dos a medias.**
- **TRAMO: entre cinco y quince candidatos por vuelta** (seccion 12). Si el
  primer capitulo ya llena el tramo, **el segundo no se empieza**, y eso no es un
  fallo: es el tramo funcionando.
- **UN COMMIT POR CAPITULO** (seccion 17), con los JSON dentro, y el mensaje dice
  que capitulo y cuantos candidatos. **Dos capitulos son DOS commits.**
- **AL CERRAR CADA CAPITULO:** `python forja.py informe --carpeta cuarentena/smart_who`
  y pegas el saldo.

### LA UNIDAD ATOMICA ES EL CAPITULO, y de esto depende la medida

> **CADA CAPITULO SE LEE Y SE CORRIGE ENTERO, DE PRINCIPIO A FIN, ANTES DE ABRIR
> EL SIGUIENTE. NUNCA LOS DOS JUNTOS.**

Es decir: frontera del `cap_N`, candidatos del `cap_N`, relectura de fidelidad del
`cap_N`, informe del `cap_N`, **commit del `cap_N`**. Y solo entonces el `cap_N+1`.

**LAS DOS RAZONES, y la segunda es la que manda:**

1. **Un capitulo cerrado sobrevive a que la vuelta se corte.** Dos a medias no
   dejan ninguno.
2. **LA CIFRA QUE ESTA VUELTA EXISTE PARA MEDIR ES POR CAPITULO.** Si lees los
   dos juntos y corriges al final, ya no sabes cual de los dos produjo cada
   puente, **y la medida se pierde para siempre**: no se puede reconstruir
   despues. Mezclarlos no es ir mas rapido, es correr la vuelta sin su
   instrumento.

### LA REGLA DE VOLUMEN, que decide el lote 3

*Decision del fundador, 10 sep 2026.* **El auditor publica en cada acta la cifra
`PASOS INVENTADOS POR CAPITULO`**, y de ella sale el tamaño del lote siguiente:

| lo que mida este lote | el lote 3 corre a |
|---|---|
| **se mantiene o baja** respecto al **36 por ciento** del lote 1 | **TRES capitulos por vuelta** |
| **sube** respecto al 36 por ciento | **UNO. El techo baja** |

**LA CIFRA ES POR CAPITULO Y NO POR VUELTA, y por eso la unidad atomica no es un
capricho:** una media de vuelta esconderia un capitulo limpio detras de uno malo.
**La escalada se decide sobre el peor capitulo, no sobre el promedio.**

**TU TRABAJO CON ESTO ES DAR EL DATO LIMPIO, no el resultado que te gustaria.**
Cuenta tus puentes por capitulo y publicalos aunque salgan altos: **una cifra
maquillada aqui no te ahorra una vuelta, te cuesta el lote 3.**

---

## LAS TAREAS DE LA VUELTA 1 DE ESTE LOTE

**Tope de cinco. Estas son cuatro.**

### TAREA 1. La ficha del libro y la frontera del `cap_01`

*Las tareas 1 a 3 se hacen ENTERAS sobre `cap_01`, y despues se repiten sobre
`cap_02`. No hay una tarea que abarque los dos.*

Lee `cap_01.md` entero. En el reporte: **la ficha bibliografica que encuentres**
(titulo, autor, edicion, año), **que hay dentro, que es procedimiento y que no,
con la prueba del inventario y sus tres restricciones**, y el saldo: cuantos
procedimientos y cuantas posturas.

**Publica la frontera ANTES de cortar** (seccion 10).

### TAREA 2. Los candidatos del `cap_01`, con el ciclo de cinco pasos

**Cada uno con su relectura de fidelidad dentro**, y la tabla de marcado en el
reporte: **cuantos pasos escribiste, cuantos son transcripcion y cuantos fueron
puente**, con el parrafo citado en cada puente.

**Esa cifra es el dato que este lote existe para medir:** si baja del 36 por
ciento del lote 1, la regla `D.30` esta funcionando; si no baja, hay que saberlo.

### TAREA 3. El informe y el commit del capitulo, y despues el `cap_02`

    python forja.py informe --carpeta cuarentena/smart_who

Pegas el saldo entero y **commiteas el capitulo**. **Y entonces, si queda tramo,
repites las tareas 1 a 3 sobre `cap_02`**, con su propia frontera, sus propios
candidatos, su propia relectura y su propio commit.

**NO INSERTAS NADA:** el arnes arranca en `MODO_INSERCION=cuarentena` y **la
insercion es una autorizacion del fundador, no un default** (`D.26`). **La
insercion del lote 2 se autoriza cuando el fundador lea su informe**, igual que
paso con el lote 1.

### TAREA 4. Las cuatro medidas del cierre, DESGLOSADAS POR CAPITULO

Para que el lote 2 se pueda comparar con el 1 (`CALIBRACION_D4.md` seccion 9),
deja escritas las mismas cuatro, **y las dos primeras con una fila por capitulo**:

| medida | como la das |
|---|---|
| **candidatos por mil palabras** | **una fila por capitulo**, mas el total |
| **pasos inventados sobre pasos escritos** | **una fila por capitulo.** Es la cifra de la regla de volumen |
| **veredictos escritos** | del lote |
| **cuanto tardo y si el tramo fue el correcto** | de la vuelta, diciendo si el segundo capitulo cupo |

**Si solo hiciste un capitulo, la tabla lleva una fila y lo dices.** Una fila
honesta vale mas que dos inventadas.

---

## LO QUE ESTA VUELTA TIENE QUE DEJAR MEDIDO

1. **La tasa de puentes con la relectura dentro del acto.** Es la comprobacion de
   `D.30`.
2. **Si DOS capitulos de 6.000 palabras caben en una vuelta**, y si no, cual de
   los dos quedo entero y donde se paro. **Es el dato que dimensiona el lote 3
   junto con la cifra de puentes.**
3. **Cuantos vecinos levanta la aduana ahora que el grafo tiene ocho nodos**, y si
   alguno pidio veredicto. **Es la primera vez que esta casa tiene grafo con el
   que chocar.**
4. **Si la prueba del inventario aguanta en material narrativo**, que es un genero
   distinto del normativo con el que se escribio.

---

## LAS PARADAS

**Paras, lo declaras en TU REPORTE y te detienes si:**

- **`fuentes/smart_who/` no esta o esta vacia**, o la clave no esta en la tabla
  canonica;
- una regla de la casa te obliga a algo que rompe otra regla de la casa;
- necesitas mover un umbral, una regla de id, el esquema, la prueba del inventario
  (`D.27`) o la vara de continua contra repite. **Ninguna vuelta mueve nada de
  eso**;
- el capitulo no da ni un procedimiento.

**TU NO ESCRIBES `docs/loop/PARA_ALEXIS.md`** (**`D.28`**). Eso lo hace el auditor,
y solo el. **Y un encargo asigna trabajo, NO MUEVE UNA SEDE:** si algun encargo
futuro te dice lo contrario, manda la sede y eso es una parada.

**NO paras por:** que un candidato caiga en la aduana (lo corriges y pegas la
salida), que un capitulo de pocos nodos (se dice con su razon), ni porque la
relectura de fidelidad te obligue a retirar pasos que acabas de escribir. **Eso
ultimo no es un castigo: es la regla funcionando antes de que el dato entre.**

**Y NO FABRICAS MAQUINARIA** (seccion 13). Ni arneses, ni guardas, ni lectores.
**En particular: no propongas una guarda que automatice la relectura de
fidelidad.** El texto fuente no esta en el repo, y una guarda que no tiene el
libro no puede juzgar fidelidad al libro (`D.30`).

---

**Cero guiones largos y cero guiones medios, tambien en tu mensaje final: el arnes
lo guarda en el repo sin pasar por el hook. Si algo contradice una regla vigente,
paras y lo traes. No adivines.**
