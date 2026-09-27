# -*- coding: utf-8 -*-
"""Fase ciega de la 74, R7 sobre el libro mayor: corre .v60aud/libro_mayor_cap13.py sin tocarlo (su salida se tira), toma
sus nodos de cap_13 con sus pasos (sobre dataset/nodos.jsonl y cuarentena/) y su tabla de firmas, y reparte los pasos en
dos clases con el mismo predicado (firmado por alguna acta, o sin firma de nadie), con la suma. Y los que quedan sin firma,
con sus pasos, contra las filas de mi fidelidad de esta fase (.v74aud/fidelidad_fuente.txt). Solo lee."""
import io, os, sys, runpy, collections, contextlib
sys.stdout.reconfigure(encoding='utf-8')
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path('.v60aud/libro_mayor_cap13.py')
pasos, firmas = g['pasos'], g['FIRMAS']
c = collections.Counter(); sin = {}
for k, (n, sede) in pasos.items():
    clase = 'con firma' if k in firmas else 'sin firma'
    c[clase] += n
    if clase == 'sin firma': sin[k] = n
print('pasos de cap_13 por firma: %s | suma: %d | nodos: %d' % (dict(sorted(c.items())), sum(c.values()), len(pasos)))
mias = collections.Counter(l.split('|')[0] for l in io.open('.v74aud/fidelidad_fuente.txt', encoding='utf-8') if l.strip())
for k in sorted(sin): print('  sin firma: %-52s %3d pasos | mis filas: %3d%s' % (k, sin[k], mias[k], '' if mias[k] == sin[k] else '  DESCUADRE'))
print('mis filas sobre los sin firma: %d de %d' % (sum(mias[k] for k in sin), sum(sin.values())))
