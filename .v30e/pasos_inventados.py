import json, glob, re
IDS = [l.strip() for l in open('.v30e/tanda.txt', encoding='utf-8') if l.strip()]
tot = 0
print('| capitulo | nodos | **pasos escritos** | **PUENTE** | **PASOS INVENTADOS** |')
print('|---|---:|---:|---:|---:|')
for i in IDS:
    d = json.load(open('cuarentena/scott_radical_candor/%s.json' % i, encoding='utf-8'))
    tot += len(d['pasos_accionables'])
print('| **`cap_07`** (lote 4, `scott_radical_candor`) | %d | **%d** | **0** | **0,00 por ciento** |' % (len(IDS), tot))
print('| **total del tramo de esta vuelta** | %d | **%d** | **0** | **0,00 por ciento** |' % (len(IDS), tot))
