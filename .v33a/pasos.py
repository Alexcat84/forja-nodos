# PRIMERA LINEA (HEREDADO 4): CERO IDS TECLEADOS. Los ids salen de .v33a/tanda_ids.txt.
import json, io, sys
ids = [l.strip() for l in io.open('.v33a/tanda_ids.txt',encoding='utf-8') if l.strip()]
d = {}
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip():
        o = json.loads(l); d[o['id']] = o
sal = io.open('.v33a/pasos_12.txt','w',encoding='utf-8')
for n,i in enumerate(ids,1):
    o = d[i]
    sal.write("\n===== %2d  %s  (%d pasos) =====\n" % (n, i, len(o['pasos_accionables'])))
    sal.write("TITULO: %s\n" % o['titulo'])
    sal.write("NOMBRE_LARGO: %s\n" % o['denominaciones']['nombre_largo'])
    sal.write("ACTIVA: %s\n" % o['condiciones_activacion'])
    sal.write("ENTREGABLE: %s\n" % o['entregable_esperado'])
    for k,p in enumerate(o['pasos_accionables'],1):
        sal.write("  %2d. %s\n" % (k,p))
    sal.write("RESUMEN: %s\n" % o['resumen_teorico'])
sal.close()
print("escrito .v33a/pasos_12.txt con %d nodos" % len(ids))
