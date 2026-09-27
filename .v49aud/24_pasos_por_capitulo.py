# -*- coding: utf-8 -*-
"""PASOS POR CAPITULO de la bandeja de grove, leyendo el cap_NN.md que la ficha declara,
mas la diferencia de pasos contra HEAD~1 y HEAD."""
import io, sys, json, glob, os, re, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def leer(ruta):
    d = json.loads(io.open(ruta, encoding='utf-8').read())
    r = d.get('resumen_teorico', '')
    m = re.search(r'cap_(\d+)\.md', r)
    return ('cap_' + m.group(1) if m else '?'), d

porcap = {}
pasos_hoy = {}
for f in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    cap, d = leer(f)
    porcap.setdefault(cap, [0, 0])
    porcap[cap][0] += 1
    porcap[cap][1] += len(d.get('pasos_accionables') or [])
    pasos_hoy[os.path.basename(f)] = (cap, [p for p in (d.get('pasos_accionables') or [])])
print("PASOS POR CAPITULO EN LA BANDEJA DE grove_high_output (cap del cap_NN.md que la ficha declara)")
for c in sorted(porcap):
    print("   %-8s %2d fichas  %4d pasos" % (c, porcap[c][0], porcap[c][1]))
print()

print("LOS PASOS DE cap_04, FICHA A FICHA, Y SU DIFERENCIA CONTRA HEAD~1 Y HEAD")
for ref in ("HEAD~1", "HEAD"):
    iguales, distintos, ausentes = 0, [], []
    for nombre, (cap, pasos) in sorted(pasos_hoy.items()):
        if cap != 'cap_04':
            continue
        ruta = 'cuarentena/grove_high_output/' + nombre
        try:
            viejo = subprocess.check_output(['git', 'show', '%s:%s' % (ref, ruta)])
            dv = json.loads(viejo.decode('utf-8'))
        except Exception:
            ausentes.append(nombre)
            continue
        if (dv.get('pasos_accionables') or []) == pasos:
            iguales += 1
        else:
            distintos.append(nombre)
    print("   contra %-7s : %2d fichas con los MISMOS pasos, %d distintas %s, %d ausentes %s"
          % (ref, iguales, len(distintos), distintos or '', len(ausentes), ausentes or ''))
