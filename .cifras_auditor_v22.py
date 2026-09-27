# -*- coding: utf-8 -*-
"""Toda cifra escrita en un paso de la vuelta 22 contra el cuerpo del capitulo.
Si una cifra no esta en el libro, la escribio el extractor (D.30, especie la cifra)."""
import io, json, re, unicodedata

PAL = {'un':1,'una':1,'uno':1,'dos':2,'tres':3,'cuatro':4,'cinco':5,'seis':6,'siete':7,
 'ocho':8,'nueve':9,'diez':10,'once':11,'doce':12,'trece':13,'catorce':14,'quince':15,
 'veinte':20,'veinticinco':25,'treinta':30,'cuarenta':40,'cincuenta':50,'cien':100,
 'ciento':100,'mil':1000,'primero':1,'segundo':2,'tercero':3,'cuarta':4,'cuarenta y cinco':45,
 'primerisimo':1}
ING = {1:['one','a ','single'],2:['two'],3:['three'],4:['four'],5:['five'],6:['six'],7:['seven'],
 8:['eight'],9:['nine'],10:['ten'],11:['eleven'],12:['twelve'],13:['thirteen'],14:['fourteen'],
 15:['fifteen'],20:['twenty'],25:['twenty-five','25'],30:['thirty'],40:['forty'],45:['forty-five'],
 50:['fifty'],100:['hundred'],1000:['thousand']}

def norm(s):
    s=unicodedata.normalize('NFD',s.lower())
    return ''.join(c for c in s if unicodedata.category(c)!='Mn')

LOTE = [l.strip() for l in io.open('.lote_v22_auditor.txt',encoding='utf-8') if l.strip()]
CUERPO = {}
for cap in ('cap_10','cap_11'):
    CUERPO[cap] = norm(io.open('fuentes/scott_radical_candor/%s.md'%cap,encoding='utf-8').read())

tot = hall = falta = 0
malas = []
for nid in LOTE:
    d = json.load(io.open('cuarentena/scott_radical_candor/%s.json'%nid,encoding='utf-8'))
    cap = 'cap_10' if nid=='desplegar_tres_conversaciones_carrera' else 'cap_11'
    cuerpo = CUERPO[cap]
    for i,p in enumerate(d['pasos_accionables'],1):
        np = norm(p)
        vistos = set()
        # cifras en digito
        for m in re.findall(r'\d+', np): vistos.add(int(m))
        # cifras en palabra
        for w,v in PAL.items():
            if re.search(r'\b'+w.replace(' ','\s+')+r'\b', np): vistos.add(v)
        for v in sorted(vistos):
            tot += 1
            formas = [str(v)] + ING.get(v,[])
            if any(f in cuerpo for f in formas): hall += 1
            else:
                falta += 1
                malas.append((nid,i,v,p[:90]))

print("CIFRAS ESCRITAS EN LOS PASOS DE LA VUELTA 22, CONTRA EL CUERPO DEL CAPITULO")
print("  candidatos barridos            : %d" % len(LOTE))
print("  cifras halladas en los pasos   : %d" % tot)
print("  cifras que SI estan en el libro: %d" % hall)
print("  cifras que NO estan en el libro: %d" % falta)
print("")
for nid,i,v,p in malas:
    print("  %-48s paso %-3d cifra %-5s | %s" % (nid,i,v,p))
