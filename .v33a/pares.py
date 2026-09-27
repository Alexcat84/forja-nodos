# PRIMERA LINEA (HEREDADO 4): CERO IDS TECLEADOS. Los pares salen de las lineas nuevas de
# bitacora/VEREDICTOS.jsonl (git diff ef3e7f9..HEAD). ESTE INSTRUMENTO NO IMPRIME LA RAZON:
# imprime el par, el veredicto y la senial, que es lo que 1.2 deja mirar ANTES de adjudicar.
import json, subprocess
ANTES = 'ef3e7f9'
def carga(ref):
    t = subprocess.check_output(['git','show','%s:bitacora/VEREDICTOS.jsonl'%ref]).decode('utf-8')
    return [json.loads(l) for l in t.splitlines() if l.strip()]
a = carga(ANTES); b = carga('HEAD')
nuevas = b[len(a):]
print("LAS %d LINEAS NUEVAS DE bitacora/VEREDICTOS.jsonl, SIN SU RAZON" % len(nuevas))
print()
for n, o in enumerate(nuevas, 1):
    print("  %2d  veredicto %-10s  operacion %-12s" % (n, o.get('veredicto','-'), o.get('operacion','-')))
    print("      candidato : %s" % o.get('candidato','-'))
    print("      vecino    : %s" % o.get('vecino','-'))
    se = o.get('senales')
    print("      senales   : %s" % (json.dumps(se, ensure_ascii=False) if se else '-'))
    print("      levantada : %s   arista: %s   campo: %s"
          % (o.get('levantada_por','-'), o.get('arista','-'), o.get('campo','-')))
    print("      razon     : %d caracteres, NO IMPRESA AQUI" % len(o.get('razon','') or ''))
