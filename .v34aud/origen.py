# -*- coding: utf-8 -*-
# CERO IDS TECLEADOS: la tanda sale de .v34aud/tanda.txt, que escribio cifras.py
# desde `git diff --name-only`. El origen se lee del propio resumen_teorico.
import io, json, re
rutas = [l.strip() for l in io.open('.v34aud/tanda.txt', encoding='utf-8') if l.strip()]
nodos = {json.loads(l)['id']: json.loads(l)
         for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()}
print('%-50s %-12s %-8s %s' % ('id', 'capitulo', 'pasos', 'lineas que declara'))
for r in rutas:
    i = json.load(io.open(r, encoding='utf-8'))['id']
    n = nodos[i]
    rt = n.get('resumen_teorico') or ''
    cap = re.search(r'fuentes/[a-z_]+/(cap_\d+)\.md', rt)
    lin = re.search(r'l[ií]neas? (\d+)\s*(?:a|-|hasta)\s*(\d+)', rt)
    lin1 = re.search(r'l[ií]nea (\d+)', rt)
    print('%-50s %-12s %-8d %s' % (
        i, cap.group(1) if cap else 'SIN CAPITULO',
        len(n['pasos_accionables']),
        ('%s a %s' % lin.groups()) if lin else (lin1.group(1) if lin1 else 'NO DECLARA')))
