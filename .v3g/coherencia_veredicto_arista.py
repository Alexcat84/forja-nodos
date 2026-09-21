# -*- coding: utf-8 -*-
"""Mide, sobre la sede, que clase lleva un par que ademas tiene arista.
No decide nada: cuenta lo que bitacora/VEREDICTOS.jsonl ya tiene escrito."""
import json, sys, collections
sys.stdout.reconfigure(encoding='utf-8')

V = [json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]
c = collections.Counter()
for v in V:
    a = v.get('arista')
    c[(v['veredicto'], bool(a) and a not in ('', None, 'ninguna'))] += 1

print("POBLACION: bitacora/VEREDICTOS.jsonl entero, %d lineas. NO es el reporte." % len(V))
print("           (la escribe la aduana con `insertar`; este frente no inserta)")
print()
print("  veredicto     con arista   sin arista")
for clase in ("CONTINUA", "SANO", "CORREGIDO"):
    print("  %-12s  %10d   %9d" % (clase, c[(clase, True)], c[(clase, False)]))
print()
print("  CONTINUA sin arista : %d" % c[("CONTINUA", False)])
print("  SANO     con arista : %d" % c[("SANO", True)])
print()
print("LO QUE EL INSTRUMENTO MIDIO: cuantas lineas de la sede llevan arista por clase.")
print("NO midio nada del reporte de este frente, que no escribe en esta sede.")
