# -*- coding: utf-8 -*-
"""CERO CONSTANTES TECLEADAS: no hay ni una lista de ids dentro. La poblacion y
los candidatos a barrer salen los dos del dato (glob sobre cuarentena/ y lectura
de dataset/nodos.jsonl). Es el REMEDIO 4 de la ACTA 30 aplicado a mi propio
instrumento: el barrido de la vuelta 21 llevaba `.lote_v21_auditor.txt` dentro.

Barrido de vecinos D.38.4 (GRAFO MAS BANDEJAS), leave-one-out.
Usa src.aduana.medir, el instrumento de la casa, EL MISMO que src.aduana.buscar_vecinos
llama por dentro. Lo unico que cambia respecto de la version de la vuelta pasada es que
el bucle va REPARTIDO EN PROCESOS: a 0,94 s por par medidos en esta misma fase, los 4.644
pares del barrido pedian 73 minutos en serie y la salida se quedo en CERO BYTES.
No hay ni una senial nueva ni un umbral tocado. CERO ESCRITURAS sobre el arbol de dato.

    python .marquet_v1/barrido_vecinos.py cuarentena/marquet_turn_the_ship
"""
import io, json, glob, os, sys
import multiprocessing as mp

sys.path.insert(0, os.path.abspath('.'))
from src import aduana, comun, config as modulo_config


def cargar_poblacion():
    nodos = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
    bandeja = []
    for p in sorted(glob.glob('cuarentena/*/*.json')):
        q = p.replace(chr(92), '/')
        if '_insertados' in q or '_derivadas' in q:
            continue
        bandeja.append((q, json.load(io.open(p, encoding='utf-8'))))
    return nodos, bandeja


_ESTADO = {}


def _arranque():
    nodos, bandeja = cargar_poblacion()
    _ESTADO['umbrales'] = modulo_config.cargar()
    _ESTADO['poblacion'] = nodos + [n for _, n in bandeja]
    _ESTADO['resolutor'] = aduana.Resolutor(_ESTADO['poblacion'])


def _medir_uno(tarea):
    ruta, indice = tarea
    cand = json.load(io.open(ruta, encoding='utf-8'))
    nodo = _ESTADO['poblacion'][indice]
    res, u = _ESTADO['resolutor'], _ESTADO['umbrales']
    if nodo.get('id') == cand.get('id'):
        return None
    if res.mismo(nodo.get('id'), cand.get('id')):
        return None
    if nodo.get('id') in res.deprecados:
        return None
    if u.get('solo_dominio_y_nucleo'):
        permitidos = set(u.get('dominios_nucleo') or [])
        permitidos.add(cand.get('dominio'))
        if nodo.get('dominio') not in permitidos:
            return None
    m = aduana.medir(cand, nodo, u)
    if not m['levantada_por']:
        return None
    return (ruta, m)


def main():
    comun.salida_utf8()
    nodos, bandeja = cargar_poblacion()
    umbrales = modulo_config.cargar()
    poblacion = nodos + [n for _, n in bandeja]

    print("POBLACION DEL BARRIDO (D.38.4)")
    print("  grafo dataset/nodos.jsonl : %d" % len(nodos))
    print("  bandejas cuarentena/*/    : %d" % len(bandeja))
    print("  TOTAL                     : %d" % len(poblacion))
    print("  umbrales: sim %s | fam %s | paso %s"
          % (umbrales.get('umbral_similitud_texto'), umbrales.get('umbral_familia_id'),
             umbrales.get('umbral_paso_contra_nodo')))
    print("")

    objetivo = sys.argv[1].replace(chr(92), '/').rstrip('/')
    aBarrer = [r for r, _ in bandeja if r.startswith(objetivo + '/')]
    print("candidatos a barrer en %s: %d (todos los de la carpeta, sin lista teclada)"
          % (objetivo, len(aBarrer)))
    print("pares a medir: %d" % (len(aBarrer) * (len(poblacion) - 1)))
    print("")

    tareas = [(r, i) for r in aBarrer for i in range(len(poblacion))]
    hallados = {}
    with mp.Pool(initializer=_arranque) as pool:
        for salida in pool.imap_unordered(_medir_uno, tareas, chunksize=8):
            if salida:
                hallados.setdefault(salida[0], []).append(salida[1])

    for ruta in aBarrer:
        vecinos = hallados.get(ruta, [])
        vecinos.sort(key=lambda v: max(aduana._ordenable_de_senal(x) for x in v["senales"].values()),
                     reverse=True)
        print("### %s   (contra %d)" % (os.path.basename(ruta), len(poblacion) - 1))
        if not vecinos:
            print("    SIN VECINOS: ninguna senial levanta nada")
        for v in vecinos:
            s = v["senales"]
            print("    vecino %s  [levantada por: %s]"
                  % (v["id"], ", ".join(v["levantada_por"])))
            print("      similitud_texto %s | familia_id %s | paso_contra_nodo %s"
                  % (s.get("similitud_texto"), s.get("familia_id"), s.get("paso_contra_nodo")))
            if v.get("detalle_paso"):
                print("      %s" % v["detalle_paso"])
        print("")


if __name__ == '__main__':
    main()
