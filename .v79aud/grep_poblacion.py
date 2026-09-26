# -*- coding: utf-8 -*-
"""Fase ciega de la 79: busca un patron (regex, sin distinguir mayusculas) en la POBLACION de D.38.4, el grafo
(dataset/nodos.jsonl) mas las bandejas (cuarentena/<libro>/*.json, sin _insertados, _derivadas ni ensayo_, como .v67aud/normal/pasos_ciego.py), campo a campo, y
NUNCA en nodos_previos, nodos_siguientes ni ninguna clave de relacion (R6). Imprime una linea por campo que casa, con
el tramo que casa y 60 caracteres a cada lado, y al final el reparto de los nodos que casan por sede, con su suma (R7).
Uso: python .v79aud/grep_poblacion.py "<patron>" [clave_de_libro]. Solo lee."""
import io, json, glob, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
pat = re.compile(sys.argv[1], re.I)
libro = sys.argv[2] if len(sys.argv) > 2 else None
FUERA = {'nodos_previos', 'nodos_siguientes', 'previos', 'siguientes'}
def poblacion():
    for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
        yield 'grafo', json.loads(l)
    for f in sorted(glob.glob('cuarentena/*/*.json')):
        g = f.replace('\\', '/')
        if '/_' in g or '/ensayo_' in g: continue
        yield 'bandeja', json.load(io.open(f, encoding='utf-8'))
nodos = collections.OrderedDict(); total = collections.Counter()
for sede, d in poblacion():
    total[sede] += 1
    if libro and not any(x.get('clave') == libro for x in d.get('fuentes', [])): continue
    for k, v in d.items():
        if k in FUERA: continue
        txt = json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v
        for m in pat.finditer(txt):
            a, b = max(0, m.start() - 60), min(len(txt), m.end() + 60)
            print('%s | %s | %s | ...%s...' % (d['id'], sede, k, txt[a:b].replace('\n', ' ')))
            nodos[d['id']] = sede
c = collections.Counter(nodos.values())
print('poblacion leida: %s | suma: %d' % (dict(total), sum(total.values())))
print('nodos que casan%s: %d | por sede: %s | suma: %d' % (' (solo %s)' % libro if libro else '', len(nodos), dict(c), sum(c.values())))
