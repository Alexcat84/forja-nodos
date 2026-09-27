# -*- coding: utf-8 -*-
"""Se puede recomponer el capitulo de cada nodo SIN leer prosa de reporte?"""
import io, json, glob, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
CAP = re.compile(r"cap_(\d+)")

def cap_de(d):
    m = CAP.findall(d.get("resumen_teorico","") or "")
    if m: return "cap_%s" % m[0]
    for f in d.get("fuentes",[]) or []:
        m = CAP.findall(json.dumps(f, ensure_ascii=False))
        if m: return "cap_%s" % m[0]
    return None

nodos = [json.loads(l) for l in io.open("dataset/nodos.jsonl",encoding="utf-8") if l.strip()]
sin = [n["id"] for n in nodos if cap_de(n) is None]
print("NODOS DEL GRAFO           : %d" % len(nodos))
print("  con capitulo recuperable de resumen_teorico/fuentes : %d" % (len(nodos)-len(sin)))
print("  SIN capitulo recuperable                            : %d" % len(sin))
for i in sin[:10]: print("      %s" % i)

DOCE = ["abrir_debate_humor_explicar_proposito","adaptar_escucha_cultura_ajena",
 "aprender_resultados_vencer_dos_presiones","bajar_detalle_organizacion_fuente_hechos",
 "cambiar_posicion_hechos_explicar_cambio","decidir_momento_despedir_persona",
 "despedir_persona_franqueza_radical","reconocer_recompensar_gente_estable",
 "retar_superestrellas_equipo_constantemente","retirar_etiquetas_permanentes_equipo",
 "revisar_cinco_causas_mal_desempenio","subir_vara_calidad_equipo"]
por = collections.Counter()
print("\nLOS DOCE DE LA VUELTA 26, CAPITULO LEIDO DEL DATO, Y SUS PASOS:")
idx = {n["id"]: n for n in nodos}
tot_pasos = collections.Counter()
for i in DOCE:
    n = idx[i]; c = cap_de(n); p = len(n.get("pasos_accionables",[]) or [])
    por[c]+=1; tot_pasos[c]+=p
    print("   %-45s %s  pasos=%2d" % (i, c, p))
print("\nREPARTO POR CAPITULO: %s" % dict(por))
print("PASOS POR CAPITULO  : %s" % dict(tot_pasos))
print("TOTAL DE PASOS DE LOS DOCE: %d" % sum(tot_pasos.values()))
