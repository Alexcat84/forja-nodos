import io,os,glob,subprocess,sys
nuevos=[l.strip() for l in io.open('.barrido_v18/faltan.txt',encoding='utf-8') if l.strip()]
lineas=sorted(glob.glob('.barrido_v18/*.line'))
grafo=[l for l in io.open('dataset/nodos.jsonl',encoding='utf-8') if l.strip()]
out=io.open('.barrido_v18/BARRIDO_RESTO.txt','w',encoding='utf-8')
for f in nuevos:
    me=os.path.basename(f)
    pob=list(grafo)
    for p in lineas:
        if os.path.basename(p)==me+'.line': continue
        pob.append(io.open(p,encoding='utf-8').read())
    io.open('.barrido_v18/pob2.jsonl','w',encoding='utf-8').writelines(pob)
    env=dict(os.environ); env['FORJA_DATASET']='.barrido_v18/pob2.jsonl'
    r=subprocess.run([sys.executable,'forja.py','informe',f],capture_output=True,env=env)
    txt=r.stdout.decode('utf-8','replace')
    i=txt.find('LA LISTA COMPLETA')
    cuerpo=txt[i:] if i>=0 else txt
    cuerpo=cuerpo.split('NADA SE INSERTO')[0]
    out.write('### %s   (contra %d titulos)\n'%(me[:-5],len(pob)))
    out.write('\n'.join(cuerpo.split('\n')[2:]).rstrip()+'\n\n')
    out.flush()
    print(me,'ok',flush=True)
out.close()
