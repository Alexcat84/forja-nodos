# -*- coding: utf-8 -*-
"""MUESTRA PINEADA, con la semilla 27 SELLADA en APERTURA_CIEGA.md seccion 7."""
import io, json, random, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
viejas = set()
out = subprocess.run(["git","show","f52f77e:bitacora/VEREDICTOS.jsonl"],capture_output=True).stdout.decode("utf-8")
for l in out.split("\n"):
    if l.strip(): viejas.add(l.strip())
nuevas = [json.loads(l) for l in io.open("bitacora/VEREDICTOS.jsonl",encoding="utf-8")
          if l.strip() and l.strip() not in viejas]
CONTAMINADOS = {("subir_vara_calidad_equipo","delimitar_franqueza_radical_cinco_noes"),
                ("subir_vara_calidad_equipo","pedir_critica_equipo_premiarla"),
                ("cambiar_posicion_hechos_explicar_cambio","abrir_debate_humor_explicar_proposito")}
pares = []
for v in nuevas:
    c = v.get("candidato"); n = v.get("vecino") or v.get("contra") or v.get("nodo")
    pares.append((c, n, v.get("veredicto")))
print("pares nuevos de la tanda            : %d" % len(pares))
print("  SANO                              : %d" % sum(1 for p in pares if p[2]=="SANO"))
print("  CONTINUA                          : %d" % sum(1 for p in pares if p[2]=="CONTINUA"))
limpios = sorted([p for p in pares if (p[0],p[1]) not in CONTAMINADOS], key=lambda p:(p[0],p[1]))
print("menos los 3 contaminados (3.2)      : %d" % len(limpios))
print("  de ellos SANO                     : %d" % sum(1 for p in limpios if p[2]=="SANO"))
print("20%% de los SANO limpios (31)        : 6,2 -> 7   |  20%% de 34 : 6,8 -> 7")
print("EL MAYOR ENTRE 3 Y 7                : 7   (techo 20, no muerde)")
print("SEMILLA SELLADA                     : 27\n")
sel = random.Random(27).sample(limpios, 7)
print("LA MUESTRA, EN EL ORDEN QUE LA SACA random.Random(27).sample:")
for i,(c,n,v) in enumerate(sel,1):
    print("  %d. %-44s contra %-44s  [%s]" % (i,c,n,v))
io.open(".v27/muestra_ids.txt","w",encoding="utf-8").write(
    "\n".join("%s\t%s\t%s"%(c,n,v) for c,n,v in sel)+"\n")
