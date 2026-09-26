# -*- coding: utf-8 -*-
"""Turno normal de la ACTA 76. Que cada insertar de la 77 arranco despues de que el anterior volviera y de que su fila se
commiteara, y que el primero arranco despues del commit de la TAREA 2 (y de la 3). El arranque es el fin menos la duracion
que cada .v77ext/insertar_NN_*.txt escribe en su ultima linea; las horas de commit, de git log. Solo lee."""
import glob, io, re, subprocess, datetime as dt
T = lambda s: dt.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
filas = []
for f in sorted(glob.glob('.v77ext/insertar_*.txt')):
    m = re.search(r'fin (\S+ \S+) \| codigo de salida (\d+) \| ([\d.]+) s', io.open(f, encoding='utf-8').read())
    fin = T(m.group(1)); filas.append((f, fin - dt.timedelta(seconds=float(m.group(3))), fin, m.group(2)))
log = subprocess.run(['git', 'log', '--format=%cI %s', '70a827c9..a70bdf05'], capture_output=True).stdout.decode('utf-8').splitlines()
com = {}
for l in log:
    h, s = l[:19].replace('T', ' '), l[26:]
    m = re.match(r'Vuelta 77, fila (\d+): (.*)', s)
    if m: com.setdefault(int(m.group(1)), []).append((T(h), m.group(2)[:30]))
    if s.startswith('Vuelta 77, T1 y T2'): t2 = T(h)
    if s.startswith('Vuelta 77, T3'): t3 = T(h)
print('commit de T1 y T2: %s | de T3: %s | arranque del insertar 1: %s | despues de los dos: %s' % (t2.time(), t3.time(), filas[0][1].time().strftime('%H:%M:%S'), 'SI' if filas[0][1] > t3 > t2 else 'NO'))
malos = 0; fins = {}
for k, (f, ini, fin, rc) in enumerate(filas, 1):
    ult = max(c[0] for c in com[k])
    sig = filas[k][1] if k < len(filas) else None
    ok = sig is None or (sig > fin and sig > ult)
    malos += not ok
    fins[rc] = fins.get(rc, 0) + 1
    print('  %2d arranque %s fin %s rc %s | commits de su fila: %d, el ultimo %s | el siguiente arranca despues: %s' % (
        k, ini.strftime('%H:%M:%S'), fin.strftime('%H:%M:%S'), rc, len(com[k]), ult.strftime('%H:%M:%S'), '(ultimo)' if sig is None else ('SI' if ok else 'NO')))
print('insertar: %d | codigos: %s | suma: %d | con solape o sin commit antes del siguiente: %d' % (len(filas), fins, sum(fins.values()), malos))
print('ficheros .fin: %d | su contenido: %s' % (len(glob.glob('.v77ext/insertar_*.fin')), sorted(set(io.open(x).read().strip() for x in glob.glob('.v77ext/insertar_*.fin')))))
