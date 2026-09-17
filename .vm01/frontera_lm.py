# -*- coding: utf-8 -*-
"""LA FRONTERA DE UNA UNIDAD DEL LOTE marquet_turn_the_ship, PUBLICADA ANTES DE CORTAR.

Hereda de .v25/frontera_l5.py y le quita LA UNICA CELDA QUE ALLI ESTABA TECLEADA:
CUERPO_DESDE valia 8 escrito a mano. Aqui se LEE del fichero, buscando el cierre
del encabezado YAML, y la primera linea de salida dice de donde salio. Es la
caida de la vuelta 31 y la TAREA 1 de este encargo la nombra por su nombre.
"""
import io, sys

RUTA = sys.argv[1]
lineas = io.open(RUTA, encoding='utf-8').read().splitlines()

# el cuerpo empieza en la linea siguiente al segundo '---' del encabezado
cierres = [i + 1 for i, l in enumerate(lineas) if l.strip() == '---']
CUERPO_DESDE = cierres[1] + 1
print('AVISO: CUERPO_DESDE=%d LEIDO del fichero (segundo cierre "---" del encabezado en L%d de %d lineas). NINGUNA CELDA TECLEADA.'
      % (CUERPO_DESDE, cierres[1], len(lineas)))

PIEZAS = eval(io.open(sys.argv[2], encoding='utf-8').read())
palabras = lambda a, b: sum(len(l.split()) for l in lineas[a - 1:b])
cuerpo = palabras(CUERPO_DESDE, len(lineas))

print('')
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
cubiertas = set()
for _n, d, h, _q, _c in PIEZAS:
    cubiertas |= set(range(d, h + 1))
sin_cubrir = [i for i in range(CUERPO_DESDE, len(lineas) + 1)
              if i not in cubiertas and lineas[i - 1].split()]
print('')
print('piezas: %d   lineas solapadas: %d   cuerpo %d   suma %d   residuo %d   lineas con palabras sin cubrir: %d %s'
      % (len(PIEZAS), solapes, cuerpo, suma, cuerpo - suma, len(sin_cubrir), sin_cubrir))
