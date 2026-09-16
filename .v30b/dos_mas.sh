#!/bin/bash
cd /c/Users/AlexDesk/Documents/forja-nodos
export PYTHONIOENCODING=utf-8
python forja.py informe --carpeta .v30b/uno_pelear > .v30b/barrido_pelear.txt 2>&1
echo "pelear hecho"
# la receta de D.38.4 al pie de la letra: poblacion = grafo MAS bandejas
python -c "
import io,glob,json,os
out=list(io.open('dataset/nodos.jsonl',encoding='utf-8'))
n=0
for f in sorted(glob.glob('cuarentena/*/*.json')):
    if '_insertados' in f or '_derivadas' in f or 'ensayo_referencia_163' in f: continue
    d=json.load(io.open(f,encoding='utf-8'))
    out.append(json.dumps(d,ensure_ascii=False)+'\n'); n+=1
io.open('.v30b/pob_literal.jsonl','w',encoding='utf-8').writelines(out)
print('poblacion a mano:',len(out),'=',len(out)-n,'del grafo mas',n,'de bandejas')
"
FORJA_DATASET=".v30b/pob_literal.jsonl" python forja.py informe --carpeta .v30b/uno_pelear > .v30b/barrido_pelear_literal.txt 2>&1
echo "literal hecho"
