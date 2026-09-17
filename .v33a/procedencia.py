# PRIMERA LINEA (HEREDADO 4): CERO IDS TECLEADOS. Los ids salen de .v33a/tanda_ids.txt,
# escrito por .v33a/tanda.py del git diff del dataset. Los campos salen del esquema.
import json, io
ids = [l.strip() for l in io.open('.v33a/tanda_ids.txt',encoding='utf-8') if l.strip()]
d = {}
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip():
        o = json.loads(l); d[o['id']] = o
print("PROCEDENCIA Y VOLUMEN DE LOS 12 QUE ENTRAN, leido de dataset/nodos.jsonl (282 nodos, arbol 1ae327e)")
print()
print("  %-44s %5s  %-24s %s" % ('id','pasos','fuente','localizador'))
tot = 0
for i in ids:
    o = d[i]
    f = (o.get('fuentes') or [{}])[0]
    loc = f.get('localizador') or f.get('capitulo') or f.get('seccion') or '(sin localizador)'
    p = len(o.get('pasos_accionables') or [])
    tot += p
    print("  %-44s %5d  %-24s %s" % (i[:44], p, f.get('clave','?'), loc))
print()
print("  TOTAL de pasos_accionables en los 12 nodos que entran: %d" % tot)
