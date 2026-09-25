# -*- coding: utf-8 -*-
"""LA MUESTRA PINEADA DE LOS SANO DE LA 70 (AUDITOR_FORJA.md 7). La semilla 70 la registre en la fase ciega (APERTURA_CIEGA.md 6.5); este script lo escribo y lo corro en el turno normal, copia de .v67aud/normal/muestra_sano.py.
Poblacion: las lineas de bitacora/VEREDICTOS.jsonl que la vuelta 70 anadio (de la 905 en adelante: la ACTA 68
68.1 cerro en 904) con veredicto SANO. Tamano: el mayor entre 3 y el 20 por ciento redondeado hacia arriba, con
techo de 20. Eleccion: random.Random(70).sample sobre esas lineas en su orden de la bitacora.
Imprime SOLO candidato y vecino de cada elegido: la razon se destapa despues de releer los pasos (1.2)."""
import io, json, math, random
L = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')][904:]
sano = [(k + 905, d) for k, d in enumerate(L) if d.get('veredicto') == 'SANO']
n = min(20, max(3, int(math.ceil(0.2 * len(sano)))))
elegidos = sorted(random.Random(70).sample(sano, min(n, len(sano))), key=lambda x: x[0])
print('lineas de la 70: %d | SANO: %d | muestra: %d | semilla 70' % (len(L), len(sano), len(elegidos)))
for k, d in elegidos: print('linea %d  %s | %s' % (k, d['candidato'], d['vecino']))
