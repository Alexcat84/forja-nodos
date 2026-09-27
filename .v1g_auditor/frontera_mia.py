# frontera_mia.py: comprueba, con mi propio codigo, que las piezas que el extractor
# declara cubren el cuerpo entero de su unidad, sin solape y sin hueco, y que sus
# palabras suman el cuerpo. Las piezas se leen de su fichero; nada se teclea.
import ast, glob, os
print("%-8s %6s %8s %8s %8s %8s %8s" % ("unidad","piezas","cuerpo","suma","residuo","solape","hueco"))
malas = 0
for p in sorted(glob.glob('.gerber_v1/piezas_cap*.txt')):
    u = os.path.basename(p)[len('piezas_'):-4].replace('cap','cap_')
    piezas = ast.literal_eval(open(p, encoding='utf-8').read())
    lineas = open('fuentes/gerber_emyth/%s.md' % u, encoding='utf-8', errors='replace').read().splitlines()
    cortes = [i for i, l in enumerate(lineas) if l.strip() == '---']
    desde = cortes[1] + 1              # indice 0 de la primera linea de cuerpo
    cuerpo = sum(len(l.split()) for l in lineas[desde:])
    vistas = {}
    suma = 0
    for nombre, a, b, _, _ in piezas:
        for n in range(a, b + 1):
            vistas[n] = vistas.get(n, 0) + 1
        suma += sum(len(l.split()) for l in lineas[a-1:b])
    todas = set(range(desde + 1, len(lineas) + 1))
    solape = sum(1 for n, c in vistas.items() if c > 1)
    hueco = len(todas - set(vistas))
    sobra = len(set(vistas) - todas)
    if suma != cuerpo or solape or hueco or sobra: malas += 1
    print("%-8s %6d %8d %8d %8d %8d %8d%s" % (u, len(piezas), cuerpo, suma, cuerpo - suma, solape, hueco,
          ("   FUERA DEL CUERPO: %d" % sobra) if sobra else ""))
print("unidades que NO cierran:", malas)
