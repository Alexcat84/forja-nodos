# -*- coding: utf-8 -*-
"""Los pasos de las seis fichas de cap_05 de la bandeja de grove_high_output,
contados del propio fichero, con la pieza que cada una declara en su cabecera.
Corrido por el auditor en la APERTURA CIEGA de la vuelta 51."""
import io,sys,json,re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
SEIS=['infundir_regularidad_reunion_proceso','usar_tres_clases_reunion_proceso',
'fijar_frecuencia_reunion_individual_madurez_tarea','fijar_duracion_lugar_reunion_individual',
'preparar_guion_reunion_individual_subordinado','cubrir_indicadores_problemas_reunion_individual']
print("%-52s %-6s %6s"%("ficha","pieza","pasos"))
tot=0
for s in SEIS:
    d=json.load(open('cuarentena/grove_high_output/%s.json'%s,encoding='utf-8'))
    n=len(d['pasos_accionables']); tot+=n
    m=re.search(r'Sale de la PIEZA (P\d+[a-z]?)',d['resumen_teorico'][:400])
    print("%-52s %-6s %6d"%(s,m.group(1) if m else '?',n))
print("%-52s %-6s %6d"%("TOTAL DE PASOS DE LAS SEIS FICHAS DE cap_05","",tot))
