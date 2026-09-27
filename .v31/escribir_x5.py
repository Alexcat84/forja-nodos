# -*- coding: utf-8 -*-
import io

RUTA = "docs/loop/REPORTE.md"
s = io.open(RUTA, encoding="utf-8").read()


def pegar(ruta, desde, hasta=None):
    lineas = io.open(ruta, encoding="utf-8").read().rstrip().split("\n")
    for numero, linea in enumerate(lineas):
        if linea.startswith(desde):
            lineas = lineas[numero:]
            break
    if hasta is not None:
        for numero, linea in enumerate(lineas):
            if numero and linea.startswith(hasta):
                lineas = lineas[:numero]
                break
    return "\n".join(l for l in lineas if l.startswith("|")).strip()


tabla = pegar(".v31/cola_v31.txt", "| lo que queda", "LAS ARISTAS")
abiertas = pegar(".v31/cola_v31.txt", "| linea |")

nuevo = """## X.5. **TAREA 5**: la cola entera, recontada fila a fila contra el dato

**LA RECUENTO CONTRA EL DATO Y NO CONTRA LA TABLA DEL ENCARGO**, que es lo que el encargo manda con
esas palabras: *si una cifra mia no te sale, gana la tuya y declaras la discrepancia.*

<!-- TALLADO: script=.v31/cola.py salida=.v31/cola_v31.txt -->

""" + tabla + """

**DE LAS DIEZ FILAS DEL ENCARGO, OCHO ME SALEN AL DIGITO** (`3` de `7` rotulos, `1` tramo de `L221`,
`1` de `3` modos de `L153`, `6` y `48` de `cap_04`, `14` de `17` unidades, `8` `SIN HUELLA`, `3` del
lote 5, y la arista de `desplegar_plan`). **Las dos que se mueven se mueven porque esta vuelta las
movio**: la arista de `nutrir_ideas` **la cerre yo** y la bandeja del lote 4 baja de `89` a `78`.

### X.5.a. **LA COLA DE ARISTAS, CONTADA ENTERA Y NO SOLO EN LAS DOS FILAS QUE EL ENCARGO NOMBRA**

*`ACTA 29` `6.5` mide que la marca `arista_en_cola` **la escribe la aduana y no la lee nadie**. Si la
unica lectura es una fila copiada a mano en el encargo, entonces la cola vale lo que valga la
memoria del que la copio. **Asi que la cuento de su sede.***

<!-- TALLADO: parcial salida=.v31/cola_v31.txt -->

""" + abiertas + """

> ### **Y AQUI TENGO LA UNICA DISCREPANCIA DE CIFRA DE ESTA TAREA, Y SALE A FAVOR DEL REGISTRO**
>
> **EL ENCARGO PUBLICA DOS ARISTAS EN COLA. LA BITACORA TIENE CUATRO ESCRITAS**, de las cuales **tres
> ya estan cableadas** y **una sigue abierta.**
>
> **NO ES QUE EL AUDITOR SE EQUIVOCARA:** sus dos filas son las dos que estaban **abiertas** cuando el
> midio, y hoy una de ellas la he cerrado yo. **Lo que su tabla no dice es cuantas hay escritas en
> total**, y esa es justo la cifra que hace falta para saber si la cola se esta vaciando o creciendo.
>
> **ASI QUE LA FILA NUEVA ES ESA:** `4` escritas, `3` resueltas, **`1` abierta**, y la abierta es la
> linea `371`. **Contada de la bitacora, no de la memoria**, que es la unica forma de que la proxima
> vuelta no tenga que fiarse de esta.

### X.5.b. LAS TRES FILAS QUE NO SE TOCAN, Y POR QUE CADA UNA

| fila | por que no se toca en esta vuelta |
|---|---|
| las entradillas de `LISTEN`, `CLARIFY` y `DEBATE` de `cap_07` | **NADA la cierra, y es deliberado.** El auditor adjudico en `ACTA 29` `5` que **es la consecuencia buena de `EXTRACTOR.md` 9**: una entradilla que solo nombra no es procedimiento. **Queda como registro, no como deuda** |
| `L221` de `cap_07`, *turn on that rock tumbler* | **`cap_07` esta cerrado en insercion** (`0` en bandeja, `25` nodos que lo citan, firmado por el auditor). **Reabrirlo pide una decision de alcance que no es mia** (`EXTRACTOR.md` 14) |
| el hueco de transcripcion de `L153` | sigue **SIN VIA**: **con un solo ejemplar no se construye una regla.** Lo dejo nombrado para que el segundo ejemplar lo encuentre |

### X.5.c. `cap_04` NO CABE OTRA VEZ, Y LO DECLARO CON SU MOTIVO

**`6` candidatos y `48` pasos, medidos hoy sobre el archivo mas la bandeja** (sus seis **ya
entraron**: lo que queda pendiente es **releerlos**, no insertarlos).

**EL MOTIVO ES EL MISMO RELOJ DE `X.4.c`, con su cifra:** once corridas de aduana a `109` segundos
cada una se llevaron **unos `53` minutos** de esta vuelta (de las `17:31` a las `18:24`, leido de las
marcas de tiempo de cada corrida). **Releer `48` pasos contra `cap_04` es una tarea de lectura entera,
y no es la que el encargo puso primero.** Va otra vez a la cola, con el mismo motivo y la misma
cifra, **que es lo que el encargo pide que haga si no cabe.**

"""

viejo = """## X.5. **TAREA 5**: la cola entera, recontada fila a fila contra el dato

PENDIENTE

"""
assert s.count(viejo) == 1
io.open(RUTA, "w", encoding="utf-8", newline="").write(s.replace(viejo, nuevo))
print("ok")
