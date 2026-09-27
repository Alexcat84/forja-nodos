import json, io, os, glob
vivos = set(json.loads(l)['id'] for l in io.open('dataset/nodos.jsonl', encoding='utf-8'))
arch = [os.path.basename(p)[:-5]
        for p in glob.glob('cuarentena/_insertados/scott_radical_candor/*.json')]
dentro = sum(1 for a in arch if a in vivos)
print('%d dentro del grafo y %d fuera, %d mas %d igual a %d'
      % (dentro, len(arch) - dentro, dentro, len(arch) - dentro, len(arch)))
