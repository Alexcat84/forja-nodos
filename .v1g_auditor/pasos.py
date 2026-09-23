# pasos.py: pasos por candidato y por unidad de origen. La unidad la saca del
# resumen_teorico con un patron, no de una lista tecleada.
import glob, json, re, collections
porcap = collections.Counter(); nodoscap = collections.Counter(); total = 0
for r in sorted(glob.glob('cuarentena/gerber_emyth/*.json')):
    d = json.load(open(r, encoding='utf-8'))
    n = len(d['pasos_accionables'])
    m = re.search(r'fuentes/gerber_emyth/(cap_\d+)\.md', d.get('resumen_teorico',''))
    u = m.group(1) if m else 'SIN UNIDAD'
    porcap[u] += n; nodoscap[u] += 1; total += n
    print("%-46s %-8s %3d pasos" % (d['id'], u, n))
print()
print("%-8s %6s %6s" % ("unidad","nodos","pasos"))
for u in sorted(porcap): print("%-8s %6d %6d" % (u, nodoscap[u], porcap[u]))
print("%-8s %6d %6d" % ("TOTAL", sum(nodoscap.values()), total))
