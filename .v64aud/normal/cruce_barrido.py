# -*- coding: utf-8 -*-
"""Cruza el barrido ciego COMPLETO de los seis de d005 (.v64aud/informe_<id>.txt, poblacion 462,
fichas de 997054d, identicas a las de 6e42f06) contra lo que el extractor midio par a par
(.v64ext/pares_despues.txt y matriz22_*.txt) y contra sus bloques de .v64ext/veredictos_listos.txt.
Dice: (1) si los vecinos del barrido son los del bloque, ni uno mas ni uno menos; (2) si las tres
seniales de cada par coinciden al redondeo entre las dos medidas."""
import io, re, glob
D005 = ['archivar_indicadores_resolver_problemas', 'construir_grafico_escalonado_pronosticos',
        'construir_indicador_tendencia_patron', 'elegir_fabricar_pedido_pronostico',
        'elegir_indicador_salida_trabajo_administrativo', 'emparejar_indicadores_efecto_contraefecto']
PAT = r'vecino (\S+)\s+\[levantada por: ([^\]]+)\]\n\s+similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)'
def barrido(i):
    t = io.open('.v64aud/informe_%s.txt' % i, encoding='utf-8').read()
    return {m.group(1): tuple(float(x) for x in m.groups()[2:5]) for m in re.finditer(PAT, t)}
ext = {}
for l in io.open('.v64ext/pares_despues.txt', encoding='utf-8'):
    c = l.split()
    if len(c) > 5 and c[0] in ('d005', 'd140', 'lectura', 'd141') and '/' in c[-2]:
        v = c[-2].split('/')
        try: ext[(c[1], c[2])] = tuple(float(x) for x in v)
        except ValueError: pass
for f in sorted(glob.glob('.v64ext/matriz22_*.txt')):
    for l in io.open(f, encoding='utf-8'):
        m = re.match(r'(NO LEVANTA|LEVANTA)\s+(\S+)\s+-> (\S+)\s+texto ([\d.]+) familia ([\d.]+) paso ([\d.]+)', l)
        if m: ext[(m.group(2), m.group(3))] = tuple(float(x) for x in m.groups()[3:6])
bloques, cur = {}, None
for l in io.open('.v64ext/veredictos_listos.txt', encoding='utf-8'):
    if l.startswith('## '): cur = l[3:].strip(); bloques[cur] = set()
    elif cur and '|' in l and not l.startswith('#'): bloques[cur].add(l.split('|')[0].strip())
tot = igual = difiere = sinmedida = 0
for i in D005:
    b = barrido(i)
    falta = sorted(set(b) - bloques.get(i, set())); sobra = sorted(bloques.get(i, set()) - set(b))
    print('%-48s barrido %d | bloque %d | en barrido y no en bloque %s | en bloque y no en barrido %s' % (i, len(b), len(bloques.get(i, ())), falta or 0, sobra or 0))
    for v, s in sorted(b.items()):
        tot += 1
        e = ext.get((i, v))
        if e is None: sinmedida += 1; print('    SIN MEDIDA DEL EXTRACTOR  %s' % v); continue
        if all(abs(x - y) < 0.0015 for x, y in zip(s, e)): igual += 1
        else: difiere += 1; print('    DIFIERE  %s  barrido %s  extractor %s' % (v, s, e))
print('pares del barrido: %d | seniales iguales al redondeo: %d | difieren: %d | sin medida del extractor: %d' % (tot, igual, difiere, sinmedida))
