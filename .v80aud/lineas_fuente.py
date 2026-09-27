# -*- coding: utf-8 -*-
"""Fase ciega de la 80 (copia libre de .v77aud/lineas_fuente.py con las lineas cambiadas): las lineas del libro que
sostienen la unica arista de la tanda, las mismas que cita mi fila sellada de la 78 (.v78aud/aristas_lectura.tsv:
cap_03 L21 y L23 de Marquet), y la L19, que abre la reunion, impresas de fuentes/marquet_turn_the_ship/ tal cual y
cortadas a 600 caracteres, con el apostrofo y las comillas curvas pasados a rectos. La cuenta de caracteres es la de la
linea original. Solo lee."""
import io, sys
sys.stdout.reconfigure(encoding="utf-8")
for cap, n in (('cap_03', 19), ('cap_03', 21), ('cap_03', 23), ('cap_03', 25)):
    t = io.open('fuentes/marquet_turn_the_ship/%s.md' % cap, encoding='utf-8').read().split('\n')[n - 1]
    c = t.strip()[:600].replace(chr(0x2019), "'").replace(chr(0x201c), '"').replace(chr(0x201d), '"')
    print('%s L%d (%d caracteres): %s%s' % (cap, n, len(t), c, ' [...]' if len(t.strip()) > 600 else ''))
