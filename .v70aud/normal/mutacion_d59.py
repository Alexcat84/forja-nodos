# -*- coding: utf-8 -*-
"""ACTA 69, 5.5 (la guarda que no muerde es cifra): el reporte de la 70 declara que el hook aborto su primer commit del cierre
por D.59 (70.5.f, correccion declarada). Se re corre por mutacion sobre el texto, sin tocar el arbol: (0) el reporte de hoy;
(1) el mismo con un parrafo al final de la vuelta viva que publica la mediana sin nombrar instrumento, como el que el
extractor dice que escribio; (2) el mismo parrafo nombrando su fichero de salida. Solo lee."""
import io, sys
sys.path.insert(0, 'scripts')
import tallar_reporte as t
base = io.open('docs/loop/REPORTE.md', encoding='utf-8').read()
frase = '\nLos veinte tardaron con una mediana de `2493,4` s y una suma de `45201,6` s.\n'
print('(0) el reporte de hoy: cifras derivadas sueltas %d' % len(t.cifras_derivadas_sueltas(texto=base)))
print('(1) mutado, la mediana sin instrumento: %d' % len(t.cifras_derivadas_sueltas(texto=base + frase)))
print('(2) mutado, la misma frase con su fichero: %d' % len(t.cifras_derivadas_sueltas(texto=base + frase.replace(' s.', ' s (`.v70ext/relojes_resumen.txt`).'))))
