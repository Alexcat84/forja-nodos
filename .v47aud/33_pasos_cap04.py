import json, glob, re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
tot = 0; filas=[]
for f in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    m = re.search(r'UNIDAD DE ORIGEN:\s*fuentes/grove_high_output/(cap_\d+)', d.get('resumen_teorico',''))
    if not m or m.group(1) != 'cap_04': continue
    n = len(d['pasos_accionables'])
    filas.append((d['id'], n)); tot += n
for i,(nom,n) in enumerate(sorted(filas),1):
    print('%2d. %3d  %s' % (i, n, nom))
print('---')
print('fichas de cap_04: %d   pasos: %d' % (len(filas), tot))
