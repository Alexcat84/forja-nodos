# -*- coding: utf-8 -*-
"""Compruebo los TRES pagos de docs/loop/DEUDA.jsonl contra el arbol de hoy.
DEUDA.jsonl es docs/ y por tanto sede de CIFRA PUBLICADA (48.9.b)."""
import io, json, os, subprocess

BAND = "cuarentena/grove_high_output"

def ficha(fid):
    return json.load(io.open(os.path.join(BAND, fid + ".json"), encoding="utf-8"))

# --- d044: la correccion nueva de P38, medida
viejo = json.loads(subprocess.check_output(
    ["git", "show", "3061fc2:%s/dimensionar_numero_subordinados_medio_dia_semanal.json" % BAND]
).decode("utf-8"))["resumen_teorico"]
nuevo = ficha("dimensionar_numero_subordinados_medio_dia_semanal")["resumen_teorico"]
anadido = nuevo[len(viejo):]
print("d044  el viejo es PREFIJO del nuevo          :", nuevo.startswith(viejo))
print("d044  caracteres de la correccion nueva      :", len(anadido),
      "   (el pago publica 2071)")
print("d044  veces que aparece 'grep' EN ELLA       :", anadido.lower().count("grep"))
print("d044  veces que aparece 'Sale de la PIEZA P34' EN ELLA:",
      anadido.count("Sale de la PIEZA P34"))
for i in ("decir_no_trabajo_excede_capacidad",
          "usar_calendario_herramienta_planificacion_produccion"):
    print("d044  el id '%s' escrito EN ELLA: %d" % (i[:40], anadido.count(i)))

# --- la linea de pago de DEUDA.jsonl, que es la sede que se rompio la vez anterior
lineas = [l for l in io.open("docs/loop/DEUDA.jsonl", encoding="utf-8") if l.strip()]
pago = [json.loads(l) for l in lineas if json.loads(l).get("id") == "d044"
        and json.loads(l).get("tipo") == "pago"][-1]
print("d044  la LINEA DE PAGO de DEUDA.jsonl contiene 'Sale de la PIEZA P34':",
      "Sale de la PIEZA P34" in json.dumps(pago, ensure_ascii=False))

# --- el metodo nuevo, corrido sobre la bandeja de HOY
declaran = {"P34": [], "P38": []}
for n in sorted(os.listdir(BAND)):
    if not n.endswith(".json"):
        continue
    rt = json.load(io.open(os.path.join(BAND, n), encoding="utf-8"))["resumen_teorico"]
    cabecera = rt.split(".")[0] + "." + (rt.split(".")[1] if "." in rt else "")
    primera = rt[:400]
    for pieza in declaran:
        if ("Sale de la PIEZA %s de" % pieza) in primera:
            declaran[pieza].append(n[:-5])
print()
print("metodo nuevo sobre los %d ficheros de la bandeja de HOY:" % len(os.listdir(BAND)))
for pieza in sorted(declaran):
    print("  declaran '%s' en su CABECERA: %d  %s"
          % (pieza, len(declaran[pieza]), declaran[pieza]))

# --- d045 y d046
print()
for fid, deuda, aguja in (
        ("buscar_regularidad_bloques_iguales_trabajo_mando", "d045", "D.29"),
        ("preparar_respuestas_estandar_interrupciones_repetidas", "d046", "L313")):
    v = json.loads(subprocess.check_output(
        ["git", "show", "3061fc2:%s/%s.json" % (BAND, fid)]).decode("utf-8"))
    n = ficha(fid)
    cambian = sorted(k for k in set(list(v) + list(n)) if v.get(k) != n.get(k))
    print("%s  %-54s claves que cambian %s" % (deuda, fid[:54], cambian))
    print("       pasos identicos: %s   titulo identico: %s   atribuciones identicas: %s"
          % (v.get("pasos_accionables") == n.get("pasos_accionables"),
             v.get("titulo") == n.get("titulo"),
             v.get("atribuciones") == n.get("atribuciones")))
    print("       el viejo resumen es PREFIJO del nuevo: %s   '%s' escrito en lo anadido: %d"
          % (n["resumen_teorico"].startswith(v["resumen_teorico"]),
             aguja, n["resumen_teorico"][len(v["resumen_teorico"]):].count(aguja)))
