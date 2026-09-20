# -*- coding: utf-8 -*-
"""CANDIDATO 5 DE LA VUELTA 53: cap_06 P23, L61, CUANDO EL PODER DE POSICION ES LEGITIMO.

Se escribe y se pasa por la aduana EN EL MISMO ACTO (EXTRACTOR.md 16).
"""
import io
import json
import os

ID = "ejercer_poder_posicion_etapa_decision_clara"
DESTINO = "cuarentena/grove_high_output/%s.json" % ID

NODO = {
    "id": ID,
    "titulo": "Ejercer el poder de posicion solo al llegar a la etapa de decision clara sin consenso, y nunca antes",
    "dominio": "gestion_equipos",
    "estado": "vivo",
    "ids_alias": [],
    "nodos_previos": [],
    "nodos_siguientes": [],
    "atribuciones": [],
    "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
    "denominaciones": {
        "nombre_largo": "La condicion y la prohibicion del poder de posicion: legitimo, y a veces inevitable, cuando se alcanza la etapa de decision clara y no hay consenso; no legitimo y destructivo un minuto antes",
        "sigla": "",
        "otros_idiomas": [
            {"idioma": "ingles", "termino": "position-power authority"},
            {"idioma": "ingles", "termino": "peer-plus-one"},
            {"idioma": "ingles", "termino": "position-power prejudice"},
        ],
    },
    "condiciones_activacion": "Cuando ninguna cantidad de discusion va a producir consenso y el momento de decidir ha llegado claramente, y el que dirige el grupo tiene que decidir si usa ya su autoridad de rango.",
    "entregable_esperado": "La decision tomada por la persona de mayor rango, con el beneficio completo de la discusion libre detras, y la constancia de que la autoridad de rango no se ejercio antes de la etapa de decision clara.",
    "pasos_accionables": [
        "Reconoce la situacion por sus dos mitades: ninguna cantidad de discusion va a producir consenso, y aun asi el momento de decidir ha llegado claramente.",
        "Cuando eso pase, acepta que la persona de mayor rango, la del par mas uno, que hasta ahora ha guiado, entrenado y espoleado al grupo, no tiene mas remedio que tomar ella misma la decision.",
        "Comprueba que el proceso vino bien hasta ese punto: que quien decide lo hace con el beneficio completo de la discusion libre, en la que todos los puntos de vista, hechos, opiniones y juicios se expusieron sin el prejuicio del poder de posicion.",
        "Ejerce entonces la autoridad del poder de posicion, que ahi es legitima y a veces inevitable, porque se alcanzo la etapa de decision clara y no aparecio ningun consenso.",
        "No la ejerzas ni un momento antes: ejercerla antes no es legitimo, y es destructivo.",
        "Cuenta con que esto no suele ser facil, porque existe reticencia a ejercer el poder de posicion de forma deliberada y explicita, ya que dar ordenes parece poco amable.",
        "Vigila la consecuencia de esa reticencia: alarga la primera fase del proceso, que es el tiempo de discusion libre, mas alla del punto optimo, y la decision se aplaza.",
    ],
    "resumen_teorico": (
        "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_06.md, unidad Cap. 5, titulo textual Decisions, Decisions. "
        "Sale de la PIEZA P23 de la frontera publicada hoy en OO.2.a, L61, 187 palabras, y de ningun otro tramo. "
        "POR QUE ES PROCEDIMIENTO, por la prueba del inventario de EXTRACTOR.md 9.1: el libro no pone un adjetivo de adecuacion en el sitio del criterio, "
        "pone la CONDICION exacta y su contraria, las dos escritas y enfrentadas (it is legitimate, in fact, sometimes unavoidable, for the senior person to "
        "wield position-power authority IF the clear decision stage is reached and no consensus has developed; It is not legitimate, in fact, it is "
        "destructive, for him to wield that authority any earlier), y nombra ademas el estado que hay que comprobar antes (having had the full benefit of "
        "free discussion wherein all points of view, facts, opinions, and judgments were aired without position-power prejudice). "
        "DE DONDE SALE CADA PASO, uno a uno, todos de L61: paso 1 (Sometimes no amount of discussion will produce a consensus, yet the time for a decision "
        "has clearly arrived); paso 2 (When this happens, the senior person or peer-plus-one who until now has guided, coached, and prodded the group along "
        "has no choice but to make a decision himself); paso 3 (If the decision-making process has proceeded correctly up to this point, the senior manager "
        "will be making the decision having had the full benefit of free discussion wherein all points of view, facts, opinions, and judgments were aired "
        "without position-power prejudice); paso 4 (it is legitimate, in fact, sometimes unavoidable, for the senior person to wield position-power authority "
        "if the clear decision stage is reached and no consensus has developed); paso 5 (It is not legitimate, in fact, it is destructive, for him to wield "
        "that authority any earlier); paso 6 (This is often not easy. We Americans tend to be reluctant to exercise position power deliberately and "
        "explicitly, it is just not nice to give orders); paso 7 (Such reluctance on the part of the senior manager can prolong the first phase of the "
        "decision-making process, the time of free discussion, past the optimum point, and the decision will be put off). "
        "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 7 pasos, 7 TRANSCRIPCION, 0 PUENTE. "
        "EL SITIO DONDE MAS TENIA QUE VIGILARME: el libro dice We Americans en el paso 6, y la tentacion era generalizarlo a todo el mundo o, al reves, "
        "convertirlo en una advertencia cultural; lo dejo como lo que el texto pone, una reticencia descrita, sin nacionalidad en el paso porque el paso se "
        "ejecuta igual la tenga quien la tenga. LO DEMAS QUE NO ESCRIBO: NO escribo cuanto se espera antes de declarar que el consenso no va a salir, porque "
        "el libro dice clearly arrived y no pone plazo, y el plazo es la segunda especie de PUENTE del lote 1. NO escribo como se comunica esa decision ni a "
        "quien, que es la primera especie. NO escribo quien comprueba que el proceso vino bien. NI UNA CIFRA A atribuciones: el tramo no trae ninguna. "
        "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: este nodo y el de P24 caen los dos sobre el momento de decidir y van a levantar vecindad entre si. "
        "Sostengo que son HERMANOS y no gemelos: este dice QUIEN puede ejercer autoridad de rango y bajo que condicion, y aquel dice CUANDO se corta la "
        "discusion, con un criterio que vale tambien cuando si hay consenso. Si cae, cae DENTRO de mi marcado."
    ),
}

if os.path.exists(DESTINO):
    raise SystemExit("YA EXISTE: %s" % DESTINO)
io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(
    json.dumps(NODO, ensure_ascii=False, indent=1) + "\n")
print("ESCRITO: %s" % DESTINO)
print("pasos: %d" % len(NODO["pasos_accionables"]))
