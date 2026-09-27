# PRIMERA LINEA (HEREDADO 4): CERO IDS Y CERO CAPITULOS TECLEADOS. El capitulo de cada
# candidato en bandeja sale del patron cap_NN.md dentro de su propio resumen_teorico.
import json, io, glob, re, collections, os
c = collections.Counter(); sin = 0; tot = 0
for p in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    o = json.load(io.open(p, encoding='utf-8'))
    tot += 1
    m = re.findall(r'cap_(\d\d)\.md', o.get('resumen_teorico',''))
    if m: c[m[0]] += 1
    else: sin += 1
print("LO QUE ESPERA EN cuarentena/scott_radical_candor/ HOY (arbol 1ae327e), por capitulo")
print("  el capitulo sale del resumen_teorico del propio candidato, no de una lista")
for k in sorted(c):
    print("  cap_%s.md   %3d candidatos" % (k, c[k]))
print("  sin capitulo legible: %d" % sin)
print("  TOTAL en bandeja: %d" % tot)
