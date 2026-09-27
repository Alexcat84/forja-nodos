import json, io, re
L = [l for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8').read().split('\n') if l.strip()]
ran = io.open('.v30e/rancios_tras_declarar.txt', encoding='utf-8').read()
sin_huella = [int(m) for m in re.findall(r'\[SIN HUELLA\][^\n]*?\(linea (\d+),', ran)]
rancio = [int(m) for m in re.findall(r'\[RANCIO\][^\n]*?\(linea (\d+),', ran)]
def declarada(n):
    d = json.loads(L[n - 1])
    return any('VIGENCIA DECLARADA' in (a.get('texto') or '')
               for a in d.get('anotaciones', []))
print('EL BLOQUE DE VIGENCIA, CRUZADO CONTRA LA MARCA QUE LO DECLARA')
print('  hallazgos del instrumento : %d' % (len(rancio) + len(sin_huella)))
print('  RANCIO                    : %d, declarados %d, sin declarar %d'
      % (len(rancio), sum(1 for n in rancio if declarada(n)),
         sum(1 for n in rancio if not declarada(n))))
print('  SIN HUELLA                : %d, declarados %d, sin declarar %d'
      % (len(sin_huella), sum(1 for n in sin_huella if declarada(n)),
         sum(1 for n in sin_huella if not declarada(n))))
print('  las lineas SIN HUELLA     : %s' % ', '.join(str(n) for n in sin_huella))
