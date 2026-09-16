import json, io
L = [l for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]
nuevas = L[289:]
aduana = declar_arista = declar_sano = 0
for l in nuevas:
    d = json.loads(l)
    if d.get('levantada_por') == ['lectura declarada']:
        if d.get('arista'):
            declar_arista += 1
        else:
            declar_sano += 1
    else:
        aduana += 1
print('LAS LINEAS NUEVAS DE LA BITACORA, REPARTIDAS POR QUIEN LAS ESCRIBIO')
print('  lineas al abrir : 289')
print('  lineas al cerrar: %d' % len(L))
print('  lineas nuevas   : %d' % len(nuevas))
print('    vecinos levantados por la aduana y juzgados   : %d' % aduana)
print('    aristas D.37 declaradas con forja.py arista   : %d' % declar_arista)
print('    veredictos declarados por lectura sin arista  : %d' % declar_sano)
print('    suma                                          : %d'
      % (aduana + declar_arista + declar_sano))
print('  lineas ANOTADAS sin aniadir linea nueva (D.15)  : 8')
