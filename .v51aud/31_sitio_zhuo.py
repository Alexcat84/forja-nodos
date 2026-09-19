# -*- coding: utf-8 -*-
"""El nodo del grafo dirigir_reunion_individual_semanal dice DONDE se tiene la reunion?
Barro sus diez pasos con las palabras de sitio que esta casa usa."""
import io,sys,json,re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
PAL=['oficina','despacho','area','sitio','lugar','sala','mesa','donde']
for l in open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip():
        n=json.loads(l)
        if n['id']=='dirigir_reunion_individual_semanal':
            t=' '.join(n['pasos_accionables']).lower()
            print("pasos del nodo: %d"%len(n['pasos_accionables']))
            for p in PAL:
                print("  '%-9s' aparece en sus pasos: %d"%(p,len(re.findall(r'\b%s'%p,t))))
