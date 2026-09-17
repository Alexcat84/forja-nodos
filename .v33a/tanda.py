# PRIMERA LINEA (HEREDADO 4): CERO IDS TECLEADOS. La tanda sale de git diff entre
# ef3e7f9 (commit anterior a la apertura de la vuelta 33) y HEAD, sobre el dato.
import json, io, subprocess
ANTES = 'ef3e7f9'
def ids_dataset(ref):
    txt = subprocess.check_output(['git','show','%s:dataset/nodos.jsonl'%ref]).decode('utf-8')
    return [json.loads(l)['id'] for l in txt.splitlines() if l.strip()]
a = ids_dataset(ANTES); b = ids_dataset('HEAD')
sa = set(a)
nuevos = [i for i in b if i not in sa]
print("NODOS QUE ENTRAN AL GRAFO EN LA VUELTA 33 (dataset/nodos.jsonl, %s -> HEAD)" % ANTES)
print("  antes: %d nodos   ahora: %d nodos   ENTRAN: %d   salen: %d"
      % (len(a), len(b), len(nuevos), len([i for i in a if i not in set(b)])))
for n, i in enumerate(nuevos, 1):
    print("  %2d  %s" % (n, i))
io.open('.v33a/tanda_ids.txt','w',encoding='utf-8').write('\n'.join(nuevos)+'\n')
print()
mov = subprocess.check_output(['git','diff','--name-status',ANTES,'HEAD','--','cuarentena/']).decode('utf-8')
print("FICHEROS DE cuarentena/ QUE SE MUEVEN EN LA VUELTA 33: %d lineas de git diff --name-status"
      % len([l for l in mov.splitlines() if l.strip()]))
