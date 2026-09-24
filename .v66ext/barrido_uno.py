# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 66 de .v65aud/barrido_uno.py, con dos rutas cambiadas: lee la ficha de
cuarentena/grove_high_output/ (la bandeja, cap_04, TAREA 3.2 del encargo) en vez de _insertados, y escribe
en .v66ext/ en vez de .v65aud/. Barrido D.38.4 para UNA ficha, normalizada como la
normaliza la aduana, contra GRAFO MAS BANDEJAS de hoy, con buscar_vecinos de
src/aduana.py (el mismo que usa insertar; se excluye a si mismo por id).
No escribe nada fuera de .v66ext/."""
import io, json, sys
sys.path.insert(0, '.')
from src import aduana, comun, config as modulo_config
i = sys.argv[1]
bruto = comun.leer_json('cuarentena/grove_high_output/%s.json' % i)
cand, _ = aduana.normalizar_candidato(bruto, aduana._hoy())
nodos = comun.leer_jsonl(comun.RUTA_DATASET)
bandejas = aduana.poblacion_de_bandejas(fecha=aduana._hoy())
umbrales = modulo_config.cargar()
vec = aduana.buscar_vecinos(cand, list(nodos) + list(bandejas), umbrales)
ids_grafo = set(n['id'] for n in nodos)
salida = {'id': i, 'grafo': len(nodos), 'bandejas': len(bandejas), 'vecinos': [
    {'id': v['id'], 'sede': 'grafo' if v['id'] in ids_grafo else 'bandeja',
     'senales': v['senales'], 'levantada_por': v['levantada_por'], 'detalle_paso': v['detalle_paso']} for v in vec]}
json.dump(salida, io.open('.v66ext/vecinos_%s.json' % i, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('%s poblacion %d (%d grafo mas %d bandejas) vecinos %d' % (i, len(nodos) + len(bandejas), len(nodos), len(bandejas), len(vec)))
