# -*- coding: utf-8 -*-
"""LA TANDA DE LA VUELTA 26, CONTADA DE SUS PROPIAS SALIDAS.

No teclea ninguna celda: abre los .v26/ins_*.txt que la aduana escribio en esta
vuelta y cuenta pasadas, vecinos y veredictos de cada candidato. La tabla del
reporte se pega de aqui (D.41).
"""
import glob, io, os, re

pasadas = {}
for ruta in sorted(glob.glob('.v26/ins_*.txt')):
    texto = io.open(ruta, encoding='utf-8').read()
    m = re.search(r"ADUANA DE INSERCION, candidato '([^']+)'", texto)
    if not m:
        continue
    ident = m.group(1)
    d = pasadas.setdefault(ident, {'pasadas': 0, 'vecinos': 0, 'veredictos': 0,
                                   'dentro': False, 'rechazos': 0, 'aristas': 0})
    d['pasadas'] += 1
    v = re.search(r'VECINOS POR ENCIMA DE UMBRAL: (\d+)', texto)
    if v:
        d['vecinos'] = max(d['vecinos'], int(v.group(1)))
    w = re.search(r'veredictos en bitacora/VEREDICTOS\.jsonl: (\d+)', texto)
    if w:
        d['veredictos'] = int(w.group(1))
    if 'NODO INSERTADO en dataset/nodos.jsonl' in texto:
        d['dentro'] = True
    if texto.startswith('ADUANA') and 'RECHAZADO:' in texto:
        d['rechazos'] += 1
    d['aristas'] += texto.count('arista madre-hijo cableada')

orden = ['decidir_momento_despedir_persona', 'despedir_persona_franqueza_radical',
         'reconocer_recompensar_gente_estable', 'retar_superestrellas_equipo_constantemente',
         'retirar_etiquetas_permanentes_equipo', 'revisar_cinco_causas_mal_desempenio',
         'subir_vara_calidad_equipo']
orden = [i for i in orden if i in pasadas] + [i for i in sorted(pasadas) if i not in orden]

print('| # | candidato | pasadas | vecinos leidos | veredictos | aristas | como acaba |')
print('|---:|---|---:|---:|---:|---:|---|')
tp = tv = tw = ta = 0
for n, ident in enumerate(orden, 1):
    d = pasadas[ident]
    tp += d['pasadas']; tv += d['vecinos']; tw += d['veredictos']; ta += d['aristas']
    print('| %d | `%s` | **%d** | %d | **%d** | %d | %s |'
          % (n, ident, d['pasadas'], d['vecinos'], d['veredictos'], d['aristas'],
             '**DENTRO**' if d['dentro'] else '**EN COLA**'))
print('| | **TOTAL** | **%d** | **%d** | **%d** | **%d** | **%d de %d DENTRO** |'
      % (tp, tv, tw, ta, sum(1 for i in orden if pasadas[i]['dentro']), len(orden)))
