import json, io, glob, re
RUTA = 'fuentes/scott_radical_candor/cap_07.md'
L = io.open(RUTA, encoding='utf-8').read().split('\n')
ROTULOS = ('LISTEN', 'CLARIFY', 'DEBATE', 'DECIDE', 'PERSUADE', 'EXECUTE', 'LEARN')
etapas = [(t.strip(), i + 1) for i, t in enumerate(L) if t.strip() in ROTULOS]
fuentes = []
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    fuentes.append(('GRAFO', json.loads(l)))
for p in glob.glob('cuarentena/scott_radical_candor/*.json'):
    fuentes.append(('bandeja', json.load(io.open(p, encoding='utf-8'))))
print('poblacion: dataset/nodos.jsonl mas cuarentena/scott_radical_candor')
print('los rotulos se leen de %s con grep -n, no se teclean' % RUTA)
print()
print('| rotulo de etapa | linea del rotulo | nodo cuyo tramo declarado lo cubre |')
print('|---|---:|---|')
for rot, ln in etapas:
    quien = []
    for sede, n in fuentes:
        m = re.search(r'cap_07\.md, lineas (\d+) a (\d+)', n.get('resumen_teorico', ''))
        if not m:
            continue
        if int(m.group(1)) <= ln <= int(m.group(2)):
            quien.append('`%s` (%s)' % (n['id'], sede))
    print('| `%s` | `L%d` | %s |'
          % (rot, ln, ', '.join(sorted(set(quien))) if quien else '**NINGUNO: es cola**'))
