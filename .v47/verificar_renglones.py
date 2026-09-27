# -*- coding: utf-8 -*-
"""Cada celda de la tabla 6.1 dice un fichero, un renglon y una frase del libro.
Esto comprueba que la frase ESTE en ese renglon. No adjudica nada: solo mide."""
import io,unicodedata
def norm(s):
    s=unicodedata.normalize('NFKD',s)
    for a,b in ((chr(8217),"'"),(chr(8220),'"'),(chr(8221),'"'),(chr(8212),'-'),(chr(8211),'-')):
        s=s.replace(a,b)
    return s.lower()
CASOS=[
 (1,'cap_02',19,'basic requirements of production'),
 (1,'cap_02',23,'limiting step'),
 (1,'cap_02',25,'total throughput time'),
 (1,'cap_02',27,'most difficult, or most sensitive, or most expensive'),
 (2,'cap_02',51,'redo your flow around the new limiting step'),
 (2,'cap_02',55,'limited toaster capacity'),
 (3,'cap_02',59,'can be traded off against each other'),
 (3,'cap_02',61,'quantifiable set of relationships'),
 (4,'cap_02',39,'three fundamental types of production operations'),
 (4,'cap_02',47,'basically similar flow of activity'),
 (5,'cap_02',67,'choose in-process tests over those that destroy product'),
 (6,'cap_02',69,'receiving inspection'),
 (6,'cap_02',69,'opportunity at risk'),
 (7,'cap_02',73,'becomes more valuable'),
 (7,'cap_02',75,'lowest-value stage possible'),
 (8,'cap_03',17,'which five would they be'),
 (8,'cap_03',29,'look at them early every day'),
 (9,'cap_03',31,'pairing indicators'),
 (9,'cap_03',33,'completion date of each software unit'),
 (10,'cap_03',35,'output of the work unit and not simply the activity'),
 (10,'cap_03',37,'physical, countable thing'),
 (11,'cap_03',73,'black box'),
 (11,'cap_03',77,'cutting some windows'),
 (12,'cap_03',81,'leading indicators'),
 (12,'cap_03',83,'linearity indicator'),
 (12,'cap_03',87,'concentrated in the last week of the month'),
 (13,'cap_03',89,'trend indicators'),
 (14,'cap_03',91,'stagger chart'),
 (15,'cap_03',99,'archive of indicators'),
 (16,'cap_03',103,'two ways to control the output'),
 (16,'cap_03',105,'build to forecast'),
 (17,'cap_03',111,'two simultaneous processes'),
 (17,'cap_03',117,'shipping dock at the same time'),
 (17,'cap_03',121,'stagger charts in both'),
 (18,'cap_03',123,'administrative factory'),
 (18,'cap_03',125,'forecast the number of people needed'),
 (19,'cap_03',135,'send it back to the vendor'),
 (19,'cap_03',137,'pacemaker'),
 (20,'cap_03',139,'inspections, of course, cost money'),
 (20,'cap_03',141,'gate-like inspection and a monitoring step'),
 (21,'cap_03',143,'variable inspections'),
 (22,'cap_03',169,'work simplification'),
 (22,'cap_03',171,'question why each step is performed'),
 ('D4','cap_03',153,'predetermined criteria'),
]
lineas={}
for c in ('cap_02','cap_03'):
    lineas[c]=io.open('fuentes/grove_high_output/%s.md'%c,encoding='utf-8').read().split('\n')
ok=mal=0
for fila,cap,n,frase in CASOS:
    txt=norm(lineas[cap][n-1])
    hit=norm(frase) in txt
    ok,mal=(ok+1,mal) if hit else (ok,mal+1)
    if not hit:
        print("  FALLA  fila %-3s %s L%-4d  no contiene: %s" % (fila,cap,n,frase))
print()
print("renglones comprobados : %d" % len(CASOS))
print("  CASAN               : %d" % ok)
print("  NO CASAN            : %d" % mal)
