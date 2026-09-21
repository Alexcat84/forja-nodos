# -*- coding: utf-8 -*-
"""LAS CITAS DE NODO CON LAS QUE cap_18 SOSTIENE SU CERO, COMPROBADAS UNA A UNA.

La tabla de cap_18 de la vuelta 60 adjudica 0 nodos sobre 25 items, y lo hace
nombrando, item por item, el nodo que ya tiene ese procedimiento. Eso es una
busqueda NEGATIVA sostenida por citas POSITIVAS, y AUDITOR_FORJA.md 1.1 dice que
una busqueda negativa no se puede citar: hay que comprobar las positivas.

La poblacion es la de D.38.4: dataset/nodos.jsonl MAS todo lo que espera en
cuarentena/<libro>/, descartando _insertados y _derivadas, mas el candidato que
la vuelta aparto a .v60ext/pendientes/.

Para no confundir una palabra castellana larga con un id, solo cuentan como cita
los identificadores que llevan al menos DOS guiones bajos, que es la forma de un
id de esta casa (REGLAS_DE_ID.md).
"""

import glob
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
CABECERA_DE_LA_VUELTA = "# VUELTA 60, lote 7"


def poblacion():
    donde = {}
    for linea in io.open(os.path.join(RAIZ, "dataset", "nodos.jsonl"),
                         encoding="utf-8"):
        linea = linea.strip()
        if linea:
            donde.setdefault(json.loads(linea)["id"], "GRAFO")
    for ruta in glob.glob(os.path.join(RAIZ, "cuarentena", "*", "*.json")):
        if "_insertados" in ruta or "_derivadas" in ruta:
            continue
        ficha = json.load(io.open(ruta, encoding="utf-8"))
        donde.setdefault(ficha["id"],
                         "BANDEJA:" + os.path.basename(os.path.dirname(ruta)))
    for ruta in glob.glob(os.path.join(RAIZ, ".v60ext", "pendientes", "*.json")):
        ficha = json.load(io.open(ruta, encoding="utf-8"))
        donde.setdefault(ficha["id"], "APARTADO")
    return donde


def main():
    donde = poblacion()
    claves_de_libro = set(
        os.path.basename(d) for d in glob.glob(os.path.join(RAIZ, "fuentes", "*"))
        if os.path.isdir(d))
    print("poblacion de D.38.4 (grafo mas bandejas mas el apartado): %d" % len(donde))
    print("claves de libro excluidas del barrido de ids           : %d" % len(claves_de_libro))

    texto = io.open(REPORTE, encoding="utf-8").read().split("\n")
    arranque = max(i for i, l in enumerate(texto)
                   if l.startswith(CABECERA_DE_LA_VUELTA))
    cap = None
    citas = {}
    for linea in texto[arranque:]:
        encabezado = re.match(r"^\| tramo de (cap_\d+) \|", linea)
        if encabezado:
            cap = encabezado.group(1)
            continue
        if cap != "cap_18":
            continue
        fila = re.match(r"^\| `L(\d+) a L\d+` \|", linea)
        if not fila:
            continue
        item = re.search(r"\| (P\d+)", linea)
        etiqueta = item.group(1) if item else ("L" + fila.group(1))
        for posible in re.findall(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+){2,}\b", linea):
            if posible in claves_de_libro:
                continue          # 'grove_high_output' es la clave del libro, no un id
            citas.setdefault(posible, etiqueta)

    print("")
    print("=== ids citados como prueba en la tabla de cap_18 ===")
    faltan = []
    for nid in sorted(citas):
        sitio = donde.get(nid)
        if sitio is None:
            faltan.append(nid)
            sitio = "NO EXISTE"
        print("  %-56s %-28s %s" % (nid, sitio, citas[nid]))
    print("")
    print("citas comprobadas                        : %d" % len(citas))
    print("CITAS QUE NO EXISTEN EN NINGUNA POBLACION: %d" % len(faltan))
    for nid in faltan:
        print("   %s" % nid)


if __name__ == "__main__":
    main()
