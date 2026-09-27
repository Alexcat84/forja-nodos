# -*- coding: utf-8 -*-
"""Fase ciega de la 75: para cada coincidencia del grep R9 de .v75aud/cap13_despues.py, el tramo LITERAL del libro que
sostiene la clausula, buscado con un patron en la linea que mi fila de fidelidad le da en fuentes/scott_radical_candor/cap_13.md.
Una fila por coincidencia, en el orden del grep. Los patrones los escribo yo leyendo la linea; si un patron no encuentra nada, sale 'NADA' y la fila seria P (R9). El
apostrofo curvo se pasa a recto. Reparte con su suma (R7). Solo lee."""
import io, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
libro = [l.rstrip('\n').replace('’', "'") for l in io.open('fuentes/scott_radical_candor/cap_13.md', encoding='utf-8')]
C = [('contar_cuatro 4, demuestras', 45, r"you are demonstrating self-awareness and humility"),
     ('contar_cuatro 8, mejor que', 49, r"Your story is by definition better than the story Kim tells"),
     ('contar_cuatro 13, en cambio', 53, r"but you instead talked to others"),
     ('contar_cuatro 15, compartelas', 55, r"share them"),
     ('dar_elogio 1, mas que el freno', 251, r"use your accelerator more than your brake"),
     ('dar_elogio 1, y si no usas', 251, r"If you never use your brake"),
     ('dar_elogio 2, no demostrar', 267, r"not to prove how smart you are"),
     ('dar_elogio 4, en vez de comparaciones', 269, r"rather than making odious comparisons"),
     ('dar_elogio 10, y no solo agradable', 273, r"Giving praise doesn't just make people feel good, it's practical"),
     ('dar_elogio 10, demuestra que te importa', 273, r"Praise shows that you care personally"),
     ('dar_elogio 15, compartid', 283, r"share one specific piece of praise"),
     ('medir_critica 1, no se mide', 291, r"measured not at your mouth"),
     ('medir_critica 1, sino en el oido', 291, r"but at the other person's ear"),
     ('medir_critica 6, importa mas que', 297, r"The way you listen is more important than the way you talk"),
     ('medir_critica 7, mide la respuesta', 297, r"gauge the other person's response"),
     ('medir_critica 20, si en cambio', 309, r"Other times.{0,80}?they just don't hear you"),
     ('medir_critica 26, prueba a preguntar', 315, r"Another thing that can help.{0,80}?is to ask"),
     ('medir_critica 28, prueba con', 315, r"Or you can try saying"),
     ('medir_critica 33, compartir', 321, r"share")]
c = collections.Counter()
for q, n, p in C:
    m = re.search(p, libro[n - 1]); c['tramo hallado' if m else 'NADA'] += 1
    print('  %-42s L%d: %s' % (q, n, m.group(0) if m else 'NADA'))
print('coincidencias del grep R9 con su tramo literal: %s | suma: %d' % (dict(c), sum(c.values())))
