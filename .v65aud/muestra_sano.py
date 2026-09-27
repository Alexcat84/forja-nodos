# -*- coding: utf-8 -*-
"""LA MUESTRA PINEADA DE LOS SANO DE LA 65 (AUDITOR_FORJA.md 7), REGISTRADA EN LA FASE CIEGA Y SIN CORRER EN ELLA.
Poblacion: las lineas de bitacora/VEREDICTOS.jsonl que la vuelta 65 anadio (de la 741 en adelante: la ACTA 63
63.1 cerro en 740) con veredicto SANO. Tamano: el mayor entre 3 y el 20 por ciento redondeado hacia arriba, con
techo de 20. Eleccion: random.Random(65).sample sobre esas lineas en su orden de la bitacora.
Imprime SOLO candidato y vecino de cada elegido: la razon se destapa despues de releer los pasos (1.2)."""
import io, json, math, random
L = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')][740:]
sano = [(k + 741, d) for k, d in enumerate(L) if d.get('veredicto') == 'SANO']
n = min(20, max(3, int(math.ceil(0.2 * len(sano)))))
elegidos = sorted(random.Random(65).sample(sano, min(n, len(sano))), key=lambda x: x[0])
print('lineas de la 65: %d | SANO: %d | muestra: %d | semilla 65' % (len(L), len(sano), len(elegidos)))
for k, d in elegidos: print('linea %d  %s | %s' % (k, d['candidato'], d['vecino']))
