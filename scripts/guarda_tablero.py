# -*- coding: utf-8 -*-
"""LA GUARDA DEL TABLERO: EL ARNES COMPRUEBA AL ABRIR VUELTA (D.49).

    python scripts/guarda_tablero.py            mide, comprueba, y devuelve 0 o 1

QUE HACE, EN TRES PASOS.

  1. **VUELVE A MEDIR EL TABLERO** y lo escribe (`docs/loop/TABLERO.jsonl`). Un tablero
     que se actualiza cuando alguien se acuerda es la frase escrita a mano que `D.49`
     vino a sustituir.
  2. **LEE QUE LIBRO DECLARA EL ENCARGO DE ESTA VUELTA**, en `PROMPT_SIGUIENTE.md`:

         LIBRO DE ESTA VUELTA: scott_radical_candor

  3. **LO PASA POR `D.49`** con la linea de este arbol. Si el libro tiene dueño y no es
     esta linea, **se detiene nombrando al dueño.**
  4. **Y LO PASA POR LA CADENCIA DE `D.58`:** si desde la ultima vuelta de saneamiento
     han pasado cinco, **la vuelta que abre ES de saneamiento y el encargo no puede
     decir otra cosa**.
  5. **Y LO PASA POR `D.51`:** el libro declarado tiene que ser **el que el orden del
     mundo 11 le toca a esta linea**, no otro. Si no lo es, se detiene **nombrando el
     que si**.

POR QUE EL ENCARGO TIENE QUE DECLARARLO, Y NO SE ADIVINA. El arnes no sabe que es un
libro (`D.45`), y buscar la clave suelta dentro del texto del encargo **es exactamente la
trampa que el tallado ya pago dos veces**: un encargo nombra a los tres frentes en su
seccion de *lo que no se toca*, y una guarda que lee menciones **tumbaria la vuelta por
decir que no los toca.** Asi que no se busca: **se exige declarado, en su propia linea.**

**Y SI NO LO DECLARA, EL ARNES SE DETIENE IGUAL.** Un encargo que no dice sobre que libro
trabaja no es un encargo que la guarda pueda mirar, y `D.49` dice que **toda linea lee el
tablero en su apertura y lo cita.** Para declarar que una vuelta no toca ningun libro
existe `NINGUNO`, y eso es una declaracion, no un silencio.
"""

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

from src import comun, credito, tablero  # noqa: E402

RUTA_ENCARGO = os.path.join(RAIZ, "docs", "loop", "PROMPT_SIGUIENTE.md")
RUTA_PARADA = os.path.join(RAIZ, "docs", "loop", "PARA_ALEXIS.md")

# LA VUELTA Y SU CLASE, LEIDAS DEL ENCARGO (D.58, 19 sep 2026).
#
# `D.55` mandaba una vuelta de saneamiento de cada cinco, **y la 49 debio serlo y no lo
# fue**: la cadencia dependia de que alguien se acordara al escribir el encargo, que es
# el genero de remedio que esta casa tiene medido que no funciona (`D.35`).
NUMERO_DE_VUELTA = re.compile(
    r"^[\s>*#`]*ENCARGO\s+DE\s+LA\s+VUELTA\s+(\d+)", re.M | re.I)
CLASE_DECLARADA = re.compile(
    r"^[\s>*#`]*CLASE\s+DE\s+ESTA\s+VUELTA\s*:?[\s*`]*([A-Za-z]+)", re.M | re.I)
CLASES = ("EXTRACCION", "INSERCION", "SANEAMIENTO")

# La declaracion, con la decoracion que esta casa escribe: negrita, cita, comillas.
DECLARACION = re.compile(
    r"^[\s>*#`]*LIBRO\s+DE\s+ESTA\s+VUELTA\s*:?[\s*`]*([A-Za-z0-9_]+)", re.M | re.I)

SIN_LIBRO = "NINGUNO"


def libro_declarado(texto=None):
    """La clave que el encargo declara, o `None` si no declara ninguna."""
    if texto is None:
        texto = comun.leer_texto(RUTA_ENCARGO) if os.path.exists(RUTA_ENCARGO) else ""
    encaje = DECLARACION.search(texto or "")
    return encaje.group(1) if encaje else None


def vuelta_y_clase(texto=None):
    """`(numero, clase)` que el encargo declara. `None` en lo que no declare."""
    if texto is None:
        texto = (comun.leer_texto(RUTA_ENCARGO)
                 if os.path.exists(RUTA_ENCARGO) else "")
    numero = NUMERO_DE_VUELTA.search(texto or "")
    clase = CLASE_DECLARADA.search(texto or "")
    declarada = clase.group(1).upper() if clase else None
    return (int(numero.group(1)) if numero else None,
            declarada if declarada in CLASES else None)


def cadencia(texto=None, linea=None):
    """LA CADENCIA LA HACE CUMPLIR EL CODIGO, NO LA MEMORIA (`D.58`).

    Si desde la ultima vuelta de saneamiento han pasado cinco, **la vuelta que abre ES
    de saneamiento y el encargo no puede decir otra cosa**. Devuelve la lista de
    motivos que lo impiden; vacia es verde.
    """
    from scripts import deuda
    numero, declarada = vuelta_y_clase(texto)
    if numero is None:
        return ["el encargo no dice de que vuelta es. D.58: la cadencia se cuenta por "
                "numero de vuelta, y sin el no se puede contar. Escribe su titulo como "
                "'ENCARGO DE LA VUELTA <n>'."]
    # LA CADENCIA ES DE UNA LINEA (d097, 22 sep 2026). Esta guarda ya sabe de
    # cual, y no pasarsela dejaba que la cuenta la decidiera el arbol donde
    # corre la prueba en vez del encargo que se esta comprobando.
    toca, motivo = deuda.clase_de_vuelta(numero, linea=linea)
    if toca != "SANEAMIENTO":
        return []
    if declarada == "SANEAMIENTO":
        return []
    return ["D.58: LA VUELTA %d ES DE SANEAMIENTO Y EL ENCARGO DICE %s. %s. La cadencia "
            "no la decide el encargo: la cuenta el registro, y la vuelta 49 debio ser "
            "de saneamiento y no lo fue porque dependia de que alguien se acordara."
            % (numero, declarada or "otra cosa", motivo)]


def hay_parada(ruta_parada=None):
    """Cierto si `docs/loop/PARA_ALEXIS.md` esta en el arbol: el bucle esta parado."""
    return os.path.exists(ruta_parada or RUTA_PARADA)


def comprobar(texto=None, linea=None, filas=None, ruta_parada=None):
    """Devuelve la lista de motivos que IMPIDEN abrir la vuelta. Vacia es verde."""
    linea = linea or credito.linea_actual()
    clave = libro_declarado(texto)

    if clave is None:
        # UN ENCARGO VACIO CON UNA PARADA AL LADO NO ES UN DESCUIDO: ES UNA PARADA.
        #
        # ESTE ES UN DEFECTO MIO, del 17 sep 2026, y lo cazo el auditor de la ACTA 34
        # en su punto 5: `AUDITOR_FORJA.md` 3 manda dejar el encargo VACIO al parar, y
        # `D.49` exige que el encargo declare su libro. **Las dos reglas piden lo mismo
        # en efecto** (que la vuelta siguiente no abra), pero mi guarda llamaba
        # "descuido" a lo que era **cumplimiento**, y con eso ponia en rojo la suite
        # entera cada vez que el bucle paraba bien.
        #
        # SIGUE SIENDO IMPEDIMENTO, que es la mitad que no se puede aflojar: la vuelta
        # NO abre. Lo que cambia es que ahora dice por que, y el motivo es el correcto.
        vacio = not (texto if texto is not None else
                     (comun.leer_texto(RUTA_ENCARGO)
                      if os.path.exists(RUTA_ENCARGO) else "")).strip()
        if vacio and hay_parada(ruta_parada):
            return ["EL BUCLE ESTA PARADO: %s esta vacio y %s esta en el arbol, que es "
                    "lo que AUDITOR_FORJA.md 3 manda al parar. No es un encargo sin "
                    "libro: es una parada sin resolver. Lee la parada."
                    % (comun.relativa(RUTA_ENCARGO), comun.relativa(RUTA_PARADA))]
        return ["el encargo de esta vuelta NO DECLARA su libro. D.49: toda linea lee el "
                "tablero en su apertura y lo cita. Escribe en %s una linea "
                "'LIBRO DE ESTA VUELTA: <clave>', o 'LIBRO DE ESTA VUELTA: NINGUNO' si "
                "la vuelta no toca ningun libro." % comun.relativa(RUTA_ENCARGO)]

    if clave.upper() == SIN_LIBRO:
        return []

    impiden = []

    vale, motivo = tablero.puede_abrir(clave, linea, filas)
    if not vale:
        impiden.append(
            "D.49: el encargo declara el libro '%s' y esta linea ('%s') NO puede "
            "tomarlo. %s" % (clave, linea, motivo))

    # D.51: NINGUNA LINEA ELIGE LIBRO. Se comprueba aunque D.49 ya haya caido, porque
    # las dos cosas que el encargo puede tener mal son distintas: D.49 dice que ese
    # libro no es tuyo, y D.51 dice cual es.
    impiden.extend(cadencia(texto, linea=linea))

    toca, porque, relevo = tablero.siguiente_por_prioridad(linea, filas)
    if toca is None:
        impiden.append("D.51: a esta linea no le toca NINGUN libro ahora mismo. %s"
                       % porque)
    elif toca != clave:
        aviso = ("D.51: el encargo declara '%s' y el orden del mundo 11 le da a esta "
                 "linea '%s'. %s" % (clave, toca, porque))
        if relevo is not None:
            aviso += (" El relevo pendiente es la rama '%s'." % relevo.get("rama"))
        impiden.append(aviso)
    return impiden


def main(argumentos=()):
    comun.salida_utf8()
    linea = credito.linea_actual()

    # SIN OBJETO, Y SE DICE EN VOZ ALTA. Un arbol sin `ORDEN_DE_LOTES.md` no tiene
    # campania que coordinar: no hay libros, no hay lineas y no hay nada que D.49 o
    # D.51 puedan decidir. **Una guarda que no puede medir no inventa un veredicto**,
    # igual que el tallado dice TALLADO SIN OBJETO cuando no hay documento.
    #
    # Y NO ES UN AGUJERO: el banco de pruebas del arnes corre asi a proposito, y hay
    # una prueba que exige que el repo de verdad SI tenga su tablero con una fila por
    # lote. Que esto pase en silencio ahi seria el agujero.
    if not os.path.exists(tablero.RUTA_ORDEN):
        print("GUARDA DEL TABLERO SIN OBJETO: no hay %s en este arbol, asi que no hay "
              "campania que coordinar (D.49, D.51)."
              % comun.relativa(tablero.RUTA_ORDEN))
        return 0

    try:
        filas = tablero.escribir()
    except tablero.TableroMalDeclarado as roto:
        print("GUARDA DEL TABLERO EN ROJO: %s" % roto)
        return 1

    clave = libro_declarado()
    print("GUARDA DEL TABLERO (D.49)")
    print("  linea de este arbol : %s" % linea)
    print("  libro que declara el encargo : %s" % (clave or "(NINGUNO DECLARADO)"))
    toca, porque, _ = tablero.siguiente_por_prioridad(linea, filas)
    print("  libro que el orden le da (D.51): %s" % (toca or "NINGUNO"))
    print("    %s" % porque[:150])
    con_dueno = [f for f in tablero.libros(filas)
                 if f["dueno"] != tablero.NINGUNO]
    for fila in con_dueno:
        print("  con dueño: %-30s %-22s lo trabaja '%s'"
              % (fila["clave"], fila["estado"], fila["dueno"]))

    impiden = comprobar(linea=linea, filas=filas)
    if not impiden:
        print("")
        print("TABLERO VERDE: la vuelta puede abrir.")
        return 0
    print("")
    print("TABLERO EN ROJO. La vuelta NO abre:")
    for motivo in impiden:
        print("  %s" % motivo)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
