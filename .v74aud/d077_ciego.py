# -*- coding: utf-8 -*-
"""Fase ciega de la 74, d077: las fichas de la tanda 58 por instrumento (los nombres de .v58ext/informe_<n>_<id>.txt, que
es lo que cita d077), donde vive cada una hoy (grafo, bandeja de Grove, _insertados), su huella de hoy contra la mia de la
fase ciega de la 73 (.v73aud/huellas_al_barrer.txt), y que carpetas de vuelta de la casa traen un barrido suyo por nombre
(barrido_<id>.txt o vecinos_<id>.json), con la fecha del fichero. NO mira .v74ext/, que es la vuelta que audito. Solo lee."""
import io, os, re, glob, json, hashlib, time, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
ids = [re.match(r'informe_\d+_(.*)\.txt$', os.path.basename(f)).group(1) for f in sorted(glob.glob('.v58ext/informe_*.txt'))]
grafo = set(json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl', encoding='utf-8'))
viejo = {}
for l in io.open('.v73aud/huellas_al_barrer.txt', encoding='utf-8'):
    h, f = l.strip().split(' *', 1); viejo[f] = h
c = collections.Counter()
for i in ids:
    b = 'cuarentena/grove_high_output/%s.json' % i
    ins = 'cuarentena/_insertados/grove_high_output/%s.json' % i
    sede = ('GRAFO' if i in grafo else '') + (' BANDEJA' if os.path.exists(b) else '') + (' _insertados' if os.path.exists(ins) else '')
    c[sede.strip()] += 1
    print('===== %s | hoy en: %s' % (i, sede.strip()))
    if os.path.exists(b):
        h = hashlib.sha1(open(b, 'rb').read()).hexdigest()
        print('  huella de hoy contra .v73aud/huellas_al_barrer.txt: %s' % ('IGUAL' if viejo.get(b) == h else 'DISTINTA o no estaba'))
    fs = [f.replace(chr(92), '/') for f in glob.glob('.v*/**/*%s*' % i, recursive=True)]
    fs = sorted(f for f in fs if not f.startswith('.v74ext') and re.search(r'/(barrido_|vecinos_)', f))
    for f in fs: print('  %s  %s' % (time.strftime('%Y-%m-%d %H:%M', time.localtime(os.path.getmtime(f))), f))
print('las fichas de la tanda 58 por sede de hoy: %s | suma: %d' % (dict(c), sum(c.values())))
