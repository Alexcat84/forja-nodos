# ENCARGO DE LA VUELTA 42: **VUELTA DE INSERCION PURA**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta. Escrito al aplicar la
decision del fundador del 18 sep 2026, archivada en
`docs/loop/paradas/2026-09-18-la-deuda-tiene-cadencia-DECISION.md`.*

> # **LIBRO DE ESTA VUELTA: `scott_radical_candor`**

> # **ESTA ES UNA VUELTA DE INSERCION, Y ESO ES UNA CLASE DE VUELTA** (`D.55`)
>
> **ABRE SIN UNA SOLA TAREA DE REPARACION. Tu unico trabajo es meter candidatos al grafo
> por la aduana.**
>
> **NO tienes tarea bloqueante.** No hay ninguna cifra que corregir, ningun rotulo que
> rehacer, ninguna arista atrasada que cablear antes de empezar. **Todo eso esta en
> `docs/loop/DEUDA.jsonl` con su cita, y se paga en una vuelta de SANEAMIENTO.**
>
>     python scripts/deuda.py        lo pendiente, y que clase de vuelta toca
>
> **LO UNICO QUE TE PUEDE BLOQUEAR ES UNA GUARDA DE DATO EN ROJO**: `gate`, el cerrojo, el
> censo no decreciente, o la fidelidad `D.30` con puente. **Eso no es deuda: es averia**, y
> una averia se arregla antes de seguir. **Si ninguna esta en rojo, insertas.**

---

## POR QUE ESTA REGLA EXISTE, Y ES TU PROPIA MEDIDA

**Tu antecesor lo midio solo, sin que nadie se lo pidiera:**

    la 40 corrio con tramo 4 y metio 0; la 41 corrio con 3 y metio 1.
    Las dos abrieron con una tarea bloqueante de reparacion y las dos se
    quedaron sin turno para insertar.

**La vuelta 36 metio `14` nodos en una sola vuelta.** Las cinco siguientes metieron `8`
entre todas. **No falto candidato y no mordio ninguna guarda.**

> **LA DEUDA NO SE PERDONA, SE AGENDA.** Sigue escrita, con su cita y su vuelta de origen,
> y se paga junta. **Lo que se acaba es que una arista de hace dieciseis vueltas decida
> cuantos nodos entran hoy.**

---

## LA UNICA TAREA: **`cap_13` Y `cap_14`, HASTA DONDE LLEGUES**

    $ python .v42/estado.py
    poblacion: el arbol entero, sin filtrar
    dataset/nodos.jsonl                        : 325 nodos
    bitacora/VEREDICTOS.jsonl                  : 514 lineas
    cuarentena/scott_radical_candor            : 20
    cuarentena/_insertados/scott_radical_candor: 122
    cuarentena/grove_high_output               : 23
    la bandeja de scott por capitulo           : cap_13 5, cap_14 15

**`122` de `142` insertados. Quedan `20`, y con ellos el lote 4 cierra.**

- **Un candidato por vez y en el orden del libro**, por la aduana, con su veredicto.
- **Las aristas `D.29` que la señal no levanta se declaran por lectura y se cablean en el
  mismo acto en que entra su nodo.** Las `56` y `57` son de dos de tus candidatos.
- **No hay techo de tramo esta vuelta.** El de candidatos por vuelta sigue siendo el de
  `EXTRACTOR.md` 12.4: **entre cinco y quince.** **Aspira a quince.**

### LO QUE SIGUE SIENDO OBLIGATORIO, PORQUE ES GUARDA DE DATO Y NO REPARACION

| | |
|---|---|
| **la fidelidad `D.30`** | de tus candidatos, **releida contra su parrafo y ANTES de la primera insercion** |
| **el cerrojo** | una sola corrida escribe el dataset. Si dice `INSERCION NO INTENTADA`, hay otra viva: **no la esquives** |
| **el censo y el tallado** | corren en cada commit y no se negocian |

### Y UNA COSA DE METODO QUE TU ANTECESOR PAGO DOS VECES

> **NO LANCES NADA QUE PUEDA SOBREVIVIR A TU TURNO.** Corre la insercion **en primer
> plano, una por vez**, y espera a que termine dentro de la misma llamada. **Nada de
> segundo plano, nada de `&`, nada de una cadena que arrancas y consultas despues.**
>
> La vuelta 40 termino su turno con una cadena viva y **metio cero**. **No es una
> reparacion: es como se inserta.**

## AL CERRAR

**La seccion de la insercion crece UNA FILA CADA VEZ QUE UN CANDIDATO ENTRA, en su propio
commit**, y al final escribes **la linea del tramo, sea cual sea el numero, incluido `0` y
incluido `20`**:

> *la vuelta cierra en el candidato `N` de `20`; los que quedaban pasan a la vuelta
> siguiente.*

    python scripts/cerrar_reporte.py
    python scripts/tabla_de_cierre.py --escribir   y se pega su salida
    python forja.py tablero --escribir
    python forja.py credito --anotar ...           una linea por especie, con su cita

**Y SI UN TURNO TUYO PASA DE `10` USD**, el acta lo declara con el desglose de en que se
fue (`D.55`). No esta prohibido gastar: **esta prohibido no decir en que.**

---

## LO QUE HA CAMBIADO BAJO TUS PIES, Y TE CONVIENE SABER

| | |
|---|---|
| **`grove_high_output` esta COSECHADO** | sus `23` candidatos estan en **tu** bandeja, con `cap_01` a `cap_03` minados. **No los toques esta vuelta**: `D.51` dice que la serial lo toma **al cerrar `scott`** |
| **el paralelo termino** | **una sola linea a partir de ahora.** `gerber_emyth` y `marquet_turn_the_ship` siguen pausados y la serial los toma por el orden |
| **la doctrina esta congelada** | la cola se queda en `11` y **no crece**. Si encuentras una pregunta nueva, **registrala en tu acta con su medida y dejala ahi**: no abre parada y no va al banco |
| **`D.53`** | un `SANO` **puede** llevar arista declarada, y declararla **no** lo convierte en `CONTINUA` |

## LO QUE NO SE TOCA

- **El banco no gana reglas nuevas** salvo que una guarda de DATO lo exija con su cita.
- **`config/frentes.json` y `config/umbrales.json`** se leen, no se editan.
- **El bucle no funde ramas y el bucle no crea remotos.**
