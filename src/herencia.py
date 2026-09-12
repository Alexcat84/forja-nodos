# -*- coding: utf-8 -*-
"""LO QUE UN AUDITOR LE DEJA AL SIGUIENTE LO ENTREGA EL ARNES, NO LA MEMORIA (D.40).

    python forja.py herencia                  imprime lo que la vuelta hereda
    python forja.py herencia --comprobar      comprueba la apertura ciega contra ello

POR QUE EXISTE. Tres actas seguidas, el mismo remedio escrito por el auditor a si
mismo, y las tres incumplido. El propio auditor lo diagnostico en la `ACTA 16` y
volvio a fallar en la 17: **no es falta de voluntad, es de arquitectura.** Un
remedio que vive en un fichero de 16.000 lineas y que hay que acordarse de ir a
buscar **no esta entregado: esta archivado.**

LO QUE HACE. Lee la ULTIMA acta de `docs/loop/ACTA_AUDITOR.md` (de su ultimo
encabezado `# ACTA` hasta el final) y saca de ahi:

  - cada bloque en cita cuyo titulo diga `TAREA BLOQUEANTE DEL AUDITOR`
  - cada seccion cuyo encabezado nombre un `REMEDIO`

y los numera. El arnes **antepone** esa lista al prompt de la fase ciega, y
**exige** que la apertura ciega traiga:

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

from . import comun

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
TITULO_TAREA = "TAREA BLOQUEANTE DEL AUDITOR"
ENCABEZADO = re.compile(r"^>?\s*#{1,6}\s")
TOPE_DE_CUERPO = 40          # lineas por item: el resto se cita por su linea


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


def extraer(ruta_acta=None):
    """Devuelve el diccionario de lo que la vuelta hereda."""
    ruta_acta = ruta_acta or RUTA_ACTA
    if not os.path.exists(ruta_acta):
        return {"huella": "sin-acta", "acta": "(no hay acta todavia)", "items": []}
    lineas = comun.leer_texto(ruta_acta).split("\n")
    inicio, titulo = _ultima_acta(lineas)
    items = []

    numero = inicio
    while numero < len(lineas):
        linea = lineas[numero]
        # 1. EL BLOQUE EN CITA con el titulo de la tarea bloqueante.
        if linea.lstrip().startswith(">") and TITULO_TAREA in linea:
            cuerpo = []
            while numero < len(lineas) and lineas[numero].lstrip().startswith(">"):
                cuerpo.append(lineas[numero])
                numero += 1
            items.append({"clase": "TAREA BLOQUEANTE", "linea": numero - len(cuerpo) + 1,
                          "cuerpo": _recortar(cuerpo, numero - len(cuerpo) + 1)})
            continue
        # 2. LA SECCION cuyo encabezado nombra un remedio.
        if ENCABEZADO.match(linea) and "REMEDIO" in linea.upper():
            primera = numero
            cuerpo = [linea]
            numero += 1
            while numero < len(lineas) and not ENCABEZADO.match(lineas[numero]):
                cuerpo.append(lineas[numero])
                numero += 1
            items.append({"clase": "REMEDIO", "linea": primera + 1,
                          "cuerpo": _recortar(cuerpo, primera + 1)})
            continue
        numero += 1

    return {"huella": huella(ruta_acta), "acta": titulo, "items": items}


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
        "NO APLICA NECESITA MOTIVO ESCRITO. Un remedio que no aplica a esta vuelta se "
        "declara y se dice por que; dejarlo en blanco es lo mismo que perderlo, que es "
        "lo que D.40 vino a impedir.",
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
    texto = _sin_adornos(comun.leer_texto(ruta_apertura))
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
        elif not any(clase == "CUMPLIDO" or resto.strip(" :.-")
                     for clase, resto in encajes):
            faltan.append("el HEREDADO %d dice NO APLICA y va SIN MOTIVO escrito" % indice)
    return faltan


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or [])
    herencia = extraer()
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
