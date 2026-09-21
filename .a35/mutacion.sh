#!/bin/sh
# LA GUARDA QUE NO MUERDE ES CIFRA (cosecha 7.C). Se muta el valor esperado y se
# comprueba que CAE. Corre sobre una COPIA fuera del arbol: cero escrituras aqui.
set -u
COPIA="$1"
rm -rf "$COPIA" && mkdir -p "$COPIA"
tar --exclude=.git --exclude=__pycache__ -cf - . | (cd "$COPIA" && tar -xf -)
cd "$COPIA" || exit 1
echo "== SANO: la copia intacta =="
python forja.py gate >/dev/null 2>&1;            echo "  gate              codigo $?"
python scripts/tabla_de_cierre.py >/dev/null 2>&1; echo "  tabla_de_cierre   codigo $?"
python scripts/tallar_reporte.py --estricto >/dev/null 2>&1; echo "  tallado D.41      codigo $?"
python scripts/censar_rutas.py >/dev/null 2>&1;  echo "  censo D.42        codigo $?"

echo "== MUTACION 1: la celda '14 de 14 del capitulo' pasa a '13 de 13' =="
python -c "import io;p='docs/loop/REPORTE.md';t=io.open(p,encoding='utf-8').read();io.open(p,'w',encoding='utf-8',newline='\n').write(t.replace('en \`AC.3\`: **14 de 14 del capitulo**','en \`AC.3\`: **13 de 13 del capitulo**'))"
python scripts/tabla_de_cierre.py 2>&1 | grep -E "DIFIERE|EN ROJO|VERDE"
python scripts/tabla_de_cierre.py >/dev/null 2>&1; echo "  tabla_de_cierre   codigo $?"
python scripts/tallar_reporte.py --estricto >/dev/null 2>&1; echo "  tallado D.41      codigo $?"

echo "== MUTACION 2: una arista a un id que no existe =="
python - <<'PY'
import io,json
p='dataset/nodos.jsonl'; ls=io.open(p,encoding='utf-8').read().splitlines()
for i,l in enumerate(ls):
    n=json.loads(l)
    if n['id']=='facilitar_despido_tres_cosas':
        n['nodos_siguientes'].append('nodo_que_no_existe_mutacion'); ls[i]=json.dumps(n,ensure_ascii=False); break
io.open(p,'w',encoding='utf-8',newline='\n').write("\n".join(ls)+"\n")
PY
python forja.py gate 2>&1 | head -2
python forja.py gate >/dev/null 2>&1; echo "  gate              codigo $?"

echo "== MUTACION 3: se borra una ruta publicada como sede de cifra =="
rm -f docs/loop/TABLA_DE_CIERRE.txt
python scripts/censar_rutas.py 2>&1 | grep -E "^CAE|EN ROJO|VERDE"
python scripts/censar_rutas.py >/dev/null 2>&1; echo "  censo D.42        codigo $?"
