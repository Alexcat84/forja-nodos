import glob, json, os, re
pat = re.compile(r'\b(dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce)\b', re.I)
for f in sorted(glob.glob('cuarentena/zhuo_manager/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    t = d.get('titulo','')
    hits = []
    if pat.search(t): hits.append('TITULO: ' + t)
    for i, p in enumerate(d.get('pasos_accionables', []), 1):
        for m in pat.finditer(p):
            frag = p[max(0,m.start()-70):m.start()+90].replace('\n',' ')
            hits.append('  P%d ...%s...' % (i, frag))
    if hits:
        print('==', os.path.basename(f)[:-5])
        for h in hits[:6]: print(h)
