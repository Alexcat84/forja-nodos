# -*- coding: utf-8 -*-
"""Segunda comprobacion: los vecinos que la APERTURA pega contra .v29/barrido_v29.txt,
y las lineas de bitacora que pega contra .v29/bitacora_v29.txt."""
import io, re
doc = io.open("docs/loop/APERTURA_CIEGA.md", encoding="utf-8").read()

# --- vecinos: nombre del vecino mas la senial que lo levanta ---
INST = re.compile(r"^\s*-\s+([a-z0-9_]+)\s+(GRAFO|BANDEJA)\s+\[([^\]]+)\]", re.M)
bar = io.open(".v29/barrido_v29.txt", encoding="utf-8").read()
a = set((m.group(1), m.group(3).strip()) for m in INST.finditer(bar))
b = set((m.group(1), m.group(3).strip()) for m in INST.finditer(doc))
print("vecinos en el instrumento : %d" % len(a))
print("vecinos pegados en el doc : %d" % len(b))
print("INVENTADOS en el doc      : %d" % len(b - a))
for x in sorted(b - a): print("   INVENTADO ->", x)
print("que me deje sin pegar     : %d" % len(a - b))
for x in sorted(a - b): print("   FALTA ->", x)
print()

# --- lineas de bitacora: numero, veredicto, candidato ---
LIN = re.compile(r"^\s*(?:linea\s+)?(2[0-9]{2})\s+(SANO|CONTINUA|REPITE|CORREGIDO)\s+([a-z0-9_]+)", re.M)
bit = io.open(".v29/bitacora_v29.txt", encoding="utf-8").read()
c = set((m.group(1), m.group(2), m.group(3)) for m in LIN.finditer(bit))
d = set((m.group(1), m.group(2), m.group(3)) for m in LIN.finditer(doc))
print("lineas de bitacora en el instrumento : %d" % len(c))
print("lineas pegadas en el doc             : %d" % len(d))
print("INVENTADAS en el doc                 : %d" % len(d - c))
for x in sorted(d - c): print("   INVENTADA ->", x)
print()
print("VERDE" if not (b - a) and not (d - c) else "ROJO")
