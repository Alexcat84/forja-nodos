# -*- coding: utf-8 -*-
"""La senial 1 de la casa mide titulo+resumen_teorico+pasos (src/comun.py:190).
Aqui la corro TAL CUAL y, al lado, la misma funcion sobre SOLO titulo+pasos,
para ver cuanto de lo que levanta un par viene del resumen y cuanto del
procedimiento. No cambia ninguna senial ni ningun umbral: solo reparte."""
import json, sys, os
sys.path.insert(0, os.getcwd())
from src import aduana, comun

def carga(i):
    for r in ('cuarentena/scott_radical_candor/%s.json' % i,):
        if os.path.exists(r):
            return json.load(open(r, encoding='utf-8'))
    import io
    for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
        d = json.loads(l)
        if d['id'] == i:
            return d
    for l in io.open('cuarentena/_insertados/scott_radical_candor/%s.json' % i, encoding='utf-8'):
        pass
    raise SystemExit('no encuentro ' + i)

def solo_pasos(n):
    return comun.normalizar_texto(' '.join([n.get('titulo') or ''] + list(n.get('pasos_accionables') or [])))

pares = [('abrazar_incomodidad_silencio_contar_seis', 'escuchar_entender_critica_dominar_defensa'),
         ('abrazar_incomodidad_silencio_contar_seis', 'practicar_triangulo_critica_tres_papeles'),
         ('abrazar_incomodidad_silencio_contar_seis', 'premiar_franqueza_hacer_escucha_tangible'),
         ('abrazar_incomodidad_silencio_contar_seis', 'contar_historias_propias_explicar_franqueza_radical')]
print('umbral de la senial 1: %s' % comun.leer_json('config/umbrales.json')['umbral_similitud_texto'])
print('%-52s %-52s %8s %8s' % ('a', 'b', 'CASA', 'solo pasos'))
for a, b in pares:
    na, nb = carga(a), carga(b)
    casa = aduana.senal_similitud_texto(comun.texto_comparable(na), comun.texto_comparable(nb))
    pas = aduana.senal_similitud_texto(solo_pasos(na), solo_pasos(nb))
    print('%-52s %-52s %8.3f %8.3f' % (a[:52], b[:52], casa, pas))
