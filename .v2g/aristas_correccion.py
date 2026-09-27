# -*- coding: utf-8 -*-
"""CORRECCION DECLARADA DE AA.4: DOS ARISTAS MAS, ENCONTRADAS RELEYENDO LA COLA DE LA ADUANA.

NO TOCA .v2g/aristas.py NI SU SALIDA. AA.4 se publico con 6 declaradas y 3 rechazadas y ahi
se queda, porque en esta casa una lectura perdedora se corrige por correccion declarada y
SIN BORRAR (P.17). Esto es la correccion, con su propio fichero y su propia tabla.

QUE PASO, Y ES LO QUE EXTRACTOR.md 11 dice que tiene que pasar: la senal no declara la
arista, pero SI ORDENA DONDE LEER. La aduana levanto seis candidatos con cola, y al leer
esos vecinos aparecieron dos lineas del libro que yo no habia pesado al escribir AA.4. Las
dos son remisiones explicitas del propio texto hacia atras.
"""
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BANDEJA = "cuarentena/grove_high_output/%s.json"
LIBRO = io.open("fuentes/grove_high_output/cap_03.md", encoding="utf-8").read().split("\n")

NUEVAS = [
    ("elegir_indicador_salida_trabajo_administrativo", 5,
     "emparejar_indicadores_efecto_contraefecto", "D.29", 35,
     "la linea que no habia pesado: L35 abre la seccion administrativa usando paired indicators "
     "como concepto YA INTRODUCIDO, y el que lo introdujo es L31, que es el hijo. El paso 5 de la "
     "madre manda emparejar en una linea y el hijo despliega el emparejado en siete pasos que la "
     "madre no tiene. En AA.4 lo rechace por creer que la pareja de calidad y la de contraefecto "
     "eran dos cosas distintas; lo son como EJEMPLO, no como procedimiento nombrado"),
    ("casar_flujo_fabricacion_flujo_ventas", 12,
     "construir_grafico_escalonado_pronosticos", "D.29", 121,
     "la segunda linea que no habia pesado: L121 dice use stagger charts in both the manufacturing "
     "and sales forecasts. As noted, y ese As noted remite a L91, que es donde el grafico "
     "escalonado se monta. El paso 12 de la madre manda usarlos en dos sitios y el hijo es quien "
     "dice como se monta uno, en ocho pasos. En AA.4 esta arista no aparecia ni declarada ni "
     "rechazada: sencillamente no la habia visto"),
]


def llana(texto):
    for viejo, nuevo in ((chr(0x2014), "-"), (chr(0x2013), "-"), (chr(0x2018), "'"),
                         (chr(0x2019), "'"), (chr(0x201C), '"'), (chr(0x201D), '"')):
        texto = texto.replace(viejo, nuevo)
    return texto


problemas = []
filas = []
for madre, paso, hijo, regla, linea_libro, razon in NUEVAS:
    datos_madre = json.load(io.open(BANDEJA % madre, encoding="utf-8"))
    json.load(io.open(BANDEJA % hijo, encoding="utf-8"))
    pasos = datos_madre["pasos_accionables"]
    if paso < 1 or paso > len(pasos):
        problemas.append("%s no tiene paso %d" % (madre, paso))
        continue
    filas.append((madre, paso, pasos[paso - 1], hijo, regla, linea_libro,
                  llana(LIBRO[linea_libro - 1])[:150], razon))

if problemas:
    for linea in problemas:
        print(linea)
    raise SystemExit(1)

print("| # | madre | `--paso` | el paso de la madre, pegado de su fichero | hijo | regla | la linea del libro que la sostiene, pegada | por que no estaba en `AA.4` |")
print("|---:|---|---:|---|---|---|---|---|")
for indice, fila in enumerate(filas, 7):
    madre, paso, texto, hijo, regla, linea_libro, cita, razon = fila
    print("| %d | `%s` | `%d` | %s | `%s` | `%s` | `L%d: %s` | %s |"
          % (indice, madre, paso, texto, hijo, regla, linea_libro, cita, razon))
print("")
print("ARISTAS DECLARADAS EN AA.4                 : 6")
print("ARISTAS ANADIDAS POR ESTA CORRECCION       : %d" % len(filas))
print("TOTAL DECLARADAS POR LECTURA EN LA VUELTA  : %d" % (6 + len(filas)))
print("CONSIDERADAS Y RECHAZADAS, TRAS CORREGIR   : 2")
print("  la del grafico escalonado como ventana de la caja negra: SIGUE RECHAZADA")
print("  la de barrera contra inspeccion variable               : SIGUE RECHAZADA")
print("  la de indicador administrativo con emparejar           : PASA A DECLARADA")
print("CABLEADAS HOY                              : 0   (D.45: este frente no inserta)")
