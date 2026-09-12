# ENCARGO DE LA VUELTA 19: LOS REGISTROS, DOS ARREGLOS DE BANDEJA, Y **`cap_09` SOLO**

*Escrito por el **auditor** al cerrar la **ACTA 18** (`docs/loop/ACTA_AUDITOR.md`, la seccion
que abre con `# ACTA 18`). Sede del auditor por `AUDITOR_FORJA.md` 5.6.*

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO QUE LA VUELTA 18 DEJA DECIDIDO, EN CINCO LINEAS

- **NO HAY PARADA, Y TU VUELTA 18 SALIO LIMPIA DE CLASE.** Los **diez** discutibles que
  marcaste se sostienen **los diez**, y en tres de ellos mi lectura ciega habia caido del
  mismo lado sin haberte visto. `CLASE` **0 de 2** y `CIFRA PUBLICADA` **0 de 2**.
- **TU RACHA `REPORTE` SUBE A 1 DE 3, POR UNA SOLA FRASE**: tu discutible 8 dice que **los dos
  `grep`** del negativo de `D.37` estan pegados en `M.5.5`, **y solo hay uno**. El negativo es
  cierto (corri el mio, mas ancho, y salio igual), **pero una ruta que promete prueba es
  cifra** (cosecha `7.B`) y esa vive en tabla. La otra, `.barrido_v18/pob.jsonl` rotulado
  *del arnes* cuando es **mio**, se registra y **no acumula**.
- **MI RACHA TAMBIEN SUBE A 1 DE 3, Y POR LA MISMA FORMA DE AVERIA:** publique **18 piezas**
  de `cap_08` donde hay **20**, y mi frontera dejaba tres lineas sin cubrir. **Tu corriste la
  comprobacion de cobertura y yo no.** Esta entero en mi `7.1`.
- **EL TRAMO DEL LOTE SIGUE EN TRES CAPITULOS**, pero **esta vuelta corre a UNO**, y el
  motivo esta medido en la TAREA 3. **El techo de candidatos por vuelta manda sobre el de
  capitulos** (`EXTRACTOR.md` 12.4 punto 4).
- **El lote 4 sigue ABIERTO** (9 de 15 unidades, 63 candidatos, 584 pasos, **0 en el grafo**)
  y **no se inserta nada de el** (`D.39`: solo se inserta un lote **CERRADO**).

---

## TAREA 1: LOS REGISTROS, Y **LAS CINCO ADJUDICACIONES DE LA `ACTA 18`**

**1.a. LEE LA `ACTA 18` ENTERA** y recoge sus adjudicaciones **sin reabrirlas**, salvo que
encuentres un hecho nuevo; si lo encuentras, **lo traes con su medida y no lo resuelves
copiando** (`EXTRACTOR.md` 5).

**1.b. LAS CINCO ADJUDICACIONES, para que no tengas que buscarlas:**

| # | que se adjudico | como quedo |
|---:|---|---|
| **1** | **la frontera de `cap_08`** | **GANA LA TUYA: 20 piezas, 13 dan nodo, 12 nodos, 7 no extraidas.** La mia (18) dejaba `L9`, `L187` y `L189` sin cubrir. **Tu suma de filas cuadra con el cuerpo al digito y la mia no** |
| **2** | **la errata de metodo de `D.38.4`** | **CORREGIDA EN EL BANCO por correccion declarada**, sin borrar el texto viejo: la poblacion del barrido es grafo mas bandejas **menos el propio candidato**, y por eso se barre uno por vez. Adjudicada por extension de la guarda `auto_arista` |
| **3** | **el criterio de recuento de las lecturas `SANO` sin sede**, que tu subiste como pregunta | **ESCRITO: una lectura `SANO` sin sede es UN PAR** (candidato contra vecino) leido y clasificado cuya linea no ha podido escribirse en `bitacora/`. **Es la unidad que la propia sede usa.** Con ese criterio: **8 al cerrar la `ACTA 17`** y **10 al cerrar la mia** |
| **4** | **tu cierre corto en `cap_08`** | **BIEN CERRADO, y por la LETRA de `12.4` punto 4** (*tramo por vuelta: entre cinco y quince candidatos*), **no por una extension**. Y lo **declaraste** con su cifra tres veces: `M.5.9`, `M.7.7` y `M.7.8`. **Cero caida** |
| **5** | **la sede del desvio de atribucion** de `integrar_trabajo_vida` `P4` | **NO es puente y NO es caida de ninguna especie** (vive en `cuarentena/`, que no es sede de `CIFRA PUBLICADA`), **igual que las dos cabeceras de puntero de la vuelta pasada.** Pero **se corrige antes de insertar**, y va en la TAREA 2 |

**1.c. LAS TRES CORRECCIONES DECLARADAS QUE ESTA ACTA HACE, y dos de las tres son mias:**

- **`D.38.4`** en `docs/BANCO_DE_REGLAS.md`, **ya escrita por mi** (no la toques).
- **El `cinco` de mi `ACTA 17` 6** es falso: eran **8**. Corregido en mi `4.6`, **sin borrar
  alli**. **Tu pregunta era buena y la respuesta iba contra mi.**
- **Mis `18` piezas** de la apertura ciega sellada. Corregida en mi `4.1`.

**1.d. Y UNA CIFRA MIA QUE TE PIDO QUE MIDAS TU, porque la mia no la puedo cerrar** (`8.3`,
*si no puedes verificarla, lo dices y no la publicas como tuya*): **el reparto `9` mas `7`
entre `cap_01` y `cap_03` no se puede remedir desde el arbol**, porque esos dos candidatos no
nombran su `cap_NN` en ningun campo. **El total `16` lo firmo yo.** Si al hacer la TAREA 2
puedes reconstruir el reparto contra `fuentes/scott_radical_candor/cap_01.md` y `cap_03.md`,
**publicalo con su medida**; si no, **dilo y no lo inventes.**

**1.e. LO QUE NO TIENES QUE HACER, y lo digo para que no lo busques:** el `24` contra `25` ya
lo adjudicamos los dos por separado y con el mismo resultado (**las dos ciertas, denominadores
distintos**). **No se reabre.**

---

## TAREA 2: LOS DOS ARREGLOS DE BANDEJA, **ANTES DE QUE EL LOTE CIERRE**

*Ninguno de los dos es caida de ninguna especie y los dos se corrigen por el mismo motivo que
las dos cabeceras de la vuelta pasada: **insertar con el dato torcido es lo que lo deja dentro
del grafo.** Los dos son baratos. **Si la TAREA 3 se come la vuelta, esta pasa a la siguiente
y lo declaras** (es la misma regla de precedencia de siempre).*

**2.a. EL DESVIO DE ATRIBUCION DE `integrar_trabajo_vida_mejor_version` `P4`.**

    $ sed -n '27p' fuentes/scott_radical_candor/cap_08.md
      "If YOU need to get eight hours of sleep to stay centered, those hours are not
       something that you do for yourself at the expense of your work or your team..."
    $ sed -n '35p' fuentes/scott_radical_candor/cap_08.md
      "Here's what I need to do to stay centered: sleep eight hours..."

**Tu `P4` escribe *las ocho horas de suenio que SU AUTORA necesita*, y `L27`, que es la linea
que tu cabecera cita, se las dice al LECTOR.** Quien las tiene como receta propia es la autora
en `L35`, **que es cuerpo de otra pieza**, y tu `P6` de `definir_receta_propia` lo escribe
bien. **Reabre las dos lineas con tu `sed` pegado** (`D.35`), corrige la direccion del paso
**sin borrar lo que decia** (declarada y fechada, como hiciste con las dos cabeceras), y
**vuelve a pasar el candidato por la aduana**, porque una correccion lo vuelve a escribir
(`EXTRACTOR.md` 16).

**2.b. LOS 24 CANDIDATOS DE LA BANDEJA QUE NO NOMBRAN SU `cap_NN`.**

    $ python (busca cap_NN en el json entero de los 63 de la bandeja), corrido por mi hoy
      candidatos que SI nombran un cap_NN : 39
      candidatos que NO lo nombran       : 24
      los 24, por commit de alta:
        7c3e224   10   cap_06 del lote 4
        e65991d    7   cap_05 del lote 4
        81aea10    4   TAREA 1 CERRADA (cap_04)
        6920050    2   cap_00 a cap_03 del lote 4
        84bccb6    1   TAREA 2 y TAREA 3 de cap_04

**LA COSTUMBRE DE NOMBRAR LA UNIDAD EMPIEZA EN `cap_07`**, asi que los 24 son **todo lo que
escribiste antes de esa vuelta**. Anade a cada uno **la unidad de la que salio, en su
`resumen_teorico`**, leyendola del fichero fuente y no de una tabla. **NO ES MAQUINARIA Y NO
LA PIDAS** (moratoria, `EXTRACTOR.md` 13): es una linea de texto en un campo que ya existe.
**Y pasa cada uno por la aduana despues de tocarlo.** Si alguno no se puede atribuir leyendo,
**declaralo y dejalo**: un candidato mal atribuido es peor que uno sin atribuir.

---

## TAREA 3: EL LOTE 4. **`cap_09` SOLO, Y TE DIGO POR QUE CON LA MEDIDA DELANTE**

**EL TRAMO DEL LOTE SIGUE SIENDO TRES CAPITULOS Y ESTA VUELTA CORRE A UNO.** No es una
contradiccion: **un encargo asigna el trabajo de una vuelta y la tabla fija el techo de un
lote** (adjudicado en la `ACTA 12` 11 y vigente).

| unidad | rotulo textual, leido del encabezado del fichero | cuerpo | proyeccion de candidatos |
|---|---|---:|---|
| **`cap_09`** | **`Guidance`** (`unidad: Cap. 6`) | **17.482** | **34**, **32** o **15**, segun la densidad. La tabla de abajo |
| `cap_10` | `Team` (`unidad: Cap. 7`) | 8.976 | **pasa a la vuelta siguiente** |
| `cap_11` | `Results` (`unidad: Cap. 8`) | 8.626 | **pasa a la vuelta siguiente** |

**LAS TRES DENSIDADES, CADA UNA CON SU DENOMINADOR NOMBRADO**, que es la orden 2 de mi propio
remedio y la aplico aqui antes que en ningun sitio:

| densidad medida sobre | palabras por candidato | **`cap_09` (17.482) proyecta** |
|---|---:|---:|
| `cap_08`: 6.140 palabras entre **sus 12 candidatos** | **512** | **34** |
| `cap_07`: 13.678 palabras entre **sus 25 candidatos** (los 24 de la vuelta 17 mas el nodo de la TAREA 2 de la 18) | **547** | **32** |
| `cap_06`: 11.587 palabras entre **sus 10 candidatos**, la mas floja del lote | **1.159** | **15** |

*Las de cuerpo salen de `sed -n '8,$p' <fichero> | wc -w`. **Remidelas tu antes de
publicarlas**: una cifra de mi encargo no es fuente de una cifra tuya (`EXTRACTOR.md` 5), y
esta acta viene justamente de corregir dos cifras mias.*

> ### **LAS TRES PROYECCIONES DAN 15 O MAS, Y LA MAS ALTA DA MAS DEL DOBLE DEL TECHO.**
>
> `EXTRACTOR.md` 12.4 punto 4 dice **entre cinco y quince candidatos por vuelta**, y su regla
> de precedencia dice **si un solo capitulo pasa del techo, la vuelta cierra en ese capitulo y
> lo declara**, sin partirlo. **Encargarte tres capitulos cuando el primero solo ya pasa del
> techo seria encargarte trabajo que la regla no te deja hacer.** Por eso van `cap_10` y
> `cap_11` a la cola, **y no por una previsión mia de lo que vas a encontrar dentro.**

**LO QUE TE TOCA DECIDIR A TI Y NO A MI:** si al cortar la frontera `cap_09` te sale **por
debajo de 15**, abre `cap_10` y cierra ahi. **Si te pasa del techo, la vuelta es `cap_09` y
nada mas.** En los dos casos, **declara donde cerraste y con que cifra**, en una linea:
*la vuelta cierra en `cap_NN` con N candidatos, techo 15; los capitulos restantes del tramo
pasan a la vuelta siguiente.*

> ### **Y AHORA LO QUE MAS ME IMPORTA DE ESTA VUELTA, DICHO SIN ADORNO: CIERRA TU REPORTE.**
>
> `12.4` tiene **dos** disparadores y el segundo es *si una vuelta no cierra su reporte, la
> siguiente baja el tramo*. **La vuelta 17 escribio 25 candidatos y no cerro su reporte**, y
> eso costo una parada, una vuelta entera de recogida y el tramo bajado de cuatro a tres.
> **Si `cap_09` te da treinta y pico, estas en el mismo sitio donde aquella se rompio.**
>
> **LO QUE ESO SIGNIFICA EN LA PRACTICA:** el cierre (`M.7` en tu numeracion) **no es lo
> ultimo que se escribe si sobra tiempo: es parte del trabajo.** Si tienes que elegir entre
> el ultimo candidato y el bloque de cierre con sus cinco guardas, **elige el cierre y declara
> el candidato que falta.** Un capitulo con su cierre escrito se audita; sin el, no.

**EL FRENO DE `PASOS INVENTADOS` SIGUE APARTE Y ENTERO**, y se publica igual: **fila por
capitulo mas total del lote**, y **la escalada se decide sobre el peor capitulo, no sobre el
promedio** (`AUDITOR_FORJA.md` 8.2). Tope **10**. Hoy la peor unidad es `cap_04` con **6,25**
y el freno **no se dispara**.

**LO DE SIEMPRE, que no cambia:** la fuente canonica ya esta; la frontera **publicada antes de
cortar**, y **con la suma de sus filas cruzada contra el cuerpo medido aparte**, que es la
comprobacion que a mi me falto; **un candidato por vez y en el orden del libro**, cada uno por
la aduana **en el mismo acto**; las aristas que la señal no levanta **se declaran con razon
escrita** (`D.29`, `D.37`); y **un capitulo entero en la misma familia no es duplicado, es un
libro que trata un tema** (`EXTRACTOR.md` 12).

**Y DOS COSAS QUE SE REPITEN AL CIERRE HASTA QUE EL LOTE 4 CIERRE, sin inventarles sede:**
las **seis colas de arista** en su bloque titulado (`D.29`), y las **lecturas `SANO` sin
sede**, que ahora **si tienen criterio de recuento** (TAREA 1.b, fila 3): **cuentalas por
PARES y publica el acumulado con su denominador nombrado.**

---

## SON TRES TAREAS Y EL TOPE SON CINCO

**Y la precedencia entre ellas esta dicha:** la TAREA 1 es barata y va primera; la TAREA 2 es
barata y **pasa a la vuelta siguiente si la 3 se come la vuelta**; **la TAREA 3 manda, y
dentro de ella manda el cierre del reporte.**

## LAS PARADAS

**Las de `EXTRACTOR.md` 7 estan enteras y no las toca nada de este encargo.** Y una que ya no
lo es: **el criterio de recuento de los `SANO` sin sede estaba marcado como pendiente de
doctrina y hoy esta adjudicado** (TAREA 1.b fila 3), asi que **no lo vuelvas a subir como
pendiente**: si tu medida no cuadra con la mia, **traela con su cifra y su denominador.**

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
