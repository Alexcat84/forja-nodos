# -*- coding: utf-8 -*-
"""Dos medidas sobre el bloque de vigencia D.15: de que LIBRO son los rancios que
forja.py rancios encuentra hoy, y si las seis fichas de cap_05 escriben alguna huella
de vigencia. Auditor, apertura ciega de la vuelta 51."""
import io,sys,json,re,subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
graf={}
for l in open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip():
        n=json.loads(l); graf[n['id']]=n
sal=subprocess.run([sys.executable,'forja.py','rancios'],capture_output=True).stdout.decode('utf-8', 'replace')
lineas=[l for l in sal.split('\n') if '[RANCIO]' in l]
libros={}
for l in lineas:
    m=re.search(r'veredicto (\S+) contra (\S+)',l)
    for i in m.groups():
        n=graf.get(i)
        if n: libros[n['fuentes'][0].get('clave')]=libros.get(n['fuentes'][0].get('clave'),0)+1
print("rancios que el bloque de vigencia D.15 encuentra hoy: %d"%len(lineas))
print("libro de los nodos que aparecen en ellos, contados: %s"%libros)
print("alguno de grove_high_output: %s"%('SI' if 'grove_high_output' in libros else 'no'))
print()
SEIS=['infundir_regularidad_reunion_proceso','usar_tres_clases_reunion_proceso',
'fijar_frecuencia_reunion_individual_madurez_tarea','fijar_duracion_lugar_reunion_individual',
'preparar_guion_reunion_individual_subordinado','cubrir_indicadores_problemas_reunion_individual']
for s in SEIS:
    t=io.open('cuarentena/grove_high_output/%s.json'%s,encoding='utf-8').read()
    print("%-50s 'huella': %d   'vigencia': %d   'D.15': %d"%(s,t.count('huella'),t.count('vigencia'),t.count('D.15')))
