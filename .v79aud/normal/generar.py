# -*- coding: utf-8 -*-
"""ACTA 78: rellena una plantilla. Cada linea @@CMD <orden>@@ se sustituye por el bloque `    $ <orden>` con la salida de la orden,
corrida con bash en el momento de generar; cada @@FILE <ruta>@@ pega el fichero tal cual, sangrado (ficheros que ya traen sus
lineas `$` con su salida, escritos por tee al correrlas). Uso: python generar.py <plantilla> <salida>"""
import io, re, subprocess, sys
BASH = r'C:\Program Files\Git\usr\bin\bash.exe'
src, dst = sys.argv[1:3]
out = []
for l in io.open(src, encoding='utf-8').read().split('\n'):
    m = re.match(r'^@@(CMD|FILE) (.*)@@$', l)
    if not m:
        out.append(l); continue
    if m.group(1) == 'CMD':
        r = subprocess.run([BASH, '-c', m.group(2)], capture_output=True, env=dict(__import__('os').environ, PYTHONIOENCODING='utf-8'))
        txt = (r.stdout + r.stderr).decode('utf-8', 'replace').replace('\r', '').rstrip('\n')
        out.append('    $ ' + m.group(2))
    else:
        txt = io.open(m.group(2), encoding='utf-8').read().replace('\r', '').rstrip('\n')
    out.extend(('    ' + x).rstrip() for x in txt.split('\n'))
io.open(dst, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('escrito %s: %d lineas' % (dst, len(out)))
