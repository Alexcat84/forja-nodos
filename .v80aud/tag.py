# -*- coding: utf-8 -*-
"""Fase ciega de la 80, SIN CORRER git: la etiqueta primer-equipo-completo leida de los ficheros de .git/ (la referencia
en refs/tags/ o en packed-refs, y el objeto de la etiqueta descomprimido con zlib si esta suelto en .git/objects/), para
decir a que commit apunta. Si el objeto esta empaquetado, lo dice y no lo lee. Que el grafo del commit etiquetado sea el
de HEAD es git diff, y va a mi turno normal. Solo lee."""
import os, zlib, sys
sys.stdout.reconfigure(encoding="utf-8")
r = '.git/refs/tags/primer-equipo-completo'
h = open(r).read().strip() if os.path.exists(r) else None
if h is None and os.path.exists('.git/packed-refs'):
    for l in open('.git/packed-refs'):
        if l.strip().endswith(' refs/tags/primer-equipo-completo'): h = l.split()[0]
print('referencia de la etiqueta: %s (%s)' % (h, 'suelta en refs/tags' if os.path.exists(r) else 'packed-refs o ninguna'))
o = '.git/objects/%s/%s' % (h[:2], h[2:]) if h else None
if o and os.path.exists(o):
    b = zlib.decompress(open(o, 'rb').read()); cab, cuerpo = b.split(b'\0', 1)
    print('objeto: %s' % cab.decode())
    for l in cuerpo.decode('utf-8', 'replace').split('\n')[:4]: print('  %s' % l)
else: print('objeto suelto: NO (empaquetado o inexistente); no lo leo')
print('HEAD de la rama: %s' % open('.git/refs/heads/extraccion-mundo-11').read().strip())
