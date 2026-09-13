# -*- coding: utf-8 -*-
"""EL PAR DE LA LUPA, MEDIDO CON EL MISMO MEDIDOR QUE USA LA ADUANA (TAREA 4).

Decision 3 del fundador del 12 sep 2026: el par `cap_10` L225 a L251 contra
`reconocer_recompensar_gente_estable` de `cap_06` se declara POR LECTURA como
CONTINUA con arista. El encargo aniade: si el informe te lo levanta, escribes el
veredicto con su razon; si NO te lo levanta, eso es un hecho nuevo y lo traes con
tu medida en vez de resolverlo copiando.

Esto es la medida. Llama a `src.aduana.medir`, que es la funcion que el informe
usa por dentro, con los umbrales de `config/umbrales.json` cargados por el mismo
cargador. Cero escrituras.
"""
import json

from src import aduana
from src import config as modulo_config

UMBRALES = modulo_config.cargar()
BASE = 'cuarentena/scott_radical_candor/%s.json'

PARES = [
    ('reconocer_excelencia_trayectoria_gradual', 'reconocer_recompensar_gente_estable',
     'EL PAR DE LA LUPA, adjudicado por la decision 3 del fundador'),
    ('sopesar_consejo_legal_despedir_humildad', 'despedir_persona_franqueza_radical',
     'par que levanto MI lectura, no el encargo'),
    ('admitir_pronto_mal_desempenio_cuatro_razones', 'decidir_momento_despedir_persona',
     'par que levanto MI lectura, no el encargo'),
    ('armar_plan_anual_crecimiento_equipo', 'cambiar_potencial_trayectoria_crecimiento',
     'par que levanto MI lectura, no el encargo'),
    ('evitar_obsesion_ascenso_estatus', 'elogiar_publico_criticar_privado_sus_tres_matices',
     'par que levanto MI lectura, no el encargo'),
    ('conversar_historia_vida_descubrir_motivadores', 'descubrir_motivacion_sentido_persona',
     'par que levanto MI lectura, no el encargo'),
]

print('umbrales de esta corrida: %s' % json.dumps(UMBRALES, sort_keys=True))
print('')
print('| candidato | vecino | similitud_texto | familia_id | paso_contra_nodo | la levanta alguna? |')
print('|---|---|---:|---:|---:|---|')
for hijo_id, madre_id, _nota in PARES:
    hijo = json.load(open(BASE % hijo_id, encoding='utf-8'))
    madre = json.load(open(BASE % madre_id, encoding='utf-8'))
    m = aduana.medir(hijo, madre, UMBRALES)
    s = m['senales']
    levantada = m['levantada_por'] or []
    print('| `%s` | `%s` | %s | %s | %s | %s |'
          % (hijo_id, madre_id,
             s.get('similitud_texto'), s.get('familia_id'), s.get('paso_contra_nodo'),
             ('**' + ', '.join(levantada) + '**') if levantada else 'NO, ninguna'))
print('')
for hijo_id, madre_id, nota in PARES:
    hijo = json.load(open(BASE % hijo_id, encoding='utf-8'))
    madre = json.load(open(BASE % madre_id, encoding='utf-8'))
    m = aduana.medir(hijo, madre, UMBRALES)
    print('%s contra %s   (%s)' % (hijo_id, madre_id, nota))
    print('  senales      : %s' % json.dumps(m['senales'], sort_keys=True))
    print('  levantada_por: %s' % (m['levantada_por'] or 'ninguna'))
    det = m.get('detalle_paso')
    if det:
        print('  detalle_paso : %s' % json.dumps(det, ensure_ascii=False)[:300])
    print('')
