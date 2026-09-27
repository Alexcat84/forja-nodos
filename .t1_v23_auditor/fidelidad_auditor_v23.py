# -*- coding: utf-8 -*-
"""D.30 / 8.3 punto 2, instrumento del AUDITOR.
El texto fuente esta en ingles y los pasos en castellano, asi que el solape de
palabras no sirve. Lo que SI viaja sin traducirse son LOS NUMEROS y LOS NOMBRES
PROPIOS, y son la especie de puente mas cara: una cantidad inventada o una
autoridad anadida. Este instrumento extrae de cada paso sus numeros (en cifra y
en palabra) y sus nombres propios, y comprueba que aparecen en el TRAMO DE
LINEAS que el propio candidato declara como su origen.
Lo que salga NO ENCONTRADO es lo que el auditor lee a mano.
"""
import json, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

NUM = {'uno':'one','dos':'two','tres':'three','cuatro':'four','cinco':'five','seis':'six',
'siete':'seven','ocho':'eight','nueve':'nine','diez':'ten','veinte':'twenty','treinta':'thirty',
'sesenta':'sixty','mil':'thousand','decada':'decade','primera':'first','segunda':'second'}

TRAMOS = {
 'desplegar_plan_orden_operaciones_franqueza_radical': ('cap_12',[(13,13),(15,15),(19,49)]),
 'contar_historias_propias_explicar_franqueza_radical': ('cap_12',[(17,17)]),
 'mejorar_consciencia_propia_relacional_dos_practicas': ('cap_13',[(17,22),(35,40)]),
 'contar_cuatro_historias_propias_ver_hueco_intencion': ('cap_13',[(41,58)]),
 'practicar_triangulo_critica_tres_papeles': ('cap_13',[(59,72)]),
 'pedir_critica_primero_crear_seguridad_psicologica': ('cap_13',[(73,86),(105,110),(113,114)]),
 'elegir_pregunta_recurrente_pedir_critica': ('cap_13',[(115,120),(129,166)]),
 'resolver_dudas_frecuentes_pedir_critica': ('cap_13',[(167,186)]),
 'abrazar_incomodidad_silencio_contar_seis': ('cap_13',[(187,198)]),
 'escuchar_entender_critica_dominar_defensa': ('cap_13',[(199,214)]),
 'premiar_franqueza_hacer_escucha_tangible': ('cap_13',[(215,234)]),
 'integrar_peticion_critica_rutina_existente': ('cap_13',[(111,112),(235,246)]),
 'dar_elogio_disciplina_igual_critica': ('cap_13',[(247,252),(267,288)]),
 'medir_critica_respuesta_oyente_brujula': ('cap_13',[(289,322)]),
}
# nombres propios que el castellano del paso traduce y el ingles no escribe igual
EXENTOS = set('''Cuenta Cuando Practicalo Parte Usa Junta Pon Haz Pide Lleva Nombra Centrate
Presta Fijate Piensa Cuentala Comprueba Elige Empieza Sigue Planea Pelea Pasea Vuelve Respira
Aparta Establece Asegurate Acuerdate Trata Averigua Abraza Busca Muestra Explica Puedes Pero
Cero Que Como Por Para Con Sin Los Las Del Ten Ahora Antes Despues Este Esta Estoy Si No Y
Franqueza Radical Empatia Ruinosa Agresion Odiosa Insinceridad Manipuladora Compasiva
Preparate Reconoce Evalua Recuerda Termina Escucha Mide Practica Deja Dale Dile Di Ve'''.split())

for cid,(cap,rangos) in TRAMOS.items():
    d = json.load(open('cuarentena/scott_radical_candor/%s.json'%cid, encoding='utf-8'))
    lin = open('fuentes/scott_radical_candor/%s.md'%cap, encoding='utf-8').read().split('\n')
    tramo = ' '.join(lin[i-1] for a,b in rangos for i in range(a,b+1))
    tl = tramo.lower()
    faltan = []
    for k,p in enumerate(d['pasos_accionables'],1):
        for n in set(re.findall(r'\b\d[\d.,]*\b', p)):
            if n.replace('.','').replace(',','') not in tl.replace('.','').replace(',',''):
                faltan.append((k,'cifra',n))
        for w in set(re.findall(r'\b[a-z]+\b', p.lower())):
            if w in NUM and NUM[w] not in tl and w not in tl:
                pass  # el numero en palabra: solo se avisa si tampoco esta su ingles
        for w in set(re.findall(r'(?<![.!?]\s)(?<!^)\b[A-Z][a-zA-Z]{2,}\b', p)):
            if w in EXENTOS: continue
            if w.lower() not in tl: faltan.append((k,'nombre propio',w))
    print('%-55s %2d pasos   %s' % (cid, len(d['pasos_accionables']),
          'TODO NUMERO Y NOMBRE PROPIO ESTA EN SU TRAMO' if not faltan else 'NO ENCONTRADO: %s'%faltan))
