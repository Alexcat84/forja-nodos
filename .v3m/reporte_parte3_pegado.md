
## 3.a. `aplicar_ejercicio_codigo_genetico_control`, corrida DESPUES de pagar el puente

    $ python forja.py informe cuarentena/marquet_turn_the_ship/aplicar_ejercicio_codigo_genetico_control.json > .v3m/aduana/c1.txt

```
============================================================================
INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
============================================================================
candidatos revisados        : 1
poblacion del barrido       : 449   (346 del grafo mas 103 que esperan en bandejas)
umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

EL SALDO
  ENTRARIAN sin leer nada          : 1
  BLOQUEARIAN esperando veredicto  : 0   (no es rechazo: es cola de lectura)
  CAERIAN por una guarda           : 0
  CHOCAN entre si dentro del lote  : 0

============================================================================
LA LISTA COMPLETA, candidato por candidato
============================================================================

[ENTRARIA] aplicar_ejercicio_codigo_genetico_control   (aplicar_ejercicio_codigo_genetico_control.json)

NADA SE INSERTO. Este informe es de SOLO LECTURA: para que un nodo
entre hace falta python forja.py insertar, uno por vez, con su
veredicto escrito por vecino.
```

**LAS TRES COLUMNAS: `1 ENTRARIA`, `0 BLOQUEARIA`, `0 CAERIA`.** El puente pagado en la `TAREA 2` no
cambio el saldo de la aduana (el informe verde de la vuelta anterior tambien decia `ENTRARIA`): lo que
cambio es que ahora el candidato tiene `6` pasos y `0` PUENTE en vez de `7` pasos y `1` PUENTE, que es
lo que la aduana NO puede ver (`EXTRACTOR.md` 15.4, ninguna guarda ve un paso que el libro no dice).

## 3.b. `asignar_responsable_unico_evolucion_planificada`, la que la vuelta 2 no llego a correr

    $ python forja.py informe cuarentena/marquet_turn_the_ship/asignar_responsable_unico_evolucion_planificada.json > .v3m/aduana/c2.txt

```
============================================================================
INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
============================================================================
candidatos revisados        : 1
poblacion del barrido       : 451   (346 del grafo mas 105 que esperan en bandejas)
umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

EL SALDO
  ENTRARIAN sin leer nada          : 1
  BLOQUEARIAN esperando veredicto  : 0   (no es rechazo: es cola de lectura)
  CAERIAN por una guarda           : 0
  CHOCAN entre si dentro del lote  : 0

============================================================================
LA LISTA COMPLETA, candidato por candidato
============================================================================

[ENTRARIA] asignar_responsable_unico_evolucion_planificada   (asignar_responsable_unico_evolucion_planificada.json)

NADA SE INSERTO. Este informe es de SOLO LECTURA: para que un nodo
entre hace falta python forja.py insertar, uno por vez, con su
veredicto escrito por vecino.
```

**LAS TRES COLUMNAS: `1 ENTRARIA`, `0 BLOQUEARIA`, `0 CAERIA`.** La poblacion subio de `449` a `451`
entre el informe de `3.a` y este: los dos candidatos de `cap_07` y `cap_08` (`TAREA 5`) ya estaban
escritos en bandeja cuando este informe corrio, y el instrumento los cuenta (`D.38.5`, poblacion es
grafo mas bandejas). No es una discrepancia: es el orden en que esta vuelta escribio sus ficheros.

## 3.c. EL SALDO DE LA TAREA

**Las dos aduanas que la vuelta 2 dejo abiertas quedan cerradas aqui, con sus dos ficheros con bytes de
verdad**: `.v3m/aduana/c1.txt` (`1092` bytes) y `.v3m/aduana/c2.txt` (`1104` bytes). Ninguna de las
dos aduanas se corrio con carga (`0` inserciones en las dos), y las dos dan `ENTRARIA` sin bloqueantes
ni caidas.
---
