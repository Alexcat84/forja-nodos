# -*- coding: utf-8 -*-
"""LA FRONTERA DE UNA UNIDAD DE gerber_emyth, PUBLICADA ANTES DE CORTAR (EXTRACTOR.md 10).

Es el instrumento de .v25/frontera_l5.py con DOS cambios, y los dos los pide el
encargo de la vuelta 1 del frente gerber_emyth por escrito:

  (a) NINGUNA CELDA TECLEADA DENTRO DEL INSTRUMENTO. La vuelta 31 cayo por una
      constante puesta a mano, asi que el arranque del cuerpo NO se teclea: se
      deriva del propio fichero (la linea siguiente al segundo ---, que cierra
      la cabecera yaml) y se IMPRIME en la primera linea de salida como AVISO.
  (b) CERO LINEAS SIN CUBRIR Y CERO SOLAPES. El instrumento viejo contaba
      solapes pero NO huecos. El encargo pide las dos cosas, asi que se anade
      el recuento de lineas del cuerpo que no cae en ninguna pieza.
"""
import io, sys

RUTA = sys.argv[1]
PIEZAS = eval(io.open(sys.argv[2], encoding='utf-8').read())

lineas = io.open(RUTA, encoding='utf-8').read().splitlines()
cierres = [i + 1 for i, l in enumerate(lineas) if l.strip() == '---']
CUERPO_DESDE = cierres[1] + 1
ULTIMA = len(lineas)

palabras = lambda a, b: sum(len(l.split()) for l in lineas[a - 1:b])
cuerpo = palabras(CUERPO_DESDE, ULTIMA)

print('AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO')
print('es una constante mia: sale de %s, linea %d, que es la siguiente al segundo'
      % (RUTA, CUERPO_DESDE))
print('--- de la cabecera yaml (cierres en L%s). El cuerpo va de L%d a L%d.'
      % (' y L'.join(str(c) for c in cierres), CUERPO_DESDE, ULTIMA))
print('')
print('| pieza | lineas | palabras | que es | clase |')
print('|---|---|---:|---|---|')
suma = 0
cubiertas = set()
for nombre, desde, hasta, que, clase in PIEZAS:
    n = palabras(desde, hasta)
    suma += n
    cubiertas |= set(range(desde, hasta + 1))
    print('| `%s` | L%d a L%d | **%d** | %s | **%s** |' % (nombre, desde, hasta, n, que, clase))
print('| **el cuerpo entero** | **L%d a L%d** | **%d** | **suma de las piezas: %d** | **residuo sin asignar: %d** |'
      % (CUERPO_DESDE, ULTIMA, cuerpo, suma, cuerpo - suma))

bordes = sorted((d, h) for _n, d, h, _q, _c in PIEZAS)
solapes = sum(1 for i in range(len(bordes) - 1) if bordes[i][1] >= bordes[i + 1][0])
huecos = sorted(set(range(CUERPO_DESDE, ULTIMA + 1)) - cubiertas)
print('')
print('piezas: %d   lineas solapadas: %d   lineas sin cubrir: %d   cuerpo %d   suma %d   residuo %d'
      % (len(PIEZAS), solapes, len(huecos), cuerpo, suma, cuerpo - suma))
if huecos:
    print('HUECOS: %s' % ', '.join('L%d' % h for h in huecos))
