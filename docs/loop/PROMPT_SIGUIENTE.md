# ENCARGO DE LA VUELTA 1: EL LOTE 1, LIBRO `onu_consumidor`

*Escrito por Alexis el 10 sep 2026. Es la PRIMERA vuelta de esta forja: el
dataset tiene DOS nodos y ninguno lo escribio un extractor.*

---

## LO QUE TIENES QUE SABER ANTES DE EMPEZAR

**ESTA ES UNA VUELTA DE CALIBRACION, y eso cambia lo que se te pide.** El lote 1
se eligio por ser **el libro de menos capitulos del mundo 11** (decision del
fundador, D.24). No se hace para meter muchos nodos: **se hace para medir el
instrumento con trabajo de verdad delante, barato.**

Por eso, en esta vuelta, **una tarea que produce cero nodos con su razon escrita
vale tanto como una que produce cinco.** Lo que no vale es una tarea sin razon.

**LEE PRIMERO `docs/loop/EXTRACTOR.md` ENTERO.** En particular, y son nuevas del
10 sep 2026:

- **seccion 15**, las reglas de id con sus dos listas y sus ejemplares. **Se
  leen antes de escribir el primer id, no despues del primer rechazo.** El
  estreno midio que cuatro de cada diez candidatos escritos sin ellas delante
  caen en la puerta.
- **seccion 16**, cada candidato pasa por la aduana **en el mismo acto en que se
  escribe**. Un candidato no esta escrito hasta que ha pasado la aduana.
- **seccion 17**, el protocolo de lote: los candidatos van a
  `cuarentena/onu_consumidor/`, y **desde el 10 sep 2026 esa carpeta VIAJA en el
  repo** (D.25).

**Y EL ARNES QUE TE LANZO ARRANCA EN `MODO_INSERCION=cuarentena`**, que es su
default desde D.26: **la insercion es una autorizacion del fundador, no un
default**. Tu prompt permanente ya te lo dice, y este encargo dice lo mismo. **No
hay contradiccion entre los dos: si crees encontrar una, eso es una parada.**

---

## EL LIBRO, Y DONDE ESTA

**Clave canonica: `onu_consumidor`.** Ya esta registrada en
`fuentes/FUENTES_CANONICAS.json`, asi que **no la registras tu**: si la aduana
te rechaza por fuente, el problema es otro.

    Directrices de las Naciones Unidas para la Proteccion del Consumidor
    UNCTAD/DITC/CPLP/MISC/2016/1, Nueva York y Ginebra, 2016
    Resolucion AG 39/248 (1985), ampliada ECOSOC 1999/7 (1999),
    revisada y aprobada AG 70/186 (22 diciembre 2015)

El recorte verbatim vive en `fuentes/onu_consumidor/`, **fuera de git** porque
es texto de otro autor. Cuatro unidades, y **esta es la correspondencia con el
recorte original del mundo 11**, que necesitas para citar:

| fichero | unidad | titulo textual | palabras |
|---|---|---|---:|
| `cap_00.md` | portada y creditos | Vigencia | 171 |
| `cap_01.md` | apartado V-B, parrafos 16 a 19 | B. Seguridad fisica | 376 |
| `cap_02.md` | apartado V-C, parrafos 20 a 32 | C. Promocion y proteccion de los intereses economicos de los consumidores | 819 |
| `cap_03.md` | apartado V-F, parrafos 37 a 41 | F. Solucion de controversias y compensacion | 389 |

**`cap_00.md` NO SE MINA:** es portada y creditos. Esta ahi porque es de donde
sale la ficha de la fuente, y para que puedas comprobarla.

---

## LA MARCA FRONTERA DE `cap_01`: LA DECISION YA ESTA TOMADA

**`cap_01.md` lleva esta marca en su linea 9, puesta por el recorte del mundo 11:**

    _Nota: seccion FRONTERA, no se mina en el nucleo (ver plan de recorte)._

**ESA MARCA SE RESPETA. Es una decision previa del fundador**, tomada en el plan
de recorte del mundo 11, y **una vuelta de extraccion no reabre una decision del
fundador** (`EXTRACTOR.md` seccion 5). No la discutes: la cumples y la registras.

**LO QUE HACES CON `cap_01`, en este orden:**

1. **LO LEES ENTERO.** Una marca no sustituye a una lectura, y sin leerlo no
   puedes hacer el punto 2.
2. **PASAS LA VARA DE LA SECCION 9 SOBRE SU MATERIAL Y ESCRIBES ESA LECTURA COMO
   EJEMPLAR.** No para decidir nada, que ya esta decidido: **para dejar en el
   reporte un caso trabajado de postura contra procedimiento en material
   normativo**, que es el caso dificil y esta casa todavia no tiene ninguno.
   Ahi hay trampa buena: *"Los Estados Miembros deben adoptar politicas
   adecuadas"* parece un imperativo y **una postura no ejecuta una busqueda**.
   Cita tus lineas.
3. **LO REGISTRAS COMO NO MINADO POR LA MARCA**, no como no minado por tu
   lectura. Son dos cosas distintas y el reporte tiene que distinguirlas: si tu
   vara y la marca coincidieran, seria informacion; si discreparan, tambien, y
   **mas**. Lo escribes tal como salga.
4. **PASAS A `cap_02.md` EN ESTA MISMA VUELTA**, y de ahi salen los candidatos.

**NO ES UNA PARADA Y NO TE CUESTA LA VUELTA.** `cap_02` es el apartado V-C,
parrafos 20 a 32, 819 palabras: **es el capitulo de esta vuelta.**

## LAS TAREAS DE ESTA VUELTA

**Tope de cinco tareas (seccion 3). Estas son cuatro.**

### TAREA 1. `cap_01`: leerlo, pasarle la vara como ejemplar, registrarlo

Lee `cap_01.md` entero. En el reporte:

- **la lectura de vara como EJEMPLAR**, con sus citas de linea: que hay dentro,
  que seria procedimiento y que es postura, y por que;
- **el registro: NO MINADO POR LA MARCA FRONTERA**, con la marca citada;
- **si tu vara coincide o no con la marca.** Las dos respuestas valen; lo que no
  vale es no decirlo.

**No extraes nada de `cap_01`.**

### TAREA 2. `cap_02`: publicar la frontera y extraer, uno a uno y por la aduana

Lee `cap_02.md`, el apartado V-C. **Publica primero que hay dentro, que es
procedimiento y que no, y donde esta la frontera.** Sin extraer todavia.

Despues, cada candidato:

    1. lo escribes en cuarentena/onu_consumidor/<id_propuesto>.json
    2. python forja.py informe cuarentena/onu_consumidor/<id>.json
    3. si CAERIA, lo corriges y vuelves al 2
    4. solo entonces cuenta como escrito

**NO INSERTAS NADA.** El arnes arranca en `MODO_INSERCION=cuarentena` y su
prompt permanente ya te lo dice: los candidatos se quedan en la bandeja y **el
fundador lee el informe antes de autorizar la primera insercion real de esta
forja**. Si un candidato esta perfecto, igual se queda.

### TAREA 3. El informe del lote en seco

Al cerrar el capitulo:

    python forja.py informe --carpeta cuarentena/onu_consumidor

Pegas el saldo en el reporte: cuantos entrarian, cuantos bloquearian, cuantos
caerian y por que guarda.

### TAREA 4. El commit del capitulo

**Un commit por capitulo** (seccion 17), en la rama `extraccion-mundo-11`, con
los JSON dentro. El mensaje dice **que capitulo y cuantos candidatos**.

---

## EL BLOQUE DE APERTURA DE `docs/loop/REPORTE.md`

**Lo abres AL EMPEZAR, no al final** (seccion 3). Copia esto tal cual y rellena:

    # REPORTE DEL EXTRACTOR

    ## VUELTA 1, lote 1 (onu_consumidor), cap_02

    | | |
    |---|---|
    | fecha | 10 sep 2026 |
    | rama | extraccion-mundo-11 |
    | lote | onu_consumidor, LOTE 1 DE CALIBRACION (D.24) |
    | capitulo de extraccion | cap_02.md, apartado V-C parrafos 20 a 32 |
    | cap_01.md | leido y registrado NO MINADO por la marca FRONTERA |
    | nodos en el dataset al empezar | 2 |
    | inserciones autorizadas en esta vuelta | CERO. Todo queda en cuarentena |

    ### Las cuatro tareas

    | # | tarea | estado | resultado |
    |---|---|---|---|
    | 1 | cap_01 leido, vara como ejemplar, registrado no minado | | |
    | 2 | cap_02: frontera publicada y candidatos por la aduana | | |
    | 3 | informe del lote en seco | | |
    | 4 | commit del capitulo | | |

    ### Discutibles marcados ANTES de saber si acierto

    (los marcas aqui segun aparecen, no al final)

**Cada fila se anexa AL CERRARSE su tarea**, no al terminar la vuelta. Una
vuelta cortada deja reporte parcial, **nunca vacio**.

---

## LO QUE ESTA VUELTA TIENE QUE DEJAR MEDIDO, Y ES LO QUE MAS IMPORTA

Es la vuelta 1 de la casa. **Ademas de los nodos, deja escrito esto en el cierre
del reporte**, porque es lo que el fundador va a leer:

1. **Cuantos candidatos cayeron en la aduana al primer intento, y por que
   guarda.** Es la primera medida real de si las reglas de id nuevas (D.21,
   D.22) le sirven a un extractor o le estorban.
2. **Cuantas veces tuviste que corregir un id**, y si alguna correccion te
   parecio que empeoraba el nombre. **Si te lo parecio, dilo:** es dato para el
   fundador, no una queja.
3. **Si la vara de la seccion 9 te dejo decidir** entre postura y procedimiento
   en este material, que es material normativo y por tanto el caso dificil.
4. **Cuanto tardo la vuelta** y si el tramo (un capitulo) fue el correcto.

---

## LAS PARADAS

**Paras y escribes `docs/loop/PARA_ALEXIS.md` si:**

- una regla de la casa te obliga a algo que rompe otra regla de la casa;
- necesitas mover un umbral, una regla de id, o el esquema. **Ninguna vuelta
  mueve nada de eso** (seccion 5 y D.23);
- **`cap_02.md` no da ni un procedimiento.** Entonces lo dices con su razon y
  paras: un lote de calibracion que no encuentra material es informacion, pero
  es informacion que el fundador tiene que leer antes de que sigas.

**NO paras por:** que un candidato caiga en la aduana (lo corriges), que un
capitulo de pocos nodos (se dice y ya), ni por la marca FRONTERA de `cap_01`
(esta decidida: registras y pasas a `cap_02`).

**Y NO FABRICAS MAQUINARIA.** Ni arneses, ni guardas, ni lectores nuevos
(seccion 13). El trabajo de esta vuelta es leer un capitulo y escribir
candidatos.
