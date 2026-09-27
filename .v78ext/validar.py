# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 78 de .v76ext/validar.py, con la bandeja cambiada a cuarentena/marquet_turn_the_ship/ y nada mas: corrida sobre
las 20 fichas despues de la ultima correccion (encargo de la 78, TAREA 2.3). Lo que decia la de la 76: COPIA DE LA VUELTA 76 de .v64ext/validar.py, con la bandeja cambiada a cuarentena/gerber_emyth/ y la salida al formato de
.v73ext/validar_siete.txt (avisos y errores por ficha): la parte de la aduana que decide CAERIA (esquema, reglas de id, fuentes
canonicas y guiones), corrida sobre las 22 fichas despues de la ultima correccion (encargo de la 76, TAREA 2.3), sin barrido."""
import io, os, sys
sys.path.insert(0, os.getcwd())
sys.stdout.reconfigure(encoding='utf-8')
from src import aduana, comun
for i in sys.argv[1:]:
    bruto = comun.leer_json('cuarentena/marquet_turn_the_ship/%s.json' % i)
    cand, avisos = aduana.normalizar_candidato(bruto)
    try:
        aduana.validar_candidato(cand)
        print('%-56s avisos %d | errores 0' % (i, len(avisos)))
    except aduana.Rechazo as r:
        print('%-56s avisos %d | errores CAERIA %s %s' % (i, len(avisos), r.titulo, r.detalles))
