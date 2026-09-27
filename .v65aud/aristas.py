# -*- coding: utf-8 -*-
"""Fase ciega de la 65: las aristas que la ACTA 63 dejo adjudicadas para la tanda, contra las que viven
HOY en dataset/nodos.jsonl entre los 20 (y desde los 20 hacia fuera).
Esperadas: las filas SOSTENGO de .v64ext/aristas_lectura.txt y las lineas CONTINUA de
.v64ext/veredictos_listos.txt (madre=...), mas la de .v63ext/cmd_02_detectar.sh que QUEDA EN COLA.
Una arista madre->hijo vive como madre en nodos_previos del hijo y/o hijo en nodos_siguientes de la madre."""
import io, json, re
los22 = [l.split()[0] for l in io.open('.v64ext/los22.txt', encoding='utf-8') if l.strip() and not l.startswith('#')]
tanda = set(los22[:20])
g = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l); g[d['id']] = d
def ids(x): return [e if isinstance(e, str) else (e.get('id') or e.get('nodo')) for e in (x or [])]
vivas = set()
for i in tanda:
    for m in ids(g[i].get('nodos_previos')): vivas.add((m, i))
    for h in ids(g[i].get('nodos_siguientes')): vivas.add((i, h))
esperadas = {}
for l in io.open('.v64ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO'):
        c = [x.strip() for x in l.split('|')]; esperadas[(c[1], c[2])] = 'aristas_lectura SOSTENGO'
sec = None
for l in io.open('.v64ext/veredictos_listos.txt', encoding='utf-8'):
    if l.startswith('## '): sec = l[3:].strip(); continue
    c = l.strip().split('|')
    if len(c) > 2 and c[1] == 'CONTINUA':
        m = re.search(r'madre=([a-z0-9_]+)', l).group(1)
        h = c[0] if m == sec else sec
        esperadas.setdefault((m, h), 'veredictos_listos CONTINUA en %s' % sec)
for (m, h), de in sorted(esperadas.items()):
    print('%-9s %-48s -> %-48s (%s)' % ('VIVE' if (m, h) in vivas else 'NO VIVE', m, h, de))
extra = sorted(vivas - set(esperadas))
for m, h in extra:
    print('%-9s %-48s -> %-48s' % ('SIN ADJUDICAR', m, h))
cola = ('detectar_arreglar_fallo_etapa_menor_valor', 'supervisar_tarea_delegada_etapa_menor_valor')
print('la de cola (%s -> %s): %s' % (cola[0], cola[1], 'VIVE' if cola in vivas else 'no vive'))
print('esperadas %d | viven %d | no viven %d | vivas sin adjudicar %d' % (len(esperadas), len([e for e in esperadas if e in vivas]), len([e for e in esperadas if e not in vivas]), len(extra)))
