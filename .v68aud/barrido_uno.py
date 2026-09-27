# -*- coding: utf-8 -*-
"""Barrido D.38.4 de la fase ciega de la 68 (copia de .v66aud/barrido_uno.py con la ruta cambiada): la ficha de
cuarentena/grove_high_output/ o, con segundo argumento 'ins', de _insertados, normalizada como la
normaliza la aduana, contra GRAFO MAS BANDEJAS de hoy, con buscar_vecinos de
src/aduana.py (el mismo que usa insertar; se excluye a si mismo por id).
No escribe nada fuera de .v68aud/."""
import io, json, sys
sys.path.insert(0, '.')
from src import aduana, comun, config as modulo_config
i = sys.argv[1]
sede = 'cuarentena/_insertados/grove_high_output/' if sys.argv[2:] == ['ins'] else 'cuarentena/grove_high_output/'
bruto = comun.leer_json(sede + '%s.json' % i)
cand, _ = aduana.normalizar_candidato(bruto, aduana._hoy())
nodos = comun.leer_jsonl(comun.RUTA_DATASET)
bandejas = aduana.poblacion_de_bandejas(fecha=aduana._hoy())
umbrales = modulo_config.cargar()
vec = aduana.buscar_vecinos(cand, list(nodos) + list(bandejas), umbrales)
ids_grafo = set(n['id'] for n in nodos)
salida = {'id': i, 'grafo': len(nodos), 'bandejas': len(bandejas), 'vecinos': [
    {'id': v['id'], 'sede': 'grafo' if v['id'] in ids_grafo else 'bandeja',
     'senales': v['senales'], 'levantada_por': v['levantada_por'], 'detalle_paso': v['detalle_paso']} for v in vec]}
json.dump(salida, io.open('.v68aud/vecinos_%s.json' % i, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('%s poblacion %d (%d grafo mas %d bandejas) vecinos %d' % (i, len(nodos) + len(bandejas), len(nodos), len(bandejas), len(vec)))
