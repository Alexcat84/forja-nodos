# -*- coding: utf-8 -*-
"""Vuelta 80, TAREA 4 (d183): escribe la frontera de Grove sobre eliminar_seguimiento_descendente_responsabilizar_dueno con
python forja.py corregir, pasando TAL CUAL la linea que sigue a 'ANADE:' y la que sigue a 'RAZON:' en .v79ext/frontera_grove.txt,
leidas del fichero por este guion y no copiadas a mano. Antes de correr comprueba que el nodo vive en dataset/nodos.jsonl, y si no,
no corre. Guarda el comando, la salida y el codigo en .v80ext/t4_corregir.txt.
    python .v80ext/frontera.py"""
import io, json, subprocess, sys
NODO = 'eliminar_seguimiento_descendente_responsabilizar_dueno'
L = io.open('.v79ext/frontera_grove.txt', encoding='utf-8').read().split('\n')
anade = L[L.index('ANADE:') + 1]
razon = L[L.index('RAZON:') + 1]
vivos = set(json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip())
if NODO not in vivos:
    print('%s NO VIVE EN EL GRAFO: no corro corregir' % NODO); sys.exit(1)
cmd = [sys.executable, 'forja.py', 'corregir', '--nodo', NODO, '--anade', anade, '--razon', razon]
p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
out = p.stdout.decode('utf-8', 'replace').replace('\r\n', '\n')
cab = ('$ python forja.py corregir --nodo %s --anade "<linea %d de .v79ext/frontera_grove.txt, %d caracteres>" '
       '--razon "<linea %d de .v79ext/frontera_grove.txt, %d caracteres>"\n' % (NODO, L.index('ANADE:') + 2, len(anade), L.index('RAZON:') + 2, len(razon)))
io.open('.v80ext/t4_corregir.txt', 'w', encoding='utf-8', newline='\n').write(cab + out + 'rc=%d\n' % p.returncode)
print(cab + out + 'rc=%d' % p.returncode)
