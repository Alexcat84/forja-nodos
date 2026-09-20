# -*- coding: utf-8 -*-
"""EL COSTE DE LA CORRIDA DE HOY, acotada por su propia linea de arranque.
CORRECCION DE MI PRIMER CORTE, escrita aqui para que se vea: 'MODO_INSERCION=
cuarentena' NO acota el regimen ligero de D.58. Hay 33 turnos en cuarentena del
10 y el 11 sep, anteriores a D.58, y acotar por la variable me daba 35 turnos y
una media falsa. Lo que acota esta corrida es su linea de arranque."""
import re
ARRANQUE = "2026-09-20 12:08:04"
turnos, modo = [], "?"
for l in open("docs/loop/loop.log", encoding="utf-8", errors="replace"):
    m = re.search(r"arranque:.*MODO_INSERCION=(\w+)", l)
    if m: modo = m.group(1)
    m = re.match(r"\[([\d\-: ]+)\]\s+(.*?) listo \(USD ([\d.]+)\), (\d+)s", l)
    if m: turnos.append((m.group(1), m.group(2), modo, float(m.group(3)), int(m.group(4))))
print("$ python .v55aud/coste_corrida.py  (fuente: docs/loop/loop.log)")
print("  linea de arranque que acota la corrida : [%s] MODO_INSERCION=cuarentena" % ARRANQUE)
hoy = [t for t in turnos if t[0] >= ARRANQUE]
print("  TURNOS CERRADOS DE ESTA CORRIDA, celda a celda y sin media: %d" % len(hoy))
for t in hoy: print("    %s  %-14s %-11s %9.4f USD  %6d s" % t)
print("  suma USD de los turnos cerrados de esta corrida : %.4f" % sum(t[3] for t in hoy))
print("    (es una SUMA, no una media: no divido dos celdas)")
print()
ei = [t for t in turnos if t[1] == "extractor" and t[2] == "insertar"]
media = sum(t[3] for t in ei) / len(ei)
print("  LA VARA: media USD/turno de extractor en insertar : %.2f USD" % media)
print("    numerador   %.2f  suma de USD de esos turnos" % sum(t[3] for t in ei))
print("    denominador %d  turnos de extractor en insertar" % len(ei))
print("    el mas barato %.4f   el mas caro %.4f" % (min(t[3] for t in ei), max(t[3] for t in ei)))
ex = [t for t in hoy if t[1] == "extractor"][0][3]
print("  EL TURNO DE EXTRACTOR DE ESTA CORRIDA             : %.4f USD" % ex)
print("  CAIDA contra esa vara                             : %.1f por ciento" % (100.0 * (ex - media) / media))
print("    numerador   %.4f  USD del turno de extractor de esta corrida menos la vara" % (ex - media))
print("    denominador %.2f  USD de la vara" % media)
print("  CONTRA EL OBJETIVO ESCRITO DE 5 USD               : %.2f veces el objetivo" % (ex / 5.0))
print("    numerador   %.4f  USD del turno de extractor de esta corrida" % ex)
print("    denominador 5  USD del objetivo escrito en el encargo de la 54")
print("  CONTRA EL DISPARADOR ESCRITO DE 8 USD             : %d de los %d turnos cerrados lo pasan" %
      (sum(1 for t in hoy if t[3] > 8.0), len(hoy)))
