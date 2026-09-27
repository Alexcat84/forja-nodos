# -*- coding: utf-8 -*-
# PRIMERA LINEA, D.40 HEREDADO 4: CERO IDS Y CERO RAZONES TECLEADAS. Las razones
# salen de bitacora/VEREDICTOS.jsonl y NO SE IMPRIMEN: solo se cuenta cuantas de
# ellas aparecen en la salida del instrumento que se le pase por argumento. Es la
# guarda del HEREDADO 2, que pide saber si una corrida IMPRIME UNA RAZON.
import io, json, subprocess, sys

razones = []
for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8'):
    if not l.strip(): continue
    r = (json.loads(l).get('razon') or '').strip()
    if len(r) >= 40: razones.append(r[:40])
salida = subprocess.run(sys.argv[1:], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode("utf-8", "replace")
filtradas = [r for r in razones if r in salida]
print('razones distintas en la bitacora (primeros 40 caracteres): %d'
      % len(set(razones)))
print('de ellas, IMPRESAS por "%s": %d' % (' '.join(sys.argv[1:]), len(filtradas)))
