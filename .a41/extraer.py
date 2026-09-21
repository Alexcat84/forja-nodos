# -*- coding: utf-8 -*-
"""Saca de la apertura TODOS los bloques pegados: el comando, su marca de corte
si la lleva, y el texto literal que va debajo. Escribe un .cmd y un .peg por
bloque para que el propio Git Bash los vuelva a correr y los diffee."""
import io, re, json, os, glob
for f in glob.glob('.a41/blk_*'):
    os.remove(f)
lineas = io.open('docs/loop/APERTURA_CIEGA.md', encoding='utf-8').read().split('\n')
bloques, i = [], 0
while i < len(lineas):
    l = lineas[i]
    if l.startswith('    $ '):
        crudo = l[6:]
        m = re.search(r'\s+\[((?:CORTADA|ALTERADA)[^\]]*)\]\s*$', crudo)
        marca = m.group(1).split(',')[0].split(':')[0].strip() if m else ''
        if m:
            crudo = crudo[:m.start()]
        salida, j = [], i + 1
        while j < len(lineas):
            s = lineas[j]
            if s.startswith('    $ ') or (not s.startswith('    ') and s.strip() != ''):
                break
            if s.strip() == '':
                k = j + 1
                while k < len(lineas) and lineas[k].strip() == '':
                    k += 1
                if k < len(lineas) and lineas[k].startswith('    ') and not lineas[k].startswith('    $ '):
                    salida.extend(x[4:] for x in lineas[j:k]); j = k; continue
                break
            salida.append(s[4:]); j += 1
        bloques.append({'linea': i+1, 'cmd': crudo.strip(), 'marca': marca, 'n': len(salida)})
        n = len(bloques) - 1
        io.open('.a41/blk_%02d.cmd' % n, 'w', encoding='utf-8', newline='\n').write(crudo.strip() + '\n')
        io.open('.a41/blk_%02d.peg' % n, 'w', encoding='utf-8', newline='\n').write('\n'.join(salida) + ('\n' if salida else ''))
        io.open('.a41/blk_%02d.meta' % n, 'w', encoding='utf-8', newline='\n').write('%d\t%s\n' % (bloques[-1]['linea'], marca))
        i = j
    else:
        i += 1
io.open('.a41/bloques.json','w',encoding='utf-8').write(json.dumps(bloques, ensure_ascii=False))
print('bloques pegados: %d' % len(bloques))
print('con marca de corte o alteracion: %d' % sum(1 for b in bloques if b['marca']))
