# -*- coding: utf-8 -*-
# Copia del auditor (ACTA 67) de .v64ext/pegado64.py con la cabecera del tramo cambiada a la vuelta 68 (ACTA 66 66.11).
"""R1 de la ACTA 60 60.15, medido: un bloque que empieza por `$` contiene lo que
el comando imprimio y nada mas. Si se acorta, se corta POR EL FINAL y se dice
`(recortado, entero en <fichero>)`.

Dos medidas mecanicas:
  A) los comandos REPRODUCIBLES hoy se vuelven a correr y se comparan;
  B) todo bloque se marca si trae elision `...` no declarada o texto anadido.
"""
import io, re, subprocess
lineas = io.open('docs/loop/REPORTE.md', encoding='utf-8').read().split('\n')
i = [k for k, l in enumerate(lineas) if l.startswith('# VUELTA 68 ')][0]
tramo = lineas[i:]

def bloque(d):
    out = []
    for l in tramo[d:]:
        if l.strip() == '':
            out.append(''); continue
        if l.startswith('    '):
            if l.strip().startswith('$ '): break
            out.append(l[4:])
        else: break
    while out and out[-1] == '': out.pop()
    return [x for x in out if x.strip()]

REPRO = {
 'tail -6 docs/loop/CREDITO_serial.jsonl': ['tail', '-6', 'docs/loop/CREDITO_serial.jsonl'],
 'tail -2 docs/loop/DEUDA.jsonl': ['tail', '-2', 'docs/loop/DEUDA.jsonl'],
 'wc -l bitacora/VEREDICTOS.jsonl dataset/nodos.jsonl config/pares_mutuos.jsonl':
     ['wc', '-l', 'bitacora/VEREDICTOS.jsonl', 'dataset/nodos.jsonl', 'config/pares_mutuos.jsonl'],
}
rotos = []; total = 0
for n, l in enumerate(tramo):
    if not (l.startswith('    ') and l.strip().startswith('$ ')): continue
    cmd = l.strip()[2:]; total += 1; peg = bloque(n + 1); motivo = None
    for x in peg:
        if re.search(r'(?<!\.)\.\.\.(?!\.)', x):
            motivo = 'ELISION `...` en medio de la salida, sin declarar'; break
    m = re.match(r"date '\+%F %T ([^']*)'", cmd)
    if not motivo and m and peg:
        e = m.group(1)
        for x in peg:
            if e in x and x.split(e, 1)[1].strip():
                motivo = 'TEXTO ANADIDO detras de la salida: ' + x.split(e, 1)[1].strip()
    if not motivo and cmd in REPRO:
        sal = [x.strip() for x in subprocess.run(REPRO[cmd], capture_output=True, text=True,
                                                 encoding='utf-8').stdout.split('\n') if x.strip()]
        p = [x.strip() for x in peg]
        sobra = [x for x in p if x not in sal]
        if sobra:
            motivo = 'NO ES LA SALIDA DEL COMANDO: %d de %d lineas pegadas que el comando no imprime' % (len(sobra), len(p))
    if motivo: rotos.append((cmd, motivo))
print('bloques abiertos con `$` en el tramo de la vuelta 68 : %d' % total)
print('bloques que ROMPEN R1 (ACTA 60 60.15)                : %d' % len(rotos))
for c, m in rotos:
    print('   $ %s\n       %s' % (c, m))
