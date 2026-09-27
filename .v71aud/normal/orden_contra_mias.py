# ACTA 70: el orden del extractor (.v71ext/orden.txt, filas 1 a 20) contra mis restricciones selladas
# (las que imprime .v71aud/restricciones_orden.py en la fase ciega). Solo lee.
import io, re, subprocess, collections
pos = {}
for l in io.open('.v71ext/orden.txt', encoding='utf-8'):
    m = re.match(r'^(\d+)\s+(\S+)\s+cap_', l)
    if m: pos[m.group(2)] = int(m.group(1))
print('filas del orden: %d' % len(pos))
sal = subprocess.run(['python', '.v71aud/restricciones_orden.py'], capture_output=True, text=True, encoding='utf-8').stdout
est = collections.Counter()
for l in sal.splitlines():
    m = re.match(r'^\s+(\S+)\s+antes que (\S+)\s+(CONTINUA|arista por lectura|D\.36, solo lo levanta \S+)\s+', l)
    if not m: continue
    a, b, tipo = m.groups(); tipo = 'obliga' if not tipo.startswith('D.36') else 'D.36 de un solo lado'
    ok = pos[a] < pos[b]
    est[(tipo, 'la cumple' if ok else 'LA VIOLA')] += 1
    print('  %-3s %-58s antes que %-3s %-58s %s | %s' % (pos[a], a, pos[b], b, tipo, 'la cumple' if ok else 'LA VIOLA'))
print('restricciones:', {'%s, %s' % k: v for k, v in sorted(est.items())}, '| suma:', sum(est.values()))
