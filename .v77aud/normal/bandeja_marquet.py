# ACTA 76: las fichas de la bandeja de Marquet, leidas del fichero vivo: su capitulo (el primero que nombra la ficha) y su cuenta de
# pasos, con la suma por capitulo y la total (R7). Copia de .v75aud/normal/bandeja_gerber.py con la ruta cambiada.
import glob, json, os, re, collections
c = collections.Counter(); p = collections.Counter()
for f in sorted(glob.glob('cuarentena/marquet_turn_the_ship/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    nodo = d.get('nodo', d)
    pasos = d.get('pasos_accionables') or []
    cap = re.search(r'cap_\d\d', json.dumps(d, ensure_ascii=False)).group(0)
    c[cap] += 1; p[cap] += len(pasos)
    print('%s %-50s pasos %d' % (cap, os.path.basename(f)[:-5], len(pasos)))
print('fichas por capitulo: %s | suma: %d' % (dict(sorted(c.items())), sum(c.values())))
print('pasos por capitulo: %s | suma: %d' % (dict(sorted(p.items())), sum(p.values())))
