# PRIMERA LINEA (HEREDADO 4): CERO IDS TECLEADOS. Destapa UNA razon por vez, la que se le
# pide por numero de linea nueva. CORRE DESPUES DE .v33a/mis_clases.txt, cuya hora esta
# publicada en .v33a/hora_clases.txt (HEREDADO 3 de la ACTA 31).
import json, sys, subprocess, time
ANTES = 'ef3e7f9'
def carga(ref):
    t = subprocess.check_output(['git','show','%s:bitacora/VEREDICTOS.jsonl'%ref]).decode('utf-8')
    return [json.loads(l) for l in t.splitlines() if l.strip()]
nuevas = carga('HEAD')[len(carga(ANTES)):]
n = int(sys.argv[1])
o = nuevas[n-1]
print("== DESTAPADA LA RAZON %d DE %d, a las %s ==" % (n, len(nuevas), time.strftime('%Y-%m-%d %H:%M:%S')))
print("   par: %s  contra  %s   veredicto %s" % (o.get('candidato'), o.get('vecino'), o.get('veredicto')))
print("   RAZON: %s" % o.get('razon'))
