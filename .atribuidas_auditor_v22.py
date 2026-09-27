# -*- coding: utf-8 -*-
"""EL INSTRUMENTO ANCHO DE .t1_v21/cuentas21.py, aplicado a los 17 de la vuelta 22.
Lista toda cuenta que un paso ATRIBUYE al libro (las N que el texto nombra, los N
que el libro pone...). No decide: lista, para releerla contra su linea."""
import io, json, re, unicodedata
NUM=r'(un|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince|veinte|treinta|cuarenta|cincuenta|cien|\d+)'
# la cuenta va pegada a una atribucion al texto
PATRONES=[
 re.compile(r'\b(?:las|los)\s+'+NUM+r'\s+([a-z]+(?:\s+[a-z]+){0,3})\s+que\s+el\s+(?:texto|libro)', re.I),
 re.compile(r'el\s+(?:texto|libro)\s+(?:dice|pone|nombra|escribe|enumera|da|llama|describe|le\s+pone|les\s+pone)[^.;:]{0,40}?\b'+NUM+r'\b', re.I),
 re.compile(r'\b(?:las|los)\s+'+NUM+r'\s+(?:cosas|propositos|papeles|goles|seniales|remedios|partes|vias|razones|asuntos|bloques|columnas|preguntas|actos|reglas|consejos|matices|errores|tecnicas|recordatorios|conversaciones|minutos|ventajas|efectos)\b', re.I),
]
def norm(s):
    s=unicodedata.normalize('NFD',s)
    return ''.join(c for c in s if unicodedata.category(c)!='Mn')
TRAMO=json.loads(io.open('.tramos_v22.json',encoding='utf-8').read())
SRC={c:io.open('fuentes/scott_radical_candor/%s.md'%c,encoding='utf-8').read().split('\n')
     for c in ('cap_10','cap_11')}
ING={'un':['one','a ','single'],'una':['one','a ','single'],'dos':['two','both','neither','either'],
 'tres':['three'],'cuatro':['four'],'cinco':['five'],'seis':['six'],'siete':['seven'],
 'ocho':['eight'],'nueve':['nine'],'diez':['ten'],'trece':['thirteen'],'catorce':['fourteen'],
 'quince':['fifteen'],'veinte':['twenty'],'treinta':['thirty'],'cuarenta':['forty'],
 'cincuenta':['fifty'],'cien':['hundred'],'once':['eleven'],'doce':['twelve']}
n=0; sinescribir=[]
for nid,(cap,tramos) in TRAMO.items():
    texto=norm(' '.join(' '.join(SRC[cap][a-1:b]) for a,b in tramos)).lower()
    d=json.load(io.open('cuarentena/scott_radical_candor/%s.json'%nid,encoding='utf-8'))
    for i,p in enumerate(d['pasos_accionables'],1):
        for pat in PATRONES:
            for m in pat.finditer(p):
                cuenta=m.group(1).lower()
                n+=1
                formas=ING.get(cuenta,[cuenta])
                if not any(f in texto for f in formas):
                    sinescribir.append((nid,i,cuenta,m.group(0)[:70]))
                break
print("CUENTAS QUE LOS PASOS ATRIBUYEN AL LIBRO (instrumento ancho)")
print("  ocurrencias halladas                          : %d" % n)
print("  cuyo numeral NO esta escrito en el tramo citado: %d" % len(sinescribir))
print("")
for nid,i,c,frag in sinescribir:
    print("  %-50s paso %-3d [%s] %s" % (nid,i,c,frag))
