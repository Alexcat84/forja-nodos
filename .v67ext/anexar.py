# -*- coding: utf-8 -*-
"""Anexa a docs/loop/REPORTE.md un trozo escrito en .v67ext/<trozo>.md, con dos marcas que se sustituyen por
salida de instrumento y no por texto tecleado (D.41, R5):
  @@PEGA <fichero>@@   el fichero entero, indentado cuatro espacios (ya lleva sus lineas `$`)
  @@CORRE <comando>@@  corre el comando con bash AHORA, y pega `$ <comando>` y su salida entera, indentados
    python .v67ext/anexar.py <trozo.md>"""
import io, re, subprocess, sys
BASH = r'C:\Program Files\Git\usr\bin\bash.exe'  # el bash de Git: el `bash` del PATH de Windows es el de WSL
src = io.open(sys.argv[1], encoding='utf-8').read().split('\n')
out = []
ind = lambda t: [('    ' + x) if x.strip() else '' for x in t.replace('\r\n', '\n').rstrip('\n').split('\n')]
for l in src:
    m = re.match(r'^@@PEGA (.+)@@$', l)
    c = re.match(r'^@@CORRE (.+)@@$', l)
    if m:
        out += ind(io.open(m.group(1), encoding='utf-8').read())
    elif c:
        p = subprocess.run([BASH, '-c', c.group(1)], capture_output=True)
        t = p.stdout.decode('utf-8', 'replace') + p.stderr.decode('utf-8', 'replace')
        out += ind('$ ' + c.group(1) + '\n' + t)
    else:
        out.append(l)
with io.open('docs/loop/REPORTE.md', 'a', encoding='utf-8', newline='\n') as f:
    f.write('\n' + '\n'.join(out).rstrip('\n') + '\n')
print('anexadas %d lineas' % len(out))
