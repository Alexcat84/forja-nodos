import json,io,sys,os
def esc(s): return s
def mk(d):
    p='cuarentena/scott_radical_candor/%s.json'%d['id']
    d.setdefault('dominio','gestion_equipos'); d.setdefault('estado','vivo')
    d.setdefault('fuentes',[{"clave":"scott_radical_candor","fecha":"2026-09-12"}])
    d.setdefault('ids_alias',[]); d.setdefault('nodos_previos',[])
    d.setdefault('nodos_siguientes',[]); d.setdefault('atribuciones',[])
    o={}
    for k in ['id','titulo','denominaciones','condiciones_activacion','entregable_esperado',
              'pasos_accionables','resumen_teorico','dominio','estado','fuentes','ids_alias',
              'nodos_previos','nodos_siguientes','atribuciones']:
        o[k]=d[k]
    io.open(p,'w',encoding='utf-8',newline='').write(json.dumps(o,ensure_ascii=False,indent=2)+"\n")
    bad=[c for c in json.dumps(o,ensure_ascii=False) if ord(c) in (0x2014,0x2013)]
    print('ESCRITO %s  %d pasos  guiones_largos=%d'%(d['id'],len(d['pasos_accionables']),len(bad)))
