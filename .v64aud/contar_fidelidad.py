# -*- coding: utf-8 -*-
"""Cuenta mi tabla ciega de fidelidad (.v64aud/fidelidad.tsv) y la cruza con los pasos
de las fichas TAL COMO ESTABAN AL ABRIR LA VUELTA 64 (commit 067c9df, copiadas en
.v64aud/antes_<id>.json): comprueba que hay una fila por paso escrito, ni mas ni menos."""
import io, json, collections
filas = [l.rstrip('\n').split('\t') for l in io.open('.v64aud/fidelidad.tsv', encoding='utf-8')][1:]
por = collections.OrderedDict()
for f in filas: por.setdefault(f[0], []).append(f)
tot = collections.Counter(); dudas = 0
print('%-48s %5s %5s %3s %3s %5s' % ('candidato', 'ficha', 'filas', 'T', 'P', 'DUDA'))
for i, fs in por.items():
    n = len(json.load(io.open('.v64aud/antes_%s.json' % i, encoding='utf-8'))['pasos_accionables'])
    c = collections.Counter(f[2] for f in fs); d = sum('DUDA' in f[4] for f in fs)
    print('%-48s %5d %5d %3d %3d %5d%s' % (i, n, len(fs), c['T'], c['P'], d, '' if n == len(fs) else '  DESCUADRE'))
    tot['ficha'] += n; tot['filas'] += len(fs); tot['T'] += c['T']; tot['P'] += c['P']; dudas += d
print('%-48s %5d %5d %3d %3d %5d' % ('total cap_03, seis de d005', tot['ficha'], tot['filas'], tot['T'], tot['P'], dudas))
print('PUENTE sobre pasos escritos: %d de %d = %.2f por ciento' % (tot['P'], tot['ficha'], 100.0 * tot['P'] / tot['ficha']))
print('si las %d DUDA cayesen a PUENTE: %d de %d = %.2f por ciento' % (dudas, tot['P'] + dudas, tot['ficha'], 100.0 * (tot['P'] + dudas) / tot['ficha']))
