# -*- coding: utf-8 -*-
"""RECOMPONE LAS TRES FRONTERAS DE LA VUELTA 5 SIN EL INSTRUMENTO DEL EXTRACTOR.

Codigo del auditor. No importa nada de .gerber_v5/: relee los ficheros del libro,
cuenta las palabras de cada pieza con su propio recorrido, y compara contra la
celda que el reporte publica. Ademas calcula solapes y lineas sin cubrir con un
conjunto de lineas propio, no con bordes consecutivos, y COMPRUEBA EL BORDE DE
ARRIBA: que ninguna pieza termine despues de la ultima linea del fichero.
"""
import io

PIEZAS = {
 'cap_15': [('R1', 8, 20, 31), ('R2', 21, 42, 390), ('R3', 43, 86, 516),
            ('R4', 87, 166, 694), ('R5', 167, 178, 87), ('R6', 179, 184, 76),
            ('R7', 185, 280, 2891)],
 'cap_16': [('R1', 8, 20, 51), ('R2', 21, 30, 87), ('R3', 31, 154, 704),
            ('R4', 155, 244, 1166), ('R5', 245, 318, 785), ('R6', 319, 420, 1138),
            ('R7', 421, 489, 904)],
 'cap_17': [('R1', 8, 18, 13), ('R2', 19, 50, 254), ('R3', 51, 221, 2181)],
}
CUERPO = {'cap_15': (8, 279), 'cap_16': (8, 489), 'cap_17': (8, 221)}

for cap in sorted(PIEZAS):
    ruta = 'fuentes/gerber_emyth/%s.md' % cap
    lineas = io.open(ruta, encoding='utf-8').read().splitlines()
    palabras = lambda a, b: len(' '.join(lineas[a - 1:b]).split())
    print('=== %s, %d lineas en el fichero' % (cap, len(lineas)))
    suma = 0
    discrepan = 0
    cubiertas = set()
    solapes = 0
    for nombre, desde, hasta, publicado in PIEZAS[cap]:
        mio = palabras(desde, hasta)
        suma += mio
        for i in range(desde, hasta + 1):
            if i in cubiertas:
                solapes += 1
            cubiertas.add(i)
        if mio != publicado:
            discrepan += 1
        print('  %s L%d a L%d   reporte %d   mio %d   %s'
              % (nombre, desde, hasta, publicado, mio,
                 'OK' if mio == publicado else 'DISCREPA'))
    desde, hasta = CUERPO[cap]
    cuerpo = palabras(desde, hasta)
    huecos = [i for i in range(desde, hasta + 1) if i not in cubiertas]
    rebasan = ['%s acaba en L%d' % (n, h) for n, d, h, _p in PIEZAS[cap]
               if h > len(lineas)]
    print('  cuerpo %d   suma %d   residuo %d   solapes %d   sin cubrir %d   '
          'celdas que discrepan %d'
          % (cuerpo, suma, cuerpo - suma, solapes, len(huecos), discrepan))
    if rebasan:
        print('  PIEZAS QUE REBASAN EL FICHERO: %s' % ', '.join(rebasan))
