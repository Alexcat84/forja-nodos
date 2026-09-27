# -*- coding: utf-8 -*-
"""Fase ciega de la 75 (copia de .v72aud/lineas_fuente.py con las lineas cambiadas): las lineas del libro que sostienen
las 3 aristas que mi lectura espera (.v75aud/esperado_75.py) y el par corregido de D73.9, con la columna 'linea' de sus
filas en .v73aud/aristas_lectura.tsv (cap_15 L111 y L113; cap_17 L51, L53, L57 y L61), impresas del fichero de
fuentes/grove_high_output/ tal cual y cortadas a 480 caracteres. La raya y el guion medio del libro se imprimen como
'(raya)', porque la casa no admite ninguno de los dos en sus paginas (forja.py guiones); la cuenta de caracteres es la de
la linea original. Solo lee."""
import io, sys
sys.stdout.reconfigure(encoding="utf-8")
for cap, n in (('cap_15', 111), ('cap_15', 113), ('cap_17', 51), ('cap_17', 53), ('cap_17', 57), ('cap_17', 61)):
    t = io.open('fuentes/grove_high_output/%s.md' % cap, encoding='utf-8').read().split('\n')[n - 1]
    c = t[:480].replace(chr(0x2014), ' (raya) ').replace(chr(0x2013), ' (raya) ')
    print('%s L%d (%d caracteres): %s%s' % (cap, n, len(t), c, ' [...]' if len(t) > 480 else ''))
