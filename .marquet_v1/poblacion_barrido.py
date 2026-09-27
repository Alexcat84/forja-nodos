# -*- coding: utf-8 -*-
"""CERO CONSTANTES TECLEADAS DENTRO: no hay ni una lista de ids ni un nombre de
carpeta escrito a mano. Todo sale del dato (os.walk sobre cuarentena/ y la tabla
fuentes/FUENTES_CANONICAS.json). Es el REMEDIO 4 de la ACTA 30 aplicado a mi
propio instrumento: los barridos .barrido_auditor.py y .barrido_auditor_v21.py
llevaban dentro un fichero de ids teclado (.lote16.txt y .lote_v21_auditor.txt).

QUE MIDE. Si la poblacion del barrido de la ADUANA es la misma que la mia
(D.38.5: `LA ADUANA YA MIDE LA MISMA POBLACION QUE TU`). Cuenta los tres pisos:
lo que hay en cuarentena/, lo que la casa descarta por carpeta, y lo que descarta
por la tabla canonica. CERO ESCRITURAS.

    python .marquet_v1/poblacion_barrido.py
"""
import io, json, os, sys
sys.path.insert(0, os.path.abspath('.'))
from src import aduana, comun

comun.salida_utf8()

nodos = sum(1 for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip())

crudos, por_carpeta = [], {}
for carpeta, subcarpetas, ficheros in os.walk(comun.DIR_CUARENTENA):
    for f in sorted(ficheros):
        if not f.lower().endswith('.json'):
            continue
        ruta = os.path.join(carpeta, f).replace(chr(92), '/')
        crudos.append(ruta)
        rel = ruta.split('cuarentena/', 1)[-1]
        por_carpeta[rel.split('/')[0]] = por_carpeta.get(rel.split('/')[0], 0) + 1

esperan = aduana.poblacion_de_bandejas()
tabla = comun.leer_json(comun.RUTA_FUENTES)
ids_esperan = set(c.get('id') for c in esperan)

print("TODOS LOS .json BAJO cuarentena/ : %d" % len(crudos))
for nombre in sorted(por_carpeta):
    print("    %-28s %4d" % (nombre, por_carpeta[nombre]))
print("")
print("CARPETAS FUERA DE POBLACION (aduana.CARPETAS_FUERA_DE_POBLACION) : %s"
      % (", ".join(aduana.CARPETAS_FUERA_DE_POBLACION),))
print("POBLACION DE BANDEJAS QUE LA CASA MIDE (aduana.poblacion_de_bandejas) : %d"
      % len(esperan))
print("GRAFO dataset/nodos.jsonl : %d" % nodos)
print("POBLACION DEL BARRIDO D.38.4 = GRAFO MAS BANDEJAS : %d" % (nodos + len(esperan)))
print("")
print("LO QUE QUEDA FUERA Y POR QUE (no por su nombre: por su tabla de fuentes)")
fuera = {}
for ruta in crudos:
    try:
        bruto = comun.leer_json(ruta)
    except (IOError, ValueError):
        fuera.setdefault('ilegible', []).append(ruta)
        continue
    cand, _ = aduana.normalizar_candidato(bruto, None)
    if cand.get('id') in ids_esperan:
        continue
    claves = [f.get('clave') for f in (cand.get('fuentes') or []) if isinstance(f, dict)]
    malas = [c for c in claves if c not in tabla]
    motivo = ('carpeta fuera de poblacion' if any(
                  s in ruta for s in aduana.CARPETAS_FUERA_DE_POBLACION)
              else ('clave(s) fuera de fuentes/FUENTES_CANONICAS.json: %s'
                    % ", ".join(sorted(set(malas))) if malas else 'sin id'))
    fuera.setdefault(motivo, []).append(ruta)
for motivo in sorted(fuera):
    print("    %4d  %s" % (len(fuera[motivo]), motivo))
print("")
print("CLAVES DE fuentes/FUENTES_CANONICAS.json : %d -> %s"
      % (len(tabla), ", ".join(sorted(tabla))))
