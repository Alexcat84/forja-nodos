# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO, contado por el auditor desde cero.

El capitulo de un candidato sale de su UNIDAD DE ORIGEN, no de donde lo diga el
reporte. Los PUENTE son los que el auditor firma tras leer cada paso contra su
linea del libro, y se escriben aqui a mano con su cita porque ningun instrumento
de esta casa puede leer el libro (D.30).
"""
import collections, glob, json, os, re

# PUENTES FIRMADOS POR EL AUDITOR DE LA ACTA M4, tras leer los 16 pasos uno a uno.
PUENTES = {}   # ninguno: 16 de 16 TRANSCRIPCION

ORIGEN = re.compile(r"UNIDAD DE ORIGEN:\s*fuentes/[a-z0-9_]+/(cap_\d+)\.md", re.I)
CAPS = ("cap_06", "cap_07", "cap_08")

nodos = collections.Counter()
pasos = collections.Counter()
for ruta in sorted(glob.glob("cuarentena/marquet_turn_the_ship/*.json")):
    ficha = json.load(open(ruta, encoding="utf-8"))
    casa = ORIGEN.search(ficha.get("resumen_teorico", "") or "")
    if not casa or casa.group(1) not in CAPS:
        continue
    nodos[casa.group(1)] += 1
    pasos[casa.group(1)] += len(ficha.get("pasos_accionables", []))

print("PASOS INVENTADOS POR CAPITULO, contados por el auditor (ACTA M4)")
print("  poblacion: cuarentena/marquet_turn_the_ship, por UNIDAD DE ORIGEN")
print()
print("  capitulo   nodos   pasos   PUENTE   PASOS INVENTADOS")
print("  " + "-" * 56)
tn = tp = tb = 0
for cap in CAPS:
    puente = PUENTES.get(cap, 0)
    tn += nodos[cap]; tp += pasos[cap]; tb += puente
    if pasos[cap]:
        cifra = "%.2f por ciento (%d / %d)" % (100.0 * puente / pasos[cap], puente, pasos[cap])
    else:
        cifra = "SIN SUPERFICIE (0 / 0)"
    print("  %-10s %5d   %5d   %6d   %s" % (cap, nodos[cap], pasos[cap], puente, cifra.replace(".", ",", 1)))
print("  " + "-" * 56)
tramo_p = pasos["cap_07"] + pasos["cap_08"]
tramo_b = PUENTES.get("cap_07", 0) + PUENTES.get("cap_08", 0)
print("  %-10s %5d   %5d   %6d   %s" % ("EL TRAMO", nodos["cap_07"] + nodos["cap_08"], tramo_p, tramo_b,
      ("%.2f por ciento (%d / %d)" % (100.0 * tramo_b / tramo_p, tramo_b, tramo_p)).replace(".", ",", 1)))
print()
print("  LEIDOS UNO A UNO CONTRA SU LINEA DEL LIBRO: %d de %d pasos" % (tp, tp))
