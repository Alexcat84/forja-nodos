# -*- coding: utf-8 -*-
"""MI PROPIO D.41 PARA LA APERTURA. El censo de rutas y el tallado no leen
docs/loop/APERTURA_CIEGA.md (medido en la seccion 1.2), asi que la compruebo yo.

Toma toda linea del documento que este dentro de un bloque indentado de salida
y que PAREZCA una fila de instrumento (lleva un id de nodo o una cifra con
etiqueta), y exige que su texto exacto viva en algun fichero de .v29/ o sea
una cita del libro en fuentes/.
"""
import io, os, glob, re

doc = io.open("docs/loop/APERTURA_CIEGA.md", encoding="utf-8").read().split("\n")
corpus = ""
for f in sorted(glob.glob(".v29/*.txt")):
    corpus += io.open(f, encoding="utf-8", errors="replace").read() + "\n"

# Filas que se presentan como salida: empiezan con 4+ espacios y contienen
# un id de nodo (minusculas con guion bajo, 3+ tramos) o "linea NNN".
SOSPECHOSA = re.compile(r"^\s{4,}(linea\s+\d+|\d{3}\s+(SANO|CONTINUA))\b")
fallos = []
mirados = 0
for n, l in enumerate(doc, 1):
    if not SOSPECHOSA.match(l):
        continue
    mirados += 1
    if l.strip() not in corpus:
        fallos.append((n, l.strip()))

print("filas de bitacora presentadas como salida : %d" % mirados)
print("las que NO viven literales en .v29/       : %d" % len(fallos))
for n, l in fallos:
    print("   linea %d del doc NO CUADRA:" % n)
    print("      %s" % l[:150])
print()
print("VERDE: toda fila pegada vive literal en su instrumento" if not fallos
      else "ROJO: hay filas pegadas que su instrumento no dice asi")
