# -*- coding: utf-8 -*-
"""LA MUESTRA PINEADA DE LOS SANO DE LA 77 (AUDITOR_FORJA.md 7). La semilla 77 la registre en la fase ciega (APERTURA_CIEGA.md 7, punto 5); este script lo escribo y lo corro en el turno normal, copia de .v75aud/normal/muestra_sano.py (ACTA 76), con la vuelta, la semilla y el corte cambiados.
Poblacion: las lineas de bitacora/VEREDICTOS.jsonl que la vuelta 77 anadio (de la 1112 en adelante: la ACTA 75
75.1 cerro en 1111) con veredicto SANO. Tamano: el mayor entre 3 y el 20 por ciento redondeado hacia arriba, con
techo de 20. Eleccion: random.Random(77).sample sobre esas lineas en su orden de la bitacora.
Imprime SOLO candidato y vecino de cada elegido: la razon se destapa despues de releer los pasos (1.2)."""
import io, json, math, random
L = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')][1111:]
sano = [(k + 1112, d) for k, d in enumerate(L) if d.get('veredicto') == 'SANO']
n = min(20, max(3, int(math.ceil(0.2 * len(sano)))))
elegidos = sorted(random.Random(77).sample(sano, min(n, len(sano))), key=lambda x: x[0])
print('lineas de la 77: %d | SANO: %d | muestra: %d | semilla 77' % (len(L), len(sano), len(elegidos)))
for k, d in elegidos: print('linea %d  %s | %s' % (k, d['candidato'], d['vecino']))
