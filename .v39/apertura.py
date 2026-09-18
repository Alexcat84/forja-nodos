import json, subprocess, glob, os

def sh(c):
    return subprocess.run(c, shell=True, capture_output=True, text=True).stdout.strip()

nodos = [json.loads(l) for l in open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
ver = [json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]
sig = sum(len(n.get('nodos_siguientes', [])) for n in nodos)
prev = sum(len(n.get('nodos_previos', [])) for n in nodos)
noc = sum(1 for v in ver if any(
    a.get('no_consumada') is True for a in v.get('anotaciones', [])) if isinstance(v.get('anotaciones'), list))
band = len(glob.glob('cuarentena/scott_radical_candor/*.json'))
ins = len(glob.glob('cuarentena/_insertados/scott_radical_candor/*.json'))
band5 = len(glob.glob('cuarentena/marquet_turn_the_ship/*.json'))
tot = band + ins

filas = [
    ('rama', sh('git rev-parse --abbrev-ref HEAD'), '`git rev-parse --abbrev-ref HEAD`'),
    ('commit al abrir mi turno', '`%s`' % sh('git rev-parse --short HEAD'), '`git rev-parse --short HEAD`'),
    ('nodos en `dataset/nodos.jsonl`', '**%d**' % len(nodos), '`dataset/nodos.jsonl`'),
    ('veredictos en `bitacora/VEREDICTOS.jsonl`', '**%d**' % len(ver), '`bitacora/VEREDICTOS.jsonl`'),
    ('de ellos, con alguna anotacion `no_consumada: true`', '**%d**' % noc, '`bitacora/VEREDICTOS.jsonl`'),
    ('aristas por `nodos_siguientes`', '**%d**' % sig, '`dataset/nodos.jsonl`'),
    ('aristas por `nodos_previos`', '**%d**' % prev, '`dataset/nodos.jsonl`'),
    ('candidatos en bandeja, lote 4', '**%d**' % band, 'PATRON: `cuarentena/scott_radical_candor/*.json`'),
    ('insertados y archivados, lote 4', '**%d**' % ins, 'PATRON: `cuarentena/_insertados/scott_radical_candor/*.json`'),
    ('candidatos en bandeja, lote 5', '**%d**' % band5, 'PATRON: `cuarentena/marquet_turn_the_ship/*.json`'),
    ('lote 4 insertado sobre `%d`, por ciento' % tot, '**%s**' % ('%.1f' % (100.0 * ins / tot)).replace('.', ','), '`cuarentena/_insertados/scott_radical_candor/`'),
]
out = ['| pieza | valor | de donde sale |', '|---|---:|---|']
for a, b, c in filas:
    out.append('| %s | %s | %s |' % (a, b, c))
print('\n'.join(out))
