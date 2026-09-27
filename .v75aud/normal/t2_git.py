# ACTA 74: la TAREA 2 por git, lo que .v75ext/t2_despues.py mide contra el arbol de trabajo y no se puede volver a correr:
# el grafo en 32531227 (antes de la TAREA 2) contra el de 4a5d2b2d (su commit), nodo a nodo y campo a campo.
import json, subprocess
def grafo(h):
    t = subprocess.run(['git', 'show', h + ':dataset/nodos.jsonl'], capture_output=True).stdout.decode('utf-8')
    return {d['id']: d for d in map(json.loads, t.splitlines())}
A, B = grafo('32531227'), grafo('4a5d2b2d')
cambian = {i: sorted(k for k in set(A[i]) | set(B[i]) if A[i].get(k) != B[i].get(k)) for i in A if i in B and A[i] != B[i]}
print('nodos antes: %d | despues: %d | nuevos: %d | que desaparecen: %d | que cambian: %d %s' % (len(A), len(B), len(set(B) - set(A)), len(set(A) - set(B)), len(cambian), cambian))
i = 'dar_elogio_disciplina_igual_critica'
print('pasos antes %d | despues %d | el resumen viejo entero al principio del nuevo: %s | caracteres %d > %d' % (
    len(A[i]['pasos_accionables']), len(B[i]['pasos_accionables']), B[i]['resumen_teorico'].startswith(A[i]['resumen_teorico']),
    len(A[i]['resumen_teorico']), len(B[i]['resumen_teorico'])))
v = A[i]['pasos_accionables']
print('los de despues son los de antes sin el 8 y sin el 17: %s' % (B[i]['pasos_accionables'] == [p for k, p in enumerate(v, 1) if k not in (8, 17)]))
