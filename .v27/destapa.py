# -*- coding: utf-8 -*-
import io, json, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
viejas = set(l.strip() for l in subprocess.run(["git","show","f52f77e:bitacora/VEREDICTOS.jsonl"],
             capture_output=True).stdout.decode("utf-8").split("\n") if l.strip())
nuevas = [json.loads(l) for l in io.open("bitacora/VEREDICTOS.jsonl",encoding="utf-8")
          if l.strip() and l.strip() not in viejas]
muestra = [tuple(l.split("\t")[:2]) for l in io.open(".v27/muestra_ids.txt",encoding="utf-8") if l.strip()]
print("=== LAS RAZONES DE LA MUESTRA PINEADA, DESTAPADAS DESPUES DE ADJUDICAR ===")
for c,n in muestra:
    for v in nuevas:
        if v.get("candidato")==c and (v.get("vecino") or v.get("contra"))==n:
            print("\n%s contra %s" % (c,n))
            print("   veredicto : %s" % v.get("veredicto"))
            print("   razon     : %s" % (v.get("razon") or "<<< SIN RAZON >>>"))
print("\n\n=== D.8: ALGUN VEREDICTO DE LA TANDA SIN RAZON ESCRITA? ===")
sin = [v for v in nuevas if not (v.get("razon") or "").strip()]
print("veredictos nuevos          : %d" % len(nuevas))
print("SIN razon escrita          : %d" % len(sin))
for v in sin: print("   %s contra %s" % (v.get("candidato"), v.get("vecino")))
cortas = [v for v in nuevas if len((v.get("razon") or "").strip()) < 40]
print("con razon de menos de 40 caracteres : %d" % len(cortas))
for v in cortas: print("   %s :: %s" % (v.get("candidato"), v.get("razon")))
print("\nlongitud media de razon    : %.0f caracteres" % (sum(len(v.get("razon") or "") for v in nuevas)/len(nuevas)))
