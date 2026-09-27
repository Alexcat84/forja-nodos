# -*- coding: utf-8 -*-
"""LA MUESTRA PINEADA DE LOS SANO DE LA 80 (AUDITOR_FORJA.md 7). La semilla 80 la registre (APERTURA_CIEGA.md 7, punto 4) en la fase ciega (APERTURA_CIEGA.md 7, punto 5); este script lo escribo y lo corro en el turno normal, copia de .v77aud/normal/muestra_sano.py (ACTA 76) para la ACTA 79, con la vuelta, la semilla y el corte cambiados.
Poblacion: las lineas de bitacora/VEREDICTOS.jsonl que la vuelta 80 anadio (de la 1173 en adelante: la ACTA 78
78.1 cerro en 1172) con veredicto SANO. Tamano: el mayor entre 3 y el 20 por ciento redondeado hacia arriba, con
techo de 20. Eleccion: random.Random(80).sample sobre esas lineas en su orden de la bitacora.
Imprime SOLO candidato y vecino de cada elegido: la razon se destapa despues de releer los pasos (1.2)."""
import io, json, math, random
L = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')][1172:]
sano = [(k + 1173, d) for k, d in enumerate(L) if d.get('veredicto') == 'SANO']
n = min(20, max(3, int(math.ceil(0.2 * len(sano)))))
elegidos = sorted(random.Random(80).sample(sano, min(n, len(sano))), key=lambda x: x[0])
print('lineas de la 80: %d | SANO: %d | muestra: %d | semilla 80' % (len(L), len(sano), len(elegidos)))
for k, d in elegidos: print('linea %d  %s | %s' % (k, d['candidato'], d['vecino']))
