# -*- coding: utf-8 -*-
# PRIMERA LINEA, D.40 HEREDADO 4: CERO IDS TECLEADOS. Los nodos que se comparan
# salen de `git show 74ddc8c:dataset/nodos.jsonl` contra el fichero de hoy; la
# diferencia la calcula el propio recorrido.
import io, json, subprocess, sys

def cargar_texto(t):
    return {json.loads(l)['id']: json.loads(l) for l in t.split('\n') if l.strip()}

antes = cargar_texto(subprocess.check_output(
    ['git', 'show', '74ddc8c:dataset/nodos.jsonl']).decode('utf-8'))
hoy = cargar_texto(io.open('dataset/nodos.jsonl', encoding='utf-8').read())

print('nodos antes (74ddc8c): %d   nodos hoy (HEAD): %d' % (len(antes), len(hoy)))
nuevos = [i for i in hoy if i not in antes]
print('ids NUEVOS: %d' % len(nuevos))
for i in nuevos: print('  + %s' % i)
def aristas(d):
    return sum(len(n.get('nodos_siguientes') or []) for n in d.values()), \
           sum(len(n.get('nodos_previos') or []) for n in d.values())
print('aristas por SIGUIENTES/PREVIOS antes: %s   hoy: %s' % (aristas(antes), aristas(hoy)))
print('--- nodos preexistentes que CAMBIARON ---')
for i in sorted(antes):
    if i in hoy and json.dumps(antes[i], sort_keys=True) != json.dumps(hoy[i], sort_keys=True):
        print('  ~ %s' % i)
        for campo in sorted(set(list(antes[i]) + list(hoy[i]))):
            a, b = antes[i].get(campo), hoy[i].get(campo)
            if a != b:
                print('      campo %s' % campo)
                print('        antes: %s' % json.dumps(a, ensure_ascii=False)[:400])
                print('        hoy  : %s' % json.dumps(b, ensure_ascii=False)[:400])
