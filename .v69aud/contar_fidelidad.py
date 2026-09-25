# -*- coding: utf-8 -*-
"""Fase ciega de la 69 (copia de .v68aud/contar_fidelidad.py, con R7 y SIN escribir .v68aud/fidelidad.tsv): mi
lectura sellada de la 68 (.v68aud/fidelidad_fuente.txt, T, P o D con su linea) contra los pasos de las fichas de la
bandeja HOY, una fila por paso ni mas ni menos, y por capitulo (8.2) las marcas con su suma. Las D las adjudique T en
la ACTA 67 67.4.a; se imprime la cuenta sellada y la adjudicada. Solo lee."""
import io, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
los20 = io.open('.v68aud/los20.txt', encoding='utf-8').read().split()
cap = dict((i, 'cap_05' if n < 12 else 'cap_06') for n, i in enumerate(los20))
filas = [l.rstrip('\n').split('|', 4) for l in io.open('.v68aud/fidelidad_fuente.txt', encoding='utf-8') if l.strip()]
por = collections.OrderedDict((i, []) for i in los20)
for f in filas: por[f[0]].append(f)
tot = collections.defaultdict(collections.Counter); desc = []
for i, fs in por.items():
    n = len(json.load(io.open('cuarentena/grove_high_output/%s.json' % i, encoding='utf-8'))['pasos_accionables'])
    if n != len(fs) or [int(f[1]) for f in fs] != list(range(1, len(fs) + 1)): desc.append(i)
    t = tot[cap[i]]; t['cand'] += 1; t['ficha'] += n
    for f in fs: t[f[2]] += 1
print('fichas con descuadre entre sus pasos de hoy y mis filas: %d %s' % (len(desc), desc))
for k in ('cap_05', 'cap_06'):
    t = tot[k]; m = dict((c, t[c]) for c in ('T', 'P', 'D'))
    print('%s: candidatos %d | pasos en ficha %d | mis marcas selladas: %s | suma: %d | PUENTE %d de %d = %.2f por ciento | con las D adjudicadas T (ACTA 67 67.4.a): T %d, P %d, suma %d' % (
        k, t['cand'], t['ficha'], m, sum(m.values()), t['P'], t['ficha'], 100.0 * t['P'] / t['ficha'], t['T'] + t['D'], t['P'], t['T'] + t['D'] + t['P']))
