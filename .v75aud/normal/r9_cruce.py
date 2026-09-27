# ACTA 74: R9 sobre los 18 pasos de hoy de dar_elogio_disciplina_igual_critica, los dos patrones a la vez: el suyo
# (.v75ext/r9.py, linea PAT) y el mio (.v75aud/cap13_despues.py, linea PAT), leidos de sus ficheros y no copiados.
# Para cada paso: si casa el suyo, si casa el mio, y lo que casa. Solo lee el grafo.
import io, json, re, collections
def pat(f):
    t = io.open(f, encoding='utf-8').read()
    src = t[t.index('PAT = re.compile('):]
    src = src[:src.index(', re.I)') + len(', re.I)')]
    ns = {'re': re}; exec(src, ns); return ns['PAT']
SUYO, MIO = pat('.v75ext/r9.py'), pat('.v75aud/cap13_despues.py')
n = [d for d in map(json.loads, io.open('dataset/nodos.jsonl', encoding='utf-8')) if d['id'] == 'dar_elogio_disciplina_igual_critica'][0]
c = collections.Counter()
for k, p in enumerate(n['pasos_accionables'], 1):
    s = [m.group(0) for m in SUYO.finditer(p)]; m_ = [m.group(0) for m in MIO.finditer(p)]
    clave = ('suyo' if s else '') + ('+' if s and m_ else '') + ('mio' if m_ else '')
    c[clave or 'ninguno'] += 1
    if s or m_:
        print('paso %2d | suyo: %s | mio: %s' % (k, ' / '.join(s) or '-', ' / '.join(m_) or '-'))
print('pasos: %d | por patron que casa: %s | suma: %d' % (len(n['pasos_accionables']), dict(c), sum(c.values())))
