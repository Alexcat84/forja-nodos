# -*- coding: utf-8 -*-
"""LA RELECTURA DE FIDELIDAD `D.30` DE LOS CUATRO CANDIDATOS DE LA VUELTA 40.

`EXTRACTOR.md` 15.4. El instrumento hace DOS cosas y ninguna de las dos es juzgar:

  1. **pega la linea del libro entera**, con su `sed -n '<n>p'` al lado, que es
     `D.35`: la cita se pega, no se promete.
  2. **pone cada paso debajo de su linea**, en el reparto que el propio candidato
     declara en su `resumen_teorico`, y **comprueba que ese reparto cubre los
     pasos sin hueco ni solape**: si un paso no cae en ningun tramo, o cae en
     dos, salta aqui.

**EL VEREDICTO `TRANSCRIPCION` O `PUENTE` DE CADA PASO LO PONE LA LECTURA Y VA
TECLEADO EN LA TABLA DEL REPORTE**, no aqui. Ninguna guarda de esta casa ve un
paso que el extractor escribio y el libro no dice.

**LA UNICA COSA QUE EL INSTRUMENTO CAMBIA DE LA LINEA DEL LIBRO, Y LA CUENTA CADA
VEZ QUE LO HACE:** el guion largo y el guion medio se sustituyen por el token
literal entre corchetes. **No es cosmetica: el barrido de guiones de esta casa
tumba el commit si uno entra**, y cortar la cita para esquivarlo perderia
palabras del libro que sostienen pasos (`L197` cierra con `off the hook`, que es
lo que sostiene su `P12`, y `L237` nombra ahi mismo los cuatro elementos, que es
lo que sostiene el `P06` del cuarto candidato). **La sustitucion es mecanica, va
contada por linea al final, y no quita ni una palabra.**
"""
import io
import json
import os
import subprocess
import sys

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIBRO = os.path.join(RAIZ, "fuentes", "scott_radical_candor", "cap_13.md")

# LOS DOS GUIONES VAN ESCRITOS POR SU PUNTO DE CODIGO Y NO LITERALES, y es por lo
# mismo que existe el barrido: un guion largo dentro de este fichero tumbaria el
# commit del instrumento que lo caza.
LARGO = unichr(0x2014) if sys.version_info[0] == 2 else chr(0x2014)
MEDIO = unichr(0x2013) if sys.version_info[0] == 2 else chr(0x2013)

# EL REPARTO DE PASOS POR LINEA, copiado del resumen_teorico de cada candidato.
REPARTO = [
    ("abrazar_incomodidad_silencio_contar_seis", "L187", [
        (191, (1, 6)),
        (195, (7, 10)),
        (197, (11, 12)),
    ]),
    ("escuchar_entender_critica_dominar_defensa", "L199", [
        (203, (1, 2)),
        (205, (3, 4)),
        (209, (5, 8)),
        (211, (9, 12)),
        (213, (13, 13)),
    ]),
    ("premiar_franqueza_hacer_escucha_tangible", "L215", [
        (217, (1, 2)),
        (219, (3, 4)),
        (221, (5, 7)),
        (225, (8, 10)),
        (227, (11, 13)),
        (229, (14, 15)),
        (233, (16, 20)),
    ]),
    ("integrar_peticion_critica_rutina_existente", "L235", [
        (111, (1, 5)),
        (237, (6, 6)),
        (239, (7, 10)),
        (241, (11, 11)),
        (245, (12, 13)),
    ]),
]


def linea_del_libro(n):
    salida = subprocess.run(["sed", "-n", "%dp" % n, LIBRO], capture_output=True)
    crudo = salida.stdout.decode("utf-8").rstrip("\r\n")
    cuantos = crudo.count(LARGO) + crudo.count(MEDIO)
    limpio = crudo.replace(LARGO, "[U+2014]").replace(MEDIO, "[U+2013]")
    return limpio, cuantos


def cortar(t, n):
    t = " ".join(t.split())
    return t if len(t) <= n else t[:n - 3] + "..."


def main():
    total_pasos = 0
    total_lineas = 0
    problemas = []
    sustituidos = []

    for cid, rotulo, tramos in REPARTO:
        ruta = os.path.join(RAIZ, "cuarentena", "scott_radical_candor", "%s.json" % cid)
        with io.open(ruta, encoding="utf-8") as f:
            ficha = json.load(f)
        pasos = ficha["pasos_accionables"]
        cubiertos = []
        print("=" * 110)
        print("%s   rotulo %s   %d pasos" % (cid, rotulo, len(pasos)))
        print("=" * 110)
        for n, (desde, hasta) in tramos:
            total_lineas += 1
            texto, guiones = linea_del_libro(n)
            if guiones:
                sustituidos.append((n, guiones))
            print("")
            print("  $ sed -n '%dp' fuentes/scott_radical_candor/cap_13.md" % n)
            print("  %d: %s" % (n, cortar(texto, 1500)))
            if guiones:
                print("      (%d guion(es) largo(s) de esa linea sustituido(s) por su token)"
                      % guiones)
            print("  --- los pasos que salen de esa linea ---")
            for i in range(desde, hasta + 1):
                cubiertos.append(i)
                print("      P%02d  %s" % (i, cortar(pasos[i - 1], 1500)))
        total_pasos += len(pasos)
        faltan = [i for i in range(1, len(pasos) + 1) if i not in cubiertos]
        repes = sorted(set(i for i in cubiertos if cubiertos.count(i) > 1))
        print("")
        print("  COBERTURA: %d paso(s), %d cubierto(s), %d sin tramo, %d en dos tramos"
              % (len(pasos), len(set(cubiertos)), len(faltan), len(repes)))
        if faltan or repes:
            problemas.append((cid, faltan, repes))
        print("")

    print("=" * 110)
    print("EL TRAMO ENTERO: %d pasos de 4 candidatos, repartidos sobre %d lineas del libro"
          % (total_pasos, total_lineas))
    if problemas:
        print("HAY HUECO O SOLAPE, y eso se declara:")
        for cid, faltan, repes in problemas:
            print("  %s  sin tramo: %s  en dos tramos: %s" % (cid, faltan, repes))
    else:
        print("NI UN HUECO NI UN SOLAPE: los %d pasos caen cada uno en una sola linea."
              % total_pasos)
    print("GUIONES SUSTITUIDOS: %d en %d de las %d lineas citadas%s"
          % (sum(c for _n, c in sustituidos), len(sustituidos), total_lineas,
             (", " + ", ".join("L%d con %d" % (n, c) for n, c in sustituidos))
             if sustituidos else ""))


if __name__ == "__main__":
    main()
