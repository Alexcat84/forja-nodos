# -*- coding: utf-8 -*-
"""CADA BLOQUE PEGADO DE LA APERTURA, CON LA FRASE QUE LO PRESENTA.

Es la comprobacion del REMEDIO DEL AUDITOR, VUELTA 49, segundo (ACTA 47, 47.9.d):
toda frase mia que acompane a un pegado dice lo que ESE pegado mide, y si habla de
otra cosa va marcada LECTURA. El instrumento NO juzga si la frase es cierta: pone
las dos cosas juntas para que se lean una contra otra, que es lo unico que una
maquina puede hacer aqui.

BLOQUE PEGADO = tramo de lineas seguidas sangradas con cuatro espacios.
FRASE DE ENCIMA = la ultima linea de prosa no vacia antes del bloque.
FRASE DE DEBAJO = la primera linea de prosa no vacia despues del bloque."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
L = io.open('docs/loop/APERTURA_CIEGA.md', encoding='utf-8').read().split('\n')

bloques, i = [], 0
while i < len(L):
    if L[i].startswith('    ') and L[i].strip():
        a = i
        while i < len(L) and (L[i].startswith('    ') or not L[i].strip()):
            i += 1
        b = i - 1
        while b > a and not L[b].strip():
            b -= 1
        bloques.append((a, b))
    else:
        i += 1

def prosa(rango, paso):
    n = rango
    while 0 <= n < len(L):
        if L[n].strip() and not L[n].startswith('    '):
            return n + 1, L[n].strip()
        n += paso
    return 0, '(no hay)'

print('bloques pegados en la pagina: %d' % len(bloques))
print()
for a, b in bloques:
    na, fa = prosa(a - 1, -1)
    nd, fd = prosa(b + 1, 1)
    print('BLOQUE lineas %d a %d, primera linea suya: %s' % (a + 1, b + 1, L[a].strip()[:95]))
    print('   frase de encima (linea %d): %s' % (na, fa[:175]))
    print('   frase de debajo (linea %d): %s' % (nd, fd[:175]))
    print()
