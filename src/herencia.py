# -*- coding: utf-8 -*-
"""LO QUE UN AUDITOR LE DEJA AL SIGUIENTE LO ENTREGA EL ARNES, NO LA MEMORIA (D.40).

    python forja.py herencia                  imprime lo que la vuelta hereda
    python forja.py herencia --comprobar      comprueba la apertura ciega contra ello

POR QUE EXISTE. Tres actas seguidas, el mismo remedio escrito por el auditor a si
mismo, y las tres incumplido. El propio auditor lo diagnostico en la `ACTA 16` y
volvio a fallar en la 17: **no es falta de voluntad, es de arquitectura.** Un
remedio que vive en un fichero de 16.000 lineas y que hay que acordarse de ir a
buscar **no esta entregado: esta archivado.**

LA HERENCIA ES LA DE SU LINEA (`D.48`, 17 sep 2026, decision del fundador). **Una linea
que no ha cerrado ninguna tanda hereda CERO remedios**, aunque tenga un `ACTA_AUDITOR.md`
entero delante. El 16 sep 2026 tres frentes de libro nacieron de la rama serial, se
llevaron su acta entera, y el arnes les entrego **`4 remedio(s)` de otra secuencia** a
cada uno; el auditor del primero paro citando como suyas **tres tandas de un libro que no
era el suyo**. Quien manda aqui es `docs/loop/CREDITO_<linea>.jsonl` (`src/credito.py`):
si esa linea no tiene ninguna tanda, no hay de quien heredar, **y se dice en voz alta**.

LO QUE HACE. Lee la ULTIMA acta de `docs/loop/ACTA_AUDITOR.md` (de su ultimo
encabezado `# ACTA` hasta el final) y saca de ahi:

  - cada bloque en cita cuyo titulo diga `TAREA BLOQUEANTE DEL AUDITOR`
  - **cada FILA de la tabla de remedios que esa acta ESCRIBE**

y los numera.

ENTREGA LOS REMEDIOS QUE EL ACTA ESCRIBE, NO LOS QUE CITA (16 sep 2026, TAREA 2 de
la vuelta 31, encargada por la `ACTA 29` `8.1` con su caida delante). **Hasta hoy
cogia cada seccion cuyo encabezado nombrara un REMEDIO, y eso es otra cosa.** Un
auditor escribe sus remedios UNA vez, en su tabla, y despues los MENCIONA muchas:
para decir que se cumplieron, para contarse una caida, hasta en el titulo del acta.
La regla vieja se quedaba con las menciones y perdia la tabla.

    LO QUE MEDIA LA REGLA VIEJA, corrido contra la ACTA 28:
      HEREDADO 1  -> ACTA 28 seccion 3.2   (CITA el remedio 2 de la ACTA 27)
      HEREDADO 2  -> ACTA 28 seccion 6.1   (CITA el heredado 1 para decir que aguanto)
    y su tabla de remedios, la de su seccion 10, NO SALIA.

    Y CONTRA LA ACTA 29 era peor: el HEREDADO 1 era **el titulo del acta**, que
    lleva la palabra remedio dentro de la frase `rompiendo el remedio que yo mismo
    escribi`.

**EL COSTE ESTA MEDIDO Y NO ES HIPOTETICO:** el auditor de la `ACTA 29` rompio en su
apertura sellada el `REMEDIO 1` que el mismo habia escrito, **porque el arnes no se lo
entrego** (`ACTA 29` `8.1`). Se lo cargo igualmente, citando `D.40`: *el fallo era de
arquitectura, y la arquitectura es del arnes.*

LA FORMA QUE SE RECONOCE, Y ES LA QUE ESTA CASA YA ESCRIBE: una tabla markdown cuya
CABECERA nombre `REMEDIO`, **fuera de cita**. Cada fila de datos es un remedio.

    | # | **REMEDIO** | como se comprueba que se cumplio |
    |---:|---|---|
    | **1** | **NINGUNA CELDA DE MI APERTURA SELLADA ...** | que ninguna celda ... |

**FUERA DE CITA es la mitad que hace el trabajo:** un acta que copia la tabla de la
anterior dentro de un bloque de cita la esta CITANDO, y eso es justo lo que no se
entrega.

**Y SI EL ACTA NOMBRA REMEDIOS Y NO PONE TABLA, EL INSTRUMENTO LO DICE EN VOZ ALTA**
en vez de callarse: un arnes que entrega cero remedios sin avisar es el mismo defecto
por la puerta de atras.

EL ARNES **antepone** esa lista al prompt de la fase ciega, y **exige** que la
apertura ciega traiga:

    ACTA ANTERIOR LEIDA: <hash>
    HEREDADO 1: CUMPLIDO            (o NO APLICA, con su motivo detras)

**Si falta alguna, el arnes se detiene ANTES de escribir el acta y nombra lo que
falta.** El `<hash>` es el de `git hash-object` sobre el acta: no vale decir que se
leyo otra version.

Y LA FASE CIEGA SI PUEDE ABRIR `ACTA_AUDITOR.md`, que conviene decirlo porque
parece lo contrario: **el acta es obra del auditor, no del extractor.** `D.34.2`
retira cuatro ficheros y ese no es ninguno de los cuatro. Leer su propia acta no es
contaminacion: es lo unico que le deja saber que se encargo a si mismo.
"""

import os
import re
import subprocess
import sys

from . import comun, credito

RUTA_ACTA = os.path.join(comun.RAIZ, "docs", "loop", "ACTA_AUDITOR.md")
RUTA_APERTURA = os.path.join(comun.RAIZ, "docs", "loop", "APERTURA_CIEGA.md")

MARCA_ACTA = re.compile(r"^#\s+ACTA\s", re.M)
# LA APERTURA ES MARKDOWN Y SE COMPRUEBA COMO MARKDOWN. Las comillas, la negrita,
# el encabezado y la cita son como escribe esta casa entera, y D.40 pide una LINEA
# DECLARADA, no una linea desnuda. Se quita el adorno ANTES de buscar.
ADORNO = re.compile(r"[`*~]+")
MARGEN = re.compile(r"^[>\s#]+", re.M)
LINEA_ACTA = re.compile(r"ACTA\s+ANTERIOR\s+LEIDA\s*:\s*([0-9a-fA-F]{7,40})")
HUELLA_MINIMA = 7            # una huella corta sigue siendo la misma huella

# UN `NO APLICA` LLEVA LA SALIDA DEL INSTRUMENTO PEGADA, NO SOLO EL MOTIVO
# (D.40 ensanchada el 16 sep 2026, decision del fundador, punto 2.a).
#
# POR QUE. La vuelta 26 declaro `NO APLICA` el heredado que le pedia sanear los
# guiones al volcar texto al arbol, con el motivo de que ninguno de sus
# instrumentos escribia en el arbol. **Seis escribian, su propia tabla los lista, y
# el barrido de guiones estaba en ROJO con ocho hallazgos suyos al empezar su turno
# normal.** D.40 exigia motivo y el motivo estaba escrito: exigia que lo hubiera,
# no que fuera cierto.
#
# UNA SALIDA PEGADA NO PRUEBA QUE EL MOTIVO SEA CIERTO, pero obliga a correr algo
# antes de escribirlo, y **habria cazado ese motivo al instante**: no hay manera de
# pegar un `grep` que diga que ninguno escribe cuando seis escriben.
SALIDA_PEGADA = re.compile(r"^\s*(?:>\s*)?\$\s+\S", re.M)
VENTANA_DE_SALIDA = 12       # lineas tras el NO APLICA donde se busca su salida
NO_APLICA_CRUDO = re.compile(
    r"HEREDADO\s*`?\s*(\d+)\s*`?\s*[:\*]*\s*\**\s*NO APLICA([^\n]*)", re.I)
TITULO_TAREA = "TAREA BLOQUEANTE DEL AUDITOR"
ENCABEZADO = re.compile(r"^>?\s*#{1,6}\s")
TOPE_DE_CUERPO = 40          # lineas por item: el resto se cita por su linea

# LA TABLA DE REMEDIOS: una tabla markdown, FUERA DE CITA, cuya cabecera nombre
# REMEDIO. Lo que se entrega son sus FILAS, una por remedio.
FILA = re.compile(r"^\s*\|")
SEPARADOR = re.compile(r"^\s*\|[\s:|-]+\|?\s*$")
EN_CITA = re.compile(r"^\s*>")
# LA CELDA TIENE QUE SER LA COLUMNA REMEDIO, NO UNA QUE NOMBRE LA PALABRA. La
# ACTA 29 9.4 pone `| lo que detecto | el remedio autorizado | donde lo encargo |`,
# que es una tabla SOBRE remedios y no la que los escribe. Se exige la cabecera
# desnuda, que es como esta casa la escribe: `| # | **REMEDIO** | como se comprueba |`.
CABECERAS_DE_REMEDIO = ("REMEDIO", "REMEDIOS")
NUMERO_ACTA = re.compile(r"^#*\s*ACTA\s+(\d+)")


def huella(ruta):
    """La misma huella que usa el testigo del arnes, para no medir de dos formas."""
    try:
        salida = subprocess.check_output(["git", "hash-object", ruta],
                                         cwd=comun.RAIZ, stderr=subprocess.STDOUT)
        return salida.decode("utf-8", "replace").strip()
    except Exception:
        return "sin-huella"


def _ultima_acta(lineas):
    """Devuelve (indice de inicio, titulo) de la ultima acta del fichero."""
    inicio, titulo = 0, "(sin encabezado de acta)"
    for numero, linea in enumerate(lineas):
        if MARCA_ACTA.match(linea):
            inicio, titulo = numero, linea.strip().lstrip("# ").strip()
    return inicio, titulo


def _recortar(cuerpo, linea_inicial):
    if len(cuerpo) <= TOPE_DE_CUERPO:
        return cuerpo
    resto = len(cuerpo) - TOPE_DE_CUERPO
    return cuerpo[:TOPE_DE_CUERPO] + [
        "",
        "[RECORTADO: %d lineas mas, desde la linea %d de docs/loop/ACTA_AUDITOR.md. "
        "PUEDES ABRIR EL ACTA: es tuya, y no es ninguno de los cuatro ficheros que "
        "D.34.2 retira.]" % (resto, linea_inicial + TOPE_DE_CUERPO)]


def _es_cabecera_de_remedios(lineas, numero):
    """Cierto si la linea `numero` abre una tabla cuya CABECERA nombra REMEDIO.

    LAS TRES CONDICIONES, y ninguna sobra:

      1. **es la PRIMERA fila de su tabla.** Sin esto, una fila de datos que diga
         `REMEDIO ROTO` abre una tabla de remedios que nadie escribio: es el falso
         positivo real de la `ACTA 29` `8.1`, cuya tabla `| | |` lleva esa celda.
      2. **lleva el separador markdown justo debajo.** Es lo que distingue una
         cabecera de una fila suelta.
      3. **no esta en cita.** Una tabla copiada dentro de un bloque de cita se esta
         CITANDO, y citar es justo lo que no se entrega.

    Se mira celda a celda y sin adorno: esta casa escribe `| # | **REMEDIO** | ... |`
    y la negrita no es parte del nombre de la columna.
    """
    linea = lineas[numero]
    if EN_CITA.match(linea) or not FILA.match(linea):
        return False
    anterior = lineas[numero - 1] if numero > 0 else ""
    if FILA.match(anterior):
        return False
    if numero + 1 >= len(lineas) or not SEPARADOR.match(lineas[numero + 1]):
        return False
    for celda in linea.strip().strip("|").split("|"):
        if ADORNO.sub("", celda).strip().upper() in CABECERAS_DE_REMEDIO:
            return True
    return False


def _seccion_de(lineas, numero):
    """El encabezado bajo el que vive esa linea, para que la fila no llegue desnuda."""
    for atras in range(numero, -1, -1):
        if ENCABEZADO.match(lineas[atras]) and not MARCA_ACTA.match(lineas[atras]):
            return lineas[atras].strip()
    return ""


def _numero_de_acta(texto):
    """El numero propio de un encabezado de acta: `# ACTA 28. VUELTA ...` da `28`."""
    encaje = NUMERO_ACTA.match(ADORNO.sub("", (texto or "").strip()))
    return encaje.group(1) if encaje else ""


def _acta_pedida(lineas, seleccion):
    """(inicio, fin, titulo) del acta pedida. Sin seleccion, la ULTIMA."""
    marcas = [n for n, l in enumerate(lineas) if MARCA_ACTA.match(l)]
    if not marcas:
        return 0, len(lineas), "(sin encabezado de acta)"
    elegida = marcas[-1]
    if seleccion:
        # SE ELIGE POR EL NUMERO PROPIO DEL ACTA, NO POR LOS QUE SU TITULO CITA.
        # El titulo de la ACTA 29 nombra dentro a la 28 y a la 27, asi que buscar
        # el texto suelto devolvia siempre la ultima: la misma especie de defecto
        # que esta tarea vino a cerrar, cazada al probarla.
        numeros = [_numero_de_acta(lineas[n]) for n in marcas]
        busca = _numero_de_acta(seleccion) or _numero_de_acta("ACTA " + str(seleccion))
        candidatas = [n for n, suyo in zip(marcas, numeros) if suyo and suyo == busca]
        if not candidatas:
            raise ValueError("ninguna acta lleva el numero de %r. Las que hay: %s"
                             % (seleccion, ", ".join(s for s in numeros if s)))
        elegida = candidatas[-1]
    siguientes = [n for n in marcas if n > elegida]
    fin = siguientes[0] if siguientes else len(lineas)
    return elegida, fin, lineas[elegida].strip().lstrip("# ").strip()


def extraer(ruta_acta=None, seleccion=None):
    """Devuelve el diccionario de lo que la vuelta hereda.

    `seleccion` es un trozo del encabezado del acta (`"ACTA 28"`), y existe para el
    CASO POSITIVO: una guarda que solo se puede probar contra el acta de hoy no se
    puede probar (cosecha 7.C). Sin ella se lee la ULTIMA, que es lo que hace el arnes.
    """
    ruta_acta = ruta_acta or RUTA_ACTA
    if not os.path.exists(ruta_acta):
        return {"huella": "sin-acta", "acta": "(no hay acta todavia)", "items": [],
                "avisos": []}

    # LA HERENCIA ES LA DE SU LINEA (D.48, 17 sep 2026, decision del fundador).
    # Una linea que no ha cerrado ninguna tanda NO HEREDA NADA, aunque tenga un acta
    # entera delante: esa acta es de la linea de la que salio. El 16 sep los tres
    # frentes nacieron de la serial, heredaron `4 remedio(s)` cada uno, y el auditor
    # del primero paro citando como suyas tres tandas de un libro que no era el suyo.
    #
    # Y EL DISCRIMINADOR NO ES "ESTA LINEA NO TIENE FICHERO", que es lo que escribi
    # primero y lo que el banco del arnes tumbo con tres rojos: en un arbol donde el
    # registro de credito NO SE USA TODAVIA, ninguna linea tiene fichero, y D.40
    # dejaba de entregar nada **por una ausencia que no significa nada**. Es el mismo
    # defecto que D.40 vino a cerrar, reintroducido por la puerta de atras.
    #
    # LO QUE SI DISCRIMINA: que el mecanismo este EN USO en este arbol. Si alguna
    # linea tiene registro y esta no, entonces esta salio de aquella y no ha dictado
    # nada (D.48). Si no lo tiene nadie, no hay de que deducir nada y se dice.
    linea = credito.linea_actual()
    if not credito.lineas_con_registro():
        pass
    elif not credito.nacida(linea):
        return {"huella": huella(ruta_acta), "acta": "(ninguna de esta linea)",
                "items": [], "linea": linea, "avisos": [
                    "LINEA RECIEN NACIDA: '%s' no tiene ninguna tanda cerrada en %s, "
                    "asi que HEREDA CERO REMEDIOS (D.48). El acta que hay en este "
                    "arbol es de la linea de la que esta rama salio, y sus remedios "
                    "son de esa secuencia, no de esta. Una racha cuenta tandas "
                    "SEGUIDAS, y entre lineas simultaneas no hay orden que seguir."
                    % (linea, comun.relativa(credito.ruta(linea)))]}
    lineas = comun.leer_texto(ruta_acta).split("\n")
    inicio, fin, titulo = _acta_pedida(lineas, seleccion)
    items, avisos = [], []
    menciones = 0

    numero = inicio
    while numero < fin:
        linea = lineas[numero]
        # 1. EL BLOQUE EN CITA con el titulo de la tarea bloqueante.
        if linea.lstrip().startswith(">") and TITULO_TAREA in linea:
            cuerpo = []
            while numero < fin and lineas[numero].lstrip().startswith(">"):
                cuerpo.append(lineas[numero])
                numero += 1
            items.append({"clase": "TAREA BLOQUEANTE", "linea": numero - len(cuerpo) + 1,
                          "cuerpo": _recortar(cuerpo, numero - len(cuerpo) + 1)})
            continue
        # 2. LA TABLA DE REMEDIOS QUE EL ACTA ESCRIBE: se entregan sus FILAS.
        if _es_cabecera_de_remedios(lineas, numero):
            cabecera, seccion = linea, _seccion_de(lineas, numero)
            numero += 1
            if numero < fin and SEPARADOR.match(lineas[numero]):
                numero += 1
            while (numero < fin and FILA.match(lineas[numero])
                   and not EN_CITA.match(lineas[numero])):
                items.append({"clase": "REMEDIO", "linea": numero + 1,
                              "cuerpo": _recortar([seccion, "", cabecera,
                                                   lineas[numero]], numero + 1)})
                numero += 1
            continue
        # 3. LO QUE SOLO MENCIONA LA PALABRA SE CUENTA, PARA PODER AVISAR.
        if ENCABEZADO.match(linea) and "REMEDIO" in linea.upper():
            menciones += 1
        numero += 1

    if menciones and not any(i["clase"] == "REMEDIO" for i in items):
        avisos.append(
            "AVISO: esta acta MENCIONA remedios en %d encabezado(s) y no ESCRIBE "
            "ninguna tabla de remedios fuera de cita. No se entrega ninguno, y se "
            "dice en voz alta: un arnes que entrega cero sin avisar es el defecto "
            "que la TAREA 2 de la vuelta 31 vino a cerrar." % menciones)

    return {"huella": huella(ruta_acta), "acta": titulo, "items": items,
            "avisos": avisos}


def texto_para_prompt(herencia):
    """El bloque que el arnes antepone al prompt de la fase ciega."""
    lineas = ["REMEDIOS PENDIENTES QUE HEREDAS",
              "",
              "Esto NO lo has buscado tu: lo entrega el arnes (D.40), porque tres actas "
              "seguidas perdieron el mismo remedio por tener que ir a buscarlo.",
              "",
              "  acta anterior : %s" % herencia["acta"],
              "  su huella     : %s" % herencia["huella"],
              "  heredados     : %d" % len(herencia["items"]),
              ""]
    for aviso in herencia.get("avisos") or []:
        lineas.extend([aviso, ""])
    if not herencia["items"]:
        lineas.append("El acta anterior no dejo ninguna tarea bloqueante ni ningun "
                      "remedio escrito. Aun asi tienes que declarar la linea de lectura.")
    for indice, item in enumerate(herencia["items"], 1):
        lineas.append("HEREDADO %d   [%s, linea %d del acta]"
                      % (indice, item["clase"], item["linea"]))
        lineas.extend(item["cuerpo"])
        lineas.append("")
    lineas.extend([
        "LO QUE TU APERTURA CIEGA TIENE QUE TRAER, O EL ARNES SE DETIENE ANTES DE QUE "
        "ESCRIBAS EL ACTA:",
        "",
        "    ACTA ANTERIOR LEIDA: %s" % herencia["huella"],
    ])
    for indice in range(1, len(herencia["items"]) + 1):
        lineas.append("    HEREDADO %d: CUMPLIDO          (o NO APLICA y su motivo detras)"
                      % indice)
    lineas.extend([
        "",
        "NO APLICA NECESITA MOTIVO ESCRITO **Y LA SALIDA DEL INSTRUMENTO PEGADA "
        "DEBAJO** (D.40, 16 sep 2026). Un remedio que no aplica a esta vuelta se "
        "declara, se dice por que, y se pega el comando que lo sostiene, con una "
        "linea que empiece por '$'. Sin salida pegada, el sello NO lo acepta.",
        "",
        "POR QUE: la vuelta 26 declaro NO APLICA un heredado con el motivo de que "
        "ninguno de sus instrumentos escribia en el arbol. Seis escribian, su propia "
        "tabla los listaba, y el barrido de guiones estaba en ROJO con ocho hallazgos "
        "suyos. Una salida pegada no prueba que el motivo sea cierto, pero obliga a "
        "correr algo antes de escribirlo, y ese lo habria cazado al instante.",
        "",
        "ESCRIBELAS COMO ESCRIBES TODO LO DEMAS. Valen las comillas, la negrita, el "
        "encabezado y la cita: se comprueba que la declaracion ESTE, no que vaya "
        "desnuda. Y puedes repetirla en tu tabla de cierre: se mira presencia y no "
        "cuenta, asi que citar la linea que declaras no te tumba la vuelta.",
        ""])
    return "\n".join(lineas)


def _sin_adornos(texto):
    """Quita el adorno de markdown para poder buscar la declaracion dentro de el."""
    return MARGEN.sub("", ADORNO.sub("", texto))


def _tiene_salida_pegada(crudo, indice):
    """Cierto si ALGUN `NO APLICA` de ese heredado trae su salida debajo.

    Se mira el texto CRUDO y no el desnudo, porque lo que se busca es la sangria y
    el `$` de una salida pegada, y `_sin_adornos` se los come.
    """
    lineas = crudo.splitlines()
    for numero, linea in enumerate(lineas):
        encaje = NO_APLICA_CRUDO.search(linea)
        if not encaje or int(encaje.group(1)) != indice:
            continue
        ventana = chr(10).join(lineas[numero:numero + VENTANA_DE_SALIDA + 1])
        if SALIDA_PEGADA.search(ventana):
            return True
    return False


def comprobar(herencia, ruta_apertura=None):
    """Devuelve la lista de lo que FALTA en la apertura ciega. Vacia es verde.

    SE COMPRUEBA PRESENCIA, NO CONTEO. Una apertura que declara su herencia arriba
    y la repite en su tabla de cierre esta declarando **mas**, no menos, y hacerla
    caer por eso es castigar a quien cumple. Basta con que UNA de las veces que
    aparece este bien puesta.
    """
    ruta_apertura = ruta_apertura or RUTA_APERTURA
    if not os.path.exists(ruta_apertura):
        return ["docs/loop/APERTURA_CIEGA.md no existe"]
    crudo = comun.leer_texto(ruta_apertura)
    texto = _sin_adornos(crudo)
    faltan = []

    huellas = LINEA_ACTA.findall(texto)
    buena = herencia["huella"]
    if not huellas:
        faltan.append("falta la linea 'ACTA ANTERIOR LEIDA: %s'" % buena)
    elif not any(len(h) >= HUELLA_MINIMA and buena.startswith(h.lower()) for h in huellas):
        faltan.append("la linea 'ACTA ANTERIOR LEIDA' esta, pero con otra huella: se "
                      "espera '%s' y se leyo %s"
                      % (buena, ", ".join("'%s'" % h for h in huellas)))

    for indice in range(1, len(herencia["items"]) + 1):
        patron = re.compile(r"HEREDADO\s+%d\s*:\s*(CUMPLIDO|NO APLICA)([^\n]*)" % indice)
        encajes = patron.findall(texto)
        if not encajes:
            faltan.append("falta la linea 'HEREDADO %d: CUMPLIDO' o 'NO APLICA' "
                          "(heredado %d de %d)" % (indice, indice, len(herencia["items"])))
        elif any(clase == "CUMPLIDO" for clase, _resto in encajes):
            continue
        elif not any(resto.strip(" :.-") for _clase, resto in encajes):
            faltan.append("el HEREDADO %d dice NO APLICA y va SIN MOTIVO escrito" % indice)
        elif not _tiene_salida_pegada(crudo, indice):
            faltan.append(
                "el HEREDADO %d dice NO APLICA con su motivo, pero SIN LA SALIDA DEL "
                "INSTRUMENTO PEGADA debajo (D.40, 16 sep 2026). Un motivo sin salida "
                "es una afirmacion; pega el comando que lo sostiene, con una linea "
                "que empiece por '$'" % indice)
    return faltan


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or [])
    seleccion = None
    if "--acta" in argumentos:
        donde = argumentos.index("--acta")
        if donde + 1 >= len(argumentos):
            print("forja.py herencia --acta necesita un trozo del encabezado del "
                  "acta, por ejemplo: --acta ACTA 28")
            return 2
        seleccion = argumentos[donde + 1]
    try:
        herencia = extraer(seleccion=seleccion)
    except ValueError as fallo:
        print("forja.py herencia: %s" % fallo)
        return 2
    if "--comprobar" in argumentos:
        faltan = comprobar(herencia)
        if not faltan:
            cuantos = len(herencia["items"])
            print("APERTURA CIEGA COMPLETA: el acta anterior va leida por su huella y "
                  "%s." % ("el heredado va declarado" if cuantos == 1
                           else "los %d heredados van declarados" % cuantos))
            return 0
        print("APERTURA CIEGA INCOMPLETA: %d cosa(s) que faltan (D.40)." % len(faltan))
        for falta in faltan:
            print("  " + falta)
        return 1
    print(texto_para_prompt(herencia))
    return 0
