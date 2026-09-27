# -*- coding: utf-8 -*-
"""LA CIFRA DEL HUECO SE CALCULA DE LA LISTA `NUM` DEL PROPIO INSTRUMENTO.

No se teclea aqui ni se copia de ningun sitio: se lee la lista `NUM` del fichero
fuente que produjo cada salida, y se cuenta la que tiene `firmado = False`. Es la
misma cuenta que la linea que ya calculaba `filas con numerador FIRMADO`, que es
lo que desmentia a la celda tecleada.

POR QUE NO SE RE EJECUTA EL INSTRUMENTO ENTERO: su poblacion de ficheros cambio
(once candidatos del lote 4 pasaron de `cuarentena/` a `_insertados/` en la vuelta
24), asi que re correrlo hoy daria un denominador de hoy bajo un rotulo de
entonces, que es falsear la historia para arreglar una celda. Se regenera LA
CELDA, con la cifra calculada, y nada mas.
"""
import io
import re
import sys

FUENTE, SALIDAS, ROTULO = sys.argv[1], sys.argv[2].split(','), sys.argv[3]

texto = io.open(FUENTE, encoding='utf-8').read()
m = re.search(r'^NUM = \[.*?^\]', texto, re.S | re.M)
NUM = eval(m.group(0).split('=', 1)[1].strip())          # la lista del instrumento
hueco = len([1 for _c, _n, _q, f in NUM if not f])
firmadas = len([1 for _c, _n, _q, f in NUM if f])
print('%s: filas en NUM %d, FIRMADAS %d, HUECO calculado %d'
      % (FUENTE, len(NUM), firmadas, hueco))

VIEJA = 'INCOMPLETO: cinco filas sin releer con el ancho'
NUEVA = 'INCOMPLETO: %d filas sin releer con el ancho' % hueco
for ruta in SALIDAS:
    t = io.open(ruta, encoding='utf-8').read()
    if VIEJA not in t:
        print('   %s: ya no la tiene' % ruta)
        continue
    n = t.count(VIEJA)
    io.open(ruta, 'w', encoding='utf-8', newline='\n').write(t.replace(VIEJA, NUEVA))
    print('   %s: %d celda(s) regenerada(s) bajo el rotulo %s' % (ruta, n, ROTULO))
