# -*- coding: utf-8 -*-
"""Sustituye en la APERTURA los bloques que reformatee por su salida literal."""
import io
R = "docs/loop/APERTURA_CIEGA.md"
t = io.open(R, encoding="utf-8").read()
n = 0
fallos = []


def sub(viejo, nuevo):
    global t, n
    if viejo not in t:
        fallos.append(viejo[:100])
        return
    t = t.replace(viejo, nuevo, 1)
    n += 1


# 1. el nombre entero de la prueba que cae
sub("      FAIL: test_e_guion_largo_rompe_el_hook (__main__.PruebaE)",
    "      FAIL: test_e_guion_largo_rompe_el_hook "
    "(__main__.PruebaE.test_e_guion_largo_rompe_el_hook)")

# 2. el bloque de bandejas, con su columna entera y su espaciado
sub("""      cuarentena/_derivadas/                -> 2     (fuera de poblacion por D.38.4)
      cuarentena/_insertados/               -> 0     (fuera de poblacion por D.38.4)
      cuarentena/ensayo_referencia_163/     -> 163
      cuarentena/marquet_turn_the_ship/     -> 3
      cuarentena/onu_consumidor/            -> 0
      cuarentena/scott_radical_candor/      -> 102
      cuarentena/smart_who/                 -> 0
      cuarentena/zhuo_manager/              -> 0""",
    """      cuarentena/_derivadas/  -> 2 en bandeja (nivel 1)
      cuarentena/_insertados/  -> 0 en bandeja (nivel 1)
      cuarentena/ensayo_referencia_163/  -> 163 en bandeja (nivel 1)
      cuarentena/marquet_turn_the_ship/  -> 3 en bandeja (nivel 1)
      cuarentena/onu_consumidor/  -> 0 en bandeja (nivel 1)
      cuarentena/scott_radical_candor/  -> 102 en bandeja (nivel 1)
      cuarentena/smart_who/  -> 0 en bandeja (nivel 1)
      cuarentena/zhuo_manager/  -> 0 en bandeja (nivel 1)

**`_derivadas` y `_insertados` quedan FUERA de la poblacion por `D.38.4`, y esa columna la anade mi
lectura: el instrumento solo cuenta los ficheros.**""")

# 3. las dos filas con el espaciado del instrumento
sub("      BANDEJA  385-387    reservar_calendario_tiempo_ejecutar                 4\n"
    "      GRAFO    389-401    aprender_resultados_vencer_dos_presiones            6",
    "      BANDEJA  385-387    reservar_calendario_tiempo_ejecutar                4\n"
    "      GRAFO    389-401    aprender_resultados_vencer_dos_presiones           6")

# 3b. las dos filas de tramo no contiguo, que el instrumento anota y yo me deje
sub("      GRAFO    155-163    adaptar_escucha_cultura_ajena                      9",
    "      GRAFO    155-163    adaptar_escucha_cultura_ajena                      9"
    "  (tramo no contiguo: 155-163 y 131-153)")
sub("      BANDEJA  303-347    persuadir_emocion_oyente_no_propia                 11",
    "      BANDEJA  303-347    persuadir_emocion_oyente_no_propia                11"
    "  (tramo no contiguo: 303-347 y 309-313 y 333-339)")

# 4. el tramo de solapadas: era MI resumen, no la salida.
sub("""    $ python .v29/cobertura_cap07.py   (el tramo de las solapadas)
      131 a 153: GRAFO adaptar_escucha_cultura_ajena | GRAFO crear_cultura_escucha_equipo   (23)
      309 a 313 y 333 a 339: BANDEJA persuadir_emocion_oyente_no_propia dos veces            (12)""",
    """    $ python .v29/cobertura_cap07.py | grep -E "^ (131|153|309|313|333|339):"
       131: GRAFO adaptar_escucha_cultura_ajena | GRAFO crear_cultura_escucha_equipo
       153: GRAFO adaptar_escucha_cultura_ajena | GRAFO crear_cultura_escucha_equipo
       309: BANDEJA persuadir_emocion_oyente_no_propia | BANDEJA persuadir_emocion_oyente_no_propia
       313: BANDEJA persuadir_emocion_oyente_no_propia | BANDEJA persuadir_emocion_oyente_no_propia
       333: BANDEJA persuadir_emocion_oyente_no_propia | BANDEJA persuadir_emocion_oyente_no_propia
       339: BANDEJA persuadir_emocion_oyente_no_propia | BANDEJA persuadir_emocion_oyente_no_propia

**MI CUENTA SOBRE ESA SALIDA, y la firmo como mia y no como del instrumento:** el tramo `131`-`153`
son **`23`** lineas y el tramo `309`-`313` mas `333`-`339` son **`12`**. **`23 + 12 = 35`**, que es
el total que la cabecera del instrumento da.""")

# 5. los cuatro nuevos: un grep reproducible
sub("""    $ tail -4 dataset/nodos.jsonl   (las cuatro que el dataset aniadio sobre las 239 de la ACTA 27)
      recorrer_rueda_conscientemente_cultura_equipo   14 pasos  prev [] sig [hacer_cosas]
      recorrer_rueda_hacer_cosas_equipo               12 pasos  prev [conscientemente] sig []
      crear_espacio_seguro_madurar_ideas_nuevas       14 pasos  prev [] sig []
      crear_obligacion_disentir_equipo                 5 pasos  prev [] sig []""",
    """    $ grep -E "^(ID|PASOS|PREVIOS) " .v29/cuatro_nuevos.txt
      ID       : recorrer_rueda_conscientemente_cultura_equipo
      PASOS    : 14
      PREVIOS  : []
      ID       : recorrer_rueda_hacer_cosas_equipo
      PASOS    : 12
      PREVIOS  : ['recorrer_rueda_conscientemente_cultura_equipo']
      ID       : crear_espacio_seguro_madurar_ideas_nuevas
      PASOS    : 14
      PREVIOS  : []
      ID       : crear_obligacion_disentir_equipo
      PASOS    : 5
      PREVIOS  : []""")

# 6. el dato de la arista, con las dos columnas enteras
sub("""    $ tail -4 dataset/nodos.jsonl
      recorrer_rueda_conscientemente_cultura_equipo   sig: ['recorrer_rueda_hacer_cosas_equipo']
      recorrer_rueda_hacer_cosas_equipo               prev: ['recorrer_rueda_conscientemente_...']""",
    """    $ grep -E "^(ID|PREVIOS|SIGUIENTS) " .v29/cuatro_nuevos.txt | head -6
      ID       : recorrer_rueda_conscientemente_cultura_equipo
      PREVIOS  : []
      SIGUIENTS: ['recorrer_rueda_hacer_cosas_equipo']
      ID       : recorrer_rueda_hacer_cosas_equipo
      PREVIOS  : ['recorrer_rueda_conscientemente_cultura_equipo']
      SIGUIENTS: []""")

# 7. el tramo de la madre, sin inventarme una salida
sub("""    $ python .v29/cap07_estado.py    (el tramo de la madre, leido de su resumen_teorico)
      recorrer_rueda_conscientemente_cultura_equipo:  cap_11 lineas 271 a 299 Y 307 a 333""",
    """    $ python .v29/mapa_capitulos.py scott_radical_candor | grep cap_11
      cap_11                1       15

    (y el tramo de la madre, leido literal de su propio `resumen_teorico` en el dataset)
      UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de
      las lineas 271 a 299 y de las lineas 307 a 333, bajo el rotulo BE CONSCIOUS OF CULTURE y
      sus rotulos interiores. ES LA PIEZA P15 DE LA FRONTERA DE cap_11, Y SU TRAMO ES NO
      CONTIGUO: entre sus dos mitades viven las lineas 301 a 305, que son el rotulo Debate and
      decide explicitly y salen en su propio nodo, debatir_decidir_asuntos_cultura_evitar_delegar.
      Lo digo aqui para que la frontera se pueda comprobar.""")

# 8. los vecinos, con el espaciado del instrumento
sub("         - recorrer_rueda_hacer_cosas_equipo                 GRAFO    [familia_id=0.429]",
    "         - recorrer_rueda_hacer_cosas_equipo                    GRAFO    [familia_id=0.429]")
sub("""         - recorrer_trece_elementos_proceso_evaluacion_formal BANDEJA [paso_contra_nodo=0.61]
         - recorrer_rueda_conscientemente_cultura_equipo      GRAFO   [familia_id=0.429]
         - reconocer_emociones_propias_avisar_equipo          BANDEJA [similitud_texto=0.353]""",
    """         - recorrer_trece_elementos_proceso_evaluacion_formal   BANDEJA  [paso_contra_nodo=0.61]
         - recorrer_rueda_conscientemente_cultura_equipo        GRAFO    [familia_id=0.429]
         - reconocer_emociones_propias_avisar_equipo            BANDEJA  [similitud_texto=0.353]""")
sub("         - nutrir_ideas_nuevas_reunion_solas                  BANDEJA [paso_contra_nodo=0.617]",
    "         - nutrir_ideas_nuevas_reunion_solas                    BANDEJA  [paso_contra_nodo=0.617]")
sub("""         - parar_debate_emocion_agotamiento                   BANDEJA [similitud_texto=0.411]
         - pedir_hechos_decision_evitar_recomendaciones        BANDEJA [similitud_texto=0.474]
         - crear_cultura_escucha_equipo                        GRAFO  [familia_id=0.333]
         - proteger_tiempo_equipo_jefe                         BANDEJA [similitud_texto=0.357]
         - compartir_logica_mostrar_razonamiento               BANDEJA [similitud_texto=0.368]
         - reservar_calendario_tiempo_ejecutar                 BANDEJA [similitud_texto=0.393]
         - cambiar_posicion_hechos_explicar_cambio             GRAFO  [similitud_texto=0.399]
         - aprender_resultados_vencer_dos_presiones            GRAFO  [similitud_texto=0.402]
         - evitar_presion_social_actos_equipo                  BANDEJA [similitud_texto=0.393]
         - crear_plan_creible_equipo                           GRAFO  [familia_id=0.333]""",
    """         - parar_debate_emocion_agotamiento                     BANDEJA  [similitud_texto=0.411]
         - pedir_hechos_decision_evitar_recomendaciones         BANDEJA  [similitud_texto=0.474]
         - crear_cultura_escucha_equipo                         GRAFO    [familia_id=0.333]
         - proteger_tiempo_equipo_jefe                          BANDEJA  [similitud_texto=0.357]
         - compartir_logica_mostrar_razonamiento                BANDEJA  [similitud_texto=0.368]
         - reservar_calendario_tiempo_ejecutar                  BANDEJA  [similitud_texto=0.393]
         - cambiar_posicion_hechos_explicar_cambio              GRAFO    [similitud_texto=0.399]
         - aprender_resultados_vencer_dos_presiones             GRAFO    [similitud_texto=0.402]
         - evitar_presion_social_actos_equipo                   BANDEJA  [similitud_texto=0.393]
         - crear_plan_creible_equipo                            GRAFO    [familia_id=0.333]""")

io.open(R, "w", encoding="utf-8", newline="\n").write(t)
print("sustituciones hechas: %d" % n)
for f in fallos:
    print("NO ENCONTRADO: %s" % f)
