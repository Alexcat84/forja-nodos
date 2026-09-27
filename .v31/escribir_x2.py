# -*- coding: utf-8 -*-
import io

RUTA = "docs/loop/REPORTE.md"
s = io.open(RUTA, encoding="utf-8").read()


def sangrado(ruta):
    texto = io.open(ruta, encoding="utf-8").read().rstrip()
    return "\n".join(("    " + l) if l.strip() else "" for l in texto.split("\n"))


def tabla(ruta, desde):
    """La tabla del instrumento, pegada entera desde su primera fila."""
    lineas = io.open(ruta, encoding="utf-8").read().rstrip().split("\n")
    for numero, linea in enumerate(lineas):
        if linea.startswith(desde):
            return "\n".join(lineas[numero:]).strip()
    raise SystemExit("no encuentro %r en %s" % (desde, ruta))


caso = io.open(".v31/caso_positivo_herencia.txt", encoding="utf-8").read().rstrip().split("\n")
corte = caso.index("LOS REMEDIOS, UNO A UNO, CON SU LINEA DEL ACTA")
tabla_resumen = "\n".join(l for l in caso[:corte] if l.startswith("|")).strip()
tabla_detalle = "\n".join(l for l in caso[corte:] if l.startswith("|")).strip()

nuevo = """## X.2. **TAREA 2, BLOQUEANTE**: el arnes que no entrega los remedios que `D.40` le manda entregar

**VA ANTES DE LA PRIMERA INSERCION, como el encargo manda**, y por un motivo que no es de orden sino
de consecuencia: mientras el arnes no entregue los remedios que el acta escribe, **el siguiente
auditor va a romper el suyo igual que lo rompio el de la `ACTA 29`**, que se lo cargo el mismo
citando `D.40` (*el fallo era de arquitectura, y la arquitectura es del arnes*).

### X.2.a. **EL DEFECTO, MEDIDO POR MI Y NO COPIADO DEL ENCARGO**

<!-- TALLADO: parcial salida=.v31/herencia_antes_full.txt -->

    $ python forja.py herencia            (con el codigo de antes de esta vuelta)
      heredados     : 4
      HEREDADO 1   [REMEDIO, linea 26226 del acta]   -> **el TITULO de la ACTA 29**
      HEREDADO 2   [REMEDIO, linea 26281 del acta]   -> la seccion 0.1, que CITA el defecto
      HEREDADO 3   [REMEDIO, linea 26952 del acta]   -> la seccion 8.1, que CITA el remedio roto
      HEREDADO 4   [REMEDIO, linea 27002 del acta]   -> la seccion 8.5, **la unica que los ESCRIBE**

> **Y LO QUE MIDO ES PEOR QUE LO QUE EL ENCARGO DESCRIBE, asi que lo digo.** El encargo publica el
> defecto corrido contra la `ACTA 28` (`secciones 3.2 y 6.1`). **Corrido hoy contra la `ACTA 29`, el
> `HEREDADO 1` es el TITULO DEL ACTA**, que lleva la palabra dentro de la frase *rompiendo el remedio
> que yo mismo escribi*. La regla vieja era **cada seccion cuyo encabezado nombre un `REMEDIO`**, y un
> encabezado `# ACTA ...` es un encabezado. **El primer remedio que el arnes le pone delante al
> auditor no era un remedio: era el resumen de la vuelta pasada.**

**LA CAUSA, EN UNA LINEA:** un auditor **escribe** sus remedios una vez, en su tabla, y despues los
**menciona** muchas, para decir que se cumplieron o para contarse una caida. **La regla vieja se
quedaba con las menciones y perdia la tabla.**

### X.2.b. **LO QUE HAY QUE HACER, HECHO: el arnes entrega la TABLA que el acta escribe**

**`src/herencia.py` ya no busca secciones: busca la tabla de remedios y entrega sus FILAS**, una por
remedio. La forma que reconoce es la que esta casa ya escribe, y **las tres condiciones estan en el
codigo con su motivo al lado**:

| condicion | por que no sobra ninguna |
|---|---|
| es la **PRIMERA fila** de su tabla | sin esto, una fila de datos que diga `REMEDIO ROTO` abre una tabla que nadie escribio. **No es hipotetico: es la tabla `\\| \\| \\|` de la `ACTA 29` `8.1`**, y me la levanto en la primera corrida |
| lleva el **separador markdown** debajo | es lo que distingue una cabecera de una fila suelta |
| **no esta en cita** | una tabla copiada dentro de un bloque de cita se esta **CITANDO**, y citar es justo lo que no se entrega |
| la celda es la **columna `REMEDIO`**, desnuda | la `ACTA 29` `9.4` pone `\\| lo que detecto \\| el remedio autorizado \\| donde lo encargo \\|`: es una tabla **SOBRE** remedios, no la que los escribe. **Tambien me la levanto, y tambien la cace probando** |

**Y SI UN ACTA NOMBRA REMEDIOS Y NO ESCRIBE TABLA, EL INSTRUMENTO LO DICE EN VOZ ALTA** con un
`AVISO`, en vez de callarse. **Un arnes que entrega cero remedios sin avisar es el mismo defecto por
la puerta de atras**, y esa era la forma mas facil de "arreglar" esto sin arreglarlo.

### X.2.c. **EL CASO POSITIVO, OBLIGATORIO** (cosecha `7.C`: una guarda que no muerde es cifra)

**Anadi `--acta` para poder correrlo contra las actas viejas**, que es lo que el caso positivo pide:
una guarda que solo se puede probar contra el acta de hoy no se puede probar.

<!-- TALLADO: salida=.v31/caso_positivo_herencia.txt -->

""" + tabla_resumen + """

""" + tabla_detalle + """

> ### **Y AQUI TENGO UNA DISCREPANCIA CONTRA EL ENCARGO, Y GANA MI INSTRUMENTO** (`EXTRACTOR.md` 5, y el propio encargo: *gana el tuyo y declaras la discrepancia*)
>
> **EL ENCARGO DICE:** *corrido contra la `ACTA 28`, tiene que devolver **los dos** remedios de su
> tabla (**el de la celda de la apertura sellada** y **el de la razon por vez**)*, y que esa tabla es
> *la que precede a su seccion `9`*.
>
> **LO QUE MIDO, y son tres cosas que no cuadran:**
>
> 1. **la tabla de remedios de la `ACTA 28` tiene CUATRO filas, no dos** (lineas `26180` a `26183`);
> 2. **no precede a su seccion `9`: es su seccion `10`**, y precede a la `11`;
> 3. **los dos remedios que el encargo nombra son, al digito, los de la tabla de la `ACTA 27`**:
>    `NINGUNA CELDA DE MI APERTURA SELLADA PUBLICA...` (linea `25165`) y
>    `LA RELECTURA CIEGA DESTAPA UNA RAZON POR VEZ...` (linea `25166`). **Dos filas, seccion `10`.**
>
> **NO ES UN DESCUIDO SUELTO: ES LA MISMA CAIDA QUE EL AUDITOR SE CARGO A SI MISMO Y LA QUE ME CARGO A
> MI.** La `ACTA 29` `8.1` escribe *LO QUE ESCRIBI (`ACTA 28`, tabla de remedios, antes de su seccion
> `9`)* y **cita debajo el texto de la tabla de la `ACTA 27`**. El encargo hereda esa atribucion. **Es
> literalmente la especie de `7.1`, la `ACTA 28` puesta donde va la `ACTA 27`**, en tres sedes ya:
> mi reporte, la razon de la linea `300`, y ahora esto.
>
> **Y NO ES PARADA, y digo por que en vez de dejarlo en el aire** (`EXTRACTOR.md` 7): lo que la
> `TAREA 2.b` me manda es **una sola frase y no admite dos lecturas** (*que entregue los remedios que
> el acta ESCRIBE, no los que CITA*), **la prueba acida del `2.c` es exacta** (*no sus secciones `3.2`
> y `6.1`*) **y se cumple en las tres actas**, y **la cifra de la `ACTA 29` me sale al digito: `3`**.
> **Lo que falla es un puntero, no el encargo**, y arreglarlo no me pedia decidir nada.
>
> **LOS DOS REMEDIOS QUE EL ENCARGO NOMBRA SALEN LOS DOS, ademas**: el de la celda de la apertura
> sellada y el de la razon por vez estan en mi tabla, como `ACTA 27` `1` y `2`. **Lo unico que no
> sale es que sean de la `ACTA 28`.**

**Y LA PRUEBA QUE FALLA SI EL EXTRACTOR VUELVE A COGER UNA SECCION QUE SOLO MENCIONA LA PALABRA**, que
es lo que el `2.c` pide con esas palabras. Vive en `PruebaHerencia` de `tests/test_aceptacion.py` y
**la corro contra el codigo viejo para probar que muerde**, que es lo unico que distingue una guarda
de una intencion:

<!-- TALLADO: parcial salida=.v31/mordida_regla_vieja.txt -->

""" + sangrado(".v31/mordida_regla_vieja.txt") + """

**SON SIETE PRUEBAS NUEVAS Y NINGUNA RETIRADA**, y el fixture del `PruebaHerencia` lleva ahora **las
cuatro trampas que el acta real lleva**: una acta vieja con su tabla, una seccion que solo menciona la
palabra, una tabla citada dentro de un bloque de cita, y una tabla que habla de remedios sin
escribirlos.

<!-- TALLADO: parcial salida=.v31/aceptacion_t2.txt -->

    $ python tests/test_aceptacion.py
      total: 200 pruebas, 0 fallos, 0 errores

**`193` al abrir y `200` al cerrar la tarea. Las `7` son las nuevas** (`X.0` publica el `193` medido
antes de tocar nada).

### X.2.d. **LA OTRA MITAD DEL ARNES: LA COLA DE VECINOS NO LLEGO, Y NO LA DEJO CALLADA**

*Es la propuesta `3` de mi reporte anterior, adjudicada por el auditor y devuelta aqui como parte de
la `TAREA 2`.*

**LO QUE `D.43` EXTENDIDA MANDA DESDE EL 16 sep:** *el arnes te entrega la cola por candidato,
sellada, como ya te entrega el informe de lote. Tu la citas por su sello; no la recomputas.*

**LO QUE MIDO:** no llego. La salida esta pegada en `X.0.a`: **ni `INFORME_DE_LOTE.txt`, ni
`SELLOS_INFORME.jsonl`, ni ningun fichero de cola en `docs/loop/`.**

| | |
|---|---|
| **lo que cuesta no traerla, medido por el auditor** | `26` corridas de la aduana dentro del turno de la vuelta 30, **de entre `63` y `136` segundos cada una** (`ACTA 29`, cierre de `W.8.f`) |
| **lo que cuesta el instrumento por su cuenta** | `buscar_vecinos` tarda **`73,3` segundos sobre `510`** (cronometrado por el auditor de la vuelta 28, citado en `D.43`) |
| **lo que hago hoy** | **la pago yo dentro del turno, una corrida por candidato**, que es lo unico que se puede hacer sin saltarse la aduana |
| **lo que NO hago** | **no la fabrico.** `EXTRACTOR.md` 13: ninguna vuelta fabrica arneses nuevos, y la `TAREA 2` ordena expresamente **un** arreglo, el de `herencia.py`. **Un segundo instrumento en la misma vuelta seria maquinaria que nadie encargo** |

> **NO CABE EN ESTA VUELTA Y LO DECLARO CON SU CIFRA**, que es exactamente lo que el `2.d` pide.
> **Queda como propuesta en `X.7`**, porque la sede donde el extractor propone es su reporte
> (`EXTRACTOR.md` 14) y **el arnes no es sede mia**.

"""

viejo = """## X.2. **TAREA 2, BLOQUEANTE**: el arnes que no entrega los remedios que `D.40` le manda entregar

PENDIENTE

"""
assert s.count(viejo) == 1
io.open(RUTA, "w", encoding="utf-8", newline="").write(s.replace(viejo, nuevo))
print("ok")
