LIBRO DE ESTA VUELTA: marquet_turn_the_ship

# ENCARGO DE LA VUELTA 7 DEL FRENTE `marquet_turn_the_ship`: **SANEAMIENTO. `d098`, EL BARRIDO ENTERO DE `d104` Y LA CUENTA DEL LIBRO**

*Linea **`marquet_turn_the_ship`** (`extraccion-marquet_turn_the_ship`, worktree
`C:/Users/AlexDesk/Documents/forja-marquet_turn_the_ship`). Escrito por el auditor al cerrar la
**`ACTA M7`**, que audita tu vuelta `6`. `MODO_INSERCION=cuarentena`, regimen ligero.*

> # **LIBRO DE ESTA VUELTA: `marquet_turn_the_ship`**
> # **CLASE DE ESTA VUELTA: SANEAMIENTO** (`python scripts/deuda.py --clase 7` da `SANEAMIENTO`: *han pasado 5 vuelta(s) desde la primera vuelta de la linea*)

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **TU TURNO ACABA CUANDO TU TRABAJO ACABA. TU VUELTA `6` NO LO CUMPLIO, Y ESTA VUELTA ES CASI ENTERA DE ESO**

Tu vuelta `6` **termino el turno con tres `forja.py informe` corriendo de fondo** y el mensaje *I'll pause
here and pick back up when it completes*. **No hay "despues" para ti: cuando tu turno acaba, acaba.** No
escribiste cierre, ni credito, ni paradas, ni commit. **Los tres informes los dejo terminar y los recogio tu
auditor** (`ACTA M7` `M7.9`); si nadie lo hubiera hecho, se habrian perdido.

**LA REGLA, SIN EXCEPCION:** puedes lanzar en paralelo, **pero te quedas en el turno vigilando hasta
recoger cada tanda entera**, con un bucle que espere a que terminen los procesos (por ejemplo, `wait` dentro
del mismo comando, o un bucle `until` que compruebe los ficheros de salida y los procesos vivos). **Lanzar y
terminar el turno es la caida.** **Si algo no cabe, NO lo lances: dilo en tu reporte con la lista exacta.**

**Y ESCRIBE EL CIERRE ANTES DEL BARRIDO LARGO, NO DESPUES:** en cuanto termines la `TAREA 2`, deja escrita
en el reporte una seccion de cierre provisional (credito, paradas, lo que queda), y ve reescribiendola al
cerrar cada tanda. **Si el turno se corta, lo que quede escrito sera verdad.**

---

## TAREA 1. **REGISTROS: EL ACTA M7**

**Lee la `ACTA M7`** (`docs/loop/ACTA_AUDITOR.md`, al final). Lo que te toca:

- **`REPORTE` BAJA de `2 de 3` a `0 de 3`** (`M7.10`): tu tanda sale limpia de la especie que acumula. **La
  adjudicacion va contra la lectura que te costaba la parada, y lo que la sostiene es que tu cabecera dijo
  `PENDIENTE` y no prometio nada** (`M7.8`). **Una cabecera que diga `CERRADA` sobre una tarea a medias SI
  acumula, y con `0 de 3` no te para, pero te sube.**
- **EL REMEDIO DE `M6.9.a` QUEDA CUMPLIDO Y MEDIDO POR MUTACION** (`M7.3`): tus dos fronteras son las brutas y
  el tallado las muerde. **Asi se hace.**
- **LO QUE SE CAYO Y NO ACUMULA** (`M7.7`): prometiste un `cerrar_reporte.py` *al cierre (`C.1`)* que no
  existio, y tu `LECTURA` de `cap_16` pone `R3` como residuo y `R6` y `R7` en dos clases a la vez. **No
  prometas una seccion que no has escrito.**
- **Tu discutible se sostiene; `cap_16` y `cap_17` estan firmados en cero** (`M7.4`, `M7.5`). **La firma en
  `config/frentes.json` la pide el reporte a la sesion: tu no la escribes.**

---

## TAREA 2. **`d098`: EL PASO 1 DE `ceder_control_reforzar_competencia_claridad`**

`d098` (`ACTA M3` `M3.2`, remedio `4` de la `ACTA M2`): *el paso 1 de
`ceder_control_reforzar_competencia_claridad` se reescribe o se retira antes de que ese nodo entre al
grafo.* **La cosecha de este libro es la siguiente parada: vence ahora.**

1. **Lee el remedio `4` de la `ACTA M2`** (`docs/loop/archivo/marquet_turn_the_ship/ACTA_AUDITOR_frente_hasta_M2.md`) y el paso contra su
   linea del libro.
2. **Reescribelo con cita literal en su linea, o retiralo**, y dilo con la linea delante (`D.30`).
3. **VA ANTES DEL BARRIDO, Y ES A PROPOSITO** (`d103`): cambiar una ficha cambia sus vecindades con todas, asi
   que **ninguna aduana de la bandeja se corre antes de que esta ficha quede escrita**.
4. Paga: `python scripts/deuda.py --pagar d098 --vuelta 7 --como "..."`.

**Si al leerlo el paso resulta estar ya bien, no lo toques: dilo con la cita, y paga `d098` con eso.**

---

## TAREA 3. **`d104`: EL BARRIDO DE LA BANDEJA ENTERA, CON EL TEXTO FINAL**

**Las `20` fichas de `cuarentena/marquet_turn_the_ship/`, una por una**, cada una a su fichero:

    python forja.py informe cuarentena/marquet_turn_the_ship/<ficha>.json > .v7m/aduana/<ficha>.txt

**EL RELOJ, MEDIDO:** tres informes en paralelo tardaron `569`, `808` y `1113` s sobre poblacion `479`
(`ACTA M7` `M7.9`), y antes `690`, `859` y `1198` (`ACTA M6` `M6.7`). **LECTURA de tu auditor, no medida:**
veinte en tandas de tres son unas siete tandas de hasta veinte minutos. **Tandas de hasta CINCO en paralelo
si quieres ir mas rapido, pero la de cinco nadie la ha medido: cronometrala.**

- **Cada tanda se RECOGE ENTERA antes de lanzar la siguiente, y se recoge DENTRO DEL MISMO COMANDO** (un
  `wait` al final, o un bucle que espere): **nunca lances una tanda y termines el turno.**
- **Los tres ficheros de `.v6m/aduana/`** (`asignar_responsable`, `acoger_inspectores`, `aplicar_ejercicio`)
  **se midieron ANTES de `d098`**. Si la `TAREA 2` no cambio ninguna ficha, **puedes reusarlos** diciendolo; si
  la cambio, **se vuelven a correr** como las demas.
- **Lo que publicas:** el saldo de las `20` (`ENTRARIAN`, `BLOQUEARIAN`, `CAERIAN`, `CHOCAN`), y **por cada
  vecindad que cambie respecto a la ultima aduana guardada de esa ficha** (`.vm01/`, `.m2/`, `.m4aud/` a `.m6aud/` y `.v3m/` a `.v6m/`), cual era y cual
  es. **Bajo `$` va solo lo que el comando imprime.**
- **Cada par en banda alta (`0,4` en adelante) lo lees por sus pasos** (`EXTRACTOR.md` `11`) y lo marcas
  discutible si dudas. Ya hay tres esperandote: `acoger_inspectores` contra `tomar_accion_deliberada`
  (`0.457`), contra `resistir_dar_solucion` (`0.412`) y contra `declarar_intencion` (`0.406`).
- **Si lo acabas:** `python scripts/deuda.py --pagar d104 --vuelta 7 --como "..."` y `--pagar d103` si
  ninguna ficha cambio despues de su aduana. **Si no, lista exacta de fichas sin barrer, y `d104` sigue viva.**

---

## TAREA 4. **LA CUENTA DEL LIBRO**

**Contada con un instrumento y con su salida pegada**, una fila por capitulo, `cap_01` a `cap_17`: candidatos
en bandeja por `UNIDAD DE ORIGEN`, pasos, y los capitulos en cero con la sede que los firma (acta y linea).
**Y di con la cifra delante si la extraccion de `marquet_turn_the_ship` esta CERRADA.** Hazla **mientras
corre una tanda de la `TAREA 3`**, no despues: es barata y no toca ninguna ficha.

**Si lo esta, NO cosechas, NO fundes y NO insertas** (`D.39`, `D.50`, decision del `22` sep punto `4`). Lo
dejas medido para que tu auditor escriba la parada de campaña consumada.

---

## LO QUE NO HACES

- **NO INSERTAS.** `MODO_INSERCION=cuarentena`.
- **NO TOCAS LA MAQUINARIA** (`D.45`): `orquestador_forja.sh`, `src/`, `scripts/`, `tests/`, `hooks/`,
  `esquema/`, **ni `config/`**. `d094`, `d095` y `d096` son de maquinaria y **no son tuyas**.
- **NO ESCRIBES DOCTRINA.** Si hace falta regla nueva, es parada.
- **NO TOCAS `cuarentena/grove_high_output/` NI `cuarentena/gerber_emyth/`**: son poblacion de tu aduana.
- **NO TOCAS NINGUNA FICHA salvo la de `d098`.**

## AL CERRAR

- **Declara la vuelta de saneamiento:** `python scripts/deuda.py --saneamiento --vuelta 7`.
- **Tu tanda**: `python forja.py credito --anotar`, **con `--cae` o `--limpia` en cada especie, coherente con
  tu tabla.**
- **`D.61`**: cada discutible ejecutado o cerrado con su motivo.
- **Commitea `docs/loop/`, `cuarentena/marquet_turn_the_ship/` y `.v7m/`.**
- **Mide las condiciones de parada una a una** y publica que las mediste. **No escribas `PARA_ALEXIS.md`**.
- **Y ANTES DE TERMINAR, COMPRUEBA QUE NO TIENES NINGUN PROCESO VIVO** y pega la comprobacion.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No adivines.
