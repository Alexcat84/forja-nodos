# -*- coding: utf-8 -*-
"""LAS ARISTAS QUE MI LECTURA LEVANTA Y NINGUNA SENAL LEVANTO (`D.29`, `EXTRACTOR.md` 11).

**ESTE FRENTE NO INSERTA** (`D.45`), asi que `python forja.py arista` NO se corre aqui: escribiria
en `bitacora/` y en `dataset/`, que son sede de la aduana. Lo que este instrumento hace es lo unico
que se puede hacer sin insertar y sin teclear: **pegar el paso de la madre que nombra al hijo**,
leido del propio candidato, al lado del comando que se correra el dia de la insercion.

El instrumento **revienta si el paso citado no existe** en el candidato, asi que una arista con la
linea mal apuntada no puede salir publicada como buena.
"""
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BANDEJA = "cuarentena/grove_high_output/%s.json"

# LO QUE PONGO YO LEYENDO: (madre, paso de la madre, hijo, regla, razon)
ARISTAS = [
    ("construir_flujo_produccion_paso_limitante", 9, "rehacer_flujo_paso_limitante_capacidad", "D.29",
     "el paso 9 de la madre construye los desfases, y el hijo es el unico tramo del libro que manda "
     "ALTERARLOS: L51 dice but your time offsets must be altered. El hijo empieza donde la madre "
     "acaba, y lo dice nombrando el producto de la madre (our breakfast operation assumed infinite "
     "capacity)"),
    ("clasificar_trabajo_proceso_montaje_prueba", 3, "preferir_inspeccion_proceso_prueba_destructiva", "D.29",
     "el paso 3 de la madre nombra la prueba en una linea y dice que somete los componentes o el "
     "total a un examen; el hijo despliega en seis pasos QUE CLASE de prueba se elige cuando la "
     "operacion es continua, que la madre no tiene"),
    ("detectar_arreglar_fallo_etapa_menor_valor", 6, "clasificar_trabajo_proceso_montaje_prueba", "D.29",
     "el paso 6 de la madre nombra la prueba unitaria de las piezas en una linea, y el hijo es quien "
     "la despliega con su vuelta a proceso, su montaje y su prueba de sistema"),
    ("detectar_arreglar_fallo_etapa_menor_valor", 4, "dimensionar_inventario_materia_prima_reposicion", "D.29",
     "el paso 4 de la madre nombra rechazar el material cuando lo entrega el proveedor, y el hijo es "
     "quien despliega esa inspeccion de recepcion y lo que hay que tener para poder rechazar sin "
     "pararse"),
]

print("| # | madre | `--paso` | el paso de la madre, pegado de su fichero | hijo | regla | por que |")
print("|---:|---|---:|---|---|---|---|")
for numero, (madre, paso, hijo, regla, razon) in enumerate(ARISTAS, 1):
    datos = json.load(io.open(BANDEJA % madre, encoding="utf-8"))
    pasos = datos["pasos_accionables"]
    if paso < 1 or paso > len(pasos):
        raise SystemExit("LA MADRE %s NO TIENE PASO %d: tiene %d" % (madre, paso, len(pasos)))
    texto = pasos[paso - 1].replace("|", "/")
    print("| %d | `%s` | `%d` | `%s` | `%s` | `%s` | %s |"
          % (numero, madre, paso, texto[:150] + ("..." if len(texto) > 150 else ""),
             hijo, regla, razon))
print("")
print("LOS COMANDOS QUE SE CORRERAN EL DIA DE LA INSERCION, Y QUE HOY NO SE CORREN (D.45)")
for madre, paso, hijo, _regla, razon in ARISTAS:
    print("")
    print("    python forja.py arista --madre %s \\" % madre)
    print("        --hijo %s --paso %d \\" % (hijo, paso))
    print("        --razon \"%s\"" % razon.replace("\"", ""))
print("")
print("ARISTAS DECLARADAS POR LECTURA : %d" % len(ARISTAS))
print("CABLEADAS EN ESTA VUELTA       : 0   (este frente no inserta: D.45)")
