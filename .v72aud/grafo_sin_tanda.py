# -*- coding: utf-8 -*-
"""Fase ciega de la 72, sin git (copia de .v70aud/grafo_sin_tanda.py con las rutas de la 71): el grafo de HOY con las 20 de la tanda quitadas es, byte a byte, el grafo que barri
en la 71? Reconstruye el fichero como lo escribe src/comun.py escribir_jsonl (json.dumps con sort_keys y
ensure_ascii=False, una fila por linea, salto final) y compara su sha1 con la huella de dataset/nodos.jsonl en
.v71aud/huellas_al_barrer.txt. Antes comprueba que esa reconstruccion reproduce el fichero de hoy tal cual.
Dos versiones: (a) solo quitando las 20 filas; (b) quitando ademas los ids de las 20 de CUALQUIER lista de texto de los
nodos que quedan, sin nombrar ninguna clave. NO IMPRIME NINGUNA CLAVE DE NINGUN NODO (R6): solo cuentas y SI o NO."""
import io, json, hashlib, sys
sys.stdout.reconfigure(encoding="utf-8")
los20 = set(io.open('.v71aud/los20.txt', encoding='utf-8').read().split())
huella = [l.split(' *')[0] for l in io.open('.v71aud/huellas_al_barrer.txt', encoding='utf-8') if l.strip().endswith('*dataset/nodos.jsonl')][0]
bruto = open('dataset/nodos.jsonl', 'rb').read()
filas = [json.loads(l) for l in bruto.decode('utf-8').splitlines() if l.strip()]
ser = lambda fs: ('\n'.join(json.dumps(f, ensure_ascii=False, sort_keys=True) for f in fs) + '\n').encode('utf-8')
print('filas del grafo hoy: %d | la reconstruccion reproduce el fichero de hoy: %s' % (len(filas), 'SI' if ser(filas) == bruto else 'NO'))
tanda = [f for f in filas if f['id'] in los20]; resto = [f for f in filas if f['id'] not in los20]
print('de las 20 de la tanda en el grafo: %d | filas que quedan sin ellas: %d' % (len(tanda), len(resto)))
pos = [k for k, f in enumerate(filas) if f['id'] in los20]
print('las 20 son las ultimas filas del fichero: %s' % ('SI' if pos == list(range(len(filas) - len(tanda), len(filas))) else 'NO'))
print('(a) sin las 20 filas, sha1 igual a la huella de mi barrido de la 71: %s' % ('SI' if hashlib.sha1(ser(resto)).hexdigest() == huella else 'NO'))
tocados = 0; limpio = []
for f in resto:
    g = {}; t = False
    for k, v in f.items():
        if isinstance(v, list) and any(isinstance(x, str) and x in los20 for x in v):
            v = [x for x in v if not (isinstance(x, str) and x in los20)]; t = True
        g[k] = v
    tocados += t; limpio.append(g)
print('(b) nodos viejos con algun id de las 20 en alguna lista: %d | sin esos ids, sha1 igual a la huella: %s' % (
    tocados, 'SI' if hashlib.sha1(ser(limpio)).hexdigest() == huella else 'NO'))
