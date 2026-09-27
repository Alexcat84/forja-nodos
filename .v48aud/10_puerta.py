# -*- coding: utf-8 -*-
"""LA PUERTA D.39, MEDIDA Y NO SUPUESTA: que libros estan declarados CERRADOS EN
EXTRACCION en config/frentes.json, que es la sede que src/tablero.py lee. Si el libro
de esta vuelta no esta ahi, sus candidatos esperan en bandeja y cero inserciones es
lo correcto."""
import json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
d = json.load(open('config/frentes.json', encoding='utf-8'))
c = d.get('cerrados_en_extraccion') or {}
print('cerrados_en_extraccion, LISTA ENTERA (%d):' % len(c))
for k, v in c.items():
    print('   %-30s cita: %s' % (k, (v or {}).get('cita')))
print()
print('grove_high_output esta en cerrados_en_extraccion:', 'grove_high_output' in c)
