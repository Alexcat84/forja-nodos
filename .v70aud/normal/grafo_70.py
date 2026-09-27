# -*- coding: utf-8 -*-
"""Turno normal de la 70: el grafo al abrir (git show 3e52cad) contra el de hoy. Nodos nuevos contra .v68aud/los20.txt;
nodos viejos que cambian y en que campos; y TODAS las aristas que tocan a las 20 (de nodos_previos y nodos_siguientes de
cualquier nodo), par a par contra las 7 de mi lectura sellada (.v69aud/aristas_70.py), y si cada arista esta en los dos
lados (madre.siguientes y hijo.previos). Reparto con suma (R7). Solo lee."""
import io, sys, json, subprocess, collections
sys.stdout.reconfigure(encoding="utf-8")
antes = {d['id']: d for d in (json.loads(l) for l in subprocess.run(['git', 'show', '3e52cad:dataset/nodos.jsonl'], capture_output=True, text=True, encoding='utf-8').stdout.splitlines() if l.strip())}
hoy = {d['id']: d for d in (json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8'))}
los20 = set(io.open('.v68aud/los20.txt', encoding='utf-8').read().split())
nuevos = set(hoy) - set(antes)
print('nodos al abrir: %d | hoy: %d | nuevos: %d | nuevos que son mis 20: %d | desaparecidos: %d' % (len(antes), len(hoy), len(nuevos), len(nuevos & los20), len(set(antes) - set(hoy))))
cam = collections.Counter()
for i in sorted(antes):
    if i in hoy and antes[i] != hoy[i]:
        campos = sorted(k for k in set(antes[i]) | set(hoy[i]) if antes[i].get(k) != hoy[i].get(k))
        gana = sorted(set(hoy[i].get('nodos_siguientes', [])) - set(antes[i].get('nodos_siguientes', [])))
        pierde = sorted(set(antes[i].get('nodos_siguientes', [])) - set(hoy[i].get('nodos_siguientes', [])))
        cam['solo nodos_siguientes' if campos == ['nodos_siguientes'] and not pierde else 'otra cosa'] += 1
        print('  VIEJO %-56s campos %s | gana %s | pierde %s' % (i, campos, gana, pierde))
print('viejos que cambian: %s | suma: %d' % (dict(cam), sum(cam.values())))
ar = set(); lados = collections.Counter()
for i, d in hoy.items():
    for s in d.get('nodos_siguientes', []):
        if i in los20 or s in los20: ar.add((i, s))
    for p in d.get('nodos_previos', []):
        if i in los20 or p in los20: ar.add((p, i))
for m, h in sorted(ar):
    lados['en los dos lados' if (h in hoy[m].get('nodos_siguientes', []) and m in hoy[h].get('nodos_previos', [])) else 'en un solo lado'] += 1
sal = subprocess.run([sys.executable, '.v69aud/aristas_70.py'], capture_output=True, text=True, encoding='utf-8').stdout
esp = set((l.split()[1], l.split()[3]) for l in sal.splitlines() if l.startswith('  CONTINUA') or l.startswith('  SOSTENGO'))
print('aristas del grafo que tocan a las 20: %d | por lados: %s | suma: %d' % (len(ar), dict(lados), sum(lados.values())))
print('esperadas por mi lectura sellada: %d | iguales: %d | solo en el grafo: %s | solo esperadas: %s' % (len(esp), len(ar & esp), sorted(ar - esp), sorted(esp - ar)))
for m, h in sorted(ar): print('  %-56s > %s' % (m, h))
print('con madre usar_tres_clases_reunion_proceso: %d' % sum(1 for m, h in ar if m == 'usar_tres_clases_reunion_proceso'))
