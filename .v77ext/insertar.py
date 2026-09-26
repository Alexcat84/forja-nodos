# -*- coding: utf-8 -*-
"""Corre UN `python forja.py insertar` de la vuelta 77, filas 1 a 22 de .v76ext/orden.txt (COPIA DE LA VUELTA 77 de .v75ext/insertar.py, con la sede de las lineas cambiada a .v77ext/veredictos_listos.txt (la copia corregida por la TAREA 2 de la 77), la bandeja a cuarentena/gerber_emyth/ y la salida a .v77ext/; la de la 75 era COPIA DE LA VUELTA 75 de .v72ext/insertar.py, con la sede de las lineas cambiada a .v73ext/veredictos_listos.txt y la salida a .v75ext/; la de la 72 era COPIA DE LA VUELTA 72 de .v70ext/insertar.py, con la sede de las lineas cambiada a .v71ext/veredictos_listos.txt y la salida a .v72ext/; la de la 70 era COPIA de .v68ext/insertar.py, que era
COPIA de la 67), y espera a que vuelva.

    python .v77ext/insertar.py <fila> <id>

Lo que cambia de la copia, y se dice: las lineas --veredicto se copian TAL CUAL de su bloque `## <id>` de
.v73ext/veredictos_listos.txt (encargo de la 75, TAREA 4.1), tal cual;
las lineas que empiezan por '#' dentro del bloque son las viejas que la correccion declarada dejo encima como comentario
y NO se pasan. Escribe .v75ext/insertar_<fila>_<id>.txt con el comando, la salida entera, el codigo y el reloj,
y al final el marcador .v75ext/insertar_<fila>_<id>.fin. No toca nada mas.
"""
import io, subprocess, sys, time

fila, cid = sys.argv[1], sys.argv[2]
lineas, dentro = [], False
for l in io.open('.v77ext/veredictos_listos.txt', encoding='utf-8').read().split('\n'):
    if l.startswith('## '):
        dentro = (l[3:].strip() == cid); continue
    if dentro and l.strip() and not l.startswith('#'):
        lineas.append(l.rstrip())
cmd = [sys.executable, 'forja.py', 'insertar', 'cuarentena/gerber_emyth/%s.json' % cid, '--sin-preguntas']
for l in lineas:
    cmd += ['--veredicto', l]
base = '.v77ext/insertar_%s_%s' % (fila, cid)
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
