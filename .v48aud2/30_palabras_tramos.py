# -*- coding: utf-8 -*-
"""Palabras de un tramo, contadas del fichero fuente y no de ninguna tabla.
Sostiene el 47.6.a de la ACTA 47: P18 y P19 dieron nodo y son mas pobres que P36."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
L = open('fuentes/grove_high_output/cap_04.md', encoding='utf-8').read().split('\n')
def pal(a, b): return sum(len(L[i - 1].split()) for i in range(a, b + 1))
for nom, a, b in [('P18',195,201),('P19',203,213),('P36',289,289),('P38',293,301),
                  ('P34',273,285),('P39',303,307),('P41',315,315),('P42',317,317)]:
    print('%-4s L%-4d a L%-4d : %4d palabras' % (nom, a, b, pal(a, b)))
