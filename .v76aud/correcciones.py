# -*- coding: utf-8 -*-
"""Fase ciega de la 76 (copia de .v73aud/correcciones.py con el libro cambiado): imprime, de cada ficha de la bandeja de Gerber, los tramos de su resumen_teorico que empiezan por
CORRECCION DECLARADA (la lectura del extractor con el texto viejo dentro), para leerlos DESPUES de escribir mi fidelidad.
No imprime claves de relacion (R6). Solo lee."""
import io, json, glob, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
for f in sorted(glob.glob('cuarentena/gerber_emyth/*.json')):
    d = json.load(io.open(f, encoding='utf-8'))
    r = d.get('resumen_teorico', '')
    r = r if isinstance(r, str) else json.dumps(r, ensure_ascii=False)
    for m in re.finditer(r'CORRECCION DECLARADA', r):
        print('=====', os.path.basename(f)[:-5]); print(r[m.start():m.start() + 3000]); print()
