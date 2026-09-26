# ACTA 77: R9 sobre los 110 pasos de hoy de las 20 fichas de Marquet, los dos patrones a la vez: el suyo (.v78ext/r9.py, linea PAT,
# el de la 76 sin tocar segun su cabecera) y el mio (.v75aud/cap13_despues.py, linea PAT), leidos de sus ficheros y no copiados. Copia
# de .v76aud/normal/r9_cruce.py con las rutas cambiadas. Para cada paso que solo casa el mio: su marca y su nota. Solo lee. R7.
import io, json, re, collections, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
def pat(f):
    t = io.open(f, encoding='utf-8').read()
    src = t[t.index('PAT = re.compile('):]
    src = src[:src.index(', re.I)') + len(', re.I)')]
    ns = {'re': re}; exec(src, ns); return ns['PAT']
SUYO, MIO = pat('.v78ext/r9.py'), pat('.v75aud/cap13_despues.py')
nota = {}
for l in io.open('.v78ext/fidelidad.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    c = [x.strip() for x in l.split('|')]
    nota[(c[0], int(c[1]))] = (c[2], ' | '.join(c[4:]))
c = collections.Counter()
for i in [l.strip() for l in io.open('.v78aud/las20.txt', encoding='utf-8') if l.strip()]:
    f = json.load(io.open('cuarentena/marquet_turn_the_ship/%s.json' % i, encoding='utf-8'))
    for k, p in enumerate(f['pasos_accionables'], 1):
        s = [m.group(0) for m in SUYO.finditer(p)]; m_ = [m.group(0) for m in MIO.finditer(p)]
        clave = ('suyo' if s else '') + ('+' if s and m_ else '') + ('mio' if m_ else '')
        c[clave or 'ninguno'] += 1
        if m_ and not s:
            print('%s paso %d | solo el mio: %s | su marca %s | su nota: %s' % (i, k, ' / '.join(m_), nota[(i, k)][0], nota[(i, k)][1][:230]))
print('pasos: %d | por patron que casa: %s | suma: %d' % (sum(c.values()), dict(c), sum(c.values())))
