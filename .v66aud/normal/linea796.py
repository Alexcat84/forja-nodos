# -*- coding: utf-8 -*-
"""ACTA 65: la unica linea nueva de la bitacora (796) contra el bloque de la fila 22 de .v64ext/veredictos_listos.txt,
campo a campo; y las claves de relacion de los dos nodos que entraron."""
import io, json
L = io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8').read().strip().split('\n')
l = json.loads(L[-1])
b = [x for x in io.open('.v64ext/veredictos_listos.txt', encoding='utf-8').read().split('\n## simplificar_trabajo_reducir_numero_pasos\n')[1].split('\n## ')[0].split('\n') if x.strip() and not x.startswith('#')]
v, c, r = b[0].split('|', 2)
print('lineas en la bitacora: %d | lineas en el bloque de la fila 22: %d' % (len(L), len(b)))
print('candidato %s | vecino igual: %s | veredicto igual: %s | razon igual letra a letra: %s | arista: %r' % (l['candidato'], l['vecino'] == v, l['veredicto'] == c, l['razon'] == r, l['arista']))
N = {json.loads(n)['id']: json.loads(n) for n in io.open('dataset/nodos.jsonl', encoding='utf-8')}
for i in ('variar_frecuencia_inspeccion_nivel_calidad', 'simplificar_trabajo_reducir_numero_pasos'):
    d = N[i]
    print(i, '| claves:', ','.join(sorted(d)))
    print('   que apuntan a otro nodo:', {k: d[k] for k in d if isinstance(d[k], (list, str)) and any(isinstance(x, str) and x in N for x in (d[k] if isinstance(d[k], list) else [d[k]]))})
