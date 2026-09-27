# -*- coding: utf-8 -*-
# Imprime los DOS pasos de cada par nuevo, mas el titulo y el entregable de los
# dos nodos. NO imprime clase ni razon (AUDITOR_FORJA.md 1.2).
import io, json, os, re, sys
BASE = 410
def cargar():
    d = {}
    for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
        if l.strip():
            n = json.loads(l); d[n['id']] = n
    for carp in ('cuarentena/scott_radical_candor',
                 'cuarentena/_insertados/scott_radical_candor'):
        for f in os.listdir(carp):
            if f.endswith('.json'):
                n = json.load(io.open(os.path.join(carp, f), encoding='utf-8'))
                d.setdefault(n['id'], n)
    return d
N = cargar()
ver = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]
for num, v in enumerate(ver[BASE:], BASE + 1):
    if not v.get('detalle_paso'): continue
    m = re.match(r'paso (\d+) del candidato contra paso (\d+) de (.+)', v['detalle_paso'])
    a, b = int(m.group(1)), int(m.group(2))
    c, w = v['candidato'], v['vecino']
    print('===== L%d  %s  <->  %s   senales=%s  levantada_por=%s' % (
        num, c, w, json.dumps(v['senales']), v['levantada_por']))
    for lado, ident, k in (('CAND', c, a), ('VECI', w, b)):
        n = N[ident]
        print('  %s %s' % (lado, ident))
        print('       titulo     : %s' % n['titulo'])
        print('       activacion : %s' % n['condiciones_activacion'])
        print('       entregable : %s' % n['entregable_esperado'])
        print('       paso %-3d   : %s' % (k, n['pasos_accionables'][k-1]))
    print()
