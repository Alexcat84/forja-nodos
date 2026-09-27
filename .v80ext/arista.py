# -*- coding: utf-8 -*-
"""Cablea UNA arista por lectura de .v78ext/aristas_lectura.txt (fila SOSTENGO), con los dos extremos ya en el grafo.
COPIA DE LA VUELTA 80 de .v77ext/arista.py (encargo de la 80, metodo de la 77). Lo cambiado, y se dice: la sede, que es
.v78ext/aristas_lectura.txt; la cita, a la vuelta 80 y a la ACTA 77 secciones 77.4 y 77.5; la salida, a .v80ext/; y UNA REGLA DE
VEREDICTO MAS: la fila SOSTENGO de esta tanda empieza por "D.29, con el criterio de la ACTA 75 seccion 75.4", que la copia de la 77 no
reconocia y no cablearia. SU VEREDICTO DE LA LECTURA ES CONTINUA, como el de fingir a recorrer en la 77 (D.53: el de la lectura, no el
de la arista): el hijo parte del producto de un paso de la madre, que es lo que la ACTA 77 77.4 sostuvo. Las dos reglas de la 77 siguen:
SANO si la razon de la fila empieza por D.37 (cabeza a parte), CONTINUA si empieza por "D.29, con veredicto de la lectura CONTINUA";
cualquier otra fila no se cablea.
    python .v80ext/arista.py <madre> <hijo> <paso_de_la_madre>
La razon es la de su fila, tal cual. Guarda la salida en .v80ext/arista_<madre>__<hijo>.txt.
La de la 77 era COPIA DE LA VUELTA 77 de .v72ext/arista.py."""
import io, subprocess, sys
madre, hijo, paso = sys.argv[1:4]
fila = None
for n, l in enumerate(io.open('.v78ext/aristas_lectura.txt', encoding='utf-8').read().split('\n'), 1):
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
elif razon.startswith('D.29, con el criterio de la ACTA 75 seccion 75.4'):
    veredicto = 'CONTINUA'
else:
    print('LA FILA %d NO DICE SU VEREDICTO: no se cablea' % n); sys.exit(1)
cita = ('leida %s por lectura: .v78ext/aristas_lectura.txt linea %d (%s; %s), adjudicada en la ACTA 77 secciones 77.4 y 77.5; '
        'cableada en la vuelta 80 en el acto de insertar el hijo, con los dos extremos ya en el grafo' % (veredicto, n, c[3], c[4]))
cmd = [sys.executable, 'forja.py', 'arista', '--madre', madre, '--hijo', hijo, '--paso', paso,
       '--razon', razon, '--veredicto', veredicto, '--cita-veredicto', cita]
p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
try:
    out = p.stdout.decode('utf-8')
except UnicodeDecodeError:
    out = p.stdout.decode('cp1252', 'replace')
out = out.replace('\r\n', '\n')
io.open('.v80ext/arista_%s__%s.txt' % (madre, hijo), 'w', encoding='utf-8', newline='\n').write(
    '$ python forja.py arista --madre %s --hijo %s --paso %s --razon <fila %d> --veredicto %s --cita-veredicto <fila %d>\n%s\ncodigo %d\n'
    % (madre, hijo, paso, n, veredicto, n, out, p.returncode))
print(out); print('codigo %d' % p.returncode)
