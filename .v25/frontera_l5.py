# -*- coding: utf-8 -*-
"""LA FRONTERA DE UN CAPITULO DEL LOTE 5, PUBLICADA ANTES DE CORTAR (EXTRACTOR.md 10).

Cuenta las palabras de cada pieza del fichero y comprueba que las piezas mas los
residuos suman el cuerpo entero. Si no suma, hay tramo del capitulo que no aparece
en ninguna pieza, que es la caida que la vuelta 7 pago con la parada del bucle.
"""
import io, sys

RUTA, CUERPO_DESDE = sys.argv[1], 8
PIEZAS = eval(io.open(sys.argv[2], encoding='utf-8').read())

lineas = io.open(RUTA, encoding='utf-8').read().splitlines()
palabras = lambda a, b: sum(len(l.split()) for l in lineas[a - 1:b])
cuerpo = palabras(CUERPO_DESDE, len(lineas))

print('| pieza | lineas | palabras | que es | clase |')
print('|---|---|---:|---|---|')
suma = 0
for nombre, desde, hasta, que, clase in PIEZAS:
    n = palabras(desde, hasta)
    suma += n
    print('| `%s` | L%d a L%d | **%d** | %s | **%s** |' % (nombre, desde, hasta, n, que, clase))
print('| **el cuerpo entero** | **L%d a L%d** | **%d** | **suma de las piezas: %d** | **residuo sin asignar: %d** |'
      % (CUERPO_DESDE, len(lineas), cuerpo, suma, cuerpo - suma))
bordes = sorted((d, h) for _n, d, h, _q, _c in PIEZAS)
solapes = sum(1 for i in range(len(bordes) - 1) if bordes[i][1] >= bordes[i + 1][0])
print('')
print('piezas: %d   lineas solapadas: %d   cuerpo %d   suma %d   residuo %d'
      % (len(PIEZAS), solapes, cuerpo, suma, cuerpo - suma))
