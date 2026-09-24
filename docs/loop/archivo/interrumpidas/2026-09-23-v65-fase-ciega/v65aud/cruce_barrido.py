# -*- coding: utf-8 -*-
"""Fase ciega de la 65: los vecinos que la aduana levanta HOY para cada una de las 20 filas
(.v65aud/vecinos_<id>.txt, de barrido_uno.py) contra (a) los pares de .v64ext/veredictos_listos.txt de
ese candidato y (b) el informe archivado con el que se escribieron (.v64aud/ para los seis de d005,
.v63aud/ para los otros catorce), senial a senial."""
import io, os, re
D005 = ['archivar_indicadores_resolver_problemas', 'construir_grafico_escalonado_pronosticos',
        'construir_indicador_tendencia_patron', 'elegir_fabricar_pedido_pronostico',
        'elegir_indicador_salida_trabajo_administrativo', 'emparejar_indicadores_efecto_contraefecto']
PAT = r'vecino (\S+)\s+\[levantada por: [^\]]+\]\n\s+similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)'
tanda = [l.split()[1] for l in io.open('.v64ext/orden.txt', encoding='utf-8') if l[:1].isdigit() and 1 <= int(l.split()[0]) <= 20]
listos = {}; cand = None
for l in io.open('.v64ext/veredictos_listos.txt', encoding='utf-8'):
    if l.startswith('## '): cand = l[3:].strip(); listos.setdefault(cand, set()); continue
    m = re.match(r'(\w+)\|', l)
    if m and cand: listos[cand].add(m.group(1))
tv = tl = ta = dl = da = ds = 0; pobs = set(); sin = []
for i in tanda:
    r = '.v65aud/vecinos_%s.txt' % i
    if not os.path.exists(r) or not io.open(r, encoding='utf-8').read().rstrip().endswith('FIN'):
        sin.append(i); continue
    t = io.open(r, encoding='utf-8').read().splitlines()
    pobs.add(re.search(r'poblacion (\d+)', t[0]).group(1))
    hoy = {}
    for l in t[1:-1]:
        c = l.split()
        hoy[c[0]] = (c[3], c[5], c[7])
    arch = '.v64aud' if i in D005 else '.v63aud'
    a = {m.group(1): m.groups()[1:] for m in re.finditer(PAT, io.open('%s/informe_%s.txt' % (arch, i), encoding='utf-8').read())}
    L = listos.get(i, set())
    tv += len(hoy)
    dif_l = (set(hoy) ^ L); dif_a = (set(hoy) ^ set(a))
    dsen = [v for v in set(hoy) & set(a) if tuple(float(x) for x in hoy[v]) != tuple(float(x) for x in a[v])]
    dl += len(dif_l); da += len(dif_a); ds += len(dsen)
    print('%-48s hoy %d | listos %d | archivo %s %d | distintos contra listos %d | contra archivo %d | seniales que difieren %d'
          % (i, len(hoy), len(L), arch, len(a), len(dif_l), len(dif_a), len(dsen)))
    for v in sorted(dif_l): print('      contra listos: %s %s' % ('SOLO HOY' if v in hoy else 'SOLO LISTOS', v))
    for v in sorted(dif_a): print('      contra archivo: %s %s' % ('SOLO HOY' if v in hoy else 'SOLO ARCHIVO', v))
    for v in sorted(dsen): print('      senial: %s hoy %s archivo %s' % (v, hoy[v], a[v]))
print('poblaciones de hoy: %s | vecinos hoy: %d | filas sin barrido terminado: %d %s' % (sorted(pobs), tv, len(sin), sin))
print('pares distintos contra listos: %d | contra archivo: %d | seniales que difieren al milesimo: %d' % (dl, da, ds))
