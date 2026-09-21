# -*- coding: utf-8 -*-
"""Cuenta de pasos de las cinco fichas de la tanda, LISTA ORDENADA ENTERA."""
import json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
rutas = [l.strip() for l in open('.v48aud/02_candidatos_nuevos.out', encoding='utf-8') if l.strip()]
filas = []
for r in rutas:
    d = json.load(open(r, encoding='utf-8'))
    filas.append((len(d['pasos_accionables']), d['id'], len(d.get('atribuciones') or []),
                  len(d.get('nodos_previos') or []), len(d.get('nodos_siguientes') or [])))
print("PASOS POR FICHA, LISTA ORDENADA ENTERA de mas a menos:")
for n, i, a, pv, sg in sorted(filas, reverse=True):
    print("   %2d pasos   %2d atribuciones   previos %d  siguientes %d   %s" % (n, a, pv, sg, i))
print()
print("TOTAL de pasos escritos en la tanda: %d en %d fichas" % (sum(f[0] for f in filas), len(filas)))
