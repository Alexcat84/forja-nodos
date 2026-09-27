# PRIMERA LINEA (HEREDADO 4): CERO FECHAS TECLEADAS COMO LISTA. Se saca toda cadena con
# forma de fecha de dataset/nodos.jsonl y bitacora/VEREDICTOS.jsonl y se cuenta.
import io, re, collections
for ruta in ('dataset/nodos.jsonl','bitacora/VEREDICTOS.jsonl'):
    t = io.open(ruta, encoding='utf-8').read()
    c = collections.Counter(re.findall(r'\b(\d{1,2} (?:ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)\w* \d{4})\b', t))
    print("%s   %d fechas en castellano distintas" % (ruta, len(c)))
    for k,v in sorted(c.items(), key=lambda x:-x[1])[:12]:
        print("    %-20s %3d" % (k,v))
