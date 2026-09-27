# -*- coding: utf-8 -*-
import io, json
FICHAS = [("P6", "infundir_regularidad_reunion_proceso"),
          ("P7", "usar_tres_clases_reunion_proceso"),
          ("P11", "fijar_frecuencia_reunion_individual_madurez_tarea"),
          ("P12", "fijar_duracion_lugar_reunion_individual"),
          ("P13", "preparar_guion_reunion_individual_subordinado"),
          ("P14", "cubrir_indicadores_problemas_reunion_individual")]
for pieza, fid in FICHAS:
    d = json.load(io.open("cuarentena/grove_high_output/%s.json" % fid, encoding="utf-8"))
    print("=" * 100)
    print("%s  %s" % (pieza, fid))
    print("  titulo: %s" % d.get("titulo"))
    print("  atribuciones: %s" % json.dumps(d.get("atribuciones"), ensure_ascii=False)[:400])
    for i, p in enumerate(d.get("pasos_accionables") or [], 1):
        print("  %2d. %s" % (i, p))
    print()
