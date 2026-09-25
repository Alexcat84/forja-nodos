# -*- coding: utf-8 -*-
"""ACTA 67: copia de .v67aud/normal/aristas_por_par.py. Las aristas del grafo de HOY menos las del commit de la ACTA 66
(587f1d8), por par, contra las dos SOSTENGO de mi .v66aud/aristas_lectura.tsv que APERTURA_CIEGA.md 3 esperaba; y la
simetria previos/siguientes de cada una."""
import io, json, subprocess
def aristas(lineas):
    N = {}; E = set(); S = set()
    for l in lineas:
        if not l.strip(): continue
        d = json.loads(l); N[d['id']] = d
    for i, d in N.items():
        for s in d.get('nodos_siguientes', []): E.add((i, s))
        for p in d.get('nodos_previos', []): S.add((p, i))
    return N, E, S
N0, E0, S0 = aristas(subprocess.run(['git', 'show', '587f1d8:dataset/nodos.jsonl'], capture_output=True).stdout.decode('utf-8').splitlines())
N1, E1, S1 = aristas(io.open('dataset/nodos.jsonl', encoding='utf-8').read().splitlines())
print('nodos: 587f1d8 %d | hoy %d | nuevos: %s' % (len(N0), len(N1), sorted(set(N1) - set(N0))))
print('aristas por siguientes: 587f1d8 %d | hoy %d | por previos: 587f1d8 %d | hoy %d' % (len(E0), len(E1), len(S0), len(S1)))
print('asimetricas hoy (siguientes sin previos o al reves): %d' % len(E1 ^ S1))
nuevas = sorted(E1 - E0); perdidas = sorted(E0 - E1)
print('nuevas: %d | perdidas: %d' % (len(nuevas), len(perdidas)))
esp = {('agrupar_tareas_semejantes_aprovechar_preparacion', 'agrupar_interrupciones_subordinados_reuniones_regulares'),
       ('buscar_regularidad_bloques_iguales_trabajo_mando', 'canalizar_interrupciones_cartel_hora_oficina')}
for m, h in nuevas: print('  %-9s %s > %s' % ('ESPERADA' if (m, h) in esp else 'NO ESPER', m, h))
print('esperadas por mi lectura: %d | nuevas que lo son: %d | esperadas que no estan: %s' % (len(esp), len(esp & set(nuevas)), sorted(esp - set(nuevas))))
cambiados = sorted(i for i in N0 if i in N1 and N0[i] != N1[i])
print('nodos de 587f1d8 que cambiaron: %d' % len(cambiados))
for i in cambiados:
    campos = sorted(k for k in set(N0[i]) | set(N1[i]) if N0[i].get(k) != N1[i].get(k))
    print('  %s: %s' % (i, campos))
