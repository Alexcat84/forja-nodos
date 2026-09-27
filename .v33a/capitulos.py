# PRIMERA LINEA (HEREDADO 4): CERO IDS Y CERO NOMBRES DE CAPITULO TECLEADOS. Los capitulos
# salen de un patron cap_NN.md buscado dentro del resumen_teorico de cada nodo del dataset,
# y los ficheros que existen salen de un glob sobre fuentes/.
import json, io, re, glob, os, collections
hay = sorted(os.path.basename(p) for p in glob.glob('fuentes/scott_radical_candor/cap_*.md'))
c = collections.Counter(); pasos = collections.Counter(); sin = 0; tot = 0
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    if not l.strip(): continue
    o = json.loads(l)
    if (o.get('fuentes') or [{}])[0].get('clave') != 'scott_radical_candor': continue
    tot += 1
    m = re.findall(r'cap_(\d\d)\.md', o.get('resumen_teorico',''))
    if m: c[m[0]] += 1; pasos[m[0]] += len(o['pasos_accionables'])
    else: sin += 1
print("NODOS DE scott_radical_candor EN EL GRAFO, por capitulo del fichero fuente")
print("  (el capitulo se saca del patron cap_NN.md dentro del resumen_teorico; dataset de 282 nodos)")
print()
print("  %-12s %-12s %8s %8s" % ('fichero','en fuentes/','nodos','pasos'))
for f in hay:
    n = f[4:6]
    print("  %-12s %-12s %8d %8d" % (f, 'SI', c.get(n,0), pasos.get(n,0)))
print()
print("  nodos de scott en el grafo: %d   sin capitulo legible en su resumen: %d" % (tot, sin))
