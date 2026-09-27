# -*- coding: utf-8 -*-
"""Que movio la vuelta 49 dentro de las dos fichas tocadas, medido con la propia
funcion de la casa: comun.texto_comparable (titulo + resumen + pasos, src/comun.py:190)
y comun.huella_de_nodo. Compara la ficha de HEAD~1 con la de HEAD."""
import io,sys,json,subprocess
sys.path.insert(0,'.')
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from src import comun
for fid in ["reunir_informacion_gerencial_vias_variadas","dimensionar_numero_subordinados_medio_dia_semanal"]:
    ruta="cuarentena/grove_high_output/%s.json" % fid
    antes=json.loads(subprocess.check_output(["git","show","HEAD~1:"+ruta]).decode("utf-8"))
    hoy=json.load(open(ruta,encoding='utf-8'))
    print("== %s" % fid)
    for campo in ["titulo","condiciones_activacion","entregable_esperado","resumen_teorico"]:
        a,b=antes.get(campo,""),hoy.get(campo,"")
        print("   %-24s antes %6d car, hoy %6d car, %s" % (campo,len(a),len(b),"IGUAL" if a==b else "CAMBIA (+%d)"%(len(b)-len(a))))
    print("   %-24s antes %6d, hoy %6d, %s" % ("pasos_accionables",len(antes["pasos_accionables"]),len(hoy["pasos_accionables"]),
          "IGUALES" if antes["pasos_accionables"]==hoy["pasos_accionables"] else "CAMBIAN"))
    ha,hb=comun.huella_de_nodo(antes),comun.huella_de_nodo(hoy)
    print("   huella del texto que mira la senial 1: antes %s, hoy %s, %s" % (ha,hb,"IGUAL" if ha==hb else "DISTINTA"))
    print("   texto_comparable: antes %d car, hoy %d car" % (len(comun.texto_comparable(antes)),len(comun.texto_comparable(hoy))))
    for campo in ["entregable_esperado","resumen_teorico"]:
        a,b=antes.get(campo,""),hoy.get(campo,"")
        if a!=b:
            print("   %s: el texto viejo entero (%d car) %s dentro del nuevo" % (campo,len(a),"SIGUE" if a in b else "NO SIGUE"))
    print()
