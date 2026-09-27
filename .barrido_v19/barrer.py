import io,os,json,glob,subprocess,sys
CAP09=[l.strip() for l in io.open('.barrido_v19/cap09.txt',encoding='utf-8') if l.strip()]
grafo=[l for l in io.open('.barrido_v19/grafo.jsonl',encoding='utf-8') if l.strip()]
band=[l for l in io.open('.barrido_v19/bandejas.jsonl',encoding='utf-8') if l.strip()]
out=io.open('.barrido_v19/BARRIDO.txt','w',encoding='utf-8')
for cid in CAP09:
    ruta='cuarentena/scott_radical_candor/%s.json'%cid
    pob=list(grafo)+[l for l in band if json.loads(l).get('id')!=cid]
    io.open('.barrido_v19/pob.jsonl','w',encoding='utf-8').writelines(pob)
    env=dict(os.environ); env['FORJA_DATASET']='.barrido_v19/pob.jsonl'
    r=subprocess.run([sys.executable,'forja.py','informe',ruta],capture_output=True,env=env)
    txt=r.stdout.decode('utf-8','replace')
    i=txt.find('LA LISTA COMPLETA')
    cuerpo=txt[i:] if i>=0 else txt
    cuerpo=cuerpo.split('NADA SE INSERTO')[0]
    out.write('### %s   (contra %d de poblacion)\n'%(cid,len(pob)))
    out.write(cuerpo.rstrip()+'\n\n')
    out.flush()
    print(cid,'ok',flush=True)
out.close()
