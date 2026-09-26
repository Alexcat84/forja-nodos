# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 78 de .v76ext/barrido_uno.py, con la ruta de escritura cambiada a .v78ext/ y la ficha leida de
cuarentena/marquet_turn_the_ship/ (la bandeja de Marquet, las 20, TAREA 3 del encargo de la 78); nada mas. Lo que decia la de la 76:
COPIA DE LA VUELTA 76 de .v73ext/barrido_uno.py, con la ruta de escritura cambiada a .v76ext/ y la ficha leida de
cuarentena/gerber_emyth/ (la bandeja de Gerber, las 22, TAREA 3 del encargo de la 76); nada mas. Lo que decia la de la 73:
COPIA DE LA VUELTA 73 de .v71ext/barrido_uno.py, con la ruta de escritura cambiada a .v73ext/ y nada mas; lee la
ficha de cuarentena/grove_high_output/ (la bandeja, las 7 de cap_15 a cap_17, TAREA 3 del encargo de la 73). Lo que
decia la de la 71: COPIA DE LA VUELTA 71 de .v68ext/barrido_uno.py, con la ruta de escritura cambiada a .v71ext/ y nada mas; lee la
ficha de cuarentena/grove_high_output/ (la bandeja, las 20 de cap_07 a cap_14, TAREA 3 del encargo de la 71). Lo que
decia la de la 68: COPIA DE LA VUELTA 68 de .v66ext/barrido_uno.py (que era COPIA de .v65aud/barrido_uno.py), con la ruta de
escritura cambiada a .v68ext/; lee la ficha de cuarentena/grove_high_output/ (la bandeja, cap_05 y cap_06, TAREA 3.2
del encargo de la 68). Barrido D.38.4 para UNA ficha, normalizada como la
normaliza la aduana, contra GRAFO MAS BANDEJAS de hoy, con buscar_vecinos de
src/aduana.py (el mismo que usa insertar; se excluye a si mismo por id).
No escribe nada fuera de .v68ext/."""
import io, json, sys
sys.path.insert(0, '.')
from src import aduana, comun, config as modulo_config
i = sys.argv[1]
bruto = comun.leer_json('cuarentena/marquet_turn_the_ship/%s.json' % i)
cand, _ = aduana.normalizar_candidato(bruto, aduana._hoy())
nodos = comun.leer_jsonl(comun.RUTA_DATASET)
bandejas = aduana.poblacion_de_bandejas(fecha=aduana._hoy())
umbrales = modulo_config.cargar()
vec = aduana.buscar_vecinos(cand, list(nodos) + list(bandejas), umbrales)
ids_grafo = set(n['id'] for n in nodos)
salida = {'id': i, 'grafo': len(nodos), 'bandejas': len(bandejas), 'vecinos': [
    {'id': v['id'], 'sede': 'grafo' if v['id'] in ids_grafo else 'bandeja',
     'senales': v['senales'], 'levantada_por': v['levantada_por'], 'detalle_paso': v['detalle_paso']} for v in vec]}
json.dump(salida, io.open('.v78ext/vecinos_%s.json' % i, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('%s poblacion %d (%d grafo mas %d bandejas) vecinos %d' % (i, len(nodos) + len(bandejas), len(nodos), len(bandejas), len(vec)))
