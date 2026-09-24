# -*- coding: utf-8 -*-
"""Corre UN `python forja.py insertar` de la tanda de la vuelta 67 (COPIA de .v66ext/insertar.py) y espera a que vuelva.

    python .v67ext/insertar.py <fila> <id>

Lo que cambia de la copia, y se dice: las lineas --veredicto se copian TAL CUAL de su bloque `## <id>` de
.v66ext/veredictos_listos.txt (encargo, TAREA 4.1), que es el fichero de los 22 de cap_04 con las correcciones de la
TAREA 2; las lineas que empiezan por '#' dentro del bloque son las viejas que la correccion declarada dejo encima
como comentario y NO se pasan. Ya no hay caso especial de detectar_arreglar_fallo_etapa_menor_valor: esta en el grafo.
Escribe .v67ext/insertar_<fila>_<id>.txt con el comando, la salida entera, el codigo y el reloj,
y al final el marcador .v67ext/insertar_<fila>_<id>.fin. No toca nada mas.
"""
import io, subprocess, sys, time

fila, cid = sys.argv[1], sys.argv[2]
lineas, dentro = [], False
for l in io.open('.v66ext/veredictos_listos.txt', encoding='utf-8').read().split('\n'):
    if l.startswith('## '):
        dentro = (l[3:].strip() == cid); continue
    if dentro and l.strip() and not l.startswith('#'):
        lineas.append(l.rstrip())
cmd = [sys.executable, 'forja.py', 'insertar', 'cuarentena/grove_high_output/%s.json' % cid, '--sin-preguntas']
for l in lineas:
    cmd += ['--veredicto', l]
base = '.v67ext/insertar_%s_%s' % (fila, cid)
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
