import glob, json, os, subprocess
from pathlib import Path
def sh(a): return subprocess.run(a, capture_output=True, text=True, encoding='utf-8')
COM = {'f2c7312':'cap_07','293f3bc':'cap_08','447bad2':'cap_09','a0734ab':'cap_10','b7aadb2':'cap_11'}
rows=[]
for f in sorted(glob.glob('cuarentena/zhuo_manager/*.json')):
    p=Path(f).as_posix()
    h = sh(['git','log','--diff-filter=A','--format=%h','--',p]).stdout.split()[0]
    d=json.load(open(f,encoding='utf-8'))
    rows.append((COM[h], d['id'], d.get('titulo','')))
for c,i,t in sorted(rows):
    print('%s | %-44s | %s' % (c,i,t))
