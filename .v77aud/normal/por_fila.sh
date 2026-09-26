# Turno normal de la ACTA 76: grafo y bitacora en el ULTIMO commit de cada fila de la 77 (git log por asunto; la arista por
# lectura se commitea con la fila del reporte), contra la cifra "Bitacora de X a Y" de la nota de esa fila en el tramo de la
# 77 de REPORTE.md (desde su cabecera, linea 65837). Solo lee.
tail -n +65837 docs/loop/REPORTE.md > /tmp/tramo77.md
for n in $(seq 1 22); do
  h=$(git log --format="%h %s" 70a827c9..a70bdf05 | grep -E "^[0-9a-f]+ Vuelta 77, fila $n:" | head -1 | cut -d' ' -f1)
  g=$(git show $h:dataset/nodos.jsonl | wc -l); b=$(git show $h:bitacora/VEREDICTOS.jsonl | wc -l)
  rep=$(awk -v n="$n" 'index($0, "### Fila `" n "`:")==1{p=1; next} /^### /{p=0} p' /tmp/tramo77.md | grep -o -E "Bitacora (de \`[0-9]+\` a \`[0-9]+\`|sin movimiento: \`[0-9]+\`)" | head -1 | tr -d '`')
  echo "fila $n $h grafo $g bitacora $b | el reporte: $rep"
done
