import json, glob
nodos=[json.loads(l) for l in open("dataset/nodos.jsonl",encoding="utf-8") if l.strip()]
ver=[json.loads(l) for l in open("bitacora/VEREDICTOS.jsonl",encoding="utf-8") if l.strip()]
print("nodos en dataset            :", len(nodos))
print("aristas por nodos_siguientes:", sum(len(n.get("nodos_siguientes") or []) for n in nodos))
print("aristas por nodos_previos   :", sum(len(n.get("nodos_previos") or []) for n in nodos))
print("lineas en VEREDICTOS.jsonl  :", len(ver))
print("  con consumada == False    :", sum(1 for v in ver if v.get("consumada") is False))
print("pasos totales del grafo     :", sum(len(n.get("pasos_accionables") or []) for n in nodos))
b4=glob.glob("cuarentena/scott_radical_candor/*.json"); a4=glob.glob("cuarentena/_insertados/scott_radical_candor/*.json")
print("bandeja lote 4 / archivados :", len(b4), "/", len(a4), " total", len(b4)+len(a4), " -> %.1f%%"%(100*len(a4)/142))
print("bandeja lote 5              :", len(glob.glob("cuarentena/marquet_turn_the_ship/*.json")))
c11=[n for n in nodos if "scott_radical_candor/cap_11.md" in (n.get("resumen_teorico") or "")]
print("nodos que declaran cap_11   :", len(c11), " pasos:", sum(len(n.get("pasos_accionables") or []) for n in c11))
for n in sorted(c11,key=lambda x:x["id"]): print("   ", n["id"], len(n.get("pasos_accionables") or []))
