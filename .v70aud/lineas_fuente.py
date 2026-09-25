# -*- coding: utf-8 -*-
"""Fase ciega de la 70: las lineas del libro que sostienen las 7 aristas que mi lectura espera (las de
.v68aud/aristas_lectura.tsv con su columna 'linea'), impresas del fichero de fuentes/grove_high_output/ tal cual y
cortadas a 360 caracteres. La raya y el guion medio del libro se imprimen como '(raya)', porque la casa no admite
ninguno de los dos en sus paginas (forja.py guiones); la cuenta de caracteres es la de la linea original. Solo lee."""
import io, sys
sys.stdout.reconfigure(encoding="utf-8")
for cap, n in (('cap_05', 21), ('cap_05', 41), ('cap_05', 49), ('cap_05', 51), ('cap_05', 55), ('cap_06', 61), ('cap_06', 63)):
    t = io.open('fuentes/grove_high_output/%s.md' % cap, encoding='utf-8').read().split('\n')[n - 1]
    c = t[:360].replace(chr(0x2014), ' (raya) ').replace(chr(0x2013), ' (raya) ')
    print('%s L%d (%d caracteres): %s%s' % (cap, n, len(t), c, ' [...]' if len(t) > 360 else ''))
