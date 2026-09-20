# -*- coding: utf-8 -*-
"""CANDIDATO 8 DE LA VUELTA 53: cap_06 P31, L93, LA DECISION QUE DEFRAUDA A LOS QUE PARTICIPARON.

Se escribe y se pasa por la aduana EN EL MISMO ACTO (EXTRACTOR.md 16).
"""
import io
import json
import os

ID = "anunciar_decision_inesperada_reconvocar_reunion"
DESTINO = "cuarentena/grove_high_output/%s.json" % ID

NODO = {
    "id": ID,
    "titulo": "Anunciar una decision radicalmente distinta de lo que el grupo esperaba, y reconvocar la reunion en vez de marcharse",
    "dominio": "gestion_equipos",
    "estado": "vivo",
    "ids_alias": [],
    "nodos_previos": [],
    "nodos_siguientes": [],
    "atribuciones": [],
    "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
    "denominaciones": {
        "nombre_largo": "Que hacer cuando la palabra final es radicalmente distinta de lo que esperaban los que participaron: anunciar, no marcharse, levantar la sesion, reconvocar cuando se hayan recuperado y pedirles entonces su opinion",
        "sigla": "",
        "otros_idiomas": [
            {"idioma": "ingles", "termino": "final word"},
            {"idioma": "ingles", "termino": "adjourn"},
        ],
    },
    "condiciones_activacion": "Cuando la palabra final sobre una decision va a ser radicalmente distinta de lo que esperaban las personas que participaron en el proceso de decision.",
    "entregable_esperado": "El anuncio hecho, la sesion levantada, la reunion reconvocada despues de que la gente se haya recuperado, y las opiniones del grupo sobre la decision recogidas en esa segunda sesion.",
    "pasos_accionables": [
        "Comprueba la condicion: la palabra final va a ser radicalmente distinta de lo que esperaban las personas que participaron en el proceso de decision.",
        "Haz tu anuncio.",
        "No te limites a anunciarlo y marcharte del asunto.",
        "Cuenta con que la gente necesita tiempo para ajustarse, racionalizar y, en general, recomponerse.",
        "Levanta la sesion.",
        "Reconvoca la reunion despues de que la gente haya tenido ocasion de recuperarse.",
        "Pideles entonces su opinion sobre la decision.",
        "Cuenta con lo que eso consigue: ayuda a todo el mundo a aceptar lo inesperado y a aprender a vivir con ello.",
    ],
    "resumen_teorico": (
        "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_06.md, unidad Cap. 5, titulo textual Decisions, Decisions. "
        "Sale de la PIEZA P31 de la frontera publicada hoy en OO.2.a, L93, 95 palabras, y de ningun otro tramo. "
        "POR QUE ES PROCEDIMIENTO, por la prueba del inventario de EXTRACTOR.md 9.1: el libro pone su propio inventario de ETAPAS y las nombra una a una y en "
        "orden, con tres verbos seguidos en imperativo (make your announcement but don't just walk away from the issue; Adjourn, reconvene the meeting after "
        "people have had a chance to recover, and solicit their views of the decision at that time). No hay adjetivo de adecuacion en el sitio del criterio: "
        "la condicion de activacion esta escrita (dramatically different from the expectations) y el disparador de la reconvocatoria tambien (after people "
        "have had a chance to recover). "
        "DE DONDE SALE CADA PASO, uno a uno, todos de L93: paso 1 (If the final word has to be dramatically different from the expectations of the people who "
        "participated in the decision-making process); paso 2 (make your announcement); paso 3 (but don't just walk away from the issue); paso 4 (People need "
        "time to adjust, rationalize, and in general put their heads back together); paso 5 (Adjourn); paso 6 (reconvene the meeting after people have had a "
        "chance to recover); paso 7 (and solicit their views of the decision at that time); paso 8 (This will help everybody accept and learn to live with "
        "the unexpected). "
        "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 8 pasos, 8 TRANSCRIPCION, 0 PUENTE. "
        "LOS SITIOS DE TENTACION QUE DECLARO, y en los que NO escribi: NO escribo CUANTO se espera antes de reconvocar, porque el libro pone el disparador en "
        "el estado de la gente (after people have had a chance to recover) y no en el reloj, y poner ahi un dia o una semana es exactamente la segunda "
        "especie de PUENTE del lote 1. NO escribo que se levante acta de la segunda sesion ni que las opiniones recogidas se hagan algo, porque el libro "
        "cierra el tramo ahi y cerrarle el bucle seria escribir yo el paso. NO escribo quien hace el anuncio cuando el que decidio no esta. "
        "EL PARENTESIS DEL AUTOR NO ES PASO (manual 3.5): had I chosen, for example, to cancel the Philippine plant project altogether es el ejemplo con el "
        "que el libro ilustra la condicion, del caso de Filipinas que ocupa L79 a L89, y por eso ni el entregable ni ningun paso llevan el nombre de aquella "
        "planta. "
        "NI UNA CIFRA A atribuciones: el tramo no trae ninguna. "
        "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: con 95 palabras y ocho pasos, este nodo tiene casi tantos pasos como frases el parrafo, y el aviso "
        "de 15.4 dice que un parrafo pobre produce un nodo inventado. Lo sostengo porque el parrafo NO es pobre en medios pese a ser corto: trae cinco verbos "
        "de accion encadenados y su condicion de entrada, y ninguno de mis ocho pasos anade un medio que el no nombre. Si cae, cae DENTRO de mi marcado."
    ),
}

if os.path.exists(DESTINO):
    raise SystemExit("YA EXISTE: %s" % DESTINO)
io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(
    json.dumps(NODO, ensure_ascii=False, indent=1) + "\n")
print("ESCRITO: %s" % DESTINO)
print("pasos: %d" % len(NODO["pasos_accionables"]))
