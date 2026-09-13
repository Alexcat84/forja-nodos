# -*- coding: utf-8 -*-
"""La senial barata de manual 3.5, comprobada y no supuesta: ningun nombre propio
de los casos del capitulo puede aparecer en un entregable_esperado ni en una
condicion_activacion. Los nombres salen del propio capitulo, no de mi cabeza."""
import io, json, re, unicodedata, collections
def norm(s):
    s=unicodedata.normalize('NFD',s)
    return ''.join(c for c in s if unicodedata.category(c)!='Mn')
LOTE=[l.strip() for l in io.open('.lote_v22_auditor.txt',encoding='utf-8') if l.strip()]
# nombres propios del capitulo: palabras con mayuscula interior de frase
nombres=collections.Counter()
for cap in ('cap_10','cap_11'):
    txt=io.open('fuentes/scott_radical_candor/%s.md'%cap,encoding='utf-8').read()
    for m in re.finditer(r'(?<![.!?\n“\u2014] )(?<!^)\b([A-Z][a-z]{2,})\b', txt, re.M):
        nombres[m.group(1)]+=1
COMUNES={'The','This','That','These','Those','You','Your','Here','When','What','Why','How','Chapter',
 'Radical','Candor','Remember','There','They','She','Once','Some','Most','Have','Just','Also','With',
 'Listen','Learn','Clarify','Good','Updates','Conversation','Cancellations','Block','Things','Make',
 'Lower','Push','Bring','Fight','Walk','Think','Mind','Show','Staff','Signs','Encourage','Employees',
 'Review','Everyone','Frequency','Follow','Debate','Give','Department','Being','Because','From','Even',
 'Silicon','Valley','But','And','For','Not','Are','All','Are','Their','Since','Given','Ask','Find',
 'First','Second','Third','Finally','Probably','Although','Getting','Neither','Believe','Sex','Gone',
 'Whether','Notice','Management','Others','Measuring','Making','Another','Early','Friends','Here',
 'Try','Schedule','According','Put','Anyone','Use','Check','Employees','Day','One','Two','Now','Its'}
PROPIOS=sorted(n for n,c in nombres.items() if n not in COMUNES)
print("NOMBRES PROPIOS QUE EL INSTRUMENTO SACA DE cap_10 Y cap_11: %d" % len(PROPIOS))
print("  " + ', '.join(PROPIOS))
print("")
sucios=0; revisados=0
for nid in LOTE:
    d=json.load(io.open('cuarentena/scott_radical_candor/%s.json'%nid,encoding='utf-8'))
    for campo in ('entregable_esperado','condiciones_activacion','titulo'):
        revisados+=1
        v=norm(d[campo])
        hits=[p for p in PROPIOS if re.search(r'\b'+re.escape(norm(p))+r'\b', v)]
        if hits:
            sucios+=1
            print("  SUCIO  %-50s %-22s -> %s" % (nid,campo,hits))
print("")
print("campos revisados (entregable, activacion y titulo de los 17): %d" % revisados)
print("campos con nombre propio de caso dentro               : %d" % sucios)
