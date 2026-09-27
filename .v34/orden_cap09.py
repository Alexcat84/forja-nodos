# -*- coding: utf-8 -*-
"""cap_09 EN EL ORDEN DEL LIBRO: la linea que cada candidato cita de cap_09.md.
D.36 manda entrar por el orden que abre la lectura, y el orden del libro es el que
esta casa usa: el primero que entra cambia lo que el segundo mide."""
import glob, json, io, re, os
RX2 = re.compile(r"lineas?\s+(\d+)")
filas = []
for f in sorted(glob.glob("cuarentena/scott_radical_candor/*.json")
                + glob.glob("cuarentena/_insertados/scott_radical_candor/*.json")):
    d = json.load(io.open(f, encoding="utf-8"))
    rt = d.get("resumen_teorico") or ""
    if "cap_09.md" not in rt:
        continue
    i = rt.find("cap_09.md")
    m = RX2.search(rt[i:i + 140])
    filas.append((int(m.group(1)) if m else 99999, os.path.basename(f)[:-5],
                  len(d.get("pasos_accionables") or [])))
filas.sort()
print("cap_09 EN EL ORDEN DEL LIBRO (linea que cada candidato cita de cap_09.md)")
print("%-4s %-4s %-58s %s" % ("#", "L", "id", "pasos"))
for k, (ln, nid, np) in enumerate(filas, 1):
    print("%-4d %-4s %-58s %d" % (k, ln, nid, np))
print("")
print("total cap_09 en bandeja: %d" % len(filas))
print("pasos totales          : %d" % sum(f[2] for f in filas))
