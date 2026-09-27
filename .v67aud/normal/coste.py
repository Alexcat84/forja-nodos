# -*- coding: utf-8 -*-
"""ACTA 66: el desglose del turno del extractor de la 67, de docs/loop/ultimo_extractor.json (D.55, turno de mas de 10 USD)."""
import json
d = json.load(open('docs/loop/ultimo_extractor.json', encoding='utf-8')); u = d['usage']
print('coste USD %.2f | duracion %d s | api %d s | turnos %d' % (d['total_cost_usd'], d['duration_ms'] / 1000, d['duration_api_ms'] / 1000, d['num_turns']))
print('entrada %d | cache creada %d | cache leida %d | salida %d (pensamiento %d)' % (u['input_tokens'], u['cache_creation_input_tokens'], u['cache_read_input_tokens'], u['output_tokens'], u['output_tokens_details']['thinking_tokens']))
print('modelo %s' % ', '.join(d['modelUsage']))
print('contexto medio releido por turno: %d tokens | segundos fuera de la api: %d' % (u['cache_read_input_tokens'] / d['num_turns'], (d['duration_ms'] - d['duration_api_ms']) / 1000))
