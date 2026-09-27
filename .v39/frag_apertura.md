
---

# VUELTA 39, **cerrar el reporte**, y **`cap_13` a tres** (lote 4, `scott_radical_candor`)

*Encargo en `docs/loop/PROMPT_SIGUIENTE.md`. Cuatro tareas, bajo el tope de cinco (`EXTRACTOR.md` 1.3).
Vuelta en **MODO AUSTERO** (`D.47`), con `MODO_INSERCION=insertar` sobre un lote **CERRADO EN
EXTRACCION** (`D.39`). **La `TAREA 2`, la fidelidad `D.30` de los tres, corre ANTES de la primera
insercion** (`EXTRACTOR.md` 15.4), y la `TAREA 1` entera es lo primero del turno porque el encargo la
marca bloqueante por partida triple: **el orden de ejecucion no es el de numeracion y lo digo aqui.**

> ## **EL PREFIJO DE MIS SECCIONES ES `CC`, Y EL ENCARGO ME PIDE ABRIR `BC.6`: LO DIGO EN VEZ DE ELEGIR EN SILENCIO**
>
> La `TAREA 4` manda *abre `BC.6` antes de insertar el primer candidato*. **`BC` es el prefijo de la
> vuelta 38**, no el mio: las vueltas 34 a 38 corrieron `AA`, `AB`, `AC`, `AC` y `BC`, asi que **esta
> vuelta abre `CC`** y la seccion que el encargo ordena es **`CC.6`**, en el mismo numero que pide.
>
>     $ grep -oE "^## [A-Z]{2}\." docs/loop/REPORTE.md | sort -u
>     ## AA.
>     ## AB.
>     ## AC.
>     ## BC.
>
> **No es una licencia: es que escribir `BC.6` dentro de la vuelta 39 pondria dos vueltas bajo el mismo
> prefijo**, que es exactamente lo que ya paso entre la `36` y la `37` con `AC`. **Lo que el encargo
> compra con ese numero (una seccion abierta ANTES de la primera insercion, con una fila por candidato
> escrita en el acto) lo entrego entero.** Si el auditor prefiere la letra literal, que lo adjudique:
> la eleccion esta escrita aqui, con su medida al lado.

## CC.0. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (`EXTRACTOR.md` 4)

**La primera operacion de mi turno es el commit del arnes pendiente** (`EXTRACTOR.md` 1.1), asi que esta
tabla se lee **justo despues de ese commit y antes de la primera tarea**: el commit que cita es ya estado
intermedio y lo digo. **Arranco de `321` nodos y `486` veredictos, como el encargo anuncia**, y los `2`
nodos y `7` veredictos que el auditor commiteo por mi **no los cuento como trabajo de hoy.**

<!-- TALLADO: script=.v39/apertura.py salida=.v39/apertura_tabla.txt -->

| pieza | valor | de donde sale |
|---|---:|---|
| rama | extraccion-mundo-11 | `git rev-parse --abbrev-ref HEAD` |
| commit al abrir mi turno | `e3950c6` | `git rev-parse --short HEAD` |
| nodos en `dataset/nodos.jsonl` | **321** | `dataset/nodos.jsonl` |
| veredictos en `bitacora/VEREDICTOS.jsonl` | **486** | `bitacora/VEREDICTOS.jsonl` |
| de ellos, con alguna anotacion `no_consumada: true` | **14** | `bitacora/VEREDICTOS.jsonl` |
| aristas por `nodos_siguientes` | **129** | `dataset/nodos.jsonl` |
| aristas por `nodos_previos` | **129** | `dataset/nodos.jsonl` |
| candidatos en bandeja, lote 4 | **24** | PATRON: `cuarentena/scott_radical_candor/*.json` |
| insertados y archivados, lote 4 | **118** | PATRON: `cuarentena/_insertados/scott_radical_candor/*.json` |
| candidatos en bandeja, lote 5 | **3** | PATRON: `cuarentena/marquet_turn_the_ship/*.json` |
| lote 4 insertado sobre `142`, por ciento | **83,1** | `cuarentena/_insertados/scott_radical_candor/` |

**LA BANDEJA POR CAPITULO, QUE ES LO QUE DIMENSIONA EL TRAMO**, corrida por mi y no copiada del encargo:

<!-- TALLADO: parcial salida=.v39/estado_apertura.txt -->

    $ python .v39/estado.py
    poblacion: el arbol entero, sin filtrar
    dataset/nodos.jsonl                        : 321 nodos
    bitacora/VEREDICTOS.jsonl                  : 486 lineas
    cuarentena/scott_radical_candor            : 24
    cuarentena/_insertados/scott_radical_candor: 118
    la bandeja por capitulo                    : cap_13 9, cap_14 15

**`cap_13` ABRE EN `9` Y NO EN `12`, Y ESO CUADRA CON LO QUE LA VUELTA 38 HIZO:** entraron `3` de sus
`6` y la bandeja del capitulo bajo de `12` a `9`. **El encargo me pide `3` de esos nueve**, o sea **un
tercio justo**, y `cap_13` **queda abierto a proposito**. **No estiro el tramo.**

### CC.0.a. **EL TABLERO Y SU PRIORIDAD** (`D.49`, `D.51`)

<!-- TALLADO: parcial salida=.v39/tablero_apertura.txt -->

      prio lote clave                          estado                 dueno                 band ult cap
      --------------------------------------------------------------------------------------------------------
      .    4    scott_radical_candor           CERRADO EN EXTRACCION  serial                  24  cap_14
      1    7    grove_high_output              EN CURSO               grove_high_output       23  cap_03
      2    9    gerber_emyth                   PAUSADO                NINGUNO                 10  cap_11
      3    5    marquet_turn_the_ship          PAUSADO                NINGUNO                  9  cap_03

<!-- TALLADO: parcial salida=.v39/tablero_siguiente.txt -->

    $ python forja.py tablero --siguiente
    D.51, EL ORDEN LO DA EL TABLERO. Linea 'serial':
      le toca: scott_radical_candor
      'scott_radical_candor' ya es de esta linea y esta CERRADO EN EXTRACCION: se continua, que D.50 releva AL CERRAR y no a mitad.

**LA COLA DE DOCTRINA ABRE EN `10` Y `0` BLOQUEAN**, linea `COLA DE DOCTRINA (D.53): 10 pregunta(s), 0
bloquea(n)` del mismo tablero. **Son las `8` que deje yo mas las `2` que subio la `ACTA 37`**, y es
exactamente la cifra que pone en rojo las dos pruebas de la `TAREA 1.A`. **Esta vuelta no sube ninguna
y no adjudica ninguna**: lo unico que toca de la cola es la celda `medida_en` de la pregunta `7`
(`TAREA 1.C`).

### CC.0.b. **EL CERROJO, EN SU SEDE DE `procesos/`** (`D.53`)

<!-- TALLADO: parcial salida=.v39/cerrojo.txt -->

    $ ls -la procesos/
    total 64
    drwxr-xr-x 1 AlexDesk 197609 0 Sep 18 03:47 .
    drwxr-xr-x 1 AlexDesk 197609 0 Sep 18 03:47 ..

**`procesos/` esta vacio: no hay otra corrida viva** y la insercion no queda `INSERCION NO INTENTADA`.

### CC.0.c. **NI SALDO DE LOTE NI COLA SELLADA, Y VAN NUEVE VUELTAS** (`D.43`)

<!-- TALLADO: parcial salida=.v39/entrega_arnes.txt -->

    $ ls docs/loop/INFORME_DE_LOTE.txt docs/loop/SELLOS_INFORME.jsonl
    ls: cannot access 'docs/loop/INFORME_DE_LOTE.txt': No such file or directory
    ls: cannot access 'docs/loop/SELLOS_INFORME.jsonl': No such file or directory
    $ ls docs/loop/ | grep -i -E "cola|vecin"
      (ni una linea)

**Lo declaro como `D.43` manda**: esta vuelta **no trae saldo de lote**, y con el se va `CHOCAN entre si
dentro del lote`. **La cola de vecinos la corro yo de a uno**, que es lo que `D.43` no me quito, y es el
coste que el encargo cronometro en `483` segundos por candidato sobre mi propio reloj de la vuelta 38.

### CC.0.d. **MI CREDITO AL ABRIR, Y NO ME LO ESCRIBO YO** (`D.48`)

<!-- TALLADO: parcial salida=.v39/credito_apertura.txt -->

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA 37
      CIFRA PUBLICADA    1 de 2     ACTA 37
      CLASE              0 de 2     ACTA 37
      DATO MOVIDO        0 de 2     ACTA 37
      REPORTE            2 de 3     ACTA 37

**`REPORTE` en `2 de 3` es mio, es el penultimo escalon y lo recojo sin reabrirlo** (`TAREA 1.D`): su
remedio entero es la `TAREA 4`. **`CIFRA PUBLICADA` en `1 de 2` tambien es de esta sede** y su remedio es
la `TAREA 1.C`. **`AUDITOR` vuelve a `0 de 3` y no es merito mio**: lo recojo y no lo celebro.

### CC.0.e. **LA COLA DE ARISTAS AL ABRIR, RECONTADA POR MI Y NO HEREDADA**

<!-- TALLADO: parcial salida=.v39/cola_apertura.txt -->

    LA COLA DE ARISTAS ENTERA, de bitacora/VEREDICTOS.jsonl
      lineas con arista_en_cola: true            : 11
      de ellas, YA CABLEADAS en el grafo         : 11
      esperan a un extremo que no ha entrado     : 0
      con LOS DOS extremos dentro y SIN cable    : 0   <-- tiene que salir 0
    

**La cifra que el encargo pide que salga `0` sale `0` al abrir**, y las `11` lineas de la cola estan
las `11` cableadas. **Mi trabajo de hoy es que siga saliendo `0` al cerrar**, con las dos aristas nuevas
que la `TAREA 3.A` manda cablear y las tres que van A COLA.

## CC.1. EL ESQUELETO DE LAS TAREAS, ABIERTO ANTES DE LA PRIMERA (`EXTRACTOR.md` 3)

| # | tarea | estado |
|---:|---|---|
| **1.A** | **BLOQUEANTE**: las dos pruebas de la cola de doctrina, que claven la sede y no el `6` | *abierta* |
| **1.B** | **BLOQUEANTE**: la cifra que ya entro (`corregir`) y las dos que entran si no las toco | *abierta* |
| **1.C** | **BLOQUEANTE**: la celda `medida_en` de la pregunta `7`, que ofrece una sede que no existe | *abierta* |
| **1.D** | las adjudicaciones de la `ACTA 37` recogidas y no reabiertas | *abierta* |
| **2** | **BLOQUEANTE**: la fidelidad `D.30` de los tres, ANTES de la primera insercion | *abierta* |
| **3** | `cap_13`, tres candidatos en el orden del libro, uno por vez, con sus aristas | *abierta* |
| **4** | `CC.6` abierta ANTES de la primera insercion, una fila por candidato en el acto | *abierta* |
| **cierre** | guardas, cifras recomputadas, cola de aristas recontada, discutibles | *abierta* |
