# -*- coding: utf-8 -*-
"""ACTA 68 68.10: remide las dos cifras de L37 y L39 de cap_05 que mi apertura publico por .v69aud/d053_mitades.py
(caracteres y signos de interrogacion de cada linea), por otro camino. Solo lee."""
import io
L = io.open('fuentes/grove_high_output/cap_05.md', encoding='utf-8').read().split('\n')
for n in (37, 39):
    print('L%d: %d caracteres | signos de interrogacion: %d' % (n, len(L[n - 1]), L[n - 1].count('?')))
