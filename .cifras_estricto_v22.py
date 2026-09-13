# -*- coding: utf-8 -*-
"""Igual que .cifras_auditor_v22.py pero ESTRICTO: cada cifra contra las lineas
que el propio nodo declara como su tramo, no contra el capitulo entero."""
import io, json, re, unicodedata
PAL = {'un':1,'una':1,'uno':1,'dos':2,'tres':3,'cuatro':4,'cinco':5,'seis':6,'siete':7,
 'ocho':8,'nueve':9,'diez':10,'once':11,'doce':12,'trece':13,'catorce':14,'quince':15,
 'veinte':20,'veinticinco':25,'treinta':30,'cuarenta':40,'cincuenta':50,'cien':100,
 'ciento':100,'mil':1000,'primero':1,'segundo':2,'tercero':3,'cuarta':4,'primerisimo':1}
ING = {1:['one',' a ','single','first'],2:['two','second'],3:['three','third'],4:['four','fourth'],
 5:['five','fifth'],6:['six'],7:['seven'],8:['eight'],9:['nine'],10:['ten'],11:['eleven'],
 12:['twelve'],13:['thirteen'],14:['fourteen'],15:['fifteen'],20:['twenty'],
 25:['twenty-five','25','quarter'],30:['thirty'],40:['forty'],45:['forty-five'],50:['fifty'],
 100:['hundred'],1000:['thousand']}
TRAMO = {
 'desplegar_tres_conversaciones_carrera':('cap_10',[(19,19),(21,21),(43,43)]),
 'decidir_quien_comunica_cada_cuanto':('cap_11',[(15,35)]),
 'montar_reuniones_solas_mentalidad_frecuencia':('cap_11',[(37,65)]),
 'preguntar_seguimiento_hallar_huecos':('cap_11',[(67,97)]),
 'nutrir_ideas_nuevas_reunion_solas':('cap_11',[(99,113)]),
 'leer_seniales_fallo_jefe_reunion_solas':('cap_11',[(115,127)]),
 'conducir_reunion_equipo_agenda_tres_bloques':('cap_11',[(129,145),(159,163)]),
 'escribir_apuntes_sala_estudio_equipo':('cap_11',[(147,157)]),
 'bloquear_tiempo_pensar_calendario':('cap_11',[(165,173)]),
 'montar_reunion_gran_debate':('cap_11',[(175,193)]),
 'montar_reunion_gran_decision':('cap_11',[(195,203)]),
 'montar_reunion_general_presentaciones_preguntas':('cap_11',[(205,221)]),
 'pelear_proliferacion_reuniones_bloquear_ejecucion':('cap_11',[(223,233)]),
 'montar_tablero_kanban_medir_actividades':('cap_11',[(235,249)]),
 'pasear_organizacion_hallar_problemas_pequenios':('cap_11',[(251,269)]),
 'recorrer_rueda_conscientemente_cultura_equipo':('cap_11',[(271,299),(307,333)]),
 'debatir_decidir_asuntos_cultura_evitar_delegar':('cap_11',[(301,305)]),
}
def norm(s):
    s=unicodedata.normalize('NFD',s.lower())
    return ''.join(c for c in s if unicodedata.category(c)!='Mn')
SRC={c:io.open('fuentes/scott_radical_candor/%s.md'%c,encoding='utf-8').read().split('\n')
     for c in ('cap_10','cap_11')}
tot=hall=0; malas=[]
for nid,(cap,tramos) in TRAMO.items():
    texto = norm(' '.join(' '.join(SRC[cap][a-1:b]) for a,b in tramos))
    d=json.load(io.open('cuarentena/scott_radical_candor/%s.json'%nid,encoding='utf-8'))
    for i,p in enumerate(d['pasos_accionables'],1):
        np=norm(p); vistos=set()
        for m in re.findall(r'\d+',np): vistos.add(int(m))
        for w,v in PAL.items():
            if re.search(r'\b'+w.replace(' ',r'\s+')+r'\b',np): vistos.add(v)
        for v in sorted(vistos):
            tot+=1
            if any(f in texto for f in [str(v)]+ING.get(v,[])): hall+=1
            else: malas.append((nid,i,v,p[:95]))
print("CIFRAS DE LOS PASOS CONTRA EL TRAMO DECLARADO DEL PROPIO NODO (estricto)")
print("  nodos           : %d" % len(TRAMO))
print("  cifras leidas   : %d" % tot)
print("  cifras EN tramo : %d" % hall)
print("  cifras FUERA    : %d" % len(malas))
print("")
for nid,i,v,p in malas:
    print("  %-50s paso %-3d cifra %-5s | %s" % (nid,i,v,p))
