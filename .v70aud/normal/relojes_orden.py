# -*- coding: utf-8 -*-
"""Turno normal de la 70: los 20 insertar de .v70ext/, por sus propios ficheros. Codigo del .fin, linea 'fin', linea
'NODO INSERTADO', poblacion de la aduana; solape (inicio de cada uno contra fin del anterior); orden contra
.v69ext/orden.txt; y las restricciones que obligan de MI .v69aud/restricciones_orden.py (madre antes que hijo) contra el
orden en que entraron de verdad. Reparto con suma (R7). Solo lee."""
import io, re, sys, glob, subprocess, collections, datetime
sys.stdout.reconfigure(encoding="utf-8")
T = lambda s: datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
filas = []
for f in sorted(glob.glob('.v70ext/insertar_[0-9][0-9]_*.txt')):
    n, i = re.match(r'.*insertar_(\d\d)_(.+)\.txt$', f.replace(chr(92), '/')).groups()
    t = io.open(f, encoding='utf-8').read()
    ini = re.search(r'^inicio (\S+ \S+)', t, re.M).group(1); fin = re.search(r'^fin (\S+ \S+) \| codigo de salida (\d+)', t, re.M)
    pob = re.search(r'contra (\d+) +\((\d+) del grafo mas (\d+)', t)
    finc = io.open(f[:-4] + '.fin', encoding='utf-8').read().strip()
    filas.append((int(n), i, T(ini), T(fin.group(1)), fin.group(2), finc, 'NODO INSERTADO' in t, pob.groups()))
est = collections.Counter()
prev = None
for n, i, a, b, c, fc, ins, pob in filas:
    sol = prev is not None and a < prev
    est['fin 0, .fin 0, INSERTADO, sin solape' if (c == '0' and fc == '0' and ins and not sol) else 'otra cosa'] += 1
    print('%2d %-52s %s a %s | fin %s .fin %s | %s | poblacion %s = %s + %s | hueco con el anterior %s s' % (n, i, a.time(), b.time(), c, fc, 'INSERTADO' if ins else 'NO', pob[0], pob[1], pob[2], '-' if prev is None else int((a - prev).total_seconds())))
    prev = b
print('insertar: %d | por estado: %s | suma: %d' % (len(filas), dict(est), sum(est.values())))
orden = [l.split()[1] for l in io.open('.v69ext/orden.txt', encoding='utf-8') if re.match(r'^\d+ ', l)][:20]
print('orden de entrada igual a las filas 1 a 20 de .v69ext/orden.txt: %s' % ('SI' if [f[1] for f in filas] == orden else 'NO'))
pos = dict((f[1], f[0]) for f in filas)
sal = subprocess.run([sys.executable, '.v69aud/restricciones_orden.py'], capture_output=True, text=True, encoding='utf-8').stdout
ob = [re.match(r'^  (\S+) +antes que (\S+) +(CONTINUA|arista por lectura)', l) for l in sal.splitlines()]
ob = [m.groups()[:2] for m in ob if m]
viol = [(a, b) for a, b in ob if a in pos and b in pos and pos[a] > pos[b]]
print('mis restricciones que obligan con los dos extremos en la tanda: %d | violadas por el orden real: %d %s' % (len(ob), len(viol), viol))
