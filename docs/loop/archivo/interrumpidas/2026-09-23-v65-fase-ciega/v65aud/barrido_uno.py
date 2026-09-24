# -*- coding: utf-8 -*-
"""Fase ciega de la 65 (D.38.4): la aduana de UN insertado, re medida hoy sobre su ficha de
cuarentena/_insertados/grove_high_output/, contra grafo mas bandejas. La poblacion union es la
misma que en el acto de insertar (lo que paso de la bandeja al grafo no cambia la union), y el
propio candidato se salta por id (aduana.buscar_vecinos). Llama a aduana.buscar_vecinos tal cual:
no mide nada que la aduana no mida. Escribe .v65aud/vecinos_<id>.txt."""
import io, os, sys
sys.path.insert(0, os.getcwd())
from src import aduana, comun
i = sys.argv[1]
ruta = 'cuarentena/_insertados/grove_high_output/%s.json' % i
tabla = comun.leer_json(comun.RUTA_FUENTES)
cand, _ = aduana.normalizar_candidato(comun.leer_json(ruta), aduana._hoy())
nodos = comun.leer_jsonl(comun.RUTA_DATASET)
band = aduana.poblacion_de_bandejas(fecha=aduana._hoy(), tabla_fuentes=tabla)
pob = list(nodos) + list(band)
vec = aduana.buscar_vecinos(cand, pob)
with io.open('.v65aud/vecinos_%s.txt' % i, 'w', encoding='utf-8') as f:
    f.write('candidato %s | grafo %d | bandejas %d | poblacion %d | vecinos %d\n'
            % (i, len(nodos), len(band), len(pob), len(vec)))
    for v in vec:
        s = v['senales']
        f.write('  %-50s %-40s texto %s familia %s paso %s | %s\n'
                % (v['id'], ','.join(v['levantada_por']), s.get('similitud_texto'),
                   s.get('familia_id'), s.get('paso_contra_nodo'), v['detalle_paso']))
    f.write('FIN\n')
