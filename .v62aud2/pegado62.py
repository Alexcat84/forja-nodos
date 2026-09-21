# -*- coding: utf-8 -*-
"""MIDE LOS BLOQUES QUE EL TRAMO DE LA VUELTA 62 ABRE CON `$`.

R1 de la ACTA 60 60.15: un bloque que empieza por `$` contiene lo que el comando
imprimio y nada mas; si se acorta, se corta POR EL FINAL y se dice
`(recortado, entero en <fichero>)`.

Dos medidas, las dos mecanicas:
  A) los comandos REPRODUCIBLES hoy (lectores puros) se vuelven a correr y se
     comparan linea a linea contra lo pegado;
  B) todo bloque se marca si trae una linea con elision `...` no declarada o
     texto anadido detras de la salida.
"""
import io, re, subprocess

REPORTE = 'docs/loop/REPORTE.md'
lineas = io.open(REPORTE, encoding='utf-8').read().split('\n')
i = [k for k, l in enumerate(lineas) if l.startswith('# VUELTA 62,')][0]
tramo = lineas[i:]

def bloque(desde):
    out = []
    for l in tramo[desde:]:
        if l.strip() == '':
            out.append(''); continue
        if l.startswith('    '):
            if l.strip().startswith('$ '): break
            out.append(l[4:])
        else: break
    while out and out[-1] == '': out.pop()
    return out

REPRO = {
    'tail -6 docs/loop/CREDITO_serial.jsonl': ['tail', '-6', 'docs/loop/CREDITO_serial.jsonl'],
    'tail -2 docs/loop/DEUDA.jsonl': ['tail', '-2', 'docs/loop/DEUDA.jsonl'],
    'git hash-object docs/loop/TABLA_DE_CIERRE.txt': ['git', 'hash-object', 'docs/loop/TABLA_DE_CIERRE.txt'],
    'git hash-object docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v62.txt': ['git', 'hash-object', 'docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v62.txt'],
    'git hash-object docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v59.txt': ['git', 'hash-object', 'docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v59.txt'],
    'wc -l bitacora/VEREDICTOS.jsonl dataset/nodos.jsonl config/pares_mutuos.jsonl': ['wc', '-l', 'bitacora/VEREDICTOS.jsonl', 'dataset/nodos.jsonl', 'config/pares_mutuos.jsonl'],
}

total = rotos = repro_ok = repro_mal = 0
print('=' * 78)
print('BLOQUES ABIERTOS CON `$` EN EL TRAMO DE LA VUELTA 62')
print('=' * 78)
for n, l in enumerate(tramo):
    if not (l.startswith('    ') and l.strip().startswith('$ ')): continue
    cmd = l.strip()[2:]
    total += 1
    peg = [x for x in bloque(n + 1) if x.strip()]
    avisos = []
    for x in peg:
        if re.search(r'(?<!\.)\.\.\.(?!\.)', x): avisos.append('ELISION `...` sin declarar: ' + x.strip()[:78])
    m = re.match(r"date '\+%F %T ([^']*)'", cmd)
    if m and peg:
        esperado = m.group(1)
        for x in peg:
            resto = x.split(esperado, 1)[-1] if esperado in x else None
            if resto and resto.strip(): avisos.append('TEXTO ANADIDO detras de la salida de date: ' + resto.strip())
    if cmd in REPRO:
        try:
            sal = subprocess.run(REPRO[cmd], capture_output=True, text=True, encoding='utf-8').stdout.rstrip('\n').split('\n')
        except Exception as e:
            sal = ['<no reproducible: %s>' % e]
        sal = [x.rstrip() for x in sal if x.strip()]
        pegs = [x.rstrip() for x in peg]
        igual = (pegs == sal)
        if igual: repro_ok += 1
        else: repro_mal += 1
        print('\n$ %s' % cmd)
        print('   REPRODUCIDO HOY: %s' % ('IDENTICO' if igual else 'DIFIERE'))
        if not igual:
            print('   lineas pegadas: %d | lineas que el comando imprime: %d' % (len(pegs), len(sal)))
            for x in pegs:
                if x not in sal: print('     + (pegada, el comando NO la imprime): %s' % x.strip()[:100])
    if avisos:
        rotos += 1
        if cmd not in REPRO: print('\n$ %s' % cmd)
        for a in avisos: print('   %s' % a)
print('\n' + '=' * 78)
print('bloques abiertos con `$`                 : %d' % total)
print('bloques con elision o texto anadido      : %d' % rotos)
print('bloques reproducidos hoy, IDENTICOS      : %d' % repro_ok)
print('bloques reproducidos hoy, QUE DIFIEREN   : %d' % repro_mal)
