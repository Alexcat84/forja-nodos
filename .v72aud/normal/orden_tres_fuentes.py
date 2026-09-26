# ACTA 71: el orden de entrada por tres fuentes: las filas 1 a 20 de .v71ext/orden.txt, las 20 ultimas filas del grafo
# (src/aduana.py anexa cada nodo nuevo al final) y la numeracion de los ficheros .v72ext/insertar_NN_<id>.txt.
import glob, json, os, re
orden = []
for l in open('.v71ext/orden.txt', encoding='utf-8'):
    m = re.match(r'(\d+)\s+(\S+)\s+cap_', l)
    if m:
        orden.append(m.group(2))
orden = orden[:20]
grafo = [json.loads(l)['id'] for l in open('dataset/nodos.jsonl', encoding='utf-8')][-20:]
ins = [re.sub(r'^insertar_\d\d_|\.txt$', '', os.path.basename(f)) for f in sorted(glob.glob('.v72ext/insertar_[0-9][0-9]_*.txt'))]
print('filas leidas de .v71ext/orden.txt: %d | ultimas filas del grafo: %d | ficheros insertar_NN: %d' % (len(orden), len(grafo), len(ins)))
print('las tres en el mismo orden, fila a fila: %s' % ('SI' if orden == grafo == ins else 'NO'))
