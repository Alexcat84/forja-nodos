# -*- coding: utf-8 -*-
"""CANDIDATO 4 DE LA VUELTA 53: cap_06 P18, L51, QUIEN TOMA EL MANDO SIN PRESIDENTE.

Se escribe y se pasa por la aduana EN EL MISMO ACTO (EXTRACTOR.md 16).
"""
import io
import json
import os

ID = "tomar_mando_reunion_pares_presidente_ausente"
DESTINO = "cuarentena/grove_high_output/%s.json" % ID

NODO = {
    "id": ID,
    "titulo": "Decidir quien toma el mando en una reunion de iguales sin presidente formal: el que mas se juega, y si no, el de mayor rango presente",
    "dominio": "gestion_equipos",
    "estado": "vivo",
    "ids_alias": [],
    "nodos_previos": [],
    "nodos_siguientes": [],
    "atribuciones": [],
    "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
    "denominaciones": {
        "nombre_largo": "El remedio del par mas uno: cuando el sindrome del grupo de pares se manifiesta y la reunion no tiene presidente formal, toma el mando el que mas se juega, y si eso no funciona, la persona presente de mayor rango",
        "sigla": "",
        "otros_idiomas": [
            {"idioma": "ingles", "termino": "peer-plus-one approach"},
            {"idioma": "ingles", "termino": "peer-group syndrome"},
            {"idioma": "ingles", "termino": "godfather"},
        ],
    },
    "condiciones_activacion": "Cuando el sindrome del grupo de pares se manifiesta en una reunion de iguales y esa reunion no tiene presidente formal, de manera que el grupo da vueltas sin que nadie lo enderece.",
    "entregable_esperado": "Alguien con el mando de la reunion tomado: el que mas se juega en el asunto, o en su defecto la persona presente de mayor rango, actuando de padrino y devolviendo al grupo la confianza para decidir.",
    "pasos_accionables": [
        "Comprueba primero las dos condiciones juntas: que el sindrome del grupo de pares se este manifestando, y que la reunion no tenga presidente formal.",
        "Haz entonces que tome el mando la persona que mas se juega en el asunto.",
        "Si eso no funciona, pide siempre que puedas a la persona presente de mayor rango que asuma el control.",
        "No cuentes con que esa persona sea mas experta en los asuntos que se tratan que los demas miembros del grupo, y cuenta con que probablemente lo sea menos.",
        "Cuenta con lo que si es probable que aporte: actuar de padrino, es decir, de deposito de conocimiento sobre como deben tomarse las decisiones.",
        "Cuenta con lo que eso le da al grupo: la confianza que hace falta para tomar una decision.",
    ],
    "resumen_teorico": (
        "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_06.md, unidad Cap. 5, titulo textual Decisions, Decisions. "
        "Sale de la PIEZA P18 de la frontera publicada hoy en OO.2.a, L51, 89 palabras. "
        "FRONTERA DENTRO DEL NODO, PUBLICADA ANTES DE CORTAR (EXTRACTOR.md 10): LOS SEIS PASOS SALEN LOS SEIS DE L51 y de ningun otro sitio. "
        "Lo unico que viene de otro tramo es el NOMBRE del remedio, peer-plus-one approach, que el libro acuna en L41 (We named this the peer-plus-one "
        "approach, and have used it since then to aid decision-making where we must), y por eso va en denominaciones y NO en los pasos. "
        "Y EL CASO DE L41 ES CASO Y NO CASA (manual 3.5): el juego de papeles de la primera sesion de formacion de Intel, con sus quince minutos de vueltas "
        "y el presidente que vuelve a entrar y golpea la mesa, es el EJEMPLO NOMBRADO de esta doctrina, no su nodo. Por eso NI EL ENTREGABLE NI NINGUN PASO "
        "llevan un dato de aquel caso, que es la senial barata de que un caso se convirtio en casa. "
        "POR QUE ES PROCEDIMIENTO, por la prueba del inventario de EXTRACTOR.md 9.1: el libro pone la condicion de activacion con sus dos mitades, pone la "
        "accion, pone la alternativa para cuando la primera falla, y pone lo que hay que esperar y lo que no de quien asume el control. Inventario de MEDIOS "
        "y de ETAPAS, no de fines. "
        "DE DONDE SALE CADA PASO, uno a uno, todos de L51: paso 1 (If the peer-group syndrome manifests itself, and the meeting has no formal chairman); "
        "paso 2 (the person who has the most at stake should take charge); paso 3 (If that doesn't work, one can always ask the senior person present to "
        "assume control); paso 4 (He is likely to be no more expert in the issues at hand than other members of the group, perhaps less expert); paso 5 (but "
        "he is likely to act as a godfather, a repository of knowledge about how decisions should be made); paso 6 (and give the group the confidence needed "
        "to make a decision). "
        "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 6 pasos, 6 TRANSCRIPCION, 0 PUENTE. "
        "LOS SITIOS DE TENTACION QUE DECLARO, y en los que NO escribi: NO escribo COMO se averigua quien se juega mas, porque el libro lo nombra y no pone la "
        "prueba. NO escribo cuanto tiempo se espera antes de declarar que no funciona y pasar al de mayor rango: el periodo es la segunda especie de PUENTE "
        "del lote 1, y aqui la tentacion es fuerte porque el caso de L41 trae unos quince minutos; esos quince minutos son del CASO y no del procedimiento, "
        "y meterlos como umbral seria exactamente convertir el caso en casa. NO escribo quien nombra al que toma el mando. NI UNA CIFRA A atribuciones. "
        "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: este nodo y el de P17 tratan los dos el mismo sindrome y van a levantar vecindad entre si. Sostengo "
        "que son HERMANOS: P17 previene, trabajando la autoconfianza de cada miembro antes y despues de la reunion, y este repara, diciendo quien coge el "
        "mando cuando el sindrome ya se manifesto y no hay presidente. Si cae, cae DENTRO de mi marcado."
    ),
}

if os.path.exists(DESTINO):
    raise SystemExit("YA EXISTE: %s" % DESTINO)
io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(
    json.dumps(NODO, ensure_ascii=False, indent=1) + "\n")
print("ESCRITO: %s" % DESTINO)
print("pasos: %d" % len(NODO["pasos_accionables"]))
