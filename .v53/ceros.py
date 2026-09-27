# -*- coding: utf-8 -*-
"""CUENTA LOS TRAMOS DE CERO DE LA FRONTERA DE OO.2, RELEYENDO LA TABLA QUE LOS IMPRIMIO.

No teclea ninguna de las tres cifras: abre .v53/frontera_tres.txt, casa cada fila de tabla con
su expresion regular y cuenta. Es el remedio de EXTRACTOR.md 5: la tabla se cuenta de su
fichero, y si no hay fichero que contar la cifra no se publica.
"""
import io
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

src = io.open(".v53/frontera_tres.txt", encoding="utf-8").read().split("\n")
fila = re.compile(r"^\| `(L\d+ a L\d+)` \| (\d+) \| \*\*(\d+)\*\* \| (P\d+)\s+(.*?) \| `")
cap = None
d = {}
for t in src:
    m = re.match(r"^2\. LA TABLA DE (cap_\d+)", t)
    if m:
        cap = m.group(1)
        d[cap] = []
    m = fila.match(t)
    if m and cap:
        d[cap].append((m.group(1), int(m.group(2)), int(m.group(3)), m.group(4), m.group(5)))

print("    de la tabla de OO.2, releida hoy fila a fila del mismo fichero que la imprimio")
print("    %-8s %8s %8s %8s  %s"
      % ("unidad", "tramos", "con nodo", "de cero", "rotulos y enlaces sin cuerpo"))
T = CN = CZ = 0
for c in sorted(d):
    filas = d[c]
    cn = sum(1 for f in filas if f[2])
    cz = len(filas) - cn
    rot = [f[3] for f in filas if "sin cuerpo que extraer" in f[4]]
    T += len(filas)
    CN += cn
    CZ += cz
    print("    %-8s %8d %8d %8d  %s" % (c, len(filas), cn, cz, ", ".join(rot) if rot else "ninguno"))
print("    %-8s %8d %8d %8d" % ("TOTAL", T, CN, CZ))
print("")
print("    tramos que dan nodo, y todos dan UNO  : %d" % CN)
print("    nodos previstos en las tres unidades  : %d" % sum(f[2] for c in d for f in d[c]))
print("    tramos de cero, cada uno con su motivo: %d" % CZ)
