# -*- coding: utf-8 -*-
"""LA COMPROBACION QUE LA PROPIA FICHA DE P38 PROPONE para sostener su afirmacion sin
barrer nada: abrir las dos fichas nombradas y leer su frase de cabecera."""
import io,sys,json,glob,re,collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
for s in ['decir_no_trabajo_excede_capacidad','usar_calendario_herramienta_planificacion_produccion','dimensionar_numero_subordinados_medio_dia_semanal']:
    r=json.load(open('cuarentena/grove_high_output/%s.json'%s,encoding='utf-8'))['resumen_teorico']
    print(s); print("   %s"%r[:170]); print()
c=collections.Counter()
for f in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    r=json.load(open(f,encoding='utf-8'))['resumen_teorico']
    m=re.search(r'Sale de la PIEZA (P\d+[a-z]?)',r[:400])
    if m: c[m.group(1)]+=1
print("fichas cuya PRIMERA frase declara 'Sale de la PIEZA P34': %d"%c['P34'])
print("fichas cuya PRIMERA frase declara 'Sale de la PIEZA P38': %d"%c['P38'])
