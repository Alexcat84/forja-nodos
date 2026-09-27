# -*- coding: utf-8 -*-
# Cuenta palabras de cuerpo de un tramo de lineas de un fichero de fuentes.
#   python .v3g/palabras_tramo.py fuentes/grove_high_output/cap_03.md 99 99
import io, sys

ruta, desde, hasta = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
lineas = io.open(ruta, encoding='utf-8').read().split('\n')
tramo = lineas[desde - 1:hasta]
palabras = ' '.join(tramo).split()
print('%s  L%d a L%d  lineas %d  palabras %d'
      % (ruta, desde, hasta, len(tramo), len(palabras)))
