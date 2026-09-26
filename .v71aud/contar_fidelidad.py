# -*- coding: utf-8 -*-
"""Copia de .v68aud/contar_fidelidad.py con las rutas cambiadas a la 71, el capitulo leido de .v70aud/normal/bandeja_grove.txt
(seis capitulos, una fila de total por capitulo, 8.2) y la suma de cada reparto por clases (R7). Arma .v71aud/fidelidad.tsv
desde .v71aud/fidelidad_fuente.txt (mi lectura ciega, clase T, P o D de duda, con su linea del capitulo) y la cruza con los
pasos de las fichas de la bandeja HOY: comprueba que hay una fila por paso escrito, ni mas ni menos. No escribe nada fuera
de .v71aud/."""
import io, json, collections
los20 = io.open('.v71aud/los20.txt', encoding='utf-8').read().split()
cap = dict((l.split()[1], l.split()[0]) for l in io.open('.v70aud/normal/bandeja_grove.txt', encoding='utf-8') if l.strip())
filas = [l.rstrip('\n').split('|', 4) for l in io.open('.v71aud/fidelidad_fuente.txt', encoding='utf-8') if l.strip()]
with io.open('.v71aud/fidelidad.tsv', 'w', encoding='utf-8', newline='\n') as f:
    f.write('id\tpaso\tclase\tcapitulo\tlinea\tlectura\n')
    for i, p, c, L, t in filas: f.write('\t'.join([i, p, c, cap[i], L, t]) + '\n')
por = collections.OrderedDict((i, []) for i in los20)
for f in filas: por[f[0]].append(f)
tot = collections.OrderedDict()
print('%-60s %5s %5s %3s %3s %5s %5s' % ('candidato', 'ficha', 'filas', 'T', 'P', 'DUDA', 'suma'))
for i, fs in por.items():
    n = len(json.load(io.open('cuarentena/grove_high_output/%s.json' % i, encoding='utf-8'))['pasos_accionables'])
    c = collections.Counter(f[2] for f in fs)
    orden = [int(f[1]) for f in fs] == list(range(1, len(fs) + 1))
    print('%-60s %5d %5d %3d %3d %5d %5d%s' % (i, n, len(fs), c['T'], c['P'], c['D'], c['T'] + c['P'] + c['D'], '' if n == len(fs) and orden and sum(c.values()) == len(fs) else '  DESCUADRE'))
    t = tot.setdefault(cap[i], collections.Counter()); t['cand'] += 1; t['ficha'] += n; t['filas'] += len(fs); t['T'] += c['T']; t['P'] += c['P']; t['D'] += c['D']
for k, t in tot.items():
    print('%s: candidatos %d | pasos en ficha %d | filas %d | T %d | P %d | DUDA %d | suma: %d | PUENTE %d de %d = %.2f por ciento | si las DUDA cayesen: %d de %d = %.2f por ciento' % (
        k, t['cand'], t['ficha'], t['filas'], t['T'], t['P'], t['D'], t['T'] + t['P'] + t['D'], t['P'], t['ficha'], 100.0 * t['P'] / t['ficha'],
        t['P'] + t['D'], t['ficha'], 100.0 * (t['P'] + t['D']) / t['ficha']))
g = sum(tot.values(), collections.Counter())
print('los seis: candidatos %d | pasos en ficha %d | filas %d | T %d | P %d | DUDA %d | suma: %d' % (g['cand'], g['ficha'], g['filas'], g['T'], g['P'], g['D'], g['T'] + g['P'] + g['D']))
