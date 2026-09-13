# DICTAMEN DEL 13 SEP 2026: **ESPECIE `ARNES`.** LA MEDIDA DEL ROL INICIAL SE DEJABA ENGAÑAR POR UN FICHERO TOCADO FUERA DE UN TURNO

*Escrito siguiendo el guion de reanudacion del fundador del 13 sep 2026, punto 2:
**si es `ARNES`, se arregla con su caso positivo y negativo, se deja el dictamen aqui,
y se relanza sin esperar.***

---

## 1. LO QUE ENCONTRE AL LEER LA COLA, Y NO ERA UNA PARADA VIVA

**`docs/loop/PARA_ALEXIS.md` NO EXISTE.** La cola de `docs/loop/loop.log` termina en:

    [2026-09-13 01:23:48] DETENIDO en la vuelta 3: existe docs/loop/PARA_ALEXIS.md. Leelo.

y **esa parada ya esta dictaminada y curada**: es la de la vuelta 22, archivada en
`docs/loop/paradas/2026-09-13-la-tabla-tecleada.md`, con su regla `D.41` corriendo en
cada commit. **No habia nada pendiente de leer.**

**PERO ANTES DE RELANZAR MEDI POR DONDE ARRANCARIA EL ARNES, Y ARRANCABA MAL.**

## 2. EL DEFECTO, CON SU MEDIDA

`decidir_rol_inicial()` comparaba **dos fechas de commit** y nada mas:

> si `REPORTE.md` es mas nuevo que `ACTA_AUDITOR.md`, la vuelta anterior quedo sin
> auditar, asi que empieza el **auditor**.

**Y esta manana el reporte era mas nuevo que el acta por un motivo que esa regla no
contempla: lo toque yo**, regenerando la tabla de frontera de `cap_11` por `D.41`,
**despues** de que la `ACTA 22` estuviera escrita y commiteada.

    docs/loop/REPORTE.md        ultimo commit  2026-09-13 09:08:49
    docs/loop/ACTA_AUDITOR.md   ultimo commit  2026-09-13 01:22:10

**CONSECUENCIA MEDIDA: el arnes habria empezado por el AUDITOR y habria auditado la
vuelta 22, que ya tiene su `ACTA 22`.** Un turno entero (los ultimos duraron entre
33 y 65 minutos y costaron entre 11 y 17 dolares), **y un acta de mas auditando nada.**

> ### **LA PREGUNTA DE VERDAD NO ES QUE FICHERO ES MAS NUEVO: ES QUIEN CORRIO EL ULTIMO TURNO.**
>
> Y de eso **el arnes tiene registro propio y de nadie mas**: sus dos testigos, que
> escribe el al acabar cada turno y que ningun modelo edita (`D.33`).

## 3. EL ARREGLO

**La medida de siempre se queda**, y solo se corrige **en una direccion** y **solo con
prueba delante**: cuando el reporte es mas nuevo que el acta, el arnes mira **cual de
sus dos testigos escribio el ultimo**.

| lo que dicen los testigos | que hace |
|---|---|
| el del **auditor** es el mas nuevo | **empieza el EXTRACTOR**, y escribe en el log que *el reporte se toco FUERA de un turno* |
| el del **extractor** es el mas nuevo | **empieza el AUDITOR**, como siempre, y lo confirma en el log |
| **falta cualquiera de los dos** | **empieza el AUDITOR**, como siempre. **Sin prueba no se corrige nada** |

**POR QUE `mtime` Y NO LA FECHA DEL COMMIT, que es lo primero que uno intentaria:**
los dos testigos **se commitean juntos**, en el mismo commit de artefactos, asi que sus
fechas de commit son **identicas** y no distinguen nada. Medido hoy:

    ultimo_extractor.json   mtime 2026-09-12 23:45:44   ultimo commit 2026-09-13 01:22:10
    ultimo_auditor.json     mtime 2026-09-13 01:23:47   ultimo commit 2026-09-13 01:22:10

**Lo que distingue es cuando los ESCRIBIO el arnes**, que es al acabar cada turno.

**Y EL ARNES PEGA LAS CUATRO FECHAS EN SU LOG** cuando corrige, para que la decision se
pueda recontar sin creerle (`D.38.3`).

## 4. LOS DOS CASOS, PORQUE UNA GUARDA SIN CASO POSITIVO NO GUARDA NADA

| escenario | que planta | que exige |
|---|---|---|
| **5** (ya existia) | reporte mas nuevo, **sin testigos** | **AUDITOR**. El comportamiento viejo se conserva donde no hay prueba |
| **5b**, **CASO POSITIVO** | reporte mas nuevo, los dos testigos, **el del auditor el ultimo** | **EXTRACTOR**, con *el reporte se toco FUERA de un turno* y las fechas pegadas |
| **5c**, **CASO NEGATIVO** | reporte mas nuevo, los dos testigos, **el del extractor el ultimo** | **AUDITOR**. Sin este, el 5b solo probaria que la guarda sabe decir que si |

`tests/prueba_arnes.sh`, **128 comprobaciones en verde** (eran 120).

## 5. LO QUE ESTE ARREGLO **NO** HACE

**No adivina.** Si el arnes no tiene sus dos testigos, se comporta exactamente como
antes. **Una guarda que adivina donde no sabe es peor que la que fallo.**

**Y no toca `EMPEZAR_EN`**, que sigue ganando sobre la medida. Lo que cambia es que
**ya no hace falta acordarse de ponerlo** despues de una correccion del fundador, que
es justo la clase de cosa que `D.40` enseño que no se puede dejar a la memoria.

## 6. ESTADO AL RELANZAR

| | |
|---|---|
| rama | `extraccion-mundo-11` |
| `PARA_ALEXIS.md` | **no existe** |
| `PROMPT_SIGUIENTE.md` | el encargo de la **vuelta 23**, escrito |
| guardas | `gate` **203**, `guiones`, `rancios`, **tallado `D.41`**, `test_aceptacion` **111**, arnes **128** |
| rol inicial que mide ahora | **EXTRACTOR**, que es el que tiene encargo |
