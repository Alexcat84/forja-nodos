# -*- coding: utf-8 -*-
"""RECOMPONGO LA FRONTERA DE LA VUELTA 60 FILA A FILA, CONTRA EL FICHERO FUENTE.

AUDITOR_FORJA.md 1.1: las cifras se recomputan DESDE EL ARCHIVO con mis propios
comandos. No leo la salida del instrumento del extractor: leo su TABLA del
REPORTE.md, saco de cada fila el tramo y las palabras que declara, cuento yo
esas palabras en el fichero fuente, y digo cuantas filas no me salen.

Comprueba ademas las tres cosas que la frontera promete: que ninguna linea con
contenido queda sin cubrir, que ningun tramo solapa con otro, y que la suma de
las filas es igual al cuerpo medido aparte.
"""

import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
CABECERA_DE_LA_VUELTA = "# VUELTA 60, lote 7"


def tramos_del_reporte():
    """(tramo_a, tramo_b, palabras_declaradas) por capitulo, leidos de su tabla."""
    texto = io.open(REPORTE, encoding="utf-8").read().split("\n")
    arranque = max(i for i, l in enumerate(texto)
                   if l.startswith(CABECERA_DE_LA_VUELTA))
    cap = None
    filas = {}
    nodos = {}
    for linea in texto[arranque:]:
        encabezado = re.match(r"^\| tramo de (cap_\d+) \|", linea)
        if encabezado:
            cap = encabezado.group(1)
            filas.setdefault(cap, [])
            nodos.setdefault(cap, 0)
            continue
        if not cap:
            continue
        fila = re.match(r"^\| `L(\d+) a L(\d+)` \| (\d+) \| \*\*(\d+)\*\* \|", linea)
        if fila:
            filas[cap].append((int(fila.group(1)), int(fila.group(2)),
                               int(fila.group(3))))
            nodos[cap] += int(fila.group(4))
    return filas, nodos


def palabras(lineas):
    return sum(len(l.split()) for l in lineas)


def analiza(ruta, filas, etiqueta, nodos):
    texto = io.open(ruta, encoding="utf-8").read().split("\n")
    # la cabecera del fichero fuente acaba en el SEGUNDO guion triple
    guiones = [i + 1 for i, l in enumerate(texto) if l.strip() == "---"]
    fin_cabecera = guiones[1]

    cubiertas = {}
    suma = 0
    no_me_salen = []
    for (a, b, declaradas) in filas:
        mias = palabras(texto[a - 1:b])
        suma += mias
        if mias != declaradas:
            no_me_salen.append((a, b, declaradas, mias))
        for L in range(a, b + 1):
            cubiertas[L] = cubiertas.get(L, 0) + 1

    con_contenido = [i + 1 for i, l in enumerate(texto)
                     if i + 1 > fin_cabecera and l.strip()]
    sin_cubrir = [L for L in con_contenido if L not in cubiertas]
    solapes = sorted(L for L, veces in cubiertas.items() if veces > 1)
    cuerpo = palabras([l for i, l in enumerate(texto) if i + 1 > fin_cabecera])

    print("=" * 70)
    print("%s  cabecera acaba en %d" % (etiqueta, fin_cabecera))
    print("filas             : %d" % len(filas))
    print("lineas contenido  : %d" % len(con_contenido))
    print("sin cubrir        : %d %s" % (len(sin_cubrir), sin_cubrir))
    print("solapes           : %d %s" % (len(solapes), solapes))
    print("suma de mis filas : %d" % suma)
    print("cuerpo aparte     : %d" % cuerpo)
    print("fichero entero    : %d" % palabras(texto))
    print("IGUALES           : %s" % (suma == cuerpo))
    print("nodos que declara : %d" % nodos)
    print("filas que NO me salen: %d" % len(no_me_salen))
    for (a, b, declaradas, mias) in no_me_salen:
        print("   L%d a L%d  reporte=%d  mio=%d" % (a, b, declaradas, mias))


def main():
    filas, nodos = tramos_del_reporte()
    for cap in ("cap_17", "cap_18"):
        analiza(os.path.join(RAIZ, "fuentes", "grove_high_output", cap + ".md"),
                filas[cap], cap, nodos[cap])


if __name__ == "__main__":
    main()
