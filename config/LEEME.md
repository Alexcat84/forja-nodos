# `config/`: LAS DOS SEDES QUE SOLO ALEXIS ESCRIBE

**Ninguna vuelta del bucle escribe aqui.** `docs/loop/EXTRACTOR.md` seccion 14 lo
dice en su tabla de sedes, y `AUDITOR_FORJA.md` lo repite: el extractor propone en
su reporte, el auditor adjudica en su acta, **y estos dos ficheros los mueve
Alexis.**

## `umbrales.json`

Los tres umbrales de las señales de la aduana, calibrados contra 3.169 nodos
auditados (`docs/CALIBRACION_D4.md`). **Ninguna vuelta mueve un umbral** (`D.23`):
si una lectura pide moverlo, eso es parada y se trae, con su medicion delante.

**Y un umbral se juzga contra su COLA, no contra la mediana** (`D.18`).

## `pares_mutuos.jsonl`

**EL REGISTRO DE CITAS DE ENLACE MUTUO** (adjudicacion `A.1`, `D.14`).

Un **MUTUO** es la **unica vuelta legitima** del grafo: dos nodos que son cada uno
hijo del otro **por lineas distintas**. Solo existe si esta declarado aqui con sus
dos citas.

**EL GATE LO VERIFICA ENTERO, NO LA MERA PERTENENCIA** (`D.14`). Cada par trae:

    par            los dos ids
    paso_ida       el numero del paso del primero que el segundo despliega
    razon_ida      su razon escrita
    huella_ida     la huella del texto de ESA linea
    paso_vuelta    paso_vuelta, razon_vuelta, huella_vuelta: lo mismo al reves

**Si las dos direcciones apuntan a LA MISMA LINEA no es esta figura: es un solape,
y se rechaza nombrando el paso** (banco de textos 9.22 de My-idea).

### Hoy esta VACIO, y eso se dice en el propio fichero

**Esta casa no ha declarado ningun enlace mutuo todavia.** El fichero nace con una
linea de cabecera que lo explica y **cero citas**.

> **Una sede que NO EXISTE y una sede VACIA se parecen demasiado**, y no son lo
> mismo: la primera hace dudar de si el protocolo la lee, y la segunda no.
> *(Decision del fundador del 11 sep 2026, punto 5.7.)*

**La cabecera lleva todas sus claves con guion bajo delante**, que es la misma
convencion de `fuentes/FUENTES_CANONICAS.json` y de los ficheros de candidato, y
**`config.cargar_pares_mutuos` la salta**. Sin eso, el gate y el bloque de vigencia
la tomarian por un par sin huellas y cantarian un fallo que no existe.

### Como se escribe: NO se escribe a mano

**Lo escribe la aduana al insertar**, cuando un veredicto declara `MUTUO`:

    --veredicto "vecino|MUTUO|ida=2:el vecino despliega entero mi paso 2|vuelta=5:yo despliego entero su paso 5"

**Las dos citas se comprueban contra los nodos de verdad**, no contra el texto del
veredicto (adjudicacion `A.4`), y **la misma cita que se simula es la que se
escribe**: si la simulacion viera una distinta, estaria probando otro dato.
