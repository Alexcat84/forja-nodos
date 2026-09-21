# -*- coding: utf-8 -*-
"""Cuantas veces el fichero de cada candidato de cap_05 escribe el id de cada vecino
del grafo. Auditor, apertura ciega de la vuelta 51."""
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
SEIS=['infundir_regularidad_reunion_proceso','usar_tres_clases_reunion_proceso',
'fijar_frecuencia_reunion_individual_madurez_tarea','fijar_duracion_lugar_reunion_individual',
'preparar_guion_reunion_individual_subordinado','cubrir_indicadores_problemas_reunion_individual']
VEC=['dirigir_reunion_individual_semanal','preguntar_conducir_reunion_individual','auditar_calendario_reuniones_semana']
for s in SEIS:
    t=io.open('cuarentena/grove_high_output/%s.json'%s,encoding='utf-8').read()
    print("%-50s %s"%(s,'  '.join('%s:%d'%(v[:12],t.count(v)) for v in VEC)))
