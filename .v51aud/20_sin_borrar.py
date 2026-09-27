# -*- coding: utf-8 -*-
"""Las tres fichas que la vuelta 51 corrigio: el resumen_teorico VIEJO (commit de apertura
de la vuelta, 3061fc2) sigue siendo PREFIJO exacto del nuevo? Y que claves cambian?
Es la prueba mecanica de 'correccion declarada SIN BORRAR' (manual principio 6)."""
import io,sys,json,subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
TRES=['dimensionar_numero_subordinados_medio_dia_semanal','buscar_regularidad_bloques_iguales_trabajo_mando','preparar_respuestas_estandar_interrupciones_repetidas']
for s in TRES:
    ruta='cuarentena/grove_high_output/%s.json'%s
    v=json.loads(subprocess.check_output(['git','show','3061fc2:'+ruta]).decode('utf-8'))
    n=json.load(open(ruta,encoding='utf-8'))
    print("%-56s viejo %5d chars, nuevo %5d, crece %5d, el viejo es PREFIJO del nuevo: %s"%(
        s,len(v['resumen_teorico']),len(n['resumen_teorico']),
        len(n['resumen_teorico'])-len(v['resumen_teorico']),n['resumen_teorico'].startswith(v['resumen_teorico'])))
print()
for s in TRES:
    ruta='cuarentena/grove_high_output/%s.json'%s
    v=json.loads(subprocess.check_output(['git','show','3061fc2:'+ruta]).decode('utf-8'))
    n=json.load(open(ruta,encoding='utf-8'))
    print("%-56s claves que cambian: %s"%(s,sorted(k for k in set(list(v)+list(n)) if v.get(k)!=n.get(k))))
