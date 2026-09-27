import io, json, re
rutas = [l.strip() for l in io.open('.v34aud/tanda.txt', encoding='utf-8') if l.strip()]
nodos = {json.loads(l)['id']: json.loads(l)
         for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()}
filas = []
for r in rutas:
    i = json.load(io.open(r, encoding='utf-8'))['id']
    rt = nodos[i]['resumen_teorico']
    a = int(re.search(r'l[ií]neas? (\d+)', rt).group(1))
    filas.append((a, i))
for a, i in sorted(filas):
    print(i)
