# -*- coding: utf-8 -*-
"""LA UNIDAD DE LA RUTA ES LA CELDA (D.42).

    python scripts/censar_rutas.py            censa y devuelve rojo si algo cae
    python scripts/censar_rutas.py --todo     ademas lista lo que pasa, una a una

POR QUE EXISTE, Y POR QUE `D.41` NO BASTABA. `D.41` ata **un instrumento a una
tabla entera**: lee la declaracion de encima y compara la tabla contra ella. La
vuelta 25 no cayo asi. Cayo publicando una ruta **por fila**, en una columna
titulada *de donde sale*:

    | los pares del candidato parado | 2 ... | `.v25/cola_lectura.txt` |

y ese fichero tenia **cero bytes** mientras la cifra decia `2` donde el
instrumento da `4`. **La unidad de `D.41` es la tabla; aqui la unidad es la
celda**, y por eso hizo falta otra guarda y no un parche a la primera.

LAS TRES FORMAS, Y SOLO TRES:

  (a) RUTA CON CONTENIDO ................ pasa
  (b) RUTA VACIA (o que no esta) ........ TUMBA, salvo que la MISMA celda lleve
                                          la marca literal
                                              VACIA A PROPOSITO: <motivo>
                                          Una ruta vacia sin marca es caida de
                                          cifra (cosecha 7.B).
  (c) PATRON ............................ la celda lo escribe como
                                              PATRON: <glob>
                                          y se exige AL MENOS UNA coincidencia
                                          con contenido. Sin coincidencias,
                                          tumba.

Mas una lista FIJA en `config/sedes_vacias.json` con las sedes que una regla
escrita manda dejar vacias (`PROMPT_SIGUIENTE.md` en una parada). **Esa lista es
del fundador y es corta a proposito**: una exencion que crece sola deja de ser
exencion y pasa a ser la regla.

POR QUE LA MARCA VA EN LA CELDA Y NO EN UN FICHERO DE EXCEPCIONES. Una excepcion
escondida en `config/` la lee quien va a buscarla; **una marca en la celda la lee
quien lee la cifra**, que es justo el que tiene que saber que la sede esta vacia.
Y obliga a escribir el motivo al lado del numero que sostiene.

UNA RUTA SE RESUELVE DESDE LA RAIZ DEL REPO **Y** DESDE LA CARPETA DEL DOCUMENTO.
Un acta que vive en `docs/loop/` y escribe `paradas/2026-09-13-....md` no esta
publicando una ruta falsa: esta escribiendo una ruta relativa, y resuelve. Tratar
eso como caida seria inventar tres caidas donde no hay ninguna.
"""

import glob as _glob
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_SEDES = os.path.join(RAIZ, "config", "sedes_vacias.json")

# LA APERTURA CIEGA ENTRA EL 16 sep 2026 (decision del fundador, punto 3). Era
# **la unica sede de cifra de esta casa que ninguna guarda leia**, y ya llevaba DOS
# ejemplares encontrados a mano: la `ACTA 27` 8.1 y la caida de la vuelta 29.
# Una sede que publica cifras y que nadie mide es una sede donde las cifras viven
# tranquilas.
DOCUMENTOS = (os.path.join("docs", "loop", "REPORTE.md"),
              os.path.join("docs", "loop", "ACTA_AUDITOR.md"),
              os.path.join("docs", "loop", "APERTURA_CIEGA.md"))

EN_COMILLAS = re.compile(r"`([^`\n]+)`")
MARCA_VACIA = re.compile(r"VACIA A PROPOSITO\s*:\s*(\S.*)")
MARCA_PATRON = re.compile(r"PATRON\s*:\s*`?([^`\s|]+)`?")
GLOB = "*?["

EXTENSIONES = (".txt", ".out", ".json", ".jsonl", ".py", ".md", ".log", ".sh")
# Un trozo de comando o una plantilla NO son una ruta publicada. `<id>.json` es
# un molde, `!fuentes/...` es la mitad de un `find`, y `.md` a secas es una
# extension suelta. Contarlos seria inventar caidas y enseñar a no mirar.
NO_ES_RUTA = re.compile(r"[<>!$\"'()]")


def _sedes_exentas():
    try:
        datos = json.loads(io.open(RUTA_SEDES, encoding="utf-8").read())
    except (IOError, ValueError):
        return {}
    return dict((s["ruta"], s.get("motivo", "")) for s in datos.get("sedes", []))


def parece_ruta(cita):
    """El texto en comillas, si es una ruta publicada de este repo."""
    texto = cita.strip()
    # UNA RUTA NO LLEVA ESPACIOS. Lo que va en comillas muchas veces es la ORDEN
    # entera (`wc -l dataset/nodos.jsonl`, `python .t1/frontera.py`), y la ruta es
    # su ultimo trozo. Sin esto el censo denunciaba el comando como si fuera un
    # fichero, que es la clase de grito que enseña a no mirar la guarda.
    if " " in texto:
        texto = texto.split()[-1]
    if NO_ES_RUTA.search(texto) or texto.startswith("..."):
        return None
    if not texto.lower().endswith(EXTENSIONES):
        return None
    # Una extension suelta no es una ruta.
    if texto.lstrip(".") == "" or "/" not in texto and not texto.startswith("."):
        return None
    if os.path.basename(texto).startswith(".") and "/" not in texto:
        pass
    if texto.lstrip(".").lstrip("/") == "":
        return None
    if texto in EXTENSIONES:
        return None
    return texto


def _archivada(ruta):
    """cuarentena/<lote>/<id>.json vive en cuarentena/_insertados/<lote>/ si entro.

    NO ES UNA EXCEPCION: ES UNA REGLA DE LA CASA. `D.31` manda archivar ahi el
    candidato en el mismo acto de insertarlo, asi que una acta que lo cito en su
    bandeja cuando todavia esperaba **no publico una ruta falsa**: publico la
    unica que habia. El fichero sigue en el arbol, con su contenido, un nivel mas
    alla. Pedirle al auditor que vuelva sobre su acta de hace cuatro vueltas cada
    vez que un candidato entra seria castigar la insercion.
    """
    piezas = ruta.replace("\\", "/").split("/")
    if len(piezas) == 3 and piezas[0] == "cuarentena" and piezas[1] != "_insertados":
        return "cuarentena/_insertados/%s/%s" % (piezas[1], piezas[2])
    return None


def _resolver(ruta, carpeta_doc, raiz=None):
    """Las formas en que una ruta publicada puede resolver."""
    raiz = raiz or RAIZ
    candidatas = [os.path.join(raiz, ruta)]
    if carpeta_doc:
        candidatas.append(os.path.join(raiz, carpeta_doc, ruta))
    archivada = _archivada(ruta)
    if archivada:
        candidatas.append(os.path.join(raiz, archivada))
    return candidatas


def _existe_con_contenido(ruta, carpeta_doc, raiz=None):
    for entera in _resolver(ruta, carpeta_doc, raiz):
        if os.path.isfile(entera) and os.path.getsize(entera) > 0:
            return True, entera
        if os.path.isdir(entera):
            return True, entera
    return False, None


def _esta_pero_vacia(ruta, carpeta_doc, raiz=None):
    for entera in _resolver(ruta, carpeta_doc, raiz):
        if os.path.isfile(entera) and os.path.getsize(entera) == 0:
            return True
    return False


def _coincidencias(patron, carpeta_doc, raiz=None):
    encontradas = []
    for entera in _resolver(patron, carpeta_doc, raiz):
        for x in _glob.glob(entera):
            if os.path.isfile(x) and os.path.getsize(x) > 0:
                encontradas.append(x)
    return encontradas


# UNA RUTA NOMBRADA NO ES UNA RUTA PUBLICADA COMO SEDE, y la diferencia esta en la
# propia decision: *toda ruta publicada ... COMO SEDE DE UNA CIFRA (en tabla, en
# columna de donde sale, o en linea)*. Una frase que HABLA de un fichero (*el
# barrido tumbo `.c9/mk.py`*, *los cinco `.frag_*.md`*) no esta ofreciendolo como
# origen de ningun numero: es el sujeto de la frase.
#
# POR QUE IMPORTA Y NO ES UN ATAJO. Censar toda mencion da 42 celdas que habria que
# marcar en dos documentos de treinta mil lineas, y casi ninguna sostiene una
# cifra. **Una marca que se pone cuarenta veces deja de leerse**, y a la quinta se
# pone sin mirar: seria fabricar exactamente la excusa que D.42 vino a cerrar.
#
# LAS DOS FORMAS EN QUE UNA RUTA SE OFRECE COMO SEDE:
#   1. la CELDA es la ruta (con sus marcas y poco mas), que es la forma de la
#      columna *de donde sale*;
#   2. la unidad trae una frase que la ofrece como origen.
# OJO CON LA PALABRA `sede` A SECAS: en estos documentos aparece sobre todo en
# frases que NIEGAN que algo lo sea (*vivia fuera de sede*, *no son sede de nada*),
# y meterla aqui hacia que el censo tratara como sede justo lo que el texto decia
# que no lo era. La forma de la columna *de donde sale* ya la coge la otra rama.
OFRECE = re.compile(r"salida de|guardad[ao] en|de donde sale|su sede es|"
                    r"medid[ao] (?:con|en)|corrid[ao] (?:con|en)|impres[ao]|"
                    r"pegad[ao]|sale de|reproducid[ao]|guarda su|"
                    # Y LAS FORMAS DE OFRECER ALGO COMO PRUEBA, que es la letra de
                    # la cosecha 7.B: *una ruta publicada COMO EVIDENCIA de una
                    # corrida*. Medido al anadirlas: una sola caida nueva, y es
                    # justo el caso que la decision del 15 sep nombra por su
                    # nombre. Un criterio que solo caza lo que ya sabias que
                    # estaba no habria ampliado nada.
                    r"lo prueba|su testigo|como prueba|lo sostiene", re.I)


def es_sede(unidad, cita):
    """Cierto si la unidad OFRECE la ruta como origen de una cifra."""
    # EL MOTIVO DE LA MARCA NO CUENTA COMO PROSA. Si contara, una celda pasaria a
    # tener seis palabras por llevar su motivo escrito y **se saldria del censo por
    # haberlo declarado bien**: la marca dejaria de aparecer en el recuento y nadie
    # veria cuantas hay. Se quita la marca ENTERA, con su motivo.
    desnuda = MARCA_VACIA.sub(" ", unidad.strip())
    for sobra in ("PATRON:", "*", "#", ">", "`", "-", " "):
        desnuda = desnuda.replace(sobra, " ")
    sin_ruta = desnuda.replace(cita, " ").strip()
    # 1. la celda ES la ruta: lo que queda al quitarla es una nota corta, no prosa.
    if len(sin_ruta.split()) <= 3:
        return True
    # 2. la unidad la ofrece como origen.
    return bool(OFRECE.search(unidad))


def unidades_de(texto):
    """Las unidades de un documento: cada CELDA de tabla, o cada linea suelta."""
    for numero, linea in enumerate(texto.split("\n"), 1):
        recorte = linea.strip()
        if recorte.startswith("|"):
            trozos = recorte.strip("|").split("|")
            for indice, celda in enumerate(trozos, 1):
                yield numero, "celda %d" % indice, celda
        else:
            yield numero, "linea", linea


def censar(documentos=None, raiz=None):
    """Devuelve (caidas, pasan). Una caida es un dict con su sitio y su motivo."""
    documentos = documentos or DOCUMENTOS
    exentas = _sedes_exentas()
    caidas, pasan = [], []
    for doc in documentos:
        entera = os.path.join(raiz or RAIZ, doc)
        if not os.path.exists(entera):
            continue
        carpeta_doc = os.path.dirname(doc)
        texto = io.open(entera, encoding="utf-8").read()
        for numero, sitio, unidad in unidades_de(texto):
            marca = MARCA_VACIA.search(unidad)
            declarado = MARCA_PATRON.search(unidad)
            for cita in EN_COMILLAS.findall(unidad):
                ruta = parece_ruta(cita)
                if ruta is None or not es_sede(unidad, cita):
                    continue
                sitio_entero = {"documento": doc, "linea": numero, "sitio": sitio,
                                "ruta": ruta, "celda": unidad.strip()[:120]}

                if any(c in ruta for c in GLOB):
                    # (c) PATRON
                    if not declarado or declarado.group(1) != ruta:
                        sitio_entero["motivo"] = (
                            "es un PATRON y la celda no lo declara. Escribela como "
                            "'PATRON: %s' en la misma celda" % ruta)
                        caidas.append(sitio_entero)
                        continue
                    hits = _coincidencias(ruta, carpeta_doc, raiz)
                    if not hits and marca and marca.group(1).strip():
                        # CERO COINCIDENCIAS ES A VECES LA CIFRA. `cuarentena/
                        # _insertados/*.json` da 0 **porque ahi no cuelga ningun
                        # JSON suelto**, y eso es justo lo que la fila publica.
                        # La marca sigue exigiendo el motivo escrito al lado.
                        sitio_entero["forma"] = "PATRON sin coincidencias, declarado"
                        pasan.append(sitio_entero)
                        continue
                    if not hits:
                        sitio_entero["motivo"] = (
                            "PATRON declarado sin NI UNA coincidencia con contenido: "
                            "no sostiene ninguna cifra")
                        caidas.append(sitio_entero)
                        continue
                    sitio_entero["forma"] = "PATRON (%d con contenido)" % len(hits)
                    pasan.append(sitio_entero)
                    continue

                hay, _donde = _existe_con_contenido(ruta, carpeta_doc, raiz)
                if hay:
                    # (a) RUTA CON CONTENIDO
                    sitio_entero["forma"] = "con contenido"
                    pasan.append(sitio_entero)
                    continue

                # (b) RUTA VACIA, o que no esta
                if ruta in exentas:
                    sitio_entero["forma"] = "vacia por protocolo (config/)"
                    pasan.append(sitio_entero)
                    continue
                if marca and marca.group(1).strip():
                    sitio_entero["forma"] = "VACIA A PROPOSITO: %s" % (
                        marca.group(1).strip()[:70])
                    pasan.append(sitio_entero)
                    continue
                sitio_entero["motivo"] = (
                    "%s, y la celda no lleva la marca 'VACIA A PROPOSITO: <motivo>'. "
                    "Una ruta publicada como sede de una cifra que no prueba nada es "
                    "caida de cifra (cosecha 7.B)"
                    % ("esta y esta VACIA" if _esta_pero_vacia(ruta, carpeta_doc, raiz)
                       else "NO esta en el arbol"))
                caidas.append(sitio_entero)
    return caidas, pasan


def texto_informe(caidas, pasan, todo=False):
    lineas = ["=" * 76,
              "CENSO DE RUTAS (D.42): la unidad de la ruta es la celda",
              "=" * 76,
              "rutas publicadas y censadas : %d" % (len(caidas) + len(pasan)),
              "  pasan                     : %d" % len(pasan),
              "  CAEN                      : %d" % len(caidas)]
    formas = {}
    for p in pasan:
        clave = p["forma"].split("(")[0].split(":")[0].strip()
        formas[clave] = formas.get(clave, 0) + 1
    for clave in sorted(formas):
        lineas.append("      %-32s %d" % (clave, formas[clave]))

    for caida in caidas:
        lineas.append("")
        lineas.append("CAE  %s linea %d, %s"
                      % (caida["documento"], caida["linea"], caida["sitio"]))
        lineas.append("     ruta : %s" % caida["ruta"])
        lineas.append("     %s" % caida["motivo"])
        lineas.append("     celda: %s" % caida["celda"])

    if todo:
        lineas.append("")
        lineas.append("LO QUE PASA, UNA A UNA")
        for p in sorted(pasan, key=lambda x: (x["documento"], x["linea"])):
            lineas.append("  %-46s %s" % (p["ruta"][:46], p["forma"]))

    lineas.append("")
    if caidas:
        lineas.append("CENSO EN ROJO: %d ruta(s) publicadas como sede de una cifra no "
                      "sostienen nada." % len(caidas))
        lineas.append("Se arregla de una de estas tres formas, y solo de estas tres:")
        lineas.append("  1. regenerando el fichero, que es lo que casi siempre toca;")
        lineas.append("  2. escribiendo en la MISMA celda 'VACIA A PROPOSITO: <motivo>';")
        lineas.append("  3. si era un conjunto, escribiendola como 'PATRON: <glob>'.")
    else:
        lineas.append("CENSO VERDE: las %d rutas publicadas sostienen lo que dicen "
                      "sostener." % len(pasan))
    return "\n".join(lineas)


def main(argumentos=None):
    argumentos = list(argumentos if argumentos is not None else sys.argv[1:])
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8")
        except Exception:
            pass
    caidas, pasan = censar()
    print(texto_informe(caidas, pasan, todo="--todo" in argumentos))
    return 1 if caidas else 0


if __name__ == "__main__":
    sys.exit(main())
