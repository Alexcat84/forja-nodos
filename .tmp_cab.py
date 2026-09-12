import glob, json, os, re
pat = re.compile(r'cabeza|serie|D\.37|las (cuatro|cinco|seis|siete|ocho|nueve|diez|tres)\b|los (cuatro|cinco|seis|siete|ocho|nueve|diez|tres)\b', re.I)
for f in sorted(glob.glob('cuarentena/zhuo_manager/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    r = d.get('resumen_teorico','')
    for m in pat.finditer(r):
        print('%-44s ...%s...' % (d['id'], r[max(0,m.start()-90):m.start()+140].replace('\n',' ')))
