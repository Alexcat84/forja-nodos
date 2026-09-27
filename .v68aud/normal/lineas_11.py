# -*- coding: utf-8 -*-
"""ACTA 67: las lineas 894 a 904 de la bitacora, una a una. Copia de .v67aud/normal/lineas_97.py con el tramo cambiado:
(1) las de veredicto contra el bloque de su candidato en .v66ext/veredictos_listos.txt de HOY (lineas # fuera);
(2) cada par contra mi barrido de la 66 (.v66aud/vecinos_tabla.txt) y contra mi clase sellada (.v66aud/mis_clases.tsv);
(3) las de arista contra las filas SOSTENGO de .v66ext/aristas_lectura.txt y contra mi .v66aud/aristas_lectura.tsv;
(4) que .v66ext/veredictos_listos.txt no cambio desde 587f1d8 (el commit de mi ACTA 66)."""
import io, json, subprocess, collections
B = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')]
nuevas = B[893:]
print('lineas en la bitacora: %d | nuevas desde la 894: %d' % (len(B), len(nuevas)))
def bloques(txt):
    d = {}; cur = None
    for l in txt.split('\n'):
        if l.startswith('## '): cur = l[3:].strip(); d[cur] = []; continue
        if cur and l.strip() and not l.startswith('#'): d[cur].append(l)
    return d
hoy_txt = io.open('.v66ext/veredictos_listos.txt', encoding='utf-8').read()
viejo_txt = subprocess.run(['git', 'show', '587f1d8:.v66ext/veredictos_listos.txt'], capture_output=True).stdout.decode('utf-8')
print('.v66ext/veredictos_listos.txt igual que en 587f1d8: %s' % (hoy_txt.replace('\r', '') == viejo_txt.replace('\r', '')))
H = bloques(hoy_txt)
barr = set()
for l in io.open('.v66aud/vecinos_tabla.txt', encoding='utf-8'):
    c = l.split()
    if len(c) > 2 and c[1] == '>': barr.add((c[0], c[2]))
MIAS = {}
for l in io.open('.v66aud/mis_clases.tsv', encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    if len(c) >= 3: MIAS[frozenset((c[0], c[1]))] = c[2]
SOST = set()
for l in io.open('.v66ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO'):
        c = [x.strip() for x in l.split('|')]; SOST.add((c[1], c[2]))
MISOST = set()
for l in io.open('.v66aud/aristas_lectura.tsv', encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    if len(c) >= 3 and c[2].startswith('SOSTENGO'): MISOST.add((c[0], c[1]))
ok = mal = 0; fuera = []; arist = []; clases = collections.Counter(); coinc = 0; disc = []
for i, l in enumerate(nuevas, 894):
    blk = H.get(l['candidato'])
    ref = [x for x in (blk or []) if x.split('|', 1)[0] == l['vecino']]
    if blk is not None and ref and not l.get('arista'):
        p = ref[0].split('|')
        if p[1] == 'CONTINUA': cl, raz = p[1], '|'.join(p[3:])
        else: cl, raz = p[1], '|'.join(p[2:])
        if l['veredicto'] == cl and l['razon'] == raz: ok += 1
        else: mal += 1; print('  DISTINTA linea %d %s ~ %s' % (i, l['candidato'], l['vecino']))
        clases[l['veredicto']] += 1
        if (l['candidato'], l['vecino']) not in barr: fuera.append((i, l['candidato'], l['vecino']))
        mia = MIAS.get(frozenset((l['candidato'], l['vecino'])))
        if mia and mia.split()[0] == l['veredicto']: coinc += 1
        else: disc.append((i, l['candidato'], l['vecino'], l['veredicto'], mia))
    else:
        arist.append((i, l))
print('lineas de veredicto: %d | iguales letra a letra a su linea preparada: %d | distintas: %d | clases: %s' % (ok + mal, ok, mal, dict(clases)))
print('pares de veredicto fuera de mi barrido de la 66: %d %s' % (len(fuera), fuera))
print('su clase igual a la mia sellada en .v66aud/mis_clases.tsv: %d | distinta o sin fila: %d %s' % (coinc, len(disc), disc))
print('lineas de arista: %d' % len(arist))
for i, l in arist:
    par = tuple(x.strip() for x in l['arista'].split('>'))
    print('  linea %d | %s > %s | veredicto %s | SOSTENGO en .v66ext: %s | SOSTENGO en mi .v66aud: %s' % (i, par[0], par[1], l['veredicto'], par in SOST, par in MISOST))
