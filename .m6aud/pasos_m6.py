import json,re,unicodedata
def norm(s):
    s=s.replace(chr(0x2019),"'").replace(chr(0x2018),"'").replace(chr(0x201c),'"').replace(chr(0x201d),'"').replace(chr(0x2014),'-').replace(chr(0x2013),'-')
    s=re.sub(r'[\"\']','',s); s=s.replace(', in a word',' in a word').replace('-in a word',' in a word')
    return re.sub(r'\s+',' ',s).strip().lower()
casos={'identificar_temas_formacion_tarjetas_decision':('cap_12',range(125,140)),
 'repetir_mensaje_invariable_diario_reunion_evento':('cap_13',[119]),
 'reforzar_principios_guia_lenguaje_prueba_conocimiento':('cap_14',[89,99])}
tot=0;ok=0
for c,(cap,lin) in casos.items():
    src=open(f'fuentes/marquet_turn_the_ship/{cap}.md',encoding='utf-8').read().split('\n')
    d=json.load(open(f'cuarentena/marquet_turn_the_ship/{c}.json',encoding='utf-8'))
    for i,p in enumerate(d['pasos_accionables'],1):
        q=p.split('El texto lo dice asi:')[1]
        hit=[n for n in lin if norm(q).rstrip('. ') in norm(src[n-1])]
        # permitir que la cita cruce dos lineas del bloque
        if not hit:
            blob=' '.join(norm(src[n-1]) for n in lin); hit=['bloque'] if norm(q).rstrip('. ') in blob else []
        tot+=1; ok+=bool(hit)
        print(f'{cap} {c[:40]:40} P{i} cita literal en: {hit if hit else "NO ENCONTRADA"}')
print(f'pasos {tot}, con cita literal en su linea {ok}')
