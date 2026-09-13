
> # **DE `142` CANDIDATOS, ENTRARON `11`. LA TANDA NO CUPO EN ESTA VUELTA Y NO LA RESUMO: LA DECLARO.**
>
> **POR QUE NO CUPO, MEDIDO Y NO SUPUESTO:** cada llamada a `forja.py insertar` tarda entre **39 y
> 115 segundos**, y **sube segun crece el grafo**, porque la aduana compara contra todos los nodos
> del dataset. Medido en esta vuelta: **39 s** con 203 nodos y **mas de 110 s** con 210. A ese ritmo
> **142 candidatos son mas de tres horas de instrumento**, y eso **antes** de leer un solo par.
>
> **ES EL MISMO COSTE QUE `D.42` MIDIO PARA EL INFORME DE LOTE** (156,5 s por candidato, mas de tres
> horas para 83) **y la misma conclusion: una cifra que no cabe en un turno no se firma en un
> turno.** La diferencia es que aquel se saco de mi turno por escrito y este no, asi que **lo que
> hago es entregar lo que cabe y decir exactamente donde me quedo.**

### R.6.e. **LO QUE LA TANDA DESTAPO, Y ES LO MAS IMPORTANTE QUE MIDE ESTA VUELTA**

**CADA INTENTO ABRE PARES QUE EL INTENTO ANTERIOR NO VEIA, porque la poblacion crece con cada
insercion.** El ejemplar entero, medido en esta vuelta sobre un solo candidato:

| momento | contra cuantos nodos midio la aduana | vecinos que levanto |
|---|---:|---:|
| primer intento de `ajustar_franqueza_oido_oyente` | **205** | **1** (`desplegar_marco_franqueza_radical`) |
| segundo intento, con ese veredicto ya escrito | **214** | **3** (los dos nuevos son `delimitar_franqueza_radical_cinco_noes` y `equilibrar_elogio_critica_equipo`) |

> **ESO NO ES UN FALLO DE LA ADUANA NI MIO: ES LA CONVERGENCIA QUE `D.36` DESCRIBE.** *Leer de mas
> cuesta una lectura; leer de menos cuesta una arista que nadie sabra que falta.* **Un lote de 142
> que entra en un grafo que crece de 203 a 345 no tiene una cola de lectura fija: tiene una cola que
> crece mientras se paga.**
>
> **Y LO QUE ESO SIGNIFICA PARA QUIEN PLANIFIQUE LA VUELTA 25, dicho como medicion y no como
> queja:** `24` pares esperan lectura sobre **7** candidatos parados, y quedan **124** sin intentar.
> **La cola final no se puede estimar desde aqui**, y cualquier cifra que yo diera seria inventada.

### R.6.f. LO QUE SI ENTRO, Y LO QUE ESO CAMBIA

| | al abrir | al cerrar |
|---|---:|---:|
| nodos en el grafo | **203** | **214** |
| veredictos en `bitacora/VEREDICTOS.jsonl` | **148** | **156** |
| ficheros en `cuarentena/_insertados/` | **201** | **212** |

> **LOS `8` VEREDICTOS NUEVOS DE LA BITACORA SON LA PRIMERA VEZ EN LA CAMPANIA QUE UN VEREDICTO MIO
> LLEGA A SU SEDE**, y el encargo me lo dijo antes y no despues: hasta hoy mis veredictos vivian en
> `REPORTE.md`, que no es sede de esa especie. **Los escribio `forja.py insertar` en el acto de la
> insercion, uno por vecino y con la razon que yo escribi leyendo a los dos**, y ni una linea se
> toco a mano.

### R.6.g. LO QUE **NO** SE HIZO DE LA TAREA 5, DICHO UNO A UNO

| punto del encargo | estado |
|---|---|
| **1. insertar uno por vez con `D.36` y `D.37` y su veredicto por vecino** | **HECHO en 11 de 142**, y los 11 con su veredicto escrito por vecino donde la aduana lo pidio. **Los 131 restantes quedan en cuarentena**, que es donde `D.39` manda que esperen |
| **2. cablear las 71 aristas** | **CERO cableadas**, y la razon es medible: `forja.py arista` rechaza una arista con un extremo en cuarentena, y **de las 71 no hay ni una con sus dos extremos dentro del grafo** |
| **la correccion 9 de la vuelta 22** | **NO ejecutada**, porque su acto es el cableado. Queda repetida por tercera vez en `R.7.c` |
| **3. el reparo de `R.4.d`** | **HECHO**, y hecho hoy y no el dia del cableado, para que no dependa de que el cableado ocurra |
| **4. los veredictos a la bitacora por `forja.py insertar`** | **HECHO**: `8` lineas nuevas, ninguna escrita a mano |
| **5. el informe de lote** | **NO lanzado y declarado** (`R.0.2` y `R.6.a`), que es lo que `D.42` manda cuando el arnes no lo entrega |
