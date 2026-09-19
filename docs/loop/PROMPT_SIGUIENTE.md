# ENCARGO DE LA VUELTA 44: **LA PRIMERA VUELTA DE SANEAMIENTO DE ESTA LINEA**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta. Escrito por la `ACTA 42`, que audito
la vuelta 43 y adjudico que **ninguna guarda de DATO esta en rojo**.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO QUE HA CAMBIADO BAJO TUS PIES, Y ES LO PRIMERO QUE TIENES QUE SABER

| | |
|---|---|
| **la vuelta 43 metio `1` de `15`, y no fue por dictado** | un cerrojo quedo **huerfano** a las `19:49:07` cuando el tope de diez minutos de una llamada mato al proceso que lo tenia. Desde esa hora **no habia insercion posible**. La medida entera esta en la `ACTA 42` seccion 42.2 |
| **ese cerrojo sigue en el arbol, y NO lo borres a mano** | `src/cerrojo.py` dice que un huerfano *se declara, se rompe y se dice en voz alta*, y que **lo que no se hace nunca es romperlo en silencio**. Su edad ya pasa del tope, asi que **tu primera escritura del dataset lo rompe sola y lo declara**. Tu trabajo es **pegar ese aviso**, no adelantarte a el |
| **esta vuelta NO inserta** | es de **SANEAMIENTO** (`D.55`), la primera de esta linea. Hay `12` deudas pendientes y `0` pagadas |
| **no tienes tarea bloqueante** | ninguna de las cuatro guardas de DATO esta en rojo, asi que la `ACTA 42` **no deja ninguna** |
| **la doctrina sigue congelada** | la cola se queda en `11` (`D.56`). Si encuentras una pregunta nueva, **registrala en tu reporte con su medida y dejala ahi**: no abre parada y no va al banco |
| **lo que la vuelta 43 hizo bien, y no se repite** | sus `17` cifras de apertura, frontera y operacion salieron **las diecisiete al digito**, y sus `2` `SANO` se sostienen los dos. **No vuelvas sobre ellas** |

---

## **POR QUE SANEAMIENTO Y NO OTRA INSERCION, MEDIDO Y NO OPINADO**

    python scripts/deuda.py        lo pendiente, y que clase de vuelta toca

`D.55` paga la deuda **una de cada cinco**, esta linea **no ha pagado ninguna** en doce, y la aduana de
este lote cuesta `8` a `9` minutos por corrida con **dos corridas por candidato**. Una vuelta de
insercion necesita horas de reloj **que el turno no te garantiza**; las doce deudas son correcciones de
texto y ocho aristas, **que caben en un turno corto**. **La deuda no se perdona, se agenda, y la agenda
dice hoy.**

> **Y LA VUELTA 45 VUELVE A INSERTAR**, con la bandeja de `grove_high_output` en `22` y su frontera ya
> publicada y nominada por la `ACTA 42` seccion 42.3.b. **No tendras que volver a medirla.**

---

## TAREA 1. **LOS REGISTROS DE LA `ACTA 42`, Y SON CINCO LINEAS**

*No es reparacion: es recoger lo adjudicado, que `AUDITOR_FORJA.md` 1.4 pone siempre en la TAREA 1.*

| # | lo que la `ACTA 42` adjudico | que haces con ello |
|---|---|---|
| `1.a` | **el cerrojo huerfano NO es averia ni guarda en rojo**: reproducido en controlado con el mismo `pid` y el mismo instante de toma, **se rompe solo y lo declara** (`ACTA 42` 42.2.a) | **nada que reparar.** Lo dices en tu reporte y pasas a la `TAREA 2`, que es donde se cobra |
| `1.b` | **la corrida que sobrevivio a tu turno por `97` s NO es caida**: su codigo fue `1` y su salida literal `INSERCION NO INTENTADA`, asi que **no movio dato** (`ACTA 42` 42.5.b) | **nada que tocar.** Queda registrada como segundo ejemplar de la pregunta `9` de la cola congelada, y anotada como `d012` |
| `1.c` | **`REPORTE` sube a `1 de 3`**: el reporte se quedo en `EE.4` con sus tres filas vacias, sin linea del tramo, sin tabla de cierre, sin `PASOS INVENTADOS` y **sin declarar el cierre corto en `1` de `15`** (`ACTA 42` 42.5.a) | **nada que borrar: el reporte de la 43 se queda como esta.** Tu reporte de hoy **si cierra**, y la `TAREA 5` dice como |
| `1.d` | **el techo de `15` NO fue caida del auditor**, porque la vuelta 42 metio `20` en un turno; pero **un techo en candidatos sin su mitad en minutos no controla nada** (`ACTA 42` 42.7, anotado `d011`) | **nada que tocar hoy.** Esta vuelta no tiene techo de candidatos porque no inserta. **El de minutos lo traes tu**, y esta en la `TAREA 5` |
| `1.e` | **`CLASE`, `CIFRA PUBLICADA` y `DATO MOVIDO` salen LIMPIAS**, y `AUDITOR` sube a `2 de 3` por una caida mia | **nada que tocar.** Lo lees al abrir con `python forja.py credito` y lo citas |

---

## TAREA 2. **EL CERROJO HUERFANO, ROTO POR LA MAQUINA Y DECLARADO POR TI**

**ES LA PRIMERA OPERACION DE LA VUELTA Y NO SE SALTA**, porque cualquier otra tarea que escriba el
dataset se lo va a encontrar antes.

    ls procesos/                          lo que hay antes de tocar nada, y se pega
    cat procesos/*.cerrojo                su pid y su instante de toma, y se pegan

1. **PEGA las dos salidas de arriba ANTES de correr nada**, que es el estado del que partes.
2. **Corre la primera escritura de la `TAREA 3`** y deja que la maquina haga su trabajo.
3. **PEGA LITERAL el aviso que imprima**, que empieza por `CERROJO HUERFANO:` y lleva el `pid`, el
   motivo y los segundos. **Ese aviso es la prueba de la tarea**: sin el, la tarea no esta hecha.
4. **Vuelve a correr `ls procesos/`** y pega su salida.

> **LO QUE NO HACES, Y ESTA ESCRITO EN EL PROPIO `src/cerrojo.py`:** no lo borras a mano. **Romperlo
> con un borrado es romperlo en silencio**, y la unica cosa que ese fichero prohibe por su nombre es
> exactamente esa. Si por lo que sea la maquina **no** lo rompe, **eso si es una guarda de DATO en
> rojo**: lo declaras con su salida pegada, **paras la vuelta ahi** y lo traes.

---

## TAREA 3. **PAGAR LA DEUDA DE TEXTO: `d001`, `d002`, `d003`, `d004` y `d010`**

    python scripts/deuda.py        lee las cinco ENTERAS antes de tocar ninguna

**Cada una se paga por CORRECCION DECLARADA, sin borrar el texto viejo**, que es como esta casa
corrige desde siempre. Las herramientas ya existen y **no se encarga ninguna nueva** (cosecha `7.F`):

    python forja.py corregir --nodo <id> --anade "CORRECCION DECLARADA ..." --razon R
    python forja.py anotar --linea <n> --anade "CORRECCION DECLARADA ..." --razon R

| deuda | lo que pide |
|---|---|
| `d003` | **va la primera de las cinco, y no por orden sino por especie**: es un **PUENTE declarado** en el paso `6` de `variar_frecuencia_inspeccion_nivel_calidad`, o sea materia de fidelidad `D.30`. Reescribelo contra su parrafo del libro **antes de que ese candidato pueda pasar por la aduana nunca** |
| `d001` | corregir sin borrar la cifra `17` a `15`, con su arrastre |
| `d002` | corregir sin borrar el rotulo *ya vive en el grafo* |
| `d004` | los `2` veredictos que la linea `grove` adjudico `CONTINUA` por la via que la deuda nombra |
| `d010` | el `resumen_teorico` de `dar_elogio_disciplina_igual_critica` |

**Y AL PAGAR CADA UNA, MARCALA**, para que la cuenta de `scripts/deuda.py` diga la verdad al cerrar.

---

## TAREA 4. **LAS OCHO ARISTAS DE `d008`, QUE LA `ACTA 41` YA ADJUDICO DECLARABLES**

**No se vuelve a discutir si son declarables: la `ACTA 41` seccion 6.1 lo adjudico y tu vuelta 43 lo
firmo contra la linea impresa del manual.** Lo que quedaba pendiente era **cablearlas**, y hoy es el dia.

    python forja.py arista --madre A --hijo B --paso N --razon R

- **Una por vez, con el paso de la madre citado**, que es lo que `D.29` pide.
- **Si alguna de las ocho ya no se sostiene contra el grafo de hoy, NO la cablees**: dilo en tu reporte
  con el grafo delante. **Una arista que no se sostiene no se pone por cumplir una deuda.**

---

## TAREA 5. **AL CERRAR, Y ESTA VEZ CIERRA**

**Recomputa desde el fichero y no copies tu propia apertura:**

    python forja.py gate
    python forja.py guiones
    python forja.py resolutor
    python tests/test_aceptacion.py
    python scripts/deuda.py
    python scripts/cerrar_reporte.py
    python scripts/tabla_de_cierre.py --escribir      y se pega su salida
    python forja.py tablero --escribir
    python forja.py credito                           lo lees; NO anotes tu propia vuelta

> # **EL TECHO DE ESTA VUELTA ESTA EN MINUTOS, NO EN CANDIDATOS** (`ACTA 42` 42.7, `d011`)
>
> **A LOS `40` MINUTOS DE TURNO, CIERRAS EL REPORTE CON LO QUE TENGAS.** Lo que quede a medias pasa a la
> vuelta siguiente **con su linea escrita**, y eso no es quedarse corto: es cerrar.
>
> **POR QUE ASI, y esta medido:** la vuelta 43 tuvo `3266` s de turno y se gasto los ultimos `600`
> esperando a un cerrojo muerto, **con el reporte sin cerrar**. Un techo en candidatos no la habria
> salvado, porque **el turno no lo eliges tu**. Este si.

**Y ESCRIBE LA LINEA DEL TRAMO, sea cual sea el numero, incluido `0`:**

> *la vuelta cierra en la tarea `N` de `5`; lo que quedaba pasa a la vuelta siguiente.*

**LAS DOS COSAS QUE LA VUELTA 43 NO PUDO ESCRIBIR Y TU SI:**

- **la tabla de cierre `D.52` con su salida pegada**;
- **`PASOS INVENTADOS` desglosado por capitulo**, si esta vuelta toca algun paso. Si no toca ninguno,
  **dilo con esas palabras**: *esta vuelta no escribe pasos nuevos, asi que no hay fila que publicar*.
  **Un `NO APLICA` lleva su salida pegada** (`D.40` ensanchada).

**Y SI TU TURNO PASA DE `10` USD**, el reporte lo declara con el desglose de en que se fue (`D.55`). No
esta prohibido gastar: **esta prohibido no decir en que**.

---

## LO QUE NO SE TOCA

- **`scott_radical_candor` esta cerrado.** No abras su bandeja ni sus nodos.
- **La bandeja de `grove_high_output` NO se inserta esta vuelta.** Sus `22` esperan a la 45. Lo unico
  que tocas de ella es el paso `6` de `d003`.
- **El banco no gana reglas nuevas** salvo que una guarda de DATO lo exija con su cita (`D.56`).
- **`config/frentes.json` y `config/umbrales.json`** se leen, no se editan.
- **`gerber_emyth` y `marquet_turn_the_ship` siguen `PAUSADO`** y los toma la serial por su orden, no
  esta vuelta.
- **El bucle no funde ramas y el bucle no crea remotos.**

---

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente,
paras y lo traes. No adivines.
