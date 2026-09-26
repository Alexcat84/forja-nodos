# -*- coding: utf-8 -*-
"""Fase ciega de la 77 (copia de .v75aud/lineas_fuente.py con las lineas cambiadas): las lineas del libro que sostienen
las dos piezas que la ACTA 75 75.4 mando a relectura conjunta, las mismas que citan mis filas selladas de la 76
(.v76aud/mis_clases.tsv y aristas_lectura.tsv): el par de la contratacion (cap_18 L117, L119, L245, L247, L267 y L269) y la
arista de fingir a recorrer (cap_11 L35; cap_13 L21, L39 y L41), impresas del fichero de fuentes/gerber_emyth/ tal cual y
cortadas a 480 caracteres. La raya y el guion medio del libro se imprimen como '(raya)', porque la casa no admite
ninguno de los dos en sus paginas (forja.py guiones); la cuenta de caracteres es la de la linea original. Solo lee."""
import io, sys
sys.stdout.reconfigure(encoding="utf-8")
for cap, n in (('cap_18', 117), ('cap_18', 119), ('cap_18', 245), ('cap_18', 247), ('cap_18', 267), ('cap_18', 269),
               ('cap_11', 35), ('cap_13', 21), ('cap_13', 39), ('cap_13', 41)):
    t = io.open('fuentes/gerber_emyth/%s.md' % cap, encoding='utf-8').read().split('\n')[n - 1]
    c = t[:480].replace(chr(0x2014), ' (raya) ').replace(chr(0x2013), ' (raya) ')
    print('%s L%d (%d caracteres): %s%s' % (cap, n, len(t), c, ' [...]' if len(t) > 480 else ''))
