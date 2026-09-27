# -*- coding: utf-8 -*-
"""Cablea UNA arista por lectura de .v77ext/aristas_lectura.txt (fila SOSTENGO), con los dos extremos ya en el grafo.
COPIA DE LA VUELTA 77 de .v72ext/arista.py (encargo de la 77, TAREA 4.2). Lo cambiado, y se dice: la sede, que es
.v77ext/aristas_lectura.txt (la copia de la TAREA 2); la cita, a la vuelta 77 y a la ACTA 75 seccion 75.4; la salida, a .v77ext/; y
el --veredicto, que ya no es CONTINUA fijo sino EL DE LA LECTURA (D.53, encargo TAREA 4.2): SANO si la razon de la fila empieza por
D.37 (cabeza a parte), CONTINUA si empieza por "D.29, con veredicto de la lectura CONTINUA"; cualquier otra fila no se cablea.
    python .v77ext/arista.py <madre> <hijo> <paso_de_la_madre>
La razon es la de su fila, tal cual. Guarda la salida en .v77ext/arista_<madre>__<hijo>.txt.
La de la 72 era COPIA DE LA VUELTA 72 de .v70ext/arista.py (que era COPIA de .v68ext/arista.py)."""
import io, subprocess, sys
madre, hijo, paso = sys.argv[1:4]
fila = None
for n, l in enumerate(io.open('.v77ext/aristas_lectura.txt', encoding='utf-8').read().split('\n'), 1):
    c = [x.strip() for x in l.split('|')]
    if len(c) >= 6 and c[0] == 'SOSTENGO' and c[1] == madre and c[2] == hijo:
        fila = (n, c)
if not fila:
    print('NO HAY FILA SOSTENGO para %s > %s' % (madre, hijo)); sys.exit(1)
n, c = fila
razon = '|'.join(c[5:])
if razon.startswith('D.37'):
    veredicto = 'SANO'
elif razon.startswith('D.29, con veredicto de la lectura CONTINUA'):
    veredicto = 'CONTINUA'
else:
    print('LA FILA %d NO DICE SU VEREDICTO: no se cablea' % n); sys.exit(1)
cita = ('leida %s por lectura: .v77ext/aristas_lectura.txt linea %d (%s; %s), adjudicada en la ACTA 75 seccion 75.4; '
        'cableada en la vuelta 77 en el acto de insertar el hijo, con los dos extremos ya en el grafo' % (veredicto, n, c[3], c[4]))
cmd = [sys.executable, 'forja.py', 'arista', '--madre', madre, '--hijo', hijo, '--paso', paso,
       '--razon', razon, '--veredicto', veredicto, '--cita-veredicto', cita]
p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
try:
    out = p.stdout.decode('utf-8')
except UnicodeDecodeError:
    out = p.stdout.decode('cp1252', 'replace')
out = out.replace('\r\n', '\n')
io.open('.v77ext/arista_%s__%s.txt' % (madre, hijo), 'w', encoding='utf-8', newline='\n').write(
    '$ python forja.py arista --madre %s --hijo %s --paso %s --razon <fila %d> --veredicto %s --cita-veredicto <fila %d>\n%s\ncodigo %d\n'
    % (madre, hijo, paso, n, veredicto, n, out, p.returncode))
print(out); print('codigo %d' % p.returncode)
