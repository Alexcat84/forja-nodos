# Auditor de la vuelta 59. Recompone las fronteras de cap_14, cap_15 y cap_16
# a partir de las FILAS QUE EL REPORTE PUBLICA, contra el fichero fuente.
# No importa nada de .v58ext/.
import re, sys

REP = open('docs/loop/REPORTE.md', encoding='utf-8').read().split('\n')

def tabla(cap):
    """Devuelve [(ini, fin, palabras, nodos)] de la tabla del reporte, y su fila TOTAL."""
    pat = re.compile(r'^\| `L(\d+) a L(\d+)` \| (\d+) \| \*\*(\d+)\*\* \|')
    tot = re.compile(r'^\| \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \|')
    cab = None
    for i, ln in enumerate(REP):
        if ln.startswith(f'| tramo de {cap} |'):
            cab = i
            break
    filas, total = [], None
    for ln in REP[cab+1:]:
        m = pat.match(ln)
        if m:
            filas.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))))
            continue
        m = tot.match(ln)
        if m:
            total = (int(m.group(1)), int(m.group(2)))
            break
    return filas, total

def cuerpo(cap):
    txt = open(f'fuentes/grove_high_output/{cap}.md', encoding='utf-8').read().split('\n')
    # la cabecera acaba en el segundo guion triple
    tres = [i for i, l in enumerate(txt) if l.strip() == '---']
    fin = tres[1] + 1          # indice 0, la linea siguiente al segundo ---
    return txt, fin

for cap in ('cap_14', 'cap_15', 'cap_16'):
    filas, total = tabla(cap)
    txt, fin = cuerpo(cap)
    con_contenido = [i+1 for i in range(fin, len(txt)) if txt[i].strip()]
    cubiertas, solapes, mal = set(), [], []
    suma = 0
    for ini, f, pal, nod in filas:
        for n in range(ini, f+1):
            if n in cubiertas:
                solapes.append(n)
            cubiertas.add(n)
        mio = sum(len(txt[n-1].split()) for n in range(ini, f+1) if txt[n-1].strip())
        suma += mio
        if mio != pal:
            mal.append((f'L{ini} a L{f}', pal, mio))
    sin_cubrir = sorted(set(con_contenido) - cubiertas)
    cuerpo_aparte = sum(len(txt[n-1].split()) for n in con_contenido)
    entero = len(open(f'fuentes/grove_high_output/{cap}.md', encoding='utf-8').read().split())
    print(f'--- {cap}')
    print(f'  la cabecera acaba en la linea          : {fin}')
    print(f'  filas de la tabla del reporte          : {len(filas)}')
    print(f'  lineas con contenido tras la cabecera  : {len(con_contenido)}')
    print(f'  lineas NO cubiertas                    : {len(sin_cubrir)}  {sin_cubrir}')
    print(f'  SOLAPES                                : {len(solapes)}  {sorted(set(solapes))}')
    print(f'  suma de las filas (contada por mi)     : {suma} palabras')
    print(f'  cuerpo medido aparte                   : {cuerpo_aparte} palabras')
    print(f'  fichero entero, para cruzar con wc -w  : {entero} palabras')
    print(f'  IGUALES                                : {suma == cuerpo_aparte}')
    print(f'  nodos que la tabla declara             : {sum(f[3] for f in filas)}')
    print(f'  FILAS CUYA CIFRA DE PALABRAS NO ME SALE: {len(mal)}  {mal}')
    print(f'  fila TOTAL del reporte                 : {total}   (mia: {suma}, {sum(f[3] for f in filas)})')
    print()
