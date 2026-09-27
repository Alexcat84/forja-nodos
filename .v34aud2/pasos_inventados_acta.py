# -*- coding: utf-8 -*-
"""`PASOS INVENTADOS POR CAPITULO` (AUDITOR_FORJA.md 8), FIRMADO POR EL AUDITOR.

Los pasos los cuento YO del dataset, nodo a nodo (8.3 punto 1). El numerador PUENTE es
MI lectura de la apertura ciega sellada, seccion 5: 180 TRANSCRIPCION y 1 PUENTE, con
las dos lineas enfrentadas alli. El reporte publica 0.
"""
import io, json, math, re, sys
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

PUENTES_MIOS = {"practicar_franqueza_radical_jefe_propio": 1}
nodos = [json.loads(l) for l in io.open("dataset/nodos.jsonl", encoding="utf-8") if l.strip()]
tramo = [n for n in nodos
         if re.search(r"fuentes/scott_radical_candor/cap_09\.md", n.get("resumen_teorico") or "")]
tramo.sort(key=lambda n: int(re.search(r"l[ií]neas? (\d+)", n["resumen_teorico"]).group(1)))

pasos = sum(len(n["pasos_accionables"]) for n in tramo)
puente = sum(PUENTES_MIOS.get(n["id"], 0) for n in tramo)

def wilson(k, n, z=1.959963985):
    if n == 0:
        return 0.0, 100.0
    p, d = float(k) / n, 1 + z * z / n
    c = p + z * z / (2.0 * n)
    r = z * math.sqrt(p * (1 - p) / n + z * z / (4.0 * n * n))
    return 100 * max(0.0, (c - r) / d), 100 * min(1.0, (c + r) / d)

print("| capitulo | nodos | **pasos escritos** | **PUENTE, firmado por mi** | **PASOS INVENTADOS** | el reporte |")
print("|---|---:|---:|---:|---:|---:|")
print("| **`cap_09`** (lote 4, `scott_radical_candor`), el tramo de esta vuelta | %d | **%d** | **%d** | **%.2f por ciento** | 0,00 |"
      % (len(tramo), pasos, puente, 100.0 * puente / pasos))
print("| **total del tramo de esta vuelta** | %d | **%d** | **%d** | **%.2f por ciento** | 0,00 |"
      % (len(tramo), pasos, puente, 100.0 * puente / pasos))
print()
lo, hi = wilson(puente, pasos)
print("PASOS INVENTADOS de cap_09, firmado por el auditor: %d de %d = %.2f por ciento"
      % (puente, pasos, 100.0 * puente / pasos))
print("  banda de Wilson al 95 por ciento: %.2f a %.2f" % (lo, hi))
print("  tope de AUDITOR_FORJA.md 8.1     : 10 por ciento    -> NO HAY ESCALADA")
print("  el peor capitulo es el unico: la vuelta no toca ninguna otra unidad")
print()
print("MI RECUENTO DE PASOS, NODO A NODO (8.3 punto 1), contra los 181 del reporte:")
for n in tramo:
    m = re.search(r"l[ií]neas? (\d+)\s*a\s*(\d+)", n["resumen_teorico"])
    print("  L%-4s a L%-4s %-52s pasos=%2d  PUENTE=%d"
          % (m.group(1), m.group(2), n["id"], len(n["pasos_accionables"]), PUENTES_MIOS.get(n["id"], 0)))
print("  TOTAL: %d nodos, %d pasos" % (len(tramo), pasos))
