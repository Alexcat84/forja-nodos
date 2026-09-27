# -*- coding: utf-8 -*-
"""Fase ciega de la 75, sin git (copia libre de .v72aud/grafo_sin_tanda.py con la tanda de la 73): el grafo de HOY, con las
7 de la tanda quitadas y con dar_elogio_disciplina_igual_critica devuelto a como estaba, es byte a byte el grafo que barri
en la 73? La vuelta 74 no movio ningun dato (ACTA 73 73.1, con git diff), asi que ese grafo es el de la apertura de la 75.
Reconstruye el fichero como lo escribe src/comun.py escribir_jsonl (json.dumps con sort_keys y ensure_ascii=False, una fila
por linea, salto final) y compara su sha1 con la huella de dataset/nodos.jsonl en .v73aud/huellas_al_barrer.txt. Antes
comprueba que esa reconstruccion reproduce el fichero de hoy tal cual.
Tres versiones: (a) solo quitando las 7 filas; (b) quitando ademas los ids de las 7 de CUALQUIER lista de texto de los
nodos que quedan, sin nombrar ninguna clave; (c) ademas, DESHACIENDO en dar_elogio las tres operaciones de la TAREA 2 de mi
encargo, por lo que su codigo escribe y nada mas: src/correccion.py solo AGREGA al final de resumen_teorico (' ' + anade) y
scripts/retirar_paso.py saca el paso N y AGREGA al final del resumen una frase con 'SU TEXTO LITERAL, QUE NO SE PIERDE: "..."'.
El resumen viejo es el prefijo hasta la primera correccion fechada el 26 sep 2026, y los pasos viejos son los de hoy con los
dos literales repuestos en las posiciones que sus frases dicen (primero sale el 17, despues el 8, asi que se reponen al reves).
Si (c) da la huella, ninguna otra fila ni ningun otro campo del grafo se movio. NO IMPRIME NINGUNA CLAVE DE NINGUN NODO (R6):
solo cuentas y SI o NO. Solo lee."""
import io, re, json, hashlib, sys, copy
sys.stdout.reconfigure(encoding="utf-8")
los7 = set(io.open('.v73aud/los7.txt', encoding='utf-8').read().split())
DE = 'dar_elogio_disciplina_igual_critica'
huella = [l.split(' *')[0] for l in io.open('.v73aud/huellas_al_barrer.txt', encoding='utf-8') if l.strip().endswith('*dataset/nodos.jsonl')][0]
bruto = open('dataset/nodos.jsonl', 'rb').read()
filas = [json.loads(l) for l in bruto.decode('utf-8').splitlines() if l.strip()]
ser = lambda fs: ('\n'.join(json.dumps(f, ensure_ascii=False, sort_keys=True) for f in fs) + '\n').encode('utf-8')
igual = lambda fs: 'SI' if hashlib.sha1(ser(fs)).hexdigest() == huella else 'NO'
print('filas del grafo hoy: %d | la reconstruccion reproduce el fichero de hoy: %s' % (len(filas), 'SI' if ser(filas) == bruto else 'NO'))
tanda = [f for f in filas if f['id'] in los7]; resto = [f for f in filas if f['id'] not in los7]
print('de las 7 de la tanda en el grafo: %d | filas que quedan sin ellas: %d' % (len(tanda), len(resto)))
pos = [k for k, f in enumerate(filas) if f['id'] in los7]
print('las 7 son las ultimas filas del fichero: %s' % ('SI' if pos == list(range(len(filas) - len(tanda), len(filas))) else 'NO'))
print('(a) sin las 7 filas, sha1 igual a la huella de mi barrido de la 73: %s' % igual(resto))
tocados = 0; limpio = []
for f in resto:
    g = {}; t = False
    for k, v in f.items():
        if isinstance(v, list) and any(isinstance(x, str) and x in los7 for x in v):
            v = [x for x in v if not (isinstance(x, str) and x in los7)]; t = True
        g[k] = v
    tocados += t; limpio.append(g)
print('(b) nodos viejos con algun id de las 7 en alguna lista: %d | sin esos ids, sha1 igual a la huella: %s' % (tocados, igual(limpio)))
deshecho = copy.deepcopy(limpio)
d = [f for f in deshecho if f['id'] == DE][0]
r = d['resumen_teorico']; pasos = d['pasos_accionables']
corte = r.index(' CORRECCION DECLARADA (26 sep 2026')
ret = re.findall(r'EL PASO (\d+) SALE DE pasos_accionables EN ESTE ACTO.*?SU TEXTO LITERAL, QUE NO SE PIERDE: "(.*?)" LOS PASOS PASAN DE (\d+) A (\d+)\.', r[corte:])
print('(c) en %s: pasos hoy %d | retiradas escritas en su resumen despues de la primera correccion del 26 sep: %d, en este orden: %s' % (
    'dar_elogio', len(pasos), len(ret), ', '.join('paso %s (de %s a %s)' % (n, a, b) for n, t, a, b in ret)))
for n, t, a, b in reversed(ret): pasos.insert(int(n) - 1, t)
d['pasos_accionables'] = pasos; d['resumen_teorico'] = r[:corte]
print('    deshechas: pasos %d | caracteres del resumen quitados del final: %d de %d' % (len(pasos), len(r) - corte, len(r)))
print('    y con dar_elogio deshecho, sha1 igual a la huella de mi barrido de la 73: %s' % igual(deshecho))
