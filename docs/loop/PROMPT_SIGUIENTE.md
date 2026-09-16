# ENCARGO DE LA VUELTA 31: **EL ARNES QUE NO ENTREGA LA HERENCIA**, LA ARISTA QUE NADIE JUZGO, Y SEGUIR INSERTANDO EL LOTE 4 POR `cap_11`

*Escrito por el **auditor** al cerrar la **ACTA 29**, que audita la vuelta 30. Sede del auditor
por `AUDITOR_FORJA.md` 5.6.*

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## EL ESTADO CON EL QUE ABRES, MEDIDO POR MI HOY Y NO COPIADO

*Lo mido yo con mis comandos y lo publico para que tu apertura lo cuadre contra el suyo. Si tu
instrumento dice otra cosa, **gana el tuyo y declaras la discrepancia** (`EXTRACTOR.md` 5).*

| | |
|---|---:|
| hash al cerrar mi turno | `b2edb7b` mas los commits de esta acta |
| nodos en `dataset/nodos.jsonl` | **256** |
| veredictos en `bitacora/VEREDICTOS.jsonl` | **375** |
| de ellos, con `no_consumada: true` | **14** |
| aristas del grafo, por los dos extremos | **92** y **92** |
| candidatos en bandeja, lote 4 (`cuarentena/scott_radical_candor`) | **89** |
| ya insertados y archivados, lote 4 | **53** |
| candidatos en bandeja, lote 5 (`cuarentena/marquet_turn_the_ship`) | **3** |
| lote 4 insertado sobre `142` | **37,3 por ciento** |
| pruebas de aceptacion | **193**, `0` fallos |

**`cap_07` QUEDA CERRADO EN INSERCION Y LO FIRMO YO**: `0` candidatos de `cap_07` en bandeja, `25`
nodos del grafo que lo citan, `53` archivados y `53` de esos `53` dentro del grafo
(`.v30c/cierre_cap07.txt`).

**NO SE ABRE NINGUN LOTE** (`D.32`): el lote 4 esta **cerrado en extraccion desde la `ACTA 24`** y lo
que corre es **insercion**, con `89` en bandeja. **No hay condicion de apertura que medir porque no
hay lote que cerrar.** El lote 5 sigue con sus `3` sin tocar, y **sigue sin tocarse** (`D.39`).

**`PASOS INVENTADOS POR CAPITULO` de la vuelta 30, firmada por mi**: `cap_07` **`0,00`** por ciento
sobre `90` pasos, `cap_11` **`0,00`** sobre `6`. **El freno de fidelidad no se activa. El que aprieta
es el reloj de la aduana**, y por eso este encargo **no sube el numero de candidatos**.

---

## TAREA 1. LOS REGISTROS DE LA `ACTA 29`, Y SUS DOS CORRECCIONES DECLARADAS

**1.a. Anexa al reporte la fila de registros** con lo que esta acta adjudica, sin rehacer mis
medidas:

- **los `8` discutibles de `W.6`: SOSTENIDOS LOS OCHO.** Cero caidas dentro del marcado.
- **`16` relecturas pineadas (semilla `300916`): las `16` se sostienen.** Tasa de caida de `CLASE`
  `0,00` por ciento, **banda al 95 por ciento de `0,00` a `17,07`**.
- **las `3` propuestas, adjudicadas**: la `1` queda registrada y **no se encarga** (moratoria `5.6`);
  la `2` **queda adjudicada por `EXTRACTOR.md` 9** y la consecuencia es la buscada; la `3` va dentro
  de la `TAREA 2`.
- **mi unica caida cargada contra ti**: `REPORTE`, la cita `ACTA 28` `2.2` que es `ACTA 27` `2.2`
  (`ACTA 29` `7.1`). **La racha `REPORTE` queda en `1 de 3`; `CLASE` y `CIFRA PUBLICADA` en `0 de 2`
  las dos.**

**1.b. CORRECCION DECLARADA en `docs/BANCO_DE_REGLAS.md`, `D.38.4`, SIN BORRAR EL TEXTO VIEJO**
(`D.13`: entre dos reglas fechadas que chocan gana la mas reciente, y la perdedora se corrige sin
borrarse).

> Lo que se escribe, tachando en su sitio y con el texto vigente al lado: **la receta de construir a
> mano la poblacion del barrido como grafo mas bandejas queda superada por `D.38.5`**, que llego a
> `src/aduana.py` el 16 sep. **Corrida al pie de la letra hoy cuenta las bandejas dos veces** (`440`
> en vez de `348`) **y tumba al candidato por la guarda `el id ya vive en el grafo`**, porque acaba
> dentro de su propia poblacion. **El barrido se hace entregando a la aduana la poblacion del grafo
> y dejando que ella ponga las bandejas.** Medido en `ACTA 29` `6.6`.

**1.c. CORRECCION DECLARADA en la linea `300` de `bitacora/VEREDICTOS.jsonl`, con
`python forja.py anotar`, SIN TOCAR LA CLASE.** Su razon cita `la ACTA 28 2.2` y la adjudicacion que
describe vive en **`ACTA 27` `2.2`**. **El veredicto `SANO` es correcto, lo reverifique, y no se
toca**: lo unico que se aniade es la correccion del puntero.

---

## TAREA 2, **BLOQUEANTE**: EL ARNES NO ENTREGA LOS REMEDIOS QUE `D.40` LE MANDA ENTREGAR

*`D.40` es del fundador y dice: **lo que un auditor le deja al siguiente lo entrega el arnes, no la
memoria.** Hoy lo mido y no lo cumple. **No es maquinaria nueva: es que un mecanismo ya ordenado haga
lo que su regla dice**, y lo exige una caida de esta misma tanda con su cita (`ACTA 29` `8.1`).*

**2.a. EL DEFECTO, MEDIDO:**

    $ python forja.py herencia
      HEREDADO 1   [REMEDIO, linea 25541 del acta]  ->  ACTA 28 seccion 3.2
      HEREDADO 2   [REMEDIO, linea 25794 del acta]  ->  ACTA 28 seccion 6.1

**Las secciones `3.2` y `6.1` de la `ACTA 28` no ESCRIBEN remedios: CITAN los de la `ACTA 27` para
decir que se cumplieron.** Los remedios que la `ACTA 28` escribe de nuevo estan en **la tabla que
precede a su seccion `9`**, y son otros dos. **El extractor de `src/herencia.py` se queda con las
secciones que mencionan la palabra y no con la tabla que los declara.**

**2.b. LO QUE HAY QUE HACER:** que `src/herencia.py` entregue **los remedios que el acta ESCRIBE**, no
los que CITA. La `ACTA 29` deja su tabla en la seccion `8.5` con la misma forma que la `ACTA 28` uso
en la suya, asi que **hay dos actas con las que probar**.

**2.c. CASO POSITIVO, OBLIGATORIO** (cosecha 7.C: una guarda que no muerde es cifra):

- corrido contra la **`ACTA 28`**, tiene que devolver **los dos remedios de su tabla** (el de la celda
  de la apertura sellada y el de la razon por vez), **no** sus secciones `3.2` y `6.1`;
- corrido contra la **`ACTA 29`**, tiene que devolver **los tres de su `8.5`**;
- y una prueba en `tests/test_aceptacion.py` que **falle** si el extractor vuelve a coger una seccion
  que solo menciona la palabra.

**2.d. Y LA OTRA MITAD DEL ARNES, que es la propuesta `3` del reporte:** `D.43` extendida el 16 sep
manda que **la cola de vecinos por candidato llegue sellada al turno**, y esta corrida no la trajo:
no existe fichero de cola en `docs/loop/`. **Lo que costo no traerla esta medido: `26` corridas de la
aduana dentro del turno, de entre `63` y `136` segundos cada una.** Si no cabe en esta vuelta,
**declaralo con su cifra y no lo dejes callado.**

---

## TAREA 3. LA ARISTA `D.29` QUE EXISTE, QUE NADIE JUZGO Y QUE HOY SE PUEDE CABLEAR

**Ya esta adjudicada por mi** (`ACTA 29` `6.2`): **adjudicar no es medir, asi que la clase la pongo yo
y tu la ejecutas.**

    madre : cuidarse_agotamiento_centro_rueda        paso 7
            Bloquea en tu calendario tiempo de pensar todos los dias.
    hija  : bloquear_tiempo_pensar_calendario        6 pasos que despliegan esa frase entera

**Los dos extremos viven en el grafo**, asi que se cablea hoy y no queda en cola.

    python forja.py arista --madre cuidarse_agotamiento_centro_rueda \
                           --hijo  bloquear_tiempo_pensar_calendario --paso 7

**Y LO COMPRUEBAS POR LOS DOS EXTREMOS EN `dataset/nodos.jsonl`, no por la prosa de la salida**, que es
lo que la vuelta 30 hizo bien en su `W.2.h`.

**POR QUE ESTA AQUI Y NO ES CAIDA TUYA:** la aduana levanto **cinco** vecinos para
`bloquear_tiempo_pensar_calendario` y `cuidarse` no estaba entre ellos, **asi que no hubo veredicto que
poner mal.** La cazo mi fase ciega leyendo. **Es `D.19` haciendo exactamente lo que dice de si misma.**

---

## TAREA 4. SEGUIR INSERTANDO EL LOTE 4, POR `cap_11` Y POR EL ORDEN DEL LIBRO

**El lote 4 esta cerrado en extraccion y `cap_07` cerrado en insercion. Lo que sigue es `cap_11`**, de
donde ya entro `bloquear_tiempo_pensar_calendario` (`L165-173`).

**4.a. Genera el orden del propio dato y no lo teclees**, como hiciste en `W.2.d`: lee el rango de
`cap_11.md` del `resumen_teorico` de cada fichero de la bandeja y ordena por el. **Publica la tabla del
instrumento entera.**

**4.b. LA RELECTURA DE FIDELIDAD `D.30` VA ANTES DE LA PRIMERA INSERCION**, como siempre, **y publicas
`PASOS INVENTADOS POR CAPITULO` con su fila de `cap_11`**, que yo firmo.

**4.c. EL TRAMO NO SUBE.** `PASOS INVENTADOS` esta en `0,00` y permitiria subir un escalon, **pero el
freno que aprieta es el reloj**: `26` corridas de aduana se comieron la vuelta 30, y una sola corrida
en seco sobre un candidato me paso hoy de `120` segundos. **Si la insercion se come la vuelta, cierras
ahi y lo declaras con su cifra** (`EXTRACTOR.md` 12.4).

**4.d. Y ESTA ES LA PARTE QUE NO SE PUEDE APLAZAR, CON FECHA DE CADUCIDAD:**

> **EN EL ACTO EN QUE `pelear_proliferacion_reuniones_bloquear_ejecucion` PASE LA PUERTA, DECLARAS SU
> ARISTA POR LECTURA.** Yo ya la adjudique (`ACTA 29` `6.1`):
>
>     madre : reservar_calendario_tiempo_ejecutar              (cap_07 L385-387, ya en el grafo)
>     hija  : pelear_proliferacion_reuniones_bloquear_ejecucion (cap_11 L225-233, en bandeja)
>
> **`CONTINUA`, y la hija aniade los tres remedios que el libro prueba y descarta, la solucion de
> combatir fuego con fuego, y el encargo al equipo.**
>
> **POR QUE NO PUEDE ESPERAR:** lo corri hoy y la aduana **lo deja entrar SIN MANDAR LEER NADA**
> (`.v30c/informe_pelear.txt`, poblacion `348`, `ENTRARIAN sin leer nada: 1`). **Las tres seniales lo
> dan por desconocido en las dos direcciones.** Si entra sin la declaracion, **no habra ninguna corrida
> que vuelva a ponerlos juntos.**

---

## TAREA 5. LA COLA ENTERA, RECONTADA FILA A FILA CONTRA EL DATO

*Va entera **porque ya se perdio una vez** y porque `ACTA 29` `6.5` mide que la marca `arista_en_cola`
la escribe la aduana y **no la lee nadie**: la cola la vacia una mano, y la mano es esta fila.*

| lo que queda | cifra que yo mido hoy | que la cierra |
|---|---:|---|
| arista en cola `crear_espacio_seguro_madurar_ideas_nuevas > nutrir_ideas_nuevas_reunion_solas` | **1** | que entre el HIJO, en bandeja del lote 4 |
| arista en cola `desplegar_plan_orden_operaciones_franqueza_radical > bloquear_tiempo_pensar_calendario` | **1** | que entre la MADRE, en bandeja del lote 4 |
| las entradillas de `LISTEN`, `CLARIFY` y `DEBATE` de `cap_07` sin nodo | **3** de **7** rotulos | **NADA: adjudicado que es la consecuencia buena** de `EXTRACTOR.md` 9 (`ACTA 29` `5`). Queda como registro, no como deuda |
| `L221` de `cap_07`, *Your job as a boss is to turn on that rock tumbler* | **1** tramo | **NO se toca**: `cap_07` esta cerrado en insercion y reabrirlo pide una decision de alcance. **Queda anotado y nombrado** (`ACTA 29` `6.8`) |
| el hueco de transcripcion de `L153` | **1** modo de **3**, en **1** nodo | sigue **SIN VIA**: con un solo ejemplar no se construye |
| `cap_04` releido, `6` candidatos y `48` pasos | **6** y **48** | sigue sin caber, **y lo declaras otra vez con su motivo si no cabe** |
| la frontera por capitulo con las `QUESTIONS TO CONSIDER` | **14** de **17** unidades | la vuelta que mine un capitulo del lote 5 |
| las `8` lineas `SIN HUELLA` de `D.15` | **8**, **las 8 declaradas** | **CERRADA**, y lo verifique por diferencia. Lo que sigue imprimiendo `8` es el instrumento, no el trabajo |
| bandeja del lote 4 | **89** | la insercion |
| lote 5 | **3** | **NO TOCAR** (`D.39`) |

**Y RECUENTALA TU CONTRA EL DATO, no contra esta tabla.** Si una cifra mia no te sale, **gana la tuya y
declaras la discrepancia.**

---

**Son CINCO tareas y el tope son cinco** (`EXTRACTOR.md` 1.3). **La `TAREA 2` es BLOQUEANTE y va antes
que la insercion**: mientras el arnes no entregue los remedios que `D.40` le manda entregar, **el
siguiente auditor va a romper el suyo igual que lo rompi yo**.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente,
paras y lo traes. No adivines.
