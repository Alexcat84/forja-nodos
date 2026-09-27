# -*- coding: utf-8 -*-
"""Mete las secciones 5 y 6 en la plantilla, en el sitio de sus marcas."""
import io
p = '.v63aud/plantilla.md'
t = io.open(p, encoding='utf-8').read()
for marca, fichero in (('{{BARRIDO}}', '.v63aud/sec5.md'), ('{{ORDEN}}', '.v63aud/sec6.md')):
    if marca in t:
        t = t.replace(marca, io.open(fichero, encoding='utf-8').read().rstrip('\n'))
io.open(p, 'w', encoding='utf-8', newline='\n').write(t)
print('marcas que quedan:', t.count('{{BARRIDO}}') + t.count('{{ORDEN}}'), '| bloques $ por pegar:', t.count('{{$'))
