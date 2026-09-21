# -*- coding: utf-8 -*-
"""COMO TERMINO EL TURNO DEL EXTRACTOR DE LA 61, LEIDO DE `ultimo_extractor.json`.

Se cita porque FECHA LA INTENCION, no porque sea sede: `D.33` dice que ningun
`docs/loop/ultimo_*.json` puede tumbar ni sostener una guarda.
"""
import io
import json

d = json.load(io.open('docs/loop/ultimo_extractor.json', encoding='utf-8'))
for k in ('is_error', 'stop_reason', 'terminal_reason', 'subtype', 'num_turns',
          'total_cost_usd'):
    print('%-16s: %s' % (k, d.get(k)))
print('%-16s: %s' % ('origin', json.dumps(d.get('origin'))))
print('%-16s: %s' % ('modelo', ', '.join(d.get('modelUsage', {}).keys())))
print('result          : %s' % d.get('result', '').strip().replace('\n', ' '))
