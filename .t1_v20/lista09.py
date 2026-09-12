# -*- coding: utf-8 -*-
import json, glob, re, os
out = []
for f in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    m = re.search(r'cap_(\d\d)', d['resumen_teorico'])
    if m and m.group(1) == '09':
        out.append(f.replace(os.sep, '/'))
print('\n'.join(out))
