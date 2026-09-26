# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 77 de .v75ext/nodos_viejos.py (encargo de la 77, TAREA 4.6). Lo cambiado, y nada mas: la apertura, 70a827c (77.0); la tanda, las filas 1 a 22 de .v76ext/orden.txt; y el rotulo de la ultima linea. La etiqueta TAREA 2 de la 75 queda, y en la 77 no puede salir: la TAREA 2 de la 77 no toco el grafo. Lo que decia la de la 75: COPIA DE LA VUELTA 75 (encargo de la 75, TAREA 4.4): la apertura cambiada a 9a5151a (75.0, antes de la TAREA 2), la tanda a las filas 1 a 7 de .v73ext/orden.txt, y una etiqueta mas, TAREA 2, para dar_elogio_disciplina_igual_critica si cambia solo en pasos_accionables y resumen_teorico, que no cuenta como cambio fuera. Lo que decia la de la 72: Vuelta 72, encargo TAREA 4 (COPIA de .v70ext/nodos_viejos.py con la apertura cambiada a 4c7a838, 72.0, y la tanda a .v71ext/orden.txt):
que ningun nodo viejo cambio fuera del nodos_siguientes de sus madres. Compara dataset/nodos.jsonl en 4c7a838 contra el de hoy: para cada nodo que ya estaba, los campos que
cambian; y si cambia nodos_siguientes, que solo GANA hijos, y que cada hijo ganado es de las filas 1 a 20 de .v71ext/orden.txt.
Y que los nodos nuevos son exactamente esas 20 filas."""
import io, json, re, subprocess
antes = dict((d['id'], d) for d in (json.loads(l) for l in subprocess.run(['git', 'show', '70a827c:dataset/nodos.jsonl'],
         capture_output=True, text=True, encoding='utf-8').stdout.splitlines() if l.strip()))
hoy = dict((d['id'], d) for d in (json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()))
tanda = [l.split()[1] for l in io.open('.v76ext/orden.txt', encoding='utf-8') if re.match(r'^\d+\s', l)][0:22]
cambian = 0; fuera = 0
for i, a in sorted(antes.items()):
    b = hoy.get(i)
    if b is None:
        print('DESAPARECE  %s' % i); fuera += 1; continue
    campos = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
    if not campos: continue
    cambian += 1
    gana = [h for h in (b.get('nodos_siguientes') or []) if h not in (a.get('nodos_siguientes') or [])]
    pierde = [h for h in (a.get('nodos_siguientes') or []) if h not in (b.get('nodos_siguientes') or [])]
    ok = campos == ['nodos_siguientes'] and not pierde and all(h in tanda for h in gana)
    t2 = i == 'dar_elogio_disciplina_igual_critica' and campos == ['pasos_accionables', 'resumen_teorico']
    if not ok and not t2: fuera += 1
    print('%-10s %-56s campos %s | gana %s | pierde %s' % ('SOLO MADRE' if ok else ('TAREA 2' if t2 else 'FUERA'), i, campos, gana, pierde))
nuevos = sorted(set(hoy) - set(antes))
print('nodos al abrir: %d | hoy: %d | nuevos: %d | nuevos que son de las 22 filas: %d | viejos que cambian: %d | cambios fuera de nodos_siguientes de una madre y de la TAREA 2: %d'
      % (len(antes), len(hoy), len(nuevos), sum(1 for n in nuevos if n in tanda), cambian, fuera))
