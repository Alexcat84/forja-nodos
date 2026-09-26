# -*- coding: utf-8 -*-
"""Corre UN `python forja.py insertar` de la vuelta 80, filas 1 a 20 de .v78ext/orden.txt (COPIA DE LA VUELTA 80 de .v77ext/insertar.py,
encargo de la 80, metodo de la 77. Lo que cambia, y nada mas: la sede de las lineas, que es .v78ext/veredictos_listos.txt; la bandeja,
cuarentena/marquet_turn_the_ship/; la tanda, las filas de .v78ext/orden.txt, y por eso comprueba antes de lanzar que el id es el de su
fila y si no, no lanza; y la salida, a .v80ext/). Lo que decia la de la 77: COPIA DE LA VUELTA 77 de .v75ext/insertar.py, con la sede de
las lineas cambiada a .v77ext/veredictos_listos.txt, la bandeja a cuarentena/gerber_emyth/ y la salida a .v77ext/; y espera a que vuelva.

    python .v80ext/insertar.py <fila> <id>

Las lineas --veredicto se copian TAL CUAL de su bloque `## <id>` de .v78ext/veredictos_listos.txt; las lineas que empiezan por '#'
dentro del bloque NO se pasan. Escribe .v80ext/insertar_<fila>_<id>.txt con el comando, la salida entera, el codigo y el reloj,
y al final el marcador .v80ext/insertar_<fila>_<id>.fin. No toca nada mas.
"""
import io, re, subprocess, sys, time

fila, cid = sys.argv[1], sys.argv[2]
orden = dict((int(l.split()[0]), l.split()[1]) for l in io.open('.v78ext/orden.txt', encoding='utf-8') if re.match(r'^\d+\s', l))
if orden.get(int(fila)) != cid:
    print('LA FILA %s DE .v78ext/orden.txt ES %s, NO %s: no lanzo' % (fila, orden.get(int(fila)), cid)); sys.exit(2)
lineas, dentro = [], False
for l in io.open('.v78ext/veredictos_listos.txt', encoding='utf-8').read().split('\n'):
    if l.startswith('## '):
        dentro = (l[3:].strip() == cid); continue
    if dentro and l.strip() and not l.startswith('#'):
        lineas.append(l.rstrip())
cmd = [sys.executable, 'forja.py', 'insertar', 'cuarentena/marquet_turn_the_ship/%s.json' % cid, '--sin-preguntas']
for l in lineas:
    cmd += ['--veredicto', l]
base = '.v80ext/insertar_%s_%s' % (fila, cid)
t0 = time.time()
with io.open(base + '.txt', 'w', encoding='utf-8') as f:
    f.write('fila %s, %s, lineas --veredicto: %d\n' % (fila, cid, len(lineas)))
    for l in lineas:
        f.write('  --veredicto %s\n' % l)
    f.write('inicio %s\n' % time.strftime('%Y-%m-%d %H:%M:%S'))
    f.write('=' * 70 + '\n')
    f.flush()
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    f.write(p.stdout.decode('utf-8', 'replace').replace('\r\n', '\n'))
    f.write('\n' + '=' * 70 + '\n')
    f.write('fin %s | codigo de salida %d | %.1f s\n' % (time.strftime('%Y-%m-%d %H:%M:%S'), p.returncode, time.time() - t0))
io.open(base + '.fin', 'w', encoding='utf-8').write('%d\n' % p.returncode)
print('FIN fila %s %s codigo %d en %.1f s' % (fila, cid, p.returncode, time.time() - t0))
