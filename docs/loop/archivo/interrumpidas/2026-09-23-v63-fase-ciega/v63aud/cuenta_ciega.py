# -*- coding: utf-8 -*-
"""Cuenta la tabla de fidelidad ciega de la vuelta 63 y la cruza contra HEAD.

Ninguna cifra de la apertura sale de contar a mano: sale de aqui.
    python .v63aud/cuenta_ciega.py
"""
import collections
import io
import json
import subprocess

filas = [l.rstrip("\n").split("\t")
         for l in io.open(".v63aud/fidelidad_ciega.tsv", encoding="utf-8") if l.strip()]
por_cand = collections.Counter(f[1] for f in filas)
descuadres = 0
for cand, n in sorted(por_cand.items()):
    crudo = subprocess.run(
        ["git", "show", "HEAD:cuarentena/grove_high_output/%s.json" % cand],
        capture_output=True).stdout.decode("utf-8")
    pasos = len(json.loads(crudo)["pasos_accionables"])
    if pasos != n:
        descuadres += 1
        print("DESCUADRE %s tabla %d HEAD %d" % (cand, n, pasos))
print("candidatos en la tabla : %d" % len(por_cand))
print("descuadres contra HEAD : %d" % descuadres)
print()
print("capitulo  pasos  TRANSCRIPCION  PUENTE  PUENTE_PARCIAL")
for cap in sorted(set(f[0] for f in filas)):
    c = collections.Counter(f[3] for f in filas if f[0] == cap)
    total = sum(c.values())
    print("%-8s  %5d  %13d  %6d  %14d" % (cap, total, c["TRANSCRIPCION"],
                                         c["PUENTE"], c["PUENTE_PARCIAL"]))
c = collections.Counter(f[3] for f in filas)
print("%-8s  %5d  %13d  %6d  %14d" % ("total", sum(c.values()), c["TRANSCRIPCION"],
                                     c["PUENTE"], c["PUENTE_PARCIAL"]))
