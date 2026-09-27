# -*- coding: utf-8 -*-
"""Vuelta 72, TAREA 5: las fichas que quedan en cuarentena/grove_high_output/, por capitulo de su resumen_teorico. Solo lee."""
import glob, io, json, re, collections
c = collections.Counter(re.search(r'fuentes/grove_high_output/(cap_\d+)\.md', json.load(io.open(f, encoding='utf-8'))['resumen_teorico']).group(1)
                        for f in glob.glob('cuarentena/grove_high_output/*.json'))
print('fichas en la bandeja de grove por capitulo: %s | total %d' % (', '.join('%s %d' % kv for kv in sorted(c.items())), sum(c.values())))
