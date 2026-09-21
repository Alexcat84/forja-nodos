# -*- coding: utf-8 -*-
"""La deuda viva de la linea, recontada del propio fichero: anotaciones tipo deuda
menos las que tienen una linea tipo pago con el mismo id."""
import io,sys,json
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
d=[json.loads(l) for l in open('docs/loop/DEUDA.jsonl',encoding='utf-8') if l.strip()]
deudas={x['id']:x for x in d if x.get('tipo')=='deuda'}
pagos={x['id'] for x in d if x.get('tipo')=='pago'}
vivas=sorted(set(deudas)-pagos)
print("lineas del fichero        : %d" % len(d))
print("deudas anotadas           : %d" % len(deudas))
print("deudas con linea de pago  : %d  (%s)" % (len(pagos), ", ".join(sorted(pagos))))
print("DEUDA VIVA                : %d  (%s)" % (len(vivas), ", ".join(vivas)))
print()
for i in sorted(vivas):
    print("  %s  [%s]  %s" % (i, deudas[i].get('especie','?'), deudas[i]['que'][:105]))
