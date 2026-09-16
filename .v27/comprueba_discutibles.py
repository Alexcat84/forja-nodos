# -*- coding: utf-8 -*-
import io, json, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
ver=[json.loads(l) for l in io.open("bitacora/VEREDICTOS.jsonl",encoding="utf-8") if l.strip()]
def busca(a,b):
    return [v for v in ver if {v.get("candidato"),v.get("vecino")}=={a,b}]
print("D.8 sobre el par de las dos listas de cinco (T.3.f):")
r=busca("revisar_cinco_causas_mal_desempenio","mover_rapido_persona_papel_equivocado")
print("  veredictos en bitacora para ese par: %d  -> el reporte dice que no existe" % len(r))
print("\nAristas que cruzan de libro en f52f77e (antes de la vuelta 26):")
antes=[json.loads(l) for l in subprocess.run(["git","show","f52f77e:dataset/nodos.jsonl"],
       capture_output=True).stdout.decode("utf-8").split("\n") if l.strip()]
def clave(d):
    fs=d.get("fuentes",[]) or []
    return fs[0].get("clave","?") if fs else "?"
idx={d["id"]:d for d in antes}
tot=0;cru=0
for d in antes:
    for h in d.get("nodos_siguientes",[]) or []:
        tot+=1
        if h in idx and clave(d)!=clave(idx[h]): cru+=1
print("  aristas por nodos_siguientes: %d   de ellas entre libros: %d" % (tot,cru))
print("\nLos 5 pares de la tanda con vecino de otro libro (recuento del arbol): ver .v27/pares_entre_libros.txt")
print("  el reporte T.5 discutible 2 dice 'los dos pares con zhuo_manager'")
z=[v for v in ver if v.get("vecino") in ("despedir_persona_respeto_franqueza","elegir_recolocar_despedir_persona")
   and v.get("candidato") in ("despedir_persona_franqueza_radical","decidir_momento_despedir_persona")]
print("  pares de la tanda cuyo vecino es de zhuo_manager: %d" % len(z))
for v in z: print("     %s contra %s -> %s" % (v.get("candidato"),v.get("vecino"),v.get("veredicto")))
