# -*- coding: utf-8 -*-
# LA ARITMETICA DE MI PROPIA LECTURA. Lo tecleado en .v3g/mi_clase.tsv son MIS
# VEREDICTOS, que no son dato y no se pueden casar. Los DENOMINADORES no se
# teclean: el numero de pasos de cada candidato y su capitulo salen del fichero
# del candidato, igual que en .v3g/pasos_por_capitulo.py.
import io, json, glob, os, re, collections

RUTA = re.compile(r'fuentes/([a-z0-9_]+)/(cap_\d\d)\.md')
libro = 'grove_high_output'

datos = {}
for p in glob.glob('cuarentena/%s/*.json' % libro):
    d = json.load(io.open(p, encoding='utf-8'))
    caps = sorted(set(m.group(2) for m in RUTA.finditer(d.get('resumen_teorico', ''))
                      if m.group(1) == libro))
    datos[d['id']] = (len(d.get('pasos_accionables', [])), caps[0] if len(caps) == 1 else '?')

filas = []
for n, linea in enumerate(io.open('.v3g/mi_clase.tsv', encoding='utf-8')):
    partes = linea.rstrip('\n').rstrip('\r').split('\t')
    if n == 0 or not partes[0].strip():
        continue
    ident = partes[0].strip()
    clase = partes[1].strip()
    puentes = [x for x in (partes[2].strip().split(',') if len(partes) > 2 and partes[2].strip() else [])]
    filas.append((ident, clase, puentes))

faltan = sorted(set(datos) - set(f[0] for f in filas))
sobran = sorted(set(f[0] for f in filas) - set(datos))
print('candidatos en la bandeja                 : %d' % len(datos))
print('candidatos con clase escrita por mi      : %d' % len(filas))
print('en la bandeja y SIN mi clase             : %d %s' % (len(faltan), faltan or ''))
print('con mi clase y NO en la bandeja          : %d %s' % (len(sobran), sobran or ''))
print()
clases = collections.Counter(f[1] for f in filas)
for k in sorted(clases):
    print('  %-24s %d' % (k, clases[k]))
print()
pasos_cap = collections.Counter()
puente_cap = collections.Counter()
nodos_cap = collections.Counter()
for ident, clase, puentes in filas:
    n, cap = datos[ident]
    pasos_cap[cap] += n
    nodos_cap[cap] += 1
    puente_cap[cap] += len(puentes)
    if len(puentes) > n:
        print('  AVISO: %s dice %d puentes sobre %d pasos' % (ident, len(puentes), n))
print('PASOS INVENTADOS POR CAPITULO, SEGUN MI PROPIA RELECTURA CIEGA')
print('  %-8s %6s %8s %8s %10s' % ('cap', 'nodos', 'pasos', 'PUENTE', 'por ciento'))
for cap in sorted(pasos_cap):
    print('  %-8s %6d %8d %8d %9.2f' % (cap, nodos_cap[cap], pasos_cap[cap],
                                        puente_cap[cap],
                                        100.0 * puente_cap[cap] / pasos_cap[cap]))
tp, tb = sum(pasos_cap.values()), sum(puente_cap.values())
print('  %-8s %6d %8d %8d %9.2f' % ('TOTAL', sum(nodos_cap.values()), tp, tb,
                                    100.0 * tb / tp))
