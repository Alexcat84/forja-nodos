# -*- coding: utf-8 -*-
"""La senial de la casa para los pares CRUZADOS DE LIBRO: los cuatro candidatos del uno a uno
de cap_05 contra los tres nodos del grafo que vienen de zhuo_manager. Son los pares que mi
lectura adjudica como frontera declarada, y aqui se ve que digito les pone la maquina."""
import io,sys,json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0,'.')
from src import aduana, comun
umbral=json.load(open('config/umbrales.json',encoding='utf-8'))['umbral_similitud_texto']
graf={}
for l in open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip():
        n=json.loads(l); graf[n['id']]=n
CAND=['fijar_frecuencia_reunion_individual_madurez_tarea','fijar_duracion_lugar_reunion_individual',
      'preparar_guion_reunion_individual_subordinado','cubrir_indicadores_problemas_reunion_individual',
      'infundir_regularidad_reunion_proceso','usar_tres_clases_reunion_proceso']
VEC=['dirigir_reunion_individual_semanal','preguntar_conducir_reunion_individual','auditar_calendario_reuniones_semana']
print("%-50s %-38s %8s %s"%("candidato de cap_05","nodo del grafo (zhuo_manager)","senial","pasa el umbral %s"%umbral))
for c in CAND:
    tc=comun.texto_comparable(json.load(open('cuarentena/grove_high_output/%s.json'%c,encoding='utf-8')))
    for v in VEC:
        s=aduana.senal_similitud_texto(tc,comun.texto_comparable(graf[v]))
        print("%-50s %-38s %8.4f %s"%(c[:50],v[:38],s,"SI" if s>=umbral else "no"))
