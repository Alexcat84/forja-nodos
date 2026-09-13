# -*- coding: utf-8 -*-
"""ESCRIBE UN CANDIDATO DE cap_14 EN LA BANDEJA DE SALIDA.

No decide nada: solo monta el JSON con la forma que la aduana pide, para que el
cuerpo del candidato se escriba una sola vez y no se copie a mano quince veces.
"""
import io
import json
import os
import sys

BANDEJA = 'cuarentena/scott_radical_candor'


def escribir(d):
    d.setdefault('dominio', 'gestion_equipos')
    d.setdefault('estado', 'vivo')
    d.setdefault('ids_alias', [])
    d.setdefault('nodos_previos', [])
    d.setdefault('nodos_siguientes', [])
    d.setdefault('atribuciones', [])
    d.setdefault('fuentes', [{"clave": "scott_radical_candor", "fecha": "2026-09-13"}])
    d.setdefault('denominaciones', {"nombre_largo": "", "otros_idiomas": [], "sigla": ""})
    ruta = os.path.join(BANDEJA, d['id'] + '.json')
    io.open(ruta, 'w', encoding='utf-8', newline='').write(
        json.dumps(d, ensure_ascii=False, indent=2))
    print('escrito %s con %d pasos' % (ruta, len(d['pasos_accionables'])))
    return ruta


if __name__ == '__main__':
    escribir(json.load(io.open(sys.argv[1], encoding='utf-8')))
