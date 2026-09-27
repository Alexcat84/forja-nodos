# -*- coding: utf-8 -*-
"""LAS CITAS DE LINEA DE LA VUELTA 60, COMPROBADAS UNA A UNA CONTRA EL LIBRO.

Es el remedio que la ACTA 58 58.3 dejo escrito: cuando se publica una linea del
libro como prueba, el numero sale de un grep -n real y no de la cuenta. La
vuelta 59 fallo 29 de 43. Este script mide lo mismo sobre las filas de hoy.

MIDE DOS COSAS APARTE, y se dicen aparte a proposito:

  EL NUMERO  : que el prefijo N: de la celda pegada sea la linea donde de verdad
               empieza el tramo. Esto es lo que el remedio pedia.
  EL TEXTO   : que el fragmento pegado sea prefijo de esa linea del fichero. Una
               diferencia AQUI no acusa a la mano si el propio fichero de salida
               del instrumento trae ya esa diferencia, asi que cuando el texto
               no cuadra se comprueba contra .v60ext/frontera_v60.txt y se dice
               de quien es.
"""

import io
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
SALIDA = os.path.join(RAIZ, ".v60ext", "frontera_v60.txt")
CABECERA_DE_LA_VUELTA = "# VUELTA 60, lote 7"


def normaliza(s):
    for viejo, nuevo in ((u"’", "'"), (u"‘", "'"),
                         (u"“", '"'), (u"”", '"')):
        s = s.replace(viejo, nuevo)
    return s


def main():
    texto = io.open(REPORTE, encoding="utf-8").read().split("\n")
    arranque = max(i for i, l in enumerate(texto)
                   if l.startswith(CABECERA_DE_LA_VUELTA))
    del_instrumento = set(l for l in io.open(SALIDA, encoding="utf-8").read().split("\n")
                          if l.startswith("| "))

    libros = {}
    for cap in ("cap_17", "cap_18"):
        libros[cap] = io.open(
            os.path.join(RAIZ, "fuentes", "grove_high_output", cap + ".md"),
            encoding="utf-8").read().split("\n")

    cap = None
    comprobadas = 0
    numero_mal = []
    texto_mal = []
    for linea in texto[arranque:]:
        encabezado = re.match(r"^\| tramo de (cap_\d+) \|", linea)
        if encabezado:
            cap = encabezado.group(1)
            continue
        if not cap:
            continue
        fila = re.match(r"^\| `L(\d+) a L(\d+)` \|.*\| `(\d+):(.*)` \|\s*$", linea)
        if not fila:
            continue
        comprobadas += 1
        arranca_en = int(fila.group(1))
        prefijo = int(fila.group(3))
        fragmento = fila.group(4)
        real = libros[cap][prefijo - 1] if 0 < prefijo <= len(libros[cap]) else "<<fuera de rango>>"

        if prefijo != arranca_en:
            numero_mal.append((cap, arranca_en, prefijo))
        if not normaliza(real).startswith(normaliza(fragmento)[:60]):
            de_quien = ("DEL INSTRUMENTO" if linea in del_instrumento
                        else "DE LA MANO")
            texto_mal.append((cap, arranca_en, de_quien, fragmento[:40], real[:40]))

    print("filas con cita comprobadas                     : %d" % comprobadas)
    print("filas cuyo NUMERO DE LINEA no cuadra            : %d" % len(numero_mal))
    for (cap, a, p) in numero_mal:
        print("   %s L%d: pegado %d" % (cap, a, p))
    print("filas cuyo TEXTO no cuadra                      : %d" % len(texto_mal))
    for (cap, a, de_quien, pegado, real) in texto_mal:
        print("   %s L%d  %s" % (cap, a, de_quien))
    de_la_mano = [f for f in texto_mal if f[2] == "DE LA MANO"]
    print("   de esas, TECLEADAS POR LA MANO               : %d" % len(de_la_mano))
    print("")
    print("EL REMEDIO DE LA ACTA 58 58.3 SE MIDE EN LA SEGUNDA LINEA:")
    print("  %d de %d numeros de linea aciertan."
          % (comprobadas - len(numero_mal), comprobadas))


if __name__ == "__main__":
    main()
