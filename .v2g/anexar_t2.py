# -*- coding: utf-8 -*-
"""Anexa AA.2 al REPORTE, pegando las tablas de sus instrumentos (D.41)."""
import io


def trozo(ruta, arranque, hasta_prefijo=None):
    lineas = io.open(ruta, encoding="utf-8").read().split("\n")
    i = [k for k, l in enumerate(lineas) if l.startswith(arranque)][0]
    j = i
    while j + 1 < len(lineas) and (lineas[j + 1].startswith("|")
                                   or (hasta_prefijo and lineas[j + 1].startswith(hasta_prefijo))):
        j += 1
    return "\n".join(lineas[i:j + 1])


def cola(ruta, arranque):
    lineas = io.open(ruta, encoding="utf-8").read().split("\n")
    i = [k for k, l in enumerate(lineas) if l.startswith(arranque)][0]
    return "\n".join("      " + l for l in lineas[i:] if l.strip())


saldo_tabla = trozo(".v2g/saldo_candidatos.txt", "| # | candidato")
saldo_cierre = cola(".v2g/saldo_candidatos.txt", "EL SALDO, RECONTADO")
veredictos_tabla = trozo(".v2g/veredictos_pares.txt", "| # | candidato")
veredictos_cierre = cola(".v2g/veredictos_pares.txt", "PARES LEVANTADOS POR LA ADUANA")
formula_tabla = trozo(".v2g/formula_cola.txt", "| par que la aduana levanto")
formula_cierre = cola(".v2g/formula_cola.txt", "PARES DISTINTOS MEDIDOS")
guardas = cola(".v2g/guardas_candidatos.txt", "POBLACION DE ESTA COMPROBACION")

texto = u"""
## AA.2. **TAREA 2**: MINAR `cap_03` UN CANDIDATO POR VEZ, CON LA ADUANA EN SECO EN EL MISMO ACTO

**QUINCE CANDIDATOS ESCRITOS, QUINCE PASADOS POR LA ADUANA UNO A UNO, CERO INSERTADOS.**
`EXTRACTOR.md` 16: un candidato no esta escrito hasta que ha pasado la aduana, y el informe va **en
el mismo acto**, no al final del lote. **Ni un `python forja.py insertar` en toda la vuelta**, que es
lo que `D.45` manda a este frente y lo que el fundador repitio al relanzarme.

### AA.2.a. EL SALDO, CANDIDATO A CANDIDATO, LEIDO DE MIS PROPIOS INFORMES

<!-- TALLADO: script=.v2g/saldo_candidatos.py salida=.v2g/saldo_candidatos.txt -->

%s

<!-- TALLADO: parcial salida=.v2g/saldo_candidatos.txt -->

%s

**LA POBLACION NO ES UNA SOLA Y POR ESO VA POR FILA**, que es el remedio bloqueante aplicado donde
mas facil seria saltarselo: el primer informe midio **`358`** y los ultimos **`371`**, porque **la
bandeja crece segun se van escribiendo los candidatos** y cada informe barre contra la que habia
cuando arranco. Publicar *una* poblacion de la tanda habria sido una cifra cierta con rotulo falso.

### AA.2.b. **LO QUE ME COSTO LA ADUANA, MEDIDO, PORQUE ES LA CIFRA QUE `D.43` USA**

<!-- TALLADO: parcial salida=.v2g/cola.log -->

    $ cat .v2g/cola.log   (5 de las 32 lineas)
      [23:25:21] ADUANA EN SECO: elegir_indicador_salida_trabajo_administrativo
      [23:35:31] elegir_indicador_salida_trabajo_administrativo codigo=0 610s
      [00:42:12] casar_flujo_fabricacion_flujo_ventas codigo=0 783s
      [01:44:29] construir_indicador_linealidad_alerta_temprana codigo=0 692s
      [01:44:30] COLA VACIA

**ENTRE `394` Y `796` SEGUNDOS POR CANDIDATO**, contra los `156,5` que `D.43` midio el 12 sep. **La
cola de los quince tardo casi dos horas y veinte minutos**, de las `23:25` a la `1:44`. No es una
queja: es la cifra que sostiene por que `D.43` saco el informe de lote del turno del extractor, y
esta vuelta la vuelve a medir con su propia poblacion, que ya es de `371`.

### AA.2.c. **LA ADUANA SE MURIO DOS VECES SIN ESCRIBIR UNA LINEA, Y LO DIGO YO ANTES QUE NADIE**

**Dos corridas de `python forja.py informe` terminaron con el fichero de salida a `0` bytes**, una
de ellas con `codigo=1` tras `522` segundos. **Las dos veces habia otro informe corriendo a la vez**;
corridas en solitario, las dos pasaron a la primera. La segunda de ellas es la que dejo
`construir_indicador_linealidad_alerta_temprana` sin informe, y **el pasador lo reintento solo** y
salio `ENTRARIA` a la `1:44`.

| corrida | cuando | con que compania | resultado |
|---|---|---|---|
| `elegir_cinco_indicadores_diarios_fabrica` | `23:11` | otro informe en marcha | **`0` bytes**, y a la segunda `ENTRARIA` |
| `construir_indicador_linealidad_alerta_temprana` | `23:45` a `23:54` | el informe del lote entero en marcha | **`0` bytes, `codigo=1`**, y al reintento `ENTRARIA` |
| el informe del LOTE, primer intento | `23:36` a `23:54` | la cola de candidatos en marcha | **`0` bytes** |

**NO LO ARREGLO, Y DIGO POR QUE:** `D.45` prohibe tocar `src/` durante el paralelo, y `EXTRACTOR.md`
13 pone moratoria de maquinaria. **Lo que hago es lo unico que me toca: no correr dos a la vez, y
declararlo.** Queda como observacion medida para quien pueda decidir, no como propuesta de cambio.

### AA.2.d. LA MITAD BARATA DEL DICTAMEN, CORRIDA ANTES QUE LA CARA

Antes de gastar dos horas de barrido corri las **mismas** funciones de `src/aduana.py` que deciden
`CAERIA` (`normalizar_candidato` y `validar_candidato`), que son las baratas, sobre los `23` ficheros
de la bandeja. **Ninguno caia y ninguno chocaba**, asi que la cola larga solo podia decidir entre
`ENTRARIA` y `BLOQUEARIA`, y ningun candidato iba a necesitar correccion de puerta a mitad de camino.

<!-- TALLADO: parcial salida=.v2g/guardas_candidatos.txt -->

%s

**NO ES UN INSTRUMENTO NUEVO Y NO SUSTITUYE A NADA:** llama a las funciones de la aduana y a nada
mas, y **los quince informes se corrieron igual, uno por uno**, mas el del lote entero.

### AA.2.e. LOS NUEVE PARES QUE LA ADUANA LEVANTO, CON MI VEREDICTO Y SU RAZON

**`12` vecindades levantadas, `9` pares distintos** (tres aparecen por las dos puntas). **Ninguno de
estos veredictos se escribe hoy en `bitacora/VEREDICTOS.jsonl`**: esa sede la escribe la aduana con
`insertar`, y este frente no inserta.

<!-- TALLADO: script=.v2g/veredictos.py salida=.v2g/veredictos_pares.txt -->

%s

<!-- TALLADO: parcial salida=.v2g/veredictos_pares.txt -->

%s

### AA.2.f. **CUANTO DE ESA COLA LA FABRICO MI FORMULA DE REDACCION, MEDIDO**

**`EXTRACTOR.md` 2 manda leer a los vecinos antes de escribir el veredicto.** Leyendolos aparecio lo
mismo nueve veces: pares sin nada en comun salvo **el armazon con el que yo escribo el
`resumen_teorico`**. La senal 1 mira `titulo` mas `resumen_teorico` mas `pasos`
(`src/comun.py`, `texto_comparable`), y en mis fichas **el resumen es con diferencia la pieza mas
larga** y repite en los quince las mismas seis rubricas.

**ASI QUE LO MEDI, con la propia funcion de la aduana, sobre los pares que la aduana ya levanto:**

<!-- TALLADO: script=.v2g/formula_cola.py salida=.v2g/formula_cola.txt -->

%s

<!-- TALLADO: parcial salida=.v2g/formula_cola.txt -->

%s

> **OCHO DE LOS NUEVE PARES DEJARIAN DE LEVANTARSE SI LA SENAL NO MIRARA MI `resumen_teorico`.** Y
> el noveno, el unico que la senal 1 **no** levanto, hace lo contrario: **sube** de `0,184` a
> `0,267` al quitar el resumen, porque ahi la coincidencia esta de verdad **en los pasos** y mi
> armazon la estaba **diluyendo**.

**LO QUE ESTO ES Y LO QUE NO ES.** Es la medida que me hacia falta para escribir nueve razones en
vez de nueve corazonadas. **No es una propuesta de mover el umbral**, que es de Alexis y del auditor
(`EXTRACTOR.md` 11: *ninguna vuelta mueve un umbral*), **ni una propuesta de cambiar la ficha**, que
seria doctrina. **Lo registro porque responde con cifras a una pregunta que ya estaba abierta**: la
cuarta propuesta de la vuelta 32, *medir si la formula de redaccion fabrica cola*
(`PARA_ALEXIS.md` 4). **La respuesta de mi tanda es que si, y cuanto: `8` de `9`.**

### AA.2.g. **Y EL CAPITULO MONOTEMATICO, QUE `EXTRACTOR.md` 12 YA TENIA ESCRITO**

Seis de mis quince candidatos bloquean, y **cinco de los nueve pares son candidatos mios contra
candidatos mios**. `EXTRACTOR.md` 12 lo dice sin que haga falta anadir nada: *cuando un capitulo
entero cae en la misma familia, eso no es una senal de duplicado, es una senal de que el libro trata
un tema; se extraen igual, uno a uno, y se espera que la cola de lectura sea larga.* `cap_03` es un
capitulo entero sobre indicadores. **Lo que NO se hace es subir un umbral para que la cola se
acorte**, y no lo propongo.

**`TAREA 2` CERRADA: `15` escritos, `15` por la aduana en el acto, `9` ENTRARIAN, `6` BLOQUEARIAN,
`0` CAERIAN, `0` CHOCAN, `0` insertados.**
""" % (saldo_tabla, saldo_cierre, guardas, veredictos_tabla, veredictos_cierre,
       formula_tabla, formula_cierre)

with io.open("docs/loop/REPORTE.md", "a", encoding="utf-8", newline="\n") as f:
    f.write(texto)

s = io.open("docs/loop/REPORTE.md", encoding="utf-8").read()
s = s.replace(
    "| 2 | minar `cap_03` un candidato por vez, con la aduana EN SECO en el mismo acto | **ABIERTA** |",
    "| 2 | minar `cap_03` un candidato por vez, con la aduana EN SECO en el mismo acto | "
    "**CERRADA** en `AA.2`: `15` escritos y `15` por la aduana en el acto, `9` ENTRARIAN, "
    "`6` BLOQUEARIAN, `0` CAERIAN, `9` pares juzgados y `0` insertados |")
io.open("docs/loop/REPORTE.md", "w", encoding="utf-8", newline="\n").write(s)
print("AA.2 ANEXADA, fila 2 cerrada")
