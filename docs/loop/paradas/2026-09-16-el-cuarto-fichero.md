# DICTAMEN DEL 16 SEP 2026: **ESPECIE `ARNES`.** ME DEJE EL CUARTO FICHERO

*Escrito siguiendo el guion de reanudacion del fundador del 13 sep 2026, punto 2:
**si es `ARNES`, se arregla con su caso positivo y negativo, se deja el dictamen aqui, y
se relanza sin esperar.***

---

## 1. QUE PASO

El arnes corrio la vuelta 30 entera (extractor `5753` s, apertura ciega `2943` s) y **se
detuvo al sellar**, con el testigo `D.45` que se estreno esta misma tarde:

    [15:28:07] SELLO NO ACEPTADO en la vuelta 1: una guarda estaba en ROJO al sellar.
                 la guarda 'censo_rutas' estaba en ROJO en el instante del sello

**EL TESTIGO HIZO EXACTAMENTE LO QUE TIENE QUE HACER.** Lo que estaba mal era el censo, y
el censo estaba mal **por un descuido mio de hace dos horas.**

## 2. EL DEFECTO, Y ES MIO

`D.34.2` retira **CUATRO** ficheros durante la fase ciega:

    retirar="REPORTE.md loop.log ultimo_extractor.json ultimo_auditor.json"

Al cablear `D.42` sobre esa ventana, meti en `config/sedes_vacias.json` **`REPORTE.md` y
los dos testigos, y me deje `loop.log`**. Asi que en la fase ciega el censo encontraba una
acta citando `docs/loop/loop.log` como sede, **no lo encontraba en el arbol** y caia:

    CAE  docs/loop/ACTA_AUDITOR.md linea 2583, celda 1
         ruta : docs/loop/loop.log
         NO esta en el arbol, y la celda no lleva la marca 'VACIA A PROPOSITO'

> **UNA RUTA AUSENTE POR PROTOCOLO SE DENUNCIO COMO CAIDA DE CIFRA, Y EL BUCLE SE PARO
> POR UNA CAIDA QUE NO EXISTIA.**

**Coste: una vuelta entera de trabajo bueno** (el extractor cerro su turno y el auditor
ciego el suyo) **detenida en el ultimo paso.** El trabajo no se pierde, pero la vuelta no
cerro.

## 3. EL ARREGLO, Y LO QUE LE ANADO PARA QUE NO SE REPITA

**Lo obvio:** `docs/loop/loop.log` entra en la lista.

**Lo que importa:** `config/sedes_vacias.json` **duplica** una lista que vive en el arnes,
y **una copia se desincroniza**. Es la misma leccion que `D.33` aprendio el 12 sep cuando
una lista cerrada se quedo sin `ultimo_apertura.json` **por haber nacido despues**.

> **AHORA HAY UNA PRUEBA QUE LEE LOS CUATRO DEL PROPIO ARNES** (`retirar="..."` de
> `orquestador_forja.sh`) **y exige que la lista los cubra.** Si mañana `D.34.2` retira un
> quinto fichero y nadie toca la lista, **la prueba cae nombrandolo.**

**UNA LISTA QUE HAY QUE ACORDARSE DE COMPLETAR NO ESTA COMPLETA.**

## 4. LOS DOS CASOS

| | |
|---|---|
| **POSITIVO** | con los **cuatro** ficheros retirados, como en la fase ciega: **censo `rc=0`** y **el sello se acepta**. Antes: `rc=1` y el bucle parado |
| **POSITIVO de la prueba** | la prueba lee `retirar="..."` del arnes y exige la lista. **Sin ella, el quinto fichero volveria a pararnos** |
| **NEGATIVO** | una ruta ausente que **no** sea de las cuatro **sigue cayendo**: la exencion es de las que `D.34.2` nombra, no de todo lo que falte |

`193` pruebas, `0` fallos. Arnes `128` en verde. Cierre completo en verde.

## 5. LO QUE NO ES

**NO es una caida del auditor ni del extractor**, y sus rachas no se mueven. **No es
`CREDITO` y no es `DOCTRINA`:** la regla estaba bien escrita y el codigo no la seguia.

**Y NO RETIRO `D.45`.** El testigo se estreno hoy y **lo primero que hizo fue detener el
bucle por un defecto mio**; eso no es un argumento contra el, es el argumento a favor.
Lo que se arregla es lo que estaba roto.

## 6. ESTADO AL RELANZAR

    rama            : extraccion-mundo-11
    PARA_ALEXIS.md  : archivado. El bucle puede correr
    nodos           : 243        veredictos : 289
    guardas         : gate (13), guiones, tallado, censo, 193 pruebas, arnes 128

    y con los CUATRO retirados, como en la fase ciega:
    censo   rc=0        testigo  EL SELLO SE ACEPTA
