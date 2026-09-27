# -*- coding: utf-8 -*-
"""LAS ARISTAS QUE LEVANTA MI LECTURA Y QUE NINGUNA SENAL LEVANTO (D.29, EXTRACTOR.md 11).

ESTE FRENTE NO CABLEA NINGUNA: python forja.py arista escribe en bitacora/ y en
dataset/, y D.45 dice que este frente no inserta. Quedan escritas con su razon y con
EL PASO DE LA MADRE PEGADO DE SU PROPIO FICHERO, que es el remedio mecanico de D.35
aplicado a esta sede: la cita se pega, no se promete.

El instrumento PARA si el paso citado no existe en la madre, o si la madre o el hijo no
estan en la bandeja. Una arista cuya cita no se puede abrir no se publica.
"""
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BANDEJA = "cuarentena/grove_high_output/%s.json"

# madre, paso de la madre, hijo, regla, razon
ARISTAS = [
    ("dimensionar_inventario_materia_prima_reposicion", 3,
     "decidir_aceptar_rechazar_material_defectuoso", "D.29",
     "el paso 3 de la madre despacha en una linea que el material inaceptable se devuelve, y nombra "
     "el precio de hacerlo (sin material, y por tanto parado). El hijo es quien despliega esa "
     "encrucijada en ocho pasos que la madre no tiene: las DOS salidas, devolver o renunciar a la "
     "especificacion, la comparacion de costes entre una y otra, el grupo de las tres areas que lo "
     "decide y la excepcion de fiabilidad que no admite componenda"),
    ("casar_flujo_fabricacion_flujo_ventas", 11,
     "detectar_arreglar_fallo_etapa_menor_valor", "D.29",
     "el paso 11 de la madre manda guardar el inventario en la etapa de menor valor y el propio "
     "libro lo dice remitiendose atras (as we have learned before, L119). El hijo es quien despliega "
     "que es esa etapa de menor valor, ordenando las etapas por el valor que el material lleva "
     "encima, cosa que la madre usa y no explica"),
    ("dimensionar_plantilla_administrativa_pronostico", 1,
     "elegir_indicador_salida_trabajo_administrativo", "D.29",
     "el paso 1 de la madre pone como condicion de entrada haber elegido con cuidado los indicadores "
     "que caracterizan a la unidad administrativa, y lo dice en una linea. El hijo es quien despliega "
     "COMO se elige ese indicador, con las dos varas del libro y su pareja de calidad, en siete pasos "
     "que la madre no tiene"),
    ("representar_actividad_caja_negra_ventanas", 8,
     "construir_indicador_linealidad_alerta_temprana", "D.29",
     "el paso 8 de la madre manda recortar ventanas en la caja y no dice cuales. El libro nombra esta "
     "en una linea y con esas palabras: A generally applicable example of a window cut into the black "
     "box is the linearity indicator (L83). El hijo la despliega en nueve pasos"),
    ("representar_actividad_caja_negra_ventanas", 8,
     "construir_indicador_tendencia_patron", "D.29",
     "misma madre y mismo paso, y el libro vuelve a usar la palabra ventana para este otro: This "
     "extrapolation gives us another window in our black box (L89). El hijo lo despliega en seis pasos"),
    ("elegir_fabricar_pedido_pronostico", 4,
     "casar_flujo_fabricacion_flujo_ventas", "D.29",
     "el paso 4 de la madre manda pasar a fabricar contra pronostico y ahi se detiene. El libro "
     "empalma con el hijo en la frase siguiente del capitulo: Delivering a product that was built to "
     "forecast to a customer consists of two simultaneous processes (L111). El hijo despliega esa "
     "entrega en doce pasos que la madre no tiene"),
]

# LAS QUE MI LECTURA CONSIDERO Y NO DECLARA, con el motivo por el que no
DESCARTADAS = [
    ("representar_actividad_caja_negra_ventanas",
     "construir_grafico_escalonado_pronosticos",
     "el libro NO llama ventana al grafico escalonado. Lo presenta como Another sound way to "
     "anticipate the future (L91), no como una ventana recortada en la caja, y las otras dos si "
     "llevan la palabra escrita. EXTRACTOR.md 15.6: la parte tiene que ser la que ese paso nombra, "
     "y compartir seccion y tema no autoriza la arista"),
    ("elegir_indicador_salida_trabajo_administrativo",
     "emparejar_indicadores_efecto_contraefecto",
     "el paso 5 de la primera manda emparejar el indicador de cantidad con uno de CALIDAD, y el "
     "segundo nodo empareja el efecto con su CONTRAEFECTO. Son dos pares distintos, y declarar la "
     "arista seria declararla porque comparten la palabra emparejar. Los dejo como lo que mi lectura "
     "dice que son, dos procedimientos hermanos"),
    ("elegir_inspeccion_barrera_monitorizacion",
     "variar_frecuencia_inspeccion_nivel_calidad",
     "el libro los presenta como dos maneras PARALELAS de bajar el coste del aseguramiento de la "
     "calidad: L143 abre con Another way to lower the cost of quality assurance, o sea otra ademas de "
     "la anterior, no una parte de ella. EXTRACTOR.md 15.6 dice que un vecino que no es una de las "
     "partes de la cabeza es un hermano, y su veredicto es SANO"),
]

problemas = []
filas = []
for madre, paso, hijo, regla, razon in ARISTAS:
    try:
        datos_madre = json.load(io.open(BANDEJA % madre, encoding="utf-8"))
    except IOError:
        problemas.append("no encuentro la madre %s en la bandeja" % madre)
        continue
    try:
        json.load(io.open(BANDEJA % hijo, encoding="utf-8"))
    except IOError:
        problemas.append("no encuentro el hijo %s en la bandeja" % hijo)
        continue
    pasos = datos_madre["pasos_accionables"]
    if paso < 1 or paso > len(pasos):
        problemas.append("%s no tiene paso %d: tiene %d" % (madre, paso, len(pasos)))
        continue
    filas.append((madre, paso, pasos[paso - 1], hijo, regla, razon))

if problemas:
    print("NO SE PUBLICA NINGUNA ARISTA. Lo que falla:")
    for linea in problemas:
        print("  " + linea)
    raise SystemExit(1)

print("| # | madre | `--paso` | el paso de la madre, pegado de su fichero | hijo | regla | por que |")
print("|---:|---|---:|---|---|---|---|")
for indice, (madre, paso, texto, hijo, regla, razon) in enumerate(filas, 1):
    print("| %d | `%s` | `%d` | %s | `%s` | `%s` | %s |"
          % (indice, madre, paso, texto, hijo, regla, razon))
print("")
print("=" * 78)
print("LAS QUE MI LECTURA CONSIDERO Y NO DECLARA, Y EL MOTIVO DE CADA UNA")
print("=" * 78)
print("")
print("| par que considere | por que NO declaro la arista |")
print("|---|---|")
for madre, hijo, razon in DESCARTADAS:
    print("| `%s` con `%s` | %s |" % (madre, hijo, razon))
print("")
print("ARISTAS DECLARADAS POR LECTURA : %d" % len(filas))
print("CONSIDERADAS Y NO DECLARADAS   : %d" % len(DESCARTADAS))
print("CABLEADAS HOY                  : 0   (D.45: este frente no inserta)")
print("DE ELLAS POR D.37 (el texto dice CUANTAS partes): 0. Ningun tramo de cap_03 dice")
print("cuantas partes tiene, asi que las %d son D.29 y las %d llevan razon escrita."
      % (len(filas), len(filas)))
