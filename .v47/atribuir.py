import json,glob,os,re,unicodedata
def norm(s):
    s=unicodedata.normalize('NFD',s.lower())
    s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9 ]',' ',s)
caps={}
for f in sorted(glob.glob('fuentes/grove_high_output/cap_*.md')):
    caps[os.path.basename(f)[:-3]]=set(norm(open(f,encoding='utf-8').read()).split())
STOP=set('el la los las de del que y a en un una por con para se su sus lo al es son o como mas no si ya sin sobre entre cuando cada este esta ese esa pon mira haz'.split())
print(f"{'candidato':<48} {'mejor':<8} {'2o':<8}  reparto (solapamiento lexico de titulo+pasos)")
tally={}
for f in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    d=json.load(open(f,encoding='utf-8'))
    txt=d.get('titulo','')+' '+' '.join(d.get('pasos_accionables') or [])+' '+d.get('entregable_esperado','')
    w=set(norm(txt).split())-STOP
    w={x for x in w if len(x)>4}
    sc={c:len(w&v)/max(1,len(w)) for c,v in caps.items()}
    top=sorted(sc.items(),key=lambda x:-x[1])[:2]
    tally[top[0][0]]=tally.get(top[0][0],0)+1
    print(f"{os.path.basename(f)[:-5]:<48} {top[0][0]:<8} {top[1][0]:<8}  {top[0][1]:.3f} / {top[1][1]:.3f}")
print()
print("reparto por capitulo ganador:", dict(sorted(tally.items())))
