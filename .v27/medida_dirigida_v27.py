# -*- coding: utf-8 -*-
"""MEDIDA DIRIGIDA DEL AUDITOR (vuelta 27, fase ciega).

El barrido entero sobre los 348 de grafo mas bandejas esta corriendo aparte y
es caro. Esta medida es la MISMA senial de la casa (`aduana.medir`, los mismos
umbrales de config/umbrales.json) contra una POBLACION DECLARADA: los vecinos
que mi lectura del capitulo senala como candidatos a par. Se declara asi
porque una poblacion recortada mide menos, no distinto: lo que salga por
encima de umbral esta por encima de umbral.
"""
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

pares_escritos = set()
for l in io.open("bitacora/VEREDICTOS.jsonl", encoding="utf-8"):
    if l.strip():
        d = json.loads(l)
        pares_escritos.add(frozenset((d["candidato"], d["vecino"])))

LOTES = {
 "adaptar_escucha_cultura_ajena": [
   "escuchar_callado_equipo_tranquilizar_incomodo",
   "escuchar_ruidoso_opinion_fuerte_pedir_agujeros",
   "crear_cultura_escucha_equipo",
   "organizar_sistema_recoger_quejas_equipo",
   "recorrer_rueda_hacer_cosas_equipo",
   "demostrar_apertura_visiones_distintas",
   "escuchar_entender_critica_dominar_defensa"],
 "abrir_debate_humor_explicar_proposito": [
   "centrar_debate_ideas_fuera_egos", "crear_obligacion_disentir_equipo",
   "parar_debate_emocion_agotamiento", "fijar_fecha_cierre_debate_equipo",
   "montar_reunion_gran_debate", "recorrer_rueda_hacer_cosas_equipo"],
 "bajar_detalle_organizacion_fuente_hechos": [
   "pedir_hechos_decision_evitar_recomendaciones",
   "repartir_decision_cercanos_hechos", "ceder_autoridad_unilateral_equipo",
   "pasear_organizacion_hallar_problemas_pequenios",
   "mantener_manos_trabajo_real_equipo", "recorrer_rueda_hacer_cosas_equipo"],
 "aprender_resultados_vencer_dos_presiones": [
   "cambiar_posicion_hechos_explicar_cambio", "cuidarse_agotamiento_centro_rueda",
   "recorrer_rueda_hacer_cosas_equipo", "recorrer_rueda_conscientemente_cultura_equipo",
   "bloquear_tiempo_pensar_calendario"],
 "cambiar_posicion_hechos_explicar_cambio": [
   "aprender_resultados_vencer_dos_presiones", "cuidarse_agotamiento_centro_rueda",
   "abrir_debate_humor_explicar_proposito", "recorrer_rueda_hacer_cosas_equipo"],
}

print("umbrales: similitud %.2f | familia %.2f | paso_contra_nodo %.2f"
      % (u["umbral_similitud_texto"], u["umbral_familia_id"], u["umbral_paso_contra_nodo"]))
print()
levantados = 0
for cid, lista in LOTES.items():
    print("CANDIDATO %s" % cid)
    cand = por[cid][1]
    for vid in lista:
        if vid not in por:
            print("   %-56s NO ESTA EN LA POBLACION" % vid); continue
        sede, vec = por[vid]
        m = aduana.medir(cand, vec, u)
        s = m["senales"]
        lev = m["levantada_por"]
        if lev: levantados += 1
        estado = ("LEVANTA (%s)" % ",".join(lev)) if lev else "no levanta"
        ver = "con veredicto" if frozenset((cid, vid)) in pares_escritos else "sin veredicto"
        print("   %-56s [%-7s] fam %.3f pxn %.3f sim %.3f  -> %-28s %s"
              % (vid, sede, s.get("familia_id",0), s.get("paso_contra_nodo",0),
                 s.get("similitud_texto",0), estado, ver))
    print()
print("PARES MEDIDOS QUE SUPERAN ALGUN UMBRAL: %d" % levantados)
