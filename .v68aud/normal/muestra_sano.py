# -*- coding: utf-8 -*-
"""LA MUESTRA PINEADA DE LOS SANO DE LA 68 (AUDITOR_FORJA.md 7). La semilla 68, el numero de la vuelta, NO la registre en la fase ciega (APERTURA_CIEGA.md 9.7 solo dice que los de cap_05 y cap_06 se muestrean en la 70) y lo declaro en el acta; copia de .v67aud/normal/muestra_sano.py.
Poblacion: las lineas de bitacora/VEREDICTOS.jsonl que la vuelta 68 anadio (de la 894 en adelante: la ACTA 66
66.1 cerro en 893) con veredicto SANO. Tamano: el mayor entre 3 y el 20 por ciento redondeado hacia arriba, con
techo de 20. Eleccion: random.Random(68).sample sobre esas lineas en su orden de la bitacora.
Imprime SOLO candidato y vecino de cada elegido: la razon se destapa despues de releer los pasos (1.2)."""
import io, json, math, random
L = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')][893:]
sano = [(k + 894, d) for k, d in enumerate(L) if d.get('veredicto') == 'SANO']
n = min(20, max(3, int(math.ceil(0.2 * len(sano)))))
elegidos = sorted(random.Random(68).sample(sano, min(n, len(sano))), key=lambda x: x[0])
print('lineas de la 68: %d | SANO: %d | muestra: %d | semilla 68' % (len(L), len(sano), len(elegidos)))
for k, d in elegidos: print('linea %d  %s | %s' % (k, d['candidato'], d['vecino']))
