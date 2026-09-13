# -*- coding: utf-8 -*-
import json,glob,io,os
ocho=[("fijar_cuatro_notas_calcular_nota_global",8,"elegir_categorias_nota_palabras_propias_empresa"),
("repartir_notas_publicar_reparto_esperado",3,"calibrar_notas_reunion_jefes_pares"),
("presionar_curva_notas_evitar_forzarla",11,"calibrar_notas_reunion_jefes_pares"),
("evaluar_desempenio_dos_veces_anio",6,"montar_evaluacion_360_grados_ligera_pares"),
("hacer_critica_pares_transparente_ensenar_escribirla",1,"montar_evaluacion_360_grados_ligera_pares"),
("mantener_proceso_evaluacion_ligero_vigilar_crecimiento",6,"montar_evaluacion_360_grados_ligera_pares"),
("mantener_proceso_evaluacion_ligero_vigilar_crecimiento",5,"hacer_critica_pares_transparente_ensenar_escribirla"),
("montar_evaluacion_360_grados_ligera_pares",6,"elegir_categorias_nota_palabras_propias_empresa")]
idx={}
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    d=json.loads(l); idx[d['id']]=('grafo',d)
for f in glob.glob('cuarentena/*/*.json')+glob.glob('cuarentena/_insertados/*/*.json'):
    if '_derivadas' in f.replace(os.sep,'/'): continue
    try: d=json.load(io.open(f,encoding='utf-8'))
    except Exception: continue
    if isinstance(d,dict) and 'id' in d: idx.setdefault(d['id'],('bandeja',d))
ok=viven=0
for m,p,h in ocho:
    sede,d=idx.get(m,('NO EXISTE',None))
    pasos=(d or {}).get('pasos_accionables') or []
    existe = d is not None and len(pasos)>=p
    ok+=existe
    sh=idx.get(h,('NO EXISTE',))[0]
    viven += (sede=='grafo' and sh=='grafo')
    print('%-54s paso %2d de %2d [%-8s] -> %-52s [%-8s] %s'%(m[:54],p,len(pasos),sede,h[:52],sh,'SI' if existe else 'NO'))
print('aristas con el paso de la madre EXISTENTE : %d de 8'%ok)
print('aristas con LOS DOS extremos en el grafo  : %d de 8'%viven)
