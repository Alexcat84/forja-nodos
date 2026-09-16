import json, io, glob
nodos = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8')]
ver = [l for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]
nc = sum(1 for l in ver
         if any(a.get('no_consumada') for a in json.loads(l).get('anotaciones', [])))
print('| lo que mido | al abrir | **al cerrar** | movimiento |')
print('|---|---:|---:|---:|')
print('| nodos en `dataset/nodos.jsonl` | 243 | **%d** | **+%d** |' % (len(nodos), len(nodos) - 243))
print('| veredictos en `bitacora/VEREDICTOS.jsonl` | 289 | **%d** | **+%d** |' % (len(ver), len(ver) - 289))
print('| de ellos, con `no_consumada: true` | 14 | **%d** | **+%d** |' % (nc, nc - 14))
print('| nodos con fuente `scott_radical_candor` | 40 | **%d** | **+%d** |'
      % (sum(1 for n in nodos if any(f['clave'] == 'scott_radical_candor' for f in n['fuentes'])),
         sum(1 for n in nodos if any(f['clave'] == 'scott_radical_candor' for f in n['fuentes'])) - 40))
b4 = len(glob.glob('cuarentena/scott_radical_candor/*.json'))
a4 = len(glob.glob('cuarentena/_insertados/scott_radical_candor/*.json'))
print('| bandeja del lote 4 | 102 | **%d** | **%d** |' % (b4, b4 - 102))
print('| archivados del lote 4 | 40 | **%d** | **+%d** |' % (a4, a4 - 40))
print('| bandeja del lote 5 | 3 | **%d** | **%d** |'
      % (len(glob.glob('cuarentena/marquet_turn_the_ship/*.json')),
         len(glob.glob('cuarentena/marquet_turn_the_ship/*.json')) - 3))
print('| aristas del grafo, contadas por `nodos_siguientes` | | **%d** | |'
      % sum(len(n['nodos_siguientes']) for n in nodos))
print('| lote 4 insertado, por ciento del total de 142 | 28 | **%d** | **+%d** |'
      % (round(a4 * 100.0 / 142), round(a4 * 100.0 / 142) - 28))
