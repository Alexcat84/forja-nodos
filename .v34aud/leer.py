# -*- coding: utf-8 -*-
# Imprime los pasos de un nodo del grafo al lado de las lineas del libro que su
# resumen_teorico declara. CERO ids tecleados: el id entra por argumento desde
# .v34aud/tanda.txt.
import io, json, re, sys
ident = sys.argv[1]
nodos = {json.loads(l)['id']: json.loads(l)
         for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()}
n = nodos[ident]
rt = n['resumen_teorico']
m = re.search(r'fuentes/([a-z_]+)/(cap_\d+)\.md', rt)
lin = re.search(r'l[ií]neas? (\d+)\s*(?:a|-|hasta)\s*(\d+)', rt)
a, b = int(lin.group(1)), int(lin.group(2))
ruta = 'fuentes/%s/%s.md' % (m.group(1), m.group(2))
print('===== %s  |  %s  L%d-L%d  |  %d pasos =====' % (ident, ruta, a, b, len(n['pasos_accionables'])))
print('--- RESUMEN TEORICO ---')
print(rt)
print('--- LIBRO, L%d a L%d ---' % (a, b))
for i, l in enumerate(io.open(ruta, encoding='utf-8'), 1):
    if a <= i <= b and l.strip():
        print('L%03d| %s' % (i, l.rstrip()))
print('--- PASOS DEL NODO ---')
for k, p in enumerate(n['pasos_accionables'], 1):
    print('  %2d. %s' % (k, p))
print('--- OTROS CAMPOS ---')
for c in ('titulo', 'condiciones_activacion', 'entregable_esperado', 'dominio',
          'nodos_previos', 'nodos_siguientes', 'ids_alias'):
    print('  %s: %s' % (c, json.dumps(n.get(c), ensure_ascii=False)))
print('  atribuciones: %s' % json.dumps(n.get('atribuciones'), ensure_ascii=False))
