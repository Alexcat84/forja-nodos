"""ACTA 79: las 54 lineas que la vuelta 80 escribio en la bitacora (1173 a 1226), una a una, contra tres sedes:
.v78ext/veredictos_listos.txt (las lineas preparadas, letra a letra), mis filas dirigidas de .v78aud/vecinos_tabla.txt (el par y
sus tres seniales al digito) y mis clases selladas de .v78aud/mis_clases.tsv (la clase del par sin orden). Solo lee."""
import json, re, collections

bit = [json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]
nuevas = bit[1172:]

listas, cand = {}, None
for l in open('.v78ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '):
        cand = l[3:].strip()
    elif l and not l.startswith('#') and '|' in l and cand:
        v, ver, razon = l.split('|', 2)
        listas[(cand, v)] = (ver, razon)

filas = {}
for l in open('.v78aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^\s+(\S+)\s+>\s+(\S+)\s+(grafo|bandeja)\s+(\S+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)', l)
    if m:
        filas[(m.group(1), m.group(2))] = (m.group(4), float(m.group(5)), float(m.group(6)), float(m.group(7)))

clases = {}
for i, l in enumerate(open('.v78aud/mis_clases.tsv', encoding='utf-8')):
    if i == 0 or not l.strip():
        continue
    a, b, c = l.rstrip('\n').split('\t')[:3]
    clases[frozenset((a, b))] = c

tipo = collections.Counter()
res = collections.Counter()
malas = []
vistos = set()
for n, r in enumerate(nuevas, start=1173):
    if r.get('veredicto') == 'CORREGIDO':
        tipo['CORREGIDO (d183)'] += 1
        continue
    if 'lectura declarada' in (r.get('levantada_por') or []):
        tipo['arista por lectura'] += 1
        continue
    tipo['linea --veredicto'] += 1
    c, v = r['candidato'], r['vecino']
    vistos.add((c, v))
    lista = listas.get((c, v))
    fila = filas.get((c, v))
    s = r.get('senales', {})
    ok_lista = lista is not None and lista[0] == r['veredicto'] and lista[1] == r['razon']
    ok_fila = fila is not None and fila[0] in r.get('levantada_por', []) and (fila[1], fila[2], fila[3]) == (
        s.get('similitud_texto'), s.get('familia_id'), s.get('paso_contra_nodo'))
    ok_clase = clases.get(frozenset((c, v))) == r['veredicto']
    clave = ('lista ' + ('SI' if ok_lista else 'NO'), 'fila ' + ('SI' if ok_fila else 'NO'), 'clase ' + ('SI' if ok_clase else 'NO'))
    res[' / '.join(clave)] += 1
    if not (ok_lista and ok_fila and ok_clase):
        malas.append((n, c, v, clave))

print('lineas nuevas de la bitacora: %d (de la %d a la %d) | por tipo: %s | suma: %d' % (
    len(nuevas), 1173, 1172 + len(nuevas), dict(tipo), sum(tipo.values())))
print('lineas --veredicto contra la preparada (veredicto y razon letra a letra) / mi fila dirigida (senial y tres cifras) / mi clase sellada:')
print('  %s | suma: %d' % (dict(res), sum(res.values())))
print('  que no casan en alguna: %d %s' % (len(malas), malas))
print('lineas preparadas: %d | escritas: %d | preparadas sin escribir: %d | escritas sin preparar: %d' % (
    len(listas), len(vistos), len(set(listas) - vistos), len(vistos - set(listas))))
print('filas dirigidas de mi barrido con candidato de las 20: %d | sin linea en la bitacora: %d %s' % (
    len(filas), len(set(filas) - vistos), sorted(set(filas) - vistos)))
print('veredictos de las lineas --veredicto: %s' % dict(collections.Counter(r['veredicto'] for r in nuevas
      if r.get('veredicto') != 'CORREGIDO' and 'lectura declarada' not in (r.get('levantada_por') or []))))
