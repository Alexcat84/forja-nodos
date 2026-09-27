# PRIMERA LINEA (HEREDADO 4): CERO RUTAS TECLEADAS. Las rutas se sacan por patron del propio
# docs/loop/APERTURA_CIEGA.md, y se comprueba cada una contra el disco. Cosecha 7.B.
import io, re, os
t = io.open('docs/loop/APERTURA_CIEGA.md', encoding='utf-8').read()
rutas = sorted(set(re.findall(r'(?:\.v33a|docs|src|dataset|bitacora|config|fuentes|tests|cuarentena)[\w./_-]*\.(?:py|txt|md|jsonl|json|sh)', t)))
malas = 0
print("LAS RUTAS QUE MI APERTURA PUBLICA COMO PRUEBA, COMPROBADAS CONTRA EL DISCO (cosecha 7.B)")
print()
for r in rutas:
    ex = os.path.exists(r)
    n = os.path.getsize(r) if ex else -1
    est = 'OK' if (ex and n > 0) else ('CERO BYTES' if ex else 'NO EXISTE')
    if est != 'OK': malas += 1
    print("  %-8s %8s  %s" % (est, n if ex else '-', r))
print()
print("  rutas publicadas: %d   en rojo: %d" % (len(rutas), malas))
