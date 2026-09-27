# -*- coding: utf-8 -*-
"""Copia de .v64aud/contar_fidelidad.py con las rutas cambiadas a la 66. Cuenta mi tabla ciega de fidelidad
(.v66aud/fidelidad.tsv, clase T, P o D de duda) y la cruza con los pasos
de las fichas de cap_04 en la bandeja HOY (sin cambios desde 3174c73, .v66aud/desde_3174c73.txt):
comprueba que hay una fila por paso escrito, ni mas ni menos."""
import io, json, collections
filas = [l.rstrip('\n').split('\t') for l in io.open('.v66aud/fidelidad.tsv', encoding='utf-8')][1:]
por = collections.OrderedDict()
for f in filas: por.setdefault(f[0], []).append(f)
tot = collections.Counter(); dudas = 0
print('%-48s %5s %5s %3s %3s %5s' % ('candidato', 'ficha', 'filas', 'T', 'P', 'DUDA'))
for i, fs in por.items():
    n = len(json.load(io.open('cuarentena/grove_high_output/%s.json' % i, encoding='utf-8'))['pasos_accionables'])
    c = collections.Counter(f[2] for f in fs); d = c['D']
    print('%-48s %5d %5d %3d %3d %5d%s' % (i, n, len(fs), c['T'], c['P'], d, '' if n == len(fs) else '  DESCUADRE'))
    tot['ficha'] += n; tot['filas'] += len(fs); tot['T'] += c['T']; tot['P'] += c['P']; dudas += d
print('%-48s %5d %5d %3d %3d %5d' % ('total cap_04', tot['ficha'], tot['filas'], tot['T'], tot['P'], dudas))
print('PUENTE sobre pasos escritos: %d de %d = %.2f por ciento' % (tot['P'], tot['ficha'], 100.0 * tot['P'] / tot['ficha']))
print('si las %d DUDA cayesen a PUENTE: %d de %d = %.2f por ciento' % (dudas, tot['P'] + dudas, tot['ficha'], 100.0 * (tot['P'] + dudas) / tot['ficha']))
