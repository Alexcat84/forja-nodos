# -*- coding: utf-8 -*-
"""Arma la seccion XX.3 (TAREA 3, minar) del reporte pegando los siete informes de aduana,
uno por candidato, en el mismo orden en que se escribieron y se corrieron (D.35: el remedio
es mecanico, se teclea la salida real). Cero texto inventado en los bloques pegados.
"""
import io

CANDIDATOS = [
    ("entregar_evaluacion_desempeno_tres_claves", "cap_14", ".v58ext/informe_1_entregar_evaluacion_desempeno_tres_claves.txt",
     "Lei a los dos vecinos: son nodos distintos (protocolo de decision de seis preguntas y reconvocar una reunion), el solape es de vocabulario de conversacion y no de doctrina. Sigue en cuarentena, sin veredicto en bitacora porque no se inserta esta vuelta (`D.39`)."),
    ("preparar_resena_mixta_hoja_trabajo", "cap_14", ".v58ext/informe_2_preparar_resena_mixta_hoja_trabajo.txt",
     "El unico vecino es su hermano de capitulo, `entregar_evaluacion_desempeno_tres_claves`: preparar la resena y entregarla son dos momentos distintos del mismo proceso, con condicion de activacion distinta. No es gemelo."),
    ("guiar_subordinado_etapas_resistencia_desempeno", "cap_14", ".v58ext/informe_3_guiar_subordinado_etapas_resistencia_desempeno.txt",
     "Sin vecinos levantados: entra limpio. Es el candidato que llevo el discutible de existencia marcado en `XX.4`."),
    ("usar_banco_nueve_preguntas_entrevista", "cap_15", ".v58ext/informe_4_usar_banco_nueve_preguntas_entrevista.txt",
     "El vecino es de otro dominio (`identificar_disparadores_propios_reaccion`), levantado por `paso_contra_nodo` en un unico paso: coincidencia de frase, no de doctrina."),
    ("responder_primer_aviso_renuncia_subordinado", "cap_15", ".v58ext/informe_5_responder_primer_aviso_renuncia_subordinado.txt",
     "Cuatro vecinos, ninguno por encima de 0,4 de similitud de texto (banda de gemelos real): son tecnicas de conversacion vecinas por vocabulario, no duplicados."),
    ("gestionar_retencion_subordinado_valioso_renuncia", "cap_15", ".v58ext/informe_6_gestionar_retencion_subordinado_valioso_renuncia.txt",
     "Bloquea contra su propio hermano de episodio, `responder_primer_aviso_renuncia_subordinado` (familia_id 0,250, bajo el umbral de 0,30 de la señal 2, y similitud_texto 0,363, bajo la banda de 0,4 de gemelos reales de `EXTRACTOR.md` 11). Es exactamente el discutible que marque en `XX.4` antes de correr este informe: la medicion no lo resuelve, lo deja donde estaba, por debajo de ambos umbrales de gemelo."),
    ("reciclar_empleado_ascendido_mas_alla_capacidad", "cap_16", ".v58ext/informe_7_reciclar_empleado_ascendido_mas_alla_capacidad.txt",
     "Sin vecinos levantados: entra limpio."),
]

out = []
out.append("## XX.3. TAREA 3. MINAR, CON EL TECHO POR DELANTE")
out.append("")
out.append("**Los siete candidatos, en el orden del libro, cada uno escrito y pasado por**")
out.append("**`python forja.py informe` en el mismo acto** (`EXTRACTOR.md` 16). Para que la prueba fuera")
out.append("real y no solo dicha, los seis candidatos todavia no probados se sacaron de")
out.append("`cuarentena/grove_high_output/` a una carpeta de espera (`.v58ext/pendientes/`) antes de correr")
out.append("el primer informe, y cada uno volvio a entrar UNO A LA VEZ, justo antes de correr su propio")
out.append("informe. **La linea `poblacion del barrido` de cada informe es la salida real del instrumento,")
out.append("no una promesa** (`D.35`): sube de candidato en candidato, `431`, `432`, `433`, `434`, `435`,")
out.append("`436` y `437`, de uno en uno, porque de uno en uno es como se escribieron.")
out.append("")
out.append("**CERO INSERCIONES.** El lote `7` sigue ABIERTO y `D.39` no deja entrar nada: los siete informes")
out.append("son de SOLO LECTURA, y ningun veredicto se escribe en `bitacora/VEREDICTOS.jsonl` esta vuelta.")
out.append("")

for i, (cid, cap, ruta, nota) in enumerate(CANDIDATOS, 1):
    contenido = io.open(ruta, encoding="utf-8").read().rstrip("\n")
    out.append("### XX.3.%d. `%s` (%s)" % (i, cid, cap))
    out.append("")
    out.append("<!-- TALLADO: salida=%s -->" % ruta)
    out.append("")
    out.append("    $ python forja.py informe cuarentena/grove_high_output/%s.json" % cid)
    out.append("")
    for linea in contenido.split("\n"):
        out.append(("    " + linea) if linea.strip() else "")
    out.append("")
    out.append("**Lectura del vecino:** %s" % nota)
    out.append("")

out.append("### XX.3.8. EL SALDO DEL TRAMO")
out.append("")
out.append("| candidato | capitulo | poblacion del barrido | saldo de la aduana |")
out.append("|---|---|---:|---|")
for i, (cid, cap, ruta, nota) in enumerate(CANDIDATOS, 1):
    contenido = io.open(ruta, encoding="utf-8").read()
    pob = [l for l in contenido.split("\n") if l.startswith("poblacion del barrido")][0].split(":")[1].split("(")[0].strip()
    saldo = "ENTRARIA" if "[ENTRARIA]" in contenido else "BLOQUEARIA"
    out.append("| `%s` | `%s` | %s | %s |" % (cid, cap, pob, saldo))
out.append("")
out.append("**El tramo de esta vuelta: `3` capitulos (`cap_14`, `cap_15`, `cap_16`) y `7` candidatos, dentro")
out.append("del techo de `30` de `D.58`.** Dos ENTRARIAN sin vecino, cinco BLOQUEARIAN esperando lectura, y")
out.append("ninguno CAE ni CHOCA dentro del lote. Los siete quedan en `cuarentena/grove_high_output/`, sin")
out.append("insertar, hasta que el lote `7` cierre y su insercion se autorice (`D.39`, `EXTRACTOR.md` 15.7).")

io.open(".v58ext/task3_seccion.md", "w", encoding="utf-8", newline="\n").write("\n".join(out))
print("escrito .v58ext/task3_seccion.md, %d lineas" % len(out))
