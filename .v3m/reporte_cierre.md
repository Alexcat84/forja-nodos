
# CIERRE DE LA VUELTA 3

## 7.a. LAS CINCO GUARDAS, CORRIDAS AL CIERRE

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py
    ...
    total: 356 pruebas, 0 fallos, 0 errores

**LAS TRES EN VERDE.** El `gate` sigue en `346` nodos verificados porque esta vuelta **no inserto
nada** (`MODO_INSERCION=cuarentena`); las `346` son las mismas de la apertura (seccion 0 del encargo).

## 7.b. `PASOS INVENTADOS`, LA TABLA CONSOLIDADA DE TODO LO QUE ESTA VUELTA TOCO

| capitulo | nodos | pasos escritos | PUENTE | PASOS INVENTADOS |
|---|---:|---:|---:|---:|
| `cap_06` (estado de la vuelta 2, `ACTA M3` `M3.7.3`, no se repite el calculo, se cita) | 2 | 9 | 1 | 11,11 por ciento (1 / 9) |
| `cap_06` (HOY, tras pagar el puente en `TAREA 2` y releer sus `51` filas en `TAREA 4`) | 2 | 8 | 0 | **0,00 por ciento (0 / 8)** |
| `cap_07` | 1 | 3 | 0 | **0,00 por ciento (0 / 3)** |
| `cap_08` | 1 | 5 | 0 | **0,00 por ciento (0 / 5)** |
| EL TRAMO DE ESTA VUELTA (`cap_07` + `cap_08`) | 2 | 8 | 0 | **0,00 por ciento (0 / 8)** |

**NINGUN CAPITULO TOCADO HOY QUEDA POR ENCIMA DEL TOPE DE `10,00`** (`8.1`): el unico que lo pasaba,
`cap_06`, baja a `0,00` tras pagar su puente. **El freno de volumen que bajo el tramo a DOS capitulos
(seccion 6, por el `11,11` de ayer) sigue siendo la cifra correcta que abrio esta vuelta**: la de hoy no
la borra, la sustituye hacia adelante.

## 7.c. LA MUESTRA DE FIDELIDAD, YA PEGADA EN `5.e`, CITADA Y NO REPETIDA

`cap_07` releido ENTERO (`3` pasos, bajo el umbral de la herramienta) y `cap_08` muestreado al `100` por
ciento (`5` de `5` pasos). **`0` PUENTE en las dos listas**, con su `sed` pegado en `5.a.3` y `5.b.3`.
Semilla `m3`, salida completa en `.v3m/muestra_fidelidad_v3.txt` (commiteado con esta vuelta).

## 7.d. EL CREDITO, ANOTADO (`EXTRACTOR.md` 14, propuesta y no adjudicacion)

*Las cuatro especies que son mias de proponer. `AUDITOR` NO es mia (`EXTRACTOR.md` 14, y el mismo
precedente que la linea `serial` sento en su vuelta `33`, `AC.4.g`: cuatro lineas, no cinco).*

    $ python forja.py credito --anotar --especie REPORTE --vuelta 3 --tanda "vuelta 3" --racha "2 de 3" --cae --cita "docs/loop/REPORTE.md, VUELTA 3 seccion 7"
    $ python forja.py credito --anotar --especie "CIFRA PUBLICADA" --vuelta 3 --tanda "vuelta 3" --racha "1 de 2" --cae --cita "docs/loop/REPORTE.md, VUELTA 3 seccion 1.a"
    $ python forja.py credito --anotar --especie CLASE --vuelta 3 --tanda "vuelta 3" --racha "1 de 2" --cae --cita "docs/loop/PROMPT_SIGUIENTE.md, VUELTA 3 cabecera"
    $ python forja.py credito --anotar --especie "DATO MOVIDO" --vuelta 3 --tanda "vuelta 3" --racha "1 de 2" --cae --cita "docs/loop/REPORTE.md, VUELTA 3 seccion 8"

| especie | lo que propongo | por que |
|---|---|---|
| `REPORTE` | **no cae, sube a `2 de 3`** | abierto antes de la primera tarea, anexado tarea por tarea (secciones `1` a `5`), las cinco guardas verdes en `7.a`, sin turno mudo |
| `CIFRA PUBLICADA` | **no cae, sube a `1 de 2`** | toda cifra de esta vuelta sale de un instrumento corrido hoy (`gate`, `guiones`, `credito`, `deuda`, cuatro `informe`, `wc`, `sed`, `awk`); la unica discrepancia contra el encargo (deuda, seccion apertura) se declaro con su causa y no se copio |
| `CLASE` | **no cae, sube a `1 de 2`** | la vuelta declaro `EXTRACCION` en su cabecera y la sostuvo entera: `0` inserciones, `MODO_INSERCION=cuarentena` de principio a fin |
| `DATO MOVIDO` | **no cae, sube a `1 de 2`** | `dataset/`, `bitacora/` y `censos/` sin tocar (seccion 8); lo unico que cambio de estado fue `cuarentena/` (sede propia del extractor) y `docs/loop/` (tablero, credito, reporte) |

    $ python forja.py credito
    CREDITO DE LA LINEA 'marquet_turn_the_ship' (D.48)
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA M3
      CIFRA PUBLICADA    1 de 2     vuelta 3
      CLASE              1 de 2     vuelta 3
      DATO MOVIDO        1 de 2     vuelta 3
      REPORTE            2 de 3     vuelta 3

      CREDITO ENTERO: ninguna especie en su tope.

## 7.e. EL TABLERO, REESCRITO Y CON SU DIFF PEGADO

*`ACTA M3` `M3.21.c` dejo escrito que el fichero seguia en `cap_03` y `9` candidatos mientras la vista
calculada ya decia `cap_06` y `12`, porque la vuelta 2 no cerro. Se corrige aqui, con el diff real:*

    $ python forja.py tablero --escribir
    ESCRITO: 22 fila(s) en docs/loop/TABLERO.jsonl

    $ git diff docs/loop/TABLERO.jsonl
    -"candidatos_en_bandeja": 12, ... "capitulos_minados": [..., "cap_04", "cap_06"], ... "ultimo_capitulo": "cap_06", ...
    +"candidatos_en_bandeja": 14, ... "capitulos_minados": [..., "cap_04", "cap_06", "cap_07", "cap_08"], ... "ultimo_capitulo": "cap_08", ...

**LA FILA DE `marquet_turn_the_ship` QUEDA AL DIA:** `14` candidatos en bandeja (`12` de antes mas los
`2` de esta vuelta), `cap_08` como ultimo capitulo minado.

## 7.f. LO QUE ESTA VUELTA NO HIZO, DICHO POR SU NOMBRE

- **Cero inserciones.** `MODO_INSERCION=cuarentena` de principio a fin; los `14` candidatos de la
  bandeja siguen esperando a que el lote `marquet_turn_the_ship` cierre (`D.39`).
- **No se abrio un tercer capitulo.** El tramo de esta vuelta fue `cap_07` y `cap_08`, dos, por el freno
  de `8.1` (seccion 6).
- **No se toco el arnes ni la maquinaria** (`D.45`): ningun fichero de `src/`, `scripts/`, `tests/`,
  `hooks/`, `esquema/` ni `orquestador_forja.sh` cambio en esta vuelta.
- **No se escribio doctrina nueva.** La cola de doctrina sigue en `11` preguntas (`python forja.py
  tablero`, seccion `COLA DE DOCTRINA`, `D.56`); esta vuelta no le anadio ninguna.
- **No se pago la deuda `d094` a `d098`.** El instrumento sigue dando `LIBRE` (`1 de 5` al abrir,
  seccion apertura); el encargo lo pidio expresamente.
- **`dataset/`, `bitacora/` y `censos/` sin tocar.** Nada se escribio a mano en esas sedes
  (`EXTRACTOR.md` 14); los cuatro candidatos viven enteros en `cuarentena/marquet_turn_the_ship/`.

## 7.g. LAS CONDICIONES DE PARADA, MEDIDAS UNA A UNA

| condicion (`EXTRACTOR.md` 7) | medida | dispara |
|---|---|---|
| algo contradice una regla vigente | ninguna contradiccion encontrada; el unico punto discutible (el par de similitud alta de `5.c.1`) se leyo y se sostiene, marcado para el auditor | NO |
| una cifra publicada con su corte se contradice sin declarar | la unica discrepancia (deuda, apertura) se declaro con su causa | NO |
| una operacion cuyo texto no alcanza para ejecutarse sin decidir | las dos salidas del puente estaban escritas en el encargo (retirar o reescribir); se eligio con su razon en `2.b` | NO |
| turno sin cerrar reporte | este reporte cierra las cinco tareas con su saldo | NO |

**NINGUNA CONDICION DE PARADA SE CUMPLE. No escribo `PARA_ALEXIS.md`** (`EXTRACTOR.md` 7 y 14: eso lo
hace el auditor, no yo).

## 7.h. EL SALDO FINAL, POR TAREA

| # | tarea | saldo |
|---:|---|---|
| 1 | Registros | correccion declarada (`3` cifras), `PASOS INVENTADOS` publicado, credito leido y anotado, deuda leida y no pagada |
| 2 | Puente de `cap_06` | RETIRADO el paso `7`; `6` pasos, `0` PUENTE |
| 3 | Aduana de la vuelta 2 | las dos corridas, guardadas en `.v3m/aduana/c1.txt` (`1092` bytes) y `c2.txt` (`1104` bytes); las dos `ENTRARIA` |
| 4 | Relectura entera de `cap_06` | `49` filas `R` sin nodo, `8` pasos TRANSCRIPCION, `cap_06` baja a `0,00` |
| 5 | `cap_07` y `cap_08` | `2` candidatos escritos, sus aduanas en `.v3m/aduana/c3.txt` y `c4.txt`, las dos `BLOQUEARIA` por vecino mutuo, leido y sostenido en `5.c.1`; muestra de fidelidad con semilla `m3` pegada |

**CANDIDATOS NUEVOS DE ESTA VUELTA: `2`** (`declarar_intencion_reemplazar_peticion_permiso`,
`resistir_dar_solucion_clasificar_decision_urgencia`). **BANDEJA TOTAL DEL LOTE: `14`.**

## 7.i. LA IDENTIDAD DE CIERRE, LEIDA DE GIT

| | |
|---|---|
| commit al cerrar (antes de este commit) | `9656eba` (`git rev-parse HEAD`, sin cambios desde la apertura: esta vuelta no ha commiteado nada todavia) |
| rama | `extraccion-marquet_turn_the_ship` (`git rev-parse --abbrev-ref HEAD`) |
| bytes de `docs/loop/REPORTE.md` al cerrar | `4062193` (`wc -c`, antes de este parrafo de cierre) |
| bytes de los cuatro candidatos tocados | `aplicar_ejercicio` `5895`, `asignar_responsable` `3549`, `declarar_intencion` `4579`, `resistir_dar_solucion` `4972` |
---
