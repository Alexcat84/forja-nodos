# ENCARGO DE LA VUELTA 43: **EL LOTE 7 (`grove_high_output`) ABRE EN INSERCION**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta. Escrito por la `ACTA 41`, que
cerro el lote 4 (`scott_radical_candor`, `142` de `142`) y midio en verde las dos condiciones de
apertura del lote siguiente (`D.32`, `ACTA 41` seccion 12.2).*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO QUE HA CAMBIADO BAJO TUS PIES, Y ES LO PRIMERO QUE TIENES QUE SABER

| | |
|---|---|
| **el lote 4 CERRO** | `scott_radical_candor` esta `INSERTADO`, bandeja `0`, `142` nodos en el grafo. **No lo toques** |
| **el lote 7 es tuyo** | `python forja.py tablero --puedo grove_high_output` responde `SI`. Esta `COSECHADO` y **sin dueno**: su rama se fundio el 18 sep |
| **su bandeja ya esta llena** | **`23` candidatos** esperan en `cuarentena/grove_high_output/`, minados por otra linea hasta `cap_03`. **Esta vuelta NO extrae: inserta lo que ya hay** |
| **el trabajo de otra mano trae deuda con el** | `d001` a `d005` de `docs/loop/DEUDA.jsonl` son suyas, y **`d005` decide que candidatos NO entran hoy**. Leelo antes de elegir |
| **la doctrina sigue congelada** | la cola se queda en `11` (`D.56`). Si encuentras una pregunta nueva, **registrala en tu reporte con su medida y dejala ahi**: no abre parada y no va al banco |

---

## **ESTA ES UNA VUELTA DE INSERCION, Y ESO ES UNA CLASE DE VUELTA** (`D.55`)

**ABRE SIN UNA SOLA TAREA DE REPARACION. Tu trabajo es meter candidatos al grafo por la aduana.**

**NO tienes tarea bloqueante.** Lo que hay que reparar esta en `docs/loop/DEUDA.jsonl` con su cita,
y se paga junto en una vuelta de SANEAMIENTO.

    python scripts/deuda.py        lo pendiente, y que clase de vuelta toca

**LO UNICO QUE TE PUEDE BLOQUEAR ES UNA GUARDA DE DATO EN ROJO**: `gate`, el cerrojo, el censo no
decreciente, o la fidelidad `D.30` con puente. **Eso no es deuda: es averia**, y una averia se
arregla antes de seguir. **Si ninguna esta en rojo, insertas.**

> **Y LA VUELTA 44 SERA DE SANEAMIENTO, escrito hoy para que no se decida por olvido.** `D.55` paga
> la deuda **una de cada cinco**, hay **`10`** pendientes y `scripts/deuda.py` dice `ultima vuelta de
> saneamiento: ninguna todavia`. **Esta es la ultima de insercion antes de pagar.**

---

## TAREA 1. **LOS REGISTROS DE LA `ACTA 41`, Y SON CUATRO LINEAS**

*No es reparacion: es recoger lo adjudicado, que `AUDITOR_FORJA.md` 1.4 pone siempre en la TAREA 1.*

| # | lo que la `ACTA 41` adjudico | que haces con ello |
|---|---|---|
| `1.a` | **los seis discutibles de la vuelta 42 se sostienen los seis**, y **mi clase ciega del `1` cae contra mi**: tu `SANO` sobre `dar_elogio_disciplina_igual_critica` contra `equilibrar_elogio_critica_equipo` **queda ratificado** | **nada que tocar.** Lo dices en tu reporte y sigues |
| `1.b` | **las OCHO aristas de la `ACTA 24` `3.1` SI son declarables** (`ACTA 41` `6.1`): manual seccion 3 punto 4 prohibe **dos compresiones**, y una arista entre hermanos **no comprime la lista, cita un paso**. `D.29` las cubre y `D.53` dice que el `SANO` no se mueve | **NO las cablees esta vuelta.** Estan en `DEUDA.jsonl` como `d008` y se pagan en la 44. **Si discrepas de la adjudicacion, dilo en tu reporte con el grafo delante**: eso es lo que `1.3` del protocolo del auditor manda y no lo cierro yo a martillazos |
| `1.c` | **tus dos caidas de la vuelta 42 son de PROSA y no acumulan** (`ACTA 41` `7`): la cita de `ED.6.f` apunta a `ACTA 24` `3.3`, que trata de otra cosa, y la cola de vigencia de `ED.7.e` dice `doce` donde el instrumento imprime `72` | **correccion declarada en tu reporte, sin borrar el texto viejo**, en las dos. La sustancia de `ED.6.f` era cierta: **lo falso era la cita** |
| `1.d` | `REPORTE` vuelve a **`0 de 3`** y `AUDITOR` sube a **`1 de 3`**, anotados los cinco en `docs/loop/CREDITO_serial.jsonl` | **nada que tocar.** Lo lees al abrir con `python forja.py credito` y lo citas |

---

## TAREA 2. **LA FRONTERA DE LO QUE VAS A INSERTAR, PUBLICADA ANTES DE LA PRIMERA INSERCION**

**LOS `23` DE LA BANDEJA NO SON TUYOS HASTA QUE LOS MIDAS.** Los mino otra mano, y la deuda dice que
no todos estan listos:

    python scripts/deuda.py          lee d001 a d005 ENTERAS antes de elegir

> **`d005`, literal:** *De los `15` candidatos de `cap_03` de grove, su aduana en seco dijo `9`
> ENTRARIAN y `6` BLOQUEARIAN: esos `6` se reparan antes de insertarse, y **NO entran en la primera
> vuelta de insercion del relevo**.*

**PUBLICA, ANTES DE INSERTAR NADA, y con el instrumento al lado de cada cifra:**

1. **cuantos candidatos hay en `cuarentena/grove_high_output/` y de que capitulo es cada uno**,
   contados del fichero y no de esta pagina;
2. **cuales son los `6` que `d005` aparta**, nombrados uno a uno;
3. **el orden del libro** en que vas a meter el resto (`EXTRACTOR.md` 12.3): **el orden no lo eliges
   tu, lo elige el libro**, y el primero que entra cambia lo que el segundo mide.

---

## TAREA 3. **INSERTAR, UN CANDIDATO POR VEZ Y POR LA ADUANA**

> # **EL TECHO DE ESTA VUELTA ES `15` CANDIDATOS.**

**Y esa es la unica cifra de techo que este encargo escribe.** Si llegas a `15`, cierras y lo
declaras; si la bandeja util se acaba antes, cierras ahi y lo declaras. `EXTRACTOR.md` 12.4.

- **Un candidato por vez y en el orden del libro**, por la aduana, con su veredicto y su razon escrita.
- **Las aristas que la senial no levanta se declaran por lectura** (`D.29`) **y se cablean en el
  mismo acto en que entra su nodo**, con el paso de la madre citado.
- **La seccion de la insercion crece UNA FILA CADA VEZ QUE UN CANDIDATO ENTRA, en su propio commit.**

### LO QUE SIGUE SIENDO OBLIGATORIO, PORQUE ES GUARDA DE DATO Y NO REPARACION

| | |
|---|---|
| **la fidelidad `D.30`** | de tus candidatos, **releida contra su parrafo y ANTES de la primera insercion**. Y ojo: **estos pasos los escribio otra mano**, asi que la relectura vale doble |
| **el cerrojo** | una sola corrida escribe el dataset. Si dice `INSERCION NO INTENTADA`, hay otra viva: **no la esquives** |
| **el censo y el tallado** | corren en cada commit y no se negocian |

### Y EL METODO DE LA INSERCION, CON LA MEDIDA DE LA VUELTA 42 DELANTE

> **NINGUNA CORRIDA SOBREVIVE A TU TURNO.** Esperala bloqueado hasta leer su codigo de salida, sin
> avanzar al candidato siguiente y sin hacer nada en medio.
>
> **Y SI TU ARNES NO PUEDE ESPERAR TANTO EN UNA SOLA LLAMADA, DILO CON LA MEDIDA AL LADO**, como
> hizo `ED.7.a` de la vuelta 42: su insercion mas larga duro `22:53` contra un tope de llamada de
> `10` minutos. **Lo que la regla protege es que nada te sobreviva, no la forma de esperarlo.** Esa
> redaccion la propuso el extractor en su sede y la `ACTA 41` la adopta aqui.

**Y LO QUE LA VUELTA 42 APRENDIO Y TE AHORRA TIEMPO:** en un capitulo cuyos nodos son partes de la
misma serie **los hermanos se levantan unos a otros casi siempre**, porque comparten el vocabulario
entero. **Escribe el veredicto de TODOS los hermanos antes de lanzar**, no solo el de los que la
senial levanto la vez anterior.

---

## TAREA 4. **AL CERRAR**

**Recomputa desde el fichero y no copies tu propia apertura:**

    python forja.py gate
    python forja.py guiones
    python forja.py resolutor
    python tests/test_aceptacion.py
    python scripts/cerrar_reporte.py
    python scripts/tabla_de_cierre.py --escribir      y se pega su salida
    python forja.py tablero --escribir
    python forja.py credito                           lo lees; NO anotes tu propia vuelta

**Y ESCRIBE LA LINEA DEL TRAMO, sea cual sea el numero, incluido `0`:**

> *la vuelta cierra en el candidato `N` de `M`; los que quedaban pasan a la vuelta siguiente.*

> **UNA COSA QUE TE VA A PASAR Y NO ES CULPA TUYA** (`ACTA 41` `6.3`, ya anotada como `d009`):
> `scripts/tabla_de_cierre.py` mide contra el **siguiente libro por prioridad del tablero**. Mientras
> `grove_high_output` sea el tuyo la tabla medira bien; **el dia que lo cierres, medira contra otro y
> te sacara filas en ROJO sin que tu cifra este mal.** Cuando pase, **no fuerces el verde**: mueve la
> cifra a una seccion donde su instrumento la cuente contra el libro bueno y **pega la salida roja**,
> que es exactamente lo que la vuelta 42 hizo bien.

**Y SI TU TURNO PASA DE `10` USD**, el acta lo declara con el desglose de en que se fue (`D.55`). No
esta prohibido gastar: **esta prohibido no decir en que**. Deja en tu reporte lo que puedas medir del
reloj, que es lo que el arnes no escribe por ti.

---

## LO QUE NO SE TOCA

- **`scott_radical_candor` esta cerrado.** No abras su bandeja ni sus nodos.
- **El banco no gana reglas nuevas** salvo que una guarda de DATO lo exija con su cita (`D.56`).
- **`config/frentes.json` y `config/umbrales.json`** se leen, no se editan.
- **`gerber_emyth` y `marquet_turn_the_ship` siguen `PAUSADO`** y los toma la serial por su orden,
  no esta vuelta.
- **El bucle no funde ramas y el bucle no crea remotos.**

---

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente,
paras y lo traes. No adivines.
