# -*- coding: utf-8 -*-
"""TOMA EL CERROJO DE VERDAD Y LO DEVUELVE BYTE A BYTE (cosecha 7.C: la guarda
que se declara se re corre; si no hay caso rojo automatico, se declara)."""
import io, json, os, sys
sys.path.insert(0, os.getcwd())
from src import cerrojo, comun
ruta_ds = os.path.join(comun.RAIZ, 'dataset', 'nodos.jsonl')
ruta = cerrojo.ruta_de(ruta_ds)
print('ruta del cerrojo :', os.path.relpath(ruta, comun.RAIZ))
print('existe           :', os.path.exists(ruta))
crudo = None
if os.path.exists(ruta):
    crudo = io.open(ruta, 'rb').read()
    try:
        d = json.loads(crudo.decode('utf-8'))
        print('dueno declarado  :', d)
        import time
        print('edad en segundos :', int(time.time() - d.get('desde', 0)))
    except Exception as e:
        print('contenido no json:', e)
print('TOPE_DE_HUERFANO :', cerrojo.TOPE_DE_HUERFANO)
try:
    with cerrojo.tomar(ruta_ds):
        print('LO TOMO          : si, no bloquea')
except Exception as e:
    print('LO TOMO          : NO ->', type(e).__name__, e)
if crudo is not None:
    io.open(ruta, 'wb').write(crudo)
    print('fichero restaurado byte a byte:', io.open(ruta,'rb').read() == crudo)
else:
    if os.path.exists(ruta):
        os.remove(ruta)
        print('no existia antes: lo borro para dejarlo como estaba')
