# -*- coding: utf-8 -*-
"""Cuantos digitos de senial declara cada ficha de cap_05 dentro de su resumen_teorico, y si
trae alguna salvedad sobre CONTRA QUE VERSION DE TEXTO se midio. Auditor, apertura ciega v51."""
import io,sys,json,re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
SEIS=['infundir_regularidad_reunion_proceso','usar_tres_clases_reunion_proceso',
'fijar_frecuencia_reunion_individual_madurez_tarea','fijar_duracion_lugar_reunion_individual',
'preparar_guion_reunion_individual_subordinado','cubrir_indicadores_problemas_reunion_individual']
CAVEAT=['texto de entonces','en el momento de la pasada','antes de escribir esta linea',
        'el texto que la aduana leyo','contra el texto de la pasada','deja de reproducir','ya no reproduce']
tot=0
for s in SEIS:
    r=json.load(open('cuarentena/grove_high_output/%s.json'%s,encoding='utf-8'))['resumen_teorico']
    n=len(re.findall(r'similitud de texto 0,\d{3}',r)); tot+=n
    hay=[c for c in CAVEAT if c in r]
    print("%-50s digitos declarados: %d   salvedad de version de texto: %s"%(s[:50],n,hay if hay else 'NINGUNA de las siete buscadas'))
print()
print("digitos declarados en la tanda: %d, repartidos en %d de las 6 fichas"%(tot,sum(1 for s in SEIS if re.search(r'similitud de texto 0,\d{3}',json.load(open('cuarentena/grove_high_output/%s.json'%s,encoding='utf-8'))['resumen_teorico']))))
