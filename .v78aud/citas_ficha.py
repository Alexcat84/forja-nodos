# -*- coding: utf-8 -*-
"""Fase ciega de la 78 (copia de .v76aud/citas_ficha.py con la ruta y el libro cambiados): de cada ficha de la bandeja de Marquet, SOLO las citas de capitulo y de linea que su
resumen_teorico nombra (cap_NN y LNN, en orden de aparicion y sin repetir), y cuantas veces trae el rotulo
CORRECCION DECLARADA. No imprime la prosa del resumen, para leer la fidelidad antes que la lectura del extractor. Solo lee."""
import io, json, re, sys
sys.stdout.reconfigure(encoding="utf-8")
for i in io.open('.v78aud/las20.txt', encoding='utf-8').read().split():
    d = json.load(io.open('cuarentena/marquet_turn_the_ship/%s.json' % i, encoding='utf-8'))
    r = d.get('resumen_teorico', '')
    corte = r.find('CORRECCION DECLARADA')
    antes = r if corte < 0 else r[:corte]
    vistos = []
    for t in re.findall(r'cap_\d+|\bL\d+\b', antes):
        if t not in vistos: vistos.append(t)
    print('%-55s correcciones %d | citas antes de la primera: %s' % (i, r.count('CORRECCION DECLARADA'), ' '.join(vistos)))
