# -*- coding: utf-8 -*-
"""ACTA 67: el orden del extractor (.v68ext/orden.txt, filas 1 a 20) contra mis seis restricciones selladas en la fase ciega
(.v68aud/restricciones_orden.py, que se corre tal cual y se lee su salida), y la huella de las 20 fichas de hoy contra mis
huellas al barrer (.v68aud/huellas_al_barrer.txt) y contra los blobs que su 68.4.e imprime."""
import io, re, subprocess, hashlib, sys
sys.stdout.reconfigure(encoding="utf-8")
orden = []
for l in io.open('.v68ext/orden.txt', encoding='utf-8'):
    m = re.match(r'^(\d+)\s+(\S+)\s+cap_0[56]', l)
    if m: orden.append(m.group(2))
pos = {n: i + 1 for i, n in enumerate(orden)}
print('filas en su orden: %d | distintas: %d | iguales a mis 20: %s' % (len(orden), len(set(orden)),
      set(orden) == set(x.strip() for x in io.open('.v68aud/los20.txt', encoding='utf-8') if x.strip())))
sal = subprocess.run([sys.executable, '.v68aud/restricciones_orden.py'], capture_output=True).stdout.decode('utf-8')
for l in sal.split('\n'):
    m = re.match(r'^  (\S+)\s+antes que (\S+)\s+(.*?)\s+(?:el orden del libro|EL ORDEN DEL LIBRO)', l)
    if not m: continue
    a, b, por = m.groups()[:3]
    print('  %-50s (fila %2d) antes que %-50s (fila %2d) | %-44s | %s' % (a, pos[a], b, pos[b], por[:44], 'LA CUMPLE' if pos[a] < pos[b] else 'LA VIOLA'))
