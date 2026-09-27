# -*- coding: utf-8 -*-
"""8.3: PASOS INVENTADOS POR CAPITULO, contados por el AUDITOR y no copiados.
Numerador = pasos que el auditor lee como PUENTE (D.30) tras correr
fidelidad_auditor_v23.py sobre los 262 y leer a mano los senialados.
Denominador = pasos escritos del capitulo, contados del fichero del candidato.
"""
import json, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
VU={'cap_12':['desplegar_plan_orden_operaciones_franqueza_radical',
              'contar_historias_propias_explicar_franqueza_radical'],
    'cap_13':['mejorar_consciencia_propia_relacional_dos_practicas',
              'contar_cuatro_historias_propias_ver_hueco_intencion',
              'practicar_triangulo_critica_tres_papeles',
              'pedir_critica_primero_crear_seguridad_psicologica',
              'elegir_pregunta_recurrente_pedir_critica',
              'resolver_dudas_frecuentes_pedir_critica',
              'abrazar_incomodidad_silencio_contar_seis',
              'escuchar_entender_critica_dominar_defensa',
              'premiar_franqueza_hacer_escucha_tangible',
              'integrar_peticion_critica_rutina_existente',
              'dar_elogio_disciplina_igual_critica',
              'medir_critica_respuesta_oyente_brujula']}
# PUENTES QUE EL AUDITOR ENCUENTRA EN SU LECTURA, por id y numero de paso.
PUENTES_DEL_AUDITOR = {}
print('%-8s %-10s %-10s %-10s %s' % ('capitulo','candidatos','pasos','puentes','pasos inventados'))
print('-'*66)
gp=gs=0
for cap in ('cap_12','cap_13'):
    s=sum(len(json.load(open('cuarentena/scott_radical_candor/%s.json'%i,encoding='utf-8'))['pasos_accionables']) for i in VU[cap])
    p=sum(len(PUENTES_DEL_AUDITOR.get(i,[])) for i in VU[cap])
    gs+=s; gp+=p
    print('%-8s %-10d %-10d %-10d %.2f por ciento' % (cap,len(VU[cap]),s,p,100.0*p/s))
print('-'*66)
print('%-8s %-10d %-10d %-10d %.2f por ciento' % ('LOTE v23',14,gs,gp,100.0*gp/gs))
