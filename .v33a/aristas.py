# PRIMERA LINEA (HEREDADO 4): CERO IDS TECLEADOS. Los ids de la tanda salen de
# .v33a/tanda_ids.txt (generado del git diff del dataset) y el resto de dataset/nodos.jsonl.
import json, io
ids = [l.strip() for l in io.open('.v33a/tanda_ids.txt',encoding='utf-8') if l.strip()]
d = {}
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip():
        o = json.loads(l); d[o['id']] = o
print("CABLEADO Y ATRIBUCIONES DE LOS 12 QUE ENTRAN (dataset de 282 nodos, arbol 1ae327e)")
print()
ent = sal_ = 0
for i in ids:
    o = d[i]
    prev = o.get('nodos_previos') or []
    sig = o.get('nodos_siguientes') or []
    atr = o.get('atribuciones') or []
    ent += len(prev); sal_ += len(sig)
    print("  %-44s previos %d %-46s siguientes %d %-46s atribuciones %d"
          % (i[:44], len(prev), str(prev)[:46], len(sig), str(sig)[:46], len(atr)))
    for a in atr:
        print("        ATRIBUCION: %s" % json.dumps(a, ensure_ascii=False))
print()
print("  aristas de entrada escritas en los 12: %d   de salida: %d" % (ent, sal_))
print()
# quien apunta a los 12 desde fuera de los 12
print("QUIEN LOS NOMBRA DESDE FUERA DE LOS 12:")
tan = set(ids); n = 0
for k,o in d.items():
    if k in tan: continue
    for s in (o.get('nodos_siguientes') or []):
        if s in tan: print("  %s  --siguiente-->  %s" % (k, s)); n += 1
    for p in (o.get('nodos_previos') or []):
        if p in tan: print("  %s  --previo-->  %s" % (k, p)); n += 1
print("  total: %d" % n)
