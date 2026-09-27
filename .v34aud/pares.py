# -*- coding: utf-8 -*-
# IMPRIME SOLO EL PAR Y SUS SENIALES. Oculta clase y razon a proposito:
# AUDITOR_FORJA.md 1.2 manda adjudicar ANTES de destapar la razon escrita.
import io, json, sys
BASE_LINEAS = int(sys.argv[1])
ver = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]
print('lineas totales: %d   lineas nuevas de esta vuelta: %d' % (len(ver), len(ver) - BASE_LINEAS))
for n, v in enumerate(ver[BASE_LINEAS:], BASE_LINEAS + 1):
    campos = {k: v[k] for k in v if k not in ('clase', 'razon', 'veredicto', 'decision')}
    print('L%-4d %s' % (n, json.dumps(campos, ensure_ascii=False)))
