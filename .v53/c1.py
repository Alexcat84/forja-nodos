# -*- coding: utf-8 -*-
"""CANDIDATO 1 DE LA VUELTA 53: cap_06 P7, L23 a L29, EL MODELO IDEAL DE DECISION.

Se escribe y se pasa por la aduana EN EL MISMO ACTO (EXTRACTOR.md 16).
"""
import io
import json
import os

ID = "conducir_etapas_modelo_ideal_decision"
DESTINO = "cuarentena/grove_high_output/%s.json" % ID

NODO = {
    "id": ID,
    "titulo": "Conducir una decision por las etapas del modelo ideal: discusion libre, decision clara y apoyo pleno",
    "dominio": "gestion_equipos",
    "estado": "vivo",
    "ids_alias": [],
    "nodos_previos": [],
    "nodos_siguientes": [],
    "atribuciones": [],
    "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
    "denominaciones": {
        "nombre_largo": "El modelo ideal de toma de decisiones en un negocio que vive de lo que sabe, con su primera etapa de discusion libre, su etapa de decision clara y su cierre de apoyo pleno",
        "sigla": "",
        "otros_idiomas": [
            {"idioma": "ingles", "termino": "ideal model of decision-making"},
            {"idioma": "ingles", "termino": "free discussion"},
            {"idioma": "ingles", "termino": "clear decision"},
            {"idioma": "ingles", "termino": "full support"},
        ],
    },
    "condiciones_activacion": "Cuando un grupo tiene que tomar una decision en un negocio que depende de lo que sabe, y quieres que el conocimiento de los que saben llegue a la decision en vez de quedarse callado.",
    "entregable_esperado": "Una decision alcanzada por el grupo con los terminos enmarcados con claridad absoluta, y el compromiso de apoyo de todos los implicados, aunque alguno no este de acuerdo.",
    "pasos_accionables": [
        "Abre la primera etapa con discusion libre, en la que todos los puntos de vista y todos los aspectos del asunto se acogen abiertamente y se debaten.",
        "Cuanto mayores sean el desacuerdo y la controversia, mas importante se vuelve la palabra libre.",
        "Vigila la practica contraria, que es la corriente: cuando la reunion se calienta, los participantes se echan atras, tantean hacia donde van las cosas y no dicen nada hasta ver que postura va a imponerse, para apoyarla despues y no quedar asociados a la que pierde.",
        "Cuenta con que, si los que saben se guardan su opinion, lo que se decida se apoyara en informacion y criterio mas incompletos de lo que podrian haber sido.",
        "Pasa despues a la etapa siguiente, que es alcanzar una decision clara, y cuanto mayor sea el desacuerdo sobre el asunto, mas importante se vuelve la palabra clara.",
        "Pon cuidado especial en enmarcar los terminos de la decision con claridad absoluta.",
        "No oscurezcas el asunto para ahorrarte la discusion cuando sepas que la decision es polemica: hablando con medias palabras no evitas la discusion, solo la aplazas.",
        "Cuenta con que a quien no le guste la decision se enfadara bastante mas si no recibe una version pronta y directa de lo que se decidio.",
        "Exige por ultimo que todos los implicados den pleno apoyo a la decision alcanzada por el grupo.",
        "No confundas ese apoyo con el acuerdo: basta con que los participantes se comprometan a respaldar la decision, y ese es un resultado satisfactorio.",
        "Cuenta con que ni el mismo tiempo ni los mismos hechos van a producir acuerdo en muchos asuntos, porque las diferencias de opinion honestas y sentidas existen, y una organizacion no vive de que sus miembros esten de acuerdo en todo.",
        "Pide a todos, y no solo a algunos, que ese compromiso de apoyo este honestamente presente: es lo unico que un mando puede esperar y lo que tiene que conseguir de cada uno.",
    ],
    "resumen_teorico": (
        "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_06.md, unidad Cap. 5, titulo textual Decisions, Decisions. "
        "Sale de la PIEZA P7 de la frontera publicada hoy en OO.2.a, L23 a L29, 484 palabras, y de ningun otro tramo. "
        "POR QUE ES PROCEDIMIENTO, por la prueba del inventario de EXTRACTOR.md 9.1: el libro pone su propio inventario de ETAPAS, "
        "no de fines, y las nombra una a una y en orden (The first stage should be free discussion; The next stage is reaching a clear decision; "
        "Finally, everyone involved must give the decision reached by the group full support), y bajo cada etapa pone el medio con que se ejecuta "
        "(all points of view and all aspects of an issue are openly welcomed and debated; particular pains should be taken to frame the terms of the "
        "decision with utter clarity; so long as the participants commit to back the decision, that is a satisfactory outcome). "
        "NO ES CABEZA DE SERIE Y NO DECLARO NINGUNA ARISTA DE D.37: el libro no dice cuantas etapas son, dice primera, siguiente y finalmente, "
        "asi que la cuenta la haria yo. Por eso las tres etapas viven en UN solo nodo y no en una cabeza con tres partes. "
        "DE DONDE SALE CADA PASO, uno a uno: pasos 1 a 4 de L23 (Illustrated on this page is an ideal model of decision-making in a know-how business. "
        "The first stage should be free discussion, in which all points of view and all aspects of an issue are openly welcomed and debated. "
        "The greater the disagreement and controversy, the more important becomes the word free; Usually when a meeting gets heated, participants hang back, "
        "trying to sense the direction of things, saying nothing until they see what view is likely to prevail. They then throw their support behind that view "
        "to avoid being associated with a losing position; because if knowledgeable people withhold opinions, whatever is decided will be based on information "
        "and insight less complete than it could have been otherwise). "
        "Pasos 5 a 8 de L27 (The next stage is reaching a clear decision. Again, the greater the disagreement about the issue, the more important becomes the "
        "word clear; In fact, particular pains should be taken to frame the terms of the decision with utter clarity; when we know a decision is controversial "
        "we want to obscure matters to avoid an argument. But the argument is not avoided by our being mealy-mouthed, merely postponed; People who don't like a "
        "decision will be a lot madder if they don't get a prompt and straight story about it). "
        "Pasos 9 a 12 de L29 (Finally, everyone involved must give the decision reached by the group full support; This does not necessarily mean agreement: "
        "so long as the participants commit to back the decision, that is a satisfactory outcome; we tend to have honest, strongly felt, real differences of "
        "opinion. No matter how much time we may spend trying to forge agreement, we just won't be able to get it on many issues. But an organization does not "
        "live by its members agreeing with one another at all times about everything; All a manager can expect is that the commitment to support is honestly "
        "present, and this is something he can and must get from everyone). "
        "L25 ES EL PIE DE LA FIGURA (The ideal decision-making process.) y no aporta paso: entra en el tramo y no en los pasos. "
        "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 12 pasos, 12 TRANSCRIPCION, 0 PUENTE. "
        "LOS SITIOS DE TENTACION QUE DECLARO, y en los que NO escribi: NO escribo cuanto dura la discusion libre ni quien la cierra, porque el tramo no lo dice "
        "y eso pertenece a P23 y P24, que son sus propios nodos. NO escribo a quien se le comunica la decision ni por que via, porque el destinatario es la "
        "primera especie de PUENTE que este libro me ha costado. NO escribo como se comprueba despues que el apoyo se mantuvo: el libro pone el compromiso y no "
        "pone su seguimiento. NI UNA CIFRA A atribuciones: el tramo no trae ninguna, y la cita del directivo del automovil es un testimonio anonimo de prensa, "
        "no una medicion del autor con fecha de corte. "
        "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: los pasos 4, 8 y 11 empiezan por Cuenta con, y un lector estricto puede decir que son POSTURA y no accion. "
        "Los sostengo porque los tres son la razon escrita por la que el paso de al lado se ejecuta asi y no de otra manera, y porque sin ellos la etapa queda "
        "con el mandato y sin su criterio. Si caen, caen DENTRO de mi marcado."
    ),
}

if os.path.exists(DESTINO):
    raise SystemExit("YA EXISTE: %s" % DESTINO)
io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(
    json.dumps(NODO, ensure_ascii=False, indent=1) + "\n")
print("ESCRITO: %s" % DESTINO)
print("pasos: %d" % len(NODO["pasos_accionables"]))
