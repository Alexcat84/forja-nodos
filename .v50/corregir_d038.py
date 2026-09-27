# -*- coding: utf-8 -*-
"""d038 PAGADA: LA LINEA DEL METODO DENTRO DE LA FICHA DE P38, CORREGIDA SIN BORRAR.

La ficha cita dentro de si misma grep -l "PIEZA P34" como prueba de que P34 es madre de dos
fichas, y ese comando devuelve hoy TRES porque la propia ficha pasa a contener la cadena.
El preciso, grep -l "Sale de la PIEZA P34", sigue dando dos.

LA AFIRMACION ES CIERTA Y NO SE TOCA: lo defectuoso es la linea del metodo. Manual principio
6: el texto viejo queda en pie y la correccion se escribe al lado.

CERO PASADAS DE ADUANA POR ADJUDICACION DEL AUDITOR (encargo de la vuelta 50, TAREA 3.c).
"""
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

RUTA = "cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json"

# EL RENGLON DEL INSTRUMENTO SE LEE DE SU FICHERO, no se teclea aqui.
salida = io.open(".v50/d038_grep.txt", encoding="utf-8").read().split("\n")
anchas = [l for l in salida if l.startswith("  fichas:")]
if len(anchas) != 2:
    raise SystemExit("PARADA: .v50/d038_grep.txt no trae las dos cuentas")
cuenta_ancha = int(anchas[0].split(":")[1])
cuenta_precisa = int(anchas[1].split(":")[1])
if (cuenta_ancha, cuenta_precisa) != (3, 2):
    raise SystemExit("PARADA: las cuentas de hoy son %d y %d, no 3 y 2"
                     % (cuenta_ancha, cuenta_precisa))

CORRECCION = (
 " CORRECCION DECLARADA DE LA VUELTA 50, SIN BORRAR LA LINEA VIEJA (manual principio 6, deuda d038, "
 "adjudicada en ACTA 48 seccion 48.4 fila 2 y declarada por mi mismo en REPORTE.md KK.2.e): donde esta "
 "ficha dice mas arriba comprobado hoy con grep -l 'PIEZA P34' sobre la bandeja, TIENE QUE LEERSE "
 "comprobado con grep -l 'Sale de la PIEZA P34' sobre la bandeja. EL MOTIVO, y es de mecanica y no de "
 "sustancia: desde que esta ficha escribio esa linea, la propia ficha contiene la cadena PIEZA P34, asi "
 "que el comando ancho devuelve TRES ficheros y uno de los tres es ella misma. El comando preciso sigue "
 "devolviendo DOS, que son las dos fichas que de verdad salen de P34. LA AFIRMACION QUE LA LINEA SOSTIENE "
 "ES CIERTA Y NO CAMBIA: P34 es madre de decir_no_trabajo_excede_capacidad y de "
 "usar_calendario_herramienta_planificacion_produccion. LOS DOS RENGLONES DEL INSTRUMENTO, pegados "
 "(.v50/d038_grep.txt): grep -l 'PIEZA P34' da 3 fichas (decir_no_trabajo_excede_capacidad, "
 "dimensionar_numero_subordinados_medio_dia_semanal, usar_calendario_herramienta_planificacion_produccion); "
 "grep -l 'Sale de la PIEZA P34' da 2 fichas (decir_no_trabajo_excede_capacidad, "
 "usar_calendario_herramienta_planificacion_produccion). Y LA LECCION, que es la que vale mas que la "
 "linea: una cita de metodo escrita DENTRO del objeto que mide deja de reproducirse en cuanto el objeto "
 "entra en la poblacion que el metodo barre."
)

ficha = json.load(io.open(RUTA, encoding="utf-8"))
if "deuda d038" in ficha["resumen_teorico"]:
    print("YA CORREGIDA, no la toco")
else:
    ficha["resumen_teorico"] = ficha["resumen_teorico"] + CORRECCION
    with io.open(RUTA, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(ficha, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("corregida %s" % RUTA)
print("cuenta ancha medida hoy: %d ; cuenta precisa medida hoy: %d"
      % (cuenta_ancha, cuenta_precisa))
