# -*- coding: utf-8 -*-
import io, json, sys
ident = sys.argv[1]
n = {json.loads(l)['id']: json.loads(l)
     for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()}[ident]
print('===== %s | %d pasos =====' % (ident, len(n['pasos_accionables'])))
print('titulo: %s' % n['titulo'])
print('activacion: %s' % n['condiciones_activacion'])
print('entregable: %s' % n['entregable_esperado'])
print('previos: %s | siguientes: %s | atrib: %d' % (n['nodos_previos'], n['nodos_siguientes'], len(n.get('atribuciones') or [])))
for k, p in enumerate(n['pasos_accionables'], 1):
    print('  %2d. %s' % (k, p))
