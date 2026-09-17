# PARA_ALEXIS: **el frente `gerber_emyth` para en su vuelta 1 por DOCTRINA NUEVA NECESARIA, y sube DOS cosas**

*Escrito por el auditor del bucle al cerrar la `ACTA G1` de `docs/loop/ACTA_AUDITOR.md`, el 17 sep
2026. Condicion de parada: `AUDITOR_FORJA.md` 3, primera fila. `docs/loop/PROMPT_SIGUIENTE.md` queda
VACIO por mandato de esa misma seccion.*

> ## **LA VUELTA NO ESTA MAL. LA VUELTA ESTA BIEN Y LO DIGO ANTES DEL MOTIVO.**
>
> `11` de `11` fronteras cierran al digito contra mi propio codigo, mis diez clases ciegas y las suyas
> **coinciden en las diez**, los `89` pasos releidos uno a uno **no traen ni un puente**, los diez
> dictamenes de la aduana me salen **identicos**, y la vuelta **no movio ni un fichero de dato ni uno
> de la moratoria**. **Lo que para el frente no es la calidad del trabajo: es una pregunta que yo no
> puedo contestar sin inventar doctrina, y en un frente eso es parada.**

---

## 1. EL MOTIVO PRINCIPAL: **NO SE DE QUIEN ES LA RACHA CUANDO HAY CUATRO SESIONES A LA VEZ**

**El estado de hecho, medido y no recordado:**

    $ git log -1 --format="%h %ad %s" --date=format:'%m-%d %H:%M' origin/extraccion-mundo-11
    8e453d3 09-16 22:21 @ ACTA 31, VUELTA 32: PARADA POR CREDITO ROTO. REPORTE llega a 3 de 3 y el bucle se detiene
    $ git merge-base HEAD origin/extraccion-mundo-11
    269c068ed604607c4d7c64057afeddba18c5eb42

**La rama de insercion declaro PARADA por `REPORTE` a `3 de 3`** (vueltas `30`, `31` y `32`) a las
`22:21` del 16 sep. **Este frente ya llevaba una hora y cuarto corriendo**, salio del commit
`269c068` de las `20:46`, y **su arbol no puede ver esa acta ni esa parada.**

**Y esta tanda mia NO sale limpia de `REPORTE`**: el reporte cita una seccion `G1.10.e` que no existe
en el documento, en una celda de tabla (`ACTA G1` `4.1`). **Asi que la pregunta es inevitable, y
tiene dos respuestas legitimas con consecuencias opuestas:**

| lectura | `REPORTE` tras esta tanda | que pasa con los tres frentes |
|---|---|---|
| **(a) la racha del extractor es UNA sola de la campana** | sigue en **`3 de 3`**: esta tanda no la reinicia | **los tres frentes estan corriendo por encima de una parada** |
| **(b) cada frente lleva la suya** | **`1 de 3`**, primera tanda de este frente | los frentes siguen, y la parada es solo de la rama serial |

**POR QUE NO LA ADJUDICO YO.** `5.2` y `D.38.1` cuentan **tandas SEGUIDAS**, y *seguidas* significa
consecutivas: **cuatro sesiones simultaneas no tienen orden entre si**, asi que la palabra que
sostiene la regla no tiene referente aqui. No es una regla que se pueda extender: **es un hueco.** Y
`5.4` cierra la otra puerta: **la racha no se reinicia sola**, y **ninguno de los dos que pueden
reiniciarla soy yo.**

**Elegir `(b)` seria absolverme para poder seguir. Elegir `(a)` seria cargarle a este frente tres
tandas de un libro que no es el suyo.** `D.45`, `PARALELO.md` 4 y el propio encargo de este frente
dicen lo mismo: **una pregunta de doctrina, cualquiera, es parada y sube.**

### LO QUE NECESITO DE TI, en una linea

> **Di si la metrica de credito de `AUDITOR_FORJA.md` 5 lleva UN contador por campana o UNO POR
> FRENTE mientras dure el paralelo, y si la parada de la `ACTA 31` alcanza a los tres frentes o solo
> a la rama de insercion.** Con eso escribo el numero y el bucle sigue.

---

## 2. LO SEGUNDO, Y ES OPERATIVO: **UNA LINEA DEL ARNES QUE `D.43` DEJO VIEJA EL 12 SEP LE ESTA COSTANDO UNA HORA A CADA FRENTE**

    $ grep -n -o "Al cerrar el capitulo corres el informe del lote entero y pegas su saldo en el reporte." orquestador_forja.sh
    439:Al cerrar el capitulo corres el informe del lote entero y pegas su saldo en el reporte.
    $ git log -1 --format="%h %ad" --date=format:'%Y-%m-%d %H:%M' -S"Al cerrar el capitulo corres el informe del lote entero" -- orquestador_forja.sh
    757870d 2026-09-09 23:40
    $ git log -1 --format="%h %ad" --date=format:'%Y-%m-%d %H:%M' -S"EL ARNES CORRE EL INFORME DE LOTE EL MISMO" -- docs/BANCO_DE_REGLAS.md
    5ba8be1 2026-09-12 19:19

**Esa frase vive en `MANDATO_INSERCION`, en la rama de `MODO_INSERCION=cuarentena`, que es la que
reciben LOS TRES FRENTES DEL PARALELO.** Es del **9 sep**. `D.43`, que saca ese informe del turno del
extractor porque **no cabe en un turno**, es del **12 sep**. **Por `D.13` gana `D.43`, y la linea
esta vieja.**

**LO QUE COSTO, medido en esta vuelta:** el extractor la obedecio, lanzo el informe del lote a las
`23:14:06`, y **no termino**: `.gerber_v1/informe_de_lote.txt` tiene `91` bytes y solo la cabecera.
Antes habia perdido `100` segundos matandolo para relanzarlo. **Es exactamente el ejemplar de `480`
bytes que motivo `D.43`, repetido.**

**NO LA TOCO YO:** `orquestador_forja.sh` es el arnes, y `D.45` prohibe tocarlo desde un frente
**aunque haya caida**. **Los otros dos frentes (`grove_high_output` y `marquet_turn_the_ship`) la
estan recibiendo ahora mismo.**

### LO QUE NECESITO DE TI

> **Retira o acota esa frase de `orquestador_forja.sh` L439**, o di expresamente que `D.43` no rige
> en modo cuarentena. **Mientras siga, cada frente gasta su turno en un instrumento de una hora que su
> propia regla ya le quito.**

---

## 3. EL ESTADO EXACTO

| pieza | valor | de donde |
|---|---|---|
| rama | `extraccion-gerber_emyth` | `git rev-parse --abbrev-ref HEAD` |
| hash al cerrar esta parada | `4c4a616` | `git rev-parse --short HEAD` |
| nodos en el grafo | **270** | `wc -l dataset/nodos.jsonl` |
| veredictos | **396** | `wc -l bitacora/VEREDICTOS.jsonl` |
| **ficheros de dato movidos por el frente** | **0** | `git diff --name-only 272e8ce..HEAD` |
| fase | **lote 9 ABIERTO en extraccion**, `11` de `22` unidades minadas (`cap_01` a `cap_11`) | `ls .gerber_v1/piezas_cap*.txt` |
| bandeja de `gerber_emyth` | **10** candidatos, **89** pasos, **0** insertados | `ls cuarentena/gerber_emyth/*.json` |
| aduana del lote entero, corrida por mi | `3` ENTRARIAN, `7` BLOQUEARIAN, **`0` CAERIAN**, **`0` CHOCAN** | `ACTA G1` seccion `2` |
| `PASOS INVENTADOS`, peor capitulo | **`0,00`** contra un tope de `10` | `ACTA G1` seccion `5` |
| guardas hoy | `gate` VERDE con `270`, `guiones` VERDE, `201` pruebas y `0` fallos, tallado VERDE con `75`, censo VERDE con `554` | `ACTA G1` seccion `1` |
| racha propia del auditor | **`1 de 3`** (`REMEDIO ROTO`, declarado por mi en `ACTA G1` `6`) | `ACTA G1` seccion `6` |

---

## 4. **LA PARADA VIEJA DE ESTE MISMO FICHERO, DECLARADA Y NO BORRADA**

**Este fichero decia, desde las `21:19` del 16 sep, que el testigo de guardas desmentia el sello**, con
la guarda `guiones` en ROJO por cuatro caracteres del `citas.py` del extractor, contra el commit
`6d2d56a`. **Ese motivo esta CADUCADO y lo mido en vez de afirmarlo:**

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ tail -1 docs/loop/SELLOS_APERTURA.jsonl
    {"vuelta": 1, "fecha": "2026-09-17 00:47:11", "sello": "845bd79445134e955c6bf5a5ff4ad391cf9d1cea"}

**La causa la declaro y la reparo el propio extractor en el commit `b820215` (`G1.5`), y el arnes
volvio a sellar y ACEPTO** a las `00:47:11`. **El extractor hizo bien en no borrar este fichero**:
esa sede es del auditor. **Lo sustituyo yo hoy, con su texto viejo declarado aqui**, que es lo que
esta casa hace con lo que caduca.

---

## 5. **EL REMEDIO QUE VA ENCARGADO AQUI, PORQUE EL ENCARGO QUEDA VACIO** (`AUDITOR_FORJA.md` 5.5)

**LO PRIMERO QUE ESTE FRENTE HACE AL RETOMAR, antes de minar nada:**

1. **Correccion declarada en `docs/loop/REPORTE.md`, sin borrar y CON TACHADO EN SU SITIO**, de tres
   celdas: la de `G1.10.d` que cita `G1.10.e` (seccion que no existe), la fila `CERRADO` del esqueleto
   `G1.0`, y la apertura de `G1.9` que promete un saldo que no llego. **El saldo que faltaba ya esta
   medido y publicado en la `ACTA G1` seccion `2`: se cita de ahi, no se vuelve a correr.**
2. **Antes de cerrar cualquier reporte, correr `python .v1g_auditor/secciones.py`**, que son catorce
   lineas y compara **toda seccion que el bloque cita contra las que el bloque tiene**. Hoy da `1`
   ausente. **Tiene que dar `0` para cerrar.** No es maquinaria nueva: el instrumento ya existe y
   viaja en este commit.
3. **El tramo de la vuelta siguiente es `5` candidatos, el suelo del rango, y arranca en `cap_12`.**
   Lo manda `EXTRACTOR.md` 12.4 (la vuelta no cerro su reporte en su turno), **no la metrica de
   volumen**, que con `0,00` de peor capitulo dejaria subir. **Y el encargo siguiente NO debe pedir el
   informe del lote entero**, por el punto `2` de arriba.

---

## 6. COMO RETOMAR

1. **Contesta el punto `1`** (un contador o cuatro) y **el punto `2`** (la linea del arnes). Las dos
   caben en dos frases.
2. **Archiva esta parada** en `docs/loop/paradas/2026-09-17-la-racha-en-paralelo.md`, como las
   anteriores, y **borra este fichero**.
3. **Escribe `docs/loop/PROMPT_SIGUIENTE.md`** con el tramo de `5` y los tres puntos del remedio de
   la seccion `5`, o dime que lo escriba yo con tu respuesta delante.
4. **Relanza el frente** tal como lo lanzaste:

        cd /c/Users/AlexDesk/Documents/forja-gerber_emyth && \
          RAMA=extraccion-gerber_emyth MODO_INSERCION=cuarentena MAX_VUELTAS=20 \
          bash orquestador_forja.sh

**LO QUE NO HE HECHO Y NO VOY A HACER:** fundir esta rama, tocar el arnes, tocar el banco, mover un
umbral, insertar un candidato o borrar la parada vieja sin declararla. **El bucle no funde ramas y el
bucle no crea remotos.**
