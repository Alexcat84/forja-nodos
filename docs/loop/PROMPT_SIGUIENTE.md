# ENCARGO DEL LOTE 2: `smart_who`, 7 capitulos

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

> **UN CAPITULO DE ESTE LIBRO NO ES UN APARTADO DE LA ONU, Y PUEDE NO CABER EN UNA
> VUELTA.** No es un fallo tuyo si no cabe: es la primera vez que esta casa mide un
> capitulo de verdad.

- **UN CAPITULO POR VUELTA**, y si no cabe, **la mitad que hiciste queda cerrada y
  lo dices**: reporte parcial, nunca vacio.
- **TRAMO: entre cinco y quince candidatos por vuelta** (seccion 12). Si un
  capitulo da mas, se parte y se dice donde.
- **UN COMMIT POR CAPITULO** (seccion 17), con los JSON dentro, y el mensaje dice
  que capitulo y cuantos candidatos.
- **AL CERRAR CADA CAPITULO:** `python forja.py informe --carpeta cuarentena/smart_who`
  y pegas el saldo.

---

## LAS TAREAS DE LA VUELTA 1 DE ESTE LOTE

**Tope de cinco. Estas son cuatro.**

### TAREA 1. La ficha del libro y la frontera del `cap_01`

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

### TAREA 3. El informe del lote y el commit del capitulo

    python forja.py informe --carpeta cuarentena/smart_who

Pegas el saldo entero. **NO INSERTAS NADA:** el arnes arranca en
`MODO_INSERCION=cuarentena` y **la insercion es una autorizacion del fundador, no
un default** (`D.26`).

### TAREA 4. Las cuatro medidas del cierre

Para que el lote 2 se pueda comparar con el 1, deja escritas las mismas cuatro:
**candidatos por mil palabras**, **pasos inventados sobre pasos escritos**,
**veredictos escritos**, y **cuanto tardo la vuelta y si el tramo fue el
correcto.**

---

## LO QUE ESTA VUELTA TIENE QUE DEJAR MEDIDO

1. **La tasa de puentes con la relectura dentro del acto.** Es la comprobacion de
   `D.30`.
2. **Si un capitulo de 6.000 palabras cabe en una vuelta**, y si no, donde se
   partio.
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
