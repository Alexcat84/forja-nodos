# PRIMERA LINEA (HEREDADO 4): ESTE INSTRUMENTO NO TIENE NI UN ID TECLEADO DENTRO.
# Todo sale de dataset/nodos.jsonl, bitacora/VEREDICTOS.jsonl y del arbol de cuarentena/.
import json, io, os, glob, subprocess, sys

def lineas(ruta):
    n = 0
    for l in io.open(ruta, encoding='utf-8'):
        if l.strip(): n += 1
    return n

hash_ = subprocess.check_output(['git','rev-parse','HEAD']).decode().strip()
sucio = subprocess.check_output(['git','status','--porcelain']).decode().strip().splitlines()
print("POBLACION MEDIDA HOY. arbol: %s  ficheros con cambio sin commitear: %d" % (hash_[:7], len(sucio)))
print()
print("  dataset/nodos.jsonl            : %4d nodos" % lineas('dataset/nodos.jsonl'))
print("  bitacora/VEREDICTOS.jsonl      : %4d lineas" % lineas('bitacora/VEREDICTOS.jsonl'))
print("  config/pares_mutuos.jsonl      : %4d lineas" % lineas('config/pares_mutuos.jsonl'))
print()
tot_b = tot_i = 0
for d in sorted(glob.glob('cuarentena/*')):
    if not os.path.isdir(d) or os.path.basename(d).startswith('_'): continue
    libro = os.path.basename(d)
    band = len(glob.glob(os.path.join(d, '*.json')))
    ins = len(glob.glob(os.path.join('cuarentena/_insertados', libro, '*.json')))
    if band or ins:
        print("  cuarentena/%-28s bandeja %3d   _insertados %3d" % (libro, band, ins))
    tot_b += band; tot_i += ins
print("  %-39s bandeja %3d   _insertados %3d" % ('TOTAL de cuarentena/', tot_b, tot_i))
