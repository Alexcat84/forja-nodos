# veredicto de aduana, poblacion y vecinos de cada informe de .v63ciega/
import glob,io,re,os
for p in sorted(glob.glob('.v63ciega/informe_*.txt')):
    t=io.open(p,encoding='utf-8',errors='replace').read()
    if not t.strip(): continue
    pob=re.search(r'poblacion del barrido\s*:\s*(\d+)',t)
    v=re.search(r'\[(ENTRARIA|BLOQUEARIA|CAERIA|CHOCA)[^\]]*\]\s+(\S+)',t)
    vec=re.findall(r'vecino (\S+)\s+\[levantada por: ([^\]]+)\]\s+similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)',t)
    print('%s %s pob=%s vecinos=%d' % (v.group(1) if v else '?', v.group(2) if v else os.path.basename(p), pob.group(1) if pob else '?', len(vec)))
    for x in vec: print('    %s  [%s] sim %s fam %s paso %s' % x)
