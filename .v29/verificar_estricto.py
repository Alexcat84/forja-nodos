# -*- coding: utf-8 -*-
"""MI PROPIO D.41 PARA LA APERTURA, version ESTRICTA.

Toda linea del documento que este dentro de un bloque de salida (indentada 6 o
mas espacios) y que contenga un id de nodo de esta casa tiene que vivir LITERAL,
sin contar el espaciado, en algun fichero de `.v29/` o en el `resumen_teorico`
de un nodo del dataset. Si no vive, la he tecleado yo, y una celda tecleada es
la especie que la ACTA 24 conto con 14.
"""
import io, glob, re, json

doc = io.open("docs/loop/APERTURA_CIEGA.md", encoding="utf-8").read().split("\n")

crudo = ""
for f in sorted(glob.glob(".v29/*.txt")):
    crudo += io.open(f, encoding="utf-8", errors="replace").read() + "\n"
for l in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    crudo += (json.loads(l).get("resumen_teorico") or "") + "\n"
corpus = " ".join(crudo.split())

ID = re.compile(r"\b[a-z]+(?:_[a-z0-9]+){3,}\b")
fallos, mirados = [], 0
for n, l in enumerate(doc, 1):
    if not l.startswith("      "):
        continue
    if not ID.search(l):
        continue
    if l.strip().startswith(("#", "$", "|", ">", "*", "(")):
        continue
    mirados += 1
    if " ".join(l.split()) not in corpus:
        fallos.append((n, l.strip()))

print("lineas de salida con id de nodo : %d" % mirados)
print("las que NO viven literales      : %d" % len(fallos))
for n, l in fallos:
    print("   linea %d: %s" % (n, l[:160]))
print()
print("VERDE: ninguna linea de salida esta tecleada" if not fallos else "ROJO")
