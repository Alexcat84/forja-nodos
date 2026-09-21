# -*- coding: utf-8 -*-
"""EL SALDO DE LA ADUANA, CANDIDATO A CANDIDATO, LEIDO DE MIS PROPIOS INFORMES.

Cada fila sale de .v2g/informe_<id>.txt, que es la salida literal de
python forja.py informe cuarentena/grove_high_output/<id>.json corrida en el acto de
escribir ese candidato (EXTRACTOR.md 16). NINGUNA CELDA SE TECLEA: el veredicto de
puerta, la poblacion y los vecinos se sacan del fichero con expresiones regulares, y el
instrumento revienta si a un candidato le falta su informe o si el informe es de otro.

LA POBLACION DE CADA FILA ES LA QUE ESE INFORME MIDIO, y por eso va en su propia celda:
crece segun se van escribiendo candidatos en la bandeja, asi que no hay UNA poblacion de
la tanda sino una por informe (remedio bloqueante de PARA_ALEXIS.md 4).
"""
import glob
import io
import os
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

ORDEN = [
    ("elegir_cinco_indicadores_diarios_fabrica", "P2"),
    ("emparejar_indicadores_efecto_contraefecto", "P3"),
    ("elegir_indicador_salida_trabajo_administrativo", "P4 mas P5"),
    ("representar_actividad_caja_negra_ventanas", "P7"),
    ("construir_indicador_linealidad_alerta_temprana", "P9"),
    ("construir_indicador_tendencia_patron", "P10"),
    ("construir_grafico_escalonado_pronosticos", "P11"),
    ("archivar_indicadores_resolver_problemas", "P12"),
    ("elegir_fabricar_pedido_pronostico", "P13"),
    ("casar_flujo_fabricacion_flujo_ventas", "P14"),
    ("dimensionar_plantilla_administrativa_pronostico", "P15"),
    ("decidir_aceptar_rechazar_material_defectuoso", "P17"),
    ("elegir_inspeccion_barrera_monitorizacion", "P18"),
    ("variar_frecuencia_inspeccion_nivel_calidad", "P19"),
    ("simplificar_trabajo_reducir_numero_pasos", "P23"),
]

POBLACION = re.compile(r"poblacion del barrido\s*:\s*(\d+)\s*\((\d+) del grafo mas (\d+)")
VEREDICTO = re.compile(r"^\[(ENTRARIA|BLOQUEARIA|CAERIA)\]\s+(\S+)", re.M)
VECINO = re.compile(r"^\s+vecino (\S+)\s+\[levantada por: ([^\]]+)\]", re.M)
SENALES = re.compile(r"similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)")

filas = []
faltan = []
for identificador, pieza in ORDEN:
    ruta = os.path.join(".v2g", "informe_%s.txt" % identificador)
    if not os.path.exists(ruta) or os.path.getsize(ruta) == 0:
        faltan.append(identificador)
        continue
    texto = io.open(ruta, encoding="utf-8").read()
    pob = POBLACION.search(texto)
    ver = VEREDICTO.search(texto)
    if not pob or not ver:
        raise SystemExit("EL INFORME %s NO TRAE SU LINEA: %s"
                         % (ruta, "poblacion" if not pob else "veredicto"))
    if ver.group(2) != identificador:
        raise SystemExit("EL INFORME %s ES DE OTRO CANDIDATO: %s" % (ruta, ver.group(2)))
    vecinos = VECINO.findall(texto)
    senales = SENALES.findall(texto)
    detalle = "cola vacia"
    if vecinos:
        piezas = []
        for (nombre, senal), (s1, s2, s3) in zip(vecinos, senales):
            piezas.append("`%s` por `%s`, similitud %s, familia %s, paso contra nodo %s"
                          % (nombre, senal.strip(), s1.replace(".", ","),
                             s2.replace(".", ","), s3.replace(".", ",")))
        detalle = "; ".join(piezas)
    filas.append((identificador, pieza, ver.group(1), pob.group(1), pob.group(2),
                  pob.group(3), len(vecinos), detalle))

if faltan:
    print("NO SE PUBLICA LA TABLA: a estos candidatos les falta su informe de aduana,")
    print("y sin el un candidato NO ESTA ESCRITO (EXTRACTOR.md 16).")
    for identificador in faltan:
        print("  " + identificador)
    raise SystemExit(1)

print("| # | candidato | pieza de cap_03 | puerta | poblacion que midio SU informe | vecinos | la cola, nombrada |")
print("|---:|---|---|---|---|---:|---|")
for numero, fila in enumerate(filas, 1):
    identificador, pieza, puerta, total, grafo, bandejas, cuantos, detalle = fila
    print("| %d | `%s` | `%s` | **%s** | %s (%s del grafo mas %s en bandejas) | %d | %s |"
          % (numero, identificador, pieza, puerta, total, grafo, bandejas, cuantos, detalle))

entrarian = sum(1 for f in filas if f[2] == "ENTRARIA")
bloquearian = sum(1 for f in filas if f[2] == "BLOQUEARIA")
caerian = sum(1 for f in filas if f[2] == "CAERIA")
vecinos = sum(f[6] for f in filas)
print("| | **%d candidatos** | | **%d ENTRARIAN, %d BLOQUEARIAN, %d CAERIAN** | | **%d** | |"
      % (len(filas), entrarian, bloquearian, caerian, vecinos))
print("")
print("EL SALDO, RECONTADO DE LAS FILAS DE ARRIBA")
print("  candidatos escritos y pasados por la aduana en el acto : %d" % len(filas))
print("  ENTRARIAN                                             : %d" % entrarian)
print("  BLOQUEARIAN (cola de lectura, no rechazo)             : %d" % bloquearian)
print("  CAERIAN                                               : %d" % caerian)
print("  vecinos levantados en total                           : %d" % vecinos)
print("  INSERTADOS                                            : 0   (D.45, y la orden del fundador)")
print("")
print("LA POBLACION NO ES UNA SOLA Y POR ESO VA POR FILA: el primer informe midio %s y el"
      % filas[0][3])
print("ultimo %s, porque la bandeja crece segun se escriben los candidatos." % filas[-1][3])
print("ficheros en la bandeja del libro al cerrar esta tabla   : %d"
      % len(glob.glob("cuarentena/grove_high_output/*.json")))
