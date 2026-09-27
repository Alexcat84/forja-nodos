# los candidatos de grove cuya UNIDAD DE ORIGEN declarada es cap_02 o cap_03, con sus pasos
import json,glob,io,re
for p in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    d=json.load(io.open(p,encoding='utf-8'))
    m=re.search(r'UNIDAD DE ORIGEN: (fuentes/grove_high_output/(cap_\d\d)\.md)',d.get('resumen_teorico',''))
    cap=m.group(2) if m else 'SIN_UNIDAD'
    if cap in ('cap_02','cap_03','SIN_UNIDAD'):
        print(cap, d['id'], 'pasos=%d'%len(d.get('pasos_accionables',[])))
