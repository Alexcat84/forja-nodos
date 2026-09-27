echo '$ git rev-parse --abbrev-ref HEAD'
git rev-parse --abbrev-ref HEAD
echo '$ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl'
wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
echo '$ ls cuarentena/grove_high_output/*.json | wc -l'
ls cuarentena/grove_high_output/*.json | wc -l
echo '$ ls cuarentena/_insertados/grove_high_output/*.json | wc -l'
ls cuarentena/_insertados/grove_high_output/*.json | wc -l
