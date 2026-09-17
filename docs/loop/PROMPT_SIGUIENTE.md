# ENCARGO DE LA VUELTA 34: **LA REPARACION PRIMERO, Y DESPUES EL LOTE 4**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta (`D.45`). Escrito al
aplicar la decision del fundador del 17 sep 2026, archivada en
`docs/loop/paradas/2026-09-17-dato-movido-y-la-ciega-que-ve-DECISION.md`.*

> # **LA PARADA ESTA LEVANTADA, Y NO POR UN PERDON**
>
> El auditor te paro con `DATO MOVIDO` en `2 de 2`. **De sus dos ejemplares, uno se
> reclasifica y el otro se repara.**
>
> | ejemplar | que pasa con el |
> |---|---|
> | **el cerrojo que entro en `git` dentro de `dataset/`** | **NO es dato: es `ARNES`.** `D.52` muda la sede fuera de `dataset/` y **el ejemplar no acumula** |
> | **el nodo que afirma que tres capitulos no estan minados** | **SI es dato, y es tu `TAREA 1`.** Se repara antes de seguir |
>
> **`DATO MOVIDO` queda en `1 de 2`**, por decision escrita del fundador (`5.4`), no por
> tanda limpia y no por ti. **Sigue en su penultimo escalon: la proxima cae al tope.**

---

## 1. LA APERTURA: **EL TABLERO Y SU PRIORIDAD** (`D.49`, `D.51`)

> # **LIBRO DE ESTA VUELTA: `scott_radical_candor`**

**El arnes lee esa linea y la comprueba contra el tablero ANTES de gastar un turno.**

    python forja.py tablero                el estado de los once libros
    python forja.py tablero --siguiente    que libro le toca a ESTA linea, y por que

**TU APERTURA CITA LAS DOS COSAS** (`D.49`: *toda linea lee el tablero en su apertura y lo
cita*): **el estado y el dueño de tu libro**, y **por que te toca ese y no otro**.

**EL ORDEN DEL MUNDO 11, QUE NO ELIGES TU** (`D.51`): `1` `grove_high_output`,
`2` `gerber_emyth`, `3` `marquet_turn_the_ship`, **y ahi esta el corte**. Mientras
`scott_radical_candor` no cierre, **te toca `scott_radical_candor`**: `D.50` releva **al
cerrar** y no a mitad.

**Y HAY UNA COLA DE DOCTRINA EN EL TABLERO**, con **seis** preguntas que tu antecesor
levanto y que **NO se resuelven ahora**: se resuelven cuando el mundo 11 cierre, **salvo
que alguna te bloquee, y entonces sube sola**. Si te topas con una de las seis, **no la
adjudiques: di que es la numero `N` de la cola y sigue.**

---

## 2. **TAREA 1, BLOQUEANTE: EL NODO QUE AFIRMA UN ESTADO DE MINERIA FALSO**

*Es el ejemplar de `DATO MOVIDO` que **si** es dato. Va **antes** de insertar nada.*

**Un nodo que entro en la vuelta 33 dice, dentro de `dataset/nodos.jsonl`, que tres
capitulos NO estan minados todavia. Uno de los tres tiene `16` nodos y `187` pasos en el
grafo**, metidos por la vuelta 32, **y la propia vuelta 33 lo probo** cableando una arista
a ese capitulo.

### 2.a. Corregirlo **contra la medicion del dia**

    python forja.py corregir --nodo <id> --anade "CORRECCION DECLARADA ..." --razon ...

**`D.13`, sin borrar el texto viejo**, y **con la cifra citada**: la afirmacion nueva dice
lo que mide tu instrumento de hoy, no lo que recuerdas. **Publica el comando con el que lo
mediste**, no solo el que lo arregla (`REMEDIO 2` de la `ACTA 31`: *todo recuento que
publico corrigiendo una tabla ajena lo genero del dato, nunca leyendo la tabla que
corrijo*).

### 2.b. Y **medir si hay mas**, que es la mitad que importa

> **ESA ESPECIE NO DEBERIA EXISTIR: un nodo describe CONOCIMIENTO, no el estado de la
> campania.**

**Barre el dataset entero buscando nodos que afirmen estado de mineria dentro de su
texto** (*no esta minado*, *pendiente de minar*, *queda por extraer*, *en bandeja*, y lo
que se te ocurra de esa familia), **y NOMBRA LO QUE SALGA**, uno a uno, con su id y la
frase. **Si no sale ninguno mas, esa cifra tambien se publica**: un barrido que solo se
cuenta cuando encuentra algo no es un barrido.

**Lo que NO haces:** corregirlos todos por tu cuenta si son muchos. **Los nombras, cuentas
cuantos son, y dices cuanto costaria.** Si es una familia grande, **es cola y sube**.

---

## 3. TAREA 2. **SEGUIR INSERTANDO EL LOTE 4**

    $ python .v34/estado.py
    poblacion: el arbol entero, sin filtrar
    dataset/nodos.jsonl                     : 282 nodos
    bitacora/VEREDICTOS.jsonl               : 410 lineas
    cuarentena/scott_radical_candor         : 63
    cuarentena/_insertados/scott_radical_candor: 79

**`79` de `142` insertados, el `55,6` por ciento.** `cap_08` cerro en insercion, `12` de
`12`. **El siguiente es `cap_09`, con `20` candidatos en bandeja contra un techo de `15`**
(`EXTRACTOR.md` 12.4). **El techo manda:** si el capitulo entero no cabe, la vuelta cierra
donde cabe y **lo declara con su cifra**.

- **Un candidato por vez y en el orden del libro**, por la aduana, con su veredicto.
- **Las aristas `D.29` que la señal no levanta se declaran por lectura y se cablean en la
  misma vuelta.**
- **`NO SE ABRE NINGUN LOTE** (`D.32`), y el lote 5 no se toca: **ahora lo impide el
  tablero, no una frase**.

> **EL CERROJO ESTA PUESTO Y HA CAMBIADO DE SITIO** (`D.44`, `D.52`): vive en
> `procesos/`, **nunca dentro de `dataset/`**. Si algo dice `INSERCION NO INTENTADA`, hay
> otra corrida viva. **No la esquives.**

## 4. TAREA 3. **LA FIDELIDAD, Y ESTA VEZ EN SU ORDEN**

**`PASOS INVENTADOS` por capitulo** (`D.30`), fila por unidad mas total, **releyendo los
pasos contra su parrafo**.

> **LA RELECTURA VA ANTES DE QUE LOS NODOS ENTREN**, que es la letra que la vuelta 33
> rompio: corrio la fidelidad con tres nodos ya dentro. Tu antecesor lo declaro el solo y
> **no se lo cargaron porque esa figura no tiene fila** (es la pregunta `5` de la cola de
> doctrina). **No lo repitas apoyandote en que no acumula.**

**La escalada se decide sobre el peor capitulo, no sobre el promedio.** Tope `10`.

---

## 5. **TU CREDITO, Y COMO SE ESCRIBE AHORA** (`D.48`, `D.52`)

    python forja.py credito              lo que tu linea trae al abrir
    python forja.py credito --citas      que ninguna cita traiga una conclusion dentro

**Al cerrar escribes tu tanda, una linea por especie, y es parte de cerrar:**

    python forja.py credito --anotar --especie "DATO MOVIDO" --vuelta 34 \
           --tanda "ACTA 33" --racha "0 de 2" --limpia --cita "ACTA 33, seccion 9.1"

> ### **Y LA `cita` ES UNA REFERENCIA, NUNCA UN RESULTADO** (`D.52`)
>
> **Ruta y linea del acta**, y nada mas: `"ACTA 33, seccion 9.1"`. **Nunca**
> `"11 SANO releidos"` ni `"censo en verde"`.
>
> **POR QUE, y es una caida de verdad:** la fase ciega leia este registro y el `cita` de
> una tanda ajena le dijo `11 SANO` **antes de que contara los suyos**. Ahora el arnes
> **retira el registro durante la fase ciega**, y ademas **una cita con conclusion dentro
> no pasa el sello**: el testigo tiene cuatro guardas.
>
> **Cinco citas ya escritas cayeron al estrenar la guarda**, todas de tu antecesor. **No
> se borro ninguna:** el texto entero vive en `cita_original`.

---

## MODO AUSTERO (`D.47`)

| | |
|---|---|
| **el reporte** | **nada que el registro ya diga** |
| **los discutibles** | **por numero y linea**, sin reabrir el argumento |
| **las cifras** | **talladas**, con la salida del instrumento pegada de su fichero (`D.41`) |
| **los instrumentos** | **CERO nuevos**, salvo que una caida **de DATO** lo exija con su cita |

> **El austero recorta tinta, no control.** La aduana entera, el cerrojo, el censo no
> decreciente y la relectura contra el parrafo **quedan intactos**.

## LO QUE NO SE TOCA

- **`src/`, el banco, el arnes y los protocolos**: moratoria de `D.45`.
- **`config/umbrales.json`**, ningun umbral.
- **`config/frentes.json`**: ahi viven **decisiones del fundador con su cita**, no
  configuracion. Se lee, no se edita.
- **El bucle no funde ramas y el bucle no crea remotos.**
- **Los frentes**: `grove_high_output` es de su linea; `gerber_emyth` y
  `marquet_turn_the_ship` estan pausados. **Ninguno es asunto tuyo.**

## AL CERRAR

    python scripts/cerrar_reporte.py
    python forja.py tablero --escribir          el tablero se vuelve a medir (D.49)
    python forja.py credito --anotar ...        una linea por especie, con su cita

**Y COMMITEA Y PUSHEA `docs/loop/`.**
