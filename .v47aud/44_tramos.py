# -*- coding: utf-8 -*-
"""Los 44 tramos de la frontera de cap_04, ordenados por palabras, con su cuenta de
nodos al lado. Sirve para comprobar DOS frases del reporte de la vuelta 47 (II.3.b)."""
import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
lines = open("docs/loop/REPORTE.md", encoding="utf-8").read().split("\n")
filas = []
i = 43935 - 1
while not lines[i].startswith("| | **8846**"):
    m = re.match(r"^\| `L(\d+) a L(\d+)` \| (\d+) \| \*\*(\d+)\*\* \| (P\d+)", lines[i])
    filas.append((m.group(5), int(m.group(3)), int(m.group(4))))
    i += 1
print("LOS 44 TRAMOS ORDENADOS POR PALABRAS, LISTA ENTERA, de mas a menos:")
for p, w, n in sorted(filas, key=lambda f: -f[1]):
    print("   %-5s %5d palabras   %d nodo(s)" % (p, w, n))
cero = [f for f in filas if f[2] == 0]; con = [f for f in filas if f[2] > 0]
print()
print("tramos con CERO nodos : %2d   palabras: media %.1f  minimo %d  maximo %d (%s)"
      % (len(cero), sum(f[1] for f in cero)/len(cero), min(f[1] for f in cero),
         max(f[1] for f in cero), max(cero, key=lambda f: f[1])[0]))
print("tramos CON nodo       : %2d   palabras: media %.1f  minimo %d  maximo %d (%s)"
      % (len(con), sum(f[1] for f in con)/len(con), min(f[1] for f in con),
         max(f[1] for f in con), max(con, key=lambda f: f[1])[0]))
TANDA47 = ["P21", "P24", "P27", "P29", "P30", "P32", "P33"]
print()
print("LOS TRAMOS DE LA TANDA DE LA VUELTA 47, ORDENADOS, LISTA ENTERA:")
for p, w, n in sorted([f for f in filas if f[0] in TANDA47], key=lambda f: -f[1]):
    print("   %-5s %5d palabras   %d nodo(s)" % (p, w, n))
