# PRIMERA LINEA (HEREDADO 4): CERO IDS TECLEADOS. Lee .v33a/barrido.txt, cuya tanda salio del
# git diff del dataset. Casa mis vecinos contra los de bitacora/VEREDICTOS.jsonl.
import io, re, json, subprocess
t = io.open('.v33a/barrido.txt', encoding='utf-8', errors='replace').read()
mios = {}
for b in t.split('===== BARRIDO DE ')[1:]:
    ident = b.split('\n')[0].replace(' =====','').strip()
    mios[ident] = re.findall(r'^\s*vecino (\S+)\s+\[levantada por', b, re.M)
ANTES='ef3e7f9'
def carga(r):
    x = subprocess.check_output(['git','show','%s:bitacora/VEREDICTOS.jsonl'%r]).decode('utf-8')
    return [json.loads(l) for l in x.splitlines() if l.strip()]
nuevas = carga('HEAD')[len(carga(ANTES)):]
suyos = {}
for o in nuevas:
    if o.get('operacion') or not o.get('vecino'): continue
    suyos.setdefault(o['candidato'], []).append(o['vecino'])
print("MI BARRIDO CONTRA EL DE LA MAQUINA, vecino a vecino")
print("  mi poblacion: 347 (281 del grafo de 282 menos el propio, mas 66 de bandejas), arbol 1ae327e")
print("  la suya: la de cada insercion de la vuelta 33, con el lote aun sin archivar")
print()
tm = ts = 0
for i in io.open('.v33a/tanda_ids.txt', encoding='utf-8'):
    i = i.strip()
    if not i: continue
    a, b2 = sorted(mios.get(i, [])), sorted(suyos.get(i, []))
    tm += len(a); ts += len(b2)
    print("  %-44s  yo %d   la maquina de la vuelta %d   %s"
          % (i[:44], len(a), len(b2), 'IGUALES' if a == b2 else 'DISTINTOS: mios=%s suyos=%s' % (a, b2)))
print()
print("  TOTAL vecinos levantados: yo %d, la vuelta %d" % (tm, ts))
