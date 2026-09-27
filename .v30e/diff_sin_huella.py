import io
a = io.open('.v30e/VEREDICTOS_antes_sin_huella.jsonl', encoding='utf-8').read().split('\n')
b = io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8').read().split('\n')
va = [x for x in a if x.strip()]
vb = [x for x in b if x.strip()]
tocadas = [i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y]
print('LA BITACORA, ANTES Y DESPUES DE LAS OCHO ANOTACIONES')
print('  lineas antes  : %d' % len(va))
print('  lineas ahora  : %d' % len(vb))
print('  lineas tocadas: %d  ->  %s' % (len(tocadas), ', '.join(str(n) for n in tocadas)))
print('  lineas intactas: %d' % (len(vb) - len(tocadas)))
