# -*- coding: utf-8 -*-
"""Vuelta 64: la parte de la aduana que decide CAERIA (esquema, reglas de id, fuentes
canonicas y guiones), corrida sobre las fichas corregidas, sin barrido de vecinos:
el barrido lo sustituye la medicion par a par que el encargo manda (2.c)."""
import io, os, sys
sys.path.insert(0, os.getcwd())
from src import aduana, comun
for i in sys.argv[1:]:
    bruto = comun.leer_json('cuarentena/grove_high_output/%s.json' % i)
    cand, avisos = aduana.normalizar_candidato(bruto)
    try:
        aduana.validar_candidato(cand)
        print('NO CAERIA  %s  (esquema, id, fuentes y guiones en verde)%s' % (i, ('  avisos: %s' % avisos) if avisos else ''))
    except aduana.Rechazo as r:
        print('CAERIA     %s  %s %s' % (i, r.titulo, r.detalles))
