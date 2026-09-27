# PRIMERA LINEA (HEREDADO 4): CERO CIFRAS TECLEADAS COMO DATO. Los dos numeros salen de
# .v33a/bitacora.py (los SANO nuevos) y de mi relectura (las caidas), y se pasan por argumento.
import math, sys, json, subprocess
ANTES = 'ef3e7f9'
def carga(r):
    x = subprocess.check_output(['git','show','%s:bitacora/VEREDICTOS.jsonl'%r]).decode('utf-8')
    return [json.loads(l) for l in x.splitlines() if l.strip()]
nuevas = carga('HEAD')[len(carga(ANTES)):]
n = len([o for o in nuevas if o.get('veredicto') == 'SANO'])
caen = int(sys.argv[1])
z = 1.959963985
p = caen / float(n)
den = 1 + z*z/n
c = (p + z*z/(2*n)) / den
h = (z/den) * math.sqrt(p*(1-p)/n + z*z/(4.0*n*n))
print("MUESTRA PINEADA DE LOS SANO (AUDITOR_FORJA.md 7)")
print("  SANO nuevos de la tanda, contados de bitacora/VEREDICTOS.jsonl: %d" % n)
print("  releidos: %d de %d (la poblacion entera, no una muestra)" % (n, n))
print("  caen: %d" % caen)
print("  tasa: %.1f por ciento" % (100*p))
print("  banda de Wilson al 95 por ciento: de %.1f a %.1f por ciento"
      % (100*max(0.0, c-h), 100*min(1.0, c+h)))
