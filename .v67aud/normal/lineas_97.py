# -*- coding: utf-8 -*-
"""ACTA 66: las lineas 797 a 893 de la bitacora, una a una.
(1) las de veredicto contra el bloque de su candidato en .v66ext/veredictos_listos.txt de HOY (lineas # fuera), campo a campo;
(2) cada par (candidato, vecino) contra mi barrido de la 66 (.v66aud/vecinos_tabla.txt);
(3) las de arista contra las filas SOSTENGO de .v66ext/aristas_lectura.txt;
(4) que .v66ext/veredictos_listos.txt de hoy, sin las lineas #, es el de d8f4e2a salvo las lineas corregidas, y que cada
    linea vieja cambiada sigue encima como comentario # vuelta 67."""
import io, json, subprocess, collections
B = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')]
nuevas = B[796:]
print('lineas en la bitacora: %d | nuevas desde la 797: %d' % (len(B), len(nuevas)))
def bloques(txt):
    d = {}; cur = None
    for l in txt.split('\n'):
        if l.startswith('## '): cur = l[3:].strip(); d[cur] = []; continue
        if cur and l.strip() and not l.startswith('#'): d[cur].append(l)
    return d
hoy_txt = io.open('.v66ext/veredictos_listos.txt', encoding='utf-8').read()
viejo_txt = subprocess.run(['git', 'show', 'd8f4e2a:.v66ext/veredictos_listos.txt'], capture_output=True).stdout.decode('utf-8')
H = bloques(hoy_txt); V = bloques(viejo_txt)
cambiadas = [(c, l) for c in V for l in V[c] if l not in H.get(c, [])]
comentadas = [l for l in hoy_txt.split('\n') if l.startswith('# vuelta 67')]
print('lineas de d8f4e2a que ya no estan vivas hoy: %d | de ellas con su comentario # vuelta 67 encima: %d' % (
    len(cambiadas), sum(1 for c, l in cambiadas if any(x.endswith(l) for x in comentadas))))
print('bloques en d8f4e2a: %d | hoy: %d | lineas vivas en d8f4e2a: %d | hoy: %d' % (len(V), len(H), sum(map(len, V.values())), sum(map(len, H.values()))))
barr = set()
for l in io.open('.v66aud/vecinos_tabla.txt', encoding='utf-8'):
    c = l.split()
    if len(c) > 2 and c[1] == '>': barr.add((c[0], c[2]))
SOST = set()
for l in io.open('.v66ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO'):
        c = [x.strip() for x in l.split('|')]; SOST.add((c[1], c[2]))
ok = mal = 0; fuera_barrido = []; arist = []; cands = collections.Counter(); clases = collections.Counter()
for i, l in enumerate(nuevas, 797):
    blk = H.get(l['candidato'])
    ref = [x for x in (blk or []) if x.split('|', 1)[0] == l['vecino']]
    if blk is not None and ref:
        p = ref[0].split('|')
        if p[1] == 'CONTINUA': v, cl, madre, raz = p[0], p[1], p[2][6:], '|'.join(p[3:])
        else: v, cl, madre, raz = p[0], p[1], '', '|'.join(p[2:])
        igual = l['veredicto'] == cl and l['razon'] == raz
        esp_ar = ('%s > %s' % (madre, l['candidato'] if madre != l['candidato'] else l['vecino'])) if madre else ''
        if igual: ok += 1
        else: mal += 1; print('  DISTINTA linea %d %s ~ %s' % (i, l['candidato'], l['vecino']))
        cands[l['candidato']] += 1; clases[l['veredicto']] += 1
        if (l['candidato'], l['vecino']) not in barr: fuera_barrido.append((i, l['candidato'], l['vecino']))
    else:
        arist.append((i, l))
print('lineas de veredicto: %d | iguales letra a letra a su linea preparada: %d | distintas: %d' % (ok + mal, ok, mal))
print('candidatos con lineas: %d | lineas por candidato suman %d | clases: %s' % (len(cands), sum(cands.values()), dict(clases)))
print('pares de veredicto fuera de mi barrido de la 66: %d %s' % (len(fuera_barrido), fuera_barrido))
print('lineas que no son de veredicto preparado: %d' % len(arist))
for i, l in arist:
    par = tuple(x.strip() for x in l['arista'].split('>')) if l['arista'] else ()
    print('  linea %d | %s ~ %s | veredicto %s | arista %r | SOSTENGO en aristas_lectura: %s' % (i, l['candidato'], l['vecino'], l['veredicto'], l['arista'], par in SOST))
