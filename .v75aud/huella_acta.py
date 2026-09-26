# -*- coding: utf-8 -*-
"""Fase ciega de la 75 (copia de .v72aud/huella_acta.py con la acta cambiada), sin git: la huella que el prompt me entrega (ACTA ANTERIOR LEIDA) contra el blob del fichero
docs/loop/ACTA_AUDITOR.md tal como esta hoy en el arbol, calculado a mano como lo calcula git (sha1 de 'blob <bytes>\0'
mas el contenido), sin correr git, y con los CRLF pasados a LF como hace git al guardarlo (.gitattributes:
'* text=auto eol=lf'; el fichero del arbol trae algunas lineas en CRLF, y se cuentan). Y la linea donde empieza la
ACTA 73, que es la que lei entera. Solo lee."""
import hashlib, sys
sys.stdout.reconfigure(encoding="utf-8")
b = open('docs/loop/ACTA_AUDITOR.md', 'rb').read()
c = b.replace(b'\r\n', b'\n')
print('sha1 del blob tal cual: %s' % hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest())
print('lineas con CRLF en el arbol: %d | sha1 del blob normalizado a LF: %s' % (b.count(b'\r\n'), hashlib.sha1(b'blob %d\0' % len(c) + c).hexdigest()))
ls = c.decode('utf-8').split('\n')
ini = [n + 1 for n, l in enumerate(ls) if l.startswith('# ACTA 73.')]
print('lineas del fichero: %d | la ACTA 73 empieza en la linea: %s' % (len(ls) - (1 if ls[-1] == '' else 0), ini))
