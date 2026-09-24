import json,glob,re,collections
c=collections.defaultdict(lambda:[0,0,[]])
for f in sorted(glob.glob('cuarentena/marquet_turn_the_ship/*.json')):
    d=json.load(open(f,encoding='utf-8'))
    m=re.search(r'fuentes/marquet_turn_the_ship/(cap_\d+)\.md',d['resumen_teorico'])
    k=m.group(1) if m else 'SIN_ORIGEN'
    c[k][0]+=1; c[k][1]+=len(d['pasos_accionables']); c[k][2].append(d['id'])
caps=sorted(glob.glob('fuentes/marquet_turn_the_ship/cap_*.md'))
print('capitulos en fuentes:',len(caps))
tc=tp=0
for p in caps:
    import os; k=os.path.basename(p)[:-3]; n,s,_=c.get(k,[0,0,[]]); tc+=n; tp+=s
    print(k,n,s)
print('SIN_ORIGEN',c.get('SIN_ORIGEN',[0])[0]); print('TOTAL',tc,tp)
