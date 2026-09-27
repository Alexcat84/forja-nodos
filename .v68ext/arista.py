# -*- coding: utf-8 -*-
"""Cablea UNA arista por lectura de .v66ext/aristas_lectura.txt (fila SOSTENGO), con la madre ya en el grafo.
COPIA DE LA VUELTA 68 de .v67ext/arista.py (que era COPIA de .v65ext/arista.py con la sede en .v66ext/aristas_lectura.txt),
con la cita cambiada a la vuelta 68 y la salida a .v68ext/.
    python .v68ext/arista.py <madre> <hijo> <paso_de_la_madre>
La razon es la de su fila, tal cual. --veredicto CONTINUA y --cita-veredicto a la fila y a la ACTA 65 (D65.2).
Guarda la salida en .v68ext/arista_<madre>__<hijo>.txt."""
import io, subprocess, sys
madre, hijo, paso = sys.argv[1:4]
fila = None
for n, l in enumerate(io.open('.v66ext/aristas_lectura.txt', encoding='utf-8').read().split('\n'), 1):
    c = [x.strip() for x in l.split('|')]
    if len(c) >= 6 and c[0] == 'SOSTENGO' and c[1] == madre and c[2] == hijo:
        fila = (n, c)
if not fila:
    print('NO HAY FILA SOSTENGO para %s > %s' % (madre, hijo)); sys.exit(1)
n, c = fila
razon = '|'.join(c[5:])
cita = ('leida CONTINUA: .v66ext/aristas_lectura.txt linea %d (%s; %s), sostenida por la ACTA 65 seccion 65.4.b; '
        'cableada en la vuelta 68 con la madre ya en el grafo' % (n, c[3], c[4]))
cmd = [sys.executable, 'forja.py', 'arista', '--madre', madre, '--hijo', hijo, '--paso', paso,
       '--razon', razon, '--veredicto', 'CONTINUA', '--cita-veredicto', cita]
p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
try:
    out = p.stdout.decode('utf-8')
except UnicodeDecodeError:
    out = p.stdout.decode('cp1252', 'replace')
out = out.replace('\r\n', '\n')
io.open('.v68ext/arista_%s__%s.txt' % (madre, hijo), 'w', encoding='utf-8', newline='\n').write(
    '$ python forja.py arista --madre %s --hijo %s --paso %s --razon <fila %d> --veredicto CONTINUA --cita-veredicto <fila %d>\n%s\ncodigo %d\n'
    % (madre, hijo, paso, n, n, out, p.returncode))
print(out); print('codigo %d' % p.returncode)
