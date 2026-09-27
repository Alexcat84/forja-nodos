import json, pathlib, subprocess, sys
BASE = pathlib.Path("cuarentena/grove_high_output")
IDS = ["infundir_regularidad_reunion_proceso", "usar_tres_clases_reunion_proceso",
       "fijar_frecuencia_reunion_individual_madurez_tarea", "fijar_duracion_lugar_reunion_individual",
       "preparar_guion_reunion_individual_subordinado", "cubrir_indicadores_problemas_reunion_individual"]
print("    LA COMPROBACION SE HACE SOBRE EL ARBOL YA CORREGIDO, contra la version de git de la vuelta 51")
print("    %-50s %8s %9s %11s %13s" % ("ficha", "prefijo", "pasos", "titulo", "atribuciones"))
ok = True
for i in IDS:
    viejo = subprocess.run(["git", "show", "b04ac62:cuarentena/grove_high_output/%s.json" % i],
                           capture_output=True, text=True, encoding="utf-8").stdout
    a = json.loads(viejo)
    b = json.loads((BASE / ("%s.json" % i)).read_text(encoding="utf-8"))
    pref = b["resumen_teorico"].startswith(a["resumen_teorico"])
    pa = a["pasos_accionables"] == b["pasos_accionables"]
    ti = a["titulo"] == b["titulo"]
    at = a.get("atribuciones") == b.get("atribuciones")
    ok = ok and pref and pa and ti and at
    print("    %-50s %8s %9s %11s %13s" % (i[:50], pref, pa, ti, at))
print()
print("    LAS SEIS PASAN LAS CUATRO: %s" % ok)
print("    y el commit contra el que se comparan es b04ac62, que es el de la vuelta 51")
