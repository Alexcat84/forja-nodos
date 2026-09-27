# -*- coding: utf-8 -*-
"""Fase ciega de la 72 (copia de .v70aud/lineas_fuente.py con las lineas cambiadas): las lineas del libro que sostienen
las 6 aristas que mi lectura espera (.v72aud/esperado_72.py: las 2 CONTINUA de .v71aud/mis_clases.tsv y las 4 SOSTENGO
de .v71aud/aristas_lectura.tsv, con la columna 'linea' de sus filas), impresas del fichero de fuentes/grove_high_output/
tal cual y cortadas a 480 caracteres. La raya y el guion medio del libro se imprimen como '(raya)', porque la casa no
admite ninguno de los dos en sus paginas (forja.py guiones); la cuenta de caracteres es la de la linea original. Solo lee."""
import io, sys
sys.stdout.reconfigure(encoding="utf-8")
for cap, n in (('cap_07', 19), ('cap_07', 25), ('cap_07', 27), ('cap_07', 29), ('cap_07', 33), ('cap_07', 37), ('cap_07', 39), ('cap_11', 61), ('cap_11', 63)):
    t = io.open('fuentes/grove_high_output/%s.md' % cap, encoding='utf-8').read().split('\n')[n - 1]
    c = t[:480].replace(chr(0x2014), ' (raya) ').replace(chr(0x2013), ' (raya) ')
    print('%s L%d (%d caracteres): %s%s' % (cap, n, len(t), c, ' [...]' if len(t) > 480 else ''))
