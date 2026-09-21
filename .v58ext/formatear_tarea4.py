# -*- coding: utf-8 -*-
"""Arma la seccion XX.4 (TAREA 4, fidelidad por muestra) pegando la salida literal del
instrumento (D.59, denominador al lado) y la relectura contra el libro, TRANSCRIPCION o
PUENTE, de cada paso que la muestra selecciono.
"""
import io

muestra = io.open(".v58ext/muestra_fidelidad.txt", encoding="utf-8").read().rstrip("\n")

FILAS = [
    ("entregar_evaluacion_desempeno_tres_claves", "P1", "cap_14", "L109",
     "You must level with your subordinate, the credibility and integrity of the entire system depend on your being totally frank.", "TRANSCRIPCION"),
    ("entregar_evaluacion_desempeno_tres_claves", "P2", "cap_14", "L111",
     "The aim of communication is to transmit thoughts from the brain of person A to the brain of person B.", "TRANSCRIPCION"),
    ("entregar_evaluacion_desempeno_tres_claves", "P3", "cap_14", "L113",
     "you should watch the person you are talking to ... it is your responsibility to keep at it until you are satisfied that you have been heard and understood.", "TRANSCRIPCION"),
    ("entregar_evaluacion_desempeno_tres_claves", "P4", "cap_14", "L115",
     "employing your entire arsenal of sensory capabilities to make certain your points are being properly interpreted.", "TRANSCRIPCION"),
    ("entregar_evaluacion_desempeno_tres_claves", "P5", "cap_14", "L119",
     "your own insecurities, anxieties, guilt, or whatever should be kept out of it. At issue are the subordinate's problems, not the supervisor's.", "TRANSCRIPCION"),
    ("entregar_evaluacion_desempeno_tres_claves", "P6", "cap_14", "L119",
     "You should work to control these emotions so that they don't affect your task.", "TRANSCRIPCION"),
    ("guiar_subordinado_etapas_resistencia_desempeno", "P1", "cap_14", "L167",
     "A poor performer has a strong tendency to ignore his problem ... denies the existence of a problem ... admits that there is a problem, but maintains it is not his problem.", "TRANSCRIPCION"),
    ("guiar_subordinado_etapas_resistencia_desempeno", "P2", "cap_14", "L167",
     "a manager needs facts and examples so that he can demonstrate its reality.", "TRANSCRIPCION"),
    ("guiar_subordinado_etapas_resistencia_desempeno", "P5", "cap_14", "L171",
     "The supervisor should keep track of what stage things are in.", "TRANSCRIPCION"),
    ("guiar_subordinado_etapas_resistencia_desempeno", "P6", "cap_14", "L179",
     "you will have to assume the formal role of the supervisor, endowed with position power, and say, This is what I, as your boss, am instructing you to do ... monitor his performance against that commitment.", "TRANSCRIPCION"),
    ("preparar_resena_mixta_hoja_trabajo", "P1", "cap_14", "L129",
     "consider as many aspects of your subordinate's performance as possible. You should scan material such as progress reports, performance against quarterly objectives, and one-on-one meeting notes.", "TRANSCRIPCION"),
    ("preparar_resena_mixta_hoja_trabajo", "P2", "cap_14", "L129",
     "sit down with a blank piece of paper ... write everything down on the paper. Do not edit in your head.", "TRANSCRIPCION"),
    ("preparar_resena_mixta_hoja_trabajo", "P3", "cap_14", "L129",
     "When you have run out of items, you can put all of your supporting documentation away.", "TRANSCRIPCION"),
    ("preparar_resena_mixta_hoja_trabajo", "P4", "cap_14", "L131",
     "look for relationships between the various items listed.", "TRANSCRIPCION"),
    ("preparar_resena_mixta_hoja_trabajo", "P6", "cap_14", "L131",
     "ask yourself if your subordinate will be able to remember all of the messages you have chosen to deliver. If not, you must delete the less important ones.", "TRANSCRIPCION"),
    ("gestionar_retencion_subordinado_valioso_renuncia", "P2", "cap_15", "L115",
     "You now must vigorously pursue every avenue available to you to keep him with the firm, even if it means transferring him to another department.", "TRANSCRIPCION"),
    ("gestionar_retencion_subordinado_valioso_renuncia", "P3", "cap_15", "L115",
     "If it seems that is the likely solution, you must become the project manager of that solution until the whole thing is settled.", "TRANSCRIPCION"),
    ("gestionar_retencion_subordinado_valioso_renuncia", "P5", "cap_15", "L119",
     "You now have to make him feel comfortable with the new arrangement ... We are just doing what we should have done without any of this happening.", "TRANSCRIPCION"),
    ("gestionar_retencion_subordinado_valioso_renuncia", "P6", "cap_15", "L121",
     "You have to make him quit again ... he's really made two commitments: first to a potential employer he only vaguely knows, and second to you, his present employer.", "TRANSCRIPCION"),
    ("responder_primer_aviso_renuncia_subordinado", "P1", "cap_15", "L111",
     "Drop what you are doing.", "TRANSCRIPCION"),
    ("responder_primer_aviso_renuncia_subordinado", "P2", "cap_15", "L111",
     "Sit him down and ask him why he is quitting.", "TRANSCRIPCION"),
    ("responder_primer_aviso_renuncia_subordinado", "P5", "cap_15", "L111",
     "Don't argue, don't lecture, and don't panic.", "TRANSCRIPCION"),
    ("usar_banco_nueve_preguntas_entrevista", "P2", "cap_15", "L41",
     "What are your weaknesses? How are you working to eliminate them?", "TRANSCRIPCION"),
    ("usar_banco_nueve_preguntas_entrevista", "P3", "cap_15", "L43",
     "Convince me why my company should hire you.", "TRANSCRIPCION"),
    ("usar_banco_nueve_preguntas_entrevista", "P4", "cap_15", "L45",
     "What are some of the problems you are encountering in your current position? How are you going about solving them? What could you have done to prevent them from cropping up?", "TRANSCRIPCION"),
    ("usar_banco_nueve_preguntas_entrevista", "P5", "cap_15", "L47",
     "Why do you think you're ready for this new job?", "TRANSCRIPCION"),
    ("usar_banco_nueve_preguntas_entrevista", "P6", "cap_15", "L49",
     "What do you consider your most significant achievements? Why were they important to you?", "TRANSCRIPCION"),
    ("usar_banco_nueve_preguntas_entrevista", "P7", "cap_15", "L51",
     "What do you consider your most significant failures? What did you learn from them?", "TRANSCRIPCION"),
    ("usar_banco_nueve_preguntas_entrevista", "P8", "cap_15", "L53",
     "Why do you think an engineer should be chosen for a marketing position? (Vary this one according to the situation.)", "TRANSCRIPCION"),
    ("usar_banco_nueve_preguntas_entrevista", "P9", "cap_15", "L55",
     "What was the most important course or project you completed in your college career? Why was it so important?", "TRANSCRIPCION"),
    ("reciclar_empleado_ascendido_mas_alla_capacidad", "P1", "cap_16", "L49",
     "management was at fault for misjudging the employee's readiness for more responsibility ... management ought to face up to its own error in judgment.", "TRANSCRIPCION"),
    ("reciclar_empleado_ascendido_mas_alla_capacidad", "P2", "cap_16", "L49",
     "take forthright and deliberate steps to place the person into a job he can do.", "TRANSCRIPCION"),
    ("reciclar_empleado_ascendido_mas_alla_capacidad", "P3", "cap_16", "L49",
     "Management should also support the employee in the face of the embarrassment that he is likely to feel.", "TRANSCRIPCION"),
    ("reciclar_empleado_ascendido_mas_alla_capacidad", "P4", "cap_16", "L49",
     "If recycling is done openly, all will be pleasantly surprised how short-lived that embarrassment will be.", "TRANSCRIPCION"),
]

out = []
out.append("## XX.4. TAREA 4. LA FIDELIDAD, POR MUESTRA Y CON SU SEMILLA `v58`")
out.append("")
out.append("**La semilla de esta vuelta es `v58`, la que el encargo fijo.** La reparte el instrumento, no yo:")
out.append("")
out.append("<!-- TALLADO: salida=.v58ext/muestra_fidelidad.txt -->")
out.append("")
out.append("    $ python scripts/muestra_fidelidad.py --libro grove_high_output \\")
out.append("             --capitulos cap_14,cap_15,cap_16 --semilla v58")
out.append("")
for linea in muestra.split("\n"):
    out.append(("    " + linea) if linea.strip() else "")
out.append("")
out.append("**La semilla reparte `cap_16` para releer ENTERO** (solo tiene un candidato, `4` pasos) **y")
out.append("`cap_14` y `cap_15` por muestra de `15` pasos cada uno.** No lo elijo yo.")
out.append("")
out.append("### XX.4.1. LA RELECTURA CONTRA EL LIBRO, PASO POR PASO")
out.append("")
out.append("| candidato | paso | capitulo | linea | el texto del libro que lo sostiene | veredicto |")
out.append("|---|---|---|---|---|---|")
for cid, p, cap, linea, cita, veredicto in FILAS:
    cita_corta = cita if len(cita) <= 140 else cita[:137] + "..."
    cita_md = cita_corta.replace("|", "\\|")
    out.append("| `%s` | %s | `%s` | `%s` | %s | **%s** |" % (cid, p, cap, linea, cita_md, veredicto))
out.append("")

total = len(FILAS)
transcripcion = sum(1 for f in FILAS if f[5] == "TRANSCRIPCION")
puente = total - transcripcion

por_capitulo = {}
for cid, p, cap, linea, cita, veredicto in FILAS:
    por_capitulo.setdefault(cap, [0, 0])
    por_capitulo[cap][0] += 1
    if veredicto == "PUENTE":
        por_capitulo[cap][1] += 1

out.append("### XX.4.2. EL TALLY, CON SU DENOMINADOR AL LADO (`D.59`)")
out.append("")
out.append("La tabla la calcula `.v58ext/formatear_tarea4.py` de la relectura fila por fila de `XX.4.1`,")
out.append("no se teclea:")
out.append("| capitulo | pasos revisados | PUENTE | por ciento inventado | dispara relectura entera (>10%%) |")
out.append("|---|---:|---:|---:|---|")
for cap in ["cap_14", "cap_15", "cap_16"]:
    n, pu = por_capitulo[cap]
    pct = (100.0 * pu / n) if n else 0.0
    dispara = "SI" if pct > 10.0 else "NO"
    nota = "" if cap != "cap_16" else " (releido ENTERO por diseno de la muestra, no por disparador)"
    out.append("| `%s` | %d de %d | %d | %.1f por ciento | %s%s |" % (cap, n, n, pu, pct, dispara, nota))
out.append("| **total del tramo** | **%d de %d** | **%d** | **%.1f por ciento** | **NO** |"
            % (transcripcion + puente, total, puente, 100.0 * puente / total))
out.append("")
out.append("**`%d` de `%d` pasos revisados, `%d` TRANSCRIPCION y `%d` PUENTE: `0,0` por ciento inventado,**"
            % (total, total, transcripcion, puente))
out.append("**bien por debajo del `10` por ciento que dispara la relectura entera de un capitulo** (el")
out.append("disparador de `EXTRACTOR.md` 15, modo austero). `cap_16` ya se releyo entero porque la propia")
out.append("semilla lo eligio para eso, no porque haya disparado nada: su `0` de `4` esta limpio igual.")

io.open(".v58ext/task4_seccion.md", "w", encoding="utf-8", newline="\n").write("\n".join(out))
print("escrito .v58ext/task4_seccion.md, %d lineas, PUENTE=%d de %d" % (len(out), puente, total))
