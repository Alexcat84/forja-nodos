# -*- coding: utf-8 -*-
"""ACTA 66: inicio y fin de cada insertar de la 67, de la primera y ultima linea con fecha de cada .v67ext/insertar_*.txt,
y si alguno arranco antes de que acabara el anterior."""
import glob, io, re, datetime
F = '%Y-%m-%d %H:%M:%S'; r = []
for f in sorted(glob.glob('.v67ext/insertar_*.txt')):
    t = io.open(f, encoding='utf-8').read()
    fechas = re.findall(r'(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)', t)
    fin = re.search(r'fin (\S+ \S+) \| codigo de salida (\d+) \| ([\d.]+) s', t)
    ffin = datetime.datetime.strptime(fin.group(1)[:19], F)
    ini = ffin - datetime.timedelta(seconds=float(fin.group(3)))
    r.append((ini, ffin, f.split('insertar_')[1][:2], fin.group(2)))
sol = 0
for a, b in zip(r, r[1:]):
    hueco = (b[0] - a[1]).total_seconds()
    if hueco < 0: sol += 1
    print('fila %s fin %s | fila %s inicio %s | hueco %6.0f s' % (a[2], a[1], b[2], b[0].strftime('%H:%M:%S'), hueco))
print('insertar: %d | codigos distintos de 0: %d | solapes: %d' % (len(r), sum(1 for x in r if x[3] != '0'), sol))
