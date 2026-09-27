# -*- coding: utf-8 -*-
"""Barrido de vecinos D.38.4 de los 20 candidatos de la vuelta 42.

POBLACION: dataset/nodos.jsonl MAS lo que espera en cuarentena/<libro>/, que es
lo que D.38.4 manda y lo que la aduana mide desde D.38.5.

SENIALES: las dos baratas de la casa, aduana.senal_similitud_texto y
aduana.senal_familia_id, con los umbrales de config/umbrales.json y con el mismo
texto que mira la maquina, comun.texto_comparable (titulo MAS resumen_teorico MAS
pasos, normalizado). LA TERCERA SENIAL, paso contra nodo, NO esta aqui: va dicho.

LO UNICO QUE CAMBIO DE LA MAQUINA ES EL REPARTO DEL TRABAJO, no la cuenta: los 20
candidatos se reparten en procesos, uno por candidato, y cada proceso corre el
ratio entero contra los 371. La cuenta de cada par es la misma que correria en
serie. El motivo esta medido: en serie son unos seis minutos por candidato, o sea
dos horas, y una cifra que no cabe en un turno no se firma en un turno (D.43)."""
import json, glob, os, sys, io
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.getcwd())
from src import aduana, comun, config as modulo_config

umbrales = modulo_config.cargar()
U_TEXTO = umbrales['umbral_similitud_texto']
U_FAM = umbrales['umbral_familia_id']

def cargar():
    tabla = comun.leer_json(comun.RUTA_FUENTES)
    nodos = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
    bandejas = aduana.poblacion_de_bandejas(tabla_fuentes=tabla)
    return nodos, bandejas

def barrer(arg):
    ruta, = arg
    nodos, bandejas = cargar()
    ids_grafo = set(n['id'] for n in nodos)
    d = json.load(io.open(ruta, encoding='utf-8'))
    c, _ = aduana.normalizar_candidato(d)
    tc = comun.texto_comparable(c)
    out = []
    for v in nodos + bandejas:
        if v['id'] == c['id']:
            continue
        st = aduana.senal_similitud_texto(tc, comun.texto_comparable(v))
        sf = aduana.senal_familia_id(c['id'], v['id'])
        cuales = []
        if not isinstance(st, aduana.NoAplica) and st >= U_TEXTO:
            cuales.append('texto=%.3f' % st)
        if not isinstance(sf, aduana.NoAplica) and sf >= U_FAM:
            cuales.append('familia_id=%.3f' % sf)
        if cuales:
            out.append((v['id'], 'GRAFO' if v['id'] in ids_grafo else 'BANDEJA', ', '.join(cuales)))
    return c['id'], sorted(out)

if __name__ == '__main__':
    nodos, bandejas = cargar()
    print('POBLACION (D.38.4): %s' % aduana.Poblacion(len(nodos), len(bandejas)))
    print('umbrales: texto %s, familia_id %s' % (U_TEXTO, U_FAM))
    rutas = sorted(glob.glob('.a41/bandeja/*.json'))
    print('CANDIDATOS DEL TRAMO: %d' % len(rutas))
    print()
    total = 0
    with ProcessPoolExecutor(max_workers=8) as ex:
        for cid, lev in ex.map(barrer, [(r,) for r in rutas]):
            total += len(lev)
            print('%-55s %d vecino(s)' % (cid, len(lev)))
            for i, donde, s in lev:
                print('    %-8s %-55s %s' % (donde, i, s))
            sys.stdout.flush()
    print()
    print('TOTAL DE PARES LEVANTADOS POR LAS DOS SENIALES BARATAS: %d' % total)
