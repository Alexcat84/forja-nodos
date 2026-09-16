# -*- coding: utf-8 -*-
"""Comprueba que las filas que la APERTURA pega como salida de .v29/cap07_estado.txt
coinciden CELDA A CELDA con el fichero del instrumento."""
import io, re
inst = io.open(".v29/cap07_estado.txt", encoding="utf-8").read().split("\n")
doc  = io.open("docs/loop/APERTURA_CIEGA.md", encoding="utf-8").read().split("\n")
FILA = re.compile(r"^\s*(GRAFO|BANDEJA)\s+(\d+-\d+)\s+([a-z0-9_]+)\s+(\d+)")
def filas(lineas):
    out = []
    for l in lineas:
        m = FILA.match(l)
        if m: out.append((m.group(1), m.group(2), m.group(3), m.group(4)))
    return out
a, b = filas(inst), filas(doc)
print("filas en el instrumento : %d" % len(a))
print("filas pegadas en el doc : %d" % len(b))
sa, sb = set(a), set(b)
print("en el doc y NO en el instrumento (celdas inventadas) : %d" % len(sb - sa))
for x in sorted(sb - sa): print("   INVENTADA ->", x)
print("en el instrumento y NO en el doc (filas que me deje) : %d" % len(sa - sb))
for x in sorted(sa - sb): print("   FALTA ->", x)
print()
print("VERDE" if not (sb - sa) else "ROJO: hay celdas en el doc que el instrumento no dice")
