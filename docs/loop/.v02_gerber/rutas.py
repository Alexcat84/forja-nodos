# rutas.py: toda ruta de fichero que la pagina nombra, con su tamano en bytes.
# Sin listas tecleadas: las rutas se sacan del propio documento, entre comillas o
# detras de un '$'. Existe porque el censo D.42 solo mira las rutas que van en una
# celda con cifra, y yo quiero mirar TODAS las que escribo.
import io, os, re, sys
texto = io.open(sys.argv[1], encoding="utf-8").read()
EXT = (".txt", ".out", ".json", ".jsonl", ".py", ".md", ".log", ".sh")
vistas = []
for cita in re.findall(r"[`\s]([A-Za-z0-9_./-]+)", texto):
    if cita.endswith(EXT) and "/" in cita and cita not in vistas:
        vistas.append(cita)
falta = vacia = bien = 0
for r in sorted(vistas):
    if not os.path.exists(r):
        print("NO ESTA        %s" % r); falta += 1
    elif os.path.getsize(r) == 0:
        print("CERO BYTES     %s" % r); vacia += 1
    else:
        bien += 1
print("rutas nombradas por la pagina : %d" % len(vistas))
print("  con contenido               : %d" % bien)
print("  de cero bytes               : %d" % vacia)
print("  que no estan en el arbol    : %d" % falta)
