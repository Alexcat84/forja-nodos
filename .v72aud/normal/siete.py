# ACTA 71: las fichas que quedan en la bandeja de Grove, leidas del fichero vivo: su capitulo (de UNIDAD DE ORIGEN o de la cita)
# y su cuenta de pasos, con la suma por capitulo y la total (R7).
import glob, json, os, re, collections
c = collections.Counter(); p = collections.Counter()
for f in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    nodo = d.get('nodo', d)
    pasos = d.get('pasos_accionables') or []
    cap = re.search(r'cap_\d\d', json.dumps(d, ensure_ascii=False)).group(0)
    c[cap] += 1; p[cap] += len(pasos)
    print('%s %-50s pasos %d' % (cap, os.path.basename(f)[:-5], len(pasos)))
print('fichas por capitulo: %s | suma: %d' % (dict(sorted(c.items())), sum(c.values())))
print('pasos por capitulo: %s | suma: %d' % (dict(sorted(p.items())), sum(p.values())))
