# -*- coding: utf-8 -*-
"""Fase ciega de la 72 (copia libre de .v70aud/esperado_70.py con la tanda de la 71): lo que MI lectura sellada de la 71
espera que la insercion de las 20 deje, contado con el mismo predicado y con su suma (R7). No lee el grafo por dentro, ni
la bitacora por dentro, ni nada del extractor.
(1) lineas de veredicto: una por fila dirigida de mi barrido (.v71aud/vecinos_tabla.txt, 'X > Y') cuyo candidato es de
    las 20, porque la poblacion de hoy es la de ese barrido (.v72aud/huellas_hoy.py, grafo_sin_tanda.py), repartidas por
    la clase de su par en .v71aud/mis_clases.tsv CON LA CORRECCION DE LA ACTA 70 70.5 APLICADA AQUI Y DECLARADA: los dos
    pares de cerrar_brecha_dos_preguntas_estrategia con examinar_demanda_entorno_dos_marcos_temporales y con
    determinar_estado_presente_capacidades_proyectos_merma, que selle CONTINUA, se adjudicaron SANO (D71.12);
(2) aristas: las CONTINUA que quedan de (1) y las SOSTENGO de .v71aud/aristas_lectura.tsv; las SOSTENGO van con
    python forja.py arista, que escribe su propia linea en la bitacora (src/arista.py), y las CONTINUA ya estan dentro de
    las lineas de (1);
(3) de esas aristas, cuantas madres o hijos no son de las 20: son los nodos viejos que la tanda tendria que reescribir.
Y la cuenta de hoy de la bitacora, solo con wc: 1027 era la de mi ACTA 70 70.1. Solo lee."""
import io, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
los20 = set(io.open('.v71aud/los20.txt', encoding='utf-8').read().split())
CB = 'cerrar_brecha_dos_preguntas_estrategia'
CORR = set(tuple(sorted((CB, x))) for x in ('examinar_demanda_entorno_dos_marcos_temporales', 'determinar_estado_presente_capacidades_proyectos_merma'))
cl = {}
for l in list(io.open('.v71aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t'); p = tuple(sorted((f[0], f[1])))
    cl[p] = ('SANO', '') if p in CORR else (f[2], f[3])
print('pares con la correccion de la ACTA 70 70.5 aplicada: %d' % sum(1 for p in cl if p in CORR))
fd = collections.Counter(); dc = collections.Counter(); filas = []
for l in io.open('.v71aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m and m.group(1) in los20:
        fd['vecino en la tanda' if m.group(2) in los20 else 'vecino fuera de la tanda'] += 1
        dc[cl.get(tuple(sorted(m.groups())), ('SIN FILA',))[0]] += 1; filas.append(m.groups())
print('filas dirigidas de mi barrido con candidato de las 20: %d | por vecino: %s | suma: %d' % (len(filas), dict(fd), sum(fd.values())))
print('lineas de veredicto esperadas, por la clase de su par: %s | suma: %d' % (dict(dc), sum(dc.values())))
ar = []
for p, (c, madre) in sorted(cl.items()):
    if c == 'CONTINUA': ar.append(('CONTINUA', madre, p[1] if p[0] == madre else p[0]))
for f in [l.rstrip('\n').split('\t') for l in io.open('.v71aud/aristas_lectura.tsv', encoding='utf-8')][1:]:
    if f[2].startswith('SOSTENGO'): ar.append(('SOSTENGO ' + f[2].split()[1].rstrip(','), f[0], f[1]))
k = collections.Counter(a[0].split()[0] for a in ar)
print('aristas esperadas: %d | por origen: %s | suma: %d' % (len(ar), dict(k), sum(k.values())))
for a in ar: print('  %-13s %s > %s' % a)
print('extremos de esas aristas que no son de las 20: %d' % sum((a[1] not in los20) + (a[2] not in los20) for a in ar))
esp = 1027 + len(filas) + k['SOSTENGO']
hoy = sum(1 for _ in open('bitacora/VEREDICTOS.jsonl', 'rb'))
print('bitacora esperada: 1027 + %d + %d = %d | hoy (lineas): %d | %s' % (len(filas), k['SOSTENGO'], esp, hoy, 'IGUAL' if esp == hoy else 'DISTINTA'))
