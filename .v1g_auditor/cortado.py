# cortado.py: suma el cuerpo de las unidades que la vuelta dice haber cortado,
# leyendo la lista de la propia carpeta de piezas del extractor (no tecleada).
import glob, os, re, subprocess, sys, json
unidades = sorted(os.path.basename(p)[len('piezas_'):-4].replace('cap','cap_') for p in glob.glob('.gerber_v1/piezas_cap*.txt'))
suma = 0
for u in unidades:
    lineas = open('fuentes/gerber_emyth/%s.md' % u, encoding='utf-8', errors='replace').read().splitlines()
    cortes = [i for i, l in enumerate(lineas) if l.strip() == '---']
    suma += sum(len(l.split()) for l in lineas[cortes[1]+1:])
libro = 0
for p in sorted(glob.glob('fuentes/gerber_emyth/cap_*.md')):
    lineas = open(p, encoding='utf-8', errors='replace').read().splitlines()
    cortes = [i for i, l in enumerate(lineas) if l.strip() == '---']
    libro += sum(len(l.split()) for l in lineas[cortes[1]+1:])
print("unidades con fichero de piezas :", len(unidades), " ", " ".join(unidades))
print("suma de su cuerpo              :", suma)
print("cuerpo del libro entero        :", libro)
print("por ciento cortado             : %.1f" % (100.0 * suma / libro))
ficha = json.load(open('fuentes/FUENTES_CANONICAS.json', encoding='utf-8'))
def buscar(o):
    if isinstance(o, dict):
        if o.get('clave') == 'gerber_emyth': return o
        for v in o.values():
            r = buscar(v)
            if r: return r
    if isinstance(o, list):
        for v in o:
            r = buscar(v)
            if r: return r
f = buscar(ficha)
print("la tabla canonica dice         :", {k: v for k, v in (f or {}).items() if 'palabra' in k or k in ('clave','unidades')})
