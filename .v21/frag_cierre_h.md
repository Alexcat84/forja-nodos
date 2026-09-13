
---

## O.10. LAS CIFRAS DEL CIERRE, **RECOMPUTADAS AL CIERRE Y NO MEDIDAS TEMPRANO** (`EXTRACTOR.md` 4)

*La regla es explicita: **medir temprano y publicar tarde sin remedir es la misma especie que citar
sin mirar.** Todo esto se corrio DESPUES de los trece candidatos, DESPUES de la correccion de las
22 cuentas y DESPUES de los trece informes finales.*

    $ python .t1_v21/reparto21.py | tail -10
      candidatos repartidos                   : 96
      candidatos en la bandeja                : 96
      pasos del lote 4                        : 1050

      MEDIDAS DEL CIERRE, recomputadas al cierre (EXTRACTOR.md 4)
        nodos en el grafo        : 203
        veredictos en bitacora   : 148
        ficheros en _insertados  : 201
        nodos con fuente scott   : 0 de 203
        extremos de arista       : 158   (aristas distintas: 79)
        unidades del libro       : 15
        cuerpo cap_11 a cap_14   : 27680 palabras

| medida | al abrir (`O.0`) | **al cerrar** | |
|---|---:|---:|---|
| nodos en el grafo | 203 | **203** | **no se movio: cero inserciones** |
| veredictos en bitacora | 148 | **148** | **no se movio: cero veredictos en sede** |
| ficheros en `cuarentena/_insertados/` | 201 | **201** | **no se movio, y ninguno es de `scott_radical_candor`** |
| candidatos del lote 4 en cuarentena | 83 | **96** | **mas 13**, los de `cap_10` |
| pasos del lote 4 | 856 | **1050** | **mas 194** |
| nodos con fuente `scott_radical_candor` en el grafo | 0 de 203 | **0 de 203** | el lote sigue entero fuera |
| extremos de arista / aristas distintas | 158 / 79 | **158 / 79** | **ninguna arista nueva: las 16 pendientes siguen pendientes** |

> ### **LAS TRES CIFRAS QUE PRUEBAN QUE ESTA VUELTA NO TOCO LA SEDE DE LA ADUANA: GRAFO `203` A `203`, BITACORA `148` A `148`, `_insertados` `201` A `201`.**
> **Es la prueba mecanica de lo que `O.0` anuncio y de lo que `O.5.c` explica:** el veredicto
> `CONTINUA` de la TAREA 4 y los seis `SANO` de `O.6.5` **estan escritos con su razon en este
> reporte y en ningun otro sitio**, porque hoy no se inserta y `bitacora/` no se escribe a mano.

    $ git rev-parse --short HEAD        (antes del commit del cierre)
      97223a5
    $ git rev-parse --abbrev-ref HEAD
      extraccion-mundo-11
    $ wc -l < docs/loop/REPORTE.md     (antes de anexar esta seccion)
      26136

> # **VUELTA 21 CERRADA. `cap_10` ENTERO: 13 CANDIDATOS, 194 PASOS, CUATRO TAREAS DE CUATRO, CERO INSERCIONES POR REGLA Y CERO PARADAS.**
