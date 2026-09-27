# -*- coding: utf-8 -*-
"""MEDIDA DIRIGIDA 2: el par que mi lectura levanta entre un nodo que ENTRO en
la vuelta 26 y un candidato que sigue en la BANDEJA. Misma senial de la casa
(`aduana.medir`) y mismos umbrales de `config/umbrales.json`."""
import io, json, os, sys
sys.path.insert(0, os.path.abspath("."))
sys.stdout.reconfigure(encoding="utf-8")
from src import aduana, informe, config as modulo_config
u = modulo_config.cargar()
por = {}
for l in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    d = json.loads(l); por[d["id"]] = ("GRAFO", d)
for d in informe.poblacion_de_bandejas():
    por.setdefault(d.get("id"), ("BANDEJA", d))
PARES = [
 ("reconocer_recompensar_gente_estable", "reconocer_excelencia_trayectoria_gradual"),
 ("reconocer_recompensar_gente_estable", "evitar_obsesion_ascenso_estatus"),
 ("retar_superestrellas_equipo_constantemente", "evitar_obsesion_ascenso_estatus"),
 ("subir_vara_calidad_equipo", "admitir_pronto_mal_desempenio_cuatro_razones"),
 ("decidir_momento_despedir_persona", "facilitar_despido_tres_cosas"),
 ("decidir_momento_despedir_persona", "calibrar_decision_despido_documentarla"),
 ("despedir_persona_franqueza_radical", "facilitar_despido_tres_cosas"),
 ("despedir_persona_franqueza_radical", "contactar_despedido_mes_despues"),
 ("despedir_persona_franqueza_radical", "sopesar_consejo_legal_despedir_humildad"),
 ("revisar_cinco_causas_mal_desempenio", "admitir_pronto_mal_desempenio_cuatro_razones"),
]
print("umbrales: similitud %.2f | familia %.2f | paso_contra_nodo %.2f"
      % (u["umbral_similitud_texto"], u["umbral_familia_id"], u["umbral_paso_contra_nodo"]))
print()
n = 0
for a, b in PARES:
    if a not in por or b not in por:
        print("%-46s x %-46s FALTA UNO" % (a, b)); continue
    m = aduana.medir(por[a][1], por[b][1], u)
    s = m["senales"]; lev = m["levantada_por"]
    if lev: n += 1
    print("%-44s [%s]" % (a, por[a][0]))
    print("  x %-42s [%s]  fam %.3f pxn %.3f sim %.3f  -> %s"
          % (b, por[b][0], s.get("familia_id",0), s.get("paso_contra_nodo",0),
             s.get("similitud_texto",0),
             ("LEVANTA (%s)" % ",".join(lev)) if lev else "no levanta"))
print()
print("DE LOS %d PARES MEDIDOS, SUPERAN UMBRAL: %d" % (len(PARES), n))
