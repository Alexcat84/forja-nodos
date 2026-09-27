# Fase ciega de la 73 (copia de .v71aud/vecinos_tabla.py con la lista cambiada a las 7 de cap_15, cap_16 y cap_17): lee los .v73aud/vecinos_<id>.json que escribio .v73aud/barrido_uno.py y publica
# (1) una fila por candidato con su poblacion y cuantos vecinos levanta, por sede;
# (2) una fila por vecino levantado (candidato, vecino, sede, senial que lo levanta y sus tres cifras);
# (3) los pares SIN ORDEN, con el lado o los lados que los levantan. Solo lee.
import io, json, glob, os, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
tanda = [l.strip() for l in io.open('.v73aud/los7.txt', encoding='utf-8') if l.strip()]
orden = tanda
filas = []; pares = collections.OrderedDict(); falta = []
print('(1) candidato | poblacion | vecinos | en grafo | en bandeja')
for i in orden:
    f = '.v73aud/vecinos_%s.json' % i
    if not os.path.exists(f): falta.append(i); continue
    d = json.load(io.open(f, encoding='utf-8'))
    g = sum(v['sede'] == 'grafo' for v in d['vecinos'])
    print('    %-56s %d  %2d  %2d  %2d' % (i, d['grafo'] + d['bandejas'], len(d['vecinos']), g, len(d['vecinos']) - g))
    for v in d['vecinos']:
        s = v['senales']
        filas.append((i, v['id'], v['sede'], '+'.join(v['levantada_por']), s.get('similitud_texto', 0), s.get('familia_id', 0), s.get('paso_contra_nodo', 0)))
        k = tuple(sorted((i, v['id'])))
        pares.setdefault(k, set()).add(i)
print('sin fichero de vecinos: %d %s' % (len(falta), falta))
print('(2) vecino levantado | senial | texto familia paso')
for i, v, sede, por, a, b, c in filas:
    print('    %-54s > %-54s %-7s %-16s %.3f %.3f %.3f' % (i, v, sede, por, a, b, c))
print('filas de vecino: %d' % len(filas))
print('(3) pares sin orden | levantado desde')
dentro = set(tanda)
for (a, b), lados in pares.items():
    tipo = 'tanda-tanda' if a in dentro and b in dentro else 'con fuera'
    print('    %-54s ~ %-54s %-11s %s' % (a, b, tipo, 'los dos' if len(lados) == 2 else 'solo ' + list(lados)[0]))
c = collections.Counter('tanda-tanda' if a in dentro and b in dentro else 'con fuera' for a, b in pares)
print('pares sin orden: %d | %s | suma: %d' % (len(pares), dict(c), sum(c.values())))
