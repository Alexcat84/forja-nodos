# PRIMERA LINEA (HEREDADO 4): CERO ROTULOS Y CERO LINEAS TECLEADAS. Los rotulos se sacan del
# propio fichero fuente por forma (linea corta, sin punto final, entre lineas en blanco), y
# lo unico tecleado es el nombre del fichero, que es el sujeto del instrumento.
import io, re, json, glob, os
RUTA = 'fuentes/scott_radical_candor/cap_08.md'
L = io.open(RUTA, encoding='utf-8').read().split('\n')
ini = [n for n,l in enumerate(L) if l.strip()=='---'][1] + 1
rot = []
for n in range(ini, len(L)):
    t = L[n].strip()
    if not t or t == '* * *': continue
    if len(t.split()) > 12: continue
    if t.endswith('.') or t.endswith('?') or t.endswith(':'): continue
    ant = L[n-1].strip() if n else ''
    sig = L[n+1].strip() if n+1 < len(L) else ''
    if ant == '' and sig == '':
        rot.append((n+1, t))
# el cuerpo de cada rotulo llega hasta el rotulo siguiente
print("ROTULOS QUE EL FICHERO %s TRAE, sacados por forma y no tecleados" % RUTA)
print("  criterio: linea de 12 palabras o menos, sin punto ni interrogacion ni dos puntos al")
print("  final, con una linea en blanco antes y otra despues. %d rotulos." % len(rot))
print()
# nodos del grafo que citan cada rotulo: se casa por el numero de linea del resumen_teorico
import collections
nodos = collections.defaultdict(list)
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    if not l.strip(): continue
    o = json.loads(l)
    r = o.get('resumen_teorico','')
    if 'cap_08.md' not in r: continue
    m = re.search(r'lineas (\d+) a (\d+)', r)
    if m: nodos[(int(m.group(1)), int(m.group(2)))].append(o['id'])
print("  %-5s %-52s %-6s %s" % ('linea','rotulo','cuerpo','nodo del grafo que lo cubre'))
for k,(n,t) in enumerate(rot):
    fin = rot[k+1][0] if k+1 < len(rot) else len(L)
    cubre = [i for (a,b),ids in nodos.items() if a <= n <= b for i in ids]
    cuerpo = fin - n - 1
    print("  L%-4d %-52s %-6d %s" % (n, t[:52], cuerpo, ', '.join(cubre) if cubre else '--- NINGUNO ---'))
print()
print("  rotulos cubiertos por un nodo: %d   sin nodo: %d"
      % (len([1 for k,(n,t) in enumerate(rot) if any(a<=n<=b for (a,b) in nodos)]),
         len([1 for k,(n,t) in enumerate(rot) if not any(a<=n<=b for (a,b) in nodos)])))
print("  nodos distintos de cap_08 en el grafo: %d" % len({i for v in nodos.values() for i in v}))
